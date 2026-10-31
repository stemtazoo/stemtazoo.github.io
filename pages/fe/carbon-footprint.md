---
layout: page
title: カーボンフットプリントとは？製品のライフサイクル排出量を知る【基本情報技術者試験】
description: カーボンフットプリント（CFP）は原材料調達から廃棄・リサイクルまでの温室効果ガス排出量をCO₂換算で示す考え方。カーボンニュートラルやトレーサビリティとの違いを、科目Aの判断基準と操作例で学びます。
permalink: /fe/carbon-footprint/
tags: [fe, fe-strategy, business-strategy]
fe_section: ストラテジ系
fe_subsection: 経営戦略
fe_order: 125
date: 2026-10-31
last_modified_at: 2026-10-31
---

## まず結論

**カーボンフットプリント（CFP：Carbon Footprint of Products）**とは、製品・サービスの原材料調達から製造、輸送、使用、廃棄・リサイクルまでの**ライフサイクル全体で発生する温室効果ガスの排出量を、CO₂換算で数値化する考え方**です。

基本情報技術者試験の科目Aでは、**「製品のライフサイクル全体」「温室効果ガス」「CO₂換算」「表示」**が判断の目印です。

## 直感的な説明

ペットボトル飲料を1本買う場面を考えましょう。飲料を作る工場だけでなく、容器の材料を作るとき、輸送するとき、使い終わった容器を処理するときにも温室効果ガスが排出されます。

```text
原材料調達 → 製造 → 輸送・販売 → 使用 → 廃棄・リサイクル
       各工程の排出量をCO₂換算で合計する
                       ↓
                製品のCFP
```

例えば、1本当たりの排出量が次のように算定されたとします（数値は学習用の仮定です）。

| 工程 | 排出量（kg-CO₂e） |
|---|---:|
| 原材料調達 | 0.4 |
| 製造 | 0.3 |
| 輸送・販売 | 0.2 |
| 使用 | 0.0 |
| 廃棄・リサイクル | 0.1 |
| **合計** | **1.0** |

**kg-CO₂e** は、さまざまな温室効果ガスを温暖化への影響に応じて二酸化炭素（CO₂）相当に換算した量を表す単位です。製品によって算定対象・前提条件は異なります。

## 定義・仕組み

CFPでは、製品のライフサイクルに含まれる工程を定め、各工程の温室効果ガス排出量をCO₂相当に換算して集計します。製品単位の排出量を見える化することで、排出量が多い工程を把握し、改善の検討に役立てられます。

**CFPは排出量を測ること**であり、それだけで排出量がゼロになったり、環境に優しいと証明されたりするわけではありません。

参考：[経済産業省・環境省「カーボンフットプリント ガイドライン」](https://www.meti.go.jp/policy/energy_environment/global_warming/LCA_CFP/LCA_CFP.html)

### 触って確認：どの工程を減らすと合計が変わる？

**見るポイント：** まず「原材料調達を0.2 kg-CO₂e減らすと合計はどうなる？」と予想してから、値を変更してください。

この教材は**合計の考え方を理解するための単純な足し算モデル**です。実際のCFP算定に必要な排出係数・活動量・算定境界などは扱いません。

<link rel="stylesheet" href="{{ '/assets/css/fe-carbon-footprint-demo.css' | relative_url }}">

<div id="fe-carbon-footprint-demo" class="fe-cfp-demo">
  <p class="fe-cfp-prompt">予想：原材料調達を0.4から0.2に減らしたら、合計はどうなる？</p>
  <div class="fe-cfp-predict" role="group" aria-label="合計排出量の予想">
    <button type="button" data-cfp-guess="down">減る</button>
    <button type="button" data-cfp-guess="same">変わらない</button>
    <button type="button" data-cfp-guess="up">増える</button>
  </div>
  <div class="fe-cfp-fields">
    <div><label for="cfp-raw">原材料調達</label><input id="cfp-raw" type="range" min="0" max="1" step="0.1" value="0.4"><output id="cfp-raw-value" for="cfp-raw">0.4</output></div>
    <div><label for="cfp-make">製造</label><input id="cfp-make" type="range" min="0" max="1" step="0.1" value="0.3"><output id="cfp-make-value" for="cfp-make">0.3</output></div>
    <div><label for="cfp-ship">輸送・販売</label><input id="cfp-ship" type="range" min="0" max="1" step="0.1" value="0.2"><output id="cfp-ship-value" for="cfp-ship">0.2</output></div>
    <div><label for="cfp-use">使用</label><input id="cfp-use" type="range" min="0" max="1" step="0.1" value="0"><output id="cfp-use-value" for="cfp-use">0.0</output></div>
    <div><label for="cfp-end">廃棄・リサイクル</label><input id="cfp-end" type="range" min="0" max="1" step="0.1" value="0.1"><output id="cfp-end-value" for="cfp-end">0.1</output></div>
  </div>
  <div class="fe-cfp-summary">
    <p>製品1本のCFP（5工程の合計）</p>
    <output id="cfp-total" aria-live="polite">1.0 kg-CO₂e</output>
    <p id="cfp-comparison" aria-live="polite">初期値からの変化：0.0 kg-CO₂e</p>
    <div id="cfp-bars" class="fe-cfp-bars" aria-hidden="true"></div>
  </div>
  <p id="cfp-feedback" aria-live="polite">予想を選んでから、原材料調達の値を動かしてみましょう。</p>
  <button type="button" id="cfp-reset">初期値に戻す</button>
</div>
<script src="{{ '/assets/js/fe-carbon-footprint-demo.js' | relative_url }}" defer></script>

<noscript><p>JavaScriptが使えない場合：初期値は0.4＋0.3＋0.2＋0.0＋0.1＝1.0 kg-CO₂eです。原材料調達を0.4から0.2に減らすと、合計は0.8 kg-CO₂eになります。工程ごとの排出量を足し合わせることがCFPの基本です。</p></noscript>

## 科目Aでどう出る？

似た言葉を、**何を調べる・何を目指す仕組みか**で区別しましょう。

| 用語 | 判断の決め手 |
|---|---|
| **カーボンフットプリント** | **製品のライフサイクル全体の温室効果ガス排出量をCO₂換算で示す** |
| カーボンニュートラル | 温室効果ガスの排出と吸収・除去などを考慮し、**実質ゼロ**を目指す |
| 自動車の排出ガス規制 | 自動車の排気ガスに含まれる大気汚染物質などの排出を規制する |
| トレーサビリティ | 商品の生産・流通・販売などの**履歴を追跡できる**ようにする |

### 確認問題

ある企業が、製品の原材料調達、製造、輸送、使用、廃棄の各段階で生じる温室効果ガスをCO₂相当に換算し、製品単位の排出量として示そうとしている。該当する考え方はどれか。

- ア：カーボンニュートラル
- イ：カーボンフットプリント
- ウ：トレーサビリティ
- エ：自動車の排出ガス規制

<details markdown="1"><summary>答えと解説を見る</summary>

**正解：イ。** 製品のライフサイクル全体を対象に、温室効果ガス排出量をCO₂換算で表すためです。「実質ゼロ」ならカーボンニュートラル、「履歴の追跡」ならトレーサビリティと判断します。

</details>

## どんな場面で使う？

- **製品設計**：材料や製造工程を変更したときの排出量を比較する。
- **調達・物流**：原材料や輸送方法の見直しを検討する。
- **情報開示**：製品の排出量を算定条件とともに示す。

ただし、異なる製品の数値を比較するときは、算定対象や前提条件がそろっているか確認が必要です。

## よくある誤解・混同

### CFPが小さければカーボンニュートラル？

**いいえ。** CFPは排出量の算定・表示であり、実質ゼロの達成を意味しません。

### 工場での排出量だけを集計する？

**いいえ。** CFPでは、対象となる製品のライフサイクル全体を考えます。算定範囲は製品ごとのルールに従います。

### CO₂だけを計算する？

**いいえ。** 他の温室効果ガスも温暖化への影響に応じてCO₂相当に換算します。

### トレーサビリティと同じ？

**違います。** トレーサビリティは「どこで作られ、どの経路を通ったか」という履歴を追える仕組みです。CFPは排出量を数値化します。

## まとめ（試験直前用）

- **CFP＝製品ライフサイクル全体の温室効果ガス排出量をCO₂換算で示す。**
- **カーボンニュートラル＝実質ゼロを目指す。**
- **トレーサビリティ＝生産・流通などの履歴を追跡する。**
- 科目Aでは「**ライフサイクル全体＋CO₂換算＋製品単位の表示**」を見つけたらCFPを選びます。

{% include fe_article_footer.html %}
