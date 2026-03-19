---
layout: page
title: GROUP BYとは？データ集計の基本を理解する【DS検定】
permalink: /ds/sql-groupby/
categories: [data-engineering]
tags: [ds, sql]
prev: /ds/sql-filtering/
next: /ds/sql-having/
---

## まず結論

GROUP BYとは、データを特定の列でグループ化して集計するSQLの仕組みです。

DS検定では、WHERE（条件抽出）とGROUP BY（集計処理）の違いを理解しているかが問われることがあります。


つまり

WHERE → 行を絞る
GROUP BY → データをグループごとに集計する

と整理できることが重要です。



## 直感的な説明

例えば、次のような売上データがあるとします。

顧客	商品	売上

田中	ノートPC	120000
佐藤	マウス	3000
田中	キーボード	8000
佐藤	モニター	30000


ここで

「顧客ごとの売上合計」

を知りたい場合があります。

このときに使うのが GROUP BY です。

結果は次のようになります。

顧客	売上合計

田中	128000
佐藤	33000


つまり

同じ値を持つ行をまとめて集計する

のがGROUP BYです。



## 定義・仕組み

GROUP BYとは

指定した列の値ごとにデータをグループ化するSQLの構文です。

基本構文

SELECT 列, 集計関数
FROM テーブル
GROUP BY 列

例

SELECT customer, SUM(sales)
FROM orders
GROUP BY customer

このSQLは

顧客ごとの売上合計を計算する

という意味になります。

よく使う集計関数

関数	意味

COUNT	件数
SUM	合計
AVG	平均
MAX	最大値
MIN	最小値


例えば

SELECT customer, COUNT(*)
FROM orders
GROUP BY customer

これは

顧客ごとの注文数を集計しています。



## どんな場面で使う？

GROUP BYはデータ分析で非常によく使われます。

例えば

売上分析

商品別売上

顧客別売上




マーケティング分析

地域別顧客数

年齢層別購入数




業務分析

担当者別売上

部門別コスト


このように

データをカテゴリーごとにまとめて分析する場合に使います。



## よくある誤解・混同

① WHEREとGROUP BYを混同する

SQL	役割

WHERE	行を条件で絞る
GROUP BY	グループ化して集計


WHEREは

集計前のデータを絞る処理

GROUP BYは

データをまとめて集計する処理

です。



② GROUP BYは並び替えと思ってしまう

GROUP BYは

並び替え（ORDER BY）ではありません。

役割は

データをグループ化すること

です。



③ 集計関数なしでもGROUP BYが必要な場合

SQLでは

SELECTにある列はGROUP BYに含める必要がある

というルールがあります。

DS検定ではこのルールが選択肢のひっかけになることがあります。



## まとめ（試験直前用）

GROUP BY = データをグループ化して集計するSQL

COUNT / SUM / AVGなどの集計関数と一緒に使う

WHEREは条件抽出、GROUP BYは集計処理

DS検定では WHEREとGROUP BYの役割の違いがよく問われる


迷ったら

WHERE → 行を絞る
GROUP BY → グループ化して集計

と覚えると判断しやすくなります。



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

[DS?? ???????????]({{ '/ds/' | relative_url }})
