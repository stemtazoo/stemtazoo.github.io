---
layout: page
title: COUNT DISTINCTとは？ユニーク数を数える方法【DS検定】
permalink: /ds/sql-count-distinct/
categories: [data-engineering]
tags: [ds, sql]
---

## まず結論

COUNT DISTINCTとは「重複を除いたユニークな件数を数える」SQLの機能

DS検定では「重複込みの件数か、ユニーク数か」を見抜けるかが重要




## 直感的な説明

例えば、購入履歴が次のようになっているとします。

Aさん
Aさん
Bさん
Aさん

このとき

COUNT → 4件（全部数える）

COUNT DISTINCT → 2人（Aさん・Bさん）


👉 「種類の数」を知りたいときに使うのがCOUNT DISTINCT



## 定義・仕組み

COUNT DISTINCTは、重複を除いた値の個数を数えるSQL関数です。

基本形：

SELECT COUNT(DISTINCT 列名) FROM テーブル名;

例：

SELECT COUNT(DISTINCT 顧客ID) FROM 売上テーブル;

👉 何人の顧客がいるか（ユニーク数）を取得できる

ポイント：

重複は1つとしてカウント

NULLはカウントされない




## どんな場面で使う？

よく使う場面

ユニークユーザー数（UU）

商品の種類数

利用した顧客数


注意が必要な場面

総件数を知りたいとき → COUNTと混同しやすい

データの回数が重要なとき → 重複を消すと意味が変わる




## よくある誤解・混同

❌ COUNTと同じ

→ ⭕ COUNTは「全部数える」

COUNT：行数（重複込み）

COUNT DISTINCT：種類数（重複なし）


👉 DS検定ではここが典型的なひっかけ



❌ DISTINCTを使ってからCOUNTするのと同じ

→ ⭕ 結果は同じでも意味の理解が重要

SELECT COUNT(DISTINCT A)

は

SELECT COUNT(*) FROM (SELECT DISTINCT A ...)

と同じ意味だが、 👉 「ユニーク数を数えている」と理解することが重要



❌ NULLも数える

→ ⭕ NULLはカウントされない

選択肢で 「NULLも含めて数える」 → ❌ 誤り



## まとめ（試験直前用）

COUNT＝全部の件数

COUNT DISTINCT＝ユニーク数

重複は1つとして数える

NULLはカウントされない

「種類の数か？」と考えるのがコツ




【対応スキル項目（データエンジニアリング力シート）】

データ基盤

データ操作

★ SQLを用いた基本的なデータ操作（検索・集計・結合等）ができる

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
