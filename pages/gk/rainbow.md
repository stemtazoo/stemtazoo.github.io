---
layout: page
title: Rainbow（強化学習アルゴリズム）とは？【G検定対策】
description: "Rainbowを、DQNに複数の改良手法を統合した価値ベースの深層強化学習として整理します。Double DQN、Dueling Network、Prioritized Experience Replay、Noisy Nets、Distributional RL、Multi-step Learningの役割と、方策勾配法との違いを確認します。"
permalink: /gk/rainbow/
tags: [gk, reinforcement_learning]
gk_section: ディープラーニングの応用例/深層強化学習
gk_order: 19
last_modified_at: 2026-08-22
---

## まず結論

- **Rainbow**は、DQNに複数の改良手法を組み合わせた**価値ベースの深層強化学習アルゴリズム**です。
- 1つの新しい仕組みではなく、**異なる弱点を改善する複数の工夫を統合した手法**です。
- G検定では、**各構成要素が何を改善するか**を切り分けるのが重要です。

## 直感的な説明

Rainbowは、DQNに対して、

- Q値の過大評価を抑える
- 重要な経験を優先して学ぶ
- 状態の良さと行動の良さを分ける
- 探索しやすくする
- 将来リターンを期待値だけでなく分布として捉える
- 数ステップ先までの報酬を学習へ使う

という改良をまとめたものです。

よく「DQN改良の全部盛り」と説明されますが、試験では**それぞれの役割が違う**ことを押さえる方が大切です。

## 定義・仕組み

Rainbowは、DQNを土台に次の6つの代表的な改良を統合します。

| 構成要素 | 主に改善する点 | 判断キーワード |
|---|---|---|
| Double DQN | Q値の過大評価 | 選択と評価を分ける |
| Prioritized Experience Replay | 経験の選び方 | 重要な経験を優先 |
| Dueling Network | 価値表現 | V(s) と A(s,a) を分ける |
| Noisy Nets | 探索 | パラメータにノイズ |
| Distributional RL | 価値の表現 | リターンの分布を学ぶ |
| Multi-step Learning | 学習目標 | n-stepの報酬を利用 |

### 価値ベース手法である

Rainbowの中心はDQNです。

そのため、

- **Q値を学ぶ価値ベース手法**
- 方策そのものを直接更新するREINFORCEなどとは異なる

と整理します。

### 各構成要素は同じ役割ではない

たとえば、

- Double DQN → **過大評価の緩和**
- Dueling Network → **価値表現の分解**
- Noisy Nets → **探索**
- Prioritized Experience Replay → **再学習する経験の選び方**

です。

## いつ使う？（得意・不得意）

### 得意

- Atariなどのゲーム環境
- 離散的な行動を選ぶ問題
- DQN系の性能や学習効率を高めたい場合

### 注意点

- 基本的には離散行動を扱うDQN系の手法
- 構成要素が多く、実装や調整が複雑
- すべての問題で各改良が同じ程度に有効とは限らない
- 方策勾配法を統合したアルゴリズムではない

## G検定ひっかけポイント

### 近い手法との違い

| 手法 | 分類 | 主な特徴 |
|---|---|---|
| DQN | 価値ベース | Q値をニューラルネットワークで近似 |
| Rainbow | 価値ベース | DQNの複数改良を統合 |
| REINFORCE | 方策勾配 | 方策を直接更新 |
| Actor-Critic | 方策＋価値 | ActorとCriticを使う |

### よくある誤解

- ❌ Rainbow＝Double DQNの別名
- ❌ Rainbow＝方策勾配法
- ❌ Rainbow＝環境モデルを学習して計画する手法
- ❌ Rainbow＝連続行動向けの代表手法

### 選択肢を切る判断基準

- 「**DQNの複数改良を統合**」→ Rainbow
- 「**Q値の過大評価**」→ Double DQN
- 「**V(s) と A(s,a)**」→ Dueling Network
- 「**重要な経験を優先**」→ Prioritized Experience Replay
- 「**パラメータにノイズ**」→ Noisy Nets
- 「**リターン分布**」→ Distributional RL
- 「**方策を直接更新**」→ Rainbowではなく方策勾配系

関連： [DQN](/gk/dqn/) / [DQN改良手法まとめ](/gk/dqn-advanced/) / [Noisy Nets](/gk/noisy-nets/) / [Dueling Network](/gk/dueling-network/)

## まとめ（試験直前用）

- Rainbow＝**DQNの複数改良を統合**
- 価値ベースの深層強化学習
- 各構成要素は**別の弱点を改善**
- 方策を直接更新する手法ではない
- 「DQN改良の統合」が見えたらRainbow

{% include gk_article_footer.html %}
