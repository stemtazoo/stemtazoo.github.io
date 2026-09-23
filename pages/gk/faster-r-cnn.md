---
layout: page
title: Faster R-CNNとは？RPNを使う2段階物体検出【G検定対策】
description: "Faster R-CNNを、Region Proposal Network（RPN）で候補領域を生成し、その候補を分類・位置補正する2段階物体検出として整理します。Fast R-CNNとの違い、YOLO・SSDの1段階検出との違いを、速度や精度の固定順位ではなく処理構造で確認します。"
permalink: /gk/faster-r-cnn/
tags: [gk, image_recognition, object_detection]
gk_section: ディープラーニングの応用例/画像認識/物体検出タスク
gk_order: 4
last_modified_at: 2026-09-23
---

## まず結論

**Faster R-CNN**は、

1. RPNで候補領域を作る
2. 候補領域ごとに分類・位置補正する

という**2段階（two-stage）物体検出モデル**です。

G検定では、**RPN＝Faster R-CNN**を最優先で押さえます。

## 直感的な説明

Faster R-CNNは、

> まず怪しい場所を探し、その場所を詳しく調べる

方式です。

一方、YOLOやSSDは、候補領域を別段階で作らずに直接検出する代表的な1段階方式です。

## 定義・仕組み

### 第1段階：RPN

Region Proposal Networkが、共有された特徴マップから、

- 物体がありそうか
- 候補領域はどこか

を予測します。

### 第2段階：検出

候補領域の特徴を使い、

- クラス分類
- バウンディングボックス補正

を行います。

Fast R-CNNでは候補領域生成が外部手法でしたが、Faster R-CNNでは**RPNをネットワーク内へ組み込んだ**ことが重要です。

## いつ使う？（得意・不得意）

Faster R-CNNは2段階検出の代表モデルとして、精密な領域処理が必要な物体検出で広く使われてきました。

ただし、

> 2段階なら常に高精度
>
> 1段階なら常に高速

と固定順位で覚えるのは避けます。

モデルの世代、バックボーン、入力サイズ、ハードウェアで速度・精度は変化します。

## G検定ひっかけポイント

### Fasterの意味

❌ YOLOより必ず高速という意味  
⭕ **従来のR-CNN / Fast R-CNNから候補領域生成までネットワーク化して高速化した流れ**

### RPN

❌ SSDやYOLOの代表機構  
⭕ **Faster R-CNNの候補領域生成**

### 1段階 / 2段階

- Faster R-CNN → **2段階**
- SSD / YOLO → **1段階**

## まとめ（試験直前用）

- Faster R-CNN＝**2段階検出**
- RPNでRegion Proposal
- 候補領域を分類・位置補正
- Fast R-CNNより候補領域生成を統合
- SSD / YOLOは代表的1段階
- **速度・精度の固定順位より構造で切る**

## 参考資料

- [Faster R-CNN｜arXiv](https://arxiv.org/abs/1506.01497)

{% include gk_article_footer.html %}
