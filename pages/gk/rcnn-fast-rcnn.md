---
layout: page
title: R-CNN・Fast R-CNNの違いとは？Faster R-CNNまでの流れ【G検定】
description: "R-CNNとFast R-CNNを、候補領域ごとにCNNを実行するR-CNN、画像全体の特徴マップを共有してRoI PoolingするFast R-CNNとして整理します。候補領域を外部生成する点は共通し、RPNまで統合したFaster R-CNNとの違いを確認します。"
permalink: /gk/rcnn-fast-rcnn/
tags: [gk, image_recognition, object_detection]
gk_section: ディープラーニングの応用例/画像認識/物体検出タスク
gk_order: 6
last_modified_at: 2026-09-26
---

## まず結論

R-CNN系の発展は、**どこまで計算を共有・ネットワーク化したか**で整理すると分かりやすくなります。

- **R-CNN**：候補領域ごとにCNN
- **Fast R-CNN**：画像全体のCNN特徴を共有
- **Faster R-CNN**：候補領域生成もRPNでネットワーク化

## 直感的な説明

### R-CNN

候補領域を1枚ずつ切り出して、それぞれCNNへ入れるイメージです。

同じ画像について何度もCNNを計算するため、処理が重くなります。

### Fast R-CNN

画像全体を一度CNNへ通して特徴マップを作り、候補領域ごとに必要な部分だけを取り出します。

これにより、**特徴抽出の重複計算を減らす**ことができます。

## 定義・仕組み

### R-CNN

- Selective Searchなどで候補領域を生成
- 各候補領域をCNNへ入力
- 特徴抽出後に分類・位置補正

### Fast R-CNN

- 画像全体から特徴マップを作る
- 外部手法で得た候補領域を特徴マップへ対応付ける
- RoI Poolingで固定サイズの特徴へ変換
- 分類・位置補正

重要なのは、Fast R-CNNでも**候補領域生成自体は外部手法**に依存することです。

### Faster R-CNNへ

[Faster R-CNN](/gk/faster-r-cnn/)では、候補領域生成をRPNでネットワーク内部へ取り込みます。

## いつ使う？（得意・不得意）

R-CNN、Fast R-CNNは現在の実用モデルを選ぶためというより、**物体検出の発展史と処理構造を理解する教材**として重要です。

G検定では、モデル名と改善点の対応を見ます。

## G検定ひっかけポイント

### R-CNN

❌ 画像全体のCNN特徴を1回だけ共有  
⭕ **候補領域ごとにCNN**

### Fast R-CNN

❌ RPNで候補領域を作る  
⭕ **特徴マップは共有するが候補領域は外部生成**

### Faster R-CNN

⭕ **RPNで候補領域生成まで統合**

## まとめ（試験直前用）

- R-CNN＝候補領域ごとにCNN
- Fast R-CNN＝**特徴マップを共有**
- Fast R-CNNでも候補領域は外部
- Faster R-CNN＝**RPN**
- 発展の軸は「何を共有・統合したか」

## 参考資料（原論文）

- [Rich Feature Hierarchies for Accurate Object Detection and Semantic Segmentation｜CVF](https://openaccess.thecvf.com/content_cvpr_2014/html/Girshick_Rich_Feature_Hierarchies_2014_CVPR_paper.html)
  - Girshickら（CVPR 2014）によるR-CNNの原論文です。Region ProposalごとにCNN特徴を計算する方式を提案しています。
- [Fast R-CNN｜CVF](https://openaccess.thecvf.com/content_iccv_2015/html/Girshick_Fast_R-CNN_ICCV_2015_paper.html)
  - Girshick（ICCV 2015）によるFast R-CNNの原論文です。画像全体のCNN特徴を共有し、RoI単位で分類・回帰する方式へ改善しています。
- [Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks｜arXiv](https://arxiv.org/abs/1506.01497)
  - RenらによるFaster R-CNNの原論文です。Region Proposal Network（RPN）によって候補領域生成もネットワーク化しています。

{% include gk_article_footer.html %}
