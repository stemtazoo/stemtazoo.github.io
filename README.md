# stemtazoo.github.io

`stemtazoo.github.io` は、Jekyll / GitHub Pages で公開している学習用サイトです。  
現在は主に次の 3 テーマを `pages/` 配下で管理しています。

- `pages/ds`: データサイエンス学習コンテンツ
- `pages/gk`: G 検定・G 検定系の学習コンテンツ
- `pages/sg`: 情報処理安全確保支援士（SG）学習コンテンツ

このリポジトリでは、記事本文だけでなく、ページ一覧、テーマ別ナビゲーション、補助データ生成、公開後の検索エンジン連携まで含めて運用しています。

## リポジトリ構成

主なディレクトリとファイルは次のとおりです。

- `_layouts/`: 共通レイアウト
- `_includes/`: テーマ別・共通の部品
- `pages/`: 公開ページ本体
- `data/`: ビルドや表示で使う補助データ
- `scripts/`: データ生成や書き出し用スクリプト
- `.github/workflows/`: GitHub Actions
- `f0977966c6644641ae35df01652658c4.txt`: IndexNow 用のルート検証ファイル

## ビルドと運用の前提

このサイトは GitHub Pages 互換を優先して運用しています。

- ローカルで通っても、GitHub Pages 側の古い Jekyll / Liquid で失敗することがあります
- レイアウトや include の変更では、簡潔さより互換性を優先します
- Liquid は複雑な条件式より、単純な `if` / `for` / `assign` ベースの実装を優先します

詳しい作業方針は [AGENTS.md](/p:/MyDocuments/GitHub/stemtazoo.github.io/AGENTS.md) を参照してください。

## コンテンツ運用

テーマごとにページを分けていますが、構成やナビゲーションの考え方はできるだけ揃える方針です。

- `pages/ds`: 学習まとめ、スキルチェック、NotebookLM 向け書き出しなどを運用
- `pages/gk`: セクション単位の学習記事と関連ナビゲーションを運用
- `pages/sg`: セキュリティ学習記事と関連ナビゲーションを運用

新しい記事やシリーズを追加するときは、front matter の `layout`、`tags`、順序項目、permalink の整合性を保つ必要があります。

## スクリプト

`scripts/` には、公開データや補助ファイルを生成するためのスクリプトがあります。

### 一覧

- `scripts/build_skillcheck_data.py`
  - `pages/ds` のスキルチェック表示に使う JSON / CSV を生成します
- `scripts/export_ds_notebooklm.py`
  - `pages/ds` の記事を NotebookLM 用 Markdown に書き出します
- `scripts/lint_ds_frontmatter.py`
  - `pages/ds` の front matter の整合性確認に使えます
- `scripts/submit_indexnow.py`
  - GitHub Pages 公開後に IndexNow へ URL を送信します

### DS スキルチェックデータ生成

`/pages/ds` 向けのスキルチェック関連データは、`data/skillcheck` 配下でバージョン管理しています。

- 実行スクリプト: `scripts/build_skillcheck_data.py`
- 詳細: `data/skillcheck/README.md`

#### Quick start

```bash
python scripts/build_skillcheck_data.py
```

この処理では、公開元データから `versions/<version>/` と `exports/` 配下の公開用データを生成し、`pages/ds` で参照できる形に整えます。

### NotebookLM 向け DS エクスポート

`pages/ds/*.md` を、NotebookLM に読み込ませやすい Markdown として書き出すために `scripts/export_ds_notebooklm.py` を使います。

#### 基本実行

```bash
python scripts/export_ds_notebooklm.py
```

#### グループ定義を使う場合

`pages/ds/index.md` の `ds_sections` ではなく、外部 JSON を使って書き出したい場合は `--groups-file` を指定します。

```bash
python scripts/export_ds_notebooklm.py --groups-file exports/notebooklm/ds/groups.template.json
```

#### 出力先

- `exports/notebooklm/ds/sections/*.md`: セクションごとのファイル
- `exports/notebooklm/ds/all.md`: 全セクションを結合したファイル

#### 更新手順の目安

1. `pages/ds/` の記事を更新する
2. 必要に応じて `pages/ds/index.md` の `ds_sections` またはグループ定義 JSON を見直す
3. `python scripts/export_ds_notebooklm.py` を実行する

必要に応じて `scripts/lint_ds_frontmatter.py` で front matter の揺れも確認できます。

## デプロイ関連

GitHub Actions では、GitHub Pages のビルドに加えて IndexNow 送信も扱っています。

- IndexNow のキー検証ファイルはリポジトリルートに置いたままにします
- `f0977966c6644641ae35df01652658c4.txt` の内容はファイル名の stem と一致させます
- IndexNow は公開前ではなく、公開後に送信する運用です

## メモ

- 日本語コンテンツを多く含むため、編集時は UTF-8 を前提にします
- GitHub Pages 互換の都合で、Liquid は保守的な書き方を優先します
- テーマごとの差分を広げすぎず、構造やナビゲーションの一貫性を保つ方針です
