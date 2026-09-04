---
layout: page
title: クラスタ分析とは？似たデータをグループ分けする分析手法【DS検定】
description: "クラスタ分析を、正解ラベルのないデータを特徴の近さにもとづいてグループ分けする教師なし学習として整理します。クラスタ数を先に決めて重心へ割り当てるk-means法と、近い対象から段階的にまとめデンドログラムで表す階層型クラスタリングを比較し、既知ラベルを予測する分類や、次元を減らす主成分分析との混同を防ぎます。"
permalink: /ds/cluster-analysis/
categories: [data-science]
tags: [ds, modeling]
ds_area: datascience
ds_section: modeling
prev: /ds/basket-analysis/
next: /ds/cnn/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**クラスタ分析（Cluster Analysis）とは、似た特徴を持つデータを自動的にグループ分けする教師なし学習の手法**です。

DS検定では、**「正解ラベルなしで似たものをまとめる」**という点を押さえることが重要です。

## 直感的な説明

例えばECサイトの顧客には、

- 高頻度で購入する人
- 高額商品をよく買う人
- セール時だけ買う人

などさまざまなタイプがあります。

クラスタ分析は、こうした特徴の似ている顧客を自動的にまとめます。

## 定義・仕組み

クラスタ分析では、正解ラベルを与えず、データ同士の類似度からグループを作ります。

代表的な手法は次の通りです。

| 手法 | 特徴 |
|---|---|
| k-means | あらかじめクラスタ数を決め、重心に近いデータをまとめる |
| 階層クラスタリング | 近いデータから段階的にまとめ、階層構造を作る |

**判断ポイント：正解ラベルがない → 教師なし学習。**

## どんな場面で使う？

### 顧客セグメンテーション

顧客の属性や行動から、似たグループを作ります。

### マーケティング分析

クラスタごとに広告・商品・キャンペーンを変える判断に使えます。

### データ探索

データの中にどのような自然なまとまりがあるかを調べます。

## よくある誤解・混同

### ❌ クラスタ分析とアソシエーション分析は同じ

| 分析 | 何を見る？ |
|---|---|
| クラスタ分析 | 似たデータをグループ化 |
| アソシエーション分析 | 事象や商品の関連関係を発見 |

### ❌ クラスタ分析とRFM分析は同じ

| 分析 | 役割 |
|---|---|
| クラスタ分析 | データから自動的にグループを作る |
| RFM分析 | R・F・Mの3指標で顧客を評価する |

### ❌ クラスタ分析は分類問題

分類は**正解ラベルあり**、クラスタリングは**正解ラベルなし**です。

## まとめ（試験直前用）

- **クラスタ分析 = 似たデータをグループ化**
- 教師なし学習
- 顧客セグメンテーションでよく使う
- アソシエーション分析は関連関係を見る
- RFM分析は3指標で顧客価値を評価

DS検定では、**「似た特徴を持つデータを自動的にグループ化」ならクラスタ分析**と判断しましょう。

## 対応スキル項目（データサイエンス力シート）

- データ分析
- データ分析手法
- ★ データの特徴や関係性を把握するための基本的な分析手法を理解している

## 🔗 関連記事

<ul style="padding-left: 20px;">
{% assign current_tags = page.tags %}
{% assign count = 0 %}
{% for p in site.pages %}
  {% if p.url != page.url and p.tags %}
    {% assign matched = false %}
    {% for tag in current_tags %}
      {% if p.tags contains tag and tag != "ds" %}{% assign matched = true %}{% endif %}
    {% endfor %}
    {% if matched %}
      <li style="margin-bottom: 6px;"><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% assign count = count | plus: 1 %}
    {% endif %}
    {% if count >= 5 %}{% break %}{% endif %}
  {% endif %}
{% endfor %}
</ul>

<hr>
<div style="margin-top: 16px;">🏠 <a href="/ds/">DS検定トップに戻る</a></div>
<div style="display:flex;justify-content:space-between;margin-top:12px;">
  {% if page.previous.url %}<a href="{{ page.previous.url }}">← {{ page.previous.title }}</a>{% endif %}
  {% if page.next.url %}<a href="{{ page.next.url }}">{{ page.next.title }} →</a>{% endif %}
</div>
