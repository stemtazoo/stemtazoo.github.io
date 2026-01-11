---
layout: page
title: AlphaGo・AlphaGo Zero・AlphaZero・OpenAI Five・AlphaStar 完全比較【G検定対策】
permalink: /gk/ai-project-comparison/
tags: [gk, reinforcement_learning, cheatsheet]
gk_section: ディープラーニングの応用例/深層強化学習
gk_order: 16
---

## まず結論
- これらはすべて **強化学習を用いたAI** だが、  
  **対象ゲーム・学習方法・汎用性が明確に異なる**。
- G検定では「**どのゲームか**」と「**人間知識を使ったか**」で切る。

## 直感的な整理（まずは一言）
- **AlphaGo**：人間知識あり囲碁AI  
- **AlphaGo Zero**：人間知識なし囲碁AI  
- **AlphaZero**：囲碁・将棋・チェス対応の汎用AI  
- **OpenAI Five**：Dota 2（5対5）専用AI  
- **AlphaStar**：StarCraft II 専用AI  

## 完全比較表（最重要）
| 項目 | AlphaGo | AlphaGo Zero | AlphaZero | OpenAI Five | AlphaStar |
|---|---|---|---|---|---|
| 開発元 | DeepMind | DeepMind | DeepMind | OpenAI | DeepMind |
| 対象ゲーム | 囲碁 | 囲碁 | 囲碁・将棋・チェス | Dota 2 | StarCraft II |
| 人間棋譜 | 使用する | 使用しない | 使用しない | 使用しない | 使用しない |
| 学習方法 | 強化学習＋教師あり | 強化学習（自己対戦） | 強化学習（自己対戦） | 強化学習（自己対戦） | 強化学習 |
| 汎用性 | 低い | 低い | 高い | 低い | 低い |
| 特徴 | 初の人間超え | 完全自己学習 | ルールだけで複数ゲーム | eスポーツAI | RTS対応AI |
| G検定の要点 | 人間知識あり | 人間知識なし | 将棋も可 | Dota 2専用 | StarCraft II |

## 各AIの要点整理
### AlphaGo
- 初めて人間トップ棋士に勝利した囲碁AI
- **人間棋譜（教師データ）を使用**
- 強化学習＋教師あり学習の組み合わせ

### AlphaGo Zero
- **人間棋譜を一切使わない**
- ルールだけを与えて自己対戦で学習
- AlphaGoを上回る性能

### AlphaZero
- AlphaGo Zeroを一般化
- **同一アルゴリズムで囲碁・将棋・チェスを制覇**
- 真の意味での「汎用ゲームAI」

### OpenAI Five
- **Dota 2（5対5・不完全情報・リアルタイム）専用**
- eスポーツ分野の代表例
- 将棋・囲碁には使えない

### AlphaStar
- **StarCraft II 専用AI**
- リアルタイム戦略ゲーム（RTS）
- 不完全情報・長期戦略に対応

## G検定ひっかけポイント
### よくある混同
- ❌「OpenAI Fiveは将棋もできる」
- ❌「AlphaGo Zeroは将棋対応」
- ❌「AlphaStarはDota 2」
- ❌「全部汎用AI」

### 正しい即断ルール
- **囲碁＋人間棋譜 → AlphaGo**
- **囲碁＋自己対戦 → AlphaGo Zero**
- **囲碁・将棋・チェス → AlphaZero**
- **Dota 2 → OpenAI Five**
- **StarCraft II → AlphaStar**

## まとめ（試験直前用）
- 全部強化学習ベース
- 違いは「ゲーム」と「人間知識」
- 汎用なのは AlphaZero だけ
- eスポーツ系は専用AI
- ゲーム名で即切る
