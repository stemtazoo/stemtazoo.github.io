---
layout: page
title: EDA（探索的データ分析）とは？分析の第一歩を理解する【DS検定】
description: "EDA（探索的データ分析）とは、可視化や基本統計量を使ってデータの分布・関係・異常値・欠損などを確認し、分析前にデータを理解するプロセスです。DS検定で問われる役割と、機械学習・前処理との違いを整理します。"
permalink: /ds/eda/
categories: [business]
tags: [ds, visualization, design]
ds_area: datascience
ds_section: visualization
prev: /ds/design-thinking/
next: /ds/agile-development/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**EDA（Exploratory Data Analysis：探索的データ分析）**とは、可視化や基本統計量を使って**データの特徴や傾向を探索するプロセス**です。

DS検定では、次のような表現が判断材料になります。

- 分析の前にデータを理解する
- 分布や外れ値を確認する
- 変数同士の関係を見る
- 欠損や入力ミスに気づく

## 直感的な説明

売上データを分析するとき、いきなり機械学習モデルを作るのではなく、まず次を確認します。

- 売上の分布はどうなっているか
- 異常値はあるか
- 季節変動はあるか
- どの変数が関係しそうか

そのために、ヒストグラム・散布図・箱ひげ図・クロス集計などを使います。

**「まずデータをよく見る」**のがEDAです。

## 定義・仕組み

EDAでは主に次の3点を確認します。

### データの分布を理解する

ヒストグラムや箱ひげ図などを使い、偏りや外れ値を確認します。

### 変数同士の関係を確認する

散布図、相関係数、クロス集計などを使い、関係性のヒントを探します。

### データ品質を確認する

- 欠損値
- 異常値
- 入力ミス

などを確認します。EDAで見つかった問題が、その後の前処理につながります。

## どんな場面で使う？

### データ分析の最初

一般的には、**データ理解 → EDA → 前処理 → モデル分析**のように進めます。

### 機械学習前の確認

モデルを作る前に、分布・変数関係・外れ値などを把握しておくと、適切な前処理や特徴量設計を考えやすくなります。

### ビジネスデータ分析

売上、顧客、行動ログなどのデータでもEDAは使われます。

## よくある誤解・混同

### ❌ EDA = 機械学習モデルの作成

EDAは**モデルそのものではなく、データ理解のプロセス**です。

### ❌ EDAと仮説思考は対立する

実務では、仮説を持ちながら探索したり、EDAから新しい仮説を作ったりします。

### ❌ データ量が多ければEDAは不要

データ量が多くても、分布・欠損・外れ値・関係性の確認は必要です。

## まとめ（試験直前用）

- EDA = **探索的データ分析**
- 可視化や基本統計量でデータを理解する
- 分布・外れ値・変数関係・データ品質を確認する
- **モデル作成そのものではない**
- 「分析前にデータを探索する」ならEDA

## 対応スキル項目（データサイエンス力シート）

- データ理解
- データ前処理
- ★ データの分布や特徴を理解し、適切に可視化・探索できる

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
