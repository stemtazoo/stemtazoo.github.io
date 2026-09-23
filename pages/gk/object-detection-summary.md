---
layout: page
title: 物体検出モデル総まとめ｜YOLO・SSD・R-CNN系の違い【G検定】
description: "物体検出モデルを、候補領域を別段階で作らず直接検出するYOLO・SSDなどの1段階型と、候補領域を作ってから分類・位置補正するR-CNN系の2段階型に整理します。Default Box、RPN、特徴共有の役割を比較し、速度・精度の固定順位ではなく構造で見分けます。"
permalink: /gk/object-detection-summary/
tags: [gk, image_recognition, object_detection, cheatsheet]
gk_section: ディープラーニングの応用例/画像認識/物体検出タスク
gk_order: 2
last_modified_at: 2026-09-23
---

## まず結論

物体検出モデルは、まず**検出パイプラインが1段階か2段階か**で整理します。

- **1段階**：YOLO、SSD
- **2段階**：R-CNN、Fast R-CNN、Faster R-CNN

G検定では、速度や精度を絶対順位で覚えるより、

> **候補領域を別段階で作るか？**

を見るのが安全です。

## 直感的な説明

### 1段階

画像から直接、

- クラス
- バウンディングボックス

を予測します。

代表例はYOLO・SSDです。

### 2段階

1. 物体がありそうな候補領域を作る
2. 候補領域を分類・位置補正する

という2段階で処理します。

代表例はR-CNN系です。

## 定義・仕組み

| モデル | 段階 | 判断キーワード |
|---|---:|---|
| SSD | 1段階 | Single Shot、Default Box |
| YOLO | 1段階 | 直接検出、リアルタイム性 |
| R-CNN | 2段階 | 候補領域ごとにCNN |
| Fast R-CNN | 2段階 | 特徴マップ共有、RoI Pooling |
| Faster R-CNN | 2段階 | RPN |

### R-CNN → Fast → Faster

発展の流れは、

- R-CNN → 候補領域ごとにCNN
- Fast R-CNN → CNN特徴を共有
- Faster R-CNN → RPNで候補領域生成までネットワーク化

と整理します。

### SSD / YOLO

どちらも代表的な1段階検出です。

ただし、YOLOには多くの世代があるため、特定世代のグリッド・アンカー設計を全YOLO共通と決めつけないようにします。

## いつ使う？（得意・不得意）

一般に1段階検出はリアルタイム性を重視する設計で多く使われ、2段階検出は候補領域を詳しく処理する設計です。

ただし、

- 1段階＝必ず低精度
- 2段階＝必ず高精度
- YOLO＝必ず最速

とは限りません。

モデル世代、バックボーン、入力サイズ、ハードウェアによって結果は変わります。

## G検定ひっかけポイント

### Faster R-CNN

❌ Fasterという名前なのでYOLOより必ず速い  
⭕ **RPNを導入してR-CNN系を高速化したモデル**

### Fast R-CNN

❌ RPNで候補領域を作る  
⭕ **候補領域は外部、特徴抽出を共有**

### SSD

❌ Region Proposalを別段階で作る  
⭕ **Default Boxを使う1段階検出**

### YOLO

❌ 2段階で候補領域を分類する  
⭕ **1段階検出系**

## まとめ（試験直前用）

- YOLO / SSD＝**1段階**
- R-CNN系＝**2段階**
- R-CNN＝候補ごとにCNN
- Fast R-CNN＝特徴共有
- Faster R-CNN＝RPN
- SSD＝Default Box
- **速度・精度の固定順位ではなく処理構造で切る**

{% include gk_article_footer.html %}
