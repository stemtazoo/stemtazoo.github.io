# DS検定 ver.6 分類監査

- 監査日: 2026-09-04
- 対象: `pages/ds/`
- 目的: スキルチェックリスト ver.6 と現行DS検定の4領域（基盤 / データサイエンス / データエンジニアリング / 価値創造）に合わせて、既存記事を安全に再分類するための方針と進捗を整理する。

## 進捗スナップショット（2026-09-04）

- 公式 ver.6 / 2026年試験範囲の確認: 完了
- `pages/ds/index.md` の4領域化: 実施済み
- index の `ds_area` 優先表示: 実施済み
- 基盤の表示区分: 行動規範・倫理・権利 / 論理的思考 / 課題の定義・仮説 / 目標・指標 / データ理解・検証 / AI・生成AIの基礎 / ITセキュリティまで拡張済み
- データエンジニアリングの `programming` 表示区分: 追加済み
- 安全に自動判定できるデータサイエンス / データエンジニアリング記事: 移行済み
- 旧 `business` / `security` / `ai-utilization` の通常記事: 個別監査完了
- 未分類記事の横断監査: 完了
- 代表的な誤分類の再監査: 実施済み
- ver.6スキルチェックデータ基盤: 旧ver.5構造からの更新が残っている

自動生成監査 `docs/audits/ds-ver6-unclassified.md` の最新集計では、`pages/ds/*.md` は **285ページ**。特殊ページ12ページを除く通常記事は **273ページ**で、**273 / 273 = 100.0%** の4領域分類が完了した。

## 分類母数から除外する特殊ページ

次の12ページは、単一の `ds_area` を付ける通常記事ではなく、索引・横断ガイド・旧スキル体系のまとめ、またはリダイレクトとして扱う。

- `index.md`
- `optional-math-algorithm.md`
- `business-skillcheck.md`
- `engineering-skillcheck.md`
- `skillcheck.md`
- `ai-utilization-skillcheck.md`
- `model-curriculum-summary.md`
- `skilllevel-2023-summary.md`
- `skilllevel-2023-assistant-ds-business.md`
- `skilllevel-2023-assistant-ds-dataengineering.md`
- `skilllevel-2023-assistant-ds-datascience.md`
- `file-transfer-protocol.md`（`/ds/ftp-ssh/` へのリダイレクト）

除外理由:

- 4領域を横断して参照する索引・学習ガイドである
- ver.5以前の「ビジネス力 / データサイエンス力 / データエンジニアリング力 / AI利活用」の旧体系そのものを説明するページが含まれる
- リダイレクトページは学習記事ではない
- 1つの `ds_area` に押し込むとページの役割を誤って表現する

## 結論

通常記事の `ds_area` / `ds_section` 移行は完了した。既存の `categories` / `tags` は、既存URLや関連リンク・補助表示への影響を避けるため、現段階では一括置換しない。

推奨メタデータ:

```yaml
ds_area: foundation        # foundation / datascience / dataengineering / value-creation
ds_section: data-understanding
```

今後の主作業は、**旧ver.5のスキルチェックページとデータ生成基盤をver.6へ更新すること**、および必要に応じて記事本文中の旧「ビジネス力シート」「AI利活用スキルシート」表記を正確なver.6対応項目へ置き換えること。

## ver.6 の4領域と記事分類方針

### 基盤 (`foundation`)

- 行動規範・倫理・権利
- 論理的思考
- 課題の定義
- KPI / KGI
- データ理解
- 生成AIの基礎
- ITセキュリティ
- 契約・個人情報

### データサイエンス (`datascience`)

- 線形代数 / 微積分 / 集合論 / 統計
- データ理解・準備・可視化
- モデル化・評価
- 非構造化データ処理

### データエンジニアリング (`dataengineering`)

- 環境構築
- データ収集・構造・蓄積・加工
- SQL / データベース
- プログラミング基礎
- 実装・運用寄りのセキュリティ

### 価値創造 (`value-creation`)

- 事業・ビジネス設計
- PoC / プロジェクト推進
- ガバナンス・リスク
- 技術・社会トレンド
- データ・AIの社会実装

## 個別監査で得た代表的な判断例

- `metacognition.md` / `mece.md` / `why-structure.md` → `foundation`
- `kpi-kgi.md` / `revenue-equation.md` → `foundation`
- `gdpr.md` / `ffp.md` / `k-anonymity.md` → `foundation`
- `mfa.md` / `pki.md` / `hash-function.md` → `foundation`
- `pest-analysis.md` / `swot-analysis.md` / `design-thinking.md` → `value-creation`
- `project-management.md` / `wbs.md` / `scrum.md` / `gantt-chart.md` → `value-creation`
- `governance.md` / `incident-management.md` → `value-creation`
- `olap.md` / `data-cube.md` / `bi-tool-functions.md` → `datascience`
- `ab-test.md` / `paired-vs-independent-data.md` / `type1-type2-error.md` → `datascience`
- `stemming-vs-lemmatization.md` / `data-transformation.md` → `datascience`
- `inheritance.md` / `constructor.md` → `dataengineering`
- `cap-theorem.md` → `dataengineering`
- `digital-twin.md` / `cps-iot-digitaltwin-cheatsheet.md` → `value-creation`

## 構造上の注意点

1. `categories: [business]` は広すぎるため、ver.6 の「価値創造」の判定キーには使わない。
2. `security` は基盤とデータエンジニアリングの両方にまたがるため、記事の主目的で判断する。
3. `design` は多数分野で使われているため領域判定キーには使わない。
4. `skillcheck` や横断ガイドは、4領域の通常記事分類とは別管理する。
5. 安全タグで自動分類した記事でも、`gantt-chart.md` や `data-literacy-practice.md` のように記事の役割とずれる場合は、元分類を明示して個別訂正する。

## 今後の作業順

1. ver.6スキルチェックExcelの実構造を確認する。
2. `scripts/build_skillcheck_data.py` と `data/skillcheck/` をver.6へ更新する。
3. 旧skillcheck系ページを4領域に合わせて再構成する。
4. 記事本文中の旧スキルシート表記を、正確なver.6対応項目へ段階的に更新する。
5. indexとGitHub Pages表示を最終監査する。

## 自動移行に使った旧タグ

| 旧タグ | ver.6領域 |
|---|---|
| `linear-algebra` | データサイエンス |
| `calculus` | データサイエンス |
| `set-theory` | データサイエンス |
| `statistics` | データサイエンス |
| `data-preparation` | データサイエンス |
| `visualization` | データサイエンス |
| `modeling` | データサイエンス |
| `unstructured-data` | データサイエンス |
| `environment-setup` | データエンジニアリング |
| `data-collection` | データエンジニアリング |
| `data-structure` | データエンジニアリング |
| `data-storage` | データエンジニアリング |
| `data-processing` | データエンジニアリング |
| `sql` | データエンジニアリング |
| `database` | データエンジニアリング |

## 自動移行しないタグ

- `business`
- `design`
- `security`
- `ai-utilization`
- `skillcheck`
- `cheatsheet`

これらは複数領域をまたぐか、記事の役割を示すタグであるため、通常記事は個別確認した。
