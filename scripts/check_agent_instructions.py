#!/usr/bin/env python3
"""Check concrete local rule references, including filename case, without judging prose."""
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
RULE_REF = re.compile(r"(?:docs/agent|project_rules)/[A-Za-z0-9_./-]+\.md")
MD_LINK = re.compile(r"\[[^\]\n]*\]\(([^)\n]+)\)")


def references(path: Path, root: Path):
    text = path.read_text(encoding="utf-8")
    for number, line in enumerate(text.splitlines(), 1):
        for match in RULE_REF.finditer(line):
            yield number, root / match.group()
        # Detailed guide links are relative to that guide, not to repository root.
        if path.is_relative_to(root / "docs/agent"):
            for match in MD_LINK.finditer(line):
                value = match.group(1).strip().split(' "', 1)[0].strip("<>")
                parsed = urlsplit(value)
                if parsed.scheme or parsed.netloc or not parsed.path or value.startswith("/"):
                    continue
                if parsed.path.endswith(".md"):
                    yield number, path.parent / unquote(parsed.path)


def check(root: Path) -> list[str]:
    files = [root / "AGENTS.md", root / "README.md"]
    files += sorted((root / "docs/agent").rglob("*.md"))
    files += sorted((root / "project_rules").rglob("*.md"))
    errors = []
    # Explicit path inventory catches case drift even on a case-insensitive filesystem.
    existing = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file() and ".git" not in p.parts}
    for path in files:
        if not path.is_file():
            errors.append(f"missing entry file: {path.relative_to(root)}")
            continue
        for line, target in references(path, root):
            try:
                relative = target.resolve().relative_to(root.resolve()).as_posix()
            except ValueError:
                errors.append(f"{path.relative_to(root)}:{line}: reference escapes repository")
                continue
            if relative not in existing:
                errors.append(f"{path.relative_to(root)}:{line}: missing or case-mismatched rule: {relative}")
    return sorted(set(errors))


if __name__ == "__main__":
    findings = check(ROOT)
    for finding in findings:
        print(f"ERROR: {finding}")
    if not findings:
        print("Agent instruction references valid (behavioral scenarios require separate review).")
    raise SystemExit(bool(findings))
