# stemtazoo.github.io

`stemtazoo.github.io` は、Jekyll / GitHub Pages で公開している日本語の学習ノートサイトです。現在は DS・GK・SG・FE の4テーマを `pages/` 配下で管理しています。

記事、テーマ別索引、サイト内検索のほか、DS スキルチェックデータ、NotebookLM 向けエクスポート、AI 向け Markdown・索引の生成と検証、公開後の IndexNow 送信も扱います。

## 公開ページとテーマ

| テーマ | 主な内容 | 入口ソース | 公開ページ |
| --- | --- | --- | --- |
| DS | DS検定リテラシー、統計、Python、SQL、データ分析・エンジニアリング、AI利活用 | `pages/ds/index.md` | [DS学習まとめ](https://stemtazoo.github.io/ds/) |
| GK | G検定、機械学習、深層学習、AIの社会実装・法律・倫理 | `pages/gk/index.md` | [G検定学習まとめ](https://stemtazoo.github.io/gk/) |
| SG | 情報セキュリティマネジメント試験、実務判断、カテゴリ別まとめ、過去問演習 | `pages/sg/index.md` | [SG学習まとめ](https://stemtazoo.github.io/sg/) |
| FE | 基本情報技術者試験、科目Aの知識整理、科目Bのアルゴリズム・疑似言語読解 | `pages/fe/index.md` | [FE学習まとめ](https://stemtazoo.github.io/fe/) |

- [サイト内検索](https://stemtazoo.github.io/search/)
- [SG公式過去問](https://stemtazoo.github.io/sg/past/)
- [SG全記事一覧](https://stemtazoo.github.io/sg/all/)

## リポジトリ構成

| パス | 用途 |
| --- | --- |
| `_config.yml` / `Gemfile` / `Gemfile.lock` | サイト設定と Jekyll の依存関係 |
| `_layouts/` / `_includes/` | 共通レイアウトとテーマ別・共通の Liquid 部品 |
| `assets/` | CSS、JavaScript、画像など |
| `pages/ds/` / `pages/gk/` / `pages/sg/` / `pages/fe/` | テーマ別の記事・索引 |
| `pages/sg/category/` / `pages/sg/past/` | SG分野別カテゴリと公式過去問演習 |
| `_data/` | 入口ページの導線や SG 過去問の構造化データ |
| `search.md` / `search-index.json` | サイト内検索ページと検索用データ |
| `data/skillcheck/` | DS協会スキルチェックリストの版別データ・エクスポート |
| `exports/notebooklm/` | DS・SG の NotebookLM 向け出力 |
| `llms.txt` / `.well-known/agent-skills/` | AI 向けのサイト案内・読解ガイド |
| `scripts/` | データ生成、メタデータ補完、監査、移行、IndexNow 送信など |
| `.github/workflows/` | Pages 公開、データ生成、監査、移行などの GitHub Actions |
| `docs/agent/` / `project_rules/` | 編集・運用ルールと補助方針 |
| `docs/audits/` | 記事・分類・Markdown の監査記録 |
| `artifacts/` | AI 向けコンテンツ監査などの出力（公開対象外） |
| `_site/` | Jekyll と後処理による公開用生成物 |

## テーマ別の運用

### DS検定 / データサイエンス

記事は `ds_area` / `ds_section` で分類します。リポジトリ内のスキルチェックデータは **ver.6.00** を基準にしています。

- 全項目: `data/skillcheck/exports/latest.json`
- DS検定対象の4領域の★1項目: `data/skillcheck/exports/exam_star1_latest.json`
- 過去版・新旧対応表: `data/skillcheck/versions/`

公式スキル項目の分類とブログ独自の `ds_area` / `ds_section` は区別して管理します。詳細は [データ運用ガイド](data/skillcheck/README.md) を参照してください。

### G検定 / AI

`pages/gk/index.md` の `gk_sections` で章立てを管理しています。個別記事の前後ナビゲーションは `gk_section` / `gk_order` と `_includes/gk_article_footer.html` に依存します。索引の変更時は [GK索引ルール](docs/agent/gk-index-rules.md) も参照してください。

### SG試験 / 情報セキュリティ

通常記事のほか、分野別カテゴリ、全記事一覧、公式過去問、ケース問題・総合演習を管理します。科目Aの知識と科目Bの実務判断をつなぎ、選択肢を切り分ける判断軸を重視します。

確認問題の追加時は [SG例題・確認問題ルール](docs/agent/sg-example-question-rules.md)、導線の変更時は [SGナビゲーションルール](docs/agent/sg-navigation-rules.md) を参照してください。

### FE試験 / 基本情報技術者

科目Aの選択肢判断と科目Bのプログラム読解・トレースを重視します。通常記事には `tags`、`fe_section`、`fe_subsection`、`fe_order` を設定し、末尾で `fe_article_footer.html` を include します。

関連記事は FE 内に限定し、`prev` / `next` は明示的な依頼がある場合のみ追加します。

## ローカル確認

コマンドはリポジトリのルートで実行します。Ruby / Bundler と Python を用意してください。Python のデータ生成・監査環境は、関連 Actions に合わせて Python 3.12 を基準にすると確認しやすくなります。

`Gemfile` は `github-pages` を **232** に固定し、`_config.yml` は Cayman リモートテーマを指定しています。

```bash
bundle install
bundle exec jekyll build
python scripts/generate_agent_resources.py
python scripts/validate_agent_resources.py
python scripts/audit_agent_content.py
```

AI 向けデータの生成・検証は Jekyll ビルド後に実行します。通常の HTML 表示をブラウザで確認する場合は `bundle exec jekyll serve` を使います。

最終的な互換性確認は GitHub Actions / GitHub Pages 側の結果を優先します。Liquid は基本的なループ・条件分岐を使い、複雑な `where_exp` や新しい構文への依存を避けます。詳細は [GitHub Pages互換性ルール](docs/agent/github-pages-compat.md) を参照してください。

## よく使うスクリプト

### DS スキルチェックデータ・ページの生成

既定の公式 ver.6 データを取得して生成します。

```bash
python scripts/build_skillcheck_data.py
```

ローカルの xlsx を使う場合:

```bash
python scripts/build_skillcheck_data.py --xlsx ./data/skillcheck/raw/skillcheck_ver6.00.xlsx --version 6.00
```

生成した★1データから総合・分野別スキルチェックページを更新する場合:

```bash
python scripts/build_ds_skillcheck_pages.py
```

### NotebookLM 向けエクスポート

```bash
python scripts/export_ds_notebooklm.py
python scripts/export_sg_notebooklm.py
```

それぞれ `exports/notebooklm/ds/`、`exports/notebooklm/sg/` の `sections/*.md` と `all.md` に出力します。外部のグループ定義を使う場合は `--groups-file path/to/groups.json` を指定します。

### メタデータと front matter の確認

まず report モードで確認します。対象は SG・GK・DS の直下の Markdown ファイルです（FE は対象外）。

```bash
python scripts/fix_page_metadata.py pages/sg
python scripts/fix_page_metadata.py pages/gk
python scripts/fix_page_metadata.py pages/ds
python scripts/lint_ds_frontmatter.py
```

`fix_page_metadata.py` は前後ナビゲーション・footer などの不足を確認します。安全に推定できる修正を書き戻す場合は `--apply` を追加し、差分を確認してください。

### IndexNow の送信内容の確認

次の例は全既知 URL を確認する dry run で、実際の送信は行いません。

```bash
python scripts/submit_indexnow.py --all-known --key-file f0977966c6644641ae35df01652658c4.txt --allow-large-batch --dry-run
```

通常の送信は公開後の Actions が担当します。全件の実送信は、意図的な手動更新時に限ります。

## デプロイと公開後の処理

[pages.yml](.github/workflows/pages.yml) は `main` への push または手動実行で、次の順序で公開します。

1. `actions/jekyll-build-pages@v1` で `_site/` に Jekyll ビルド
2. `generate_agent_resources.py` で記事 Markdown、テーマ別 `llms.txt`、生成マニフェストを追加
3. `validate_agent_resources.py` で生成物と HTML の参照整合性を検証
4. `audit_agent_content.py` でコンテンツ監査レポートを `artifacts/` に出力
5. `_site/` をアップロードし、GitHub Pages にデプロイ

記事 Markdown は HTML 記事の URL 配下の `index.md`、テーマ別索引は `/ds/llms.txt` などで公開します。修正は `_site/` の生成物ではなく元記事や生成スクリプトに対して行います。

公開後は [indexnow.yml](.github/workflows/indexnow.yml) が IndexNow 送信を行います。

- `github-pages` 環境の `deployment_status` 成功時に実行
- 通常は前回成功デプロイとの差分 URL のみ送信
- 差分範囲を取得できない場合、または100 URL の上限を超える場合は送信をスキップ
- 手動実行の `auto` は差分範囲がないためスキップし、`all-known` を明示的に選ぶと全既知 URL を送信

検証ファイル `f0977966c6644641ae35df01652658c4.txt` はルートに保持し、ファイル名の拡張子を除いた文字列と内容を一致させます。移動や front matter の追加はしないでください。詳細は [IndexNow運用ルール](docs/agent/indexnow.md) を参照してください。

Pages 公開とは別に、DS ver.6 データ・ページ生成、分類・Markdown監査、記事移行、SGタグ監査、DS/GK更新日の補完用ワークフローがあります。一部は結果を自動コミットするため、実行条件と書き込み対象は [.github/workflows/](.github/workflows/) の各定義を確認してください。

## 編集・共同作業のルール

運用ルールは **[AGENTS.md](AGENTS.md) → [docs/agent/](docs/agent/) → 必要に応じて [project_rules/](project_rules/)** の順に参照します。README は概要と作業の入口で、詳細な判断基準は各ガイドにまとめています。

| テーマ | 執筆方針 | 記事テンプレート |
| --- | --- | --- |
| DS | [DS記事ルール](docs/agent/ds-content-rules.md) | [DSテンプレート](docs/agent/ds-article-template.md) |
| GK | [GK記事ルール](docs/agent/gk-content-rules.md) | [GKテンプレート](docs/agent/gk-article-template.md) |
| SG | [SG記事ルール](docs/agent/sg-content-rules.md) | [SGテンプレート](docs/agent/sg-article-template.md) |
| FE | [FE記事ルール](docs/agent/fe-content-rules.md) | [FEテンプレート](docs/agent/fe-article-template.md) |

front matter・タグ・ナビゲーションの詳細は `AGENTS.md` の参照一覧から確認できます。共通の変更では [テーマ整合性](docs/agent/theme-consistency.md)、[AI検索・読者理解](docs/agent/ai-search-content-rules.md)、教材を追加する場合は [インタラクティブ教材ルール](docs/agent/interactive-learning-rules.md) も参照してください。

SG記事で判断軸や関連記事との役割分担を強化する場合は、補助方針 [SG記事改善ルール](project_rules/sg_article_ai_search_improvement.md) を必要に応じて参照します。

編集時は次を確認してください。

- 4テーマの既存記事を検索し、新規記事・既存記事更新・比較・まとめ・導線改善のどれが適切か判断する
- 通常記事と索引・カテゴリ・まとめの役割を区別し、近似重複を増やさない
- 日本語は UTF-8 で扱い、front matter とテーマ別の分類・並び順・footer の整合性を保つ
- 新規記事には `last_modified_at` を設定し、既存記事で使用している更新日も内容変更時に更新する
- 法令・規格・公的基準は現在の公式版を確認し、過去問の歴史的な前提と区別する
- URL・構造変更時は内部リンク、カテゴリ・索引、NotebookLM 出力、AI 向け生成物、IndexNow への影響を確認する
- レイアウト・include・front matter・索引の変更後はビルドを確認し、Pages の Liquid エラーを解消してから公開する
