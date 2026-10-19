---
layout: page
title: WHERE句とは？条件抽出の基本を理解する【DS検定】
permalink: /ds/sql-where/
categories: [data-engineering]
tags: [ds, data-processing, sql]
ds_area: dataengineering
ds_section: data-processing
prev: /ds/sql-union/
next: /ds/left-join-where/
description: "WHERE句を、条件がTRUEになる行を選ぶSQLの構文として整理します。売上の抽出前後、NULL、AND・OR、UPDATE・DELETEの対象指定、JOINやHAVINGとの違いを具体例で確認します。"
last_modified_at: 2026-10-19
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

WHERE句とは、SQLで**条件に一致する行だけを対象にするための構文**です。

DS検定では、次のように切り分けると判断しやすくなります。

- `JOIN`：テーブルを結合する
- `WHERE`：行を条件で絞り込む
- `HAVING`：集計後のグループを絞り込む

特に、WHEREは「データを表示するための条件」だけでなく、`UPDATE` や `DELETE` で**どの行を対象にするか**を指定する役割もあります。

## 直感的な説明

例えば、次の売上データがあるとします。

| 日付 | 店舗 | 売上 |
|---|---|---:|
| 4/1 | 東京 | 80万円 |
| 4/2 | 東京 | 120万円 |
| 4/3 | 大阪 | 90万円 |
| 4/4 | 東京 | 150万円 |

金額の表は万円単位、SQLで扱う`売上`列は円単位です。

「売上が100万円以上の日だけ知りたい」なら、必要な行は次の2件です。

| 日付 | 店舗 | 売上 |
|---|---|---:|
| 4/2 | 東京 | 120万円 |
| 4/4 | 東京 | 150万円 |

このように、**条件に合う行だけを残す**のがフィルタリングです。

SQLでは `WHERE` 句を使います。

```sql
SELECT *
FROM sales
WHERE 売上 >= 1000000;
```


## 定義・仕組み

WHERE句は、SQLで行を絞り込む条件を指定する部分です。

```sql
SELECT 列名
FROM テーブル名
WHERE 条件;
```

例えば、東京の顧客だけを取得するSQLは次の通りです。

```sql
SELECT name
FROM customers
WHERE city = 'Tokyo';
```

ここからは、`price`を円単位の価格列とする別の売上表の例で考えます。よく使う条件演算子は次の通りです。

| 演算子 | 意味 |
|---|---|
| `=` | 等しい |
| `<>` | 等しくない |
| `>` | より大きい |
| `<` | より小さい |
| `>=` | 以上 |
| `<=` | 以下 |

複数条件を組み合わせる場合は、`AND` や `OR` を使います。

| 条件指定 | 意味 |
|---|---|
| `AND` | すべての条件を満たす |
| `OR` | いずれかの条件を満たす |
| `IN` | 指定した値の集合に含まれる |
| `LIKE` | 文字列のパターンに一致する |
| `BETWEEN` | 両端を含む範囲に入る |

ANDとORを混ぜるときは、括弧で条件のまとまりを明確にします。

```sql
SELECT *
FROM sales
WHERE price >= 1000
  AND price < 10000;
```

### TRUE・FALSE・NULLの扱い

WHEREは、条件の結果が**TRUEの行だけ**を残します。FALSEやUNKNOWN（NULLに関わる不明な判定）の行は残りません。

例えば`price >= 1000`では、`price`がNULLの行は残りません。欠損を探す場合は`price IS NULL`を使い、`price = NULL`とは書き分けます。

DS検定では、SQLを完全に暗記するよりも、**条件が行に対して働くのか、集計後の結果に対して働くのか**を見分けることが重要です。

## どんな場面で使う？

WHERE句は、データ分析の前処理や確認作業で頻繁に使います。

### 売上分析

- 高額商品の行だけを抽出する
- 特定商品の売上だけを確認する
- 期間を絞って月次・年次の分析対象を作る

### 顧客分析

- 特定地域の顧客だけを取り出す
- 年齢や会員ランクで対象を絞る
- キャンペーン対象者の候補を抽出する

### ログ分析

- 特定日時のログだけを見る
- エラーが発生した行だけを抽出する
- あるユーザーIDの操作履歴を確認する

実務では、WHERE句の条件を間違えると「分析対象が多すぎる」「必要な行が消える」「更新対象を誤る」といったミスにつながります。

## よくある誤解・混同

### ① JOINとWHEREを混同する

| SQL | 役割 |
|---|---|
| `JOIN` | テーブルを結合する |
| `WHERE` | 条件に合う行を残す |

`JOIN` は表をつなぐ操作、`WHERE` は結合後または取得対象の行を絞る操作です。

基本形では、`JOIN ... ON`で表同士の対応、WHEREで取得する行の条件を表します。なお、複数の表をFROMに並べ、WHEREに表同士の対応条件を書く記法もあります。「WHEREでは表同士の対応を指定できない」とは一般化しません。

### ② WHEREとHAVINGを混同する

| 句 | 絞り込む対象 |
|---|---|
| `WHERE` | 集計前の行 |
| `HAVING` | `GROUP BY`で集計した後のグループ |

例えば「価格が1000円以上の明細行を抽出する」はWHEREですが、「売上合計が10万円以上の店舗を残す」はHAVINGが自然です。

### ③ WHEREはデータを変更する句だと思う

WHERE自体は「変更処理」ではありません。対象行を指定する条件です。

ただし、`UPDATE` や `DELETE` と一緒に使うと、更新・削除される行を決めます。

```sql
UPDATE customers
SET rank = 'gold'
WHERE total_amount >= 100000;
```

このため実務では、更新や削除のWHERE条件を誤ると影響範囲が大きくなります。

### ④ フィルタリングはデータ削除？

SELECTで条件に合う行だけを取得しても、元の行は消えません。一方、DELETEと組み合わせると削除対象を指定します。**句の役割と、SQL全体で行う処理を分けて読みます。**

[GROUP BY](/ds/sql-groupby/)での集計、[HAVING](/ds/sql-having/)での集計後の条件、[LEFT JOINとWHERE](/ds/left-join-where/)でのNULL行の注意も関連します。

## まとめ（試験直前用）

- WHERE句は「条件に一致する行」を対象にするSQLの構文
- JOINはテーブル結合、WHEREは行の絞り込み
- WHEREは集計前、HAVINGは集計後の条件
- SELECTだけでなくUPDATEやDELETEでも対象行の指定に使う
- DS検定では「何を絞る条件か」を見れば選択肢を切りやすい

## 公式情報・参考リンク

- [PostgreSQL公式：Table Expressions](https://www.postgresql.org/docs/current/queries-table-expressions.html)
  - WHERE句によって条件を満たさない行がSELECT結果から除外される処理を確認できます。

## 対応スキル項目（ver.6 データエンジニアリング）

- **分類**：ITエンジニアリング
- **スキルカテゴリ**：プログラミング
- **サブカテゴリ**：SQL
- **必須スキル**：◯
- ★ SQLの構文を一通り知っていて、記述・実行できる（DML・DDLの理解、各種JOINの使い分け、集計関数とGROUP BY、CASE文を使用した縦横変換、副問合せやEXISTSの活用など）
- [ver.6 ★1スキルチェックで確認する](/ds/engineering-skillcheck/)
