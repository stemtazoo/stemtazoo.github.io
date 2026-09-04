---
layout: page
title: 機械学習アルゴリズム一覧チートシート（教師あり・教師なし・強化学習）【DS検定】
description: "機械学習アルゴリズムを、正解ラベルから分類・回帰を学ぶ教師あり学習、ラベルなしデータの構造を探すクラスタリング・次元削減、報酬を手掛かりに行動方策を学ぶ強化学習へ分類します。予測対象、与えられる教師情報、出力の目的から代表手法を選び、分類とクラスタリングなどの混同を防ぐ一覧です。"
permalink: /ds/machine-learning-algorithms-cheatsheet/
categories: [data-science]
tags: [ds, modeling]
ds_area: datascience
ds_section: modeling
prev: /ds/logistic-regression/
next: /ds/machine-learning-methods/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

機械学習アルゴリズムは、まず**教師あり・教師なし・強化学習**に分けると整理しやすくなります。

| 学習タイプ | 主な目的 |
|---|---|
| 教師あり学習 | 正解付きデータから予測・分類 |
| 教師なし学習 | 正解なしで構造やグループを発見 |
| 強化学習 | 報酬を手掛かりに行動を学習 |

DS検定では、**アルゴリズム名 → 学習タイプ → 用途**の順に判断できることが重要です。

## 直感的な説明

| 目的 | 代表アルゴリズム |
|---|---|
| 数値予測 | 線形回帰 |
| 分類 | ロジスティック回帰・SVM |
| グループ分け | k-means |
| 画像認識 | CNN |
| 物体検出 | YOLO |
| 文章生成 | GPT |

## 定義・仕組み

### 教師あり学習

#### 回帰

| アルゴリズム | 特徴 |
|---|---|
| 線形回帰 | 基本的な回帰モデル |
| リッジ回帰 | L2正則化で過学習を抑える |
| Lasso回帰 | L1正則化で係数を0にしやすい |

#### 分類

| アルゴリズム | 特徴 |
|---|---|
| ロジスティック回帰 | 代表的な分類モデル |
| k近傍法（kNN） | 近いデータから判断 |
| SVM | マージンを最大化 |
| 決定木 | 条件分岐で判断 |
| ランダムフォレスト | 複数の決定木を組み合わせる |
| 勾配ブースティング | 弱学習器を順に改善 |

### 教師なし学習

#### クラスタリング

| アルゴリズム | 特徴 |
|---|---|
| k-means | 代表的なクラスタリング |
| 階層クラスタリング | 階層構造を作る |
| DBSCAN | 密度ベース |

#### 次元削減

| アルゴリズム | 特徴 |
|---|---|
| PCA | 主成分へ圧縮 |
| t-SNE | 可視化向け |
| UMAP | 高次元データの可視化など |

### 強化学習

| アルゴリズム | 特徴 |
|---|---|
| Q学習 | 代表的な価値ベース手法 |
| DQN | Q学習と深層学習を組み合わせる |
| 方策勾配法 | 方策を直接学習 |

### 深層学習でよく見る手法

| 手法 | 主な用途 |
|---|---|
| CNN | 画像認識 |
| RNN / LSTM | 系列データ |
| GAN | データ生成 |
| VAE | 生成・潜在表現 |
| YOLO | 物体検出 |
| Transformer | NLPなどの基盤構造 |
| GPT | 文章生成 |
| BERT | 文書理解・分類 |

## どんな場面で使う？

| 用途 | 代表例 |
|---|---|
| 売上予測 | 線形回帰 |
| 顧客セグメント | k-means |
| 画像認識 | CNN |
| 物体検出 | YOLO |
| 文章生成 | GPT |

## よくある誤解・混同

### ❌ ロジスティック回帰は回帰問題の手法

代表的には**分類**に使います。

### ❌ k-meansは教師あり学習

k-meansは**教師なし学習**です。

### ❌ YOLOは画像分類

YOLOは**物体検出**です。

### ❌ GANは分類モデル

GANは**生成モデル**です。

## まとめ（試験直前用）

- 教師あり → 正解あり
- 教師なし → 正解なし
- 強化学習 → 報酬で学習
- **ロジスティック回帰 = 分類**
- **k-means = 教師なし**
- **YOLO = 物体検出**
- **GAN = 生成**

DS検定では、アルゴリズム名だけでなく**何をする手法か**までセットで覚えましょう。

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
