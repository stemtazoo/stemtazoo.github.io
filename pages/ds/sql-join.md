---
layout: page
title: JOINとは？テーブル結合の基本を理解する【DS検定】
description: JOINはテーブル結合の基本を理解するを理解するための用語です。この記事では仕組み・役割・使いどころを押さえ、DS検定で問われる判断ポイントとひっかけポイントを解説します。
permalink: /ds/sql-join/
categories: [data-engineering]
tags: [ds, data-processing, sql]
prev: /ds/sql-in-exists/
next: /ds/sql-union/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

JOINとは、複数のテーブルを結合してデータを取得するSQLの仕組みです。

DS検定では、複数テーブルの情報を組み合わせて分析する場面で使うSQL操作として理解しておくことが重要です。


試験では
**「JOINはテーブル結合」**と理解しているかが問われることが多く、
WHEREとの違いや、結合の目的を理解しているかがポイントになります。



## 直感的な説明

例えば、次のような2つのテーブルがあるとします。

顧客テーブル

顧客ID	名前

1	田中
2	佐藤


注文テーブル

注文ID	顧客ID	商品

101	1	ノートPC
102	2	スマートフォン


このとき

「誰が何を買ったか」

を知りたい場合、
2つのテーブルを組み合わせる必要があります。

そこで使うのが JOIN です。

JOINを使うと

名前	商品

田中	ノートPC
佐藤	スマートフォン


のように

複数テーブルの情報を1つにまとめて取得できます。



## 定義・仕組み

JOINとは

複数のテーブルを共通の列（キー）で結合するSQLの機能

です。

基本構文

SELECT 列
FROM テーブルA
JOIN テーブルB
ON 結合条件

例

SELECT customers.name, orders.product
FROM customers
JOIN orders
ON customers.id = orders.customer_id;

このSQLでは

customers（顧客テーブル）

orders（注文テーブル）


を

顧客IDをキーとして結合しています。



## どんな場面で使う？

JOINはデータ分析で非常によく使われます。

例えば

売上分析

顧客テーブル
＋
注文テーブル

→ 顧客ごとの売上分析



ECサイト分析

商品テーブル
＋
注文テーブル

→ 商品別売上ランキング



ビジネス分析

顧客テーブル
＋
地域テーブル

→ 地域別売上分析

このように

データは複数テーブルに分かれて保存されるため、
分析ではJOINが必須になります。



## よくある誤解・混同

① JOINとWHEREを混同する

DS検定ではよく

JOINとWHEREの役割の違い

がひっかけになります。

SQL	役割

JOIN	テーブルを結合する
WHERE	データを条件で絞る


つまり

JOIN → テーブル結合

WHERE → 条件抽出


です。



② JOINはデータを追加する操作と思う

JOINは

データを変更するSQLではありません

あくまで

データを取得するときに結合する仕組み

です。



③ JOINは2テーブルだけと思う

JOINは

3つ以上のテーブルでも使用できます。

A JOIN B JOIN C

のように複数結合することも可能です。



## まとめ（試験直前用）

JOIN = 複数テーブルを結合するSQL

共通キーを使ってデータを組み合わせる

データ分析では頻繁に使う操作

DS検定では
JOIN（テーブル結合）とWHERE（条件抽出）を混同させる問題が多い


迷ったら

JOIN → テーブル結合
WHERE → 条件抽出

と覚えておくと選択肢を切りやすくなります。



## 対応スキル項目（データエンジニアリング力シート）

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
