#!/usr/bin/env python3
"""Finish reviewed SG primary-tag normalization for the final legacy cases."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

PRIMARY_TAGS = {
    "sg-security-overview",
    "sg-security-management",
    "sg-security-measures",
    "sg-security-law",
    "sg-technology",
    "sg-management",
    "sg-strategy",
}

LEGACY_TAGS = {
    "security_overview",
    "security_management",
    "security_measures",
    "security_law",
    "technology",
    "management",
    "strategy",
}

OVERRIDES = {
    "common-port-numbers.md": "sg-technology",
    "contract-types.md": "sg-strategy",
    "dns.md": "sg-technology",
    "personal-information-protection-law-sensitive-data.md": "sg-security-law",
    "project-lifecycle-characteristics.md": "sg-management",
    "specific-personal-information.md": "sg-security-law",
}

FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
TAGS_LINE_RE = re.compile(r"^tags:\s*\[(.*?)\]\s*$", re.MULTILINE)


def split_tags(raw: str) -> list[str]:
    return [item.strip().strip("'\"") for item in raw.split(",") if item.strip()]


def normalize(tags: list[str], primary: str) -> list[str]:
    kept = [tag for tag in tags if tag not in PRIMARY_TAGS and tag not in LEGACY_TAGS]
    if "sg" in kept:
        kept.insert(kept.index("sg") + 1, primary)
    else:
        kept[:0] = ["sg", primary]

    result: list[str] = []
    seen: set[str] = set()
    for tag in kept:
        if tag not in seen:
            result.append(tag)
            seen.add(tag)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default="pages/sg")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    root = Path(args.root)
    changed = 0

    for filename, primary in OVERRIDES.items():
        path = root / filename
        text = path.read_text(encoding="utf-8")
        front = FRONT_MATTER_RE.search(text)
        if not front:
            raise RuntimeError(f"No front matter: {path}")
        match = TAGS_LINE_RE.search(front.group(1))
        if not match:
            raise RuntimeError(f"No inline tags: {path}")

        tags = split_tags(match.group(1))
        new_tags = normalize(tags, primary)
        if new_tags == tags:
            print(f"SKIP         {path}")
            continue

        new_line = "tags: [" + ", ".join(new_tags) + "]"
        new_text = text.replace(match.group(0), new_line, 1)
        if args.apply:
            path.write_text(new_text, encoding="utf-8")
        changed += 1
        print(f"{'UPDATED' if args.apply else 'WOULD_UPDATE':12} {path} -> {primary}")

    print(f"changed={changed} mode={'apply' if args.apply else 'dry-run'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
