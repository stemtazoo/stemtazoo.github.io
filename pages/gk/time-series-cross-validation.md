---
layout: page
title: 時系列データの交差検証｜通常のk-foldとの違い【G検定】
description: "時系列データの交差検証を、時間順序と未来情報の混入という観点から整理します。通常のランダムなk-foldが不向きな理由、Time Series Splitや拡大型・移動窓型の考え方、G検定でデータリーケージを見抜く判断基準を確認できます。"
permalink: /gk/time-series-cross-validation/
tags: [gk, machine_learning, evaluation]
gk_section: 機械学習の概要/モデルの選択・評価/データ分割・交差検証
gk_order: 3
last_modified_at: 2026-11-25
---

## まず結論

時系列データで問題なのは**交差検証そのもの**ではなく、**時間順序を無視した分割**です。

> **過去で学習 → 未来で検証**

この順序を守るのが基本です。

## 直感的な説明

売上予測で、来月の情報を見てから今月を予測できたら不公平です。

時系列では、データの並びに意味があります。そのため、一般的なデータのように無作為に混ぜて分割すると、未来の情報が学習側へ入り込むことがあります。

## 定義・仕組み

通常のk-foldでは、順序に依存しないデータを複数のfoldへ分け、訓練・検証を入れ替えて評価します。

一方、時系列では時間の前後関係を守ります。

### 拡大型のイメージ

- 学習：1〜100日 → 検証：101〜120日
- 学習：1〜120日 → 検証：121〜140日

### 移動窓型のイメージ

- 学習：1〜100日 → 検証：101〜120日
- 学習：21〜120日 → 検証：121〜140日

どちらも**検証期間より未来のデータを学習に使わない**点が共通です。

### 触って覚える：学習と検証を時間順に分ける

「次の分割」を押して、学習と検証の月がどちらに動くか見てください。「ランダム分割の例」に切り替えると、検証する月より後の月が学習に含まれる例と比べられます。

<link rel="stylesheet" href="{{ '/assets/css/first-step-demos.css' | relative_url }}">
<div class="first-step-demo" data-first-step="time" hidden>
  <fieldset>
    <legend>分割方法</legend>
    <label><input type="radio" name="demo-time-mode" value="time" checked> 時間順（拡大型）</label>
    <label><input type="radio" name="demo-time-mode" value="mixed"> ランダム分割の例</label>
  </fieldset>
  <div class="first-step-demo__actions">
    <button type="button" data-action="next">次の分割</button>
    <button type="button" data-action="reset">最初から</button>
  </div>
  <ol class="first-step-demo__months" data-board aria-label="月ごとのデータの使い方"></ol>
  <p role="status" data-result></p>
</div>
<noscript><p>時系列の例では1〜3月で学習・4月で検証し、次は1〜4月で学習・5月で検証します。2月を検証しながら3〜6月を学習に含めると、検証時点より後の情報を使うことになります。</p></noscript>

ランダム分割は未来情報が混ざる固定例です。実際に過去の時点から未来を予測する場面を想定しています。

<script defer src="{{ '/assets/js/first-step-demos.js' | relative_url }}"></script>

## いつ使う？（得意・不得意）

時間の順序が予測条件に関係するデータで使います。

- 売上・需要
- 株価などの金融時系列
- センサーログ
- 時系列の利用履歴

ただし、時刻が付いているだけで必ず同じ分割が必要とは限りません。重要なのは、**実運用で未来情報を利用できない問題か**です。

## G検定ひっかけポイント

- ❌ **時系列では交差検証は使えない** → 言い切りは誤り
- ❌ **データをランダムに混ぜてからk-foldする** → 未来情報混入に注意
- ⭕ **時間順序を維持して複数回評価する** → 時系列交差検証
- ⭕ **未来情報が学習へ入ると評価が過大になり得る** → データリーケージ

判断基準は、

> **その予測時点で本当に使える情報だけで学習しているか？**

です。

## まとめ（試験直前用）

- 時系列でも交差検証はできる
- NGなのは時間順序を壊す分割
- 基本は「過去で学習 → 未来で検証」
- ランダムshuffleは要注意
- 未来情報の混入＝データリーケージを疑う

関連： [交差検証](/gk/cross-validation/) / [学習・検証・テストデータ](/gk/train-validation-test/)

{% include gk_article_footer.html %}
