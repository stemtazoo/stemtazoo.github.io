---
layout: page
title: 最適化手法まとめ｜SGD・Momentum・AdaGrad・RMSprop・Adam【G検定】
description: "ニューラルネットワークの最適化手法を、慣性、勾配二乗の累積、指数移動平均、1次・2次モーメント、動的な学習率境界という判断軸で比較します。SGDからAdam、AdaDelta、AdaBound、AMSBoundまでをG検定向けに整理します。"
last_modified_at: 2026-08-21
permalink: /gk/optimization-cheatsheet/
tags: [gk, neural_network, optimization, cheatsheet]
gk_section: ディープラーニングの概要/最適化手法
gk_order: 12
---

## まず結論

最適化手法は、**勾配をどう記憶し、更新幅をどう調整するか**で切り分けます。

| 判断キーワード | 手法 |
|---|---|
| 基本の勾配更新 | SGD |
| 慣性・過去の更新方向 | Momentum |
| 勾配二乗を累積 | AdaGrad |
| 勾配二乗の指数移動平均 | RMSprop |
| 勾配と更新量の移動平均 | AdaDelta |
| 1次・2次モーメント | Adam |
| Adam系＋動的な境界 | AdaBound |
| AMSGrad系＋動的な境界 | AMSBound |

G検定では、**どれが一番優れているかではなく、何を使って更新するか**を見るのが安全です。

## 直感的な説明

坂を下る方法として考えます。

- SGD：今の傾きを見て進む
- Momentum：これまでの勢いも使う
- AdaGrad：よく動いた方向は歩幅を小さくする
- RMSprop：昔の情報を弱めながら歩幅を調整する
- AdaDelta：最近の勾配と更新量から歩幅を決める
- Adam：勢いと歩幅調整を両方使う
- Bound系：適応的な歩幅に上限・下限を付ける

## 定義・仕組み

### SGD

勾配を使ってパラメータを更新する基本形です。

狭義のSGDは1サンプルずつ更新しますが、深層学習の実務ではミニバッチSGDを単にSGDと呼ぶこともあります。

### Momentum

過去の更新方向を利用して**慣性**を持たせます。

```text
キーワード → 慣性・速度・振動抑制
```

### AdaGrad

各パラメータについて**過去の勾配二乗を累積**します。

```text
AdaGrad → ためる
```

累積値が増え続けるため、学習後半に実効学習率が小さくなりすぎることがあります。

### RMSprop

勾配二乗を**指数移動平均**で管理し、古い情報の影響を弱めます。

```text
AdaGrad → 累積
RMSprop → 移動平均
```

### AdaDelta

勾配二乗の移動平均に加えて、**更新量の移動平均**も利用します。

AdaGradの学習率縮小問題を補う系統として整理できます。

### Adam

勾配の**1次モーメント推定**と**2次モーメント推定**を使います。

Momentum系とRMSprop系の考え方を組み合わせたものとして理解すると切り分けやすいです。

2次モーメントを単純に「分散」と覚えるのではなく、**勾配二乗のモーメント推定**と押さえます。

### Bound系

AdaBoundやAMSBoundは、パラメータごとの実効学習率に**時間とともに変化する上限・下限**を設けます。

| 手法 | 基盤 | 判断キーワード |
|---|---|---|
| AdaBound | Adam | Adam＋動的な境界 |
| AMSBound | AMSGrad | AMSGrad＋動的な境界 |

学習後半にSGDに近い更新へ移ることを狙いますが、途中で突然SGDへ切り替えるわけではありません。

## いつ使う？（得意・不得意）

- SGD：基本形。設定次第で高い性能を出せる
- Momentum：振動を抑えたい
- AdaGrad：疎な特徴量などで有効なことがある
- RMSprop：最近の勾配二乗を重視して調整したい
- AdaDelta：AdaGradの累積問題を補いたい
- Adam：Momentum系＋適応的学習率を併用したい
- Bound系：適応的学習率へ動的な制約を加えたい

**AdamやBound系が常に最良とは限りません。** 問題・モデル・設定によって適する手法は変わります。

## G検定ひっかけポイント

- ❌「Adamは学習率を設定しなくてよい」
  - 基本学習率は必要です。
- ❌「Momentumは勾配二乗の移動平均を使う」
  - それはRMSprop系です。
- ❌「AdaGradは古い勾配を忘れる」
  - AdaGradは累積します。
- ❌「AdaBoundは途中でSGDへ完全に切り替える」
  - 動的な境界によりSGDに近い更新へ移ります。
- ❌「AdaBoostは最適化手法」
  - AdaBoostはアンサンブル学習です。

**判断基準**

- 慣性 → Momentum
- 二乗を累積 → AdaGrad
- 二乗の移動平均 → RMSprop
- 更新量の移動平均 → AdaDelta
- 1次＋2次モーメント → Adam
- 動的な上下限 → Bound系

## まとめ（試験直前用）

- SGD＝基本形
- Momentum＝慣性
- AdaGrad＝二乗を累積
- RMSprop＝二乗の移動平均
- AdaDelta＝勾配＋更新量の移動平均
- Adam＝1次＋2次モーメント
- Bound系＝実効学習率へ動的な境界

{% include gk_article_footer.html %}
