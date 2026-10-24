---
layout: page
title: SQLのINとBETWEENの違いとは？値の指定と範囲検索を見分ける【基本情報技術者試験】
description: SQLのINは指定値のいずれか、BETWEENは両端を含む範囲から行を選ぶ条件です。ORによる書換え、AND・INTERSECTとの違いを商品データと操作できる抽出表で学びます。
permalink: /fe/sql-in-between/
tags: [fe, fe-technology, database, sql]
fe_section: テクノロジ系
fe_subsection: データベース
fe_order: 75
date: 2026-10-25
last_modified_at: 2026-10-25
related_articles:
  - /fe/sql-logical-operators/
  - /fe/relational-operations/
  - /fe/sql-aggregate-functions/
---

## まず結論

SQLの **IN** は「指定した値の**いずれか**に一致する行」、**BETWEEN** は「二つの値の**間の範囲**にある行」を選ぶ条件です。

基本情報技術者試験の科目Aでは、次の違いを押さえます。

| 条件 | 選び方 |
|---|---|
| IN ('M002', 'M004') | **M002 または M004 だけ** |
| BETWEEN 'M002' AND 'M004' | **M002からM004まで**（間のM003も含む） |

**IN＝値の列挙、BETWEEN＝範囲指定**と考えれば、どの行が抽出されるか判断できます。

## 直感的な説明

商品の仕入先を管理する表を考えます。次のデータは説明用のオリジナル例です。仕入先IDは同じ形式で、NULLはないものとします。

| 商品ID | 商品名 | 仕入先ID |
|---|---|---|
| P01 | ノートPC | M001 |
| P02 | USBハブ | M002 |
| P03 | キーボード | M003 |
| P04 | マウス | M003 |
| P05 | ディスプレイ | M004 |
| P06 | ケーブル | M004 |

M002とM004の仕入先の商品**だけ**を探すなら、INを使います。

~~~sql
SELECT *
FROM 商品
WHERE 仕入先ID IN ('M002', 'M004');
~~~

残るのは **P02・P05・P06 の3行**です。

一方、M002からM004までの**範囲全部**を探すなら、BETWEENを使います。

~~~sql
SELECT *
FROM 商品
WHERE 仕入先ID BETWEEN 'M002' AND 'M004';
~~~

M003の2行も含まれ、**P02・P03・P04・P05・P06 の5行**になります。

## 定義・仕組み

### INは列挙した値のいずれかに一致

~~~sql
WHERE 仕入先ID IN ('M002', 'M004')
~~~

指定した値のどれかに一致すれば対象です。次のOR条件と同じ行を選びます。

~~~sql
WHERE 仕入先ID = 'M002'
   OR 仕入先ID = 'M004'
~~~

INに並べた値は、連続している必要はありません。

### BETWEENは両端を含む範囲

~~~sql
WHERE 仕入先ID BETWEEN 'M002' AND 'M004'
~~~

これは次の範囲条件に相当します。

~~~sql
WHERE 仕入先ID >= 'M002'
  AND 仕入先ID <= 'M004'
~~~

**M002・M003・M004のすべて**が対象です。この例では、IDがM001、M002…の順で比較されるものとします。一般の文字列比較は照合順序などの影響を受けるため、すべての文字列に同じ順序が保証されるわけではありません。

### 条件を切り替えて、残る行を見比べる

条件ボタンを押すと、該当する行と件数が変わります。**見るポイント：M003の行が選ばれるかどうか**です。

<div class="fe-learning-demo fe-sql-conditions-demo" data-fe-sql-conditions-demo>
  <p class="fe-learning-demo__title">SQLの検索条件と該当行</p>
  <div class="fe-sql-conditions-demo__choices" role="group" aria-label="SQLの検索条件">
    <button type="button" class="fe-learning-demo__button" data-fe-sql-case="in" aria-pressed="true">IN</button>
    <button type="button" class="fe-learning-demo__button" data-fe-sql-case="or" aria-pressed="false">OR</button>
    <button type="button" class="fe-learning-demo__button" data-fe-sql-case="and" aria-pressed="false">AND</button>
    <button type="button" class="fe-learning-demo__button" data-fe-sql-case="between" aria-pressed="false">BETWEEN</button>
  </div>
  <p class="fe-sql-conditions-demo__sql" data-fe-sql-expression>仕入先ID IN ('M002', 'M004')</p>
  <p class="fe-sql-conditions-demo__result" role="status" aria-live="polite">該当：<strong data-fe-sql-count>3</strong> / 6行</p>
  <div class="fe-sql-conditions-demo__table-wrap">
    <table class="fe-sql-conditions-demo__table">
      <thead><tr><th scope="col">商品ID</th><th scope="col">商品名</th><th scope="col">仕入先ID</th><th scope="col">判定</th></tr></thead>
      <tbody>
        <tr data-fe-sql-supplier="M001" class="is-excluded"><td>P01</td><td>ノートPC</td><td>M001</td><td data-fe-sql-verdict>—</td></tr>
        <tr data-fe-sql-supplier="M002" class="is-matched"><td>P02</td><td>USBハブ</td><td>M002</td><td data-fe-sql-verdict>○</td></tr>
        <tr data-fe-sql-supplier="M003" class="is-excluded"><td>P03</td><td>キーボード</td><td>M003</td><td data-fe-sql-verdict>—</td></tr>
        <tr data-fe-sql-supplier="M003" class="is-excluded"><td>P04</td><td>マウス</td><td>M003</td><td data-fe-sql-verdict>—</td></tr>
        <tr data-fe-sql-supplier="M004" class="is-matched"><td>P05</td><td>ディスプレイ</td><td>M004</td><td data-fe-sql-verdict>○</td></tr>
        <tr data-fe-sql-supplier="M004" class="is-matched"><td>P06</td><td>ケーブル</td><td>M004</td><td data-fe-sql-verdict>○</td></tr>
      </tbody>
    </table>
  </div>
  <p class="fe-sql-conditions-demo__note" data-fe-sql-note>INは列挙したM002・M004だけ。間のM003は含みません。</p>
  <p class="fe-learning-demo__hint">○＝条件に一致、—＝一致しない。行の並びは説明用であり、SQLの出力順を保証するものではありません。</p>
  <noscript><p>JavaScript無効時はINの結果を表示しています。ORは3行、ANDは0行、BETWEENは5行になります。</p></noscript>
</div>

## 科目Aでどう出る？

指定した複数の値を選ぶのか、範囲内すべてを選ぶのかを見ます。

| 条件・演算 | この例の結果 | 理由 |
|---|---:|---|
| IN ('M002', 'M004') | 3行 | 二つの指定値だけ |
| M002 OR M004 | 3行 | いずれかに一致 |
| M002 AND M004 | 0行 | 同じ仕入先IDが同時に別の値にはならない |
| BETWEEN 'M002' AND 'M004' | 5行 | M003も範囲内 |
| M002の結果 INTERSECT M004の結果 | 0行 | 両方に共通する行がない |

**INTERSECT**は、二つのSELECT文の検索結果に**共通して含まれる行**を返す集合演算です。WHERE句の条件を結ぶANDとは構文が異なり、今回の例で結果がたまたま同じ0行になるだけです。

~~~sql
SELECT * FROM 商品 WHERE 仕入先ID = 'M002'
INTERSECT
SELECT * FROM 商品 WHERE 仕入先ID = 'M004';
~~~

試験では、**M003が結果に入っていないか**を確認すると素早く絞れます。

## どんな場面で使う？

例えば、特定の店舗IDや商品区分だけを選ぶときはIN、ある期間のデータを取得するときはBETWEENが役立ちます。

日付・時刻の範囲をBETWEENで指定するときは、**時刻まで含むか**にも注意します。終了日を日付だけで指定した場合に、その日の23時59分まで自動的に含むとは限りません。

## よくある誤解・混同

### INは指定した二つの値の間も選ぶ？

違います。INは**リスト内の値だけ**を選びます。間の値は自動的に追加されません。

### BETWEENは端の値を含まない？

含みます。通常のBETWEEN a AND b は **a以上・b以下**です。

### BETWEENのANDと普通のANDは同じ使い方？

BETWEEN a AND b は**範囲を指定する一つの構文**です。条件Aと条件BをANDでつなぐ場合と分けて理解します。

### 同じ列の二つの値をANDで結んだら二つとも選べる？

同じ仕入先IDがM002とM004に同時一致することはないため、この例では0行です。

### NULLが入っていても普通の文字列と同じ？

違います。SQLではNULLとの比較が不明（UNKNOWN）になる場合があります。今回の説明例にはNULLがないことを前提にしています。

AND・OR・NOTの詳しい論理演算と排他的論理和は、[SQLの論理演算子](/fe/sql-logical-operators/)で確認できます。

## まとめ（試験直前用）

- **IN＝指定値のどれか**。ORで書いた等価な条件に直せる
- **BETWEEN＝両端を含む範囲**。間の値も含む
- 同じ列に異なる値をANDで同時指定すると該当しない
- **INTERSECT＝二つの検索結果の共通部分**。ORと混同しない
- 検索結果を比べるときは、**指定値の間の値が含まれるか**を確認する

参考：[PostgreSQL公式｜BETWEENなどの比較演算](https://www.postgresql.org/docs/current/functions-comparison.html)／[PostgreSQL公式｜INTERSECTなどの集合演算](https://www.postgresql.org/docs/current/queries-union.html)

<link rel="stylesheet" href="{{ '/assets/css/fe-visualizer.css' | relative_url }}?v=20261025-sql-in">
<script src="{{ '/assets/js/fe-visualizer.js' | relative_url }}?v=20261025-sql-in" defer></script>

{% include fe_article_footer.html %}
