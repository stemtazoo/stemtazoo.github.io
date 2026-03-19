---
layout: page
title: 自己結合とは？同じテーブルを結合する理由を理解する【DS検定】
permalink: /ds/self-join/
categories: [data-engineering]
tags: [ds, sql]
prev: /ds/left-join-where/
next: /ds/batch-vs-stream/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

自己結合（Self Join）とは、同じテーブルを2回使って結合するSQL処理です。

DS検定では
「同じテーブル内のデータ同士を結びつける」ケースで使われます。

ポイントは

テーブルが1つしかない

しかし 別の行の情報を取得したい


という状況です。



## 直感的な説明

自己結合は

「同じ表の中の別の行を参照する」

ために使います。

例えば次の 社員テーブルを考えます。

社員テーブル

社員ID	名前	上司ID

1	田中	3
2	鈴木	3
3	山本	NULL


この表には

社員の名前

上司のID


はあります。

しかし

上司の名前はありません。

つまり

社員	上司

田中	?
鈴木	?


という状態です。

ここで

上司ID = 社員ID

を使って
同じテーブルを結合します。

自己結合のイメージ

社員テーブル（社員）
×
社員テーブル（上司）



自己結合の結果

社員	上司

田中	山本
鈴木	山本
山本	NULL


ここで初めて

上司の名前を取得できます。

つまり自己結合とは

同じテーブルの別の行の情報を取得する処理

です。



## 定義・仕組み

自己結合とは

同じテーブルに別名（エイリアス）を付けてJOINすることです。

SQLでは次のように書きます。

SELECT
  e1.name AS 社員,
  e2.name AS 上司
FROM employees e1
LEFT JOIN employees e2
ON e1.manager_id = e2.employee_id;

ここで

e1 は「社員として見る employees」

e2 は「上司として見る employees」

です。

つまり、

同じテーブルを役割別に2回使っている

のが自己結合のポイントです。



## どんな場面で使う？

自己結合は次のような場面で使われます。

社員と上司の関係

商品カテゴリの親子関係

組織ツリー

前日データとの比較


例えばカテゴリテーブルで、

親カテゴリID

子カテゴリID


を持っていれば、

同じテーブル同士を結合して親カテゴリ名を取得できます。



## よくある誤解・混同

混同①：自己結合は特別なJOIN構文

自己結合は特別な構文ではなく、

同じテーブルに別名を付けて通常のJOINをする

だけです。



混同②：同じテーブルだからJOINできない

実際には、

エイリアスを使えば別テーブルのように扱える

ため問題なく結合できます。



混同③：自己結合は常に親子関係だけに使う

自己結合は親子関係だけでなく、

同一テーブル内で別行同士を比較したい場面全般

で使えます。



## まとめ（試験直前用）

自己結合＝同じテーブルを2回使って結合すること

エイリアスを付けて役割を分ける

社員と上司、親と子などの関係表現でよく使う

DS検定では「同じテーブル内の別行を対応づける」と理解する



## 対応スキル項目（データエンジニアリング力シート）

データ操作

SQL

★ 同一テーブルを別名で結合して関係を取り出せる

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
