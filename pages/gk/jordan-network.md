---
layout: page
title: Jordan Networkとは？出力側の情報を状態へ戻すRNN【G検定対策】
description: "Jordan Networkを、前時刻の出力側情報をState Unitへ戻し、その状態を次時刻の隠れ層計算へ使う初期RNNとして整理します。隠れ層をContext UnitへコピーするElman Networkとの違いを、outputとhiddenという判断軸で確認します。"
permalink: /gk/jordan-network/
tags: [gk, neural_network, rnn]
gk_section: ディープラーニングの要素技術/リカレントニューラルネットワーク (RNN)
gk_order: 12
last_modified_at: 2026-09-23
---

## まず結論

**Jordan Network**は、前時刻の**出力側の情報をState Unitへ戻し、その状態を次時刻の隠れ層計算へ使う**初期RNNです。

G検定では、

- output → state → **Jordan**
- hidden → context → **Elman**

で切り分けます。

## 直感的な説明

Jordan Networkは、

> **前回どんな出力をしたかを手掛かりに、次の内部状態を作る**

イメージです。

単純に出力値を入力層へそのまま戻すだけではなく、**状態ユニットを介して系列文脈を保持する**点を押さえます。

## 定義・仕組み

JordanのSequential Networkでは、出力パターンをState Unitへコピーし、次時刻の処理で利用します。

また原典では、State Unit自身の前状態も次状態へ影響します。

したがってG検定向けには、

> **Jordan＝出力側の情報を状態へフィードバックするRNN**

と覚えるのが安全です。

## いつ使う？（得意・不得意）

Jordan Networkも現在の主流モデルというより、

- 初期RNN
- 時系列状態の保持
- Elman Networkとの構造比較

を理解するためのモデルです。

長期依存を扱うためのゲート構造は持たないため、LSTMやGRUとは別です。

## G検定ひっかけポイント

### Jordan＝隠れ層を戻す？

❌ hidden → context  
⭕ それは**Elman**

### Jordan＝出力をそのまま入力層へ戻すだけ？

❌ 単純コピーのみ  
⭕ **出力側情報をState Unitへ戻し、状態として次時刻に利用**

### LSTMとの違い

❌ ゲート付き長期記憶RNN  
⭕ **初期の再帰構造**

## まとめ（試験直前用）

- Jordan＝初期RNN
- **output側 → state**
- 状態を次時刻の隠れ層へ利用
- Elman＝**hidden → context**
- LSTM / GRUとは別構造
- **outputならJordan、hiddenならElman**

## 参考資料

- Jordan, M. I. (1986), *Serial Order: A Parallel Distributed Processing Approach*
- [Parallel Distributed Processing Handbook Chapter 5｜Stanford](https://web.stanford.edu/group/pdplab/originalpdphandbook/Chapter%205.pdf)

{% include gk_article_footer.html %}
