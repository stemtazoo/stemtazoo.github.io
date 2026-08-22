---
layout: page
title: AR / MA / ARMA / ARIMAの違いまとめ【G検定対策】
description: "AR・MA・ARMA・ARIMAを、過去の値、過去の誤差、両方、差分を含むモデルという軸で比較します。ARIMAのIがIntegratedを表し、差分次数dと関係することをG検定の判断基準として整理します。"
permalink: /gk/time-series-ar-arma-arima/
tags: [gk, time_series]
gk_section: 機械学習の概要/代表的な手法/教師あり学習
gk_order: 7
last_modified_at: 2026-08-22
---

## まず結論

AR / MA / ARMA / ARIMA は、時系列の予測・モデル化で使われる代表的なモデルです。

- **AR**：過去の値を使う
- **MA**：過去の誤差を使う
- **ARMA**：AR＋MA
- **ARIMA**：ARMAに**差分（Integrated）**の考え方を加える

G検定では、**何を使って予測するか**で切り分けます。

## 直感的な説明

- AR → 「自分の過去を見る」
- MA → 「過去の予測誤差を見る」
- ARMA → 「両方を見る」
- ARIMA → 「必要なら差分してからARMAの考え方を使う」

## 定義・仕組み

### AR（AutoRegressive）

現在の値を、過去の自分自身の値から説明します。

### MA（Moving Average）

ここでいうMAは、単純な移動平均ではなく、**過去の誤差項**を使う時系列モデルです。

### ARMA

ARとMAを組み合わせたモデルで、基本的に定常な系列を対象とします。

### ARIMA

ARIMAの `I` は **Integrated** を表します。実務・試験では、非定常な系列に差分を取り、差分後の系列をARMAで表すモデルとして理解すると分かりやすいです。

`ARIMA(p, d, q)` の `d` は**差分次数**です。

> I = 差分そのものの英訳

と覚えるより、**Integratedという名前と差分次数dの関係**で押さえる方が正確です。

## いつ使う？（得意・不得意）

- 自己相関を利用したい → AR
- 誤差項の時間的な関係を扱いたい → MA
- 両方を扱いたい定常系列 → ARMA
- 差分で定常化を図りたい非定常系列 → ARIMA

ただし、ARIMAを使えばあらゆる非定常性を扱えるわけではありません。季節性にはSARIMAなど別の拡張もあります。

## G検定ひっかけポイント

- ❌「MAは過去の観測値の単純平均」→ この文脈のMAは**誤差項**を使うモデル
- ❌「ARIMAは多変量モデル」→ 基本形は単変量
- ❌「ARIMAのIは差分の英単語」→ Iは**Integrated**
- ⭕「ARIMA(p,d,q)のd」→ 差分次数
- ⭕「ARMAは定常系列を基本に考える」

## まとめ（試験直前用）

- AR＝過去の値
- MA＝過去の誤差
- ARMA＝AR＋MA
- ARIMA＝差分を含むARMA系モデル
- **I = Integrated、d = 差分次数**

次に読むなら、[定常性](/gk/stationarity/)と[VAR](/gk/var/)を確認するとつながります。

{% include gk_article_footer.html %}
