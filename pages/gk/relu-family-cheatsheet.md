---
layout: page
title: ReLU・Leaky ReLU・PReLUの違い【G検定比較】
description: "ReLU・Leaky ReLU・PReLUを、負の入力を0にするReLU、固定された小さな傾きを残すLeaky ReLU、その傾きを学習するPReLUとして比較します。Dying ReLUとの関係を押さえ、負側の傾きが固定か学習可能かで選択肢を切ります。"
permalink: /gk/relu-family-cheatsheet/
tags: [gk, cheatsheet, neural_network, activation]
gk_section: ディープラーニングの概要/活性化関数
gk_order: 4
last_modified_at: 2026-09-26
---

## まず結論

違いは、**負の入力をどう扱うか**です。

| 関数 | 負の入力 | 負側の傾き |
|---|---|---|
| ReLU | 0 | 0 |
| Leaky ReLU | 小さな負値を通す | 固定 |
| PReLU | 小さな負値を通す | 学習する |

G検定では、

> **固定 → Leaky ReLU**  
> **学習 → PReLU**

で切ります。

## 直感的な説明

### ReLU

負の入力を0にします。

### Leaky ReLU

負の領域でも、小さな傾きを残します。

### PReLU

負側の傾きそのものをパラメータとして学習します。

## 定義・仕組み

### ReLU

正の入力はそのまま、負の入力は0です。

負の領域では勾配が0になるため、ニューロンが負側に入り続けると更新されにくくなる**Dying ReLU**が起こることがあります。

### Leaky ReLU

負の領域に固定された小さな傾きを持たせます。

これにより、負の領域でも勾配を完全には0にしません。

傾きの値は実装・設定によって異なり、

> Leaky ReLUの傾きは必ず0.01

とは限りません。

### PReLU

Leaky ReLUに似ていますが、負側の傾きを**学習可能なパラメータ**にします。

## いつ使う？（得意・不得意）

Leaky ReLU・PReLUは、ReLUの負領域で勾配が0になる問題を緩和する選択肢です。

ただし、

> Leaky ReLUやPReLUなら常にReLUより高性能

という意味ではありません。

モデルやタスクに応じて使い分けます。

## G検定ひっかけポイント

### Leaky ReLU

❌ 負側の傾きを学習する  
⭕ **固定された傾き**

### PReLU

❌ 負側を完全に0にする  
⭕ **負側の傾きを学習する**

### Dying ReLU

❌ ReLUの正の領域で勾配が大きくなりすぎる問題  
⭕ **負領域で勾配0が続き、更新されにくくなる問題**

## まとめ（試験直前用）

- ReLU＝負は0
- Leaky ReLU＝負側に**固定傾き**
- PReLU＝負側の傾きを**学習**
- Dying ReLU対策としてLeaky/PReLUを考える
- **固定か学習か**で切る

## 参考資料（原論文）

- [Rectified Linear Units Improve Restricted Boltzmann Machines｜ICML 2010](https://www.cs.toronto.edu/~fritz/absps/reluICML.pdf)
  - Nair・Hinton（2010）。ReLUを扱った初期の代表的な一次資料です。
- [Rectifier Nonlinearities Improve Neural Network Acoustic Models｜Stanford](https://ai.stanford.edu/~amaas/papers/relu_hybrid_icml2013_final.pdf)
  - Maas・Hannun・Ng（2013）。負の領域に小さな傾きを残すLeaky ReLU系のrectifierを検討しています。
- [Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification｜CVF](https://openaccess.thecvf.com/content_iccv_2015/html/He_Delving_Deep_into_ICCV_2015_paper.html)
  - Heら（ICCV 2015）。負の傾きを学習可能にするPReLUを提案しています。

{% include gk_article_footer.html %}
