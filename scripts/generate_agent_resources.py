#!/usr/bin/env python3
"""Generate agent-readable Markdown resources after the Jekyll build."""

from __future__ import annotations

from pathlib import Path

from agent_resource_lib import (
    ROOT,
    SECTION_DESCRIPTIONS,
    SECTION_LABELS,
    SECTIONS,
    SITE_DIR,
    classify_page,
    clean_body,
    discover_pages,
    sort_key,
    write_json,
)


MANIFEST_PATH = SITE_DIR / "agent-resources-manifest.json"


def front_matter_for(record) -> str:
    fields = {
        "title": record.title,
        "description": record.description,
        "last_modified_at": record.front_matter.get("last_modified_at", ""),
        "canonical_url": record.canonical_url,
        "section": record.section,
        "content_status": record.front_matter.get("content_status", ""),
    }
    lines = ["---"]
    for key, value in fields.items():
        if value == "" or value is None:
            continue
        escaped = str(value).replace('"', '\\"')
        lines.append(f'{key}: "{escaped}"')
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def write_article_markdown(record) -> None:
    path: Path = Path(record.markdown_path)
    if path.name != "index.md":
        raise ValueError(f"unsafe generated path for {record.rel_source}: {path}")
    if ".." in path.parts:
        raise ValueError(f"path traversal in generated path for {record.rel_source}: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    body = clean_body(record.body, record)
    path.write_text(front_matter_for(record) + body, encoding="utf-8")


def write_section_llms(section: str, records: list) -> None:
    path = SITE_DIR / section / "llms.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {SECTION_LABELS[section]}",
        "",
        SECTION_DESCRIPTIONS[section],
        "",
        "## Articles",
        "",
    ]
    for record in sorted(records, key=sort_key):
        description = record.description or f"{record.title} の学習記事です。"
        if not record.description:
            record.warnings.append("fallback description used in llms.txt")
        lines.append(f"- [{record.title}]({record.markdown_url})")
        lines.append(f"  - {description}")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    if not SITE_DIR.exists():
        print("_site does not exist. Run the Jekyll build first.")
        return 1

    pages, parse_errors = discover_pages()
    included = []
    excluded = []
    for page in pages:
        classify_page(page)
        if page.excluded:
            excluded.append(page)
        else:
            included.append(page)

    included, duplicate_excluded = exclude_duplicate_outputs(included)
    excluded.extend(duplicate_excluded)

    for record in included:
        write_article_markdown(record)

    by_section = {section: [] for section in SECTIONS}
    for record in included:
        by_section[record.section].append(record)
    for section in SECTIONS:
        write_section_llms(section, by_section[section])

    manifest = {
        "site_url": "https://stemtazoo.github.io",
        "generated_by": "scripts/generate_agent_resources.py",
        "parse_errors": parse_errors,
        "included": [
            {
                "source_path": record.rel_source,
                "section": record.section,
                "title": record.title,
                "description": record.description,
                "permalink": record.permalink,
                "canonical_url": record.canonical_url,
                "markdown_path": Path(record.markdown_path).relative_to(ROOT).as_posix(),
                "markdown_url": record.markdown_url,
                "warnings": sorted(set(record.warnings)),
            }
            for record in sorted(included, key=sort_key)
        ],
        "excluded": [
            {
                "source_path": record.rel_source,
                "section": record.section,
                "title": record.title,
                "permalink": record.permalink,
                "reason": record.exclusion_reason,
            }
            for record in sorted(excluded, key=lambda r: (r.section, r.rel_source))
        ],
    }
    write_json(MANIFEST_PATH, manifest)

    print(f"Generated {len(included)} article Markdown resources.")
    for section in SECTIONS:
        print(f"- {section}: {len(by_section[section])} entries")
    if parse_errors:
        print(f"Parse errors recorded: {len(parse_errors)}")
    return 0


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
                record.warnings.append("duplicate output path representative")
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
