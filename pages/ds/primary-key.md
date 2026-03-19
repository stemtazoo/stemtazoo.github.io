---
layout: page
title: 主キー（Primary Key）とは？データベースの基本ルールを理解【DS検定】
permalink: /ds/primary-key/
categories: [data-engineering]
tags: [ds, database]
prev: /ds/olap/
next: /ds/rdb-vs-nosql/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**主キー（Primary Key）とは、テーブルの中で1つのレコードを一意に識別するための列（または列の組み合わせ）**です。

DS検定では 「重複しない」「NULLにならない」識別子として理解できるかが重要です。




## 直感的な説明

データベースでは、同じようなデータがたくさん存在します。

例えば顧客テーブルを考えてみます。

顧客ID	名前

1001	田中
1002	鈴木
1003	田中


ここでは「田中」という名前が複数あります。

もし名前だけで管理すると、

どの田中さんなのか

どの注文に紐づくのか


が分からなくなります。

そこで 必ず1人だけを識別できる番号を用意します。

それが

**主キー（Primary Key）**です。



## 定義・仕組み

主キーとは

> テーブル内の各行（レコード）を一意に識別する列



です。

主キーには次の特徴があります。

① 重複してはいけない

同じ値が2つ存在すると、 レコードを区別できません。

例（NG）

顧客ID	名前

1001	田中
1001	鈴木


この場合、どちらのレコードか判断できません。



② NULLになってはいけない

主キーがNULLだと

「誰のレコードなのか」

を識別できなくなります。



③ 1テーブルに1つだけ設定

主キーは

1つのテーブルにつき1つだけ設定されます。

ただし、

複数列を組み合わせた

複合主キー（Composite Key）

という形もあります。

例

注文ID	商品ID	数量



この場合

注文ID + 商品ID

の組み合わせで1レコードを識別することがあります。



## どんな場面で使う？

主キーは すべてのテーブル設計で必ず使われる基本概念です。

例えば

顧客管理

顧客テーブル

顧客ID(PK)	名前





注文管理

注文テーブル

注文ID(PK)	顧客ID(FK)



ここで

顧客ID → 主キー

注文テーブル → 外部キー


という関係が作られます。

この仕組みによって

データの関係性（リレーション）

を管理できます。



## よくある誤解・混同

主キー = 一意制約ではない

DS検定ではここがよく出ます。

概念	内容

主キー	NOT NULL + UNIQUE
一意制約	重複のみ禁止


つまり

主キーは

一意制約よりも強いルールです。



主キーと外部キーの違い

用語	役割

主キー	テーブルの識別子
外部キー	他テーブルを参照する列


DS検定では

主キー = 識別

外部キー = 関係

と覚えておくと判断しやすいです。



DS検定の典型的なひっかけ

選択肢で次のような文章が出ます。

❌ 「主キーはNULLを許可できる」

これは誤りです。

主キーは

NULL不可

重複不可


です。



## まとめ（試験直前用）

主キーは レコードを一意に識別する列

主キーは NULL不可・重複不可

1テーブルに1つ設定

外部キーは主キーを参照する


DS検定では

主キー = 識別

という理解が重要です。



【対応スキル項目（データエンジニアリング力シート）】

データ管理

データベース


★ データベースの基本概念（テーブル、主キー、外部キーなど）を理解している ★ データの整合性や品質を保つ仕組みを理解している

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
