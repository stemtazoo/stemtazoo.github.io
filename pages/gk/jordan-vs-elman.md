---
layout: page
title: ジョルダンネットワークとElmanネットワークの違いとは？【RNN比較｜G検定対策】
description: "JordanとElmanを、構造図の帰還する矢印の出発点から判別する比較です。outputからStateへ戻るか、hiddenをContextへコピーするかを横並びにし、「過去を記憶する」「Contextがある」だけでは区別できない理由を確認します。"
permalink: /gk/jordan-vs-elman/
tags: [gk, neural_network, rnn]
gk_section: ディープラーニングの要素技術/リカレントニューラルネットワーク (RNN)
gk_order: 13
last_modified_at: 2026-10-19
---

## まず結論

JordanとElmanを見分けるときは、**次時刻へ戻る矢印がどこから出ているか**を確認します。

| 帰還の出発点 | モデル | 次へ渡す場所 |
| --- | --- | --- |
| 出力側（output） | Jordan | State Unit |
| 隠れ層（hidden） | Elman | Context Unit |

このページは、構造図や説明文から2つを判別するための比較です。時刻ごとの処理は[Jordanの状態更新](/gk/jordan-network/)・[ElmanのContext更新](/gk/elman-network/)で追えます。

## 直感的な説明

「前回の出力を手掛かりにする」のがJordan、「前回の内部表現を手掛かりにする」のがElmanです。どちらにも記憶があるという共通点だけでは見分けられません。

## 定義・仕組み

| 比較する点 | Jordan | Elman |
| --- | --- | --- |
| 主に戻す情報 | 出力側の情報 | 隠れ層の活性 |
| 状態の作り方 | 前出力と前状態の影響を受ける | 前隠れ層をContextへコピー |
| 外部入力との関係 | Stateを次の処理に使う | Contextを次の隠れ層計算に使う |
| 図で探す箇所 | 出力からStateへの帰還 | 隠れ層からContextへのコピー |

StateやContextという名前だけを探すのではなく、**何がそこへ入ってくるか**を追います。Jordanを「出力をそのまま外部入力へ戻すだけ」と省略すると、状態ユニットを介する点が抜け落ちます。

## いつ使う？（得意・不得意）

この比較は、初期RNNの構造を説明文や矢印から判別するときに使います。用途名だけでどちらのモデルかを決めたり、性能の優劣を付けたりするための表ではありません。

長期依存への工夫まで確認したい場合は、[LSTM](/gk/lstm/)へ進めます。Jordan・ElmanをそのままLSTMやGRUの別名とは考えません。

## G検定ひっかけポイント

| 説明 | 判断 |
| --- | --- |
| 隠れ層をContextへ1対1にコピーする | Elman |
| 出力側をStateへ戻す | Jordan |
| 過去の情報を次時刻に使う | 両者に共通。これだけでは判別できない |
| Contextという名前がある | 名称だけでなく、帰還元がhiddenかを確認する |

## まとめ（試験直前用）

- **output → State：Jordan**
- **hidden → Context：Elman**
- 記憶の有無ではなく、記憶へ戻す情報で判別する
- 更新の時間順序は各モデルの個別解説で確認する

### 参考資料（原典）

- Jordan, M. I. (1986), *Serial Order: A Parallel Distributed Processing Approach*
- Elman, J. L. (1990), [Finding Structure in Time](https://doi.org/10.1207/S15516709COG1402_1)

{% include gk_article_footer.html %}
