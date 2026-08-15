---
layout: page
title: CNN（畳み込みニューラルネットワーク）とは？画像認識AIの基本【DS検定】
description: "CNNを、畳み込み層で画像の特徴を抽出し、プーリングなどで情報を整理しながら分類などを行うニューラルネットワークとして整理します。カーネル・畳み込み・CNNの役割の違いと、DS検定での判断基準を確認します。"
permalink: /ds/cnn/
categories: [data-science]
tags: [ds, modeling]
prev: /ds/cluster-analysis/
next: /ds/convolution/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**CNN（Convolutional Neural Network）は、畳み込みを使って画像から特徴を抽出するニューラルネットワーク**です。

DS検定では、次の関係を押さえると判断しやすくなります。

| 用語 | 役割 |
|---|---|
| カーネル | 特徴を検出するための小さな行列 |
| 畳み込み | カーネルを使って特徴を計算する処理 |
| CNN | 畳み込みを組み込んだ学習モデル |

## 直感的な説明

人は画像を見るとき、いきなり「猫」と判断するのではなく、

- 輪郭
- 模様
- 耳や目の形

などの特徴を手掛かりにしています。

CNNも同じように、画像の局所的な特徴を段階的に取り出し、最終的な分類や認識につなげます。

## 定義・仕組み

CNNは、主に次の処理を組み合わせます。

### ① 畳み込み層

カーネルを使い、画像からエッジ・模様・形などの特徴を抽出します。

### ② プーリング層

特徴マップを縮小し、重要な情報を残しながら計算量を減らします。

### ③ 全結合層など

抽出した特徴を使って、分類などの最終判断を行います。

### CNNの特徴

| 特徴 | 意味 |
|---|---|
| 局所的な特徴を見る | 近くの画素の関係を利用する |
| 重みを共有する | 同じカーネルを画像の各位置で使う |
| カーネルを学習する | 人が固定するのではなく、学習で調整される |

## どんな場面で使う？

### 画像分類

猫・犬・車など、画像全体のカテゴリを判定します。

### 物体検出・画像認識

画像内の物体や特徴を検出するモデルの基礎として使われます。

### 医療画像・外観検査

病変や製品欠陥など、画像内の特徴を捉える用途で使われます。

CNNは画像以外にも応用されますが、DS検定ではまず**画像認識に強いモデル**として押さえるのが基本です。

## よくある誤解・混同

### ❌ CNN = 畳み込みそのもの

畳み込みは処理、CNNはその処理を利用するモデルです。

### ❌ CNNは画像をそのまま全結合層へ入れるモデル

CNNでは、畳み込みによって局所的な特徴を抽出してから後段の処理につなげます。

### ❌ カーネルは人が必ず固定する

通常の画像フィルタでは固定カーネルを使うことがありますが、CNNでは**カーネルの重みを学習**します。

### ❌ CNNは画像にしか使えない

画像が代表的ですが、1次元信号や時系列などへ応用されることもあります。

## まとめ（試験直前用）

- **CNN = 畳み込みを使うニューラルネットワーク**
- 畳み込み層で特徴を抽出する
- プーリングで情報をまとめることがある
- CNNではカーネルの重みを学習する
- **カーネル = ルール / 畳み込み = 計算 / CNN = モデル**

DS検定では、**「画像の局所的な特徴を畳み込みで抽出する」**と書かれていたらCNNを疑いましょう。

## 対応スキル項目（AI利活用スキルシート）

- スキルカテゴリ名：AIの技術理解
- サブカテゴリ名：機械学習
- ★ 代表的な機械学習手法の概要を理解している

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
