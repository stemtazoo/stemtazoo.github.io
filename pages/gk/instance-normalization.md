---
layout: page
title: Instance Normalizationとは？画像ごと・チャネルごとに正規化【G検定】
description: "Instance Normalizationを、各サンプル・各チャネルごとに空間方向の平均と分散を使って正規化する手法として整理します。Batch Normalization・Layer Normalizationとの違い、バッチサイズ依存の有無、スタイル変換で使われる理由、G検定で統計量を取る単位から切る判断基準を確認します。"
permalink: /gk/instance-normalization/
tags: [gk, neural_network, cnn]
gk_section: ディープラーニングの要素技術/ネットワークの構成要素
gk_order: 9
last_modified_at: 2026-08-26
---

## まず結論

Instance Normalization（IN）は、**各サンプル・各チャネルごとに、空間方向の平均と分散を使って正規化する手法**です。

G検定では、

- バッチをまたぐ → Batch Normalization
- 1サンプル内の特徴全体 → Layer Normalization
- **1サンプル・1チャネルごと** → Instance Normalization

と切り分けます。

## 直感的な説明

INは、画像を1枚ずつ見て、さらにRGBなどのチャネルごとに明るさ・コントラストの基準を整えるイメージです。

他の画像の統計量を使わないため、**バッチサイズに依存しにくい**のが特徴です。

## 定義・仕組み

画像テンソルを考えると、INは各サンプル・各チャネルについて、主に高さ・幅の空間方向から平均と分散を計算します。

そのため、Batch Normalizationのようにバッチ内の別サンプルの値を使いません。

| 手法 | 統計量を取る主な単位 | バッチサイズ依存 |
|---|---|---|
| Batch Normalization | バッチ内の複数サンプルを含む | あり |
| Layer Normalization | 各サンプル内の特徴 | なし |
| Instance Normalization | 各サンプル・各チャネルの空間方向 | なし |

## いつ使う？（得意・不得意）

INは特に、**スタイル変換や画像生成**などでよく知られています。

画像ごとのコントラストやスタイルに関わる統計量を整えたい場合に向いています。

一方で、画像分類などすべてのCNNで常に有利とは限りません。用途だけで覚えるより、**どの単位で統計量を取るか**で判断する方が安全です。

## G検定ひっかけポイント

- ❌ 「バッチ全体の統計量を使う」→ BN
- ❌ 「各サンプルの全特徴をまとめる」→ LN
- ⭕ 「画像ごと・チャネルごと」→ IN
- ❌ 「特徴量間の相関をなくす」→ [白色化](/gk/whitening/)

また、INは入力画像を0〜1へ変換する前処理の正規化とは別物です。

## まとめ（試験直前用）

- IN＝**1サンプル・1チャネルごと**
- 空間方向の平均・分散を使う
- バッチ統計に依存しない
- スタイル変換・画像生成でよく使われる

[BN・LN・INの比較](/gk/normalization-cheatsheet/)もあわせて確認すると整理しやすいです。

{% include gk_article_footer.html %}
