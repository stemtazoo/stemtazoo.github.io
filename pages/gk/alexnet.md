---
layout: page
title: AlexNetとは？2012年ImageNetと深層CNNの転機【G検定対策】
description: "AlexNetを、2012年ILSVRCで高い画像分類性能を示し、深層CNNの有効性を広く認識させた歴史的モデルとして整理します。ReLU、GPU学習、Dropout、データ拡張を押さえ、VGG・ResNetなど後続CNNとの違いをG検定向けに確認します。"
permalink: /gk/alexnet/
tags: [gk, cnn]
gk_section: ディープラーニングの応用例/画像認識/物体認識タスク
gk_order: 1
last_modified_at: 2026-09-23
---

## まず結論

**AlexNet**は、2012年のILSVRCで高い画像分類性能を示し、**深層CNNが大規模画像認識で有効であることを強く印象付けた歴史的モデル**です。

G検定では、

- 2012年 ILSVRC
- CNN
- ReLU
- GPU学習
- Dropout
- データ拡張

を関連付けて覚えます。

## 直感的な説明

AlexNet以前にもCNNは存在していました。

AlexNetの重要性は、

> **CNNを初めて発明したことではなく、大規模データ・GPU・深いCNNを組み合わせて画像認識で大きな成果を示したこと**

です。

この成功が、その後の深層学習ブームを加速させました。

## 定義・仕組み

AlexNetは、畳み込み層と全結合層を組み合わせたCNNです。

代表的な工夫として、

- **ReLU**
- **GPUを使った学習**
- **Dropout**
- **データ拡張**

などがあります。

当時の大規模画像分類で、深いニューラルネットワークを実用的に学習するうえで重要な組合せでした。

## いつ使う？（得意・不得意）

現在ではAlexNetそのものより、**CNN発展史を理解するための基準点**として重要です。

学習順としては、

AlexNet → VGG / GoogLeNet → ResNet

と追うと、CNNが深層化・効率化されていく流れを理解しやすくなります。

## G検定ひっかけポイント

### AlexNet＝最初のCNN？

❌ CNNを初めて発明したモデル  
⭕ **CNNの歴史はより古く、AlexNetは2012年に深層CNNの有効性を強く示した代表例**

### AlexNet＝残差接続？

❌ skip connection  
⭕ それは**ResNet**

### AlexNet＝Attention？

❌ Self-Attention中心  
⭕ それは**Transformer系**

## まとめ（試験直前用）

- AlexNet＝**2012年ILSVRC**
- 深層CNNの成功を広く示した
- ReLU
- GPU学習
- Dropout
- データ拡張
- **「最初のCNN」とは覚えない**

{% include gk_article_footer.html %}
