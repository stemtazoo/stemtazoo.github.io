---
layout: page
title: Precision–Recall曲線とは？ROC曲線との違い【G検定対策】
description: Precision–Recall曲線は、しきい値を変えたときのPrecisionとRecallの関係を見る評価グラフです。陽性が少ないクラス不均衡でROC曲線より実態を捉えやすい理由、軸の違い、APとの関係をG検定向けに整理します。
permalink: /gk/precision-recall-curve/
tags: [gk, 機械学習, 評価指標, 頻出]
gk_section: 機械学習の概要/モデルの選択・評価
gk_order: 7
last_modified_at: 2026-08-21
---

## まず結論

Precision–Recall（PR）曲線は、**しきい値を変化させたときのPrecisionとRecallの関係**を見るグラフです。

G検定では、まず次で切ります。

> **陽性が少ない不均衡データで、陽性クラスの性能を重視 → PR曲線**

## 直感的な説明

しきい値を緩くすると、多くを陽性として拾うためRecallは上がりやすくなりますが、誤検知も増えてPrecisionは下がりやすくなります。

逆に、しきい値を厳しくするとPrecisionは上がりやすい一方、見逃しが増えてRecallは下がりやすくなります。

```text
積極的に陽性判定
→ Recall ↑ / Precision ↓

慎重に陽性判定
→ Recall ↓ / Precision ↑
```

PR曲線は、このトレードオフをしきい値全体で確認します。

## 定義・仕組み

PR曲線の軸は次のとおりです。

- 横軸：Recall
- 縦軸：Precision

ROC曲線との違いはここが最重要です。

| 観点 | ROC曲線 | PR曲線 |
|---|---|---|
| 横軸 | FPR | Recall |
| 縦軸 | TPR（Recall） | Precision |
| 主な着目 | 陽性・陰性を含む識別性能 | 陽性クラスの検出と誤検知 |
| 不均衡データ | 高く見えることがある | 陽性が少ないとき有用になりやすい |

ROC曲線については[ROC曲線・AUC](/gk/roc-auc/)も確認してください。

### AP（Average Precision）

APは、PR曲線上のPrecisionをRecallの変化に応じて要約する代表的な指標です。

実装や定義によって計算方法の細部は異なりますが、G検定では **PR性能を1つの値に要約する指標** と押さえれば十分です。

## いつ使う？（得意・不得意）

### 得意なこと

- 異常検知
- 不正検知
- 医療診断
- 検索や情報抽出など、陽性が少ない問題

### 苦手・注意点

- クラスがほぼ均等ならROC曲線でも十分比較しやすいことがある
- PR曲線だけでは特定しきい値での業務コストまでは決まらない
- PrecisionとRecallのどちらを重視するかは用途次第

## G検定ひっかけポイント

- PR曲線の横軸はRecall
- PR曲線の縦軸はPrecision
- ROC曲線の横軸はFPR
- 「クラス不均衡なら必ずPRだけを見る」とは限らない
- 特に **陽性が少なく、陽性クラスの性能を重視したいとき** PR曲線が有用
- APはPR性能を要約する代表的指標

## まとめ（試験直前用）

- PR曲線 = **PrecisionとRecallの関係**
- 横軸Recall、縦軸Precision
- 陽性が少ない不均衡データで有用になりやすい
- ROCはTPRとFPR、PRはPrecisionとRecall
- APはPR性能を1つの値に要約する指標

{% include gk_article_footer.html %}