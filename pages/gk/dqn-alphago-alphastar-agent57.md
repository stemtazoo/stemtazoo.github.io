---
layout: page
title: DQN / AlphaGo / AlphaStar / Agent57【強化学習の系譜まとめ】
permalink: /gk/dqn-alphago-alphastar-agent57/
tags: [gk, neural_network, cheatsheet]
gk_section: ディープラーニングの応用例/深層強化学習
gk_order: 11
---

## まず結論
- **DQN → AlphaGo → AlphaStar → Agent57 は、強化学習が「単一タスク攻略」から「複雑環境対応」「汎用性」へ進化した流れ**。
- G検定では **「どのゲーム・環境を解いたモデルか」**で正しく切り分けられるかが問われる。

## 直感的な説明
- DQN：🎮 **1つのゲームを覚える**
- AlphaGo：♟ **囲碁という超難問を極める**
- AlphaStar：🛰 **状況が刻々と変わる対戦ゲームを戦う**
- Agent57：🕹 **ゲームが変わっても対応できる**

人間で例えると：
- DQN：特定ゲーム職人  
- AlphaGo：囲碁の天才  
- AlphaStar：eスポーツのプロ選手  
- Agent57：万能ゲーマー  

## 定義・仕組み
### DQN（Deep Q-Network）
- **:contentReference[oaicite:1]{index=1} が開発**
- Q学習 × ニューラルネットワーク
- Atariゲームで人間レベル達成
- 特徴：
  - Q値を学習
  - **単一タスク向け**

### AlphaGo
- 囲碁専用の強化学習システム
- 特徴：
  - 方策ネットワーク（Policy）
  - 価値ネットワーク（Value）
  - モンテカルロ木探索（MCTS）
- 人間トップ棋士に勝利
- **完全情報ゲーム・特化型**

### AlphaStar
- **:contentReference[oaicite:2]{index=2} 用の強化学習エージェント**
- 特徴：
  - 不完全情報（視界制限）
  - リアルタイム戦略（RTS）
  - マルチエージェント的要素
- 人間トッププレイヤーに勝利
- **複雑・動的環境への対応が進化点**

### Agent57
- Atari **57種類すべて**で人間平均超え
- 特徴：
  - 複数ポリシーの切り替え
  - エピソディックメモリ
  - 探索と活用の自動調整
- **汎用強化学習エージェント**

## いつ使う？（得意・不得意）
**DQN**
- 得意：単純なゲーム環境
- 注意：タスク変更に弱い

**AlphaGo**
- 得意：囲碁・将棋など完全情報ゲーム
- 注意：他分野に汎用化しにくい

**AlphaStar**
- 得意：不完全情報・リアルタイム環境
- 注意：特定ゲーム依存

**Agent57**
- 得意：複数タスク・未知環境
- 注意：計算資源が大きい

## G検定ひっかけポイント
- **ゲーム名とモデル名の対応が頻出**
- よくある誤解：
  - ❌ AlphaStar は囲碁
  - ❌ AlphaGo は汎用AI
  - ❌ Agent57 は言語モデル
- 正しい対応関係：
  - Atari + Q学習 → **DQN**
  - 囲碁 + MCTS → **AlphaGo**
  - RTS + 不完全情報 → **AlphaStar**
  - Atari57種 + 汎用 → **Agent57**
- 選択肢の切り方：
  - 「囲碁」「棋士」→ AlphaGo
  - 「StarCraft」「リアルタイム」→ AlphaStar
  - 「57種類すべて」→ Agent57

## まとめ（試験直前用）
- DQN：深層強化学習の出発点
- AlphaGo：完全情報ゲームで人間超え
- AlphaStar：不完全情報・リアルタイム対応
- Agent57：**複数タスクで人間超え**
- 進化軸は **環境の複雑さ → 汎用性**
