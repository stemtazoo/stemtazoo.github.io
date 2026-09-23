---
layout: page
title: Elman Networkとは？隠れ状態をContextへ戻すRNN【G検定対策】
description: "Elman Networkを、前時刻の隠れ層の活性をContext Unitへコピーし、次時刻の隠れ層計算に利用する初期RNNとして整理します。出力側の情報を状態へ戻すJordan Networkとの違いを、hiddenとoutputという判断軸で確認します。"
permalink: /gk/elman-network/
tags: [gk, rnn]
gk_section: ディープラーニングの要素技術/リカレントニューラルネットワーク (RNN)
gk_order: 11
last_modified_at: 2026-09-23
---

## まず結論

**Elman Network**は、前時刻の**隠れ層の活性**をContext Unitへコピーし、次時刻の隠れ層計算へ使う初期のRNNです。

G検定では、

- hidden → context → hidden → **Elman**
- output側 → state → **Jordan**

と切り分けます。

## 直感的な説明

Elman Networkは、

> **前回、内部でどんな状態だったかを覚えて次を考える**

ネットワークです。

前時刻の隠れ層をContext Unitへ保存し、現在の入力と一緒に次の隠れ状態を計算します。

## 定義・仕組み

ElmanのSimple Recurrent Networkでは、

- 入力層
- 隠れ層
- Context Unit
- 出力層

を使います。

前時刻の隠れ層の活性をContext Unitへ1対1でコピーし、次時刻の隠れ層へ入力します。

この仕組みにより、過去の内部表現を現在の処理へ反映できます。

## いつ使う？（得意・不得意）

Elman Networkは現在の実務の主流モデルというより、

- RNNの基本構造
- 系列情報の保持
- Jordan Networkとの比較

を理解するための歴史的・教育的モデルとして重要です。

長期依存では単純RNN特有の勾配消失・爆発が問題になりやすく、LSTMやGRUが発展しました。

## G検定ひっかけポイント

### Elman＝出力を戻す？

❌ 前時刻の出力側の情報を状態へ戻す  
⭕ **前時刻の隠れ層をContextへコピー**

### Context Unit

❌ 独立した特徴抽出層  
⭕ **前時刻の隠れ層の活性を保持する**

### Jordanとの違い

- hidden → context → **Elman**
- output側 → state → **Jordan**

## まとめ（試験直前用）

- Elman＝初期RNN
- **隠れ層をContextへコピー**
- 次時刻の隠れ層計算に利用
- 長期依存には弱い
- Jordanとの違いは**どの情報を戻すか**

## 参考資料

- Elman, J. L. (1990), [Finding Structure in Time](https://doi.org/10.1207/S15516709COG1402_1)

{% include gk_article_footer.html %}
