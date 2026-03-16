---
layout: page
title: Precision–Recall曲線
permalink: /gk/precision-recall-curve/
tags: [gk, 機械学習, 評価指標, 頻出]
gk_section: 機械学習の概要/モデルの選択・評価
gk_order: 7
---

## まず結論

Precision–Recall（PR）曲線は、**しきい値を変化させたときの Precision（適合率）と Recall（再現率）の関係**を表すグラフです。

👉 **クラス不均衡データでは、ROC曲線より重要になることが多い** 指標です。

---

## 直感的な説明

* Precision：当たったと言ったものは、本当に当たっている？
* Recall：本物をどれだけ拾えている？

しきい値を変えると、

* 積極的に拾う → Recall↑ / Precision↓
* 慎重に拾う → Recall↓ / Precision↑

👉 **このトレードオフを1枚で見る**のが PR曲線です。

---

## PR曲線の軸

* **横軸**：Recall（再現率）
* **縦軸**：Precision（適合率）

```text
縦軸：Precision
↑
|●
|  ●
|    ●
|       ●
+----------------→ 横軸：Recall
```

---

## ROC曲線との違い（重要）

| 観点   | ROC曲線       | PR曲線       |
| ---- | ----------- | ---------- |
| 縦軸   | TPR（Recall） | Precision  |
| 横軸   | FPR         | Recall     |
| 強い場面 | 全体性能        | **クラス不均衡** |

👉 陽性が少ない問題では、PR曲線の方が実態を反映しやすい。

---

## いつ使う？（得意・不得意）

### 得意

* 異常検知（異常が少ない）
* 医療診断（病気が少ない）
* 不正検知

### 苦手

* クラスがほぼ均等な場合（ROCでも十分）

---

## Average Precision（AP）について

PR曲線では、**Average Precision（AP）** という指標がよく使われます。

* PR曲線下の面積を表す指標
* ROCのAUCに相当

👉 **APが大きいほど、PrecisionとRecallのバランスが良い**。

---

## G検定ひっかけポイント

* PR曲線は **Precision × Recall の関係**を見る
* クラス不均衡では **ROCよりPR**
* APは PR曲線の面積

---

## よくある勘違い

* ❌ ROCがあればPRはいらない
  → ⭕ 不均衡データではPRが重要
* ❌ PR曲線はAccuracyを見る
  → ⭕ PrecisionとRecallを見る

---

## まとめ（試験直前用）

* PR曲線：PrecisionとRecallの関係
* クラス不均衡データで強い
* APはPR曲線の面積
* ROC/AUCと**使い分ける**
