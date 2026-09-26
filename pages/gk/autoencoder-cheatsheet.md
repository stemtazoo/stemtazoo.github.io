---
layout: page
title: オートエンコーダまとめ（AE / CAE / DAE / VAE）とは？G検定対策
description: "* オートエンコーダ（AE）系は、入力データをいったん圧縮し、元に復元することで本質的な特徴を学習するモデル群です。 AI・機械学習での位置づけ、関連モデルや手法との違い、G検定で混同しやすい判断軸を確認できます。"
permalink: /gk/autoencoder-cheatsheet/
tags: [gk, neural_network, cheatsheet]
gk_section: ディープラーニングの要素技術/オートエンコーダ/基本・派生モデル
gk_order: 1
last_modified_at: 2026-09-26
---

## まず結論

* **オートエンコーダ（AE）系**は、入力データをいったん圧縮し、元に復元することで**本質的な特徴を学習するモデル群**です。
* G検定では「**可視化（CAM）と混同していないか**」「**それぞれの役割の違い**」が問われます。

## 直感的な説明

* オートエンコーダは「**一度メモ用紙に要点だけ書き写して、元の文章を復元する練習**」のようなものです。
* どの情報が重要かを学ぶことで、

  * ノイズに強くなる
  * 次元を減らせる
  * 異常を見つけられる
    ようになります。

## 定義・仕組み

* **AE（Autoencoder）**

  * 基本形のオートエンコーダ
  * Encoder / Decoder で構成

* **CAE（Convolutional Autoencoder）**

  * 畳み込み層を用いる
  * 画像の空間構造を保った特徴学習

* **DAE（Denoising Autoencoder）**

  * 入力にノイズを加えて学習
  * ノイズ除去・ロバストな特徴抽出

* **VAE（Variational Autoencoder）**

  * 潜在変数を確率分布として扱う
  * データ生成が可能

## いつ使う？（得意・不得意）

### 共通して得意

* 次元削減
* 特徴学習
* 異常検知の基礎

### 注意点

* 分類結果の理由説明（XAI）には使えない
* 可視化手法ではない

## G検定ひっかけポイント

* **最大のひっかけ**

  * 「AE系は判断根拠を可視化する」→ ❌
* よくある混同

  * CAM（説明・可視化）
  * CAE / DAE / VAE（学習モデル）
* 選択肢で

  * 「ノイズ除去」→ DAE
  * 「画像特徴学習」→ CAE
  * 「生成モデル」→ VAE

## まとめ（試験直前用）

* AE系は特徴を学習するモデル
* CAE：畳み込み
* DAE：ノイズ除去
* VAE：確率的生成
* CAMとは役割が別

## 参考資料（原論文）

- [Reducing the Dimensionality of Data with Neural Networks｜Science](https://doi.org/10.1126/science.1127647)
  - Hinton・Salakhutdinov（2006）。入力を再構成しながら低次元コードを学習する深いAutoencoderの代表的な一次資料です。
- [Extracting and Composing Robust Features with Denoising Autoencoders｜ACM](https://doi.org/10.1145/1390156.1390294)
  - Vincentら（ICML 2008）。入力を意図的に破損させ、元の入力を復元するDenoising Autoencoderを提案しています。
- [Stacked Convolutional Auto-Encoders for Hierarchical Feature Extraction｜Springer](https://link.springer.com/chapter/10.1007/978-3-642-21735-7_7)
  - Masciら（2011）。畳み込みを用いるConvolutional Autoencoderを扱った代表的な一次資料です。
- [Auto-Encoding Variational Bayes｜arXiv](https://arxiv.org/abs/1312.6114)
  - Kingma・WellingによるVAEの原論文です。確率的潜在変数と再パラメータ化を使う点が通常のAEとの重要な違いです。

{% include gk_article_footer.html %}
