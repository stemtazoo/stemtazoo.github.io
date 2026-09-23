---
layout: page
title: DenseNetとは？Dense ConnectionとResNetとの違い【G検定対策】
description: "DenseNet（Densely Connected Convolutional Network）を、各層がそれ以前の層の特徴マップをconcatenateして受け取るCNNとして整理します。特徴再利用と勾配伝播を助ける設計、growth rate、ResNetの加算との違いをG検定向けに確認します。"
permalink: /gk/densenet/
tags: [gk, cnn]
gk_section: ディープラーニングの応用例/画像認識/物体認識タスク
gk_order: 6
last_modified_at: 2026-09-24
---

## まず結論

**DenseNet**は、各層が**それ以前のすべての層の特徴マップを連結（concatenate）して受け取る**CNNです。

G検定では、

- ResNet → **加算**
- DenseNet → **連結**

で切り分けます。

## 直感的な説明

ResNetは、元の情報を近道経路から**足し合わせる**設計です。

DenseNetは、それまでに作られた特徴を**別々のチャネルとして連結し、後段へ渡す**設計です。

> 足す → ResNet  
> つなげて並べる → DenseNet

と覚えると分かりやすくなります。

## 定義・仕組み

Dense block内では、ある層への入力として、それ以前の層の出力をconcatenateします。

これにより、

- 初期層の特徴を後段で再利用しやすい
- 各層までの情報・勾配経路を短くできる
- 比較的小さなgrowth rateでも多様な特徴を蓄積できる

という特徴があります。

### Growth Rate

各層が新しく追加する特徴マップ数を**growth rate**と呼びます。

DenseNetでは既存特徴を再利用するため、各層で大量の新規チャネルを作らなくても表現を増やせます。

## いつ使う？（得意・不得意）

DenseNetは画像分類などで提案されたCNNです。

一方、特徴マップを連結して保持するため、

- メモリ使用量
- 実装上のデータ移動

が課題になる場合があります。

## G検定ひっかけポイント

### DenseNet＝ResNet？

❌ どちらも加算  
⭕ **ResNetは加算、DenseNetはconcatenate**

### 勾配消失

❌ DenseNetなら勾配消失が完全になくなる  
⭕ **短い接続経路によって勾配伝播を助ける**

### Dense＝全結合層？

❌ Fully Connected LayerのDense  
⭕ **層同士が密に接続されるDense Connection**

## まとめ（試験直前用）

- DenseNet＝**Dense Connection**
- 過去の特徴をconcatenate
- ResNet＝加算
- 特徴再利用
- growth rate
- 勾配伝播を助けるが万能ではない

## 参考資料

- [Densely Connected Convolutional Networks｜CVPR 2017](https://arxiv.org/abs/1608.06993)

{% include gk_article_footer.html %}
