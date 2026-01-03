---
layout: page
title: Contrastive LossとTriplet Lossの違い【G検定対策】
permalink: /gk/contrastive-vs-triplet-loss/
tags: [gk, neural_network, metrics]
---

## まず結論
- **Contrastive Loss** は「2点（ペア）」の距離を調整し、  
  **Triplet Loss** は「3点（トリプレット）」の相対関係を学習する。
- G検定では **ペアか3点か・何を基準に距離を比べるか** が問われる。

## 直感的な説明
- Contrastive Loss  
  👉「この2つ、似てる？似てない？」  
- Triplet Loss  
  👉「Aに一番近いのは、B？それともC？」

つまり  
**絶対距離**か  
**相対距離**か  
の違い。

## 定義・仕組み
### Contrastive Loss
- 入力：**データのペア**
  - 類似ペア
  - 非類似ペア
- 目的：
  - 類似 → 距離を小さく
  - 非類似 → 距離を大きく

### Triplet Loss
- 入力：**3点セット（トリプレット）**
  - Anchor（基準）
  - Positive（同じクラス）
  - Negative（異なるクラス）
- 目的：
  - Anchor–Positive < Anchor–Negative  
  となるように学習

👉 **距離の大小関係そのものを学習**する。

## いつ使う？（得意・不得意）
**Contrastive Loss が向く**
- 類似・非類似が明確
- ペアデータが作りやすい
- 小〜中規模タスク

**Triplet Loss が向く**
- クラス内のばらつきが大きい
- 類似度の順位が重要
- 顔認識・人物認識など

## G検定ひっかけポイント
- ❌「Triplet Lossはペアで学習する」
- ❌「Contrastive Lossは相対順位を学習する」
- ❌「どちらも分類損失である」

👉 **どちらも距離学習・分類精度は直接扱わない**

### 判断基準
- **2点で距離調整** → Contrastive Loss
- **3点で距離比較** → Triplet Loss
- **順位・相対関係** → Triplet Loss

## まとめ（試験直前用）
- Contrastive：ペア・絶対距離
- Triplet：3点・相対距離
- どちらも埋め込み学習
- 分類損失ではない
- 「Anchor」が出たらTriplet
