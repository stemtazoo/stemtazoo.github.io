---
layout: page
title: PPOとは？Clippingで方策更新を抑える強化学習【G検定対策】
description: "PPO（Proximal Policy Optimization）を、新旧方策の確率比を使うClipped Surrogate Objectiveによって急激な方策更新を抑える代表的な方策最適化手法として整理します。Q学習との違い、Actor-Critic構成、オンポリシー型としての位置付けを確認します。"
permalink: /gk/ppo/
tags: [gk, reinforcement_learning, neural_network]
gk_section: 機械学習の概要/代表的な手法/強化学習/方策勾配・Actor-Critic
gk_order: 5
last_modified_at: 2026-09-23
---

## まず結論

**PPO（Proximal Policy Optimization）**は、方策を直接最適化する代表的な強化学習手法で、**新しい方策が古い方策から急激に変わりすぎないように更新を抑える**のが特徴です。

G検定では、

- 方策最適化
- 新旧方策の確率比
- clipping

を押さえます。

## 直感的な説明

学習で良い方向が見つかっても、方策を一気に変えると、それまでうまくいっていた行動まで崩れることがあります。

PPOは、

> **改善するが、一度に変えすぎない**

という考え方で方策を更新します。

## 定義・仕組み

PPOでは、新しい方策と古い方策について、

**同じ行動を選ぶ確率の比**

を使います。

この確率比が大きく変化したとき、目的関数への影響を**clip**して、極端な更新を抑えます。

代表的には**Clipped Surrogate Objective**を使います。

### Actor-Criticとの関係

PPOは実装上、一般に、

- Actor：方策
- Critic：価値関数

を学ぶActor-Critic型で使われます。

ただし、PPOを見分ける最大のキーワードは**clipを使った方策更新**です。

### オンポリシー

PPOは代表的な**オンポリシー系の方策最適化手法**です。

現在の方策に近いデータを使って更新するため、Replay Bufferを長期間再利用するDQN系とはデータ利用の考え方も異なります。

## いつ使う？（得意・不得意）

PPOは、

- 連続制御
- ゲーム
- ロボット
- 方策を直接学ぶ問題

などで広く使われます。

ただし、

> PPOなら必ず安定  
> PPOなら常に最も性能が高い

とは限りません。

環境・実装・ハイパーパラメータによって学習結果は変わります。

## G検定ひっかけポイント

### PPO＝Q学習？

❌ Q値の最大値を使って更新  
⭕ **方策を直接最適化する**

### clip

❌ 勾配そのものを単純に一定値へ切るGradient Clippingと同じ  
⭕ **新旧方策の確率比を使う目的関数をクリップするのが代表的PPO**

### PPO＝オフポリシー？

❌ 過去データを自由に何度でも再利用する代表的オフポリシー  
⭕ **代表的にはオンポリシー**

## まとめ（試験直前用）

- PPO＝**Proximal Policy Optimization**
- 方策を直接最適化
- 新旧方策の確率比
- Clipped Surrogate Objective
- Actor-Critic構成が一般的
- 代表的オンポリシー手法
- **Gradient Clippingと混同しない**

## 参考資料

- [Proximal Policy Optimization Algorithms｜arXiv](https://arxiv.org/abs/1707.06347)

{% include gk_article_footer.html %}
