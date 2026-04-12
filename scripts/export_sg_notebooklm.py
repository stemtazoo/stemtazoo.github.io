#!/usr/bin/env python3
"""Export SG pages into NotebookLM-friendly markdown bundles.

Default behavior:
- Read grouping from `pages/sg/index.md`.
- Export one markdown file per section.
- Export one combined markdown file including all sections.

Optional behavior:
- `--groups-file` can point to a JSON file with explicit groups, e.g.
  {
    "groups": [
      {"id": "network", "title": "Network", "items": ["/sg/dns/"]}
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
SG_DIR = ROOT / "pages" / "sg"
INDEX_MD = SG_DIR / "index.md"
DEFAULT_OUT_DIR = ROOT / "exports" / "notebooklm" / "sg"

TITLE_RE = re.compile(r"^title:\s*(.+?)\s*$")
PERMALINK_RE = re.compile(r"^permalink:\s*(.+?)\s*$")
TAGS_RE = re.compile(r"^tags:\s*\[(.*?)\]\s*$")

HEADING_RE = re.compile(r"^(##|###)\s+(.+?)\s*$")
LATEST_URLS_RE = re.compile(r'sg_latest_urls\s*=\s*"([^"]+)"')
TAG_CONTAINS_RE = re.compile(r"contains\s+'([^']+)'")


@dataclass
class Page:
    path: Path
    title: str
    permalink: str
    tags: list[str]
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
    tags: list[str] = []

    for line in lines:
        title_match = TITLE_RE.match(line)
        if title_match:
            title = title_match.group(1).strip().strip('"')

        permalink_match = PERMALINK_RE.match(line)
        if permalink_match:
            permalink = permalink_match.group(1).strip().strip('"')

        tags_match = TAGS_RE.match(line)
        if tags_match:
            raw_tags = tags_match.group(1)
            tags = [part.strip().strip('"').strip("'") for part in raw_tags.split(",") if part.strip()]

    if not title or not permalink:
        return None

    return Page(path=md_path, title=title, permalink=permalink, tags=tags, body=body)


def slugify(value: str) -> str:
    s = value.strip().lower()
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"[^\w\-\u3040-\u30ff\u4e00-\u9fff]", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "group"


def parse_groups_from_index(index_path: Path, pages_by_url: dict[str, Page]) -> list[Group]:
    _, body = parse_front_matter(index_path.read_text(encoding="utf-8"))
    groups: list[Group] = []
    seen_titles: set[str] = set()
    seen_tags: set[str] = set()
    current_heading: str | None = None

    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("{% assign shown_urls"):
            break

        heading_match = HEADING_RE.match(stripped)
        if heading_match:
            current_heading = heading_match.group(2).strip()
            continue

        latest_match = LATEST_URLS_RE.search(stripped)
        if latest_match and current_heading and current_heading not in seen_titles:
            items = [item.strip() for item in latest_match.group(1).split(",") if item.strip()]
            groups.append(Group(id=slugify(current_heading), title=current_heading, items=items))
            seen_titles.add(current_heading)
            continue

        tag_match = TAG_CONTAINS_RE.search(stripped)
        if not tag_match or current_heading is None:
            continue

        tag = tag_match.group(1).strip()
        if not tag.startswith("sg-") or tag in seen_tags:
            continue

        items = [
            page.permalink
            for page in sorted(pages_by_url.values(), key=lambda p: (p.path.name, p.permalink))
            if tag in page.tags
        ]
        groups.append(Group(id=slugify(current_heading), title=current_heading, items=items))
        seen_tags.add(tag)

    return groups


def parse_groups_from_json(groups_file: Path) -> list[Group]:
    payload = json.loads(groups_file.read_text(encoding="utf-8"))
    raw_groups = payload.get("groups", [])
    groups: list[Group] = []
    for idx, group in enumerate(raw_groups, start=1):
        title = str(group.get("title", f"group-{idx}"))
        gid = str(group.get("id", slugify(title)))
        items = [str(item) for item in group.get("items", []) if str(item).startswith("/sg/")]
        groups.append(Group(id=gid, title=title, items=list(dict.fromkeys(items))))
    return groups


def collect_pages() -> dict[str, Page]:
    pages: dict[str, Page] = {}
    for md in sorted(SG_DIR.glob("*.md")):
        if md.name == "index.md":
            continue
        page = parse_page(md)
        if page is None:
            continue
        pages[page.permalink] = page
    return pages


def add_uncategorized_group(groups: list[Group], pages_by_url: dict[str, Page]) -> list[Group]:
    seen = {url for group in groups for url in group.items}
    uncategorized = sorted(url for url in pages_by_url if url not in seen)
    if not uncategorized:
        return groups

    return groups + [Group(id="uncategorized", title="Uncategorized", items=uncategorized)]


def build_group_markdown(group: Group, pages_by_url: dict[str, Page]) -> str:
    out = [f"# {group.title}", ""]
    for url in group.items:
        page = pages_by_url.get(url)
        if page is None:
            out.append(f"## [MISSING] {url}")
            out.append("")
            continue

        out.append(f"## {page.title}")
        out.append(f"- Source: {page.path.relative_to(ROOT)}")
        out.append(f"- Permalink: {page.permalink}")
        out.append("")
        out.append(page.body.strip())
        out.append("")
        out.append("---")
        out.append("")

    return "\n".join(out).strip() + "\n"


def export(groups: Iterable[Group], pages_by_url: dict[str, Page], out_dir: Path) -> None:
    sections_dir = out_dir / "sections"
    sections_dir.mkdir(parents=True, exist_ok=True)

    combined_parts: list[str] = ["# SG NotebookLM Export", ""]

    for group in groups:
        markdown = build_group_markdown(group, pages_by_url)
        (sections_dir / f"{group.id}.md").write_text(markdown, encoding="utf-8")

        combined_parts.append(f"## {group.title}")
        combined_parts.append("")
        combined_parts.append(markdown)
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
        groups = parse_groups_from_index(INDEX_MD, pages_by_url)

    groups = add_uncategorized_group(groups, pages_by_url)
    export(groups, pages_by_url, args.out_dir)

    print(f"Exported {len(groups)} group files to {args.out_dir / 'sections'}")
    print(f"Combined file: {args.out_dir / 'all.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
