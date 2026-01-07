---
layout: page
title: Permutation Importance vs SHAP【G検定頻出比較】
permalink: /gk/permutation-importance-vs-shap/
tags: [gk, metrics, cheatsheet]
---

## まず結論
- **Permutation Importance は「特徴量をシャッフルして性能低下を見る」手法**。
- **SHAP（SHapley Additive exPlanations）は「予測結果を各特徴量の貢献に分解する」手法**。
- G検定では **「何を評価しているか」**を区別できるかが問われる。

## 直感的な説明
- **Permutation Importance**
  - 特徴量を1つ壊す
  - モデルがどれだけ困るかを見る
  - 👉「この特徴がなくなると困る？」
- **SHAP（SHapley Additive exPlanations）**
  - 1つの予測を分解
  - どの特徴がどれだけ押し上げ／押し下げたかを見る
  - 👉「この予測は誰のせい？」

たとえ話：
- Permutation Importance：🧪 **部品を壊して性能テスト**
- SHAP：🧩 **結果を原因ごとに分解**

## 定義・仕組み
### Permutation Importance
- 学習済みモデルに対して使用
- 特徴量の値を **ランダムに並び替える**
- 性能低下量を重要度とする
- 特徴：
  - モデル非依存
  - グローバルな重要度評価

### SHAP（SHapley Additive exPlanations）
- **Shapley値（協力ゲーム理論）**が基礎
- 予測値を **各特徴量の寄与の和**として表現
- 特徴：
  - 個々の予測を説明可能
  - ローカル／グローバル両対応
  - 理論的に厳密

## いつ使う？（得意・不得意）
### Permutation Importance
**得意**
- モデル全体で重要な特徴量を知りたい
- 手軽に重要度を確認したい

**注意**
- 相関の強い特徴量があると誤解しやすい
- 個々の予測理由は分からない

### SHAP（SHapley Additive exPlanations）
**得意**
- なぜその予測になったかを説明したい
- 個別サンプルの説明（XAI）

**注意**
- 計算コストが高い
- 実装がやや複雑

## G検定ひっかけポイント
- **略語の意味を知らないと不安になるが、意味理解は必須ではない**
- よくある誤解：
  - ❌ SHAP は性能低下を見る手法
  - ❌ Permutation Importance は予測理由を説明できる
- 正しい判断基準：
  - 「シャッフル」「性能劣化」→ **Permutation Importance**
  - 「Shapley」「寄与の分解」→ **SHAP**
- 選択肢での即断ワード：
  - 「並び替え」→ Permutation Importance
  - 「Shapley値」→ SHAP
  - 「個々の予測」→ SHAP

## まとめ（試験直前用）
- Permutation Importance：**壊して測る**
- SHAP（SHapley Additive exPlanations）：**分解して説明する**
- グローバル重要度 → Permutation Importance
- 個別予測の理由 → SHAP
- **シャッフルか？ 分解か？で切る**
