#!/usr/bin/env python3
"""Safely normalize SG primary-category tags.

Default mode is dry-run. Use --apply to write only unambiguous changes:

1. If exactly one current primary tag exists, remove only legacy broad tags
   that map to that same primary category.
2. If no current primary tag exists and exactly one legacy primary candidate
   exists, replace that legacy tag with the current primary tag.
3. If multiple current primary tags or multiple legacy candidates exist,
   report the file and do not modify it.

This deliberately avoids guessing article classification.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

PRIMARY_TAGS = (
    "sg-security-overview",
    "sg-security-management",
    "sg-security-measures",
    "sg-security-law",
    "sg-technology",
    "sg-management",
    "sg-strategy",
)

LEGACY_TO_PRIMARY = {
    "security_overview": "sg-security-overview",
    "security_management": "sg-security-management",
    "security_measures": "sg-security-measures",
    "security_law": "sg-security-law",
    "technology": "sg-technology",
    "management": "sg-management",
    "strategy": "sg-strategy",
}

SKIP_PATH_PARTS = {"category", "past"}
SKIP_FILENAMES = {"index.md", "all.md"}

FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
TAGS_LINE_RE = re.compile(r"^tags:\s*\[(.*?)\]\s*$", re.MULTILINE)


def split_tags(raw: str) -> list[str]:
    return [
        item.strip().strip("'\"")
        for item in raw.split(",")
        if item.strip()
    ]


def format_tags(tags: list[str]) -> str:
    return "tags: [" + ", ".join(tags) + "]"


def should_skip(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    if path.name in SKIP_FILENAMES:
        return True
    return any(part in SKIP_PATH_PARTS for part in rel.parts[:-1])


def normalize_tags(tags: list[str]) -> tuple[list[str], str]:
    current = [tag for tag in tags if tag in PRIMARY_TAGS]
    legacy = [tag for tag in tags if tag in LEGACY_TO_PRIMARY]
    legacy_candidates = sorted({LEGACY_TO_PRIMARY[tag] for tag in legacy})

    if len(current) > 1:
        return tags, "manual: multiple current primary tags"

    if len(current) == 1:
        primary = current[0]
        removable = {
            legacy_tag
            for legacy_tag, mapped in LEGACY_TO_PRIMARY.items()
            if mapped == primary
        }
        new_tags = [tag for tag in tags if tag not in removable]
        if new_tags == tags:
            return tags, "ok"
        return new_tags, f"remove legacy alias for {primary}"

    if len(legacy_candidates) == 1:
        primary = legacy_candidates[0]
        new_tags: list[str] = []
        inserted = False
        for tag in tags:
            if tag in LEGACY_TO_PRIMARY:
                if not inserted:
                    new_tags.append(primary)
                    inserted = True
                continue
            new_tags.append(tag)
        if not inserted:
            new_tags.insert(1 if new_tags and new_tags[0] == "sg" else 0, primary)
        return new_tags, f"migrate to {primary}"

    if len(legacy_candidates) > 1:
        return tags, "manual: multiple legacy primary candidates"

    return tags, "manual: no primary category candidate"


def process_file(path: Path, apply: bool) -> tuple[str, bool]:
    text = path.read_text(encoding="utf-8")
    front_match = FRONT_MATTER_RE.search(text)
    if not front_match:
        return "manual: no front matter", False

    tags_match = TAGS_LINE_RE.search(front_match.group(1))
    if not tags_match:
        return "manual: no inline tags list", False

    tags = split_tags(tags_match.group(1))
    new_tags, status = normalize_tags(tags)
    if new_tags == tags:
        return status, False

    old_line = tags_match.group(0)
    new_line = format_tags(new_tags)
    new_text = text.replace(old_line, new_line, 1)

    if apply:
        path.write_text(new_text, encoding="utf-8")
    return status, True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default="pages/sg")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write safe changes. Without this flag, only report them.",
    )
    args = parser.parse_args()

    root = Path(args.root)
    if not root.exists():
        print(f"ERROR: root not found: {root}")
        return 2

    changed = 0
    manual = 0
    unchanged = 0

    for path in sorted(root.rglob("*.md")):
        if should_skip(path, root):
            continue

        status, would_change = process_file(path, args.apply)
        rel = path.as_posix()

        if would_change:
            changed += 1
            prefix = "UPDATED" if args.apply else "WOULD_UPDATE"
            print(f"{prefix:12} {rel} -> {status}")
        elif status.startswith("manual:"):
            manual += 1
            print(f"MANUAL       {rel} -> {status}")
        else:
            unchanged += 1

    mode = "apply" if args.apply else "dry-run"
    print(f"\nmode={mode} changed={changed} manual={manual} unchanged={unchanged}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
