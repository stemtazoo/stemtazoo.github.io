---
layout: page
title: 機械学習アルゴリズム一覧チートシート（教師あり・教師なし・強化学習）【DS検定】
permalink: /ds/machine-learning-algorithms-cheatsheet/
categories: [data-science]
tags: [ds, cheatsheet]
prev: /ds/logistic-regression/
next: /ds/machine-learning-methods/
---

## まず結論

機械学習アルゴリズムは「教師あり学習・教師なし学習・強化学習」の3つに分類されます。

DS検定では

アルゴリズム名

学習タイプ

主な用途


を結び付けて判断する問題がよく出ます。

つまり

「このアルゴリズムはどの学習タイプか？」

を判断できることが重要です。



## 直感的な説明

機械学習のアルゴリズムは、役割で整理すると理解しやすくなります。

目的	代表アルゴリズム

数値予測	線形回帰
分類	ロジスティック回帰・SVM
グループ分け	k-means
画像認識	CNN
文章生成	GPT


DS検定では

用途 → アルゴリズム

の対応を問う問題がよく出ます。



## 定義・仕組み

教師あり学習（Supervised Learning）

正解付きデータを使って学習する方法です。

回帰（数値予測）

アルゴリズム	特徴

線形回帰	最も基本的な回帰モデル
リッジ回帰	過学習を抑える
Lasso回帰	特徴量選択が可能




分類

アルゴリズム	特徴

ロジスティック回帰	分類モデル
k近傍法（kNN）	近いデータで判断
SVM	境界を最大化
決定木	ルールベース分類
ランダムフォレスト	決定木の集合
勾配ブースティング	弱学習器を組み合わせる


実務では

XGBoost

LightGBM


などもよく使われます。



教師なし学習（Unsupervised Learning）

正解がないデータからパターンを見つけます。

クラスタリング

アルゴリズム	特徴

k-means	最も有名なクラスタリング
階層クラスタリング	階層構造を作る
DBSCAN	密度ベースクラスタリング




次元削減

アルゴリズム	特徴

PCA	主成分分析
t-SNE	可視化向け
UMAP	高次元可視化




強化学習（Reinforcement Learning）

試行錯誤しながら最適行動を学習します。

アルゴリズム	特徴

Q学習	基本的強化学習
Deep Q Network	深層学習との組み合わせ
方策勾配法	行動方針を直接学習




ディープラーニング手法

モデル	用途

CNN	画像認識
RNN	時系列データ
LSTM	長期時系列
GAN	データ生成
VAE	生成モデル
YOLO	物体検出




LLM関連モデル

モデル	用途

Transformer	LLMの基盤モデル
GPT	文章生成
BERT	文章理解




## どんな場面で使う？

用途	アルゴリズム

売上予測	線形回帰
顧客セグメント	k-means
不正検知	ランダムフォレスト
画像認識	CNN
物体検出	YOLO
文章生成	GPT




## よくある誤解・混同

ロジスティック回帰

名前に回帰が付いていますが

分類アルゴリズムです。

DS検定では非常に狙われます。



k-means

教師なし学習です。

教師あり学習と混同する問題がよく出ます。



YOLO

画像分類ではなく

物体検出アルゴリズムです。



GAN

分類モデルではなく

データ生成モデルです。



## まとめ（試験直前用）

機械学習は 教師あり・教師なし・強化学習

DS検定では アルゴリズム名 → 学習タイプ が頻出

ロジスティック回帰は 分類

k-meansは 教師なし学習

GAN・YOLO・Transformerは ディープラーニング系




対応スキル項目

【対応スキル項目（AI利活用スキルシート）】

スキルカテゴリ名 AI・人工知能

サブカテゴリ名 機械学習

★ 機械学習にあたる解析手法の名称を3つ以上知っており、手法の概要を説明できる

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

---

[DS?? ???????????]({{ '/ds/' | relative_url }})
