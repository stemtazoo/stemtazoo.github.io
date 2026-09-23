---
layout: page
title: FPNとは？マルチスケール特徴を作るFeature Pyramid Network【G検定】
description: "FPN（Feature Pyramid Network）を、CNNの高解像度特徴と深い層の意味情報をトップダウン経路と横方向接続で統合し、複数スケールの特徴マップを作る構造として整理します。検出器そのものではなく、Faster R-CNNなどへ組み込める点を確認します。"
permalink: /gk/fpn/
tags: [gk, cnn, object_detection]
gk_section: ディープラーニングの応用例/画像認識/物体検出タスク
gk_order: 7
last_modified_at: 2026-09-23
---

## まず結論

**FPN（Feature Pyramid Network）**は、異なる解像度の特徴マップを組み合わせ、**複数スケールで意味的に強い特徴を作る構造**です。

G検定では、

- top-down path
- lateral connection
- feature pyramid
- 大きさの異なる物体

を押さえます。

FPNは、YOLOやSSDのような「検出器そのもの」と同じ分類ではありません。

## 直感的な説明

CNNでは、

- 浅い層 → 解像度が高く細かな位置情報が多い
- 深い層 → 解像度は低いが意味情報が強い

という特徴があります。

FPNは、深い層の意味情報を上へ戻しながら浅い層の高解像度情報と組み合わせます。

> **細かく見える情報と、意味が分かる情報を合流させる**

イメージです。

## 定義・仕組み

FPNは主に、

- **bottom-up path**：通常のCNNで特徴を抽出
- **top-down path**：深い層の特徴を高解像度側へ伝える
- **lateral connection**：同じスケール付近の特徴を結合

から構成されます。

これにより、複数の解像度で意味的に強い特徴マップを作ります。

## いつ使う？（得意・不得意）

FPNは、大きさの異なる物体を扱う物体検出やセグメンテーションなどで利用されます。

原論文ではFaster R-CNNと組み合わせて評価されています。

重要なのは、

> **FPN単体が1段階検出器・2段階検出器というわけではない**

ことです。

さまざまな検出器の特徴抽出部へ組み込めます。

## G検定ひっかけポイント

### FPN＝物体検出モデル？

❌ FPNだけでクラスとバウンディングボックスを最終出力する  
⭕ **マルチスケール特徴を作る構造**

### FPN＝Attention？

❌ Query / Key / Valueで重み付けする  
⭕ **トップダウン経路と横方向接続で特徴を統合する**

### FPN＝SSD？

❌ 同じもの  
⭕ **SSDは1段階検出器、FPNは特徴ピラミッド構造**

## まとめ（試験直前用）

- FPN＝**Feature Pyramid Network**
- bottom-up + top-down
- lateral connection
- マルチスケール特徴
- 大小の物体を扱いやすくする
- 検出器そのものとは限らない
- **Faster R-CNNなどと組み合わせられる**

## 参考資料

- [Feature Pyramid Networks for Object Detection｜arXiv](https://arxiv.org/abs/1612.03144)
- [FPN・SSD・YOLOの違い](/gk/fpn-ssd-yolo/)

{% include gk_article_footer.html %}
