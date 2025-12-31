---
layout: page
title: 強化学習の代表的手法まとめ（DQN・Policy Gradient・Actor-Critic）【G検定対策】
permalink: /gk/rl-methods/
tags: [gk, reinforcement_learning, cheatsheet]
---

## まず結論
- **DQN**：行動価値（Q値）を学習する手法  
- **Policy Gradient**：方策（行動確率）を直接学習する手法  
- **Actor-Critic**：価値と方策を同時に学習する手法  
- G検定では「**何を学習しているか**」で切るのが最短ルート。

## 直感的な説明
強化学習は、学び方が3パターンあります。

- DQN：  
  👉 「どの行動が得か？」を数値で覚える
- Policy Gradient：  
  👉 「どんな行動を取りやすくするか？」を直接覚える
- Actor-Critic：  
  👉 「両方いいとこ取り」

この違いを押さえるだけで、選択肢はかなり削れます。

## 定義・仕組み
### DQN（Deep Q-Network）
- 学習対象：**行動価値関数 Q(s, a)**
- ニューラルネットワークで Q値を近似
- 行動は「Q値が最大のもの」を選ぶ

#### 特徴
- 離散行動向き
- 実装が比較的わかりやすい
- 改良版：Double DQN / Dueling DQN など

---

### Policy Gradient
- 学習対象：**方策（ポリシー）そのもの**
- 行動の確率分布を直接更新
- 「良い行動をより選びやすく」する

#### 特徴
- 連続行動に強い
- 学習が不安定になりやすい
- Q値を使わない

---

### Actor-Critic
- Actor：方策を学習
- Critic：価値関数を学習
- Criticの評価を使ってActorを改善

#### 特徴
- Policy Gradientより安定
- DQNとPolicy Gradientの中間的存在
- 実用でよく使われる構成

## いつ使う？（得意・不得意）
### DQN
- 得意：離散行動、シンプルな環境
- 不得意：連続行動、高次元制御

### Policy Gradient
- 得意：連続行動、複雑な制御
- 不得意：学習の安定性

### Actor-Critic
- 得意：安定性と柔軟性の両立
- 不得意：構造がやや複雑

## G検定ひっかけポイント
ここは **用語の言い換え**に注意。

### よくあるひっかけ
- ❌ DQNは方策を直接学習する  
- ❌ Policy GradientはQ値を学習する  
- ❌ Actor-Criticはどちらか一方だけ

### 正しい切り方
- **Q値** → DQN
- **方策を直接更新** → Policy Gradient
- **Actor / Critic の2つ** → Actor-Critic

### キーワード対応
| 選択肢の表現 | 手法 |
|---|---|
| 行動価値関数 | DQN |
| 方策を直接学習 | Policy Gradient |
| 価値で方策を改善 | Actor-Critic |

## まとめ（試験直前用）
- DQN：**Q値を学習**
- Policy Gradient：**方策を直接学習**
- Actor-Critic：**価値＋方策**
- 連続行動 → DQNは不利
- 迷ったら「何を学習しているか」を見る
