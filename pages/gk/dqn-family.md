---
layout: page
title: DQN / Double DQN / Prioritized Replay / APE-X【強化学習の系譜まとめ】
permalink: /gk/dqn-family/
tags: [gk, neural_network, cheatsheet]
---

## まず結論
- **DQN → Double DQN → Prioritized Experience Replay → APE-X は、「安定性・効率・スケール」を段階的に改善してきた強化学習アルゴリズムの進化系譜**。
- G検定では **「何を解決するための改良か」**を対応づけられるかが問われる。

## 直感的な説明
- DQN：🎮 **とりあえず動くようにした**
- Double DQN：⚖ **評価の偏りを直した**
- Prioritized Replay：📚 **大事な経験を重点復習**
- APE-X：🌐 **それを分散環境で一気に回す**

人間で例えると：
- DQN：全部の問題を同じ頻度で復習
- Double DQN：自己採点の甘さを修正
- Prioritized Replay：間違えた問題を重点的に復習
- APE-X：クラス全員で問題を解いて、先生が重要部分を教える

## 定義・仕組み
### DQN（Deep Q-Network）
- Q学習 × ニューラルネットワーク
- 経験再生（Experience Replay）を導入
- 問題点：
  - **Q値の過大評価**

### Double DQN
- Q値の **選択と評価を分離**
- 目的：
  - **過大評価問題の緩和**
- 改善点は「評価の正確さ」

### Prioritized Experience Replay
- 経験を **一様に使わない**
- TD誤差が大きい経験を優先
- 改善点は「学習効率」

### APE-X
- **:contentReference[oaicite:1]{index=1} が提案**
- 特徴：
  - 分散 Actor による大量経験収集
  - Prioritized Experience Replay
  - オフポリシー学習
- 改善点は「スケーラビリティ」

## いつ使う？（得意・不得意）
**DQN 系全体の得意**
- ゲーム・シミュレーション
- 行動価値関数ベースの問題

**APE-X の強み**
- 大規模環境
- 並列計算が可能な場合

**注意点**
- 教師あり学習ではない
- Attention や時系列予測モデルではない

## G検定ひっかけポイント
- **改良点の対応づけを聞かれる**
- よくある混同：
  - ❌ Double DQN＝分散学習
  - ❌ APE-X＝Attention
- 正しい対応：
  - 過大評価 → **Double DQN**
  - 学習効率 → **Prioritized Replay**
  - 分散化 → **APE-X**
- 即断キーワード：
  - 「TD誤差」→ Prioritized
  - 「Actor / 分散」→ APE-X
  - 「評価分離」→ Double DQN

## まとめ（試験直前用）
- DQN：基礎
- Double DQN：過大評価対策
- Prioritized Replay：重要経験を優先
- APE-X：分散強化学習
- **「安定 → 効率 → スケール」の進化**
