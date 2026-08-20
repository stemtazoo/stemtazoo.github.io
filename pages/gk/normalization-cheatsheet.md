---
layout: page
title: BatchNorm・LayerNorm・InstanceNormの違い【G検定】
description: "Batch Normalization・Layer Normalization・Instance Normalizationを、どの軸・単位で平均と分散を計算するかで比較します。BNはバッチ統計、LNは各サンプル内の特徴、INは各サンプル・チャネルごとの空間方向という違いを整理し、G検定で選択肢を切る判断基準を確認します。"
permalink: /gk/normalization-cheatsheet/
tags: [gk, neural_network, cnn, cheatsheet]
gk_section: ディープラーニングの要素技術/ネットワークの構成要素
gk_order: 11
last_modified_at: 2026-08-21
---

## まず結論

Batch Normalization（BN）・Layer Normalization（LN）・Instance Normalization（IN）の違いは、**平均・分散をどの単位で計算するか**です。

G検定では、次の3点で切り分けます。

- **バッチ内の複数サンプルをまたぐ** → BN
- **1サンプル内の特徴をまとめる** → LN
- **1サンプル・1チャネルごとに空間方向を整える** → IN

## 直感的な説明

同じ「正規化」でも、**誰と比べて整えるか**が違います。

- BN：同じバッチの仲間も使って基準を作る
- LN：そのサンプル自身の特徴から基準を作る
- IN：その画像の各チャネルごとに基準を作る

ここでいう正規化は、入力値を0〜1へ変換するMin-Max正規化とは別文脈です。

## 定義・仕組み

| 手法 | 統計量を取る主な単位 | バッチサイズ依存 | よく使われる場面 |
|---|---|---|---|
| Batch Normalization | バッチ内の複数サンプルを含む単位 | あり | CNNなど |
| Layer Normalization | 各サンプル内の特徴 | なし | Transformerなど |
| Instance Normalization | 各サンプル・各チャネルの空間方向 | なし | スタイル変換など |

### Batch Normalization

学習時はミニバッチの統計量を使って正規化します。推論時は通常、学習中に蓄積した統計量を使います。

### Layer Normalization

サンプルごとに特徴方向を正規化するため、バッチサイズに依存しません。Transformerで広く使われます。

### Instance Normalization

画像ごと・チャネルごとに空間方向の平均・分散を使います。特にスタイル変換などで知られています。

## いつ使う？（得意・不得意）

- **BN**：十分なバッチサイズを確保できるCNNなどで使いやすい
- **LN**：バッチサイズに依存したくない場合やTransformerで使われる
- **IN**：画像ごとの見た目・スタイルに関わる統計量を整えたい場面で使われる

ただし、用途だけで断定せず、試験では**統計量を取る単位**を優先して判断します。

## G検定ひっかけポイント

- ❌ 「特徴量間の相関を除去する」→ これは[白色化](/gk/whitening/)の説明
- ❌ 「0〜1の範囲に変換する」→ 入力前処理としての[正規化](/gk/normalization/)の説明
- ⭕ 「ミニバッチの統計量」→ BN
- ⭕ 「各サンプル内の特徴」→ LN
- ⭕ 「画像ごと・チャネルごと」→ IN

**BN・LN・INを、前処理としてのNormalizationと同じものだと考えない**ことが重要です。

## まとめ（試験直前用）

- BN：**バッチ統計**
- LN：**1サンプル内の特徴**
- IN：**1サンプル・1チャネルごと**
- 迷ったら「平均・分散をどの単位で取る？」を見る

{% include gk_article_footer.html %}
