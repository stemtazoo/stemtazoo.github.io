#!/usr/bin/env python3
"""Report FE redirect stubs and possible overlapping article bodies.

Read-only standard-library audit. A similarity match is *not* a merge decision:
compare exam use, reader intent, and unique explanations before editing pages.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
import re
import unicodedata
import zlib

ROOT = Path(__file__).resolve().parents[1]
FE_DIR = ROOT / "pages" / "fe"
FM_RE = re.compile(r"\A\ufeff?---\s*\n(.*?)\n---\s*\n", re.DOTALL)
META_REFRESH_RE = re.compile(
    r"<meta\b[^>]*\bhttp-equiv\s*=\s*['\"]?refresh['\"]?[^>]*>",
    re.IGNORECASE | re.DOTALL,
)
REDIRECT_URL_RE = re.compile(r"\burl\s*=\s*(?:\{\{\s*)?['\"]?(/fe/[\w/-]+/)", re.IGNORECASE)
FENCE_RE = re.compile(r"^\s*(```|~~~)")
LINK_RE = re.compile(r"\[([^]]+)\]\([^)]*\)")
HTML_RE = re.compile(r"<[^>]+>")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s")
TABLE_RULE_RE = re.compile(r"^\s*\|?\s*[-:]+(?:\s*\|\s*[-:]+)+\s*\|?\s*$")


@dataclass
class Page:
    path: Path
    title: str
    permalink: str
    redirect: bool
    target: str | None
    fingerprints: set[int]


def split_frontmatter(content: str) -> tuple[dict[str, str], str]:
    match = FM_RE.match(content)
    if not match:
        return {}, content
    props: dict[str, str] = {}
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep and not line[:1].isspace():
            props[key.strip()] = value.strip().strip("\"'")
    return props, content[match.end():]


def plain_lines(body: str) -> list[str]:
    lines: list[str] = []
    fence: str | None = None
    in_html_comment = False
    for raw in body.splitlines():
        line = raw.strip()
        if in_html_comment:
            if "-->" in line:
                in_html_comment = False
            continue
        if line.startswith("<!--"):
            in_html_comment = "-->" not in line
            continue
        match = FENCE_RE.match(line)
        if match:
            marker = match.group(1)[:3]
            if fence is None:
                fence = marker
            elif marker == fence:
                fence = None
            continue
        if fence or not line or HEADING_RE.match(line) or TABLE_RULE_RE.match(line):
            continue
        if line.startswith(("{%", "{{", "<script", "<style")):
            continue
        line = LINK_RE.sub(r"\1", line)
        line = HTML_RE.sub("", line)
        line = unicodedata.normalize("NFKC", line).casefold()
        line = re.sub(r"[^\w]+", "", line, flags=re.UNICODE)
        if len(line) >= 18:
            lines.append(line)
    return lines


def fingerprints(body: str, width: int = 9) -> set[int]:
    """Stable, sparsely sampled Japanese character n-grams (not title matching)."""
    result: set[int] = set()
    for line in plain_lines(body):
        for i in range(len(line) - width + 1):
            checksum = zlib.crc32(line[i:i + width].encode("utf-8"))
            if checksum % 3 == 0:
                result.add(checksum)
    return result


def read_pages(directory: Path) -> list[Page]:
    pages: list[Page] = []
    for path in sorted(directory.rglob("*.md")):
        content = path.read_text(encoding="utf-8-sig")
        front, body = split_frontmatter(content)
        is_redirect = front.get("layout", "").lower() == "null" and bool(META_REFRESH_RE.search(body))
        target_match = REDIRECT_URL_RE.search(body) if is_redirect else None
        pages.append(Page(
            path=path,
            title=front.get("title", path.stem),
            permalink=front.get("permalink", ""),
            redirect=is_redirect,
            target=target_match.group(1) if target_match else None,
            fingerprints=set() if is_redirect else fingerprints(body),
        ))
    return pages


def candidate_pairs(
    pages: list[Page], min_rare_shared: int = 12, min_overlap: float = 0.22,
    max_document_frequency: int = 24,
) -> list[tuple[int, int, int, float, float]]:
    """Rank by containment; cap common boilerplate grams at 24 documents."""
    article_ids = [i for i, page in enumerate(pages) if not page.redirect and page.fingerprints]
    postings: dict[int, list[int]] = defaultdict(list)
    for i in article_ids:
        for fp in pages[i].fingerprints:
            postings[fp].append(i)

    rare_shared: Counter[tuple[int, int]] = Counter()
    for owners in postings.values():
        if 2 <= len(owners) <= max_document_frequency:
            for x, i in enumerate(owners):
                for j in owners[x + 1:]:
                    rare_shared[(i, j)] += 1

    results = []
    for (i, j), rare in rare_shared.items():
        if rare < min_rare_shared:
            continue
        left, right = pages[i].fingerprints, pages[j].fingerprints
        intersection = len(left & right)
        containment = intersection / min(len(left), len(right))
        if containment < min_overlap:
            continue
        jaccard = intersection / len(left | right)
        results.append((i, j, intersection, containment, jaccard))
    results.sort(key=lambda r: (-r[3], -r[4], -r[2], pages[r[0]].path.as_posix(), pages[r[1]].path.as_posix()))
    return results


def display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def report(pages: list[Page], pairs: list[tuple[int, int, int, float, float]], top: int) -> str:
    redirects = [p for p in pages if p.redirect]
    articles = [p for p in pages if not p.redirect]
    urls = {p.permalink for p in articles if p.permalink}
    missing = [p for p in redirects if p.target and p.target not in urls]
    lines = [
        "# FE本文重複・転送ページ候補（自動監査）", "",
        "これは候補抽出結果です。**類似度のみで記事を統合しないでください。**", "",
        "## 集計", "",
        f"- Markdown総数: **{len(pages)}件**",
        f"- HTML meta refresh転送専用ページ: **{len(redirects)}件**",
        f"- 実記事（転送専用ページを除く）: **{len(articles)}件**",
        f"- 類似候補: **{len(pairs)}組**（表示は上位{min(top, len(pairs))}組）",
        f"- 転送先の実記事permalinkと一致しない転送: **{len(missing)}件**（手動確認）", "",
        "## 類似候補（本文の9文字連続片に基づく）", "",
        "| 小さい方に対する重複率 | Jaccard | 共通片 | 記事A | 記事B |", "|---:|---:|---:|---|---|",
    ]
    for i, j, shared, overlap, jaccard in pairs[:top]:
        a, b = pages[i], pages[j]
        lines.append(f"| {overlap:.1%} | {jaccard:.1%} | {shared} | `{display_path(a.path)}` | `{display_path(b.path)}` |")
    if not pairs:
        lines.append("| — | — | — | 候補なし | — |")
    lines += ["", "## 転送専用ページ", "", "| 転送元 | 転送先 |", "|---|---|"]
    for p in redirects:
        lines.append(f"| `{display_path(p.path)}` | `{p.target or '対象URLを自動抽出できず'}` |")
    if missing:
        lines += ["", "## 転送先の要確認", ""]
        lines += [f"- `{display_path(p.path)}` → `{p.target}`" for p in missing]
    lines += [
        "", "## 判定と再現方法", "",
        "- 転送: `layout: null` と HTML `meta http-equiv=refresh` を本文で両方確認。ファイルサイズでは判定しない。",
        "- 類似: front matter、見出し、コードブロック、リンク先URLを除いた本文から9文字片を抽出し、約3分の1を安定サンプリング。",
        "- 広く使われる定型表現を抑制するため、25記事以上に出る文字片は候補生成で除外する。",
        "- 重複率は『小さい記事の特徴片のうち共通する割合』。Jaccardは『共通片 ÷ 両記事の特徴片の和集合』。",
        "- 比較の漏れ、一般的な用語・定型文による誤検知がある。**検索意図・独自例・科目A/Bの判断基準を読んで最終判定する。**", "",
        "```bash", "python scripts/audit_fe_duplicate_content.py --output docs/audits/fe-duplicate-candidates.md", "```", "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, default=FE_DIR)
    parser.add_argument("--output", type=Path, help="Write Markdown report to path; otherwise print summary")
    parser.add_argument("--top", type=int, default=100)
    parser.add_argument("--min-rare-shared", type=int, default=12)
    parser.add_argument("--min-overlap", type=float, default=0.22)
    args = parser.parse_args()
    if not args.directory.is_dir():
        parser.error(f"article directory not found: {args.directory}")
    pages = read_pages(args.directory)
    pairs = candidate_pairs(pages, min_rare_shared=args.min_rare_shared, min_overlap=args.min_overlap)
    redirects = sum(page.redirect for page in pages)
    print(f"files={len(pages)} redirects={redirects} articles={len(pages)-redirects} candidates={len(pairs)}")
    if args.output:
        output = args.output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(report(pages, pairs, args.top), encoding="utf-8")
        print(f"wrote={output}")
    else:
        for i, j, shared, overlap, _ in pairs[:args.top]:
            print(f"{overlap:.1%}\t{shared}\t{pages[i].path}\t{pages[j].path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
