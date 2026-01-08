---
layout: page
title: SENet（Squeeze-and-Excitation Network）とは？G検定対策
permalink: /gk/senet/
tags: [gk, cnn]
---

## まず結論

* **SENet（Squeeze-and-Excitation Network）**とは、**チャネル方向のAttention機構**を導入し、重要な特徴チャネルを強調することで認識性能を向上させたCNNアーキテクチャ。
* G検定では**「チャネル方向のAttention」**を見抜けるかが最重要ポイント。

## 直感的な説明

* 画像の特徴量には、

  * 重要な特徴
  * あまり重要でない特徴
    が混ざっています。
* SENetは、
  👉 **「どのチャネルが重要か？」を自動で学習し、重要なものだけを強く見る**仕組みです。
* 人で言えば、
  👉 **注目すべきポイントにだけ意識を集中する**イメージです。

## 定義・仕組み

* SENetは、各チャネルの重要度を学習するために、

  1. **Squeeze**：空間方向に平均化し、チャネルごとの代表値を取得
  2. **Excitation**：全結合層を用いてチャネル重み（Attention）を計算
  3. **Recalibration**：重みを各チャネルに掛けて特徴を再調整
     という処理を行います。

* 特徴：

  * チャネル方向のAttention
  * 既存CNN（ResNetなど）に組み込み可能
  * ImageNetで大きな性能向上

## いつ使う？（得意・不得意）

### 使われる場面（得意）

* 画像分類
* 既存CNNの性能向上

### 注意点・不得意

* 計算量がわずかに増加
* 空間方向のAttentionではない

## G検定ひっかけポイント

* よくある誤り表現：

  * ❌ 「空間方向のAttention」
  * ❌ 「セグメンテーション専用モデル」

* 正しい理解：

  * **チャネル方向のAttention**
  * CNNに付加するモジュール

* 判断基準：

  * **チャネルに注目 → SENet**
  * **空間ピラミッド → PSPNet**

## まとめ（試験直前用）

* SENet＝チャネルAttention
* 重要チャネルを強調
* Squeeze & Excitation が名前の由来
* ResNetなどに組み込める
* 空間Attentionではない
