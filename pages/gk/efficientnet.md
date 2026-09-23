---
layout: page
title: EfficientNetとは？Compound Scalingで深さ・幅・解像度を調整【G検定】
description: "EfficientNetを、CNNの深さ・幅・入力解像度を一定の規則でまとめて拡張するCompound Scalingを提案した画像認識モデルとして整理します。B0を基準にB1以降へスケールする考え方を押さえ、ResNetやWideResNetとの違いを固定的な一軸比較にしない判断基準を確認します。"
permalink: /gk/efficientnet/
tags: [gk, neural_network, cnn]
gk_section: ディープラーニングの応用例/画像認識/物体認識タスク
gk_order: 10
last_modified_at: 2026-09-23
---

## まず結論

**EfficientNet**は、CNNを大きくするときに、

- 深さ（depth）
- 幅（width）
- 入力解像度（resolution）

を**まとめてバランスよく拡張するCompound Scaling**を提案したモデルです。

G検定では、**3要素を同時に調整する**ことが最大の判断軸です。

## 直感的な説明

CNNを高性能化する方法には、

- 層を増やす
- チャネル数を増やす
- 入力画像を大きくする

などがあります。

EfficientNetでは、どれか1つだけを増やすのではなく、

> **3つを一定の比率で一緒にスケールする**

考え方を使います。

## 定義・仕組み

EfficientNetでは、ベースとなるEfficientNet-B0を作り、Compound Scalingを使ってB1、B2…へ拡張します。

### Compound Scaling

計算資源を増やすときに、

- depth
- width
- resolution

をあらかじめ決めた係数に従って同時に増やします。

重要なのは、

> **EfficientNet＝単に深いCNN**

ではないことです。

原論文ではB0の設計にNeural Architecture Searchも利用されています。

## いつ使う？（得意・不得意）

EfficientNetは画像分類を中心に提案され、効率のよい画像特徴抽出器として他タスクにも利用できます。

ただし、

> ResNet＝深さだけ
>
> WideResNet＝幅だけ
>
> EfficientNet＝3つ

という比較は、試験用の直感としては使えても、各モデルの設計全体を完全に表すものではありません。

G検定では**Compound ScalingというEfficientNet固有の考え方**を見つけることを優先します。

## G検定ひっかけポイント

### EfficientNetの特徴

❌ 入力解像度だけを上げる  
❌ ネットワークの深さだけを増やす  
⭕ **深さ・幅・解像度をまとめてスケール**

### 時系列モデル？

❌ RNNやTransformer系の系列モデル  
⭕ **画像認識向けCNNとして提案されたモデル**

### B0〜B7

❌ 別々の無関係なモデル  
⭕ **B0を基準にスケーリングしたモデル群**

## まとめ（試験直前用）

- EfficientNet＝**Compound Scaling**
- depth・width・resolution
- 3つをバランスよく拡張
- B0を基準にモデル群を構成
- CNN系画像モデル
- **「何を同時にスケールするか」で切る**

## 参考資料

- [EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks｜arXiv](https://arxiv.org/abs/1905.11946)

{% include gk_article_footer.html %}
