---
layout: page
title: DQN・AlphaGo・AlphaStar・Agent57の違い【G検定対策】
description: "DQN、AlphaGo、AlphaStar、Agent57を、対象環境と技術的な役割で比較します。DQNは価値ベース深層強化学習、AlphaGoは囲碁とMCTS、AlphaStarはStarCraft II、Agent57はAtari 57ゲームでの探索強化という違いをG検定の判断軸として整理します。"
permalink: /gk/dqn-alphago-alphastar-agent57/
tags: [gk, reinforcement_learning, cheatsheet]
gk_section: ディープラーニングの応用例/深層強化学習/代表エージェント・プロジェクト
gk_order: 4
last_modified_at: 2026-08-26
---

## まず結論

DQN・AlphaGo・AlphaStar・Agent57は、すべて深層学習と強化学習に関係しますが、**単純な一直線の進化系譜として覚えない**ことが重要です。

G検定では、

- **DQN** → Q学習＋ニューラルネットワーク
- **AlphaGo** → 囲碁＋MCTS＋方策/価値ネットワーク
- **AlphaStar** → StarCraft II＋複雑なリアルタイム対戦
- **Agent57** → Atari 57ゲーム＋探索強化

と、**対象環境と代表キーワード**で切り分けます。

## 直感的な説明

4つは「何を得意とするか」が違います。

- DQN：**Q値をニューラルネットワークで学ぶ基本手法**
- AlphaGo：**囲碁で探索と学習を組み合わせたシステム**
- AlphaStar：**不完全情報を含むリアルタイム戦略ゲームへ対応したエージェント**
- Agent57：**多数のAtariゲームで探索方法を使い分けるエージェント**

「新しいほど何でもできる」と考えるのではなく、**解いた問題と使った仕組みを見る**のが安全です。

## 定義・仕組み

### DQN

- Q学習のQ値をニューラルネットワークで近似
- Experience ReplayやTarget Networkを使う
- 価値ベースの深層強化学習

DQNそのものが「1つのゲーム専用」という意味ではありません。代表的な実験として複数のAtariゲームで評価されましたが、**1つの学習済みモデルが57ゲームすべてを同時に攻略するAgent57とは位置づけが異なる**と整理します。

### AlphaGo

- 対象：**囲碁**
- 方策ネットワーク
- 価値ネットワーク
- **モンテカルロ木探索（MCTS）**

初期のAlphaGoでは人間の棋譜を使った教師あり学習も取り入れ、その後に自己対戦による強化学習を行いました。

### AlphaStar

- 対象：**StarCraft II**
- リアルタイム戦略ゲーム
- 不完全情報
- 多数の対戦相手を使うリーグ学習などを活用

「囲碁」「MCTS」が中心のAlphaGoとは、対象環境も学習構成も異なります。

### Agent57

- 対象：**Atari 57ゲーム**
- 内発的報酬で探索を強化
- 探索の強さなどが異なる複数方策を使い分ける
- メタコントローラで方策を選択

Agent57は「汎用AI」やAGIを意味するものではありません。**Atari 57ゲームという同一ベンチマーク群で幅広く高い性能を示したエージェント**と理解します。

## いつ使う？（得意・不得意）

### DQN

- 離散行動の価値ベース強化学習
- Atariなどのゲーム環境

### AlphaGo

- 囲碁のような完全情報のボードゲーム
- 学習と木探索を組み合わせる問題

### AlphaStar

- StarCraft IIのような複雑なリアルタイム対戦環境

### Agent57

- 探索の難しさがゲームごとに異なるAtariベンチマーク
- 複数の探索設定を使い分けたい問題

## G検定ひっかけポイント

### ゲーム名で切る

- 「Atari＋Q値」→ **DQN**
- 「囲碁＋MCTS」→ **AlphaGo**
- 「StarCraft II」→ **AlphaStar**
- 「Atari 57ゲームすべて」→ **Agent57**

### よくある誤解

- ❌ DQN＝単一タスクしか扱えないアルゴリズム
- ❌ AlphaGo＝汎用AI
- ❌ AlphaStar＝囲碁AI
- ❌ Agent57＝AGI

### 判断基準

まず**対象ゲーム**を確認し、その次に**価値学習・木探索・探索強化**のどれが中心かを見ると切り分けやすくなります。

関連： [DQN](/gk/dqn/) / [Agent57](/gk/agent57/) / [AlphaGoとAlphaStarの比較](/gk/alphago-vs-alphastar/)

## まとめ（試験直前用）

- DQN＝**Q学習＋NN**
- AlphaGo＝**囲碁＋MCTS**
- AlphaStar＝**StarCraft II**
- Agent57＝**Atari 57＋探索強化**
- 「一直線の進化」ではなく**対象環境と役割で切る**

{% include gk_article_footer.html %}
