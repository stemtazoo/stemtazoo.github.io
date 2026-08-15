---
layout: page
title: データ前処理（Preprocessing）とは？分析前に行う重要ステップ【DS検定】
description: "データ前処理は、分析や機械学習の前に欠損値、外れ値、重複、表記ゆれ、尺度の違いを整える作業です。クレンジング、変換、標準化、カテゴリ変数処理との関係、前処理がモデル精度や解釈に与える影響、分析前の品質確認方法の観点をDS検定向けに整理します。"
permalink: /ds/preprocessing/
categories: [data-science]
tags: [ds, data-preparation, preprocessing]
prev: /ds/nlp-cleaning/
next: /ds/regular-expression-basic/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**データ前処理とは、分析や機械学習を行う前にデータを整える作業**です。

DS検定では、モデルを作る前に**データ品質を整える工程**として理解できることが重要です。

## 直感的な説明

売上データを分析しようとしても、実際のデータには、

- 欠損値がある
- 商品名などの表記が揺れている
- 文字データが混ざっている
- 数値の尺度が大きく異なる

といった問題があります。

そこで、

- 欠損値を補完・削除する
- データ形式をそろえる
- カテゴリを数値化する
- 数値のスケールを調整する

といった処理を行います。

このように、**データを分析できる状態に整える作業**がデータ前処理です。

## 定義・仕組み

代表的な前処理は次の通りです。

| 処理 | 内容 |
|---|---|
| 欠損値処理 | 空白データを補完・削除する |
| エンコーディング | カテゴリ変数を数値化する |
| 正規化・標準化 | 数値のスケールを調整する |
| マッピング | 値を別の値へ対応づけて変換する |
| 特徴量エンジニアリング | 新しい特徴量を作成・変換する |

> **判断ポイント：** 前処理は「モデルを学習させること」ではなく、**学習前にデータを整えること**です。

## どんな場面で使う？

### ① 機械学習モデルを作る前

- 欠損値
- データ形式
- スケール
- カテゴリ変数

などを整えます。

前処理が不十分だと、モデルが学習できなかったり、性能や解釈に悪影響が出たりします。

### ② 統計分析・BI分析

機械学習だけでなく、統計分析やBIでもデータ形式や表記をそろえる前処理が必要です。

つまり、前処理は**データ分析全体の基礎工程**です。

## よくある誤解・混同

### ❌ 前処理 = データ収集

- **データ収集** → データを集める
- **前処理** → 集めたデータを整える

### ❌ 前処理 = モデル学習

一般的な流れは、

> **前処理 → モデル学習 → 評価**

です。

### ❌ 特徴量エンジニアリングと完全に同じ

特徴量エンジニアリングは、前処理と重なる部分がありますが、特に**モデルに役立つ特徴量を作成・変換すること**に焦点を置く考え方です。

## まとめ（試験直前用）

- **データ前処理 = 分析前にデータを整える作業**
- 欠損値処理・エンコーディング・正規化などが代表例
- **収集ではなく整理**
- **モデル学習の前に行う**

DS検定では、**「分析可能な形にデータを整える工程」なら前処理**と判断しましょう。

## 対応スキル項目（データサイエンス力シート）

- データ理解・前処理
- データ加工
- ★ データの前処理（欠損値処理、正規化、カテゴリ変数の処理など）を理解している

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
