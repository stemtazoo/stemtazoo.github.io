---
layout: page
title: ジョルダンネットワークとElmanネットワークの違いとは？【RNN比較｜G検定対策】
description: "ジョルダンネットワークとElmanネットワークを、何を状態として次時刻へ引き継ぐかで比較します。Jordanは出力をもとに状態を更新し、Elmanは隠れ層の活性をcontext unitsへコピーする構造として、G検定での判断基準を整理します。"
permalink: /gk/jordan-vs-elman/
tags: [gk, neural_network, rnn]
gk_section: ディープラーニングの要素技術/リカレントニューラルネットワーク (RNN)
gk_order: 13
last_modified_at: 2026-09-04
---

## まず結論

ジョルダンネットワークとElmanネットワークは、どちらも**過去の情報を次時刻へ引き継ぐ再帰型ニューラルネットワーク**です。

G検定では、まず次の違いを押さえます。

- **Jordan**：前時刻の**出力をもとに状態を更新**する
- **Elman**：前時刻の**隠れ層の活性をcontext unitsへコピー**する

試験では、

**出力側の情報を戻す → Jordan**  
**隠れ層の状態を戻す → Elman**

と切り分けると分かりやすいです。

## 直感的な説明

2つの違いは、**「何を記憶として次へ渡すか」**です。

- **Jordan**：前回の**出力結果に関係する状態**を次へ渡す
- **Elman**：前回の**内部状態（隠れ層）**を次へ渡す

イメージすると、

- Jordan：**前回どう出力したか**を手掛かりに次を考える
- Elman：**前回内部でどんな状態だったか**を手掛かりに次を考える

という違いです。

ただし、Jordanを単純に「出力をそのまま次の入力へ入れるだけ」と考えるのは少し不正確です。

## 定義・仕組み

### ジョルダンネットワーク（Jordan Network）

Jordanの1986年のモデルでは、**state units（状態ユニット）**が系列の文脈を保持します。

この状態は、

- 前時刻の**出力**
- 前時刻の**状態**

の影響を受けて次時刻へ更新されます。

原典では、出力ユニットから状態ユニットへの再帰結合に加えて、状態ユニット自身への再帰結合も用いられています。

したがって、G検定向けに簡略化すると、

> **Jordan＝出力側の情報を状態へ戻すRNN**

と覚えるのが安全です。

### Elmanネットワーク（Elman Network）

Elmanの1990年のSimple Recurrent Networkでは、**隠れ層の活性をcontext unitsへ1対1でコピー**します。

次の時刻では、

- 現在の入力
- 1つ前の隠れ層を保存したcontext

の両方を使って新しい隠れ状態を計算します。

つまり、

> **Elman＝隠れ層の内部状態を次時刻へ渡すRNN**

です。

### 2つを比較

| 観点 | Jordan | Elman |
|---|---|---|
| 主に戻す情報 | 出力側の情報 | 隠れ層の活性 |
| 状態・context | 前出力と前状態に依存 | 前隠れ層をコピー |
| 記憶するイメージ | 過去の出力履歴 | 過去の内部表現 |
| G検定でのキーワード | **output** | **hidden / context** |

## いつ使う？（得意・不得意）

### Jordanが向く考え方

- 過去の出力系列が次の状態に強く関係する問題
- 出力履歴を文脈として利用したい場合

### Elmanが向く考え方

- 入力系列の時間的文脈を内部状態として保持したい場合
- 系列データの内部表現を学習したい場合

Elmanの原著では、時系列XORだけでなく、単語系列から統語的・意味的構造を学習する実験にも使われています。

### 共通の注意点

JordanもElmanも初期のRNNです。

長い時間間隔の依存関係を学習する場合、単純なRNNでは勾配消失・勾配爆発などが問題になりやすく、後にLSTMやGRUなどが広く使われるようになりました。

ただし、**JordanやElmanをそのままLSTM/GRUの同義語や直接の構造と考えない**ことが重要です。

## G検定ひっかけポイント

### どこから戻す？

❌ Jordan＝隠れ層をcontextへコピー  
⭕ それは**Elman**

❌ Elman＝出力側の情報を状態へ戻す  
⭕ それは**Jordan側の特徴**

### Jordanは「出力をそのまま入力へ戻す」？

❌ 出力値を単純に入力層へコピーするだけ  
⭕ **出力の情報をstate unitsへ戻し、前状態と合わせて文脈を保持する**

### Elmanのcontext units

❌ context unitsは独立に新しい特徴量を学習する層  
⭕ **前時刻の隠れ層の活性を保存し、次時刻へ渡す役割**

### LSTM・GRUとの違い

❌ Jordan / Elman ＝ LSTM / GRU  
⭕ どちらもRNN系だが、**LSTM・GRUには長期依存を扱いやすくするゲート構造がある**

### 試験中の判断基準

- **output → state/context** → Jordan
- **hidden → context** → Elman

この2語を見れば、まず選択肢を切れます。

## まとめ（試験直前用）

- JordanとElmanはどちらも**初期のRNN**
- **Jordan：出力側の情報を状態へ戻す**
- Jordanの状態は**前出力＋前状態**の影響を受ける
- **Elman：隠れ層の活性をcontextへコピー**
- Elmanではcontextが**前時刻の内部状態**を保持する
- G検定では **output＝Jordan / hidden＝Elman** で切る
- LSTM・GRUとは別の構造

### 参考資料（原典）

- Jordan, M. I. (1986), *Serial Order: A Parallel Distributed Processing Approach*
- Elman, J. L. (1990), [Finding Structure in Time](https://doi.org/10.1207/S15516709COG1402_1)

{% include gk_article_footer.html %}
