---
layout: page
title: レスポンスタイムとは？ターンアラウンドタイムとの違いを時間軸で理解【基本情報技術者試験】
description: オンライン処理の入力完了から出力開始までのレスポンスタイムと、入力開始から出力完了までのターンアラウンドタイムを、4区間の操作教材で比較します。
permalink: /fe/response-time/
tags: [fe, fe-technology, computer-system, performance]
fe_section: テクノロジ系
fe_subsection: コンピュータシステム
fe_order: 125
date: 2026-11-04
last_modified_at: 2026-11-05
related_articles:
  - /fe/throughput/
  - /fe/turnaround-time/
  - /fe/system-performance-evaluation/
---

## まず結論

**レスポンスタイム（response time、応答時間）**は、オンライン処理では一般に、**入力を完了してから、処理結果の出力が始まるまで**の時間です。

**ターンアラウンドタイム**は、オンライン処理の一連の作業を測る場合、**入力を開始してから、結果の出力がすべて完了するまで**の時間です。終点だけでなく、**始点の違い**にも注目しましょう。

| 性能指標 | この教材で測る区間 |
|---|---|
| レスポンスタイム | 入力完了 → 出力開始（最初の応答） |
| ターンアラウンドタイム | 入力開始 → 全出力完了 |
| スループット | 単位時間に完了できる処理件数（量） |

**測定範囲は文脈によって異なります。試験問題の測定開始・終了時点の指定が最優先**です。ジョブの到着から完了までをターンアラウンドタイムとする計算は、[ジョブの待ち時間とターンアラウンドタイム](/fe/turnaround-time/)で扱います。

## 直感的な説明

検索画面で、検索条件を入力する場面を考えます。

- **入力開始**：条件を入力し始める。
- **入力完了**：検索ボタンを押して要求を送る。
- **出力開始**：最初の検索結果が表示される。
- **出力完了**：検索結果の表示がすべて終わる。

検索ボタンを押してから最初の結果を待つ時間が、この教材の**レスポンスタイム**です。条件を入力し始めてから全結果の表示が終わるまでが、**ターンアラウンドタイム**です。単に「受付中」と返す表示ではなく、処理結果の出力開始を応答として扱います。

## 定義・仕組み

この教材では、入力開始を **0秒** とし、次の4区間を順に並べます。

| 区間 | 初期値 | レスポンスタイムに含む | ターンアラウンドタイムに含む |
|---|---:|---|---|
| 入力開始 → 入力完了 | 2秒 | 含まない | 含む |
| 入力完了 → 処理開始（待ち） | 3秒 | 含む | 含む |
| 処理開始 → 出力開始（処理） | 4秒 | 含む | 含む |
| 出力開始 → 全出力完了（残りの出力） | 5秒 | 含まない | 含む |

- **レスポンスタイム = 待ち時間 + 処理時間**（初期値：3＋4＝7秒）
- **ターンアラウンドタイム = 入力時間 + レスポンスタイム + 残りの出力時間**（初期値：2＋7＋5＝14秒）

この区間の取り方は、電力広域的運営推進機関の[要件定義書の「画面の応答時間」図（本文27ページ）](https://www.occto.or.jp/choutatsu/2022/files/221207_ippan_unit_youkenteigi.pdf)でも示されています。式は**この教材の測定条件**に対応しており、すべての計測場面での固定公式ではありません。

### 触って覚える：最初の応答と全完了の区間を比べよう

**予想してみよう：残りの出力時間だけを長くすると、レスポンスタイムとターンアラウンドタイムのどちらが長くなるでしょうか？**

入力時間・待ち時間・処理時間・残りの出力時間を変更し、「反映して比較」を押すと、時間軸が更新されます。

<link rel="stylesheet" href="{{ '/assets/css/fe-response-time-visualizer.css' | relative_url }}">

<div class="fe-response-demo" id="fe-response-demo">
  <p class="fe-response-demo__step"><strong>① 条件を設定</strong>（単位は秒）</p>
  <div class="fe-response-demo__controls">
    <label for="fe-response-input">入力開始から入力完了までの時間
      <input id="fe-response-input" type="range" min="0" max="10" step="1" value="2">
      <output for="fe-response-input" id="fe-response-input-value">2秒</output>
    </label>
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
  <p data-feedback class="fe-response-demo__feedback" role="status" aria-live="polite">初期条件：入力2秒、待ち3秒、処理4秒、出力5秒。変更して結果を比べてください。</p>
  <div class="fe-response-demo__display" data-display>
    <p>時間軸（入力開始を0秒とする）</p>
    <div class="fe-response-demo__timeline" data-timeline aria-label="入力2秒、待ち3秒、処理4秒、残りの出力5秒">
      <span class="fe-response-demo__bar fe-response-demo__bar--input" data-bar="input" style="flex:2" aria-hidden="true"></span>
      <span class="fe-response-demo__bar fe-response-demo__bar--wait" data-bar="wait" style="flex:3" aria-hidden="true"></span>
      <span class="fe-response-demo__bar fe-response-demo__bar--work" data-bar="work" style="flex:4" aria-hidden="true"></span>
      <span class="fe-response-demo__bar fe-response-demo__bar--output" data-bar="output" style="flex:5" aria-hidden="true"></span>
    </div>
    <p data-phases>入力2秒 → 待ち3秒 → 処理4秒 → 残りの出力5秒</p>
    <p data-response><strong>レスポンスタイム：7秒</strong>（待ち3＋処理4）</p>
    <div class="fe-response-demo__measure" aria-hidden="true"><span data-response-range style="margin-left:14.2857%;width:50%"></span></div>
    <p data-response-endpoints>入力完了2秒 → 出力開始9秒</p>
    <p data-turnaround><strong>ターンアラウンドタイム：14秒</strong>（入力2＋待ち3＋処理4＋出力5）</p>
    <div class="fe-response-demo__measure fe-response-demo__measure--turnaround" aria-hidden="true"><span></span></div>
    <p data-turnaround-endpoints>入力開始0秒 → 全出力完了14秒</p>
    <p data-reason>開始位置は、レスポンスタイムが入力完了、ターンアラウンドタイムが入力開始です。</p>
  </div>
  <p class="fe-response-demo__note">棒の長さは上の時間軸と同じ縮尺です。入力時間を0秒にすると両指標の開始位置が重なります。この教材では「出力時間」は最初の応答が返った<strong>後の残りの出力時間</strong>です。実際の応答時間・処理完了時点は設問や計測仕様に従います。</p>
</div>
<noscript><p>初期条件は入力2秒、待ち3秒、処理4秒、残りの出力5秒。レスポンスタイムは入力完了2秒から出力開始9秒までの<strong>7秒</strong>、ターンアラウンドタイムは入力開始0秒から出力完了14秒までの<strong>14秒</strong>です。出力だけを5秒から8秒に増やすと、それぞれ7秒、17秒になります。</p></noscript>
<script src="{{ '/assets/js/fe-response-time-visualizer.js' | relative_url }}" defer></script>

## 科目Aでどう出る？

「いつから」「いつまで」の両方を確認するのがポイントです。

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

- この教材のレスポンスタイム：**入力完了**から**出力開始**まで。
- この教材のターンアラウンドタイム：**入力開始**から**全出力完了**まで。
- スループット：**単位時間当たりの処理量**。
- 必ず設問で測定の開始時点と終了時点を確認する。
- 待ち時間を落とさず、最初の応答以降の出力時間を混ぜない。

{% include fe_article_footer.html %}
