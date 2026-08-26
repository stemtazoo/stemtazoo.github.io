---
layout: page
title: DQN改良手法まとめ（Double / Dueling / Noisy / Prioritized）【G検定対策】
description: "DQNの代表的な改良手法を、何の弱点を改善するかで整理します。Double DQNはQ値の過大評価、Dueling Networkは価値表現、Noisy Netsは探索、Prioritized Experience Replayは経験の選び方を改善するという役割分担をG検定向けに確認します。"
permalink: /gk/dqn-advanced/
tags: [gk, reinforcement_learning, cheatsheet]
gk_section: ディープラーニングの応用例/深層強化学習/DQN・改良手法
gk_order: 3
last_modified_at: 2026-08-26
---

## まず結論

DQNの改良手法は、**同じDQN系でも改善する弱点が異なります**。

G検定では、手法名を暗記するより、

- **過大評価** → Double DQN
- **価値の分解** → Dueling Network
- **探索** → Noisy Nets
- **重要な経験を優先** → Prioritized Experience Replay

と対応づけると選択肢を切りやすくなります。

## 直感的な説明

DQNには、学習を進める中で別々の課題があります。

- Q値を高く見積もりすぎることがある
- どの行動でも大差ない状態では、状態そのものの価値を学びたい
- 探索方法をどう設計するか決める必要がある
- すべての経験を同じように再学習するのは効率的とは限らない

それぞれの改良手法は、**同じ問題を別の方法で解くのではなく、違う弱点を担当する**と考えると整理しやすいです。

## 定義・仕組み

| 手法 | 主に改善する点 | 仕組みの要点 |
|---|---|---|
| Double DQN | Q値の過大評価 | 行動選択と評価を分ける |
| Dueling Network | 価値表現 | V(s) と A(s,a) を分けて推定 |
| Noisy Nets | 探索 | 重み・バイアスへ学習可能なノイズを加える |
| Prioritized Experience Replay | 経験の選び方 | TD誤差などを使って重要な経験を優先 |

### Double DQN

通常のDQNで起こり得る**Q値の過大評価**を緩和します。

「最大の行動を選ぶ処理」と「その行動を評価する処理」を分ける点が判断基準です。

### Dueling Network

Q値を直接1本で出すのではなく、

- 状態価値 V(s)
- アドバンテージ A(s,a)

に分けて推定し、Q値を構成します。

### Noisy Nets

ニューラルネットワークの**パラメータに学習可能なノイズ**を加え、探索を促します。

ε-greedyを必ず「解消する」と考えるのではなく、**明示的なε-greedyへの依存を減らせる探索手法**として整理するのが安全です。

### Prioritized Experience Replay

Replay Bufferの経験をすべて同じ確率で選ぶのではなく、**学習上重要だと考えられる経験を優先して再生**します。

## いつ使う？（得意・不得意）

### Double DQN

- Q値の過大評価を抑えたい
- DQNの価値推定を改善したい

### Dueling Network

- 行動差が小さい状態でも、状態そのものの価値を効率よく表現したい

### Noisy Nets

- 探索のランダム性をネットワーク内部へ組み込みたい

### Prioritized Experience Replay

- 学習効果の高い経験を重点的に再利用したい

これらは排他的ではありません。**Rainbowのように複数の改良を組み合わせる手法**もあります。

## G検定ひっかけポイント

### よくある誤解

- ❌ Double DQN＝分散学習
- ❌ Dueling Network＝Q値の過大評価を直接抑える手法
- ❌ Noisy Nets＝入力データへノイズを加えるデータ拡張
- ❌ Prioritized Replay＝探索手法

### 正誤を切る判断基準

- 「選択と評価を分ける」→ **Double DQN**
- 「V(s) と A(s,a)」→ **Dueling Network**
- 「重み・バイアスにノイズ」→ **Noisy Nets**
- 「TD誤差が大きい経験を優先」→ **Prioritized Experience Replay**
- 「複数のDQN改良を統合」→ **Rainbow**

関連： [DQN](/gk/dqn/) / [Dueling Network](/gk/dueling-network/) / [Noisy Nets](/gk/noisy-nets/) / [Rainbow](/gk/rainbow/)

## まとめ（試験直前用）

- Double DQN＝**過大評価対策**
- Dueling Network＝**価値表現を分ける**
- Noisy Nets＝**探索を改善**
- Prioritized Replay＝**重要経験を優先**
- 「何の弱点を改善？」で選択肢を切る

{% include gk_article_footer.html %}
