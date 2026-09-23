---
layout: page
title: 分類の評価指標まとめ｜Accuracy・Precision・Recall・F1・ROC-AUC【G検定】
description: "分類の主要評価指標を、Accuracyは全体正解率、Precisionは誤検知、Recallは見逃し、F1は両者の調和平均、ROC-AUCはTPRとFPR、PR曲線はPrecisionとRecallという判断軸で整理します。目的とクラス不均衡から指標を選ぶ基準を確認します。"
permalink: /gk/classification-metrics-cheatsheet/
tags: [gk, cheatsheet]
gk_section: 機械学習の概要/モデルの選択・評価/分類の評価指標
gk_order: 8
last_modified_at: 2026-09-23
---

## まず結論

分類指標は、**何を失敗として重く見るか**で選びます。

| 指標 | 何を見る？ | 判断キーワード |
|---|---|---|
| Accuracy | 全体の正解割合 | 全体 |
| Precision | 陽性予測の信頼性 | FP・誤検知 |
| Recall | 実際の陽性を拾えた割合 | FN・見逃し |
| F1-score | PrecisionとRecallのバランス | 調和平均 |
| ROC-AUC | TPRとFPRをしきい値全体で評価 | 識別・順位付け |
| PR曲線 | PrecisionとRecallの関係 | 少数陽性・陽性性能 |

G検定では、式を暗記するだけでなく、**どの誤りを減らしたいか**を見るのが重要です。

## 直感的な説明

異常検知なら、

- 異常を見逃したくない → **Recall**
- 無駄な警報を減らしたい → **Precision**
- 両方をバランスよく見たい → **F1**
- 全体で何件当たったか → **Accuracy**

と考えます。

しきい値を固定せずモデルのスコア全体を見るなら、ROC曲線やPR曲線を考えます。

## 定義・仕組み

### 混同行列が土台

まず[混同行列](/gk/confusion-matrix/)の4要素を確認します。

- TP：陽性を陽性
- TN：陰性を陰性
- FP：陰性を陽性 → **誤検知**
- FN：陽性を陰性 → **見逃し**

### Accuracy

[Accuracy](/gk/accuracy/)は全体の正解割合です。

クラスが大きく偏ると、多数派だけを予測して高く見える場合があります。

### Precision

[Precision](/gk/precision/)は、

**TP / (TP + FP)**

です。

分母は**予測陽性**です。

### Recall

[Recall](/gk/recall/)は、

**TP / (TP + FN)**

です。

分母は**実際陽性**です。

### F1-score

[F1-score](/gk/f1-score/)はPrecisionとRecallの**調和平均**です。

TNは式に直接入りません。

### ROC-AUC

[ROC-AUC](/gk/roc-auc/)は、

- 縦軸：TPR = Recall
- 横軸：FPR

で、しきい値を変えたときの識別性能を見ます。

### PR曲線

[Precision-Recall曲線](/gk/precision-recall-curve/)は、

- 縦軸：Precision
- 横軸：Recall

です。

陽性が少なく、陽性クラスの性能を重点的に見たいとき有用になりやすい指標です。

## いつ使う？（得意・不得意）

### 見逃しが重大

医療スクリーニングや重大故障などでは、FNを減らす**Recall**を重視します。

### 誤検知が重大

不要な警報・確認作業を減らしたいなら、FPを意識した**Precision**を重視します。

### 両方重要

PrecisionとRecallを1値にまとめたいなら**F1-score**を考えます。

### クラス不均衡

不均衡だから自動的にF1やPRだけを使うのではありません。

**業務上どの誤りが重要か**を先に決めます。

## G検定ひっかけポイント

### PrecisionとRecall

- 予測陽性が分母 → **Precision**
- 実際陽性が分母 → **Recall**

### FP / FN

- FP → **誤検知**
- FN → **見逃し**

### ROCとPR

- ROC → **TPR / FPR**
- PR → **Precision / Recall**

### Accuracy

❌ 高ければ必ず良いモデル  
⭕ **クラス比率・誤りコストも確認する**

## まとめ（試験直前用）

- 全体 → **Accuracy**
- 誤検知を減らす → **Precision**
- 見逃しを減らす → **Recall**
- 両者のバランス → **F1**
- TPRとFPR → **ROC**
- PrecisionとRecall → **PR**
- **指標名より「何を失敗と見るか」で切る**

{% include gk_article_footer.html %}
