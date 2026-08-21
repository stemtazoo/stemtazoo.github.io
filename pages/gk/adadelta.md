---
layout: page
title: AdaDeltaとは？AdaGradの弱点を補う最適化手法【G検定】
description: "AdaDeltaを、勾配二乗の指数移動平均と更新量の移動平均を使って更新幅を調整する最適化手法として整理します。AdaGradの累積による学習率縮小をどう補うか、RMSprop・Adamとの違いをG検定向けに確認します。"
permalink: /gk/adadelta/
tags: [gk, neural_network, optimization]
gk_section: ディープラーニングの概要/最適化手法
gk_order: 8
last_modified_at: 2026-08-21
---

## まず結論

AdaDeltaは、**AdaGradのように過去すべてを累積せず、最近の勾配や更新量を使って更新幅を調整する最適化手法**です。

G検定では、AdaGradの「学習率が小さくなりすぎる」弱点を補う手法として整理します。

## 直感的な説明

AdaGradは過去を全部ため込むため、学習が進むほど歩幅が小さくなりやすくなります。

AdaDeltaは、**最近の情報を重視して歩幅を決め直す**イメージです。

## 定義・仕組み

AdaDeltaでは、勾配二乗の指数移動平均に加えて、過去の更新量の情報も利用します。

```text
AdaGrad
→ 勾配二乗を累積

AdaDelta
→ 最近の勾配＋最近の更新量を利用
```

元のAdaDeltaでは、SGDのような固定のグローバル学習率を明示的に置かずに更新量を決める設計が特徴です。

## いつ使う？（得意・不得意）

### 得意なこと

- AdaGradの更新幅縮小を緩和したい
- 最近の勾配・更新量を使って自動調整したい

### 注意点

- RMSpropと似ていますが、更新量の移動平均も使う点が異なります
- Adamのように1次・2次モーメントを組み合わせる手法ではありません
- 常に他の最適化手法より優れるわけではありません

## G検定ひっかけポイント

- ❌「勾配二乗を過去すべて累積する」→ AdaGrad
- ❌「1次・2次モーメントを使う」→ Adam
- ⭕「AdaGradの弱点を、移動平均を使って補う」→ AdaDelta / RMSprop系を疑う
- ⭕「更新量の移動平均も使う」→ AdaDelta

## まとめ（試験直前用）

- AdaDelta＝AdaGradの弱点を補う適応的最適化
- 過去すべてを累積しない
- 勾配と更新量の移動平均を使う
- RMSprop・Adamとは仕組みが異なる
- 「更新量の移動平均」ならAdaDelta

{% include gk_article_footer.html %}
