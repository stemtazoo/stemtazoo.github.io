---
layout: page
title: DQNとPolicy Gradientの違い｜Q値か方策か【G検定対策】
description: "DQNとPolicy Gradientを、DQNはQ値をニューラルネットワークで近似する価値ベース、Policy Gradientは方策を直接最適化する方策ベースとして比較します。離散・連続行動を絶対的な分類にせず、何を直接学ぶかというG検定の判断軸で整理します。"
permalink: /gk/dqn-vs-policy-gradient/
tags: [gk, reinforcement_learning, cheatsheet]
gk_section: ディープラーニングの応用例/深層強化学習/DQN・改良手法
gk_order: 7
last_modified_at: 2026-09-23
---

## まず結論

DQNとPolicy Gradientの最大の違いは、**何を直接学ぶか**です。

- **DQN**：行動価値 Q(s,a) を学ぶ
- **Policy Gradient**：方策 π(a|s) を直接最適化する

G検定では、まず

> **Q値？ → DQN系**  
> **方策？ → Policy Gradient系**

で切ります。

## 直感的な説明

### DQN

「この状態で、この行動をしたらどれくらい得か？」という**点数表（Q値）**を学び、その値から行動を選びます。

### Policy Gradient

「この状態では、この行動をどれくらい選びやすくするか」という**行動方針そのもの**を学びます。

## 定義・仕組み

### DQN

[DQN](/gk/dqn/)はQ学習を深層学習へ拡張し、Q値をニューラルネットワークで近似します。

代表的な要素は、

- Experience Replay
- Target Network

です。

基本的なDQNは、各行動に対応するQ値を出力して最大値を選ぶため、**離散行動空間で使われる代表手法**です。

### Policy Gradient

Policy Gradientは、期待収益が大きくなる方向へ**方策パラメータを直接更新**します。

代表例には、

- REINFORCE
- PPO

などがあります。

Actor-Criticでは、方策を直接更新しながらCriticの価値推定も利用します。

## いつ使う？（得意・不得意）

行動空間については、次のように整理します。

- 基本DQN → 離散行動に自然に対応
- Policy Gradient → 連続行動を表現しやすい場合がある

ただし、

> 離散行動なら必ずDQN  
> 連続行動なら必ずPolicy Gradient

という絶対ルールではありません。

方策勾配法は離散行動にも使えます。モデル選択は、行動空間だけでなく学習方式や問題設定によって変わります。

## G検定ひっかけポイント

### DQN＝方策を直接学ぶ？

❌ 方策 π を直接最適化する  
⭕ **Q値を学び、Q値から行動を選ぶ**

### Policy Gradient＝価値関数を使わない？

❌ 価値推定は一切使えない  
⭕ **Actor-CriticではCriticの価値推定を利用できる**

### 離散 / 連続

❌ 離散＝DQN、連続＝Policy Gradientと完全固定  
⭕ **代表的な得意領域ではあるが、分類の本質は「Q値か方策か」**

### Experience Replay

DQNで代表的ですが、**強化学習全体に必須の仕組みではありません。**

## まとめ（試験直前用）

- DQN＝**Q値を学ぶ価値ベース**
- Policy Gradient＝**方策を直接学ぶ**
- DQN＝Experience Replay＋Target Networkが代表的
- Policy Gradient＝REINFORCE・PPOなど
- Actor-Critic＝方策＋価値
- **離散 / 連続より「何を直接学ぶか」を優先して判断**

{% include gk_article_footer.html %}
