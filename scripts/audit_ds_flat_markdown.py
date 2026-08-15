#!/usr/bin/env python3
"""Audit DS Markdown articles for visually flat body structure.

This complements structural/front-matter audits. It looks for Markdown that is
syntactically valid but likely renders as a long sequence of plain text lines,
for example pseudo-tables, naked numbered labels, and list-like short lines.

The audit intentionally favors precision over recall. It is a candidate finder,
not an automatic rewrite signal, so healthy prose, formulas, and intentionally
compact teaching examples should not score highly on their own.

Usage:
    python scripts/audit_ds_flat_markdown.py
    python scripts/audit_ds_flat_markdown.py --output docs/audits/ds-flat-markdown-audit.md
    python scripts/audit_ds_flat_markdown.py --min-score 4
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DS_DIR = ROOT / "pages" / "ds"
DEFAULT_OUTPUT = ROOT / "docs" / "audits" / "ds-flat-markdown-audit.md"

STANDARD_H2 = {
    "まず結論",
    "直感的な説明",
    "定義・仕組み",
    "どんな場面で使う？",
    "よくある誤解・混同",
    "まとめ（試験直前用）",
}

STRUCTURAL_PREFIXES = (
    "#",
    "- ",
    "* ",
    "+ ",
    ">",
    "|",
    "```",
    "~~~",
    "<",
    "{%",
    "{{",
)

CIRCLED_RE = re.compile(r"^[①②③④⑤⑥⑦⑧⑨⑩]\s*\S+")
NUMBER_LABEL_RE = re.compile(r"^(?:誤解|ポイント|注意|特徴|例)[①②③④⑤⑥⑦⑧⑨⑩0-9]+(?:[：:]|\s|$)")
ARROW_ONLY_RE = re.compile(r"^[↓↑⇄⇔]+$")
TABULAR_RE = re.compile(r"\S+\t+\S+")
MARKDOWN_ORDERED_RE = re.compile(r"^\d+[.)]\s+")
LINK_DEF_RE = re.compile(r"^\[[^]]+\]:\s+")
MATHISH_RE = re.compile(r"^[A-Za-z0-9_{}^\\+\-*/=()\[\].,|\s]+$")

LABEL_WORDS = {
    "意味",
    "特徴",
    "覚えるポイント",
    "ポイント",
    "説明変数",
    "目的変数",
    "値の範囲",
    "使う場面",
    "判断基準",
}


@dataclass
class Finding:
    kind: str
    line: int
    excerpt: str
    points: int


@dataclass
class ArticleAudit:
    path: Path
    score: int = 0
    findings: list[Finding] = field(default_factory=list)

    @property
    def priority(self) -> str:
        if self.score >= 10:
            return "高"
        if self.score >= 6:
            return "中"
        return "低"


def strip_front_matter(lines: list[str]) -> tuple[list[str], int]:
    if not lines or lines[0].lstrip("\ufeff").strip() != "---":
        return lines, 0
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return lines[i + 1 :], i + 1
    return lines, 0


def is_plain(line: str) -> bool:
    s = line.strip()
    if not s:
        return False
    if s.startswith(STRUCTURAL_PREFIXES):
        return False
    if MARKDOWN_ORDERED_RE.match(s) or LINK_DEF_RE.match(s):
        return False
    if s in {"---", "***", "___", "$$"}:
        return False
    return True


def is_label_like_circled_line(s: str) -> bool:
    """Return True for compact circled-number labels, not normal prose."""
    if not CIRCLED_RE.match(s):
        return False
    if len(s) > 36:
        return False
    if re.search(r"[。！？]$", s):
        return False
    if "とは、" in s or "は、" in s:
        return False
    return True


def is_short_plain_candidate(line: str) -> bool:
    """Identify compact prose likely to be a list item rather than a sentence."""
    s = line.strip()
    if not is_plain(line) or len(s) > 28:
        return False
    if s.startswith(("http://", "https://")):
        return False
    if re.search(r"[。.!?！？、,:：；;]$", s):
        return False
    # Formula fragments such as `A =` or `A^{-1} =` should not make an
    # otherwise structured statistics article look visually flat.
    if MATHISH_RE.fullmatch(s) and re.search(r"[=^{}\\]", s):
        return False
    return True


def add(audit: ArticleAudit, kind: str, line: int, excerpt: str, points: int) -> None:
    # Avoid flooding one article with the same heuristic. Multiple independent
    # signals are more useful than dozens of repeated short-line warnings.
    same_kind = sum(1 for f in audit.findings if f.kind == kind)
    limits = {
        "短い通常行の連続": 3,
        "裸の番号付きラベル": 4,
        "裸の説明ラベル": 3,
        "矢印チェーン": 2,
        "タブ区切り擬似表": 3,
        "構造要素が少ない長文": 1,
    }
    if same_kind >= limits.get(kind, 3):
        return
    audit.findings.append(Finding(kind, line, excerpt[:90], points))
    audit.score += points


def audit_file(path: Path) -> ArticleAudit:
    raw_lines = path.read_text(encoding="utf-8-sig").splitlines()
    body, offset = strip_front_matter(raw_lines)
    audit = ArticleAudit(path=path)

    in_fence = False
    content_lines = 0
    structural_lines = 0
    plain_short_run: list[tuple[int, str]] = []
    blank_count = 0

    def flush_short_run() -> None:
        nonlocal plain_short_run
        # Four compact items is a stronger signal than three prose fragments.
        # Severe flat articles still trigger, while ordinary teaching prose is
        # less likely to be reported merely because of intentional line breaks.
        if len(plain_short_run) >= 4:
            line_no, sample = plain_short_run[0]
            add(audit, "短い通常行の連続", line_no, sample, 2)
        plain_short_run = []

    for idx, line in enumerate(body, start=offset + 1):
        s = line.strip()
        if s.startswith(("```", "~~~")):
            in_fence = not in_fence
            flush_short_run()
            blank_count = 0
            continue
        if in_fence:
            continue

        if not s:
            blank_count += 1
            # A single blank line is common inside visually-flat pseudo-lists,
            # but two or more blanks usually separate prose blocks.
            if blank_count >= 2:
                flush_short_run()
            continue

        blank_count = 0
        content_lines += 1
        if (
            s.startswith(STRUCTURAL_PREFIXES)
            or MARKDOWN_ORDERED_RE.match(s)
            or "**" in s
            or s.startswith("$$")
        ):
            structural_lines += 1

        if TABULAR_RE.search(line) and not s.startswith("|"):
            add(audit, "タブ区切り擬似表", idx, s, 4)

        if is_label_like_circled_line(s) and not s.startswith("#"):
            add(audit, "裸の番号付きラベル", idx, s, 2)

        if NUMBER_LABEL_RE.match(s) and not s.startswith("#"):
            add(audit, "裸の番号付きラベル", idx, s, 2)

        if s in LABEL_WORDS:
            add(audit, "裸の説明ラベル", idx, s, 1)

        if ARROW_ONLY_RE.match(s):
            add(audit, "矢印チェーン", idx, s, 1)

        if is_short_plain_candidate(line):
            plain_short_run.append((idx, s))
        else:
            flush_short_run()

    flush_short_run()

    # Long articles with almost no Markdown structure are often visually flat.
    if content_lines >= 45:
        ratio = structural_lines / max(content_lines, 1)
        if ratio < 0.10:
            add(
                audit,
                "構造要素が少ない長文",
                offset + 1,
                f"構造行率 {ratio:.1%} ({structural_lines}/{content_lines})",
                4,
            )
        elif ratio < 0.16:
            add(
                audit,
                "構造要素が少ない長文",
                offset + 1,
                f"構造行率 {ratio:.1%} ({structural_lines}/{content_lines})",
                2,
            )

    return audit


def build_report(audits: list[ArticleAudit], checked: int, min_score: int) -> str:
    candidates = [a for a in audits if a.score >= min_score]
    candidates.sort(key=lambda a: (-a.score, str(a.path)))

    high = sum(a.priority == "高" for a in candidates)
    medium = sum(a.priority == "中" for a in candidates)
    low = sum(a.priority == "低" for a in candidates)

    lines = [
        "# DS記事 平坦Markdown監査レポート",
        "",
        "## 1. サマリー",
        "",
        f"- 対象: `pages/ds/**/*.md`",
        f"- チェックしたDS Markdownファイル数: **{checked}**",
        f"- 候補数（score >= {min_score}）: **{len(candidates)}件**（高: **{high}件** / 中: **{medium}件** / 低: **{low}件**）",
        "- 目的: Markdown文法としては有効でも、箇条書き・表・小見出しが不足して本文が『ただの文字』に見える記事を抽出する。",
        "- 注意: 自動判定は修正対象の確定ではない。まとめ記事・短い定義列など、意図した表現も候補に含まれるため、編集前に目視確認する。",
        "",
        "## 2. 判定シグナル",
        "",
        "- 4行以上の短い通常テキストが連続し、箇条書き候補に見える",
        "- タブ区切りの擬似表がMarkdown表になっていない",
        "- `①` `②` や `誤解①` などの短いラベルが小見出しになっていない",
        "- `↓` などの矢印だけで構造を表現している",
        "- `特徴` `意味` `覚えるポイント` などのラベルが通常テキストのまま",
        "- 長い本文に対して見出し・箇条書き・表・強調などの構造要素が少ない",
        "",
        "## 3. 優先度付き候補",
        "",
        "| 優先度 | score | ファイル | 主な検出理由 |",
        "|---|---:|---|---|",
    ]

    for audit in candidates:
        reasons = "; ".join(
            f"{f.kind} (L{f.line}: `{f.excerpt.replace('|', '｜')}`)"
            for f in audit.findings[:4]
        )
        rel = audit.path.relative_to(ROOT).as_posix()
        lines.append(f"| {audit.priority} | {audit.score} | `{rel}` | {reasons} |")

    lines += [
        "",
        "## 4. 読み方",
        "",
        "- **高**: 複数の強いシグナルが重なっている。優先して目視確認する。",
        "- **中**: 一部セクションが平坦な可能性がある。該当行周辺を確認する。",
        "- **低**: 軽微な表記・装飾候補。記事全体が読みやすければ修正不要。",
        "",
        "## 5. 推奨修正方針",
        "",
        "1. 内容や説明粒度を変えず、まずMarkdown構造だけを正常化する。",
        "2. 並列項目は箇条書き、比較は表、節の役割を持つ行は `###` 小見出しにする。",
        "3. 試験の判断基準は太字で強調するが、強調しすぎない。",
        "4. 通常のDS記事では標準6見出しを維持し、まとめ記事は役割に合った構造を優先する。",
        "5. 自動監査のscoreだけで一括書き換えせず、必ず記事ごとに目視確認する。",
        "",
        "## 6. 実行方法",
        "",
        "```bash",
        "python scripts/audit_ds_flat_markdown.py",
        "```",
        "",
        "閾値を変更する場合:",
        "",
        "```bash",
        "python scripts/audit_ds_flat_markdown.py --min-score 6",
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--min-score", type=int, default=4)
    parser.add_argument("--no-write", action="store_true", help="Print summary only")
    args = parser.parse_args()

    paths = sorted(DS_DIR.rglob("*.md"))
    audits = [audit_file(path) for path in paths]
    report = build_report(audits, len(paths), args.min_score)

    candidates = [a for a in audits if a.score >= args.min_score]
    print(f"checked={len(paths)} candidates={len(candidates)}")
    for audit in sorted(candidates, key=lambda a: (-a.score, str(a.path)))[:20]:
        print(f"{audit.priority}\t{audit.score}\t{audit.path.relative_to(ROOT)}")

    if not args.no_write:
        output = args.output
        if not output.is_absolute():
            output = ROOT / output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(report + "\n", encoding="utf-8")
        print(f"wrote={output.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
