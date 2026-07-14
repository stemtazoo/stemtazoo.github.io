#!/usr/bin/env python3
"""Create a conservative audit report for agent-facing content quality."""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from agent_resource_lib import ROOT, SECTIONS, classify_page, discover_pages, sort_key, write_json


ARTIFACTS_DIR = ROOT / "artifacts"
REPORT_MD = ARTIFACTS_DIR / "agent-content-audit.md"
REPORT_JSON = ARTIFACTS_DIR / "agent-content-audit.json"
OPENING_HEADINGS = ("## まず結論", "## まず結論：", "## まず結論・")
BOILERPLATE_PATTERNS = (
    "基本から",
    "わかりやすく解説",
    "この記事では",
    "試験対策として重要なポイント",
)


def main() -> int:
    pages, parse_errors = discover_pages()
    findings: list[dict] = []
    for page in pages:
        classify_page(page)

    by_section = {section: [p for p in pages if p.section == section] for section in SECTIONS}
    included = [p for p in pages if not p.excluded]
    excluded = [p for p in pages if p.excluded]
    included, duplicate_excluded = exclude_duplicate_outputs(included)
    excluded.extend(duplicate_excluded)

    add_parse_errors(findings, parse_errors)
    add_metadata_findings(findings, pages)
    add_opening_findings(findings, pages)
    add_overlap_findings(findings, pages)
    add_status_findings(findings, pages)
    add_related_role_findings(findings, pages)

    summary = build_summary(findings, by_section, included, excluded)
    report = render_markdown(summary, findings, by_section, excluded)

    ARTIFACTS_DIR.mkdir(exist_ok=True)
    REPORT_MD.write_text(report, encoding="utf-8")
    write_json(REPORT_JSON, {"summary": summary, "findings": findings})
    print(f"Wrote {REPORT_MD.relative_to(ROOT)}")
    print(f"Wrote {REPORT_JSON.relative_to(ROOT)}")
    return 0


def add_finding(findings, section, category, severity, source_path, title, message):
    findings.append(
        {
            "section": section,
            "category": category,
            "severity": severity,
            "source_path": source_path,
            "title": title,
            "message": message,
        }
    )


def add_parse_errors(findings, parse_errors):
    for item in parse_errors:
        add_finding(
            findings,
            item.get("section", "unknown"),
            "metadata",
            "high",
            item.get("source_path", ""),
            "",
            f"Malformed front matter: {item.get('error')}",
        )


def add_metadata_findings(findings, pages):
    permalinks = defaultdict(list)
    descriptions = defaultdict(list)
    for page in pages:
        permalinks[page.permalink].append(page)
        if page.description:
            descriptions[page.description].append(page)
        if not page.title:
            add_finding(findings, page.section, "metadata", "high", page.rel_source, "", "Missing title.")
        if not page.permalink:
            add_finding(findings, page.section, "metadata", "high", page.rel_source, page.title, "Missing permalink.")
        if not page.description:
            add_finding(findings, page.section, "metadata", "medium", page.rel_source, page.title, "Missing description.")
        elif len(page.description) < 40:
            add_finding(findings, page.section, "metadata", "low", page.rel_source, page.title, "Description is very short.")
        elif any(pattern in page.description for pattern in BOILERPLATE_PATTERNS):
            add_finding(findings, page.section, "metadata", "low", page.rel_source, page.title, "Description may contain boilerplate wording.")
        if not page.front_matter.get("last_modified_at") and not page.excluded:
            add_finding(findings, page.section, "metadata", "low", page.rel_source, page.title, "Missing last_modified_at.")
        if page.permalink and not page.permalink.startswith(f"/{page.section}/"):
            add_finding(findings, page.section, "metadata", "medium", page.rel_source, page.title, "Section/path and permalink appear inconsistent.")

    for permalink, group in permalinks.items():
        if permalink and len(group) > 1:
            for page in group:
                add_finding(findings, page.section, "metadata", "high", page.rel_source, page.title, f"Duplicate permalink: {permalink}")
    for description, group in descriptions.items():
        if len(group) > 1:
            for page in group[:10]:
                add_finding(findings, page.section, "metadata", "medium", page.rel_source, page.title, "Exact duplicate description.")


def add_opening_findings(findings, pages):
    for page in pages:
        if page.excluded:
            continue
        body = page.body
        has_opening = any(heading in body for heading in OPENING_HEADINGS)
        if not has_opening:
            add_finding(findings, page.section, "opening conclusion", "low", page.rel_source, page.title, "Opening conclusion heading was not detected.")
            continue
        title_term = main_title_term(page.title)
        opening = extract_opening_section(body)
        if title_term and title_term not in opening[:400]:
            add_finding(findings, page.section, "opening conclusion", "low", page.rel_source, page.title, "Title term was not found near the opening conclusion.")
        if len(opening.strip()) < 80:
            add_finding(findings, page.section, "opening conclusion", "low", page.rel_source, page.title, "Opening conclusion appears very short.")
        if re.match(r"^\s*(これ|それ|この|前述|上記)", opening):
            add_finding(findings, page.section, "opening conclusion", "low", page.rel_source, page.title, "Opening conclusion may start with a vague reference.")


def add_overlap_findings(findings, pages):
    title_groups = defaultdict(list)
    stem_groups = defaultdict(list)
    for page in pages:
        if page.excluded or not page.title:
            continue
        title_groups[normalize_topic(page.title)].append(page)
        stem_groups[topic_from_path(page.source_path)].append(page)

    for group in list(title_groups.values()) + list(stem_groups.values()):
        if len(group) < 2:
            continue
        sections = sorted({page.section for page in group})
        message = "Likely overlapping article title/topic."
        if len(sections) > 1:
            message = f"Cross-section topic overlap; confirm role separation across {', '.join(sections)}."
        for page in group[:8]:
            add_finding(findings, page.section, "title and topic consistency", "low", page.rel_source, page.title, message)


def add_status_findings(findings, pages):
    permalink_map = {page.permalink: page for page in pages if page.permalink}
    for page in pages:
        status = str(page.front_matter.get("content_status", "current")).strip().lower() or "current"
        if status in {"superseded", "deprecated"}:
            add_finding(findings, page.section, "content status", "medium", page.rel_source, page.title, f"Page marked {status}.")
        if status == "superseded":
            target = str(page.front_matter.get("superseded_by", "")).strip()
            if not target:
                add_finding(findings, page.section, "content status", "high", page.rel_source, page.title, "Superseded page is missing superseded_by.")
            elif target not in permalink_map:
                add_finding(findings, page.section, "content status", "medium", page.rel_source, page.title, f"superseded_by target not found: {target}")


def add_related_role_findings(findings, pages):
    comparison_words = ("違い", "比較", "vs", "VS", "まとめ", "チートシート")
    for page in pages:
        if page.excluded:
            continue
        text = f"{page.title}\n{page.body[:1200]}"
        if any(word in text for word in comparison_words):
            add_finding(
                findings,
                page.section,
                "related article roles",
                "low",
                page.rel_source,
                page.title,
                "May benefit from role-based related links that distinguish comparison, summary, and individual concept pages.",
            )


def build_summary(findings, by_section, included, excluded):
    counts_by_section = {}
    for section, pages in by_section.items():
        section_included = [p for p in included if p.section == section]
        section_excluded = [p for p in excluded if p.section == section]
        reason_counts = Counter(p.exclusion_reason for p in section_excluded)
        counts_by_section[section] = {
            "source_pages": len(pages),
            "included": len(section_included),
            "excluded": len(section_excluded),
            "excluded_by_reason": dict(reason_counts),
            "fallback_descriptions": sum(1 for p in section_included if not p.description),
        }
    return {
        "total_source_pages": sum(len(pages) for pages in by_section.values()),
        "included": len(included),
        "excluded": len(excluded),
        "counts_by_section": counts_by_section,
        "counts_by_category": dict(Counter(item["category"] for item in findings)),
        "counts_by_section_and_category": {
            section: dict(Counter(item["category"] for item in findings if item["section"] == section))
            for section in SECTIONS
        },
    }


def render_markdown(summary, findings, by_section, excluded):
    lines = [
        "# Agent Content Audit",
        "",
        "This report is generated by `scripts/audit_agent_content.py`. It records content-quality signals for later editorial work and does not rewrite source articles.",
        "",
        "## Executive summary",
        "",
        f"- Source pages inspected: {summary['total_source_pages']}",
        f"- Generated-resource eligible pages: {summary['included']}",
        f"- Excluded pages: {summary['excluded']}",
        f"- Findings recorded: {len(findings)}",
        "",
        "## Counts by section",
        "",
        "| Section | Source pages | Included | Excluded | Fallback descriptions |",
        "|---|---:|---:|---:|---:|",
    ]
    for section in SECTIONS:
        item = summary["counts_by_section"][section]
        lines.append(f"| {section} | {item['source_pages']} | {item['included']} | {item['excluded']} | {item['fallback_descriptions']} |")

    lines.extend(["", "## Counts by finding category", "", "| Category | Count |", "|---|---:|"])
    for category, count in sorted(summary["counts_by_category"].items()):
        lines.append(f"| {category} | {count} |")

    lines.extend(["", "## High-priority findings", ""])
    high = [item for item in findings if item["severity"] == "high"]
    append_examples(lines, high, limit=40)

    for section in SECTIONS:
        lines.extend(["", f"## {section.upper()} findings", ""])
        section_findings = [item for item in findings if item["section"] == section and item["severity"] != "high"]
        append_grouped_examples(lines, section_findings)

    lines.extend(["", "## Cross-section overlap findings", ""])
    cross = [item for item in findings if "Cross-section" in item["message"]]
    append_examples(lines, cross, limit=40)

    lines.extend(["", "## Excluded pages and reasons", ""])
    for section in SECTIONS:
        section_excluded = [p for p in excluded if p.section == section]
        reason_counts = Counter(p.exclusion_reason for p in section_excluded)
        lines.append(f"### {section.upper()}")
        if not reason_counts:
            lines.append("- None")
        else:
            for reason, count in sorted(reason_counts.items()):
                examples = ", ".join(p.rel_source for p in section_excluded if p.exclusion_reason == reason)[:300]
                lines.append(f"- {reason}: {count} examples: {examples}")
        lines.append("")

    lines.extend(
        [
            "## Suggested next steps",
            "",
            "- Review high-priority metadata issues first, especially malformed front matter and duplicate permalinks.",
            "- Use overlap findings as editorial prompts, not automatic merge instructions.",
            "- Add role-based related links only where they improve learner navigation.",
            "- Improve descriptions and opening conclusions in small, topic-focused batches.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def append_grouped_examples(lines, items, limit=25):
    if not items:
        lines.append("- No findings.")
        return
    grouped = defaultdict(list)
    for item in items:
        grouped[item["category"]].append(item)
    for category, group in sorted(grouped.items()):
        lines.append(f"### {category} ({len(group)})")
        append_examples(lines, group, limit=limit)
        lines.append("")


def append_examples(lines, items, limit=20):
    if not items:
        lines.append("- None")
        return
    for item in items[:limit]:
        lines.append(f"- `{item['source_path']}`: {item['title']} - {item['message']}")
    if len(items) > limit:
        lines.append(f"- ... {len(items) - limit} more. See `artifacts/agent-content-audit.json`.")


def main_title_term(title: str) -> str:
    return re.split(r"とは|？|\?|【|（|\(", title)[0].strip()


def extract_opening_section(body: str) -> str:
    for heading in OPENING_HEADINGS:
        idx = body.find(heading)
        if idx >= 0:
            rest = body[idx + len(heading) :]
            next_heading = re.search(r"\n##\s+", rest)
            return rest[: next_heading.start()] if next_heading else rest
    return ""


def normalize_topic(title: str) -> str:
    value = main_title_term(title).lower()
    value = re.sub(r"[\s・:：/／\-＿_]+", "", value)
    return value


def topic_from_path(path: Path) -> str:
    stem = path.stem.lower()
    for token in ("-comparison", "-summary", "-cheatsheet", "-vs-"):
        stem = stem.replace(token, "-")
    return stem.strip("-")


def exclude_duplicate_outputs(records: list) -> tuple[list, list]:
    grouped = {}
    for record in records:
        grouped.setdefault(record.markdown_path, []).append(record)

    kept = []
    excluded = []
    for group in grouped.values():
        if len(group) == 1:
            kept.append(group[0])
            continue
        winner = choose_duplicate_winner(group)
        kept.append(winner)
        for record in group:
            if record is winner:
                continue
            record.excluded = True
            record.exclusion_reason = f"duplicate output path; representative: {winner.rel_source}"
            excluded.append(record)
    return kept, excluded


def choose_duplicate_winner(group: list):
    def key(record):
        slug = record.permalink.strip("/").split("/")[-1]
        stem = record.source_path.stem
        exact_slug = 0 if stem == slug else 1
        suffix_copy = 1 if stem.endswith("-1") else 0
        return (exact_slug, suffix_copy, len(stem), record.rel_source)

    return sorted(group, key=key)[0]


if __name__ == "__main__":
    raise SystemExit(main())
