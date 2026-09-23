---
layout: page
title: 勾配ブースティングとは？損失の負の勾配を逐次学習【G検定対策】
description: "勾配ブースティング（Gradient Boosting）を、現在のアンサンブルの損失を減らす方向、すなわち負の勾配に弱学習器を逐次適合させる手法として整理します。二乗誤差では残差との関係が見えること、AdaBoostやBaggingとの違いをG検定向けに確認します。"
permalink: /gk/gradient-boosting/
tags: [gk, ensemble]
gk_section: 機械学習の概要/代表的な手法/教師あり学習/アンサンブル学習
gk_order: 5
last_modified_at: 2026-09-23
---

## まず結論

**Gradient Boosting（勾配ブースティング）**は、現在のモデルの損失を減らす方向に、**弱学習器を1つずつ逐次追加するアンサンブル学習**です。

G検定では、

- Boosting → 逐次
- Gradient Boosting → **損失の負の勾配を近似**
- Bagging → 主に独立・並列

で切り分けます。

## 直感的な説明

最初のモデルで予測し、どこを直せば損失が下がるかを調べます。

次の弱学習器は、

> **今のモデルに足すと、損失が減る方向**

を学びます。

これを繰り返して予測関数を改善します。

## 定義・仕組み

Gradient Boostingでは、現在のモデルに対する損失関数の**負の勾配**を計算し、その値を次の弱学習器で近似します。

弱学習器には**浅い決定木**がよく使われます。

### 二乗誤差の場合

二乗誤差を損失に使う回帰では、負の勾配が**残差**に対応します。

そのため、

> 前の残差を次の木が学ぶ

と説明されることがあります。

ただし、これは二乗誤差で特に直感的な見方です。

一般のGradient Boostingは、**損失関数の勾配**として理解する方が正確です。

### 勾配降下法との関係

Gradient Boostingとニューラルネットワークの通常の勾配降下法は同じアルゴリズムではありません。

一方で、どちらも**損失を勾配方向に減らす**という考え方を持ちます。

- ニューラルネット → パラメータを勾配で更新
- Gradient Boosting → 予測関数へ弱学習器を追加

という違いです。

## いつ使う？（得意・不得意）

Gradient Boostingは、

- 分類
- 回帰
- 表形式データ

などで広く使われます。

逐次学習のためBaggingほど単純に並列化しにくく、木の数・深さ・学習率などを調整しないと過学習する場合があります。

## G検定ひっかけポイント

### Gradient Boosting＝Bagging？

❌ ブートストラップ標本で独立に学習  
⭕ **弱学習器を逐次追加**

### 必ず誤分類サンプルの重みを増やす？

❌ BoostingならすべてAdaBoost方式  
⭕ **誤分類サンプルの重み付けはAdaBoostの代表的特徴**

### 残差を学ぶ？

⭕ 二乗誤差では分かりやすい説明  
ただし一般には**負の勾配を近似**すると覚える方が安全です。

## まとめ（試験直前用）

- Gradient Boosting＝**逐次アンサンブル**
- 損失の**負の勾配**を学ぶ
- 弱学習器は決定木が代表的
- 二乗誤差では残差と対応
- AdaBoostとは補正方法が異なる
- Baggingは主に独立、Boostingは逐次

## 参考資料

- [Greedy Function Approximation: A Gradient Boosting Machine｜Friedman](https://statweb.stanford.edu/~jhf/ftp/trebst.pdf)
- [Boosting](/gk/boosting/)

{% include gk_article_footer.html %}
