---
layout: page
title: SQLのGROUP BYとは？集計関数・WHERE・HAVINGの見分け方【基本情報技術者試験】
description: SQLのGROUP BYで行をグループ化し、COUNT・SUM・AVGなどの集計関数を使う方法を、WHEREとHAVINGの違いや試験での誤答の切り方とあわせて解説します。
permalink: /fe/sql-group-by-aggregate-functions/
tags: [fe, fe-technology, database, sql]
fe_section: テクノロジ系
fe_subsection: データベース
fe_order: 120
date: 2026-08-03
last_modified_at: 2026-08-03
---

## まず結論

`GROUP BY` は、同じ値をもつ行をまとめ、グループごとに集計するために使います。

```sql
SELECT 注文日, AVG(数量)
FROM 注文明細
GROUP BY 注文日;
```

このSQLは、注文日ごとに行をまとめ、その日の平均数量を求めています。

基本情報技術者試験では、次の3点を判断できれば選択肢を切りやすくなります。

```text
SELECTに通常列と集計関数がある
→ 通常列をGROUP BYに指定する

集計前の行を絞る
→ WHERE

集計後のグループを絞る
→ HAVING
```

## 直感的な説明

注文データを日付ごとに箱へ分けるイメージです。

| 注文日 | 数量 |
|---|---:|
| 8月1日 | 10 |
| 8月1日 | 20 |
| 8月2日 | 15 |

`GROUP BY 注文日` を使うと、次のようにまとめられます。

```text
8月1日の箱
→ 10、20

8月2日の箱
→ 15
```

各箱に `AVG(数量)` を使うと、箱ごとの平均を求められます。

| 注文日 | 平均数量 |
|---|---:|
| 8月1日 | 15 |
| 8月2日 | 15 |

`GROUP BY` は、行を消す処理ではなく、**同じ値をもつ行を集計単位にまとめる処理**です。

## 定義・仕組み

### GROUP BY

`GROUP BY` は、指定した列の値が同じ行を一つのグループとして扱います。

```sql
SELECT 部署, COUNT(*)
FROM 社員
GROUP BY 部署;
```

このSQLは、部署ごとの社員数を求めます。

### 主な集計関数

| 関数 | 求めるもの |
|---|---|
| `COUNT` | 件数 |
| `SUM` | 合計 |
| `AVG` | 平均 |
| `MAX` | 最大値 |
| `MIN` | 最小値 |

例として、商品ごとの販売数量の合計を求める場合は次のように書きます。

```sql
SELECT 商品コード, SUM(数量)
FROM 売上明細
GROUP BY 商品コード;
```

### SELECTに通常列と集計関数がある場合

次のSQLでは、`注文日` は通常列、`AVG(数量)` は集計結果です。

```sql
SELECT 注文日, AVG(数量)
FROM 注文明細
GROUP BY 注文日;
```

グループごとに1行を返すため、集計されていない通常列は、原則として `GROUP BY` に指定します。

```text
SELECTに表示する通常列
→ GROUP BYへ

集計関数の中にある列
→ GROUP BYへ入れない
```

### WHERE

`WHERE` は、グループ化する前に元の行を絞ります。

```sql
SELECT 注文日, SUM(数量)
FROM 注文明細
WHERE 数量 >= 10
GROUP BY 注文日;
```

これは、数量が10以上の明細だけを使って、注文日ごとの合計を求めます。

### HAVING

`HAVING` は、グループ化して集計した後のグループを絞ります。

```sql
SELECT 注文日, SUM(数量)
FROM 注文明細
GROUP BY 注文日
HAVING SUM(数量) > 1000;
```

これは、合計数量が1000を超える注文日だけを残します。

### WHEREとHAVINGの違い

| 句 | 絞り込む対象 | 実行のタイミング |
|---|---|---|
| `WHERE` | 元の表の行 | グループ化前 |
| `HAVING` | 集計後のグループ | グループ化後 |

覚え方は次のとおりです。

```text
WHERE
→ 行を選ぶ

HAVING
→ グループを選ぶ
```

### SQLの論理的な処理順序

試験対策では、次の順番で考えると整理しやすくなります。

```text
FROM
↓
WHERE
↓
GROUP BY
↓
HAVING
↓
SELECT
↓
ORDER BY
```

`WHERE` の時点ではまだグループ化されていないため、通常は `SUM` や `AVG` などの集計結果を条件にできません。

公式の出題範囲やシラバスは、[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html)から確認できます。

## 科目Aでどう出る？

科目Aでは、正しいSQL構文を選ぶ問題や、`GROUP BY`、`WHERE`、`HAVING` の役割を切り分ける問題が出ます。

### 試験中のチェック手順

```text
1. SELECTに集計関数があるか確認する
2. 集計されていない通常列があるか確認する
3. 通常列がGROUP BYに指定されているか確認する
4. 条件が行に対するものか、集計結果に対するものか確認する
5. 集計結果の条件ならHAVINGか確認する
```

### 正しい形

```sql
SELECT 注文日, AVG(数量)
FROM 注文明細
GROUP BY 注文日;
```

`注文日` ごとにまとめ、各グループの平均数量を求めています。

### GROUP BYがない形

```sql
SELECT 注文日, AVG(数量)
FROM 注文明細;
```

`注文日` と集計結果を同時に表示しようとしていますが、注文日ごとのグループ化がありません。

FE試験では、不適切な構文として判断します。

### WHEREで集計関数を使う形

```sql
SELECT 注文日
FROM 注文明細
WHERE SUM(数量) > 1000
GROUP BY 注文日;
```

`WHERE` はグループ化前の行を絞るため、集計結果である `SUM(数量)` の条件には使えません。

正しくは次の形です。

```sql
SELECT 注文日
FROM 注文明細
GROUP BY 注文日
HAVING SUM(数量) > 1000;
```

### 集計関数を直接重ねる形

```sql
SELECT 注文日, AVG(SUM(数量))
FROM 注文明細
GROUP BY 注文日;
```

同じSELECTの階層で、集計関数を単純に重ねることはできません。

グループごとの合計をさらに平均したい場合は、サブクエリなどで一度集計結果を作ります。

```sql
SELECT AVG(日別合計)
FROM (
  SELECT 注文日, SUM(数量) AS 日別合計
  FROM 注文明細
  GROUP BY 注文日
) AS 日別集計;
```

ただし、試験ではまず、**集計関数が不自然に入れ子になっていないか**を確認すれば十分です。

## どんな場面で使う？

`GROUP BY` は、分類ごとの件数・合計・平均などを求める場面で使います。

例えば、次のような集計です。

- 日付ごとの売上合計
- 商品ごとの販売数量
- 部署ごとの社員数
- 顧客ごとの注文回数
- 月ごとの平均単価

データ分析では、pandasの `groupby` と近い考え方です。

```python
df.groupby("注文日")["数量"].mean()
```

SQLでもPythonでも、基本は次の流れです。

```text
分類する列を決める
↓
同じ値の行をまとめる
↓
合計・平均・件数を求める
```

## よくある誤解・混同

### SELECTにある列はすべてGROUP BYへ書く

集計関数の中にある列は、`GROUP BY` に指定しません。

```sql
SELECT 注文日, AVG(数量)
FROM 注文明細
GROUP BY 注文日;
```

この場合、`注文日` は通常列なので `GROUP BY` に指定しますが、`数量` は `AVG` の対象なので指定しません。

### GROUP BYを書けば集計関数が必須

必須ではありません。

```sql
SELECT 注文日
FROM 注文明細
GROUP BY 注文日;
```

このSQLは、注文日の重複をまとめた結果を返します。

ただし、実務や試験では集計関数と組み合わせる形が多く出ます。

### WHEREとHAVINGは書く位置だけが違う

役割が異なります。

```text
WHERE
→ 集計する前の行を絞る

HAVING
→ 集計した後のグループを絞る
```

### AVGの引数には列名しか書けない

通常の数値式は使えます。

```sql
AVG(単価 * 数量)
```

ただし、`AVG(SUM(数量))` のように、同じ階層で集計関数を直接重ねる形は不適切です。

### COUNT(*)とCOUNT(列名)は同じ

同じとは限りません。

```text
COUNT(*)
→ 行数を数える

COUNT(列名)
→ NULLでない値の件数を数える
```

NULLを含む可能性がある問題では、この違いに注意します。

## まとめ（試験直前用）

- `GROUP BY` は、同じ値の行をグループ化する
- `COUNT`、`SUM`、`AVG`、`MAX`、`MIN` は集計関数
- SELECTに通常列と集計関数がある場合、通常列は原則 `GROUP BY` に指定する
- `WHERE` は集計前の行を絞る
- `HAVING` は集計後のグループを絞る
- 集計結果を条件にするなら `HAVING`
- 同じ階層で集計関数を単純に重ねない
- 処理順序は `FROM → WHERE → GROUP BY → HAVING → SELECT`

```text
通常列＋集計関数
→ GROUP BYを確認

行の条件
→ WHERE

集計結果の条件
→ HAVING
```

{% include fe_article_footer.html %}
