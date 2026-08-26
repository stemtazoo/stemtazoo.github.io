---
layout: page
title: Actor–Critic とは？（オン／オフポリシーの位置づけ）【G検定対策】
description: "Actor–Criticを、行動を選ぶActorと、その行動を価値で評価するCriticを組み合わせる強化学習手法として整理します。方策ベースと価値ベース双方の役割、方策勾配の分散を抑える考え方、実装によってオンポリシーにもオフポリシーにもなる点をG検定向けに確認します。"
permalink: /gk/actor-critic/
tags: [gk, reinforcement_learning, neural_network]
gk_section: 機械学習の概要/代表的な手法/強化学習/方策勾配・Actor-Critic
gk_order: 2
last_modified_at: 2026-08-26
---

## まず結論
- **Actor–Critic は、「方策を更新する Actor」と「価値を推定する Critic」を組み合わせる強化学習の枠組み**です。
- G検定では **Actor＝方策、Critic＝価値** と切り分け、さらに **オンポリシーにもオフポリシーにもなり得る**点を押さえます。

## 直感的な説明
- Actor–Critic は「**プレイヤーとコーチの分業**」。
- Actor：次に何をするか決める
- Critic：その選択がどれくらい良いか評価する

REINFORCEがエピソード収益をそのまま使う基本形なのに対し、Actor-CriticではCriticの価値推定を使ってActorの更新を助けます。

## 定義・仕組み
- **Actor**：方策 π(a|s) を更新
- **Critic**：状態価値 V(s) や行動価値 Q(s,a) などを推定

学習の流れは概ね次の通りです。

1. Actor が行動を選ぶ
2. 環境から報酬と次状態を得る
3. Critic が価値を推定する
4. Criticの評価を使ってActorを更新する

Criticを使うことで、モンテカルロ収益だけに頼るREINFORCEより、方策勾配の分散を抑えやすくなります。

## いつ使う？（得意・不得意）
### 向いている場面
- 方策を直接学びたい
- 価値推定も利用して更新を安定させたい
- 連続行動を含む問題

### 注意点
- ActorとCriticの両方を学習するため設計が複雑になる
- Criticの推定誤差がActorの更新に影響する

## オン／オフポリシーの位置づけ
Actor-Criticは1つの固定アルゴリズム名というより、**設計の枠組み**です。

- **A2C / A3C**：代表的なオンポリシー系
- **DDPG / SAC**：代表的なオフポリシー系

したがって、**Actor-Critic＝必ずオンポリシー**ではありません。

## G検定ひっかけポイント
- ❌ Actor-Criticは必ずオンポリシー
- ❌ Actorが価値関数、Criticが方策を学ぶ
- ❌ Actor-CriticはDQNの別名

### 判断基準
- 「Actor＝方策」→ 正しい
- 「Critic＝価値」→ 正しい
- 「ActorとCriticを分ける」→ Actor-Critic
- 「オン／オフは派生アルゴリズム次第」→ 正しい

## まとめ（試験直前用）
- Actor-Critic＝方策役と価値評価役を分ける
- Actor：方策
- Critic：価値
- REINFORCEより価値推定を活用して分散を抑えやすい
- オン／オフポリシーは派生アルゴリズム次第

{% include gk_article_footer.html %}
