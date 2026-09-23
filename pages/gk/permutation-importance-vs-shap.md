---
layout: page
title: Permutation ImportanceとSHAPの違い【G検定対策】
description: "Permutation ImportanceとSHAPを、特徴量を並び替えたときのモデル性能低下を見る手法と、Shapley値に基づいて個々の予測を特徴量寄与へ分解する手法として比較します。相関特徴量への注意と、グローバル・ローカルの違いを整理します。"
permalink: /gk/permutation-importance-vs-shap/
tags: [gk, xai, cheatsheet]
gk_section: ディープラーニングの応用例/モデルの解釈性/比較・使い分け
gk_order: 2
last_modified_at: 2026-09-24
---

## まず結論

- **Permutation Importance**：特徴量をシャッフルし、**モデル性能がどれだけ低下するか**を見る
- **SHAP**：予測を**特徴量ごとの寄与**へ分解する

G検定では、

> シャッフル＋性能低下 → Permutation Importance  
> Shapley値＋寄与 → SHAP

で切ります。

## 直感的な説明

Permutation Importanceは、

> この特徴を壊したら、モデルはどれくらい困る？

を見る方法です。

SHAPは、

> この予測値を作るのに、各特徴がどれくらい寄与した？

を見る方法です。

## 定義・仕組み

### Permutation Importance

学習済みモデルに対し、ある特徴量だけをランダムに並び替え、評価指標がどれだけ悪化するかを測ります。

モデル内部構造に依存しない方法です。

一般には検証データなどでモデル全体の重要度を見る用途に使われます。

### SHAP

Shapley値を基礎に、ある予測と基準値との差を特徴量寄与として表します。

個別予測を説明でき、複数サンプルを集約して全体傾向を見ることもできます。

## いつ使う？（得意・不得意）

### 相関特徴量に注意

Permutation Importanceでは、強く相関した特徴量があると、一方をシャッフルしても他方が情報を補い、重要度が低く見えることがあります。

SHAPも、特徴量依存関係の扱い方によって解釈が変わる場合があります。

したがって、

> 数値が出たらそのまま因果的重要度

とは考えません。

## G検定ひっかけポイント

### Permutation Importance

❌ 特徴量を学習データから削除して再学習するのが必須  
⭕ **学習済みモデルで特徴量を並び替え、性能変化を見る**

### SHAP

❌ モデル性能の低下量そのもの  
⭕ **予測の特徴量寄与**

### 因果

❌ 重要度が高い＝因果原因  
⭕ **予測への依存・寄与と因果は別**

## まとめ（試験直前用）

- Permutation＝**シャッフル→性能低下**
- SHAP＝**Shapley値→寄与**
- Permutationは全体重要度を見る用途が代表的
- SHAPは個別説明＋集約が可能
- 相関特徴量に注意
- 重要度と因果を混同しない

{% include gk_article_footer.html %}
