---
layout: page
title: DQN改良手法まとめ（Double / Dueling / Noisy / Prioritized）【G検定対策】
permalink: /gk/dqn-advanced/
tags: [gk]
---

## まず結論

DQNの改良手法はそれぞれ**解決したい「弱点」が異なる**。G検定では「どの問題に対する改良か」を正確に対応づけられるかが問われる。

* **Double DQN**：Q値の過大評価を抑制
* **Dueling Network**：状態価値と行動価値を分離
* **Noisy Network**：探索（ε-greedy）の問題を解消
* **Prioritized Experience Replay**：重要な経験を重点的に学習

## 直感的な説明

DQNは優秀だが、実運用ではいくつかの欠点がある。

* 期待値を盛りすぎる（過大評価）
* 行動より「状態そのもの」が重要な場面がある
* 探索率 ε の調整が難しい
* 重要な経験とそうでない経験を同じ重みで学習してしまう

それぞれの改良手法は、**これらの欠点を1つずつ潰すために生まれた**。

## 定義・仕組み（4手法の役割分担）

| 手法                 | 解決する問題  | 仕組みの要点            |
| ------------------ | ------- | ----------------- |
| Double DQN         | Q値の過大評価 | 行動選択と評価を分離        |
| Dueling Network    | 状態の重要度  | V(s) と A(s,a) を分離 |
| Noisy Network      | 探索の制御   | ネットワークにノイズ        |
| Prioritized Replay | 学習効率    | TD誤差が大きい経験を優先     |

## いつ使う？（得意・不得意）

### Double DQN

* 学習が不安定なとき
* Q値が過大評価されやすい環境

### Dueling Network

* 行動差が小さい環境
* 状態の良し悪しが重要な問題

### Noisy Network

* ε の調整が難しい場合
* 長期探索が必要なタスク

### Prioritized Experience Replay

* データが多い場合
* 学習を効率化したい場合

## G検定ひっかけポイント

G検定では、**「探索」と「Q値評価」を混同させる選択肢**が頻出。

### よくある誤解

* Double DQNは探索手法 → ✕
* Noisy NetworkはQ値補正 → ✕

### 正誤を切る判断基準

* **過大評価？** → Double DQN
* **探索方法？** → Noisy Network
* **状態価値の分離？** → Dueling Network
* **重要経験を優先？** → Prioritized Replay

## まとめ（試験直前用）

* Double：過大評価対策
* Dueling：価値の分離
* Noisy：探索改善
* Prioritized：経験の重み付け
* G検定は「何の問題を解決？」で切る
