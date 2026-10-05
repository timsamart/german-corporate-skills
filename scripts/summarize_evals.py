"""Recount saved semantic grades; never runs a model or estimates missing metrics."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


def words(text: str) -> int:
    """Count whitespace-separated items containing a letter/number, not Markdown marks."""
    return sum(bool(re.search(r"\w", token)) for token in text.split())


def verify_evidence_hashes(directory: Path) -> None:
    """Check retained bytes, including those that Git might otherwise normalize."""
    repo = Path(__file__).resolve().parents[1]
    freeze = json.loads((directory / "freeze.json").read_text(encoding="utf-8"))

    def check(path: Path, expected: str) -> None:
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected, f"{path}: frozen hash mismatch"

    for relative, digest in freeze["candidate_files"].items():
        check(repo / relative, digest)
    for relative, digest in freeze["fixture_files"].items():
        check(repo / "evals/fixtures" / relative, digest)
    amendment = json.loads((directory / "assertion-amendment.json").read_text(encoding="utf-8"))
    assert freeze["tasks_sha256"] == amendment["original_tasks_sha256"]
    check(directory / "tasks-before-amendment.json", amendment["original_tasks_sha256"])
    check(repo / "evals/tasks.json", amendment["amended_tasks_sha256"])
    source = directory / "transfer/source"
    transfer = json.loads((source / "freeze.json").read_text(encoding="utf-8"))
    for item in transfer["files"]:
        check(source / item["path"], item["sha256"])


def summarize(directory: Path) -> dict:
    verify_evidence_hashes(directory)
    records = []
    for split, configs in [("development", ["new_skill", "old_skill", "without_corporate"]),
                           ("transfer", ["new_skill"])]:
        for case in sorted((directory / split).glob("eval-*")):
            meta = json.loads((case / "eval_metadata.json").read_text(encoding="utf-8"))
            expected = {a["text"]: a for a in meta["assertions"]}
            for config in configs:
                run = case / config
                grade = json.loads((run / "grading.json").read_text(encoding="utf-8"))
                actual = grade["expectations"]
                assert len(actual) == len(expected), f"{run}: criterion count mismatch"
                assert {a["text"] for a in actual} == set(expected), f"{run}: criterion mismatch"
                assert all(isinstance(a["passed"], bool) and a.get("evidence") for a in actual), run
                passed = sum(a["passed"] for a in actual)
                total = len(actual)
                summary = grade["summary"]
                assert (summary["passed"], summary["failed"], summary["total"]) == (
                    passed, total - passed, total), f"{run}: grade arithmetic mismatch"
                assert abs(summary["pass_rate"] - passed / total) < 0.011, run
                critical = [a for a in actual if expected[a["text"]]["critical"]]
                output = (run / "outputs/output.md").read_text(encoding="utf-8")
                records.append({
                    "split": split, "case": case.name, "skill": meta["skill"],
                    "configuration": config, "passed": passed, "total": total,
                    "critical_passed": sum(a["passed"] for a in critical),
                    "critical_total": len(critical),
                    "critical_gate": all(a["passed"] for a in critical),
                    "all_criteria": passed == total, "words": words(output),
                    "failures": [a for a in actual if not a["passed"]],
                })
    assert len(records) == 28, f"Expected 21 development and 7 transfer outputs, got {len(records)}"
    totals = {}
    for split, config in sorted({(r["split"], r["configuration"]) for r in records}):
        subset = [r for r in records if r["split"] == split and r["configuration"] == config]
        totals[f"{split}/{config}"] = {
            "cases": len(subset), "all_criteria_cases": sum(r["all_criteria"] for r in subset),
            "critical_gate_cases": sum(r["critical_gate"] for r in subset),
            "criteria_passed": sum(r["passed"] for r in subset),
            "criteria_total": sum(r["total"] for r in subset),
            "critical_passed": sum(r["critical_passed"] for r in subset),
            "critical_total": sum(r["critical_total"] for r in subset),
        }
    return {"kind": "Descriptive recount of saved model grades; not population accuracy.",
            "critical_gate_definition": "All premarked required critical criteria met. Omissions can fail this gate; it does not count factual errors.",
            "unknown_metrics": ["exact_model_id", "sampling_settings", "tokens", "full_tool_traces", "runtime"],
            "totals": totals, "runs": records}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()
    result = summarize(args.directory)
    target = args.directory / "summary.json"
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["totals"], ensure_ascii=False, indent=2))
