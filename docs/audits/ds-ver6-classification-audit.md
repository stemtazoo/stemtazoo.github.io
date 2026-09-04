# DS検定 ver.6 分類監査

- 監査日: 2026-09-04
- 対象: `pages/ds/`
- 目的: スキルチェックリスト ver.6 と現行DS検定の4領域（基盤 / データサイエンス / データエンジニアリング / 価値創造）に合わせて、既存記事を安全に再分類するための方針を整理する。

## 進捗スナップショット（2026-09-04）

- 公式 ver.6 / 2026年試験範囲の確認: 完了
- `pages/ds/index.md` の4領域化: 実施済み
- index の `ds_area` 優先表示: 実施済み
- 基盤の表示区分: 論理的思考 / 課題の定義・仮説 / 目標・指標 / データ理解・検証 / ITセキュリティまで拡張済み
- 安全に自動判定できるデータサイエンス / データエンジニアリング記事: 移行済み
- 旧 `business` 記事: 個別監査を進行中
- `security`: 個別監査未着手
- `ai-utilization`: 個別監査未着手
- ver.6スキルチェックデータ基盤: 旧ver.5構造からの更新が残っている

記事分類の進捗は、2026-09-04時点の保守的な集計で約6割。特殊ページ（index / skillcheck / cheatsheet等）を含むため、最終的な分類対象数は監査完了時に再確定する。

## 結論

現時点では、既存記事の `categories` / `tags` を一括置換しない。

現在の `pages/ds/index.md` はタグ・カテゴリを表示条件に使っており、特に `categories: [business]` が非常に広く使われている。先に ver.6 用の分類メタデータを追加し、表示側を切り替えた後で旧分類を整理する方が安全。

推奨メタデータ:

```yaml
ds_area: foundation        # foundation / datascience / dataengineering / value-creation
ds_section: data-understanding
```

既存の `categories` と `tags` は移行期間中は残す。

## ver.6 の4領域と既存記事の移行方針

### 基盤 (`foundation`)

候補:
- 行動規範・倫理
- 論理的思考
- 課題の定義
- KPI / KGI
- データ理解
- 生成AIの基礎利用
- ITセキュリティ
- 契約・権利・個人情報

既存タグでは `data-understanding` が比較的対応しやすい。`security` はデータエンジニアリングにもまたがるため自動移行しない。

### データサイエンス (`datascience`)

既存タグから安全に対応しやすいもの:
- `linear-algebra`
- `calculus`
- `set-theory`
- `statistics`
- `data-preparation`
- `visualization`
- `modeling`
- `unstructured-data`

### データエンジニアリング (`dataengineering`)

既存タグから安全に対応しやすいもの:
- `environment-setup`
- `data-collection`
- `data-structure`
- `data-storage`
- `data-processing`
- `sql`
- `database`

`security` と MLOps / AIシステム運用は個別確認する。

### 価値創造 (`value-creation`)

旧 `categories: [business]` の記事を丸ごと移すのは不可。

候補:
- 事業課題の再定義
- ビジネスモデル / 事業設計
- AI・データ活用の企画
- PoC
- 効果測定
- プロジェクト推進
- ガバナンス
- 組織への実装

旧ビジネス記事のうち論理思考・データ理解・KPIなどは「基盤」に入るため、記事単位の判定が必要。

## 代表例

- `metacognition.md` → `foundation`
- `kpi-kgi.md` → `foundation`
- `hypothesis-thinking.md` → `foundation`
- `mece.md` → `foundation`
- `pest-analysis.md` → `value-creation`
- `swot-analysis.md` → `value-creation`
- `five-forces-analysis.md` → `value-creation`
- `design-thinking.md` → `value-creation`
- `poc-concept-proof.md` → `value-creation`
- `project-management.md` / `wbs.md` / `scrum.md` / `critical-path.md` → `value-creation`
- `key-stretching.md` → `foundation` 候補。ただし実装・運用中心なら `dataengineering`
- `japanese-morphological-analysis-tools.md` → `datascience`
- `morphological-dependency-parsing.md` → `datascience`
- `nltk.md` → `datascience`
- `inheritance.md` → `dataengineering` 第一候補

## 構造上の問題

1. `categories: [business]` が広すぎる。自然言語処理、プログラミング、セキュリティなどにも付いているため、ver.6 の「価値創造」の判定には使えない。
2. `security` は基盤とデータエンジニアリングの両方にまたがる。
3. `design` は多数の分野で使われており、ver.6 の領域判定キーには使えない。

## 推奨する移行手順

1. `ds_area` / `ds_section` を追加する。
2. `pages/ds/index.md` を `ds_area` 優先表示へ切り替える。
3. 旧 `business` 記事を個別監査する。
4. `security` 記事を個別監査する。
5. `ai-utilization` 記事を個別監査する。
6. ver.6スキルチェックデータ基盤を更新する。
7. 最後に未分類記事を再計測する。

## 自動移行してよいタグ

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

## 自動移行しないもの

- `business`
- `design`
- `security`
- `ai-utilization`
- `skillcheck`
- `cheatsheet`

これらは複数領域をまたぐか、記事の役割を示すタグであるため個別確認する。
