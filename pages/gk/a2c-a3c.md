---
layout: page
title: A2C / A3C とは？（Actor–Critic の実装差）【G検定対策】
description: A2CとA3CをActor-Critic系強化学習の実装差として整理します。同期・非同期の違い、方策と価値関数の役割、G検定での比較ポイントを確認できます。
permalink: /gk/a2c-a3c/
tags: [gk, reinforcement_learning, neural_network]
gk_section: 機械学習の概要/代表的な手法/強化学習/方策勾配・Actor-Critic
gk_order: 4
last_modified_at: 2026-08-26
---

## まず結論
- **A2C と A3C は、Actor–Critic をベースにした代表的なオンポリシー強化学習アルゴリズム**です。
- 最大の違いは、**A2Cは同期型、A3Cは非同期型**で学習を進める点です。

## 直感的な説明
- **A3C**：複数のワーカーがそれぞれ進み、更新を非同期に共有する
- **A2C**：複数環境で経験を集め、足並みをそろえて同期的に更新する

どちらも、
- Actor が方策を学ぶ
- Critic が価値を推定する
- Advantage を使って方策更新を助ける

というActor-Critic系の考え方を使います。

## 定義・仕組み
### 共通点
- Actor–Critic 構造
- 代表的にはオンポリシー
- Advantageを利用して方策勾配を更新

### A3C（Asynchronous Advantage Actor–Critic）
- 複数のワーカーが独立して環境と相互作用
- 各ワーカーが非同期に共有パラメータを更新
- 非同期処理によって経験の相関を弱める狙いがある

### A2C（Advantage Actor–Critic）
- A3Cの同期型に近い実装
- 複数環境から経験を集め、まとめて同期的に更新
- バッチ化しやすい

## いつ使う？（得意・不得意）
### A3C
- 非同期に複数ワーカーを動かしたい場合
- 分散的に経験を集めたい場合

### A2C
- 同期更新で実装を整理したい場合
- 複数環境の経験をまとめて計算したい場合

性能や計算効率は実装・環境に依存するため、**「A2Cは必ずGPU向き」「A3Cは必ず探索性能が高い」**のような断定は避けます。

## G検定ひっかけポイント
- ❌ A3C はオフポリシーだから非同期である
- ❌ A2C は DQN 系である
- ❌ A2C と A3C の違いは Actor と Critic の有無

### 判断基準
- 「非同期」→ A3C
- 「同期」→ A2C
- 「Actor＋Critic＋Advantage」→ A2C / A3C

## まとめ（試験直前用）
- A2C / A3C は Actor-Critic 系
- 代表的にはオンポリシー
- A3C：非同期
- A2C：同期
- **違いは主に更新・並列化の方式**

{% include gk_article_footer.html %}
