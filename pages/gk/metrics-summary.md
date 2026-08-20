---
layout: page
title: 分類の評価指標まとめ｜Accuracy・Precision・Recall・F1・ROC・PR【G検定】
description: "分類の主要評価指標を、全体正解率・誤検知・見逃し・PrecisionとRecallのバランス・しきい値全体という観点で整理します。Accuracy、Precision、Recall、F1、ROC-AUC、PR曲線をG検定で選択肢から切り分ける判断基準を確認できます。"
permalink: /gk/metrics-summary/
tags: [gk, 機械学習, 評価指標, まとめ, 頻出]
gk_section: 機械学習の概要/モデルの選択・評価
gk_order: 8
last_modified_at: 2026-08-21
---

## まず結論

分類指標は、**何を失敗として重く見るか**で選びます。

> **全体 → Accuracy**  
> **誤検知 → Precision**  
> **見逃し → Recall**  
> **PrecisionとRecallの両方 → F1**  
> **しきい値全体 → ROC / PR**

## 直感的な説明

同じ分類モデルでも、目的によって良い指標は変わります。

- スパム判定で正常メールを誤って捨てたくない → **Precision**を意識
- 病気の人を見逃したくない → **Recall**を意識
- 全体の正解数を見たい → **Accuracy**

つまり、指標名を暗記するより、**FP（誤検知）とFN（見逃し）のどちらが困るか**を先に考えると切りやすくなります。

## 定義・仕組み

### 混同行列

| | 予測：陽性 | 予測：陰性 |
|---|---|---|
| 実際：陽性 | TP | FN |
| 実際：陰性 | FP | TN |

- **FP**：誤検知
- **FN**：見逃し

Accuracy・Precision・Recall・F1など、多くの分類指標はこの4要素をもとに整理できます。ただし、ROC-AUCのように**しきい値を変えたときの性能全体**を見る指標は、単一の混同行列だけでは表せません。

| 指標 | 何を見る？ | 判断キーワード |
|---|---|---|
| Accuracy | 全体でどれだけ正しいか | 全体正解率 |
| Precision | 予測陽性のうち本当に陽性か | FP・誤検知 |
| Recall | 実際陽性をどれだけ拾えたか | FN・見逃し |
| F1 | PrecisionとRecallの調和平均 | 両方のバランス |
| ROC-AUC | FPRとTPRの関係をしきい値全体で見る | 識別・ランキング性能 |
| PR曲線 | PrecisionとRecallの関係を見る | 陽性が少ない・陽性重視 |

## いつ使う？（得意・不得意）

- クラス比率が比較的素直で、全体の正解率を見たい → Accuracy
- 誤検知コストが高い → Precision
- 見逃しコストが高い → Recall
- PrecisionとRecallの両方を1値にまとめたい → F1
- しきい値全体でモデルの識別性能を比較したい → ROC-AUC
- 陽性が少なく、その陽性クラスを重視したい → PR曲線

「不均衡データなら必ずF1・PR」と機械的に決めるのではなく、**何を評価したいか**を見るのが大切です。

## G検定ひっかけポイント

- ❌ **すべての評価指標は単一の混同行列から計算できる** → 誤り
- ❌ **Precisionは見逃しを直接重視する** → Recallと逆
- ❌ **Recallの分母は予測陽性** → それはPrecision
- ❌ **F1はPrecisionとRecallの算術平均** → 調和平均
- ❌ **ROC-AUCが高ければ、特定のしきい値で必ず最適** → 誤り

迷ったら、分母と失敗の種類を確認します。

> **予測陽性が分母 → Precision**  
> **実際陽性が分母 → Recall**

## まとめ（試験直前用）

- Accuracy＝全体
- Precision＝誤検知FPを意識
- Recall＝見逃しFNを意識
- F1＝PrecisionとRecallの調和平均
- ROC / PR＝しきい値全体を見る

関連： [混同行列](/gk/confusion-matrix/) / [ROC-AUC](/gk/roc-auc/) / [Precision-Recall曲線](/gk/precision-recall-curve/)

{% include gk_article_footer.html %}
