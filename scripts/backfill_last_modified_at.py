#!/usr/bin/env python3
"""Backfill missing update dates for normal DS and GK articles.

For each eligible Markdown file whose YAML front matter does not contain a
non-empty ``last_modified_at`` value, use the date of the file's latest Git
commit. Existing values are never changed.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

ARTICLE_DIRS = (Path("pages/ds"), Path("pages/gk"))
FIELD_RE = re.compile(r"^last_modified_at\s*:\s*(.*?)\s*$", re.MULTILINE)
LAYOUT_NULL_RE = re.compile(r"^layout\s*:\s*(?:null|~)\s*$", re.MULTILINE)
SITEMAP_FALSE_RE = re.compile(r"^sitemap\s*:\s*false\s*$", re.MULTILINE)


def latest_commit_date(path: Path) -> str:
    result = subprocess.run(
        ["git", "log", "-1", "--format=%cs", "--", path.as_posix()],
        check=False,
        capture_output=True,
        text=True,
    )
    value = result.stdout.strip()
    if not value:
        raise RuntimeError(f"No Git history found for {path.as_posix()}")
    return value


def front_matter(text: str) -> tuple[str, int] | None:
    if not text.startswith("---\n"):
        return None

    closing = text.find("\n---", 4)
    if closing == -1:
        return None

    return text[4:closing], closing


def is_normal_article(path: Path, metadata: str) -> bool:
    if path.name.lower() == "index.md":
        return False
    if LAYOUT_NULL_RE.search(metadata) or SITEMAP_FALSE_RE.search(metadata):
        return False
    return True


def update_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    parsed = front_matter(text)
    if parsed is None:
        return False

    metadata, closing = parsed
    if not is_normal_article(path, metadata):
        return False

    match = FIELD_RE.search(metadata)
    if match and match.group(1):
        return False

    value = latest_commit_date(path)
    if match:
        updated_metadata = FIELD_RE.sub(
            f"last_modified_at: {value}", metadata, count=1
        )
    else:
        updated_metadata = metadata.rstrip() + f"\nlast_modified_at: {value}\n"

    updated = "---\n" + updated_metadata + text[closing:]
    path.write_text(updated, encoding="utf-8", newline="\n")
    return True


def main() -> None:
    changed: list[Path] = []
    for article_dir in ARTICLE_DIRS:
        for path in sorted(article_dir.glob("*.md")):
            if update_file(path):
                changed.append(path)

    print(f"Updated {len(changed)} DS/GK article files.")
    for path in changed:
        print(path.as_posix())


if __name__ == "__main__":
    main()
