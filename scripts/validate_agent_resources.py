#!/usr/bin/env python3
"""Validate generated agent-readable resources."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

from agent_resource_lib import ROOT, SECTIONS, SITE_DIR, SITE_URL


MANIFEST_PATH = SITE_DIR / "agent-resources-manifest.json"


def load_manifest() -> dict:
    if not MANIFEST_PATH.exists():
        raise FileNotFoundError(f"missing manifest: {MANIFEST_PATH.relative_to(ROOT)}")
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    try:
        manifest = load_manifest()
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1

    entries = manifest.get("included", [])
    parse_errors = manifest.get("parse_errors", [])
    for item in parse_errors:
        errors.append(f"malformed source front matter: {item.get('source_path')} ({item.get('error')})")

    markdown_paths = [item.get("markdown_path", "") for item in entries]
    canonical_urls = [item.get("canonical_url", "") for item in entries]
    markdown_urls = [item.get("markdown_url", "") for item in entries]

    for duplicate, count in duplicated(markdown_paths).items():
        errors.append(f"duplicate generated Markdown path ({count}): {duplicate}")
    for duplicate, count in duplicated(canonical_urls).items():
        errors.append(f"duplicate canonical URL ({count}): {duplicate}")
    for duplicate, count in duplicated(markdown_urls).items():
        errors.append(f"duplicate Markdown URL ({count}): {duplicate}")

    for item in entries:
        source = item.get("source_path", "")
        title = item.get("title", "")
        permalink = item.get("permalink", "")
        path_text = item.get("markdown_path", "")
        markdown_url = item.get("markdown_url", "")
        if not title:
            errors.append(f"included article has no title: {source}")
        if not permalink or not permalink.startswith(f"/{item.get('section')}/") or not permalink.endswith("/"):
            errors.append(f"included article has invalid permalink: {source} ({permalink})")
        if "../" in path_text or "..\\" in path_text:
            errors.append(f"generated path contains traversal: {path_text}")
        path = ROOT / path_text
        try:
            path.resolve().relative_to(SITE_DIR.resolve())
        except ValueError:
            errors.append(f"generated path escapes _site: {path_text}")
        if not path.exists():
            errors.append(f"generated Markdown file missing: {path_text}")
        else:
            try:
                path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                errors.append(f"generated Markdown is not valid UTF-8: {path_text}")
        html_path = path.with_suffix(".html")
        if path == html_path:
            errors.append(f"generated Markdown would overwrite HTML: {path_text}")
        if not markdown_url.endswith("/index.md") or not markdown_url.startswith(SITE_URL):
            errors.append(f"invalid generated Markdown URL: {markdown_url}")
        for warning in item.get("warnings", []):
            warnings.append(f"{source}: {warning}")
        if not item.get("description"):
            warnings.append(f"{source}: missing description")
        elif len(item.get("description", "")) < 40:
            warnings.append(f"{source}: description is very short")

    for section in SECTIONS:
        section_file = SITE_DIR / section / "llms.txt"
        if not section_file.exists():
            errors.append(f"missing section llms.txt: _site/{section}/llms.txt")
            continue
        text = section_file.read_text(encoding="utf-8")
        linked = re.findall(r"\((https://stemtazoo\.github\.io/[^)]+/index\.md)\)", text)
        for url in linked:
            rel = url.removeprefix(SITE_URL).strip("/")
            if not (SITE_DIR / rel).exists():
                errors.append(f"section llms.txt points to missing index.md: {url}")
        if section == "fe" and not linked:
            errors.append("/fe/llms.txt has no article links")

    root_llms = ROOT / "llms.txt"
    root_text = root_llms.read_text(encoding="utf-8")
    for section in SECTIONS:
        expected = f"{SITE_URL}/{section}/llms.txt"
        if expected not in root_text:
            errors.append(f"root llms.txt missing section discovery link: {expected}")

    # Validate generated-resource alternate links in representative built HTML.
    for item in entries[:50]:
        permalink = item.get("permalink", "")
        html_path = SITE_DIR / permalink.strip("/") / "index.html"
        if html_path.exists():
            html = html_path.read_text(encoding="utf-8", errors="replace")
            expected_href = item.get("markdown_url", "")
            if 'rel="alternate"' not in html or expected_href not in html:
                errors.append(f"article page does not advertise generated Markdown alternate: {permalink}")

    if warnings:
        print("Warnings:")
        for warning in warnings[:200]:
            print(f"- {warning}")
        if len(warnings) > 200:
            print(f"- ... {len(warnings) - 200} more warnings")

    if errors:
        print("Errors:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Agent resources valid: {len(entries)} generated Markdown files.")
    return 0


def duplicated(values: list[str]) -> dict[str, int]:
    counts = Counter(value for value in values if value)
    return {value: count for value, count in counts.items() if count > 1}


if __name__ == "__main__":
    raise SystemExit(main())

