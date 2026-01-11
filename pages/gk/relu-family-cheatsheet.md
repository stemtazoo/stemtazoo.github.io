---
layout: page
title: ReLU / Leaky ReLU / PReLU（比較チートシート）
permalink: /gk/relu-family-cheatsheet/
tags: [gk, cheatsheet, neural_network]
gk_section: ディープラーニングの概要/活性化関数
gk_order: 4
---

## まず結論（試験で即切る）

**違いは「負の入力をどう扱うか」だけ。**

* **ReLU**：負は **0に切る**
* **Leaky ReLU**：負も **少し通す（固定）**
* **PReLU**：負を **学習して通す**

👉 G検定では、この対応関係を覚えていれば十分。

---

## 一目でわかる対応表（最重要）

| 活性化関数      | 入力 < 0 の出力 | 係数α        | 学習される？ | 代表キーワード      |
| ---------- | ---------- | ---------- | ------ | ------------ |
| ReLU       | 0          | 0          | なし     | シンプル・基本      |
| Leaky ReLU | α×入力       | 固定（例:0.01） | なし     | Dying ReLU対策 |
| PReLU      | α×入力       | 学習される      | あり     | 適応的          |

---

## 直感的な覚え方

* **ReLU**：

  > マイナスは完全に無視

* **Leaky ReLU**：

  > マイナスも「ちょっとだけ」通す

* **PReLU**：

  > マイナスをどれくらい通すかを学習する

---

## なぜLeaky ReLU / PReLUが生まれた？

ReLUには次の問題があります。

* 入力 < 0 のとき
* 勾配が 0
* 学習が止まる

👉 **Dying ReLU 問題**

これを緩和するために、

* Leaky ReLU
* PReLU

が提案されました。

---

## G検定ひっかけポイント

* ❌「Leaky ReLUは負の入力で0を出力する」
  → **ReLUの説明**

* ❌「PReLUは固定係数を使う」
  → **Leaky ReLUの説明**

* ❌「ReLUも負の入力を通す」
  → **誤り**

* ✅ **Leaky = 漏れる → 0にならない**

* ✅ **PReLU = Parameter → 学習する**

---

## よくある穴埋め問題対策

> Leaky ReLUでは、入力が負の値の場合、
> 出力は（　　　）となる。

👉 正解：**入力に小さな係数を掛けた負の値**

---

## まとめ（試験直前用）

* ReLU：負は0
* Leaky ReLU：負も少し通す（固定）
* PReLU：負の通し方を学習

👉 迷ったら

> **Leaky = 漏れる / P = Parameter**
