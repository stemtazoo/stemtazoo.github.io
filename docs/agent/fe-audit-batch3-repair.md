# FE監査 Batch 3 修正指示

対象は `docs/audits/fe-full-audit-2026-08-29.md` の P1 Batch 3 です。

## 目的

以下12記事を、現在のFE記事ルールに合わせて修正してください。本文の大規模な書き換えは禁止です。既存説明をできるだけ活かし、front matter・標準見出し・分類・タグを中心に最小限の修正を行ってください。

対象:

1. `pages/fe/core-competence.md`
2. `pages/fe/core-technology.md`
3. `pages/fe/corporate-governance.md`
4. `pages/fe/cpu-registers.md`
5. `pages/fe/cpu-scheduling-idle-time.md`
6. `pages/fe/cyber-physical-security-framework.md`
7. `pages/fe/database-backup-recovery.md`
8. `pages/fe/defect-repair-cost-expected-value.md`
9. `pages/fe/disk-striping.md`
10. `pages/fe/diversity-management.md`
11. `pages/fe/dma.md`
12. `pages/fe/dmz-server-placement.md`

作業前に必ず以下を読み直してください。

- `docs/agent/fe-content-rules.md`
- `docs/agent/fe-article-template.md`
- `docs/agent/fe-frontmatter-rules.md`
- `docs/agent/fe-tag-rules.md`

## 共通ルール

- 通常記事は `layout: page`、`title`、`description`、`permalink`、`tags`、`fe_section`、`fe_subsection`、`fe_order`、`date`、`last_modified_at` を満たす。
- FE主要カテゴリタグは `fe-technology` / `fe-management` / `fe-strategy` のうち記事分類に対応するものを **1つだけ** 持たせる。
- 通常記事末尾は `{% include fe_article_footer.html %}` を維持する。
- `last_modified_at` は今回変更した記事のみ `2026-08-29` とする。
- `date` が不足している場合、**推測・一律日付・現在日を使用しないこと**。対象ファイルのGit履歴を確認し、そのファイルが最初に追加されたコミットの日付を `YYYY-MM-DD` で設定する。
- PR本文に、今回追加した各 `date` について `file -> date -> 初回追加commit SHA` を必ず列挙する。履歴を確認できなかったファイルは `date` を勝手に追加せず報告する。
- `fe_order` は同じ `fe_section` + `fe_subsection` の既存記事を確認して決める。既存値を不用意に変更しない。
- 既存内容にすでに判断基準がある場合、それを標準見出しへ整理し、同じ説明を重複追加しない。
- 科目Bと直接関係しない記事に `## 科目Bでどう使う？` を無理に追加しない。

## 記事別の修正方針

### 1. `core-competence.md`

監査指摘: `## 科目Aでどう出る？` 不足。

既存の `## どんな場面で使う？` と `## よくある誤解・混同` に、

- 競争優位の源泉
- 他社がまねしにくい能力
- 能力 vs 事業領域
- ベンチマーキングとの違い

という十分な判断材料があります。

`## 定義・仕組み` の後に `## 科目Aでどう出る？` を追加し、既存内容を重複させず短く整理してください。中心は次の切り分けです。

```text
他社がまねしにくい企業独自の中核能力 → コアコンピタンス
優良企業と比較して改善する           → ベンチマーキング
企業が事業を行う領域                 → 事業ドメイン
企業経営を監督する仕組み             → コーポレートガバナンス
```

### 2. `core-technology.md`

監査指摘: `fe_order` 不足。

- 同じストラテジ系の経営戦略周辺の記事を確認し、適切な `fe_order` を追加する。
- `fe_subsection: 経営戦略マネジメント` が現在のサイト分類語彙と一致しているかも確認する。現在の同系統記事が `経営戦略` へ統一されている場合は `経営戦略` に合わせる。
- 本文は変更しない。既に `科目Aでどう出る？` があり、内容も十分。

### 3. `corporate-governance.md`

監査指摘: `## 科目Aでどう出る？` 不足。

既存の `どんな場面で使う？` と `よくある誤解・混同` に判断材料があるため、新しい知識を広げず、標準見出しを追加して整理してください。

中心は次の切り分けです。

```text
企業経営全体の監督・透明性 → コーポレートガバナンス
IT投資・IT活用の統制       → ITガバナンス
他社がまねしにくい強み     → コアコンピタンス
```

### 4. `cpu-registers.md`

監査指摘: `fe_order`, `date` 不足。

- `fe_order` を同じ `テクノロジ系 / コンピュータ構成要素` の近隣記事から決める。
- `date` はGit履歴の最初の追加コミットから取得する。推測禁止。
- 本文は変更しない。既存記事の判断軸は十分。

### 5. `cpu-scheduling-idle-time.md`

監査指摘: `## 科目Bでどう使う？` または `## どんな場面で使う？` 不足。

この記事はCPU/I/Oのタイムチャート計算が中心で、科目B固有の記事として無理に扱わない。

`## 科目Aでどう出る？` の後に、短い `## どんな場面で使う？` を追加してください。内容は、

- 複数タスクの実行順を追う
- I/O待ちを除外する
- CPU遊休時間・処理順を求める
- タイムチャート問題で使う

程度に限定する。

既存の `## タイムチャートの書き方` は残し、重複説明を増やさない。

### 6. `cyber-physical-security-framework.md`

監査指摘: `fe_order`, `date` 不足。

- `fe_order` を同じ `ストラテジ系 / システム戦略` の近隣記事から決める。
- `date` はGit履歴の初回追加コミットから取得する。
- primary FE tag は既に `fe-strategy` なので維持する。
- 本文は原則変更しない。

### 7. `database-backup-recovery.md`

監査指摘: `fe_order`, `date` 不足。

- `fe_order` を `テクノロジ系 / データベース` の近隣記事から決める。
- `date` はGit履歴の初回追加コミットから取得する。
- 本文は原則変更しない。

### 8. `defect-repair-cost-expected-value.md`

監査指摘: `date` 不足。

- `date` だけをGit履歴の初回追加コミットから追加する。
- `fe_order: 90` は維持する。
- 本文は変更しない。

### 9. `disk-striping.md`

監査指摘: `fe_order`, `date` 不足。

- `fe_order` を `テクノロジ系 / コンピュータ構成要素` の近隣記事から決める。
- `date` はGit履歴の初回追加コミットから取得する。
- 本文は原則変更しない。

### 10. `diversity-management.md`

監査指摘: `fe_order` 不足。

- `ストラテジ系 / 企業活動` の近隣記事を確認して `fe_order` を追加する。
- 既存 `date: 2026-08-25` は変更しない。
- 本文は変更しない。

### 11. `dma.md`

監査指摘: `fe_order`, `date` 不足、主要カテゴリタグ不正。

- `tags: [fe, technology, ...]` の `technology` を正式な主要カテゴリ `fe-technology` に修正する。
- FE主要カテゴリタグが1個だけになることを確認する。
- `fe_order` を `テクノロジ系 / コンピュータ構成要素` の近隣記事から決める。
- `date` はGit履歴の初回追加コミットから取得する。
- 本文は変更しない。

### 12. `dmz-server-placement.md`

監査指摘: `fe_order`, `date` 不足。

- `fe_order` を `テクノロジ系 / ネットワーク` の近隣記事から決める。
- `date` はGit履歴の初回追加コミットから取得する。
- 本文は原則変更しない。

## 完了前チェック

12記事について以下をスクリプト等で確認してください。

1. YAML front matter が正しくparseできる。
2. 通常記事の必須front matterがすべて存在する。
3. FE主要カテゴリタグがちょうど1個。
4. `core-competence.md` と `corporate-governance.md` に `## 科目Aでどう出る？` がちょうど1個ある。
5. `cpu-scheduling-idle-time.md` に `## どんな場面で使う？` がちょうど1個ある。
6. 12記事すべてが `{% include fe_article_footer.html %}` で終わる。
7. `git diff --check` を通す。
8. 変更ファイルがこの12記事だけであることを確認する。
9. 今回追加した各 `date` について、初回追加commit SHAと日付をPR本文に記載する。
10. `bundle exec jekyll build` が実行可能なら行う。環境上実行できなければ、その理由をPR本文に記載し、GitHub Actionsで最終確認する。

## 禁止事項

- `date: 2026-08-27` のように複数記事へ同じ日付を一律設定しない。
- Git履歴を確認せず `date` を推測しない。
- 監査対象外の記事をついでに修正しない。
- 科目B見出しを機械的に追加しない。
- 既存の良い本文を全面的に書き換えない。
