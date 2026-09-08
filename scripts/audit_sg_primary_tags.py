#!/usr/bin/env python3
"""Audit SG primary-category tags.

This script checks Markdown files under pages/sg and reports:
- missing primary category tags
- multiple primary category tags
- deprecated broad tags that should be migrated

It intentionally does not rewrite files because some legacy articles need
human judgment when choosing their single primary category.
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

LEGACY_TAGS = {
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
TAGS_RE = re.compile(r"^tags:\s*\[(.*?)\]\s*$", re.MULTILINE)


def parse_tags(text: str) -> list[str] | None:
    front_matter_match = FRONT_MATTER_RE.search(text)
    if not front_matter_match:
        return None

    tags_match = TAGS_RE.search(front_matter_match.group(1))
    if not tags_match:
        return None

    return [
        item.strip().strip("'\"")
        for item in tags_match.group(1).split(",")
        if item.strip()
    ]


def should_skip(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    if path.name in SKIP_FILENAMES:
        return True
    return any(part in SKIP_PATH_PARTS for part in rel.parts[:-1])


def audit(root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for path in sorted(root.rglob("*.md")):
        if should_skip(path, root):
            continue

        rel = path.as_posix()
        text = path.read_text(encoding="utf-8")
        tags = parse_tags(text)

        if tags is None:
            errors.append(f"MISSING_TAGS  {rel}")
            continue

        if "sg" not in tags:
            errors.append(f"MISSING_SG    {rel}")

        primary = [tag for tag in tags if tag in PRIMARY_TAGS]
        if len(primary) == 0:
            legacy = [tag for tag in tags if tag in LEGACY_TAGS]
            suggestion = ""
            if legacy:
                mapped = sorted({LEGACY_TAGS[tag] for tag in legacy})
                suggestion = f" -> candidates: {', '.join(mapped)}"
            errors.append(f"NO_PRIMARY    {rel}{suggestion}")
        elif len(primary) > 1:
            errors.append(
                f"MULTI_PRIMARY {rel} -> {', '.join(primary)}"
            )

        legacy_present = [tag for tag in tags if tag in LEGACY_TAGS]
        if legacy_present:
            mapped = [f"{tag}->{LEGACY_TAGS[tag]}" for tag in legacy_present]
            warnings.append(f"LEGACY_TAG    {rel} -> {', '.join(mapped)}")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        default="pages/sg",
        help="SG Markdown root (default: pages/sg)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return exit code 1 when errors are found",
    )
    args = parser.parse_args()

    root = Path(args.root)
    if not root.exists():
        print(f"ERROR: root not found: {root}")
        return 2

    errors, warnings = audit(root)

    print("SG primary-tag audit")
    print(f"root: {root}")
    print(f"errors: {len(errors)}")
    print(f"warnings: {len(warnings)}")

    if errors:
        print("\n[ERRORS]")
        for item in errors:
            print(item)

    if warnings:
        print("\n[WARNINGS]")
        for item in warnings:
            print(item)

    if not errors and not warnings:
        print("OK: no tag issues found")

    if args.strict and errors:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
