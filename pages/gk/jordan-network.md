---
layout: page
title: Jordan Networkとは？出力側の情報を状態へ戻すRNN【G検定対策】
description: "Jordan Networkの出力からStateへ戻る経路を、前出力・前状態・次状態の時間表で確認します。出力を外部入力へ単純コピーする説明と区別し、出力履歴を状態として次時刻の計算に利用する仕組みを整理します。"
permalink: /gk/jordan-network/
tags: [gk, neural_network, rnn]
gk_section: ディープラーニングの要素技術/リカレントニューラルネットワーク (RNN)
gk_order: 12
last_modified_at: 2026-10-19
---

## まず結論

**Jordan Network**は、出力側の情報をState Unitへ戻し、その状態を次時刻の隠れ層計算に利用する初期RNNです。

ここでは、**出力履歴がStateを介して次の処理へ伝わる流れ**を追います。隠れ層を戻すElmanとの判別は、[JordanとElmanの比較](/gk/jordan-vs-elman/)を使ってください。

## 直感的な説明

系列を出力するとき、直前に何を出したかが次の判断に関係することがあります。Jordanは、出力側からStateへ戻る経路で、その履歴を保持します。

単に「出力値を外部入力の欄へ入れ直す」処理と考えず、**出力を記憶する状態ユニットがある**点を押さえます。

## 定義・仕組み

原典のStateは、前時刻の出力とState自身の前状態の影響を受けます。

| 処理 | 戻ってくる出力側の情報 | 併せて使う状態 | 結果 |
| --- | --- | --- | --- |
| 時刻1に向けた更新 | 直前の出力y₀ | 前状態s₀ | 次に使う状態s₁ |
| 時刻2に向けた更新 | 時刻1の出力y₁ | 前状態s₁ | 次に使う状態s₂ |
| 時刻3に向けた更新 | 時刻2の出力y₂ | 前状態s₂ | 次に使う状態s₃ |

ここでの添字は処理順を示すための表記です。y₀・s₀は開始時の値として扱います。

新しい状態は、その時刻の外部入力とともに隠れ層の計算へ使われ、出力につながります。**出力→State→次の処理**と一周する経路を追うと、出力と状態を取り違えにくくなります。

## いつ使う？（得意・不得意）

過去の出力を系列の文脈として使う初期RNNの構造を理解するためのモデルです。ゲート構造を持つLSTMやGRUと同一のモデルではありません。

## G検定ひっかけポイント

- **output側 → state**という帰還元を見るのがJordanの判断基準です。
- Stateは前出力だけの単純な置き場とは限らず、前状態の影響も受けます。
- 隠れ層の活性をContextへコピーする構造は[Elman Network](/gk/elman-network/)です。
- 出力を戻すという説明だけから、長期記憶のゲートを持つとは判断しません。

## まとめ（試験直前用）

- Jordanは**出力側の情報**をStateへ戻す
- Stateは前出力と前状態の影響を受ける
- その状態を次の隠れ層計算へ利用する
- 出力を外部入力へ入れ直すだけの処理と混同しない

## 参考資料

- Jordan, M. I. (1986), *Serial Order: A Parallel Distributed Processing Approach*
- [Parallel Distributed Processing Handbook Chapter 5｜Stanford](https://web.stanford.edu/group/pdplab/originalpdphandbook/Chapter%205.pdf)

{% include gk_article_footer.html %}
