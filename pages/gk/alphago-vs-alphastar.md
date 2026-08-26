---
layout: page
title: AlphaGoとAlphaStarの違い【比較チートシート｜G検定対策】
description: "AlphaGoとAlphaStarを、対象ゲームと環境の違いから比較します。囲碁・MCTS・交互手番のAlphaGoと、StarCraft II・リアルタイム・不完全情報のAlphaStarをG検定で迷わない形に整理します。"
permalink: /gk/alphago-vs-alphastar/
tags: [gk, reinforcement_learning, cheatsheet]
gk_section: ディープラーニングの応用例/深層強化学習/代表エージェント・プロジェクト
gk_order: 3
last_modified_at: 2026-08-26
---

## まず結論

**AlphaGo**は囲碁を対象に、方策・価値ネットワークとモンテカルロ木探索（MCTS）を組み合わせたAIです。

**AlphaStar**はStarCraft IIを対象に、リアルタイム・不完全情報の複雑な対戦環境へ対応したAIです。

G検定では、**「囲碁＋MCTS → AlphaGo」「StarCraft II＋リアルタイム → AlphaStar」**で切り分けます。

## 直感的な説明

- AlphaGo：盤面を見て、次の手を探索しながら選ぶ囲碁AI
- AlphaStar：刻々と変わるゲーム状況で、長期戦略と多数の行動を扱うStarCraft II AI

重要なのは、**単純に「単一エージェント vs マルチエージェント」で分けない**ことです。

## 定義・仕組み

### AlphaGo

- 対象：囲碁
- 2人対戦・交互手番
- 方策ネットワーク
- 価値ネットワーク
- **MCTS**を利用

### AlphaStar

- 対象：StarCraft II
- リアルタイム
- 不完全情報
- 長い時間軸と大きな行動空間
- 自己対戦を含む学習を利用

両者はどちらも対戦ゲームAIですが、**対象環境と採用する仕組みが異なる**と覚えるのが安全です。

## いつ使う？（得意・不得意）

この2つは一般-purposeのアルゴリズムを選ぶ問題ではなく、著名なAIシステムの**対象ゲームと特徴の対応**として問われることが中心です。

## G検定ひっかけポイント

### よくある誤解

- ❌ AlphaGo＝単一エージェントだから、AlphaStar＝マルチエージェントと覚える
- ❌ 複数ユニットを操作するから、それだけでマルチエージェント強化学習
- ❌ AlphaStarは囲碁AI

### 選択肢を切る判断基準

- 囲碁 / MCTS / 交互手番 → **AlphaGo**
- StarCraft II / RTS / リアルタイム / 不完全情報 → **AlphaStar**
- 「複数エージェント」が論点なら、ゲーム名ではなく**複数の意思決定主体をどう扱うか**を確認する

## まとめ（試験直前用）

- AlphaGo＝囲碁＋MCTS
- AlphaStar＝StarCraft II＋リアルタイム
- 単純な単一／マルチ分類で覚えない
- 対象ゲームと環境特性で切る
- 「StarCraft II」ならAlphaStar

{% include gk_article_footer.html %}
