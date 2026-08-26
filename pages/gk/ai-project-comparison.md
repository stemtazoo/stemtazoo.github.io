---
layout: page
title: AlphaGo・AlphaGo Zero・AlphaZero・OpenAI Five・AlphaStar比較【G検定】
description: "AlphaGo、AlphaGo Zero、AlphaZero、OpenAI Five、AlphaStarを、対象ゲーム・人間棋譜・自己対戦・探索の違いから比較します。G検定でゲーム名と特徴を正しく対応づけるための判断基準を整理します。"
permalink: /gk/ai-project-comparison/
tags: [gk, reinforcement_learning, cheatsheet]
gk_section: ディープラーニングの応用例/深層強化学習/代表エージェント・プロジェクト
gk_order: 5
last_modified_at: 2026-08-26
---

## まず結論

これらは、ゲームを対象に深層学習・強化学習・自己対戦などを活用した著名なAIシステムですが、**対象ゲームと学習・探索の仕組みは同じではありません**。

G検定では、まず**ゲーム名**、次に**人間棋譜・自己対戦・MCTSなどの特徴**で切り分けます。

## 直感的な説明

- **AlphaGo**：囲碁。人間棋譜も利用し、方策・価値ネットワークとMCTSを組み合わせる
- **AlphaGo Zero**：囲碁。人間棋譜を使わず自己対戦から学習
- **AlphaZero**：囲碁・将棋・チェスへ同じ基本アルゴリズムを適用
- **OpenAI Five**：Dota 2の5対5チーム戦
- **AlphaStar**：StarCraft IIのリアルタイム戦略ゲーム

「どれが一番汎用的か」という曖昧な軸より、**何を対象に、どう学んだか**で覚えます。

## 定義・仕組み

| システム | 対象 | 人間の対局データ | 自己対戦 | 代表的な判断キーワード |
|---|---|---|---|---|
| AlphaGo | 囲碁 | 使用 | 使用 | 囲碁、方策・価値、MCTS |
| AlphaGo Zero | 囲碁 | 不使用 | 使用 | 囲碁、人間棋譜なし |
| AlphaZero | 囲碁・将棋・チェス | 不使用 | 使用 | 3ゲーム、自己対戦、MCTS |
| OpenAI Five | Dota 2 | 対局棋譜という形では使わない | 使用 | Dota 2、5対5 |
| AlphaStar | StarCraft II | 人間のリプレイも利用 | 使用 | StarCraft II、RTS |

### AlphaGo

人間棋譜を使った教師あり学習を含み、その後に強化学習を行い、MCTSと組み合わせました。

### AlphaGo Zero

人間棋譜を使わず、囲碁のルールから自己対戦で学習しました。

### AlphaZero

AlphaGo Zeroの考え方を、囲碁だけでなく将棋・チェスにも適用したシステムです。

**「汎用AI」ではなく、複数のボードゲームに同じ基本アルゴリズムを適用した**と理解するのが安全です。

### OpenAI Five

Dota 2の5対5チーム戦を対象に、大規模な自己対戦による強化学習を行いました。

### AlphaStar

StarCraft IIを対象とし、不完全情報・リアルタイム・長期戦略を扱います。学習には自己対戦だけでなく、人間プレイヤーのリプレイも利用されています。

## いつ使う？（得意・不得意）

これらは一般-purposeのアルゴリズムを選ぶ問題というより、**著名AIシステムと対象ゲーム・特徴の対応**として覚えるのが実用的です。

## G検定ひっかけポイント

### よくある誤解

- ❌ AlphaZero＝汎用AI
- ❌ AlphaStarは人間データを一切使わない
- ❌ AlphaGo Zeroは将棋・チェスにも対応
- ❌ OpenAI Five＝StarCraft II

### 選択肢を切る判断基準

- 囲碁＋人間棋譜＋MCTS → **AlphaGo**
- 囲碁＋人間棋譜なし＋自己対戦 → **AlphaGo Zero**
- 囲碁・将棋・チェス → **AlphaZero**
- Dota 2＋5対5 → **OpenAI Five**
- StarCraft II＋RTS → **AlphaStar**

## まとめ（試験直前用）

- AlphaGo＝囲碁＋人間棋譜＋MCTS
- AlphaGo Zero＝囲碁＋自己対戦
- AlphaZero＝囲碁・将棋・チェス
- OpenAI Five＝Dota 2
- AlphaStar＝StarCraft II

{% include gk_article_footer.html %}
