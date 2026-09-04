#!/usr/bin/env python3
"""Add DS ver.6 classification metadata to safely mappable DS articles.

Default behavior is dry-run. Use --write to modify files.

The script intentionally skips ambiguous tags such as business, design, security,
ai-utilization, skillcheck, and cheatsheet. Existing categories/tags are preserved.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DS_DIR = ROOT / "pages" / "ds"

SAFE_TAG_MAP: dict[str, tuple[str, str]] = {
    "linear-algebra": ("datascience", "linear-algebra"),
    "calculus": ("datascience", "calculus"),
    "set-theory": ("datascience", "set-theory"),
    "statistics": ("datascience", "statistics"),
    "data-preparation": ("datascience", "data-preparation"),
    "visualization": ("datascience", "visualization"),
    "modeling": ("datascience", "modeling"),
    "unstructured-data": ("datascience", "unstructured-data"),
    "environment-setup": ("dataengineering", "environment-setup"),
    "data-collection": ("dataengineering", "data-collection"),
    "data-structure": ("dataengineering", "data-structure"),
    "data-storage": ("dataengineering", "data-storage"),
    "data-processing": ("dataengineering", "data-processing"),
    "sql": ("dataengineering", "sql"),
    "database": ("dataengineering", "database"),
}

TAG_LINE = re.compile(r"^tags:\s*\[(.*?)\]\s*$")
AREA_LINE = re.compile(r"^ds_area:\s*")


def front_matter_bounds(lines: list[str]) -> tuple[int, int] | None:
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return 0, i
    return None


def parse_tags(line: str) -> list[str]:
    m = TAG_LINE.match(line.strip())
    if not m:
        return []
    return [x.strip().strip("'\"") for x in m.group(1).split(",") if x.strip()]


def read_front_matter_tags(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8-sig")
    lines = text.splitlines()
    bounds = front_matter_bounds(lines)
    if bounds is None:
        return []
    _, end = bounds
    for line in lines[1:end]:
        tags = parse_tags(line)
        if tags:
            return tags
    return []


def classify(tags: list[str]) -> tuple[str, str, str] | None:
    matches = [(tag, *SAFE_TAG_MAP[tag]) for tag in tags if tag in SAFE_TAG_MAP]
    if not matches:
        return None

    areas = {area for _, area, _ in matches}
    if len(areas) != 1:
        return None

    # Prefer the first safely mappable topic tag already present in front matter.
    tag, area, section = matches[0]
    return tag, area, section


def update_file(path: Path, write: bool) -> tuple[str, str | None]:
    text = path.read_text(encoding="utf-8-sig")
    newline = "\r\n" if "\r\n" in text else "\n"
    lines = text.splitlines()
    bounds = front_matter_bounds(lines)
    if bounds is None:
        return "skip", "invalid-front-matter"

    _, end = bounds
    fm = lines[1:end]
    if any(AREA_LINE.match(line.strip()) for line in fm):
        return "skip", "already-classified"

    tags: list[str] = []
    tag_index: int | None = None
    for i, line in enumerate(fm):
        parsed = parse_tags(line)
        if parsed:
            tags = parsed
            tag_index = i
            break

    if tag_index is None:
        return "skip", "no-tags"

    result = classify(tags)
    if result is None:
        return "skip", "ambiguous-or-unmapped"

    source_tag, area, section = result
    insert_at = 1 + tag_index + 1
    lines[insert_at:insert_at] = [
        f"ds_area: {area}",
        f"ds_section: {section}",
    ]

    if write:
        path.write_text(newline.join(lines) + newline, encoding="utf-8")

    return "change", f"{source_tag} -> {area}/{section}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Apply changes. Default is dry-run.")
    parser.add_argument("--tag", choices=sorted(SAFE_TAG_MAP), help="Only process files whose front matter contains this safe tag.")
    args = parser.parse_args()

    changed = 0
    skipped = 0
    for path in sorted(DS_DIR.glob("*.md")):
        if path.name == "index.md":
            continue

        if args.tag and args.tag not in read_front_matter_tags(path):
            continue

        status, detail = update_file(path, args.write)
        rel = path.relative_to(ROOT)
        if status == "change":
            changed += 1
            prefix = "UPDATED" if args.write else "WOULD UPDATE"
            print(f"{prefix}: {rel} ({detail})")
        else:
            skipped += 1

    mode = "write" if args.write else "dry-run"
    print(f"\nMode: {mode}")
    print(f"Candidates: {changed}")
    print(f"Skipped: {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
