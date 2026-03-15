#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DS_DIR = ROOT / "pages" / "ds"
REQUIRED_KEYS = ["layout", "title", "permalink", "tags"]

BAD_COMBINED = re.compile(r"^layout:\s*page\s+title:")
KEY_LINE = {k: re.compile(rf"^{k}:\s*") for k in REQUIRED_KEYS}


def lint_file(path: Path) -> list[str]:
    errors: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines()

    for i, line in enumerate(lines, start=1):
        if BAD_COMBINED.search(line):
            errors.append(f"line {i}: found combined keys 'layout: page title:'")

    present = {k: any(KEY_LINE[k].match(line) for line in lines[:40]) for k in REQUIRED_KEYS}
    if not all(present.values()):
        return errors

    if not lines or lines[0].strip() != "---":
        errors.append("front matter must start with '---' on line 1")
        return errors

    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        errors.append("front matter closing '---' not found")
        return errors

    fm = lines[1:end]
    for key in REQUIRED_KEYS:
        matches = [i for i, line in enumerate(fm, start=2) if KEY_LINE[key].match(line)]
        if len(matches) == 0:
            errors.append(f"missing key line in front matter: {key}")
        elif len(matches) > 1:
            errors.append(f"duplicate key lines in front matter: {key}")

    if end + 1 < len(lines):
        if lines[end + 1].strip() != "":
            errors.append("exactly one blank line required between front matter and body")
        elif end + 2 < len(lines) and lines[end + 2].strip() == "":
            errors.append("exactly one blank line required between front matter and body")

    return errors


def main() -> int:
    md_files = sorted(DS_DIR.glob("*.md"))
    count = 0
    for p in md_files:
        errs = lint_file(p)
        if errs:
            count += len(errs)
            print(p.relative_to(ROOT))
            for e in errs:
                print(f"  - {e}")
    if count:
        print(f"\nFound {count} front matter issue(s).")
        return 1
    print(f"OK: {len(md_files)} files passed DS front matter lint")
    return 0


if __name__ == "__main__":
    sys.exit(main())
