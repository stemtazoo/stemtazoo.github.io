# stemtazoo.github.io
## NotebookLM向け DS エクスポート

`pages/ds/*.md` を NotebookLM に読み込ませやすい Markdown に変換するため、
`scripts/export_ds_notebooklm.py` を追加しています。

### 使い方

- `pages/ds/index.md` の `ds_sections` を分類定義として使う（デフォルト）

```bash
python scripts/export_ds_notebooklm.py
```

- 独自分類（例: スキルチェックリスト単位）を JSON で渡す

```bash
python scripts/export_ds_notebooklm.py \
  --groups-file exports/notebooklm/ds/groups.template.json
```

### 出力

- `exports/notebooklm/ds/sections/*.md` : 分類ごとのファイル
- `exports/notebooklm/ds/all.md` : 全分類を結合した1ファイル

### 新規記事追加時の更新手順

1. `pages/ds/` に記事を追加
2. `pages/ds/index.md` の `ds_sections` または独自 JSON 分類を更新
3. 次を実行して再出力

```bash
python scripts/export_ds_notebooklm.py
```

必要なら `scripts/lint_ds_frontmatter.py` で front matter の整合性確認も可能です。
