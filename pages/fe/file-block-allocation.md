---
layout: page
title: ファイルのブロック割当とは？セクタ数と切り上げ計算【基本情報技術者試験】
description: ファイルのブロック割当で必要なセクタ数を求める方法を、ファイルごとの切り上げ、未使用領域、容量変更を試せる図解で整理します。
permalink: /fe/file-block-allocation/
tags: [fe, fe-technology, computer-system]
fe_section: テクノロジ系
fe_subsection: コンピュータシステム
fe_order: 231
date: 2026-10-10
last_modified_at: 2026-10-10
related_articles:
  - /fe/memory-fragmentation/
---
## まず結論

ファイルを**ブロック単位で割り当てる**方式では、ファイルがブロックの途中までしか使わなくても、**1ブロック分の領域を確保**します。

試験では、**ファイルごとに必要ブロック数を切り上げてから、合計する**のが判断基準です。

## 直感的な説明

4,000バイト入る箱に、4,001バイトのファイルを入れると、ほんの1バイトだけはみ出します。それでも箱はもう1個必要です。

- 4,000バイト → 1ブロック
- 4,001バイト → 2ブロック
- 8,000バイト → 2ブロック
- 8,001バイト → 3ブロック

## 定義・仕組み

**セクタ**は記憶装置の記録単位を表す用語、**ブロック**はこの例では複数のセクタをまとめたファイル領域の割当単位です。実際の装置やファイルシステムでは単位や大きさが異なるため、問題文の条件を優先します。

例えば、1セクタ500バイト、1ブロック8セクタなら、

```text
1ブロック = 500 × 8 = 4,000バイト
```

必要ブロック数は、ファイル容量を4,000で割って**端数を切り上げた整数**です。0バイトのファイルの扱いは方式により異なるため、ここでは正の容量を扱います。

### 動かして確認する：容量と割当ブロック

容量を変えると、使用領域（青）と未使用領域（薄い部分）、必要なブロック数が変わります。

<link rel="stylesheet" href="{{ '/assets/css/fe-visualizer.css' | relative_url }}">

<div class="fe-learning-demo fe-block-allocation-demo" data-fe-block-allocation-demo>
  <p class="fe-learning-demo__title">1ブロック＝4,000バイト（8セクタ）</p>
  <label for="fe-block-size">ファイル容量：<strong data-fba-size>9,000</strong>バイト</label>
  <input id="fe-block-size" type="range" min="500" max="16000" step="500" value="9000" data-fba-slider>
  <div class="fe-block-allocation-demo__blocks" data-fba-blocks aria-label="割り当てられたブロック"></div>
  <p class="fe-block-allocation-demo__legend">■ 使用中（青）／ □ ブロック内の未使用部分</p>
  <p class="fe-learning-demo__result" data-fba-result role="status" aria-live="polite">9,000バイト → 3ブロック → 24セクタ</p>
  <div class="fe-learning-demo__controls">
    <button type="button" class="fe-learning-demo__button" data-fba-set="4000">4,000バイト</button>
    <button type="button" class="fe-learning-demo__button" data-fba-set="4500">4,500バイト</button>
    <button type="button" class="fe-learning-demo__button" data-fba-set="9000">9,000バイト</button>
  </div>
  <noscript><p>JavaScriptが無効の場合も、下の計算表で確認できます。</p></noscript>
</div>

<script src="{{ '/assets/js/fe-visualizer.js' | relative_url }}" defer></script>

| ファイル容量 | 必要ブロック数 | 割当セクタ数 | 未使用領域 |
|---:|---:|---:|---:|
| 2,000バイト | 1 | 8 | 2,000バイト |
| 4,000バイト | 1 | 8 | 0バイト |
| 4,500バイト | 2 | 16 | 3,500バイト |
| 9,000バイト | 3 | 24 | 3,000バイト |

この「割り当てた領域の中の余り」は**内部フラグメンテーション**と考えられます。主記憶での例は[フラグメンテーション](/fe/memory-fragmentation/)で確認できます。ただし、ファイルのブロック割当と主記憶の管理方式は同一ではありません。

## 科目Aでどう出る？

複数ファイルを格納するときは、**各ファイルのブロック数を個別に求める**必要があります。

例えば、1ブロック4,000バイト、1ブロック8セクタとして、

| ファイル | 容量 | 必要ブロック数 |
|---|---:|---:|
| A | 2,000バイト | 1 |
| B | 9,000バイト | 3 |
| 合計 | 11,000バイト | 4 |

したがって、割当セクタ数は **(1 + 3) × 8 = 32セクタ**です。

## どんな場面で使う？

固定長の割当単位を使うファイル管理では、小さなファイルにも最低1単位の領域が必要になることがあります。ファイルが多いほど、末尾に生じる未使用部分も合計して考える必要があります。

## よくある誤解・混同

### ファイル容量を先に合計してから切り上げる

別々のファイルにそれぞれブロックを割り当てる条件では誤りです。2,000 + 9,000 = 11,000バイトをまとめて切り上げると3ブロックですが、実際には**1 + 3 = 4ブロック**必要です。

### 使用していない部分はセクタ数に含めない

割り当てられたブロックの一部が未使用でも、**割当セクタ数**にはそのブロック全体を含めます。

### セクタとブロックはいつも同じ大きさ

同じとは限りません。問題文に「8セクタを1ブロック」とあれば、その条件で計算します。

## まとめ（試験直前用）

- まず **1ブロックの容量＝1セクタの容量 × セクタ数**を求める
- **ファイルごとに割り算し、端数を切り上げる**
- 最後にブロック数を合計し、必要ならセクタ数に換算する

{% include fe_article_footer.html %}
