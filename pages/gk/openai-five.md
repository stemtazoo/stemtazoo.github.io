---
layout: page
title: OpenAI Fiveとは？Dota 2特化AI【G検定対策】
description: "OpenAI Fiveを、Dota 2の5対5チーム戦を対象に自己対戦と大規模強化学習で訓練されたAIシステムとして整理します。AlphaGo・AlphaZero・AlphaStarとの違いをゲーム名と環境特性から切り分けます。"
permalink: /gk/openai-five/
tags: [gk, reinforcement_learning, deep_reinforcement_learning]
gk_section: ディープラーニングの応用例/深層強化学習
gk_order: 15
last_modified_at: 2026-08-23
---

## まず結論

**OpenAI Five**は、オンライン対戦ゲーム**Dota 2**の5対5チーム戦を対象にした強化学習ベースのAIシステムです。

G検定では、まず**「Dota 2 → OpenAI Five」**で切り分けます。

## 直感的な説明

囲碁のように交互に1手ずつ進むゲームではなく、Dota 2では複数のプレイヤーがリアルタイムに行動します。

OpenAI Fiveは、

- 5対5のチーム戦
- 不完全情報
- 長い時間軸
- 多数の行動の組み合わせ

を含む環境で学習した点が特徴です。

## 定義・仕組み

OpenAI Fiveでは、大規模な自己対戦を通して方策を学習しました。

試験では細かな実装より、次の位置づけを押さえれば十分です。

- 対象：**Dota 2**
- 学習：**強化学習・自己対戦**
- 特徴：**5対5、リアルタイム、不完全情報**
- 特定ゲーム向けのAIであり、汎用AIではない

AlphaGoやAlphaZeroと同じ「強化学習を使ったゲームAI」でも、対象ゲームと仕組みは異なります。

## いつ使う？（得意・不得意）

OpenAI Fiveは、Dota 2という複雑な対戦環境で強化学習をスケールさせた代表例として理解します。

一般目的の強化学習アルゴリズム名ではなく、**特定タスク向けに構築されたAIシステム**です。

## G検定ひっかけポイント

### よくある誤解

- ❌ 囲碁AI → OpenAI Five
- ❌ StarCraft II → OpenAI Five
- ❌ 複数ゲームへそのまま対応する汎用AI

### 選択肢を切る判断基準

- Dota 2 / 5対5 → **OpenAI Five**
- 囲碁 / MCTS → AlphaGo
- 囲碁・将棋・チェス → AlphaZero
- StarCraft II → AlphaStar

## まとめ（試験直前用）

- OpenAI Five＝Dota 2
- 5対5のチーム戦
- 強化学習＋自己対戦
- リアルタイム・不完全情報の環境
- ゲーム名で他の著名AIと切り分ける

{% include gk_article_footer.html %}
