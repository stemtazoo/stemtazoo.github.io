---
layout: page
title: HAVINGとは？WHEREとの違いを整理【DS検定】
permalink: /ds/sql-having/
categories: [data-engineering]
tags: [ds, sql]
prev: /ds/sql-groupby/
next: /ds/sql-in-exists/
---

## まず結論

HAVINGとは、GROUP BYで集計した結果に対して条件を指定するSQLの仕組みです。

DS検定では、WHERE（行の条件）とHAVING（集計結果の条件）の違いを理解しているかがよく問われます。


整理すると

WHERE → 集計前の行を絞る
HAVING → 集計後の結果を絞る

という違いになります。



## 直感的な説明

例えば、次のような注文データがあるとします。

顧客	商品	売上

田中	ノートPC	120000
田中	キーボード	8000
佐藤	マウス	3000
佐藤	モニター	30000


ここで

「売上合計が5万円以上の顧客だけ知りたい」

とします。

まずGROUP BYで顧客ごとに集計します。

顧客	売上合計

田中	128000
佐藤	33000


そして

売上合計が50000以上の顧客だけを取り出します。

このときに使うのが HAVING です。



## 定義・仕組み

HAVINGとは

GROUP BYで集計した結果に対して条件を指定するSQLの構文です。

基本構文

SELECT 列, 集計関数
FROM テーブル
GROUP BY 列
HAVING 条件

例

SELECT customer, SUM(sales)
FROM orders
GROUP BY customer
HAVING SUM(sales) >= 50000

このSQLは

売上合計が50000以上の顧客だけ取得する

という意味になります。



## どんな場面で使う？

HAVINGは、

集計結果に条件をつけたい場合に使います。

例えば

売上分析

売上が一定以上の顧客

売上が少ない商品




マーケティング分析

購入回数が多い顧客

注文数が多い商品




業務分析

売上が多い店舗

利用回数が多いサービス


このように

集計した結果をさらに絞り込みたい場合に使用します。



## よくある誤解・混同

① WHEREとHAVINGを混同する

DS検定で非常に多いひっかけです。

SQL	役割

WHERE	行の条件（集計前）
HAVING	集計結果の条件


つまり

WHERE → 行を絞る

HAVING → 集計結果を絞る


です。



② HAVINGはGROUP BYなしでも使えると思う

基本的には

HAVINGはGROUP BYとセットで使う

構文です。

DS検定では

「HAVINGはGROUP BYのあとに使う」

という理解があれば十分です。



③ WHEREで集計条件を書いてしまう

例えば

WHERE SUM(sales) > 50000

これは誤りです。

集計関数の条件はHAVINGで指定します。



## まとめ（試験直前用）

HAVING = 集計結果に条件をつけるSQL

GROUP BYとセットで使う

WHEREは行の条件、HAVINGは集計結果の条件

DS検定では WHEREとHAVINGの違いが頻出ポイント


迷ったら

WHERE → 集計前の行
HAVING → 集計後の結果

と覚えると選択肢を切りやすくなります。



対応スキル項目

【対応スキル項目（データエンジニアリング力シート）】

スキルカテゴリ：プログラミング

サブカテゴリ：SQL


★ SQLの構文を一通り知っていて、記述・実行できる（DML・DDLの理解、各種JOINの使い分け、集計関数とGROUP BY、CASE文を使用した縦横変換、副問合せやEXISTSの活用など）

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

---

[DS検定 学習まとめトップに戻る]({{ '/ds/' | relative_url }})
