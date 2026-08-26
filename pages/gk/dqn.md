---
layout: page
title: DQN（Deep Q-Network）とは？Experience ReplayとTarget Network【G検定対策】
description: "DQNを、Q学習のQ値をニューラルネットワークで近似する深層強化学習手法として整理します。Experience ReplayとTarget Networkが学習を安定させる役割、基本DQNが離散行動を扱う点、Double DQNなどの改良手法との違いをG検定向けに確認します。"
permalink: /gk/dqn/
tags: [gk, reinforcement_learning, neural_network]
gk_section: ディープラーニングの応用例/深層強化学習/DQN・改良手法
gk_order: 1
last_modified_at: 2026-08-26
---

## まず結論

- **DQN（Deep Q-Network）**は、Q学習の**行動価値関数 Q(s, a) をニューラルネットワークで近似**する深層強化学習手法です。
- 代表的な安定化の工夫は、**Experience Replay（経験再生）**と**Target Network**です。
- G検定では「**Q学習＋ニューラルネットワーク**」「**経験再生**」「**Target Network**」をDQNと結び付けられることが重要です。

## 直感的な説明

DQNでは、過去の経験をその場限りで捨てません。

- 経験をいったん保存する
- 保存した経験をランダムに取り出して学習する
- 更新対象とは別のネットワークを使って、学習目標が急に動きすぎないようにする

という工夫を使います。

イメージとしては、

- **Experience Replay**：過去問をシャッフルして復習する
- **Target Network**：採点基準を毎回すぐ書き換えず、少し固定して使う

と考えると整理しやすいです。

## 定義・仕組み

### Q学習＋ニューラルネットワーク

通常のQ学習では、状態と行動ごとのQ値を表として持つことがあります。

DQNでは状態空間が大きい問題に対応するため、**ニューラルネットワークでQ値を近似**します。

### Experience Replay

経験として、たとえば

- 状態
- 行動
- 報酬
- 次状態

をReplay Bufferへ保存し、そこからミニバッチを取り出して学習します。

連続した経験をそのまま順番に学び続けるより、データ間の強い相関を弱めやすくなります。

### Target Network

DQNでは、更新中のネットワークだけを使って学習目標まで毎回大きく動かすと、学習が不安定になりやすくなります。

そこで、**一定期間パラメータを固定したTarget Network**を学習目標の計算に使い、周期的に更新します。

試験では、

> **Experience Replay＝経験の再利用**  
> **Target Network＝学習目標を安定させる**

と役割を分けて覚えるのが有効です。

## いつ使う？（得意・不得意）

### 得意

- 状態数が多く、Qテーブルで扱いにくい問題
- Atariなどのゲーム環境
- **離散的な行動**を選ぶ問題

### 注意点

- 基本のDQNは連続行動をそのまま扱う代表手法ではない
- Experience ReplayだけがDQNの特徴ではなく、Target Networkも重要
- DQNは価値ベース手法であり、方策を直接最適化する方策勾配法とは異なる

## G検定ひっかけポイント

### Experience ReplayとTarget Network

- 「過去の経験を保存して再利用」→ **Experience Replay**
- 「学習目標を計算する別ネットワーク」→ **Target Network**

### DQNと改良手法

- Q値の過大評価を緩和 → **Double DQN**
- 状態価値とアドバンテージを分ける → **Dueling Network**
- パラメータへノイズを加えて探索 → **Noisy Nets**
- 複数のDQN改良を統合 → **Rainbow**

### 選択肢を切る判断基準

- 「Q学習＋ニューラルネットワーク」→ DQN
- 「経験再生」→ DQNの代表的要素
- 「Target Network」→ DQNの代表的要素
- 「方策を直接更新」→ 方策勾配系を疑う

関連： [DQN改良手法まとめ](/gk/dqn-advanced/) / [Dueling Network](/gk/dueling-network/) / [Rainbow](/gk/rainbow/)

## まとめ（試験直前用）

- DQN＝**Q学習＋ニューラルネットワーク**
- Experience Replay＝**経験を保存・再利用**
- Target Network＝**学習目標を安定化**
- 基本DQNは主に**離散行動**向け
- 改良手法は「何を改善するか」で切り分ける

{% include gk_article_footer.html %}
