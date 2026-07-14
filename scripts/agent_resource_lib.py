#!/usr/bin/env python3
"""Shared helpers for agent-readable article resource generation."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://stemtazoo.github.io"
SECTIONS = ("sg", "fe", "gk", "ds")
SECTION_DIRS = {section: ROOT / "pages" / section for section in SECTIONS}
SITE_DIR = ROOT / "_site"

SECTION_LABELS = {
    "sg": "情報セキュリティマネジメント試験 学習記事",
    "fe": "基本情報技術者試験 学習記事",
    "gk": "G検定 学習記事",
    "ds": "データサイエンス・Python 学習記事",
}

SECTION_DESCRIPTIONS = {
    "sg": "This file lists agent-readable Markdown versions of the SG learning articles.",
    "fe": "This file lists agent-readable Markdown versions of the FE learning articles.",
    "gk": "This file lists agent-readable Markdown versions of the G検定 learning articles.",
    "ds": "This file lists agent-readable Markdown versions of the DS and Python learning articles.",
}


@dataclass
class PageRecord:
    source_path: Path
    section: str
    front_matter: dict[str, Any]
    body: str
    warnings: list[str] = field(default_factory=list)
    excluded: bool = False
    exclusion_reason: str = ""
    markdown_path: str = ""
    markdown_url: str = ""
    canonical_url: str = ""

    @property
    def rel_source(self) -> str:
        return self.source_path.relative_to(ROOT).as_posix()

    @property
    def title(self) -> str:
        return str(self.front_matter.get("title", "")).strip()

    @property
    def description(self) -> str:
        return str(self.front_matter.get("description", "")).strip()

    @property
    def permalink(self) -> str:
        return str(self.front_matter.get("permalink", "")).strip()

    @property
    def tags(self) -> list[str]:
        value = self.front_matter.get("tags", [])
        return value if isinstance(value, list) else []

    @property
    def categories(self) -> list[str]:
        value = self.front_matter.get("categories", [])
        return value if isinstance(value, list) else []


class FrontMatterError(ValueError):
    pass


def read_text(path: Path) -> str:
    # utf-8-sig also reads ordinary UTF-8 while removing a leading BOM.
    return path.read_text(encoding="utf-8-sig")


def split_front_matter(path: Path) -> tuple[dict[str, Any], str]:
    text = read_text(path)
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text.strip() + "\n"

    end_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = index
            break
    if end_index is None:
        raise FrontMatterError("missing closing front matter delimiter")

    front_matter = parse_simple_yaml(lines[1:end_index])
    body = "\n".join(lines[end_index + 1 :]).strip() + "\n"
    return front_matter, body


def parse_simple_yaml(lines: list[str]) -> dict[str, Any]:
    data: dict[str, Any] = {}
    current_key: str | None = None
    for raw in lines:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue

        if raw.startswith("  - ") and current_key:
            data.setdefault(current_key, [])
            if isinstance(data[current_key], list):
                data[current_key].append(clean_scalar(raw[4:]))
            continue

        if raw.startswith(" ") or raw.startswith("\t"):
            continue

        if ":" not in raw:
            raise FrontMatterError(f"malformed front matter line: {raw}")

        key, value = raw.split(":", 1)
        key = key.strip()
        value = value.strip()
        current_key = key
        if value == "":
            data[key] = []
        else:
            data[key] = parse_value(value)
    return data


def parse_value(value: str) -> Any:
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [clean_scalar(item.strip()) for item in inner.split(",")]
    if value.lower() in {"true", "false"}:
        return value.lower() == "true"
    if re.fullmatch(r"-?\d+", value):
        try:
            return int(value)
        except ValueError:
            return value
    return clean_scalar(value)


def clean_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def discover_pages() -> tuple[list[PageRecord], list[dict[str, str]]]:
    pages: list[PageRecord] = []
    errors: list[dict[str, str]] = []
    for section, directory in SECTION_DIRS.items():
        for path in sorted(directory.rglob("*.md")):
            try:
                front_matter, body = split_front_matter(path)
            except (UnicodeDecodeError, FrontMatterError) as exc:
                errors.append(
                    {
                        "source_path": path.relative_to(ROOT).as_posix(),
                        "section": section,
                        "error": str(exc),
                    }
                )
                continue
            pages.append(PageRecord(path, section, front_matter, body))
    return pages, errors


def classify_page(record: PageRecord) -> PageRecord:
    status = str(record.front_matter.get("content_status", "current")).strip().lower()
    if status in {"deprecated", "superseded", "draft", "noindex"}:
        record.excluded = True
        record.exclusion_reason = f"content_status:{status}"
        return record

    if not record.permalink:
        record.excluded = True
        record.exclusion_reason = "missing permalink"
        return record

    if not valid_permalink(record.permalink, record.section):
        record.excluded = True
        record.exclusion_reason = "permalink outside section"
        return record

    rel_parts = record.source_path.relative_to(SECTION_DIRS[record.section]).parts
    if len(rel_parts) > 1:
        record.excluded = True
        record.exclusion_reason = "section utility subdirectory"
        return record

    stem = record.source_path.stem.lower()
    tags = {tag.lower() for tag in record.tags}
    if stem in {"index", "all"} or "index" in tags or "search" in tags:
        record.excluded = True
        record.exclusion_reason = "index or listing page"
        return record

    if record.section not in tags:
        record.excluded = True
        record.exclusion_reason = "missing section tag"
        return record

    if not record.title:
        record.excluded = True
        record.exclusion_reason = "missing title"
        return record

    record.canonical_url = SITE_URL + record.permalink
    record.markdown_path = permalink_to_markdown_path(record.permalink).as_posix()
    record.markdown_url = SITE_URL + record.permalink + "index.md"
    return record


def valid_permalink(permalink: str, section: str) -> bool:
    if not permalink.startswith(f"/{section}/"):
        return False
    if not permalink.endswith("/"):
        return False
    return ".." not in Path(permalink).parts


def permalink_to_markdown_path(permalink: str) -> Path:
    clean = permalink.strip("/")
    return SITE_DIR / clean / "index.md"


def clean_body(body: str, record: PageRecord) -> str:
    cleaned_lines: list[str] = []
    in_fence = False
    fence_marker = ""
    liquid_block_depth = 0
    block_tags = {"case", "capture", "comment", "for", "if", "raw", "unless"}

    for line in body.splitlines():
        stripped = line.strip()
        fence_match = re.match(r"^(```+|~~~+)", stripped)
        if fence_match:
            marker = fence_match.group(1)
            if not in_fence:
                in_fence = True
                fence_marker = marker[:3]
            elif marker.startswith(fence_marker):
                in_fence = False
            cleaned_lines.append(line)
            continue

        if in_fence:
            cleaned_lines.append(line)
            continue

        liquid_tags = re.findall(r"{%\s*([a-zA-Z_]+)\b[^%]*%}", line)
        if liquid_block_depth:
            for tag in liquid_tags:
                if tag in block_tags:
                    liquid_block_depth += 1
                elif tag.startswith("end"):
                    liquid_block_depth = max(0, liquid_block_depth - 1)
            continue

        if liquid_tags:
            record.warnings.append("unsupported Liquid construct removed")
            for tag in liquid_tags:
                if tag in block_tags:
                    liquid_block_depth += 1
                elif tag.startswith("end"):
                    liquid_block_depth = max(0, liquid_block_depth - 1)
            continue
        if stripped.startswith("<script") or stripped.startswith("</script") or stripped.startswith("<style") or stripped.startswith("</style"):
            record.warnings.append("script or style tag removed")
            continue

        rendered_line = render_known_liquid_outputs(line, record)
        if "{{" in rendered_line or "}}" in rendered_line:
            record.warnings.append("unsupported Liquid output removed")
            continue
        cleaned_lines.append(rendered_line)

    cleaned = "\n".join(cleaned_lines).strip()
    cleaned = rewrite_internal_links(cleaned)
    cleaned = remove_empty_liquid_wrappers(cleaned)
    return cleaned + "\n"


def render_known_liquid_outputs(line: str, record: PageRecord) -> str:
    line = re.sub(r"{{\s*page\.title\s*}}", record.title, line)

    def relative_url_repl(match: re.Match[str]) -> str:
        return SITE_URL + match.group("path")

    return re.sub(
        r"{{\s*(?P<quote>['\"])(?P<path>/[^'\"]*)(?P=quote)\s*\|\s*relative_url\s*}}",
        relative_url_repl,
        line,
    )


def remove_empty_liquid_wrappers(text: str) -> str:
    empty_container = re.compile(
        r"<(?P<tag>div|nav|ol|ul)\b[^>]*>\s*</(?P=tag)>",
        flags=re.IGNORECASE,
    )
    while empty_container.search(text):
        text = empty_container.sub("", text)
    return re.sub(
        r"(?m)^##[^\n]*関連記事[^\n]*\n+(?=(?:<hr\b|##\s|\Z))",
        "",
        text,
    ).strip()


def rewrite_internal_links(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        label, url = match.group(1), match.group(2)
        if url.startswith(("#", "mailto:", "http://", "https://", "data:")):
            return match.group(0)
        if url.startswith("/") and re.match(r"^/(sg|fe|gk|ds)/", url):
            return f"[{label}]({SITE_URL}{url})"
        return match.group(0)

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl, text)


def sort_key(record: PageRecord) -> tuple:
    fm = record.front_matter
    order = fm.get(f"{record.section}_order", fm.get("order", 999999))
    if not isinstance(order, int):
        try:
            order = int(str(order))
        except ValueError:
            order = 999999
    return (
        record.section,
        str(fm.get(f"{record.section}_section", fm.get("fe_section", ""))),
        str(fm.get("fe_subsection", "")),
        order,
        record.title,
        record.permalink,
    )


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
