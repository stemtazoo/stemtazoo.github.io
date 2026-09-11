#!/usr/bin/env python3
"""Migrate manually reviewed legacy DS skill blocks to official ver.6 items.

Mappings are explicit filename -> official ver.6 item_id (or item_id tuple) pairs.
Reviewed supplemental topics are also supported when the article remains useful
but the ver.6 ★1 list has no direct item for the same theme. Already-migrated
mappings are accepted so the script remains idempotent.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DS_DIR = ROOT / "pages" / "ds"
DATA = ROOT / "data" / "skillcheck" / "exports" / "exam_star1_latest.json"

REVIEWED: dict[str, str | tuple[str, ...] | None] = {
    "nosql.md": "dataengineering-0069",
    "spark.md": "dataengineering-0068",
    "yarn.md": "dataengineering-0068",
    "visualization-basic-perspectives.md": "datascience-0153",
    "malware.md": "foundation-0032",
    "rdb-vs-nosql.md": "dataengineering-0069",
    "analysis-approach-selection.md": "datascience-0075",
    "causal-inference.md": "datascience-0017",
    "bcp.md": "value-creation-0049",
    "risk-management.md": "value-creation-0049",
    "operational-risk.md": "value-creation-0049",
    "incident-management.md": "value-creation-0049",
    "data-mart.md": "dataengineering-0080",
    "data-warehouse-vs-datamart.md": "dataengineering-0080",
    "analysis-approach-design.md": "foundation-0002",
    "revenue-equation.md": "foundation-0016",
    "hallucination.md": ("foundation-0017", "foundation-0018"),
    "kpi-kgi.md": "foundation-0016",
    "poc-concept-proof.md": "value-creation-0037",
    "pdca-cycle.md": "value-creation-0115",
    "pest-analysis.md": "value-creation-0001",
    "five-forces-analysis.md": "value-creation-0031",
    "swot-analysis.md": "value-creation-0031",
    "internal-control.md": "value-creation-0052",
    "data-governance.md": "value-creation-0052",
    "governance.md": "value-creation-0094",
    "customer-journey.md": "value-creation-0010",
    "design-thinking.md": "value-creation-0016",
    "open-data.md": "dataengineering-0001",
    "managed-service.md": "dataengineering-0022",
    "opt-out.md": "foundation-0008",
    "data-driven-management.md": "foundation-0001",
    "data-literacy.md": "foundation-0001",
    "why-structure.md": "foundation-0012",
    "sora-ame-kasa.md": "foundation-0003",
    "gdpr.md": "foundation-0008",
    "eda.md": "datascience-0153",
    # Reviewed supplemental topics: useful learning pages without a direct
    # same-theme item in the ver.6 ★1 list.
    "agile-development.md": None,
    "critical-path.md": None,
    "gantt-chart.md": None,
    "project-management.md": None,
    "scrum.md": None,
    "wbs.md": None,
    "paper-structure.md": None,
    "anchoring-effect.md": None,
    "availability-heuristic.md": None,
    "cognitive-bias.md": None,
    "confirmation-bias.md": None,
    "dunning-kruger-effect.md": None,
    "compliance-risk.md": None,
    "contract-ukeoi-juninin.md": None,
    "ab-test.md": None,
    "bi-tool-functions.md": None,
    "hot-cool-archive.md": None,
    "elsi.md": None,
    "human-centered-ai-principles.md": None,
    "bi-operations-cheatsheet.md": None,
    "data-cube.md": None,
    "drilldown-drillup.md": None,
    "drillthrough.md": None,
    "filter.md": None,
    "olap.md": None,
    "pivot.md": None,
    "slice-dice.md": None,
    "deviation-score.md": "datascience-0109",
    "random-sampling-methods.md": "datascience-0101",
    "regular-expression-summary.md": "dataengineering-0086",
    "statistics-overview.md": ("datascience-0013", "datascience-0017"),
    "statistics-summary.md": ("datascience-0013", "datascience-0017"),
    "average-methods-comparison.md": None,
    "categorical-variable.md": None,
    "data-transformation.md": None,
    "estimator-properties.md": None,
    "euclidean-norm.md": None,
    "feature.md": None,
    "rfm-analysis.md": None,
    "sampling-methods-comparison.md": None,
    "mapping.md": None,
    "data-extraction-vs-aggregation.md": "dataengineering-0135",
    "left-join-where.md": "dataengineering-0135",
    "regular-expression-email.md": "dataengineering-0086",
    "regular-expression-postalcode.md": "dataengineering-0086",
    "rest-api-methods.md": "dataengineering-0096",
    "self-join.md": "dataengineering-0135",
    "sql-count-diff.md": "dataengineering-0135",
    "sql-distinct.md": "dataengineering-0135",
    "sql-exists.md": "dataengineering-0135",
    "sql-filtering.md": "dataengineering-0135",
    "sql-in-exists.md": "dataengineering-0135",
    "sql-union.md": "dataengineering-0135",
    "sql-where.md": "dataengineering-0135",
    "batch-vs-stream.md": None,
    "etl.md": None,
    "ftp-ssh.md": None,
    "rest-api.md": None,
    "soap.md": None,
    "web-api.md": None,
    "web-crawling-scraping.md": None,
}

SUPPLEMENTAL: dict[str, tuple[str, str, str]] = {
    "agile-development.md": ("value-creation", "project-management", "プロジェクト推進の補助学習"),
    "critical-path.md": ("value-creation", "project-management", "プロジェクト推進の補助学習"),
    "gantt-chart.md": ("value-creation", "project-management", "プロジェクト推進の補助学習"),
    "project-management.md": ("value-creation", "project-management", "プロジェクト推進の補助学習"),
    "scrum.md": ("value-creation", "project-management", "プロジェクト推進の補助学習"),
    "wbs.md": ("value-creation", "project-management", "プロジェクト推進の補助学習"),
    "paper-structure.md": ("foundation", "logical-thinking", "論理的な文章構成の補助学習"),
    "anchoring-effect.md": ("foundation", "logical-thinking", "認知バイアスの補助学習"),
    "availability-heuristic.md": ("foundation", "logical-thinking", "認知バイアスの補助学習"),
    "cognitive-bias.md": ("foundation", "logical-thinking", "認知バイアスの補助学習"),
    "confirmation-bias.md": ("foundation", "logical-thinking", "認知バイアスの補助学習"),
    "dunning-kruger-effect.md": ("foundation", "logical-thinking", "認知バイアスの補助学習"),
    "compliance-risk.md": ("foundation", "action-norms", "コンプライアンス・リスクの補助学習"),
    "contract-ukeoi-juninin.md": ("foundation", "action-norms", "契約形態の補助学習"),
    "ab-test.md": ("datascience", "statistics", "実験・効果検証の補助学習"),
    "bi-tool-functions.md": ("datascience", "data-understanding", "BI・データ活用の補助学習"),
    "hot-cool-archive.md": ("dataengineering", "data-storage", "ストレージ階層設計の補助学習"),
    "elsi.md": ("foundation", "action-norms", "倫理・法・社会課題の補助学習"),
    "human-centered-ai-principles.md": ("foundation", "action-norms", "人間中心のAI原則の補助学習"),
    "bi-operations-cheatsheet.md": ("datascience", "visualization", "BI・OLAP操作の補助学習"),
    "data-cube.md": ("datascience", "data-understanding", "OLAP・多次元分析の補助学習"),
    "drilldown-drillup.md": ("datascience", "visualization", "BI・OLAP操作の補助学習"),
    "drillthrough.md": ("datascience", "visualization", "BI・OLAP操作の補助学習"),
    "filter.md": ("datascience", "data-understanding", "BI・データ抽出操作の補助学習"),
    "olap.md": ("datascience", "data-understanding", "OLAP・多次元分析の補助学習"),
    "pivot.md": ("datascience", "visualization", "BI・集計操作の補助学習"),
    "slice-dice.md": ("datascience", "visualization", "BI・OLAP操作の補助学習"),
    "average-methods-comparison.md": ("datascience", "modeling", "分類評価指標の補助学習"),
    "categorical-variable.md": ("datascience", "data-preparation", "カテゴリ変数理解の補助学習"),
    "data-transformation.md": ("datascience", "data-preparation", "データ変換全般の補助学習"),
    "estimator-properties.md": ("datascience", "statistics", "推定量の性質の補助学習"),
    "euclidean-norm.md": ("datascience", "linear-algebra", "ベクトルのノルムの補助学習"),
    "feature.md": ("datascience", "data-preparation", "特徴量の基礎概念の補助学習"),
    "rfm-analysis.md": ("datascience", "modeling", "顧客分析手法の補助学習"),
    "sampling-methods-comparison.md": ("datascience", "data-preparation", "標本抽出法の補助学習"),
    "mapping.md": ("dataengineering", "data-processing", "値の対応付け・変換の補助学習"),
    "batch-vs-stream.md": ("dataengineering", "data-processing", "バッチ処理・ストリーム処理の補助学習"),
    "etl.md": ("dataengineering", "data-collection", "ETL・データ統合の補助学習"),
    "ftp-ssh.md": ("dataengineering", "data-collection", "ファイル転送・安全な通信の補助学習"),
    "rest-api.md": ("dataengineering", "data-collection", "REST API設計概念の補助学習"),
    "soap.md": ("dataengineering", "data-processing", "SOAP・Webサービス通信の補助学習"),
    "web-api.md": ("dataengineering", "data-collection", "Web API基礎概念の補助学習"),
    "web-crawling-scraping.md": ("dataengineering", "data-collection", "Webデータ収集手法の補助学習"),
}

METADATA_CORRECTIONS: dict[str, tuple[tuple[str, str], tuple[str, str]]] = {
    "regular-expression-summary.md": (
        ("datascience", "unstructured-data"),
        ("dataengineering", "data-processing"),
    ),
}

LEGACY_LABELS = (
    "ビジネス力シート",
    "AI利活用スキルシート",
    "データサイエンス力シート",
    "データエンジニアリング力シート",
)
AREA_LABEL = {
    "foundation": "基盤",
    "value-creation": "価値創造",
    "datascience": "データサイエンス",
    "dataengineering": "データエンジニアリング",
}
AREA_PAGE = {
    "foundation": "/ds/foundation-skillcheck/",
    "value-creation": "/ds/value-creation-skillcheck/",
    "datascience": "/ds/datascience-skillcheck/",
    "dataengineering": "/ds/engineering-skillcheck/",
}
HEADING_RE = re.compile(
    r"^## 対応スキル項目（(?:" + "|".join(map(re.escape, LEGACY_LABELS)) + r")）\s*$",
    re.MULTILINE,
)


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def front_matter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"')
    return data


def bounds(text: str, match: re.Match[str]) -> tuple[int, int]:
    after = match.end()
    nxt = re.search(r"^##\s+", text[after:], re.MULTILINE)
    end = after + nxt.start() if nxt else len(text)
    return match.start(), end


def canonical_block(rows: list[dict[str, str]]) -> str:
    first = rows[0]
    area = first["area"]
    lines = [f"## 対応スキル項目（ver.6 {AREA_LABEL[area]}）", ""]

    common_fields = (
        ("phase", "フェーズ"),
        ("section", "分類"),
        ("category", "スキルカテゴリ"),
        ("subcategory", "サブカテゴリ"),
    )
    for key, label in common_fields:
        values = {normalize(row.get(key, "")) for row in rows if normalize(row.get(key, ""))}
        if len(values) == 1:
            lines.append(f"- **{label}**：{next(iter(values))}")

    if len(rows) == 1:
        required = normalize(first.get("required_skill", "")) or "—"
        lines.extend([
            f"- **必須スキル**：{required}",
            f"- ★ {normalize(first['item'])}",
        ])
    else:
        for row in rows:
            required = normalize(row.get("required_skill", "")) or "—"
            lines.append(f"- ★ {normalize(row['item'])}（必須スキル：{required}）")

    lines.extend([
        f"- [ver.6 ★1スキルチェックで確認する]({AREA_PAGE[area]})",
        "",
    ])
    return "\n".join(lines)


def supplemental_block(area: str, position: str) -> str:
    return "\n".join([
        f"## 対応スキル項目（ver.6 {AREA_LABEL[area]}）",
        "",
        f"- **位置づけ**：{position}",
        "- **★1直接対応**：なし",
        "- 旧ver.5では対応項目がありましたが、ver.6の★1一覧には同一テーマの直接項目として掲載されていません。試験理解を補う関連テーマとして整理します。",
        f"- [ver.6 ★1スキルチェックで確認する]({AREA_PAGE[area]})",
        "",
    ])


def mapping_ids(value: str | tuple[str, ...] | None) -> tuple[str, ...]:
    if value is None:
        return ()
    return (value,) if isinstance(value, str) else tuple(value)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    rows = json.loads(DATA.read_text(encoding="utf-8"))
    by_id = {row["item_id"]: row for row in rows}
    changed: list[str] = []
    already: list[str] = []

    for filename, mapping in REVIEWED.items():
        path = DS_DIR / filename
        text = path.read_text(encoding="utf-8-sig")
        meta = front_matter(text)

        correction = METADATA_CORRECTIONS.get(filename)
        if correction:
            source, target = correction
            current = (meta.get("ds_area", ""), meta.get("ds_section", ""))
            if current == source:
                text = re.sub(
                    r"^ds_area:\s*.*$", f"ds_area: {target[0]}", text,
                    count=1, flags=re.MULTILINE,
                )
                text = re.sub(
                    r"^ds_section:\s*.*$", f"ds_section: {target[1]}", text,
                    count=1, flags=re.MULTILINE,
                )
                meta = front_matter(text)
            elif current != target:
                raise SystemExit(
                    f"{filename}: unexpected metadata {current}; "
                    f"expected {source} or {target}"
                )

        if mapping is None:
            supplemental = SUPPLEMENTAL.get(filename)
            if not supplemental:
                raise SystemExit(f"{filename}: supplemental metadata is not configured")
            area, section, position = supplemental
            if meta.get("ds_area") != area or meta.get("ds_section") != section:
                raise SystemExit(
                    f"{filename}: supplemental metadata mismatch "
                    f"{meta.get('ds_area')}/{meta.get('ds_section')} != {area}/{section}"
                )
            match = HEADING_RE.search(text)
            if not match:
                if (
                    f"## 対応スキル項目（ver.6 {AREA_LABEL[area]}）" in text
                    and "**★1直接対応**：なし" in text
                ):
                    already.append(filename)
                    continue
                raise SystemExit(f"{filename}: neither legacy nor supplemental ver.6 block found")
            start, end = bounds(text, match)
            new_text = text[:start] + supplemental_block(area, position) + text[end:]
            if new_text != text:
                changed.append(filename)
                if args.write:
                    path.write_text(new_text, encoding="utf-8")
            continue

        item_ids = mapping_ids(mapping)
        mapped_rows: list[dict[str, str]] = []
        for item_id in item_ids:
            row = by_id.get(item_id)
            if not row:
                raise SystemExit(f"{filename}: official item not found: {item_id}")
            mapped_rows.append(row)

        areas = {row.get("area") for row in mapped_rows}
        if len(areas) != 1:
            raise SystemExit(f"{filename}: mapped items span multiple areas: {sorted(areas)}")
        area = mapped_rows[0]["area"]

        if meta.get("ds_area") != area:
            raise SystemExit(f"{filename}: ds_area mismatch {meta.get('ds_area')} != {area}")

        match = HEADING_RE.search(text)
        if not match:
            canonical_heading = f"## 対応スキル項目（ver.6 {AREA_LABEL[area]}）"
            expected_items = [f"★ {normalize(row['item'])}" for row in mapped_rows]
            if canonical_heading in text and all(item in text for item in expected_items):
                already.append(filename)
                continue
            raise SystemExit(f"{filename}: neither legacy nor expected ver.6 skill block found")

        start, end = bounds(text, match)
        block = text[start:end]
        stars = re.findall(r"^(?:[-*+]\s*)?★\s*(.+?)\s*$", block, re.MULTILINE)
        if len(stars) < 1:
            raise SystemExit(f"{filename}: expected at least one legacy ★ item, got 0")

        new_text = text[:start] + canonical_block(mapped_rows) + text[end:]
        if new_text != text:
            changed.append(filename)
            if args.write:
                path.write_text(new_text, encoding="utf-8")

    mode = "WRITE" if args.write else "DRY-RUN"
    print(f"{mode}: reviewed migrations={len(changed)}, already={len(already)}")
    for filename in changed:
        ids = mapping_ids(REVIEWED[filename])
        target = ",".join(ids) if ids else "supplemental-no-direct-star1"
        print(f"CHANGE {filename} -> {target}")
    for filename in already:
        ids = mapping_ids(REVIEWED[filename])
        target = ",".join(ids) if ids else "supplemental-no-direct-star1"
        print(f"ALREADY {filename} -> {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
