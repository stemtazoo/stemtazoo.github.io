---
layout: page
title: REINFORCEとActor-Criticの違いとは？G検定対策
permalink: /gk/reinforce-vs-actor-critic/
tags: [gk, reinforcement_learning]
gk_section: 機械学習の概要/代表的な手法/強化学習
gk_order: 5
---

## まず結論

* **REINFORCE**は価値関数を使わず**方策（ポリシー）を直接勾配で更新**する手法、**Actor-Critic**は**方策（Actor）と価値関数（Critic）を併用**して学習を安定させる手法です。
* G検定では「**価値関数を使うかどうか**」「**分散を下げる工夫があるか**」が判断ポイントになります。

## 直感的な説明

* **REINFORCE**：行動して結果を見て、良ければクセを強め、悪ければ弱める“**一発反省型**”。
* **Actor-Critic**：行動（Actor）に対して、その良し悪しを評価役（Critic）がすぐ教える“**コーチ付き**”。
* コーチがいる分、Actor-Criticの方が**学習が安定**します。

## 定義・仕組み

* **REINFORCE（方策勾配法）**

  * 方策 (\pi(a|s;\theta)) を**直接最適化**
  * **価値関数を使わない**（モンテカルロ報酬）
  * 分散が大きくなりやすい

* **Actor-Critic**

  * **Actor**：方策を更新
  * **Critic**：価値関数（VやQ）で評価
  * **Advantage** 等を使い分散を低減

## いつ使う？（得意・不得意）

### REINFORCE

* 得意：実装がシンプル、理論が分かりやすい
* 不得意：学習が不安定、サンプル効率が悪い

### Actor-Critic

* 得意：学習が安定、実用向き
* 不得意：構成が複雑

## G検定ひっかけポイント

* **最大のひっかけ**

  * 「REINFORCEは価値関数を最適化する」→ ❌
* 正しい切り分け

  * 価値関数なしで方策更新 → **REINFORCE**
  * 価値関数を使って方策更新 → **Actor-Critic**
* 選択肢で

  * 「分散を下げるためCriticを用いる」→ Actor-Critic
  * 「モンテカルロで直接更新」→ REINFORCE

## まとめ（試験直前用）

* REINFORCE：方策のみ、価値関数なし
* Actor-Critic：Actor＋Criticの二役
* 安定性重視ならActor-Critic
* 「価値関数を使うか」が最短判断軸
