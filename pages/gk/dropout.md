---
layout: page
title: Dropoutとは？学習時だけニューロンをランダムに無効化する過学習対策【G検定対策】
description: "Dropoutを、学習時に一部のニューロンをランダムに無効化して特定の経路への依存を抑える過学習対策として整理します。L1・L2正則化やEarly Stoppingとの違い、推論時には通常Dropoutを適用しない点を、G検定の選択肢を切る判断基準として確認します。"
permalink: /gk/dropout/
tags: [gk, neural_network, regularization]
gk_section: ディープラーニングの概要/正則化
gk_order: 3
last_modified_at: 2026-11-26
---

## まず結論

Dropoutは、**学習時に一部のニューロンをランダムに無効化することで、特定のニューロンや経路への依存を抑える過学習対策**です。

G検定では、次の対応で切ります。

- **重みに罰則項を加える** → [L1・L2正則化](/gk/regularization-l1-l2/)
- **ニューロンをランダムに無効化する** → Dropout
- **検証性能を見て学習を止める** → [Early Stopping](/gk/early-stopping/)

特に重要なのは、**Dropoutは主に学習時に使い、推論時は通常すべてのニューロンを使う**ことです。

## 直感的な説明

Dropoutは、いつも同じメンバーだけに頼らず、毎回少し違うメンバーで練習するイメージです。

いつも同じニューロンだけに頼ると、学習データに特化したパターンを覚えすぎることがあります。そこで学習中に一部をランダムに休ませ、**ほかのニューロンでも役割を分担できるようにする**のがDropoutです。

## 定義・仕組み

学習時に、各ニューロンの出力を一定確率で0にします。どのニューロンを無効化するかはランダムに変わります。

そのため、毎回まったく同じネットワークで学習するのではなく、異なる部分ネットワークを使って学習しているような効果が得られます。

### 学習時と推論時

| 場面 | Dropout |
|---|---|
| 学習時 | 一部のニューロンをランダムに無効化 |
| 推論時 | 通常は無効化せず、全体を使う |

実装では、学習時と推論時で出力の大きさが不自然に変わらないようスケーリングが行われます。G検定では細かな式より、**「学習時にランダム無効化」**を押さえれば十分です。

### 触って覚える：学習時と推論時のDropout

「次の学習例」を押し、8個のニューロンのうち出力を0にする位置が変わることを見てください。確率を変えたり、通常の推論時に切り替えたりして比べます。

<link rel="stylesheet" href="{{ '/assets/css/first-step-demos.css' | relative_url }}">
<div class="first-step-demo" data-first-step="dropout" hidden>
  <fieldset>
    <legend>モード</legend>
    <label><input type="radio" name="demo-dropout-mode" value="train" checked> 学習時</label>
    <label><input type="radio" name="demo-dropout-mode" value="infer"> 通常の推論時</label>
  </fieldset>
  <label>各ニューロンを無効化する確率
    <select data-rate>
      <option value="0">0%</option>
      <option value="25" selected>25%</option>
      <option value="50">50%</option>
      <option value="75">75%</option>
    </select>
  </label>
  <div class="first-step-demo__actions">
    <button type="button" data-action="next">次の学習例</button>
    <button type="button" data-action="reset">最初から</button>
  </div>
  <ul class="first-step-demo__cards" data-board aria-label="ニューロンの状態"></ul>
  <p role="status" data-result></p>
</div>
<noscript><p>学習時はニューロンごとに指定された確率で無効化されます。例えば8個で50%でも、毎回必ず4個になるとは限りません。通常の推論時は8個すべてを使います。</p></noscript>

教材は再現可能な3種類の抽選例を順に使います。各出力を独立に無効化する確率であり、毎回必ずその割合だけ無効になるとは限りません。出力のスケーリングは本文の説明を参照してください。

<script defer src="{{ '/assets/js/first-step-demos.js' | relative_url }}"></script>

## いつ使う？（得意・不得意）

### 得意な場面

- パラメータ数の多いニューラルネットワーク
- 学習データに過度に適合しているとき
- 特定のニューロンへの依存を弱めたいとき

### 注意点

- 無効化する割合が大きすぎると学習しにくくなる
- すべてのモデルで必ず効果が高いわけではない
- Dropout率を上げれば上げるほど良い、というものではない

Dropoutは過学習対策の1つであり、[正則化](/gk/regularization/)やデータ拡張などと目的に応じて使い分けます。

## G検定ひっかけポイント

### L1・L2との違い

❌ Dropoutは損失関数に罰則項を追加する  
⭕ それはL1・L2正則化。Dropoutは**ニューロンをランダムに無効化**します。

### 重みを永久に0にするわけではない

❌ Dropoutは不要な重みを0にして削除する  
⭕ 学習ステップごとに一部の出力を一時的に無効化します。

### 推論時にそのままDropoutしない

❌ 推論時も毎回ランダムにニューロンを落とす  
⭕ 通常の推論ではDropoutを無効にします。

### 選択肢を切る判断基準

- **ランダムにニューロンを休ませる** → Dropout
- **重みに絶対値・二乗の罰則** → L1・L2
- **検証性能が改善しなくなったら止める** → Early Stopping

## まとめ（試験直前用）

- Dropout＝**学習時にニューロンをランダム無効化**
- 目的は過学習を抑え、汎化性能を高めること
- 推論時は通常Dropoutを適用しない
- L1・L2は重みへの罰則、Dropoutはニューロンの無効化
- **「ランダムにノードを落とす」ならDropout**

次に読むなら、[正則化の全体像](/gk/regularization/)と[Early Stopping](/gk/early-stopping/)を比較すると整理しやすくなります。

## 参考資料（原論文）

- [Dropout: A Simple Way to Prevent Neural Networks from Overfitting｜JMLR](https://www.jmlr.org/papers/v15/srivastava14a.html)
  - Srivastavaら（2014）によるDropoutの代表的な原論文です。学習時にユニットとその接続をランダムに無効化し、過学習を抑える考え方を示しています。

{% include gk_article_footer.html %}
