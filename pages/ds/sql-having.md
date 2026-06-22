---
layout: page
title: HAVINGとは？WHEREとの違いを整理【DS検定】
description: "HAVINGは、GROUP BYで集計した結果に条件を付けるSQL構文です。WHEREとの処理順序の違い、集計前後の絞り込み、DS検定で迷いやすい集計条件の見分け方を整理します。"
permalink: /ds/sql-having/
categories: [data-engineering]
tags: [ds, data-processing, sql]
prev: /ds/sql-groupby/
next: /ds/sql-in-exists/
last_modified_at: 2026-06-22
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

HAVINGは、GROUP BYで集計した後の結果に条件を付けるSQL構文です。

DS検定では、**WHEREは集計前の行を絞る、HAVINGは集計後のグループを絞る**という処理タイミングの違いを判断できることが重要です。

## 直感的な説明

注文データから「売上合計が5万円以上の顧客」を探す場面を考えます。

| 顧客 | 商品 | 売上 |
|---|---|---:|
| 田中 | ノートPC | 120000 |
| 田中 | キーボード | 8000 |
| 佐藤 | マウス | 3000 |
| 佐藤 | モニター | 30000 |

最初から「売上合計」は各行には存在しません。まず顧客ごとにGROUP BYでまとめて、合計を計算する必要があります。

| 顧客 | 売上合計 |
|---|---:|
| 田中 | 128000 |
| 佐藤 | 33000 |

この集計結果に対して「50000以上」という条件をかけるのがHAVINGです。

## 定義・仕組み

HAVINGは、GROUP BYで作られたグループや集計結果に条件を指定します。

```sql
SELECT customer, SUM(sales) AS total_sales
FROM orders
GROUP BY customer
HAVING SUM(sales) >= 50000;
```

このSQLは、顧客ごとに売上を合計し、その合計が50000以上の顧客だけを返します。

処理の流れは、初学者向けには次の順で理解すると十分です。

1. FROMでテーブルを見る
2. WHEREで集計前の行を絞る
3. GROUP BYでグループ化する
4. HAVINGで集計後の結果を絞る
5. SELECTで表示する列を決める

## どんな場面で使う？

HAVINGは、集計した結果に条件を付けたいときに使います。

- 売上合計が一定以上の顧客を抽出する
- 注文回数が多い商品を探す
- 平均単価が一定以上の店舗を確認する
- グループごとの件数が少なすぎるデータを除外する

実務では、分析対象を「行」ではなく「顧客・商品・店舗などのまとまり」で判断したいときに使います。

## よくある誤解・混同

### ① WHEREとHAVINGを同じ条件指定だと思う

どちらも条件を書く構文ですが、対象が違います。

| 構文 | 絞り込む対象 | 例 |
|---|---|---|
| WHERE | 集計前の行 | `sales >= 1000` |
| HAVING | 集計後のグループ | `SUM(sales) >= 50000` |

DS検定では、「集計前か集計後か」を読むだけで誤答を切れることがあります。

### ② 集計関数をWHEREに書いてしまう

次のようなSQLは、考え方として誤りです。

```sql
SELECT customer, SUM(sales)
FROM orders
WHERE SUM(sales) >= 50000
GROUP BY customer;
```

`SUM(sales)` はGROUP BY後に計算されるため、WHEREではなくHAVINGに書きます。

### ③ HAVINGは何でもWHEREの代わりになると思う

行単位で絞れる条件は、基本的にはWHEREに書きます。先に不要な行を絞ってから集計した方が、意図も処理も分かりやすくなります。

## まとめ（試験直前用）

- HAVINGは集計後の結果に条件を付ける
- WHEREは集計前の行、HAVINGは集計後のグループを絞る
- `SUM` や `COUNT` などの集計条件はHAVINGで判断する
- GROUP BYとセットで読むと理解しやすい
- DS検定では「条件の対象が行か、集計結果か」を見る

## 対応スキル項目（データエンジニアリング力シート）

- スキルカテゴリ：プログラミング
- サブカテゴリ：SQL
- ★ SQLの構文を一通り知っていて、記述・実行できる（DML・DDLの理解、各種JOINの使い分け、集計関数とGROUP BY、CASE文を使用した縦横変換、副問合せやEXISTSの活用など）

## 🔗 関連記事

<ul style="padding-left: 20px;">
{% assign current_tags = page.tags %}
{% assign count = 0 %}

{% for p in site.pages %}
  {% if p.url != page.url and p.tags %}
    {% assign matched = false %}

    {% for tag in current_tags %}
      {% if p.tags contains tag and tag != "ds" %}
        {% assign matched = true %}
      {% endif %}
    {% endfor %}

    {% if matched %}
      <li style="margin-bottom: 6px;">
        <a href="{{ p.url }}">{{ p.title }}</a>
      </li>
      {% assign count = count | plus: 1 %}
    {% endif %}

    {% if count >= 5 %}
      {% break %}
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

<hr>

<div style="margin-top: 16px;">
  🏠 <a href="/ds/">DS検定トップに戻る</a>
</div>

<div style="display:flex;justify-content:space-between;margin-top:12px;">

  {% if page.previous.url %}
    <a href="{{ page.previous.url }}">← {{ page.previous.title }}</a>
  {% endif %}

  {% if page.next.url %}
    <a href="{{ page.next.url }}">{{ page.next.title }} →</a>
  {% endif %}

</div>
