---
layout: page
title: SSDとは？Default Boxを使う1段階物体検出【G検定対策】
description: "SSD（Single Shot MultiBox Detector）を、複数解像度の特徴マップ上にDefault Boxを用意し、クラスと位置補正を1つのネットワークで直接予測する1段階物体検出として整理します。Faster R-CNNの2段階方式、YOLOとの共通点を構造で比較します。"
permalink: /gk/ssd/
tags: [gk, image_recognition, object_detection]
gk_section: ディープラーニングの応用例/画像認識/物体検出タスク
gk_order: 3
last_modified_at: 2026-09-23
---

## まず結論

**SSD（Single Shot MultiBox Detector）**は、候補領域生成を別段階で行わず、**1つのネットワークでクラスとバウンディングボックスを直接予測する1段階物体検出モデル**です。

G検定では、

- Single Shot
- Default Box
- 複数スケールの特徴マップ

を押さえます。

## 直感的な説明

Faster R-CNNが、

> 候補を探す → 候補を詳しく分類する

の2段階なのに対し、SSDは、

> **複数の場所・大きさについて、一度の検出パイプラインでまとめて予測する**

方式です。

## 定義・仕組み

SSDでは、複数の特徴マップ上にさまざまな形・大きさの**Default Box**を用意します。

各Default Boxについて、

- クラスのスコア
- ボックス位置の補正量

を予測します。

また、解像度の異なる複数特徴マップから予測することで、異なる大きさの物体を扱います。

## いつ使う？（得意・不得意）

SSDは、候補領域生成を別処理にしないため、リアルタイム性を重視した検出システムに適した設計です。

一方、特に初期SSDでは小物体検出が課題として知られました。

ただし、

> SSDは必ずFaster R-CNNより低精度

とは限りません。原論文でも条件によってFaster R-CNNと競合する精度が報告されています。

## G検定ひっかけポイント

### SSD＝2段階？

❌ Region Proposalを作ってから分類  
⭕ **1段階で直接予測**

### Single Shotの意味

❌ 画像中に1個の物体しか検出できない  
⭕ **候補領域生成を別段階にせず1つのネットワークで検出する**

### YOLOとの関係

SSDもYOLOも代表的な**1段階物体検出**です。

細かな世代差より、まず1段階 / 2段階で切り分けます。

## まとめ（試験直前用）

- SSD＝**1段階物体検出**
- Default Box
- 複数解像度の特徴マップ
- クラスと位置を直接予測
- Faster R-CNN＝2段階
- YOLOも1段階
- **速度・精度を絶対順位で覚えない**

## 参考資料

- [SSD: Single Shot MultiBox Detector｜arXiv](https://arxiv.org/abs/1512.02325)

{% include gk_article_footer.html %}
