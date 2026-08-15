---
layout: page
title: 抽出方法の違いを整理（単純無作為・層化・集落・多段・系統）【DS検定】
description: "単純無作為抽出・系統抽出・層化無作為抽出・集落抽出・多段抽出の違いを、目的と選び方から整理します。特にDS検定で混同しやすい層化抽出と集落抽出を、精度・偏り・調査コストの観点で切り分けます。"
permalink: /ds/sampling-methods-comparison/
categories: [data-science]
tags: [ds, data-preparation, statistics]
prev: /ds/sample-variance-unbiased-variance/
next: /ds/significance-level-and-pvalue/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

抽出方法は、**母集団の中からどのように標本を選ぶか**を決める方法です。

| 方法 | 判断キーワード |
|---|---|
| 単純無作為抽出 | 全対象からランダム |
| 系統抽出 | 一定間隔 |
| 層化無作為抽出 | 層ごとに抽出して偏りを抑える |
| 集落抽出 | 集団単位で選び調査コストを抑える |
| 多段抽出 | 複数段階で絞る |

DS検定では特に、**層化抽出と集落抽出の目的の違い**を押さえるのが重要です。

## 直感的な説明

全国の家庭の電気使用量を調べるとしても、全家庭を調査するのは現実的ではありません。

そこで一部だけを選びますが、選び方によって

- 調査の精度
- コスト
- 偏りのリスク

が変わります。

つまり、サンプリングでは**「どう選ぶか」だけでなく「なぜその方法を選ぶか」**が大切です。

## 定義・仕組み

### 単純無作為抽出（Simple Random Sampling）

母集団からランダムに抽出する基本的な方法です。

- 例：住民名簿から乱数で100人を選ぶ
- 判断語：ランダム、同じ確率

### 系統抽出（Systematic Sampling）

最初の位置を決め、その後は**一定間隔**で抽出します。

- 例：最初の1人をランダムに選び、その後10人ごとに選ぶ
- 注意：並びに周期性があると偏る可能性がある

### 層化無作為抽出（Stratified Sampling）

母集団を属性などの**層**に分け、それぞれの層から抽出します。

- 例：20代・30代・40代に分け、それぞれから抽出
- 狙い：各層を標本に反映し、推定精度を高める

### 集落抽出（Cluster Sampling）

母集団を地域・学校などの**集落（クラスター）**に分け、一部の集落を選んで調査します。

- 例：全国から市区町村を選び、選ばれた地域を調査
- 狙い：調査範囲をまとめてコストを下げる

### 多段抽出（Multistage Sampling）

複数の段階を踏んで対象を絞ります。

1. 都道府県を抽出
2. 市町村を抽出
3. 世帯を抽出

大規模調査で現実的な標本設計を作るときに使います。

## どんな場面で使う？

| 目的 | 向いている方法 |
|---|---|
| シンプルにランダム抽出 | 単純無作為抽出 |
| 一覧から一定間隔で選ぶ | 系統抽出 |
| 各属性をきちんと含めたい | 層化無作為抽出 |
| 調査コストを抑えたい | 集落抽出 |
| 全国規模など段階的に絞りたい | 多段抽出 |

## よくある誤解・混同

### 層化抽出 vs 集落抽出

| 観点 | 層化抽出 | 集落抽出 |
|---|---|---|
| グループ分け | 属性などの層 | 地域・学校などの集落 |
| 抽出 | 各層から取る | 一部の集落を選ぶ |
| 主な狙い | 各層を反映・精度向上 | 調査コスト削減 |

**「全部の層から取る」なら層化、「一部の集団を選ぶ」なら集落**と考えると切り分けやすくなります。

### ❌ 無作為 = 適当に選ぶ

無作為抽出は、恣意的に選ばず**確率的なルールで選ぶ**という意味です。

## まとめ（試験直前用）

- ランダム → **単純無作為抽出**
- 一定間隔 → **系統抽出**
- 各層から抽出 → **層化無作為抽出**
- 一部の集落を選ぶ → **集落抽出**
- 複数段階 → **多段抽出**

DS検定では、**層化 = 各層を反映 / 集落 = 集団単位で効率化**で切り分けます。

## 対応スキル項目（データサイエンス力シート）

- 数理・統計基礎
- データの分布とサンプリング
- ★ 母集団と標本の違いを理解し、適切なサンプリング方法を説明できる

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
