"""Verify v0.3 frozen evidence and recount saved grades; does not execute models."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: Path) -> dict | list:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def check_hash(path: Path, expected: str) -> None:
    assert hashlib.sha256(path.read_bytes()).hexdigest() == expected, f"Frozen hash mismatch: {path}"


def summarize(directory: Path) -> dict:
    freeze = read(directory / "freeze.json")
    for role in ("candidate", "baseline"):
        for relative, digest in freeze[f"{role}_files"].items():
            check_hash(directory / role / relative, digest)
            if role == "candidate":
                check_hash(ROOT / relative, digest)
    for relative, digest in freeze["development_files"].items():
        check_hash(ROOT / relative, digest)
    source = directory / "transfer/source"
    check_hash(source / "freeze.json", freeze["reserved_set_freeze_sha256"])
    for item in read(source / "freeze.json")["files"]:
        check_hash(source / item["path"], item["sha256"])
    original_tasks = {
        "development": {t["id"]: t for t in read(ROOT / "evals/v0.3.0/tasks.json")},
        "transfer": {t["id"]: t for t in read(source / "manifest.json")["cases"]},
    }
    records = []
    for split, configs in (("development", ("new_skill", "old_skill", "without_corporate")),
                           ("transfer", ("new_skill",))):
        seen = set()
        for case in sorted((directory / split).glob("eval-*")):
            meta = read(case / "eval_metadata.json")
            assert meta["id"] not in seen, f"Duplicate task: {case}"
            seen.add(meta["id"])
            original = original_tasks[split][meta["id"]]
            for key in ("skill", "prompt", "input", "assertions"):
                assert meta[key] == original[key], f"Task metadata differs from frozen source: {case}/{key}"
            expected = {a["text"]: a for a in meta["assertions"]}
            assert len(expected) == len(meta["assertions"]), f"Duplicate criterion: {case}"
            for config in configs:
                run = case / config
                grade = read(run / "grading.json")
                actual = grade["expectations"]
                assert len(actual) == len(expected) and {a["text"] for a in actual} == set(expected), run
                assert all(isinstance(a["passed"], bool) and a.get("evidence") for a in actual), run
                passed = sum(a["passed"] for a in actual)
                summary = grade["summary"]
                assert (summary["passed"], summary["failed"], summary["total"]) == (passed, len(actual)-passed, len(actual)), run
                assert abs(summary["pass_rate"] - passed / len(actual)) < 0.011, run
                output = (run / "outputs/output.md").read_text(encoding="utf-8-sig")
                words = sum(bool(re.search(r"\w", token)) for token in output.split())
                critical = [a for a in actual if expected[a["text"]]["critical"]]
                records.append({"split": split, "case": case.name, "skill": meta["skill"],
                    "configuration": config, "criteria_passed": passed, "criteria_total": len(actual),
                    "critical_passed": sum(a["passed"] for a in critical), "critical_total": len(critical),
                    "all_criteria": passed == len(actual), "critical_gate": all(a["passed"] for a in critical),
                    "words": words, "word_limit": meta["word_limit"], "within_word_limit": words <= meta["word_limit"],
                    "failures": [a for a in actual if not a["passed"]]})
        assert seen == set(original_tasks[split]), f"Missing or extra {split} tasks"
    assert len(records) == 35, f"Expected 21 comparison and 14 transfer outputs, found {len(records)}"
    totals = {}
    for split, config in sorted({(r["split"], r["configuration"]) for r in records}):
        subset = [r for r in records if (r["split"], r["configuration"]) == (split, config)]
        totals[f"{split}/{config}"] = {"cases": len(subset),
            "all_criteria_cases": sum(r["all_criteria"] for r in subset),
            "critical_gate_cases": sum(r["critical_gate"] for r in subset),
            "within_word_limit": sum(r["within_word_limit"] for r in subset),
            **{key: sum(r[key] for r in subset) for key in ("criteria_passed", "criteria_total", "critical_passed", "critical_total")}}
    return {"kind": "Descriptive recount of saved model grades, not population accuracy or human usefulness.",
            "critical_gate_definition": "All marked required criteria met; omissions can fail a gate and are not automatically factual errors.",
            "unknown_metrics": freeze["unknown_metrics"], "totals": totals, "runs": records}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()
    result = summarize(args.directory)
    (args.directory / "summary.json").write_bytes((json.dumps(result, ensure_ascii=False, indent=2)+"\n").encode())
    print(json.dumps(result["totals"], ensure_ascii=False, indent=2))
