---
layout: page
title: REINFORCEとActor-Criticの違いとは？G検定対策
description: "REINFORCEとActor-Criticの違いを、方策更新に何を使うかという観点から比較します。モンテカルロ収益を使う基本形のREINFORCEと、Criticの価値推定を利用するActor-Criticを切り分けます。"
permalink: /gk/reinforce-vs-actor-critic/
tags: [gk, reinforcement_learning]
gk_section: 機械学習の概要/代表的な手法/強化学習
gk_order: 14
last_modified_at: 2026-08-22
---

## まず結論

* **REINFORCE**は、基本形ではモンテカルロ収益を使って**方策を直接更新**します。
* **Actor-Critic**は、**Actorが方策を更新し、Criticが価値を推定してその更新を助ける**枠組みです。
* G検定では、**Criticによる価値推定を使うか**が大きな判断軸です。

## 直感的な説明

* **REINFORCE**：最後までやってみて、結果を見て方針を修正する
* **Actor-Critic**：行動しながら、評価役のCriticから途中でフィードバックを受ける

Actor-Criticでは価値推定を使うため、REINFORCEの基本形より勾配推定の分散を抑えやすくなります。

## 定義・仕組み

### REINFORCE
- 方策 `π(a|s; θ)` を直接最適化
- 基本形ではモンテカルロ収益を利用
- 価値関数を学習するCriticは持たない
- ベースラインを加えて分散を下げる拡張は可能

### Actor-Critic
- **Actor**：方策を更新
- **Critic**：V値やQ値などを推定
- Criticの評価を使ってActorの更新を助ける

## いつ使う？（得意・不得意）

### REINFORCE
- 方策勾配法の基本を理解しやすい
- 実装が比較的単純
- 一方で分散が大きくなりやすい

### Actor-Critic
- 価値推定を利用して更新を効率化・安定化しやすい
- ActorとCriticの両方を学ぶため構成は複雑になる

## G検定ひっかけポイント

### よくある誤解
- ❌ REINFORCEはQ値を直接学習する
- ❌ Actor-Criticでは方策を学習しない
- ❌ REINFORCEはどんな拡張でも価値情報を一切使わない

最後は強すぎる表現です。**基本形のREINFORCEにはCriticがありません**が、ベースラインとして価値推定を使う拡張はあります。

### 判断基準
- 「モンテカルロ収益で方策を直接更新」→ REINFORCE
- 「Actor＋Critic」→ Actor-Critic
- 「Criticが価値を推定」→ Actor-Critic

## まとめ（試験直前用）

- REINFORCE＝基本形はモンテカルロ型の方策勾配法
- Actor-Critic＝Actorが方策、Criticが価値
- Criticを使うことで分散を抑えやすい
- 「価値関数を絶対使わない」と一般化しすぎない
- **Criticの有無**が最短の判断軸

{% include gk_article_footer.html %}
