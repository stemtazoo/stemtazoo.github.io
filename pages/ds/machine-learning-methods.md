---
layout: page
title: 機械学習の解析手法とは？（代表的アルゴリズムを整理）【DS検定】
description: "機械学習の解析手法とは、データからパターンを学習し予測や分類を行うアルゴリズムのことです。DS検定で問われる定義、具体例、似た概念との違い、選択肢の見分け方を整理します。主要な混同パターンや実務での読み取り方も確認します。初学者が迷いやすい判断ポイントも確認します。"
permalink: /ds/machine-learning-methods/
categories: [data-science]
tags: [ds, modeling]
ds_area: datascience
ds_section: modeling
prev: /ds/machine-learning-algorithms-cheatsheet/
next: /ds/market-basket-analysis/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

機械学習の解析手法は、まず次の3つに分けて整理すると判断しやすくなります。

| 学習タイプ | 基本イメージ |
|---|---|
| 教師あり学習 | 正解付きデータから予測・分類する |
| 教師なし学習 | 正解なしで構造やグループを見つける |
| 強化学習 | 試行錯誤しながら報酬が大きくなる行動を学ぶ |

DS検定では、**アルゴリズム名から学習タイプや用途を判断できること**が重要です。

## 直感的な説明

### 教師あり学習

**正解付きデータで学習する**方法です。

例：

- 過去の売上データ → 将来の売上を予測
- メール → スパムかどうか判定

### 教師なし学習

**正解なしでデータの構造を見つける**方法です。

例：顧客データから、

- 若年層グループ
- ファミリー層
- 高所得層

のような自然なグループを見つけます。

### 強化学習

**行動 → 報酬 → 学習**を繰り返し、よりよい行動を学ぶ方法です。

例：

- ゲームAI
- ロボット制御
- 自動運転の一部の学習問題

## 定義・仕組み

### 教師あり学習の代表手法

教師あり学習では、特徴量から目的変数との関係を学びます。

#### 回帰：数値を予測する

- 線形回帰
- リッジ回帰
- Lasso回帰

例：住宅価格予測、売上予測

#### 分類：カテゴリを予測する

- ロジスティック回帰
- k近傍法（kNN）
- サポートベクターマシン（SVM）
- 決定木
- ランダムフォレスト
- 勾配ブースティング

> **ひっかけ：** ロジスティック回帰は名前に「回帰」がありますが、代表的には**分類**に使います。

### 教師なし学習の代表手法

#### クラスタリング

似たデータをグループにまとめます。

- k-means
- 階層クラスタリング
- DBSCAN

例：顧客セグメント分析

#### 次元削減

多数の特徴を少ない軸へまとめます。

- 主成分分析（PCA）
- t-SNE
- UMAP

例：可視化、特徴の圧縮

### 強化学習の代表手法

- Q学習
- Deep Q Network（DQN）
- 方策勾配法
- Actor-Critic

### ニューラルネットワーク・深層学習でよく見る用語

| 用語 | 主な役割・用途 |
|---|---|
| CNN | 画像認識など |
| RNN / LSTM | 系列・時系列データ |
| GAN | 生成モデル |
| VAE | 生成・潜在表現 |
| YOLO | 物体検出 |
| Transformer | 自然言語処理などの基盤構造 |
| GPT | 文章生成など |
| BERT | 文書理解・分類など |

ここでは細部を暗記するより、**「何をするモデル・手法か」**を区別できることが重要です。

## どんな場面で使う？

| 目的 | 代表例 |
|---|---|
| 数値予測 | 線形回帰 |
| 顧客のグループ分け | k-means |
| 画像認識 | CNN |
| 物体検出 | YOLO |
| 文章生成 | GPT |

DS検定では、実務でよく使う手法だけでなく、**基礎アルゴリズムの役割を正しく切り分けること**が大切です。

## よくある誤解・混同

### ❌ 機械学習 = ディープラーニング

ディープラーニングは機械学習の一部です。

> AI ⊃ 機械学習 ⊃ ディープラーニング

### ❌ k-meansは教師あり学習

k-meansは**教師なし学習のクラスタリング**です。

### ❌ ロジスティック回帰は回帰問題だけに使う

ロジスティック回帰は、代表的には**分類問題**に使います。

### ❌ YOLOは画像分類

YOLOは代表的な**物体検出**の手法です。

## まとめ（試験直前用）

- **教師あり** → 正解あり、予測・分類
- **教師なし** → 正解なし、クラスタリング・次元削減
- **強化学習** → 行動と報酬から学ぶ
- **k-means = 教師なし**
- **ロジスティック回帰 = 分類**
- **YOLO = 物体検出**

DS検定では、**アルゴリズム名 → 学習タイプ・用途**の順で切り分けられるようにしておきましょう。

## 対応スキル項目（AI利活用スキルシート）

- **スキルカテゴリ名**：AI・人工知能
- **サブカテゴリ名**：機械学習
- ★ 機械学習にあたる解析手法の名称を3つ以上知っており、手法の概要を説明できる

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
