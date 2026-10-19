---
layout: page
title: 機械学習の解析手法とは？（代表的アルゴリズムを整理）【DS検定】
permalink: /ds/machine-learning-methods/
categories: [data-science]
tags: [ds, modeling]
ds_area: datascience
ds_section: modeling
next: /ds/market-basket-analysis/
description: "教師あり・教師なし・強化学習を、正解情報・報酬と用途から区別します。代表アルゴリズムの早見表と、学習タイプとCNN・Transformerなどの構造名を混同しない判断を整理します。"
last_modified_at: 2026-10-19
prev: /ds/logistic-regression/
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
| Actor-Critic | 方策と価値の推定を組み合わせる |

### モデル構造・モデル名と学習タイプは別の軸

CNNやTransformerはモデルの構造を表す名前です。**構造名だけで、教師あり・教師なし・強化学習のどれかが一意に決まるわけではありません。** 次の表は代表的な用途をまとめたものです。

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

### ❌ GANは分類モデル

GANは代表的な**生成モデル**です。分類、検出、生成という出力の目的も区別します。

## まとめ（試験直前用）

- **教師あり** → 正解あり、予測・分類
- **教師なし** → 正解なし、クラスタリング・次元削減
- **強化学習** → 行動と報酬から学ぶ
- **k-means = 教師なし**
- **ロジスティック回帰 = 分類**
- **YOLO = 物体検出**

DS検定では、**アルゴリズム名 → 学習タイプ・用途**の順で切り分けられるようにしておきましょう。

## 公式情報・参考リンク

- [scikit-learn公式：線形モデルとロジスティック回帰](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)
  - ロジスティック回帰が、名前に反して分類に使われる点を確認できます。

## 対応スキル項目（ver.6 データサイエンス）

- **分類**：解析技術
- **スキルカテゴリ**：モデル化
- **サブカテゴリ**：機械学習
- **必須スキル**：—
- ★ 機械学習の手法を3つ以上知っており、それぞれの概要と解決できる問題（回帰・分類・クラスター分析など）を説明できる
- [ver.6 ★1スキルチェックで確認する](/ds/datascience-skillcheck/)
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
