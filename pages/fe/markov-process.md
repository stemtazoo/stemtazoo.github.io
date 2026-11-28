---
layout: page
title: マルコフ過程とは？状態遷移と確率の掛け算・足し算を判断する方法【基本情報技術者試験】
description: マルコフ過程を「次の状態が現在の状態だけに依存する確率過程」として整理し、状態遷移表から複数ステップ後の確率を求めるときの掛け算・足し算の判断をFE試験向けに解説します。
permalink: /fe/markov-process/
tags: [fe, fe-technology, basic-theory, probability]
fe_section: テクノロジ系
fe_subsection: 基礎理論
fe_order: 40
date: 2026-08-20
last_modified_at: 2026-11-28
image:
  path: https://filedn.com/lT3xytsFKGXmaz5GJGqwvRz/stemtazoo/eyecatch/fe/markov-process.png
  width: 1200
  height: 630
  alt: "マルコフ過程の確率計算。1本の経路A→B→Cの確率は0.5×0.4＝0.20と掛け算で求め、同じ到達先への複数経路の確率は足し合わせる。"
---

## まず結論

マルコフ過程とは、**次の状態が現在の状態によって決まり、それより前の過去には直接依存しないと考える確率過程**です。

基本情報技術者試験では、状態遷移表から数ステップ後の確率を求める問題で使われます。

まずは次の2つを押さえます。

```text
1本の経路をたどる確率
→ 掛け算

同じ到達先に至る複数の経路
→ 足し算
```

覚える一文はこれです。

> **経路の中は掛ける。経路どうしは足す。**

<figure style="margin:16px 0 20px;">
  <img src="https://filedn.com/lT3xytsFKGXmaz5GJGqwvRz/stemtazoo/eyecatch/fe/markov-process.png"
       width="1200" height="630" loading="lazy" decoding="async"
       alt="マルコフ過程の確率計算。1本の経路A→B→Cの確率は0.5×0.4＝0.20と掛け算で求め、同じ到達先への複数経路の確率は足し合わせる。"
       style="display:block;width:100%;max-width:100%;height:auto;">
</figure>

このページは、**現在の状態から数ステップ後の確率を求める計算**を中心に扱います。表の行・列の読み方や、同じ条件の確率の合計が1になる理由は、[遷移確率表の読み方](/fe/transition-probability/)で確認できます。

## 直感的な説明

天気が「晴れ・曇り・雨」の3状態を行き来すると考えます。

例えば、今日が雨なら、明日の天気は次のような確率で決まるとします。

```text
雨 → 晴れ 30%
雨 → 曇り 50%
雨 → 雨   20%
```

このとき、2日後が晴れになる経路は1つではありません。

```text
雨 → 晴れ → 晴れ
雨 → 曇り → 晴れ
雨 → 雨   → 晴れ
```

それぞれの経路の確率を掛け算で求め、最後に足し合わせます。

これが、マルコフ過程の確率計算で基本になる考え方です。

## 定義・仕組み

マルコフ過程では、現在の状態から次の状態へ移る確率を**遷移確率**といいます。

例えば、状態Aから状態Bへ移る確率が0.4なら、

```text
A → B
確率 0.4
```

と考えます。

### マルコフ性

重要な特徴は、**次の状態を決めるときに現在の状態だけを見る**ことです。

```text
過去の状態を全部さかのぼる
→ しない

現在の状態を見る
→ 次の状態の確率を決める
```

この性質をマルコフ性といいます。

### 状態遷移表

状態遷移表では、一般に

- 行：現在の状態
- 列：次の状態

として読むことが多いです。

ただし、問題ごとに表の向きは必ず確認します。

また、1つの状態から次の各状態へ進む確率の合計は、通常1になります。

```text
0.3 + 0.5 + 0.2 = 1.0
```

これを使うと、表の読み間違いにも気付きやすくなります。

このテーマは、基本情報技術者試験の基礎理論や確率に関係します。公式の出題範囲やシラバスは、[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html)から確認できます。

### 触って覚える：確率を次の状態へ移す

状態AとBの2状態の例です。最初は全てAです。「次の時点へ」を押して、図の中のA・Bの確率と掛け算、足し算の内訳を見てください。矢印の確率は変わりません。もう一度押すと、1回目の確率を使って次の確率を計算します。

<link rel="stylesheet" href="{{ '/assets/css/first-step-demos.css' | relative_url }}">
<div class="first-step-demo" data-first-step="markov" hidden>
  <svg class="first-step-demo__markov-graph" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 206" width="300" height="206" role="img" aria-labelledby="fe-markov-graph-title fe-markov-graph-desc">
    <title id="fe-markov-graph-title">AとBの確率付き状態遷移図</title>
    <desc id="fe-markov-graph-desc">AからAへ70%、AからBへ30%、BからAへ40%、BからBへ60%。矢印の遷移確率は固定で、状態内の確率は時点ごとに変化する。状態確率は図の下の結果文でも確認でき、計算式は到達先ごとに表示する。</desc>
    <defs>
      <marker id="fe-markov-arrow" viewBox="0 0 8 8" markerWidth="7" markerHeight="7" refX="7" refY="4" orient="auto"><path d="M1 1 L7 4 L1 7" fill="none" stroke="#34465b" stroke-width="1.2"/></marker>
    </defs>
    <rect width="300" height="206" rx="8" fill="#fff"/>
    <text class="markov-time" x="150" y="17" data-markov-time>時点0</text>
    <g class="markov-edges" marker-end="url(#fe-markov-arrow)">
      <path d="M47 88 C8 40 120 40 81 88"/>
      <path d="M219 88 C180 40 292 40 253 88"/>
      <path d="M104 104 Q150 74 196 104"/>
      <path d="M196 139 Q150 169 104 139"/>
    </g>
    <g class="markov-edge-labels">
      <text x="64" y="40">70%</text>
      <text x="236" y="40">60%</text>
      <text x="150" y="79">30%</text>
      <text x="150" y="173">40%</text>
    </g>
    <rect x="24" y="88" width="80" height="72" rx="13" fill="#e2eefb" stroke="#527ba5" stroke-width="1.5"/>
    <rect x="196" y="88" width="80" height="72" rx="13" fill="#e2f2e9" stroke="#4c806d" stroke-width="1.5"/>
    <g class="markov-state-labels">
      <text x="64" y="113">状態A</text><text x="236" y="113">状態B</text>
      <text class="markov-value" x="64" y="143" data-markov-a>100%</text>
      <text class="markov-value" x="236" y="143" data-markov-b>0%</text>
    </g>
    <text class="markov-note" x="150" y="196">矢印の確率は固定</text>
  </svg>
  <p class="first-step-demo__markov-legend">矢印の数値は移る確率（固定）、状態A・Bの中の数値は今その状態にいる確率（変化）です。</p>
  <div class="first-step-demo__actions">
    <button type="button" data-action="next">次の時点へ</button>
    <button type="button" data-action="reset">最初から</button>
  </div>
  <div data-calculation aria-label="到達先ごとの計算内訳"></div>
  <p role="status" data-result></p>
</div>
<noscript><p>初期A＝100%、B＝0%。1回後はA＝70%、B＝30%。2回後のAは70%×0.7＋30%×0.4＝61%、Bは39%です。</p></noscript>

この教材では同じ遷移確率を3回まで使います。

<script defer src="{{ '/assets/js/first-step-demos.js' | relative_url }}"></script>

## 科目Aでどう出る？

科目Aでは、状態遷移表を使って「2回後」「3回後」の状態確率を求める問題が出ます。

### 1本の経路は掛ける

例えば、

```text
A → B の確率 = 0.5
B → C の確率 = 0.4
```

なら、

```text
A → B → C
```

という1本の経路の確率は、

```text
0.5 × 0.4 = 0.20
```

です。

### 複数の経路は足す

2回後にCへ到達する経路が複数あるなら、それぞれを求めて足します。

```text
A → A → C
A → B → C
A → C → C
```

なら、

```text
各経路の確率を求める
↓
すべて足す
↓
2回後にCである確率
```

となります。

### 判断手順

試験では、次の順番で考えると安全です。

1. 初期状態を確認する
2. 何回遷移するのか確認する
3. 目的の状態へ届く経路を列挙する
4. 各経路内の確率を掛ける
5. 複数経路の確率を足す

## どんな場面で使う？

マルコフ過程は、状態が確率的に変化する現象を表すときに使われます。

例えば、次のような場面があります。

- 天気の状態変化
- 機械の正常・劣化・故障状態
- 顧客の行動状態
- 在庫や需要の状態変化
- 通信やシステムの状態遷移

FE試験では、実務分野の細かい応用よりも、**遷移確率表を正しく読んで計算できること**が重要です。

## よくある誤解・混同

### ❌ 2日後の確率だから、確率を全部足す

誤りです。

同じ1本の経路の中では、順番に起こる事象なので掛け算します。

```text
A → B → C
→ 掛け算
```

複数の別経路をまとめるときに足し算します。

```text
A → B → C
A → D → C
→ それぞれ求めて足す
```

### ❌ 過去の状態をすべて使って次を決める

マルコフ過程では、基本的に次の状態は現在の状態に依存すると考えます。

### ❌ 行と列は必ず決まっている

問題によって表の見せ方が異なることがあります。

見出しを確認して、**現在の状態から次の状態へ**読めているかを確かめます。

### ❌ 目的の状態へ行く経路を1本だけ選ぶ

複数の経路があるなら、すべて考える必要があります。

特に「2回後にAである確率」のような問題では、途中状態ごとに経路を分けると漏れにくくなります。

## まとめ（試験直前用）

- マルコフ過程は、次の状態が現在の状態に依存する確率過程
- 状態から状態へ移る確率を遷移確率という
- 状態遷移表は、行と列の意味を最初に確認する
- **1本の経路は掛け算**
- **同じ到達先への複数経路は足し算**
- 数ステップ後の確率は、到達経路を列挙すると解きやすい
- 各行の遷移確率の合計が1になるかも確認する

> **マルコフ過程は「現在を見る」。計算は「経路内で掛ける、経路どうしで足す」。**

{% include fe_article_footer.html %}
