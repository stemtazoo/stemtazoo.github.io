#!/usr/bin/env python3
"""Export DS pages into NotebookLM-friendly markdown bundles.

Default behavior:
- Read grouping from `pages/ds/index.md` front matter `ds_sections`.
- Export one markdown file per top-level section.
- Export one combined markdown file including all sections.

Optional behavior:
- `--groups-file` can point to a JSON file with explicit groups, e.g.
  {
    "groups": [
      {"id": "A1", "title": "行動規範", "items": ["/ds/foo/"]}
    ]
  }
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
DS_DIR = ROOT / "pages" / "ds"
INDEX_MD = DS_DIR / "index.md"
DEFAULT_OUT_DIR = ROOT / "exports" / "notebooklm" / "ds"

TITLE_RE = re.compile(r"^title:\s*(.+?)\s*$")
PERMALINK_RE = re.compile(r"^permalink:\s*(.+?)\s*$")
TOP_TITLE_RE = re.compile(r'^  - title: "([^"]+)"\s*$')
SUBSECTION_RE = re.compile(r"^    subsections:\s*$")
ITEM_RE = re.compile(r"^\s{4,8}-\s*(/ds/[^\s]+/)\s*$")


@dataclass
class Page:
    path: Path
    title: str
    permalink: str
    body: str


@dataclass
class Group:
    id: str
    title: str
    items: list[str]


def parse_front_matter(text: str) -> tuple[list[str], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return [], text

    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return [], text

    return lines[1:end], "\n".join(lines[end + 1 :]).lstrip("\n")


def parse_page(md_path: Path) -> Page | None:
    lines, body = parse_front_matter(md_path.read_text(encoding="utf-8"))
    title = ""
    permalink = ""
    for line in lines:
        m = TITLE_RE.match(line)
        if m:
            title = m.group(1).strip().strip('"')
        m = PERMALINK_RE.match(line)
        if m:
            permalink = m.group(1).strip().strip('"')

    if not title or not permalink:
        return None

    return Page(path=md_path, title=title, permalink=permalink, body=body)


def parse_groups_from_index(index_path: Path) -> list[Group]:
    fm_lines, _ = parse_front_matter(index_path.read_text(encoding="utf-8"))
    groups: list[Group] = []

    current_title: str | None = None
    current_items: list[str] = []
    in_subsections = False

    def flush() -> None:
        nonlocal current_title, current_items, in_subsections
        if current_title is not None:
            groups.append(
                Group(
                    id=slugify(current_title),
                    title=current_title,
                    items=list(dict.fromkeys(current_items)),
                )
            )
        current_title = None
        current_items = []
        in_subsections = False

    for line in fm_lines:
        top = TOP_TITLE_RE.match(line)
        if top:
            flush()
            current_title = top.group(1)
            continue

        if current_title is None:
            continue

        if SUBSECTION_RE.match(line):
            in_subsections = True
            continue

        item = ITEM_RE.match(line)
        if item:
            # Include both direct items and subsection items.
            current_items.append(item.group(1).strip())
            continue

        if in_subsections and re.match(r"^  - title:", line):
            # defensive; shouldn't happen because TOP_TITLE_RE handles above
            flush()

    flush()
    return groups


def parse_groups_from_json(groups_file: Path) -> list[Group]:
    payload = json.loads(groups_file.read_text(encoding="utf-8"))
    raw_groups = payload.get("groups", [])
    groups: list[Group] = []
    for idx, g in enumerate(raw_groups, start=1):
        title = str(g.get("title", f"group-{idx}"))
        gid = str(g.get("id", slugify(title)))
        items = [str(x) for x in g.get("items", []) if str(x).startswith("/ds/")]
        groups.append(Group(id=gid, title=title, items=list(dict.fromkeys(items))))
    return groups


def slugify(value: str) -> str:
    s = value.strip().lower()
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"[^\w\-ぁ-んァ-ン一-龥]", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "group"


def build_group_markdown(group: Group, pages_by_url: dict[str, Page]) -> str:
    out = [f"# {group.title}", ""]
    for url in group.items:
        p = pages_by_url.get(url)
        if p is None:
            out.append(f"## [MISSING] {url}")
            out.append("")
            continue

        out.append(f"## {p.title}")
        out.append(f"- Source: {p.path.relative_to(ROOT)}")
        out.append(f"- Permalink: {p.permalink}")
        out.append("")
        out.append(p.body.strip())
        out.append("")
        out.append("---")
        out.append("")

    return "\n".join(out).strip() + "\n"


def collect_pages() -> dict[str, Page]:
    pages: dict[str, Page] = {}
    for md in sorted(DS_DIR.glob("*.md")):
        if md.name == "index.md":
            continue
        page = parse_page(md)
        if page is None:
            continue
        pages[page.permalink] = page
    return pages


def add_uncategorized_group(groups: list[Group], pages_by_url: dict[str, Page]) -> list[Group]:
    seen = {url for g in groups for url in g.items}
    uncategorized = sorted(url for url in pages_by_url if url not in seen)
    if not uncategorized:
        return groups

    return groups + [Group(id="uncategorized", title="未分類", items=uncategorized)]


def export(groups: Iterable[Group], pages_by_url: dict[str, Page], out_dir: Path) -> None:
    sections_dir = out_dir / "sections"
    sections_dir.mkdir(parents=True, exist_ok=True)

    combined_parts: list[str] = ["# DS NotebookLM Export", ""]

    for group in groups:
        md = build_group_markdown(group, pages_by_url)
        section_path = sections_dir / f"{group.id}.md"
        section_path.write_text(md, encoding="utf-8")

        combined_parts.append(f"## {group.title}")
        combined_parts.append("")
        combined_parts.append(md)
        combined_parts.append("")

    (out_dir / "all.md").write_text("\n".join(combined_parts).strip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--groups-file", type=Path, default=None)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    args = parser.parse_args()

    pages_by_url = collect_pages()

    if args.groups_file:
        groups = parse_groups_from_json(args.groups_file)
    else:
        groups = parse_groups_from_index(INDEX_MD)

    groups = add_uncategorized_group(groups, pages_by_url)
    export(groups, pages_by_url, args.out_dir)

    print(f"Exported {len(groups)} group files to {args.out_dir / 'sections'}")
    print(f"Combined file: {args.out_dir / 'all.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
