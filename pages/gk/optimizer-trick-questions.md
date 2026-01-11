---
layout: page
title: G検定ひっかけ最適化問題10連発【SGD / Adam / RMSprop ほか｜解説付き】
permalink: /gk/optimizer-trick-questions/
tags: [gk, cheatsheet, neural_network]
gk_section: ディープラーニングの概要/最適化手法
gk_order: 22
---

## まず結論
- G検定の最適化問題は **用語暗記ではなく「問題文のキーワード」**で切る。
- この10問が判断できれば、最適化手法は落とさない。

---

## 問題1
**学習率を固定して更新する、最も基本的な最適化手法はどれか。**

A. Adam  
B. RMSprop  
C. SGD  
D. AdaGrad  

**正解：C**

👉 **「学習率固定」**が見えたら即SGD。

---

## 問題2
**勾配の二乗和を蓄積し、頻出特徴の学習率が小さくなりやすい手法はどれか。**

A. RMSprop  
B. AdaGrad  
C. Adam  
D. SGD  

**正解：B**

👉 **「二乗和を蓄積」＝ AdaGrad**

---

## 問題3
**AdaGradの「学習率が減りすぎる」欠点を改善した手法はどれか。**

A. Adam  
B. Adadelta  
C. RMSprop  
D. AMSGrad  

**正解：C**

👉 **AdaGradの改良 → RMSprop**

---

## 問題4
**学習率を明示的に設定せず、勾配の移動平均を利用する手法はどれか。**

A. RMSprop  
B. Adam  
C. Adadelta  
D. SGD  

**正解：C**

👉 **「学習率を設定しない」＝ Adadelta**

---

## 問題5
**モーメント法とRMSpropの考え方を組み合わせた手法はどれか。**

A. AdaGrad  
B. Adam  
C. AMSGrad  
D. SGD  

**正解：B**

👉 **「モーメント＋Adaptive」＝ Adam**

---

## 問題6
**Adamの収束性の問題を理論的に改善した手法はどれか。**

A. RMSprop  
B. AdaBound  
C. AMSGrad  
D. SGD  

**正解：C**

👉 **Adamの安定版 → AMSGrad**

---

## 問題7
**学習初期はAdamのように振る舞い、終盤はSGDに近づく手法はどれか。**

A. AMSGrad  
B. AdaBound  
C. RMSprop  
D. Adadelta  

**正解：B**

👉 **Adam → SGD の流れ＝ AdaBound**

---

## 問題8
**学習初期はAMSGrad、終盤はSGDに近づく手法はどれか。**

A. Adam  
B. AdaBound  
C. AMSBound  
D. RMSprop  

**正解：C**

👉 **AMSGrad → SGD の流れ＝ AMSBound**

---

## 問題9
**汎化性能が高いが、収束が遅くなりやすい手法はどれか。**

A. Adam  
B. RMSprop  
C. AdaGrad  
D. SGD  

**正解：D**

👉 **「汎化が良いが遅い」＝ SGD**

---

## 問題10（超ひっかけ）
**文章中の単語の重要度を数値化する手法として最も適切なものはどれか。**

A. RMSprop  
B. Adam  
C. TF-IDF  
D. AdaGrad  

**正解：C**

👉 **TF-IDFは最適化手法ではない！**

---

## G検定での最終判断ルール（超重要）
- **学習率固定 → SGD**
- **二乗和 → AdaGrad**
- **AdaGrad改良 → RMSprop**
- **学習率不要 → Adadelta**
- **モーメント＋Adaptive → Adam**
- **Adam安定化 → AMSGrad**
- **Adam → SGD → AdaBound**
- **AMSGrad → SGD → AMSBound**
- **最適化じゃない → TF-IDF**

---

## まとめ（試験直前用）
- 名前を見て判断しない
- 問題文のキーワードを拾う
- 「Adam系」「Bound系」を見分ける
- TF-IDFは最適化ではない
- この10問が解ければ十分
