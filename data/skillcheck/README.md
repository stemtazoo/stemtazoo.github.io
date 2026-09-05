# skillcheck data

スキルチェックリスト（データサイエンティスト協会）のデータを**バージョンごと**に保持するためのディレクトリです。

## 現在の正本

2026年DS検定向けの正本は、公式 **スキルチェックリスト ver.6.00（2025年版）** です。

- 基盤: 33項目（★ 21）
- 価値創造: 153項目（★ 51）
- データサイエンス: 354項目（★ 108）
- データエンジニアリング: 180項目（★ 58）
- 融合: 125項目（★ 0）
- 合計: 845項目
- DS検定の4領域に含まれる★1: 238項目

`価値創造力` シートは1行に ★ / ★★ / ★★★ の3レベルが横持ちされているため、出力時に**1レベル1行の縦長形式**へ正規化します。

## ディレクトリ構成

- `raw/`
  - 取得した公式xlsxを保存（再現性確保）
- `versions/<version>/skillcheck.csv`
  - 全領域を1レベル1行に正規化した正本
- `versions/<version>/skillcheck.json`
  - 上記と同じ内容のJSON
- `versions/<version>/exam_star1.json`
  - DS検定対象の4領域（基盤 / 価値創造 / データサイエンス / データエンジニアリング）の★1のみ
- `versions/<version>/skilllevel_definition_<year>.csv/json`
  - その版に対応するスキルレベル定義
- `versions/<version>/change_mapping_datascience.csv/json`
  - ver.6に含まれるデータサイエンス力の新旧対応表
- `versions/<version>/change_mapping_dataengineering.csv/json`
  - ver.6に含まれるデータエンジニアリング力の新旧対応表
- `exports/latest.json`
  - 最新版の全項目エイリアス
- `exports/exam_star1_latest.json`
  - 最新版のDS検定★1エイリアス
- `exports/skilllevel_definition_latest.json`
  - 最新版のスキルレベル定義エイリアス
- `exports/index.json`
  - バージョン一覧、ハッシュ、領域別件数、★1件数などのマニフェスト

## 正規化列

ver.6では、既存列をできるだけ維持しながら次の情報を共通化します。

- `area`: `foundation` / `value-creation` / `datascience` / `dataengineering` / `fusion`
- `phase`: 価値創造のフェーズ
- `section`: DS / DE / 融合シートの「分類」
- `category`: スキルカテゴリ
- `subcategory`: サブカテゴリ
- `skill_level`: ★ / ★★ / ★★★
- `skill_level_rank`: 1 / 2 / 3
- `skill_definition`: 価値創造のスキル定義
- `item`: そのレベルで求められるチェック項目
- `required_skill`: 必須スキル表示
- `vc` / `ds` / `de` / `bz`: 他領域との関係を示す元シート列
- `old_division`: 基盤シートにある旧区分
- `source_url`: 公式xlsxのURL

## 運用ルール

1. 新しい公式版が出たら `scripts/build_skillcheck_data.py` を実行する。
2. 既存バージョンは削除せず保持する。
3. ver.6では `基盤` / `価値創造力` / `データサイエンス力` / `データエンジニアリング力` / `融合` を全データとして保持する。
4. DS検定ページでは原則 `exports/exam_star1_latest.json` を基準にする。
5. `融合` はver.6の重要領域だが★1が定義されていないため、DS検定★1エクスポートには含めない。
6. 表示や記事との対応付けでは、公式のスキル項目とブログ独自の `ds_area` / `ds_section` を混同しない。
7. 過去版比較や検証時は `versions/<version>/` と新旧対応表を参照する。

## 実行例

公式ver.6を取得して生成:

```bash
python scripts/build_skillcheck_data.py
```

ダウンロード済みのローカルファイルを使う場合:

```bash
python scripts/build_skillcheck_data.py \
  --xlsx ./tmp/skillcheck_ver6.00.xlsx \
  --version 6.00 \
  --source-url https://www.datascientist.or.jp/common/docs/skillcheck_ver6.00.xlsx
```

ver.5を再生成する場合も、`--xlsx` と `--version 5.00` を指定すれば旧4シート構造を判定して処理します。
