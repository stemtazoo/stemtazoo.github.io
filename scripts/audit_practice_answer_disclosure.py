#!/usr/bin/env python3
"""Report exposed practice-question answers across FE/GK/DS/SG Markdown.

This is a conservative review aid, not a complete semantic classifier.
Run: python scripts/audit_practice_answer_disclosure.py
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GROUPS = ("fe", "gk", "ds", "sg")
ANSWER = re.compile(r"(?:^|\s)(?:\*\*)?(?:正解|正答|解答)[：:]\s*[ア-エA-Da-d0-9①-⑩]|^\s*[-*]?\s*正解方向[：:]")
QUESTION = re.compile(r"(?:確認問題|練習問題|演習問題|例題|ひっかけ|問題\d+|問題例|次のうち|どれか[。？?]?|どれでしょう)")
HEADING = re.compile(r"^#{1,6}\s+")
OPEN_DETAILS = re.compile(r"<details\b", re.I)
CLOSE_DETAILS = re.compile(r"</details\s*>", re.I)
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")


def audit(source: str):
    """Return high-confidence exposed answers and broader review candidates."""
    output = []
    details_depth = 0
    in_fence = False
    fence_char = ""
    section_is_question = False
    recent_question = -1000
    for line_no, line in enumerate(source.splitlines(), 1):
        fence = FENCE.match(line)
        if fence:
            marker = fence.group(1)
            if not in_fence:
                in_fence, fence_char = True, marker[0]
            elif marker[0] == fence_char:
                in_fence = False
            continue
        if in_fence:
            continue
        if HEADING.match(line):
            section_is_question = bool(QUESTION.search(line))
            recent_question = line_no if section_is_question else -1000
        elif QUESTION.search(line) and not line.strip().startswith(("<!--", ">", "{%")):
            recent_question = line_no
        # A closing tag on its own line ends the protected block.
        if CLOSE_DETAILS.search(line):
            details_depth = max(0, details_depth - len(CLOSE_DETAILS.findall(line)))
        if ANSWER.search(line) and details_depth == 0:
            near_question = section_is_question or line_no - recent_question <= 25
            output.append({
                "line": line_no,
                "level": "exposed_practice_answer" if near_question else "review_answer_context",
                "text": line.strip()[:170],
            })
        if OPEN_DETAILS.search(line):
            details_depth += len(OPEN_DETAILS.findall(line))
    return output


def scan(root=ROOT):
    results = []
    totals = {}
    for group in GROUPS:
        files = sorted((root / "pages" / group).rglob("*.md"))
        totals[group] = len(files)
        for path in files:
            hits = audit(path.read_text(encoding="utf-8"))
            if hits:
                results.append({"path": str(path.relative_to(root)), "findings": hits})
    return {"total_articles": sum(totals.values()), "by_group": totals, "files_with_findings": len(results),
            "findings": results}


def main():
    result = scan()
    path = ROOT / "artifacts" / "practice-answer-disclosure-audit.json"
    path.parent.mkdir(exist_ok=True, parents=True)
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    summary = {}
    for item in result["findings"]:
        for finding in item["findings"]:
            key = finding["level"]
            summary[key] = summary.get(key, 0) + 1
    print(f"Scanned {result['total_articles']} articles ({result['by_group']}).")
    print(f"Potentially affected articles: {result['files_with_findings']}; finding counts: {summary}")
    print(f"Review report: {path.relative_to(ROOT)}")
    # Reporting mode: do not break unrelated content changes before triage.


if __name__ == "__main__":
    main()
