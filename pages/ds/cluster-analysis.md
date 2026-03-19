---
layout: page
title: クラスタ分析とは？似たデータをグループ分けする分析手法【DS検定】
permalink: /ds/cluster-analysis/
categories: [data-science]
tags: [ds, modeling]
prev: /ds/basket-analysis/
next: /ds/cnn/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**クラスタ分析（Cluster Analysis）**とは、似た特徴を持つデータ同士を自動的にグループ分けする分析手法です。

DS検定では 教師なし学習の代表的な手法として出題され、顧客セグメンテーションなどの例で問われることが多いです。


DS検定では特に

アソシエーション分析

RFM分析


との違いを判断できるかが重要になります。



## 直感的な説明

例えばECサイトの顧客データを考えます。

顧客には次のような違いがあります。

若い顧客

高額商品をよく買う顧客

セールのときだけ買う顧客


これらを人間が手作業で分類するのは大変です。

そこでデータの特徴から

似ている顧客を自動的にグループ化する

のがクラスタ分析です。

例えば次のようなグループが見つかることがあります。

高頻度購入グループ

高額購入グループ

セール購入グループ


このように

似た行動パターンのデータをまとめる分析がクラスタ分析です。



## 定義・仕組み

クラスタ分析は

データの特徴の類似度をもとにグループ分けする分析手法

です。

このとき

正解ラベル

教師データ


は存在しません。

そのためクラスタ分析は

教師なし学習（Unsupervised Learning）

に分類されます。

代表的なアルゴリズムには

k-means

階層クラスタリング


などがあります。

DS検定では

データを似たグループに分ける


という理解ができていれば十分です。



## どんな場面で使う？

クラスタ分析は次のような場面で使われます。

顧客セグメンテーション

顧客の行動や属性をもとに

若年層

高額購入層

割引志向層


などのグループを作ります。



マーケティング分析

顧客グループごとに

広告

商品

キャンペーン


を変えることができます。



データ探索

データにどのようなパターンがあるかを調べるために使われます。



## よくある誤解・混同

DS検定では次の分析との違いがよく問われます。

アソシエーション分析との違い

分析	内容

クラスタ分析	似たデータをグループ分けする
アソシエーション分析	事象の関連関係を見つける


例

クラスタ分析
→ 顧客グループ分け

アソシエーション分析
→ 商品の同時購入



RFM分析との違い

分析	内容

クラスタ分析	データを自動的にグループ分け
RFM分析	3指標で顧客価値を評価


DS検定では

> 顧客を似た特徴でグループ分けする



と書かれていたら クラスタ分析です。



## まとめ（試験直前用）

クラスタ分析は 似たデータをグループ分けする分析

教師なし学習の代表例

顧客セグメンテーションなどに使われる

アソシエーション分析は 商品関係の分析

RFM分析は 顧客価値の評価


DS検定では

> 「似た特徴を持つデータをグループ化する」



と書かれていたら

クラスタ分析と判断するのがポイントです。



## 対応スキル項目（データサイエンス力シート）

データ分析

データ分析手法

★ データの特徴や関係性を把握するための基本的な分析手法を理解している

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
