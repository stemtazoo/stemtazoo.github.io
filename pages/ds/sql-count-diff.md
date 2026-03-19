---
layout: page
title: COUNTの違いとは？COUNT(*)・COUNT(列)・COUNT DISTINCTを整理【DS検定】
permalink: /ds/sql-count-diff/
categories: [data-engineering]
tags: [ds, sql]
---

## まず結論

COUNT(*)＝全行数（NULL含む）

COUNT(列)＝NULLを除いた件数

COUNT DISTINCT＝重複を除いたユニーク数

DS検定では「何を数えているか」を見抜く問題が頻出




## 直感的な説明

データが次のようにあったとします。

顧客ID
A
A
B
NULL

このとき

COUNT(*) → 4（全部数える）

COUNT(顧客ID) → 3（NULLは除く）

COUNT DISTINCT → 2（AとB）


👉 「何をカウントしているか」で結果が変わる



## 定義・仕組み

COUNT(*)

すべての行をカウント

NULLも含む


COUNT(列)

指定した列の「NULL以外」をカウント


COUNT DISTINCT

重複を除いた値の個数をカウント


基本形：

SELECT COUNT(*) FROM テーブル;
SELECT COUNT(列名) FROM テーブル;
SELECT COUNT(DISTINCT 列名) FROM テーブル;



## どんな場面で使う？

COUNT(*)

データ件数の確認


COUNT(列)

欠損（NULL）を除いた数を知りたいとき


COUNT DISTINCT

ユニーク数（顧客数・商品数など）




## よくある誤解・混同

❌ COUNT(列)は全件数

→ ⭕ NULLは数えない

👉 DS検定では「NULLを含むか」でひっかける



❌ COUNT(*)とCOUNT(列)は同じ

→ ⭕ NULLがあると結果が変わる



❌ COUNT DISTINCTはCOUNTと同じ

→ ⭕ 重複を除くため結果は小さくなる



❌ DISTINCTは行全体にかかる

→ ⭕ 列単位（または組み合わせ）で判定



## まとめ（試験直前用）

COUNT(*)＝全部（NULL含む）

COUNT(列)＝NULL除く

COUNT DISTINCT＝重複除く

「何を数えているか」で選択肢を切る

NULLと重複の扱いが最大のポイント




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
