"""Build deterministic source ZIPs for manual skill installation; no host mutation."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def archive(path: Path, entries: dict[str, bytes]) -> dict:
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as output:
        for name, data in sorted(entries.items()):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            output.writestr(info, data)
    with zipfile.ZipFile(path) as output:
        assert output.testzip() is None
        assert set(output.namelist()) == set(entries)
        for name, expected in entries.items():
            assert output.read(name) == expected, name
    return {"file": path.name, "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "files": {name: hashlib.sha256(data).hexdigest() for name, data in sorted(entries.items())}}


def build(destination: Path) -> dict:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    assert re.fullmatch(r"\d+\.\d+\.\d+", version), "Invalid version"
    destination.mkdir(parents=True, exist_ok=True)
    records = []
    all_skills = {}
    for folder in sorted((ROOT / "skills").iterdir()):
        if not folder.is_dir():
            continue
        entries = {f"{folder.name}/{p.relative_to(folder).as_posix()}": p.read_bytes()
                   for p in folder.rglob("*") if p.is_file() and "__pycache__" not in p.parts}
        assert f"{folder.name}/SKILL.md" in entries
        all_skills.update(entries)
        entries["LICENSE"] = (ROOT / "LICENSE").read_bytes()
        records.append(archive(destination / f"{folder.name}-v{version}.zip", entries))
    all_skills["LICENSE"] = (ROOT / "LICENSE").read_bytes()
    all_skills["INSTALL.txt"] = ("German Corporate Skills " + version + "\n\n"
        "Copy each desired complete skill folder to your agent's project skill directory.\n"
        "For Codex: .agents/skills/; for Claude Code: .claude/skills/.\n"
        "These ZIPs contain instructions and references; they do not run an installer.\n"
        "Provide suitable document-reading/rendering tools for deck reviews.\n"
        "Repository and detailed instructions: https://github.com/timsamart/german-corporate-skills\n").encode()
    records.append(archive(destination / f"german-corporate-skills-v{version}.zip", all_skills))
    manifest = {"version": version, "kind": "Deterministic skill-source ZIPs, verified by byte comparison",
                "artifacts": records}
    (destination / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    result = build(args.output_dir)
    print(f"PASS: {len(result['artifacts'])} ZIPs built; archived bytes match their source files.")
