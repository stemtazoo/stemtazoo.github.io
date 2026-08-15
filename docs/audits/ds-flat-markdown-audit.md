# DS記事 平坦Markdown監査レポート

## 1. サマリー

- 対象: `pages/ds/**/*.md`
- チェックしたDS Markdownファイル数: **285**
- 候補数（score >= 4）: **116件**
- 内訳: **高 65件 / 中 35件 / 低 16件**
- 実行日: 2026-08-15
- 実行方法: `scripts/audit_ds_flat_markdown.py` を GitHub Actions 上で実行

この監査は、既存の `ds-markdown-structure-audit.md` では拾いにくかった「Markdown文法としては成立しているが、箇条書き・表・小見出しが不足し、公開ページで本文がただの文字列のように見える」記事を抽出するための補助監査です。

自動判定は修正対象の確定ではありません。数式、コード、短い説明文、意図したフロー表現なども候補になるため、**score順に目視確認してから修正する**ことを前提とします。

## 2. 判定シグナル

- 短い通常テキスト行が複数連続し、箇条書き候補に見える
- タブ区切りの擬似表がMarkdown表になっていない
- `①` `②` や `誤解①` などが小見出しになっていない
- `↓` などの矢印だけで構造を表現している
- `特徴` `意味` `覚えるポイント` などのラベルが通常テキストのまま
- 長い本文に対して見出し・箇条書き・表・強調などの構造要素が少ない

## 3. 最優先で目視確認する候補

GitHub Actionsで生成した全116件のうち、score上位は次の通りです。

| score | ファイル | 主な検出理由 |
|---:|---|---|
| 29 | `pages/ds/machine-learning-methods.md` | 短い通常行の連続、裸の `例` ラベル |
| 28 | `pages/ds/encoding.md` | タブ区切りの擬似表、短い通常行の連続 |
| 28 | `pages/ds/gantt-chart.md` | 短い通常行の連続、`① タスク` などの裸ラベル |
| 28 | `pages/ds/mapping.md` | タブ区切りの擬似表 |
| 27 | `pages/ds/categorical-variable.md` | タブ区切りの擬似表 |
| 27 | `pages/ds/data-extraction-vs-aggregation.md` | タブ区切りの擬似表 |
| 27 | `pages/ds/feature-engineering2.md` | タブ区切りの擬似表 |
| 27 | `pages/ds/revenue-equation.md` | 短い通常行の連続、裸の番号付きラベル |
| 26 | `pages/ds/critical-path.md` | 短い通常行の連続、裸の番号付きラベル |
| 26 | `pages/ds/digital-image-representation.md` | `① 標本化` `② 量子化` などの裸ラベル |
| 26 | `pages/ds/digital-signature2.md` | 裸の番号付きラベル、短い通常行の連続 |
| 26 | `pages/ds/malware.md` | タブ区切りの擬似表、短い通常行の連続 |
| 26 | `pages/ds/preprocessing.md` | タブ区切りの擬似表、短い通常行の連続 |
| 26 | `pages/ds/web-api.md` | 裸の番号付きラベル、短い通常行の連続 |
| 25 | `pages/ds/primary-key.md` | タブ区切りの擬似表 |
| 25 | `pages/ds/spark.md` | `① メモリ上で処理する` などの裸ラベル |
| 25 | `pages/ds/sql-groupby.md` | タブ区切りの擬似表 |
| 25 | `pages/ds/sql-join.md` | タブ区切りの擬似表 |
| 24 | `pages/ds/rest-api-methods.md` | タブ区切りの擬似表 |
| 24 | `pages/ds/sql-filtering.md` | タブ区切りの擬似表 |

## 4. 今回の症状と一致することを目視確認済みの記事

### `pages/ds/correlation-vs-causation.md`

自動監査では **score 7（中）** ですが、実際の本文を確認すると今回の `statistics-overview.md` と同型の問題があります。

- `気温` / `アイスクリームの売上` が裸の通常テキストで並ぶ
- `相関` / `因果` が小見出しではなく通常テキスト
- 広告費・売上・季節・キャンペーンなどの並列項目が箇条書きになっていない
- `覚えるポイント` が通常テキスト

この例から、**scoreが中でも修正効果が大きい記事がある**ことが分かります。

### 比較用に問題が小さい記事

- `pages/ds/covariance-and-correlation.md`
- `pages/ds/f-test.md`

これらは同じ時期の記事でも、`###` 小見出し、箇条書き、引用などが使われており、今回の症状は小さいと判断できます。

## 5. 監査結果の読み方

### 高（score >= 10）

`statistics-overview.md` と同型の可能性が比較的高い候補です。ただし、数式やコードブロックを含む記事では誤検出があり得ます。

### 中（score 6〜9）

記事全体ではなく、一部セクションだけ平坦なケースを含みます。今回確認した `correlation-vs-causation.md` のように、目視では修正価値が高い場合があります。

### 低（score 4〜5）

軽微な表記・装飾候補です。記事全体が読みやすければ修正不要です。

## 6. 推奨する修正順

自動scoreだけではなく、表示崩れに直結しやすいシグナルを優先します。

1. **タブ区切り擬似表**がある記事
2. **①②などの裸の番号付きラベル**が多い記事
3. **短い通常テキストが大量に連続**する記事
4. `覚えるポイント` `特徴` `意味` などが裸のラベルになっている記事
5. 矢印だけで長いフローを表現している記事

特にタブ区切り擬似表は、Markdown表に直すだけで表示改善が大きく、内容変更もほぼ不要なので優先度が高いです。

## 7. 修正方針

1. 内容や説明粒度を変えず、まずMarkdown構造だけを正常化する。
2. 並列項目は箇条書き、比較・データ例は表、節の役割を持つ行は `###` 小見出しにする。
3. 試験で選択肢を切る判断基準は太字で強調するが、強調しすぎない。
4. 修正後もDS記事の標準6見出しを維持する。
5. 自動監査のscoreだけで一括書き換えせず、記事ごとに目視確認する。

## 8. 再実行方法

ローカルでは次で全DS記事を再監査できます。

```bash
python scripts/audit_ds_flat_markdown.py
```

閾値を変更する場合:

```bash
python scripts/audit_ds_flat_markdown.py --min-score 6
```

GitHub Actionsの `DS flat Markdown audit` から手動実行することもできます。結果は `ds-flat-markdown-audit` artifact として保存されます。
