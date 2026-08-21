---
layout: page
title: G検定ひっかけ最適化問題10問｜SGD・Momentum・Adamほか
description: "SGD、Momentum、AdaGrad、RMSprop、AdaDelta、Adam、AdaBound、AMSBoundの違いを10問で確認します。慣性、勾配二乗の累積と移動平均、1次・2次モーメント、動的な学習率境界という判断語から選択肢を切る練習問題です。"
permalink: /gk/optimizer-trick-questions/
tags: [gk, cheatsheet, neural_network, optimization]
gk_section: ディープラーニングの概要/最適化手法
gk_order: 13
last_modified_at: 2026-08-21
---

## まず結論

最適化手法は、名前ではなく**問題文に出る仕組みのキーワード**で切ります。

先に[最適化手法まとめ](/gk/optimization-cheatsheet/)を確認してから、次の10問で判断できるか試してください。

## 直感的な説明

試験では「どれが最強か」ではなく、

- 慣性を使うのか
- 勾配二乗をためるのか
- 移動平均を使うのか
- 1次・2次モーメントを使うのか
- 学習率へ境界を設けるのか

を見ます。

## 定義・仕組み

### 問題1

**過去の更新方向を利用して慣性を持たせる手法はどれか。**

A. AdaGrad  
B. Momentum  
C. RMSprop  
D. AdaBound

**正解：B**

「慣性」「速度」「振動抑制」なら[Momentum](/gk/momentum/)です。

### 問題2

**過去の勾配二乗を累積し続ける手法はどれか。**

A. AdaGrad  
B. RMSprop  
C. Adam  
D. Momentum

**正解：A**

「二乗を累積」なら[AdaGrad](/gk/adagrad/)です。

### 問題3

**勾配二乗の指数移動平均を使い、古い情報の影響を弱める手法はどれか。**

A. SGD  
B. AdaGrad  
C. RMSprop  
D. Momentum

**正解：C**

「二乗の移動平均」なら[RMSprop](/gk/rmsprop/)です。

### 問題4

**勾配だけでなく、更新量の移動平均も使って更新幅を調整する手法はどれか。**

A. AdaDelta  
B. Momentum  
C. AdaGrad  
D. SGD

**正解：A**

[AdaDelta](/gk/adadelta/)はAdaGradの累積問題を補う系統です。

### 問題5

**勾配の1次モーメント推定と2次モーメント推定を使う手法はどれか。**

A. RMSprop  
B. Adam  
C. AdaGrad  
D. SGD

**正解：B**

「1次＋2次モーメント」なら[Adam](/gk/adam/)です。

### 問題6

**Adam系の実効学習率に、時間とともに変化する上限・下限を設ける手法はどれか。**

A. AdaDelta  
B. AdaBound  
C. RMSprop  
D. Momentum

**正解：B**

「Adam基盤＋動的な境界」なら[AdaBound](/gk/adabound/)です。

### 問題7

**AMSGradを基盤に、動的な学習率境界を加える手法はどれか。**

A. Adam  
B. AdaBound  
C. AMSBound  
D. AdaGrad

**正解：C**

「AMSGrad＋Bound」なら[AMSBound](/gk/amsbound/)です。

### 問題8

**「Adamを使えば学習率を設定する必要がない」という説明は正しいか。**

A. 正しい  
B. 誤り

**正解：B**

Adamでも基本学習率などのハイパーパラメータを設定します。

### 問題9

**「最適化手法をAdamに変えれば過学習を必ず防げる」という説明は正しいか。**

A. 正しい  
B. 誤り

**正解：B**

最適化と汎化・過学習対策は関連しますが、Adamへ変えるだけで過学習が必ず防げるわけではありません。

### 問題10

**弱学習器を逐次的に組み合わせる手法はどれか。**

A. AdaGrad  
B. AdaBound  
C. AdaBoost  
D. Adam

**正解：C**

AdaBoostは最適化手法ではなく、**ブースティングによるアンサンブル学習**です。

## いつ使う？（得意・不得意）

このページは個別手法の詳細説明ではなく、**選択肢を切る練習用**です。

仕組みを確認したい場合は[最適化手法まとめ](/gk/optimization-cheatsheet/)や各個別記事へ戻ります。

## G検定ひっかけポイント

最終的には次の対応を即答できれば十分です。

| キーワード | 手法 |
|---|---|
| 慣性 | Momentum |
| 二乗を累積 | AdaGrad |
| 二乗の移動平均 | RMSprop |
| 更新量の移動平均 | AdaDelta |
| 1次＋2次モーメント | Adam |
| Adam＋動的境界 | AdaBound |
| AMSGrad＋動的境界 | AMSBound |

「Adam＝学習率不要」「Adam＝過学習防止」のような極端な説明は切ります。

## まとめ（試験直前用）

- 慣性＝Momentum
- 累積＝AdaGrad、移動平均＝RMSprop
- 更新量も見る＝AdaDelta
- 1次＋2次＝Adam
- 動的な上下限＝Bound系
- AdaBoostは最適化ではない

{% include gk_article_footer.html %}
