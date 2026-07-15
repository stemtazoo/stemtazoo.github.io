#!/usr/bin/env python3
"""Backfill missing Jekyll ``last_modified_at`` values under ``pages/``.

For each Markdown file whose YAML front matter does not contain a non-empty
``last_modified_at`` value, use the date of the file's latest Git commit.
Existing values are never changed.
"""

from __future__ import annotations

import re
import subprocess
from datetime import date
from pathlib import Path

PAGES_DIR = Path("pages")
FIELD_RE = re.compile(r"^last_modified_at\s*:\s*(.*?)\s*$", re.MULTILINE)


def latest_commit_date(path: Path) -> str:
    result = subprocess.run(
        ["git", "log", "-1", "--format=%cs", "--", path.as_posix()],
        check=False,
        capture_output=True,
        text=True,
    )
    value = result.stdout.strip()
    return value or date.today().isoformat()


def update_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return False

    closing = text.find("\n---", 4)
    if closing == -1:
        return False

    front_matter = text[4:closing]
    match = FIELD_RE.search(front_matter)
    if match and match.group(1):
        return False

    value = latest_commit_date(path)
    if match:
        updated_front_matter = FIELD_RE.sub(
            f"last_modified_at: {value}", front_matter, count=1
        )
    else:
        updated_front_matter = front_matter.rstrip() + f"\nlast_modified_at: {value}\n"

    updated = "---\n" + updated_front_matter + text[closing:]
    path.write_text(updated, encoding="utf-8", newline="\n")
    return True


def main() -> None:
    changed: list[Path] = []
    for path in sorted(PAGES_DIR.rglob("*.md")):
        if update_file(path):
            changed.append(path)

    print(f"Updated {len(changed)} Markdown files.")
    for path in changed:
        print(path.as_posix())


if __name__ == "__main__":
    main()
