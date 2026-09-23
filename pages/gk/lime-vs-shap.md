---
layout: page
title: LIMEとSHAPの違い｜局所近似とShapley値【G検定対策】
description: "LIMEとSHAPを、LIMEは説明対象の周辺を単純モデルで局所近似し、SHAPはShapley値を基礎に特徴量寄与を表す手法群として比較します。SHAPが常に厳密・低速、LIMEが常に高速という固定順位を避け、仕組みで選択肢を切ります。"
permalink: /gk/lime-vs-shap/
tags: [gk, xai, cheatsheet]
gk_section: ディープラーニングの応用例/モデルの解釈性/比較・使い分け
gk_order: 1
last_modified_at: 2026-09-24
---

## まず結論

- **LIME**：説明したい入力の周辺を、解釈しやすい単純モデルで**局所近似**
- **SHAP**：ゲーム理論の**Shapley値**を基礎に、特徴量の寄与を表す

G検定では、

> 局所近似 → LIME  
> Shapley値 → SHAP

で切ります。

## 直感的な説明

### LIME

「この1件の近くだけなら、単純なモデルでどう説明できるか？」を見ます。

### SHAP

「基準となる予測から、この特徴がどれくらい押し上げ・押し下げたか？」を寄与として表します。

## 定義・仕組み

### LIME

説明対象の周辺に摂動データを作り、元モデルの出力を取得し、その近傍で線形モデルなどの単純な代理モデルを学習します。

そのため、

- モデル非依存
- 局所説明
- 近似方法やサンプリングに依存

という特徴があります。

### SHAP

Shapley値を基礎に、予測と基準値の差を特徴量寄与へ分解する枠組みです。

ただしSHAPには複数の計算方法があり、

- 厳密計算
- 近似計算
- 特定モデル向け高速アルゴリズム

などがあります。

したがって、

> SHAPは常に厳密計算  
> SHAPは常にLIMEより遅い

とは言えません。

## いつ使う？（得意・不得意）

LIMEは個別予測を局所的に説明したい場合に使われます。

SHAPは個別予測の寄与説明に加え、複数サンプルのSHAP値を集約して全体傾向を見ることもできます。

どちらも、説明結果が因果関係を証明するわけではありません。

## G検定ひっかけポイント

### LIME

❌ Shapley値を使う  
⭕ **局所代理モデルで近似**

### SHAP

❌ 性能低下量を測るだけ  
⭕ **Shapley値に基づく特徴量寄与**

### 速度

❌ LIMEは必ず速くSHAPは必ず遅い  
⭕ **実装・モデル・近似方法による**

## まとめ（試験直前用）

- LIME＝**局所近似**
- SHAP＝**Shapley値**
- SHAPは局所説明にも全体傾向にも使える
- SHAPには厳密・近似など複数方式がある
- 速度や精度を固定順位で覚えない

## 参考資料

- [Why Should I Trust You?｜arXiv](https://arxiv.org/abs/1602.04938)
- [A Unified Approach to Interpreting Model Predictions｜arXiv](https://arxiv.org/abs/1705.07874)

{% include gk_article_footer.html %}
