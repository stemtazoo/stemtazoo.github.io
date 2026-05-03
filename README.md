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
- `AGENTS.md`: AIエージェント・共同編集者向けの詳細な運用ルール

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

SG の通常記事に確認問題を追加するときの細かいルールは `AGENTS.md` の「SG確認問題（SG試験対策）追加ルール」を参照してください。

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

より詳しい互換性ルールや既知の失敗例は `AGENTS.md` を参照してください。

## デプロイと IndexNow

GitHub Pages の公開後、`.github/workflows/indexnow.yml` が IndexNow 送信を行います。

- post-deploy の `deployment_status` 成功時に動く
- 手動実行 `workflow_dispatch` に対応
- 週次の full refresh に対応
- 差分範囲が取れない場合は `--all-known` にフォールバック

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
