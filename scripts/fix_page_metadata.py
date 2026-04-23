#!/usr/bin/env python3
"""Audit and safely fix page navigation/footer metadata for a theme folder.

Default behavior:
- Scan only the specified folder's direct `*.md` files.
- Report missing breadcrumb/footer/prev-next related settings by theme.
- Apply only fixes that can be inferred uniquely from existing metadata.

Supported folders:
- `pages/sg`
- `pages/gk`
- `pages/ds`
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES_DIR = ROOT / "pages"

FRONT_MATTER_BOUNDARY = "---"
FOOTER_INCLUDE = {
    "sg": "{% include sg_article_footer.html %}",
    "gk": "{% include gk_article_footer.html %}",
}


@dataclass
class PageFile:
    path: Path
    folder: str
    front_matter_lines: list[str]
    body: str
    permalink: str
    prev: str | None
    next: str | None
    gk_section: str | None
    gk_order: str | None


def parse_front_matter(text: str) -> tuple[list[str], str]:
    lines = text.splitlines()
    if lines:
        lines[0] = lines[0].lstrip("\ufeff")

    if not lines or lines[0].strip() != FRONT_MATTER_BOUNDARY:
        return [], text

    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == FRONT_MATTER_BOUNDARY:
            end = i
            break
    if end is None:
        return [], text

    return lines[1:end], "\n".join(lines[end + 1 :]).lstrip("\n")


def parse_key(front_matter_lines: list[str], key: str) -> str | None:
    prefix = f"{key}:"
    for line in front_matter_lines:
        if line.startswith(prefix):
            return line.split(":", 1)[1].strip()
    return None


def load_page(path: Path, folder: str) -> PageFile:
    text = path.read_text(encoding="utf-8")
    front_matter_lines, body = parse_front_matter(text)

    return PageFile(
        path=path,
        folder=folder,
        front_matter_lines=front_matter_lines,
        body=body,
        permalink=(parse_key(front_matter_lines, "permalink") or "").strip('"').strip("'"),
        prev=(parse_key(front_matter_lines, "prev") or "").strip('"').strip("'") or None,
        next=(parse_key(front_matter_lines, "next") or "").strip('"').strip("'") or None,
        gk_section=(parse_key(front_matter_lines, "gk_section") or "").strip('"').strip("'") or None,
        gk_order=(parse_key(front_matter_lines, "gk_order") or "").strip('"').strip("'") or None,
    )


def is_article(page: PageFile) -> bool:
    return page.path.name.lower() != "index.md"


def replace_or_add_front_matter_key(lines: list[str], key: str, value: str) -> list[str]:
    prefix = f"{key}:"
    updated = []
    replaced = False
    for line in lines:
        if line.startswith(prefix):
            updated.append(f"{key}: {value}")
            replaced = True
        else:
            updated.append(line)
    if not replaced:
        updated.append(f"{key}: {value}")
    return updated


def ensure_footer_include(body: str, include_line: str) -> tuple[str, bool]:
    if include_line in body:
        return body, False

    stripped = body.rstrip()
    if stripped:
        new_body = stripped + "\n\n" + include_line + "\n"
    else:
        new_body = include_line + "\n"
    return new_body, True


def serialize(front_matter_lines: list[str], body: str) -> str:
    return (
        FRONT_MATTER_BOUNDARY
        + "\n"
        + "\n".join(front_matter_lines)
        + "\n"
        + FRONT_MATTER_BOUNDARY
        + "\n\n"
        + body.lstrip("\n")
    )


def resolve_folder(input_path: str) -> Path:
    candidate = Path(input_path)
    if not candidate.is_absolute():
        candidate = (ROOT / candidate).resolve()
    else:
        candidate = candidate.resolve()

    try:
        candidate.relative_to(PAGES_DIR)
    except ValueError as exc:
        raise SystemExit(f"Folder must be inside {PAGES_DIR}") from exc

    if not candidate.is_dir():
        raise SystemExit(f"Folder not found: {candidate}")

    return candidate


def collect_pages(folder_path: Path) -> list[PageFile]:
    folder_name = folder_path.name.lower()
    return [load_page(path, folder_name) for path in sorted(folder_path.glob("*.md"))]


def candidate_prev(page: PageFile, pages: list[PageFile]) -> tuple[str | None, list[str]]:
    matches = [other.permalink for other in pages if other.next == page.permalink]
    if len(matches) == 1:
        return matches[0], matches
    return None, matches


def candidate_next(page: PageFile, pages: list[PageFile]) -> tuple[str | None, list[str]]:
    matches = [other.permalink for other in pages if other.prev == page.permalink]
    if len(matches) == 1:
        return matches[0], matches
    return None, matches


def update_sg_or_ds_page(page: PageFile, pages: list[PageFile], apply_changes: bool) -> list[str]:
    changes: list[str] = []
    updated_front_matter = list(page.front_matter_lines)
    updated_body = page.body

    prev_guess, prev_matches = candidate_prev(page, pages)
    next_guess, next_matches = candidate_next(page, pages)

    if page.prev is None:
        if prev_guess:
            updated_front_matter = replace_or_add_front_matter_key(updated_front_matter, "prev", prev_guess)
            changes.append(f"set prev -> {prev_guess}")
        elif len(prev_matches) > 1:
            changes.append(f"unresolved prev (multiple backlinks: {', '.join(prev_matches)})")
        else:
            changes.append("unresolved prev")

    if page.next is None:
        if next_guess:
            updated_front_matter = replace_or_add_front_matter_key(updated_front_matter, "next", next_guess)
            changes.append(f"set next -> {next_guess}")
        elif len(next_matches) > 1:
            changes.append(f"unresolved next (multiple backlinks: {', '.join(next_matches)})")
        else:
            changes.append("unresolved next")

    include_line = FOOTER_INCLUDE.get(page.folder)
    if include_line:
        updated_body, footer_added = ensure_footer_include(updated_body, include_line)
        if footer_added:
            changes.append("added footer include")

    if apply_changes and any(change.startswith("set ") or change == "added footer include" for change in changes):
        page.path.write_text(serialize(updated_front_matter, updated_body), encoding="utf-8")

    return changes


def update_gk_page(page: PageFile, apply_changes: bool) -> list[str]:
    changes: list[str] = []
    updated_body = page.body

    if page.gk_section is None:
        changes.append("unresolved gk_section")
    if page.gk_order is None:
        changes.append("unresolved gk_order")

    updated_body, footer_added = ensure_footer_include(updated_body, FOOTER_INCLUDE["gk"])
    if footer_added:
        changes.append("added footer include")

    if apply_changes and "added footer include" in changes:
        page.path.write_text(serialize(page.front_matter_lines, updated_body), encoding="utf-8")

    return changes


def audit_folder(folder_path: Path, apply_changes: bool) -> int:
    pages = collect_pages(folder_path)
    folder_name = folder_path.name.lower()
    article_pages = [page for page in pages if is_article(page)]
    actionable = 0

    print(f"Folder: {folder_path.relative_to(ROOT)}")
    print(f"Mode: {'apply' if apply_changes else 'report'}")
    print(f"Scope: direct markdown files only ({len(article_pages)} article files)")

    for page in article_pages:
        if not page.permalink:
            print(f"- {page.path.name}: skipped (missing permalink)")
            continue

        if folder_name in {"sg", "ds"}:
            changes = update_sg_or_ds_page(page, article_pages, apply_changes)
        elif folder_name == "gk":
            changes = update_gk_page(page, apply_changes)
        else:
            raise SystemExit(f"Unsupported folder: {folder_name}")

        if changes:
            actionable += 1
            print(f"- {page.path.name}")
            for change in changes:
                print(f"  - {change}")

    if actionable == 0:
        print("No missing settings found.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", help="Target folder, e.g. pages/sg")
    parser.add_argument("--apply", action="store_true", help="Write safe fixes back to files")
    args = parser.parse_args()

    folder_path = resolve_folder(args.folder)
    return audit_folder(folder_path, apply_changes=args.apply)


if __name__ == "__main__":
    raise SystemExit(main())
