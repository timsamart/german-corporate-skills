"""Validate packaging and local references; does not run behavioral model evals."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]\n]+\]\(([^)\n]+)\)")
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    skills: dict[str, Path] = {}

    def fail(path: Path, message: str) -> None:
        errors.append(f"{path.relative_to(root)}: {message}")

    for folder in sorted((root / "skills").iterdir()):
        if not folder.is_dir():
            continue
        manifest = folder / "SKILL.md"
        if not manifest.is_file():
            fail(folder, "missing SKILL.md")
            continue
        text = manifest.read_text(encoding="utf-8")
        parts = text.split("---", 2)
        if len(parts) != 3 or parts[0].strip():
            fail(manifest, "missing YAML frontmatter")
            continue
        try:
            meta = yaml.safe_load(parts[1])
        except yaml.YAMLError as exc:
            fail(manifest, f"invalid YAML: {exc}")
            continue
        if not isinstance(meta, dict):
            fail(manifest, "frontmatter must be a mapping")
            continue
        name = meta.get("name")
        if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) > 64:
            fail(manifest, "invalid skill name")
            continue
        if name != folder.name:
            fail(manifest, "name does not match directory")
        if name in skills:
            fail(manifest, "duplicate skill name")
        skills[name] = folder
        description = meta.get("description")
        if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
            fail(manifest, "description must contain 1-1024 characters")
        if meta.get("license") != "MIT":
            fail(manifest, "license must match repository MIT license")
        if not parts[2].strip():
            fail(manifest, "empty instructions")
        if re.search(r"\bTODO\b|\[INSERT[^\]]*\]|\[TODO[^\]]*\]", text):
            fail(manifest, "unfinished scaffold marker")
        example = folder / "references" / "beispiel.md"
        if not example.is_file():
            fail(folder, "missing worked example")

    if not skills:
        errors.append("No skills found")

    markdown = [path for path in root.rglob("*.md")
                if ".git" not in path.parts and "runs" not in path.parts]
    for path in markdown:
        for target in LINK.findall(path.read_text(encoding="utf-8")):
            target = target.strip().strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            if not resolved.is_relative_to(root):
                fail(path, f"local link escapes repository: {target}")
            elif not resolved.exists():
                fail(path, f"broken local link: {target}")
            if path.name == "SKILL.md" and not resolved.is_relative_to(path.parent):
                fail(path, f"skill depends on a file outside its own folder: {target}")

    cases_path = root / "evals" / "cases.json"
    try:
        cases = json.loads(cases_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(cases_path, f"cannot load cases: {exc}")
        return errors
    if not isinstance(cases, list) or not cases:
        fail(cases_path, "cases must be a nonempty list")
        return errors
    ids: set[str] = set()
    covered: set[str] = set()
    for case in cases:
        if not isinstance(case, dict):
            fail(cases_path, "each case must be an object")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id or case_id in ids:
            fail(cases_path, f"invalid or duplicate case ID: {case_id!r}")
        else:
            ids.add(case_id)
        skill = case.get("skill")
        if not isinstance(skill, str) or skill not in skills:
            fail(cases_path, f"{case_id}: unknown skill {skill!r}")
        else:
            covered.add(skill)
        if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
            fail(cases_path, f"{case_id}: empty prompt")
        for field in ("must", "must_not"):
            values = case.get(field)
            if not isinstance(values, list) or not values or any(
                    not isinstance(item, str) or not item.strip() for item in values):
                fail(cases_path, f"{case_id}: {field} must be a nonempty string list")
    for skill in skills.keys() - covered:
        fail(cases_path, f"no behavioral cases for {skill}")
    return errors


if __name__ == "__main__":
    issues = validate(ROOT)
    if issues:
        print("\n".join(issues), file=sys.stderr)
        raise SystemExit(1)
    count = len(list((ROOT / "skills").glob("*/SKILL.md")))
    cases_count = len(json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8")))
    print(f"PASS: {count} skills, local references, and {cases_count} evaluation cases validated.")
    print("Behavioral model evaluations are not executed by this check.")
