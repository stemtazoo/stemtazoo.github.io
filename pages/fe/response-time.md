---
layout: page
title: レスポンスタイムとは？ターンアラウンドタイムとの違いを時間軸で理解【基本情報技術者試験】
description: レスポンスタイムは要求から最初の応答まで、ターンアラウンドタイムは全処理完了までの時間として、待ち時間・処理時間・出力時間を変える操作教材でFE科目Aの判断方法を学びます。
permalink: /fe/response-time/
tags: [fe, fe-technology, computer-system, performance]
fe_section: テクノロジ系
fe_subsection: コンピュータシステム
fe_order: 125
date: 2026-11-04
last_modified_at: 2026-11-04
related_articles:
  - /fe/throughput/
  - /fe/turnaround-time/
  - /fe/system-performance-evaluation/
---

## まず結論

**レスポンスタイム（response time、応答時間）**とは、利用者がシステムへ要求を出してから、**最初の応答が返るまで**にかかる時間です。

**ターンアラウンドタイム**は、要求の受付から**処理結果の出力がすべて完了するまで**の時間です。基本情報技術者試験（FE）の科目Aでは、**どの時点までを測るか**を見分けます。

| 性能指標 | 注目する区間 |
|---|---|
| レスポンスタイム | 要求 → 最初の応答 |
| ターンアラウンドタイム | 要求 → 全処理・出力の完了 |
| スループット | 単位時間に完了できる処理件数（量） |

※実際のシステムでは「応答」をいつとするかの測定条件が異なる場合があります。**試験問題の測定開始・終了時点の指定が最優先**です。

## 直感的な説明

レストランで注文する場面を考えます。

- **レスポンスタイム**：注文を伝えてから、店員から「承りました」と最初の返事があるまで。
- **ターンアラウンドタイム**：注文を伝えてから、注文した料理がすべて提供されるまで。

**最初の返事が早くても、料理がすべて届くまでの時間が短いとは限りません。**

## 定義・仕組み

オンライン処理を例に、測定時点を明確にします。

```text
要求開始       最初の応答        全出力完了
  │────待機・処理────│────残りの出力────│
  │←レスポンスタイム→│
  │←──ターンアラウンドタイム──→│
```

今回の学習用モデルでは、要求を出した時点を **0秒** として、次の3つを足し合わせます。

- **待ち時間**：処理が開始されるまでの時間
- **処理時間**：最初の応答を作るまでの時間
- **残りの出力時間**：最初の応答から全結果の出力が終わるまでの時間

このモデルであれば、

```text
レスポンスタイム = 待ち時間 + 処理時間
ターンアラウンドタイム = レスポンスタイム + 残りの出力時間
```

となります。これは**この教材の測定条件における式**であり、すべてのシステムの固定公式ではありません。

### 触って覚える：最初の応答と全完了の区間を比べよう

**予想してみよう：残りの出力時間だけを長くすると、レスポンスタイムとターンアラウンドタイムのどちらが長くなるでしょうか？**

待ち時間・処理時間・残りの出力時間を変更し、「反映して比較」を押すと、時間軸が更新されます。

<link rel="stylesheet" href="{{ '/assets/css/fe-response-time-visualizer.css' | relative_url }}">

<div class="fe-response-demo" id="fe-response-demo">
  <p class="fe-response-demo__step"><strong>① 条件を設定</strong>（単位は秒）</p>
  <div class="fe-response-demo__controls">
    <label for="fe-response-wait">処理開始までの待ち時間
      <input id="fe-response-wait" type="range" min="0" max="10" step="1" value="3">
      <output for="fe-response-wait" id="fe-response-wait-value">3秒</output>
    </label>
    <label for="fe-response-work">最初の応答までの処理時間
      <input id="fe-response-work" type="range" min="1" max="10" step="1" value="4">
      <output for="fe-response-work" id="fe-response-work-value">4秒</output>
    </label>
    <label for="fe-response-output">最初の応答後、全出力完了までの時間
      <input id="fe-response-output" type="range" min="0" max="10" step="1" value="5">
      <output for="fe-response-output" id="fe-response-output-value">5秒</output>
    </label>
  </div>
  <p class="fe-response-demo__step"><strong>② 予想を選ぶ</strong>（省略もできます）</p>
  <fieldset class="fe-response-demo__predict">
    <legend>最後の出力時間だけを延ばすと？</legend>
    <label><input type="radio" name="fe-response-guess" value="response"> レスポンスタイムだけ長くなる</label>
    <label><input type="radio" name="fe-response-guess" value="turnaround"> ターンアラウンドタイムだけ長くなる</label>
    <label><input type="radio" name="fe-response-guess" value="both"> 両方長くなる</label>
  </fieldset>
  <div class="fe-response-demo__actions">
    <button type="button" data-apply>反映して比較</button>
    <button type="button" data-reset>最初から</button>
  </div>
  <p data-feedback class="fe-response-demo__feedback" role="status" aria-live="polite">初期条件：待ち3秒、処理4秒、出力5秒。変更して結果を比べてください。</p>
  <div class="fe-response-demo__display" data-display>
    <div class="fe-response-demo__timeline" data-timeline aria-label="時間軸：待ち3秒、処理4秒、出力5秒">
      <span class="fe-response-demo__bar fe-response-demo__bar--wait" data-bar="wait" style="flex:3">待ち</span>
      <span class="fe-response-demo__bar fe-response-demo__bar--work" data-bar="work" style="flex:4">処理</span>
      <span class="fe-response-demo__bar fe-response-demo__bar--output" data-bar="output" style="flex:5">出力</span>
    </div>
    <p data-response>最初の応答：7秒（待ち3＋処理4）</p>
    <p data-turnaround>全出力完了：12秒（7＋出力5）</p>
    <p data-reason>レスポンスタイムは最初の応答まで。ターンアラウンドタイムは出力完了までです。</p>
  </div>
  <p class="fe-response-demo__note">この教材では「出力時間」は最初の応答が返った**後の残りの出力時間**です。実際の応答時間・処理完了時点は設問や計測仕様に従います。</p>
</div>
<noscript><p>JavaScriptが無効でも学習できます。初期条件では待ち3秒＋処理4秒＝**レスポンスタイム7秒**、さらに残りの出力5秒を足して**ターンアラウンドタイム12秒**です。出力だけを5秒から8秒に増やすと、最初の応答は7秒のまま、全完了は15秒になります。</p></noscript>
<script src="{{ '/assets/js/fe-response-time-visualizer.js' | relative_url }}" defer></script>

## 科目Aでどう出る？

「最初の応答まで」と「全処理の終了まで」を区別するのがポイントです。

| 問題文の表現 | 判断 |
|---|---|
| 画面に応答が返るまでの待ち時間 | レスポンスタイム |
| ジョブの投入から結果の出力終了まで | ターンアラウンドタイム |
| 1秒間に完了した要求の件数 | スループット |

### 確認問題

あるシステムでは、要求受付後に処理開始まで2秒待ち、最初の応答を返すまでの処理に3秒かかり、さらに結果の残りを出力し終えるまで4秒かかった。この問題では、要求受付から最初の応答までをレスポンスタイムとする。

レスポンスタイムとして適切な値はどれか。

- ア：3秒
- イ：5秒
- ウ：9秒

<details markdown="1">
<summary>正解と解説を見る（タップして開く）</summary>

**正解：イ（5秒）**。要求から最初の応答までなので、待ち2秒＋処理3秒＝5秒です。

- ア：処理時間だけを数え、待ち時間を見落としています。
- イ：指定された測定区間を正しく合計しています。
- ウ：残りの出力時間4秒まで足した全出力完了の時間です。

</details>

## どんな場面で使う？

オンラインシステムでは利用者が最初の応答を待つ時間、バッチ処理ではジョブを投入してから結果が完了するまでの時間が重要になる場合があります。

ただし、**レスポンスタイムが短いからといってスループットまで高いとは限りません**。大量の要求を並列処理できるかどうかは別の要素です。[スループット](/fe/throughput/)や[ターンアラウンドタイム](/fe/turnaround-time/)と合わせて整理すると判断しやすくなります。

## よくある誤解・混同

### 「レスポンスタイムには待ち時間が含まれない」？

いいえ。要求してから最初の応答までを計測するのであれば、処理開始を待つ時間も含みます。

### 「最初の応答があれば処理はすべて完了している」？

そうとは限りません。途中から結果が出力されるシステムでは、最初の応答の後も処理や出力が続きます。

### 「ターンアラウンドタイムはCPU処理時間だけ」？

違います。要求受付から完了までが測定区間なら、待ち時間や入出力時間も含みます。

## まとめ（試験直前用）

- レスポンスタイム：要求から**最初の応答**まで。
- ターンアラウンドタイム：要求から**結果の出力が全部完了**するまで。
- スループット：**単位時間当たりの処理量**。
- 必ず設問で測定の開始時点と終了時点を確認する。
- 待ち時間を落とさず、最初の応答以降の出力時間を混ぜない。

{% include fe_article_footer.html %}
