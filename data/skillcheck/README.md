# skillcheck data

スキルチェックリスト（DS協会）のデータを**バージョンごと**に保持するためのディレクトリです。

## ディレクトリ構成

- `raw/`
  - 取得した元のxlsxを保存（再現性確保）
- `versions/<version>/skillcheck.csv`
  - 正規化した正本（レビューしやすい）
- `versions/<version>/skillcheck.json`
  - ページ実装向けJSON
- `exports/latest.json`
  - 最新版のエイリアス
- `exports/index.json`
  - バージョン一覧・ハッシュ・件数のマニフェスト

## 運用ルール

1. 新しい公式版が出たら `scripts/build_skillcheck_data.py` を実行する。
2. 既存バージョンは削除せず保持する。
3. 表示側（`/pages/ds`）は原則 `exports/latest.json` を読む。
4. 過去版比較や検証時は `versions/<version>/` を参照する。

## 実行例

```bash
python scripts/build_skillcheck_data.py
```

ローカルファイルを使う場合:

```bash
python3 scripts/build_skillcheck_data.py --xlsx ./tmp/skillcheck_ver5.00_simple.xlsx --version 5.00
```
