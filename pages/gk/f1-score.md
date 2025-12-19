---
layout: page
title: F1-score
permalink: /gk/f1-score/
tags: [gk, 機械学習, 評価指標, 頻出]
---

## まず結論
F1-score は、**Precision（適合率）と Recall（再現率）のバランスを1つの値で表した指標**です。

**F1-score = 2 × (Precision × Recall) / (Precision + Recall)**

👉 **どちらか一方が低いと、F1-score も低くなります。**

---

## なぜ F1-score が必要？
Precision と Recall は、よく **トレードオフ** になります。

- Precision を上げる  
  → 慎重になる → Recall が下がる  
- Recall を上げる  
  → 積極的になる → Precision が下がる  

👉 **両方を同時に評価したい** ときに使うのが F1-score です。

---

## 直感的な説明
- Precision：当たったと言ったものは本当に当たっている？
- Recall：本物をちゃんと拾えている？

F1-score は  
👉 **「当てる力」と「拾う力」のバランス点**  
と考えると分かりやすいです。

---

## 混同行列との関係
混同行列では、

- Precision = TP / (TP + FP)
- Recall = TP / (TP + FN)

これらを組み合わせたのが F1-score です。

👉 **TP・FP・FN の3つが効く指標**  
（TN は直接使われない点もひっかけポイント）

---

## いつ使う？（得意・不得意）
### 得意
- クラスの偏りがあるデータ
- 誤検知も見逃しも、どちらも困る場合
- Accuracy だけでは評価できない問題

例：
- 異常検知
- 医療診断
- 不正検知

### 苦手
- Precision と Recall のどちらか一方だけを重視したい場合

---

## Accuracy との違い
- Accuracy：全体の正解率  
- F1-score：**陽性クラスに注目したバランス評価**

👉 データが偏っている場合、  
**F1-score のほうが実態を表す**ことが多い。

---

## G検定ひっかけポイント
- F1-score は **調和平均**
- Precision または Recall が 0 なら、F1-score も 0
- **TN は直接使われない**

---

## よくある勘違い
- ❌ F1-score が高い＝完璧  
  → ⭕ Precision と Recall のバランスが良いだけ
- ❌ F1-score は正解率  
  → ⭕ **別の概念**

---

## まとめ（試験直前用）
- F1-score = **Precision と Recall のバランス指標**
- どちらかが低いと値は上がらない
- クラス不均衡データで有効
- Accuracy と **役割が違う**
