# stemtazoo.github.io

`stemtazoo.github.io` は、Jekyll / GitHub Pages で公開している日本語の学習ノートサイトです。

現在は主に、次の 3 テーマを `pages/` 配下で管理しています。

- `pages/ds`: DS検定リテラシー、データサイエンス、統計、データエンジニアリング、AI利活用
- `pages/gk`: G検定、AI、機械学習、深層学習、画像認識、自然言語処理、強化学習、法律・倫理
- `pages/sg`: 情報セキュリティマネジメント試験、セキュリティ用語、カテゴリ別まとめ、過去問演習

記事本文だけでなく、テーマ別インデックス、前後ナビゲーション、NotebookLM 向けエクスポート、DS スキルチェックデータ、公開後の IndexNow 送信もこのリポジトリで扱います。

## 公開ページ

- DS検定: <https://stemtazoo.github.io/ds/>
- G検定: <https://stemtazoo.github.io/gk/>
- 情報セキュリティマネジメント試験: <https://stemtazoo.github.io/sg/>
- SG公式過去問: <https://stemtazoo.github.io/sg/past/>
- SG全記事一覧: <https://stemtazoo.github.io/sg/all/>

## リポジトリ構成

- `_layouts/`: 共通レイアウト
- `_includes/`: テーマ別・共通の Liquid 部品
- `pages/ds/`: DS検定・データサイエンス系の記事
- `pages/gk/`: G検定・AI系の記事
- `pages/sg/`: SG試験・情報セキュリティ系の記事
- `pages/sg/category/`: SG の分野別カテゴリページ
- `pages/sg/past/`: SG 公式過去問演習ページ
- `data/skillcheck/`: DS協会スキルチェックリストのバージョン管理データ
- `scripts/`: データ生成、メタデータ補完、NotebookLM エクスポート、IndexNow 送信用スクリプト
- `.github/workflows/`: GitHub Actions
- `f0977966c6644641ae35df01652658c4.txt`: IndexNow のルート検証ファイル
- `AGENTS.md`: AIエージェント・共同編集者向けの入口ルール
- `docs/agent/`: GitHub Pages互換性、IndexNow、テーマ設計、SG記事ルールなどの詳細な運用メモ

## テーマ別の運用

### DS検定 / データサイエンス

`pages/ds/` は DS検定リテラシーを中心に、統計、SQL、分析手法、AI利活用、データエンジニアリング、セキュリティ基礎などを扱います。

主な入口は `pages/ds/index.md` です。スキルチェックリスト関連のデータは `data/skillcheck/` に保持し、表示側では原則 `data/skillcheck/exports/latest.json` を参照します。

### G検定 / AI

`pages/gk/` は G検定対策向けの記事群です。`pages/gk/index.md` の `gk_sections` で表示順と章立てを管理しています。

個別記事の前後ナビゲーションは `gk_section` / `gk_order` と `_includes/gk_article_footer.html` に依存します。GitHub Pages の古い Liquid でも動くよう、include 側の条件式は保守的に書く方針です。

### SG試験 / 情報セキュリティ

`pages/sg/` は情報セキュリティマネジメント試験向けの記事群です。通常記事に加えて、分野別カテゴリページ、全記事一覧、過去問ページ、ケース問題・総合演習系の記事があります。

主な入口は次の通りです。

- `pages/sg/index.md`: 学習まとめトップ
- `pages/sg/all.md`: 全記事一覧
- `pages/sg/category/*.md`: 分野別カテゴリ
- `pages/sg/past/*.md`: 公式過去問演習

SG の通常記事に確認問題を追加するときの細かいルールは `docs/agent/sg-content-rules.md` を参照してください。

## よく使うスクリプト

### DS スキルチェックデータを生成する

```bash
python scripts/build_skillcheck_data.py
```

ローカルの xlsx を使う場合:

```bash
python scripts/build_skillcheck_data.py --xlsx ./data/skillcheck/raw/skillcheck_ver5.00_simple.xlsx --version 5.00
```

詳細は `data/skillcheck/README.md` を参照してください。

### DS 記事を NotebookLM 向けに出力する

```bash
python scripts/export_ds_notebooklm.py
```

出力先:

- `exports/notebooklm/ds/sections/*.md`
- `exports/notebooklm/ds/all.md`

外部のグループ定義を使う場合:

```bash
python scripts/export_ds_notebooklm.py --groups-file exports/notebooklm/ds/groups.template.json
```

### SG 記事を NotebookLM 向けに出力する

```bash
python scripts/export_sg_notebooklm.py
```

出力先:

- `exports/notebooklm/sg/sections/*.md`
- `exports/notebooklm/sg/all.md`

外部のグループ定義を使う場合:

```bash
python scripts/export_sg_notebooklm.py --groups-file path/to/sg-groups.json
```

### ページのメタデータを確認・補完する

まずは report モードで確認します。

```bash
python scripts/fix_page_metadata.py pages/sg
python scripts/fix_page_metadata.py pages/gk
python scripts/fix_page_metadata.py pages/ds
```

安全に補完できるものを書き戻す場合:

```bash
python scripts/fix_page_metadata.py pages/sg --apply
```

このスクリプトは、テーマごとに `prev` / `next`、`gk_section` / `gk_order`、footer include などの不足を確認します。

### DS front matter を確認する

```bash
python scripts/lint_ds_frontmatter.py
```

### IndexNow に URL を送信する

通常は GitHub Actions が GitHub Pages のデプロイ成功後に実行します。手元で動作確認する場合は、送信対象やキーを明示して実行します。

```bash
python scripts/submit_indexnow.py --all-known --key-file f0977966c6644641ae35df01652658c4.txt
```

## GitHub Pages 互換性

このサイトは GitHub Pages でのビルド成功を最優先します。ローカル環境では通っても、GitHub Pages 側の Jekyll / Liquid が古くて失敗することがあります。

Liquid を編集するときは、次を優先します。

- 複雑な `where_exp` より、明示的な `{% for %}` と `{% if %}`
- 複雑な boolean 条件より、段階的な分岐
- 新しい Liquid 構文より、GitHub Pages で確実に動く書き方
- きれいさより、ビルド安定性

より詳しい互換性ルールや既知の失敗例は `docs/agent/github-pages-compat.md` を参照してください。

## AIエージェント・共同編集者向けルール（役割整理）

このリポジトリの運用ルールは、**「入口（AGENTS.md）→ 分野別詳細（docs/agent）→ SG補助方針（project_rules）」** の3層で管理します。

### 1) 入口: `AGENTS.md`

- 役割: リポジトリ全体で必ず最初に読む「総合ガイド」
- 含む内容:
  - サイト全体の優先順位（Pages互換性、内容正確性、テーマ整合など）
  - 新規記事作成の判断フロー（重複・近似重複の扱い）
  - 編集前に確認すべき詳細ルールへのリンク
- 使い方: まず `AGENTS.md` を読んで、対象作業に必要な詳細ファイルへ進む

### 2) 分野別の正式ルール: `docs/agent/*.md`

`AGENTS.md` から参照する詳細ルールです。実作業時は、変更対象に応じて次を参照します。

- `docs/agent/github-pages-compat.md`
  - 役割: GitHub Pages で壊れない Liquid / Jekyll 記法の基準
  - 主な用途: include / layout / Liquid 条件分岐を編集するとき
- `docs/agent/indexnow.md`
  - 役割: IndexNow 送信とワークフロー運用の基準
  - 主な用途: URL変更、送信対象、運用確認
- `docs/agent/theme-consistency.md`
  - 役割: DS/GK/SG のテーマ間で見た目・構造を揃える基準
  - 主な用途: レイアウト、ナビ、カテゴリ導線の調整
- `docs/agent/sg-content-rules.md`
  - 役割: SG通常記事の執筆・改善方針（試験判断軸重視）
- `docs/agent/sg-article-template.md`
  - 役割: SG記事のテンプレート構造
- `docs/agent/sg-frontmatter-rules.md`
  - 役割: SG front matter の定義・更新ルール
- `docs/agent/sg-tag-rules.md`
  - 役割: SGタグ設計と一貫性ルール
- `docs/agent/sg-example-question-rules.md`
  - 役割: SGの例題・確認問題ブロック追加ルール
- `docs/agent/sg-series-summary-rules.md`
  - 役割: SGのまとめ・シリーズ系ページ構成ルール

### 3) SG補助ルール: `project_rules/*.md`

- `project_rules/sg_article_ai_search_improvement.md`
  - 役割: SG記事で「読者の切り分け判断」を強化するための追加ガイド
  - 位置づけ: `docs/agent/` の正式ルールを補助する実践ガイド
  - 主な用途: 「このページで切り分けること」「判断軸」「関連記事との役割分担」ブロックを追加・調整するとき

### ルール参照の実務フロー（最短）

1. `AGENTS.md` で優先順位と作業方針を確認  
2. 変更箇所に対応する `docs/agent/*.md` を確認  
3. SG記事で必要な場合のみ `project_rules/sg_article_ai_search_improvement.md` を追加参照  
4. 変更後は GitHub Pages 互換性を意識して最小修正で反映

新しい運用メモを追加する場合は、`AGENTS.md` には概要のみを書き、詳細は原則 `docs/agent/`（または補助方針なら `project_rules/`）へ分離してください。

## デプロイと IndexNow

GitHub Pages の公開後、`.github/workflows/indexnow.yml` が IndexNow 送信を行います。

- post-deploy の `deployment_status` 成功時に動く
- 通常は前回成功デプロイとの差分 URL だけを送信する
- 差分範囲が取れない場合は、全件バッチ送信を避けるため送信をスキップする
- 手動実行 `workflow_dispatch` に対応し、明示的に `all-known` を選んだ場合だけ全既知 URL を送信する

IndexNow キーファイル `f0977966c6644641ae35df01652658c4.txt` はリポジトリルートに置き、ファイル名 stem と中身を一致させる必要があります。移動したり front matter を付けたりしないでください。

## 編集時の注意

- 日本語本文は UTF-8 で扱う
- 端末表示が文字化けしても、ファイル自体が壊れているとは限らない
- front matter の `layout`、`title`、`description`、`permalink`、`tags` は慎重に変更する
- G検定記事では `gk_section` / `gk_order` を崩さない
- SG や DS の前後ナビゲーションでは `prev` / `next` と footer include の整合性を見る
- Index / 一覧 / 比較 / まとめページと、通常の1用語記事を混同しない
- 大きな構造変更の前後では、NotebookLM エクスポートや IndexNow 対象 URL への影響も確認する

## ローカル確認

可能であれば、レイアウト・include・front matter・インデックスを触った後に Jekyll ビルドを確認します。

```bash
bundle exec jekyll build
```

ただし、最終的な互換性確認は GitHub Actions / GitHub Pages 側の結果を優先します。特に `Liquid syntax error`、`Liquid Exception`、`_includes/...`、`_layouts/...` に関するエラーはブロッカーとして扱います。
