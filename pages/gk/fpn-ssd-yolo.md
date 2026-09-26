---
layout: page
title: FPN・SSD・YOLOの違いとは？物体検出の役割で整理【G検定】
description: "FPN・SSD・YOLOを、マルチスケール特徴を作るFPNと、1段階物体検出を行うSSD・YOLOに分けて整理します。FPNは検出器そのものではなく他の検出モデルへ組み込める構造である点を押さえ、速度・精度の固定順位ではなく役割で切り分けます。"
permalink: /gk/fpn-ssd-yolo/
tags: [gk, cnn, object_detection, cheatsheet]
gk_section: ディープラーニングの応用例/画像認識/物体検出タスク
gk_order: 8
last_modified_at: 2026-09-26
---

## まず結論

FPN・SSD・YOLOは、同じ種類のものではありません。

- **FPN**：異なる解像度の特徴を統合する**特徴ピラミッド構造**
- **SSD**：Default Boxと複数特徴マップを使う**1段階検出**
- **YOLO**：画像から位置・クラスを直接予測する**1段階検出系**

G検定では、

> **特徴を作る構造か、検出器か**

を最初に分けます。

## 直感的な説明

### FPN

小さい物体と大きい物体を扱うため、**粗い特徴と細かい特徴を組み合わせる**仕組みです。

### SSD

異なる解像度の特徴マップ上で、複数のDefault Boxを使って直接検出します。

### YOLO

画像全体から、物体の位置とクラスを1つの検出パイプラインで直接予測します。

## 定義・仕組み

### FPN

Feature Pyramid Networkは、

- top-down path
- lateral connection

を使って、複数スケールで意味的に強い特徴マップを作ります。

FPNは**単体で完成した物体検出器というより、検出器へ組み込める特徴抽出構造**です。

### SSD

[SSD](/gk/ssd/)は、

- 1段階検出
- Default Box
- 複数解像度の特徴マップ

が判断キーワードです。

### YOLO

[YOLO](/gk/yolo/)も代表的な1段階検出系です。

YOLOには多数の世代があるため、特定世代のアンカーやグリッド設計を全YOLO共通の絶対条件として覚えないようにします。

## いつ使う？（得意・不得意）

- FPN → マルチスケール特徴が必要な検出器へ組み込む
- SSD → 1段階で複数スケールを直接検出
- YOLO → リアルタイム性を重視する1段階検出系

FPNはFaster R-CNNなどの2段階検出器とも組み合わせられます。

したがって、

> FPN＝1段階

ではありません。

## G検定ひっかけポイント

### FPN＝物体検出アルゴリズム？

❌ 単体でクラスとバウンディングボックスを出す検出器  
⭕ **複数スケール特徴を作る構造**

### SSD / YOLO

⭕ 代表的な**1段階物体検出**

### FPNはSSD・YOLOと排他的？

❌ どれか1つしか使えない  
⭕ **FPNのようなマルチスケール構造を検出器へ組み込むこともできる**

## まとめ（試験直前用）

- FPN＝**特徴ピラミッド構造**
- SSD＝**1段階＋Default Box**
- YOLO＝**1段階物体検出系**
- FPNは検出器そのものとは限らない
- 速度・精度の固定順位で判断しない
- **構造か検出器か**を先に見る

## 参考資料（原論文）

- [Feature Pyramid Networks for Object Detection｜CVF](https://openaccess.thecvf.com/content_cvpr_2017/html/Lin_Feature_Pyramid_Networks_CVPR_2017_paper.html)
  - Linら（CVPR 2017）によるFPNの原論文です。Top-down経路とlateral connectionでマルチスケール特徴を構成します。
- [SSD: Single Shot MultiBox Detector｜arXiv](https://arxiv.org/abs/1512.02325)
  - LiuらによるSSDの原論文です。複数解像度の特徴マップ上でDefault Boxを使い、1段階で物体検出します。
- [You Only Look Once: Unified, Real-Time Object Detection｜CVF](https://openaccess.thecvf.com/content_cvpr_2016/html/Redmon_You_Only_Look_CVPR_2016_paper.html)
  - Redmonら（CVPR 2016）によるYOLOの原論文です。物体検出を単一ネットワークによる回帰問題として扱います。

{% include gk_article_footer.html %}
