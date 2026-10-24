---
layout: page
title: ポーリング制御とは？割込み制御との違いと使い分け【基本情報技術者試験】
description: ポーリング制御を「CPUやプログラムが装置の状態を繰り返し確認する方式」として整理し、割込み制御との違い、確認間隔と検知遅れ、CPU負荷の考え方をFE科目A向けに解説します。
permalink: /fe/polling-control/
tags: [fe, fe-technology, operating-system, computer-architecture]
fe_section: テクノロジ系
fe_subsection: オペレーティングシステム
fe_order: 85
date: 2026-10-24
last_modified_at: 2026-10-24
related_articles:
  - /fe/internal-external-interrupts/
  - /fe/device-driver/
---

## まず結論

**ポーリング制御（Polling）**は、**CPUやプログラムが入出力装置などの状態を繰り返し読み取り、変化や処理完了を確認する方式**です。

基本情報技術者試験（FE）の科目Aでは、次の違いを最初に押さえます。

- **ポーリング**：CPU・プログラムが装置へ「終わった？」と確認する
- **割込み**：装置などがCPUへ「終わった」と通知する

判断の決め手は、**状態を調べに行く側がCPU・プログラムか、それとも装置などから通知が来るか**です。

## 直感的な説明

プリンタの印刷完了を待つ場面で考えます。

~~~text
ポーリング制御
CPU「印刷は終わった？」
装置「まだ」
CPU「印刷は終わった？」
装置「終わった！」
→ 次の処理へ
~~~

これに対して割込み方式では、CPUはほかの仕事をしながら待ち、完了の通知を受けて必要な処理を行えます。

~~~text
割込み制御
CPU「印刷を開始して」
CPU：ほかの処理を実行
装置「印刷が終わった！」→ 割込みで通知
CPU：必要な完了処理を実行
~~~

**問い合わせるのがポーリング、通知されるのが割込み**と考えると混同しにくくなります。

## 定義・仕組み

### 状態レジスタやビジー信号を調べる

入出力装置には、処理中か、完了したかなどを示す状態情報があります。CPUやプログラムがその情報を読み出して調べるのがポーリングです。

考え方を簡単に書くと、次のようになります（処理のイメージを示す簡略表現で、IPAの正式な疑似言語ではありません）。

~~~text
繰り返す：
  装置の状態を読む
  完了していたら、完了時の処理をして終了
  まだなら、必要に応じて一定時間待つ
~~~

ずっと連続して調べる場合も、間隔を空けて調べる場合もあります。**ポーリングは必ず「CPUを休まず使い続ける」という意味ではありません。**

### ポーリングと割込みの特徴

| 観点 | ポーリング制御 | 割込み制御 |
|---|---|---|
| 状態を知る方法 | CPU・プログラムが確認 | 装置などが通知 |
| 確認のための処理 | 繰り返し必要 | 通知待ちの間は繰返し確認が不要 |
| 検知の速さ | 確認間隔や処理状況に左右される | 割込み受付・処理の遅れに左右される |
| 向いている例 | 少数の機器の単純な定期確認 | 不定期に起きる入出力完了の通知 |

確認間隔を短くすると変化を早く見つけやすくなる一方、確認回数は増えます。逆に間隔を長くすると確認処理は減りますが、変化を見つけるまで待つことがあります。

### 確認間隔と検知の遅れを動かしてみる

下の例では、**0.5秒で異常が発生し、その状態が続く**とします。CPUは0秒から一定間隔で状態を確認します。スライダーで確認間隔を変え、**次の確認までに何秒待つか**を見てみましょう。

<div class="fe-learning-demo fe-polling-demo" data-fe-polling-demo>
  <p class="fe-learning-demo__title">ポーリング間隔と検知タイミング</p>
  <label for="fe-polling-interval">確認間隔：<output data-fe-polling-interval>2</output>秒</label>
  <input id="fe-polling-interval" type="range" min="1" max="5" step="1" value="2" aria-controls="fe-polling-result">
  <div class="fe-polling-demo__timeline">
    <div class="fe-polling-demo__track" aria-hidden="true">
      <div data-fe-polling-marks>
        <span class="fe-polling-demo__mark" style="left:0%"></span>
        <span class="fe-polling-demo__mark" style="left:33.333%"></span>
        <span class="fe-polling-demo__mark" style="left:66.667%"></span>
        <span class="fe-polling-demo__mark" style="left:100%"></span>
      </div>
      <span class="fe-polling-demo__event" style="left:8.333%"></span>
      <span class="fe-polling-demo__detect" data-fe-polling-detect style="left:33.333%"></span>
    </div>
    <div class="fe-polling-demo__ticks"><span>0秒</span><span>3秒</span><span>6秒</span></div>
  </div>
  <p class="fe-polling-demo__legend">│ 定期確認　▲ 異常発生（0.5秒）　● 初回検知</p>
  <p id="fe-polling-result" class="fe-polling-demo__result" role="status" aria-live="polite">初回検知：<output data-fe-polling-first>2</output>秒 ／ 検知の遅れ：<strong><output data-fe-polling-delay>1.5</output>秒</strong></p>
  <p class="fe-learning-demo__hint">見るポイント：0.5秒で起きた異常を、次の確認で初めて発見します。確認の所要時間や割込みの処理時間は考えない説明用モデルです。</p>
</div>

確認間隔が2秒のときは、0秒、2秒、4秒…で確認します。異常は0.5秒で発生するので、2秒に初めて気づき、**1.5秒の遅れ**が生じます。

この例では間隔を長くすると遅れも増えます。ただし実際の遅れは**異常がいつ起きたか**にもよるため、間隔を延ばせばどんな場合も必ず遅れが増すわけではありません。

JavaScriptが使えない場合も、上の2秒間隔の例と説明で仕組みを確認できます。

## 科目Aでどう出る？

科目Aでは「何を監視・制御しているか」よりも、**何をきっかけに処理するか**に注目します。

| 説明文の手掛かり | 考える用語 |
|---|---|
| CPUが状態レジスタやビジー信号を読み取る | **ポーリング** |
| 入出力完了を装置からCPUへ通知する | 割込み |
| タスク間でデータや通知を受け渡す | タスク間通信・同期 |
| 共有資源を一つのタスクが使えるように制限する | 排他制御 |

例えば「装置の状態を一定時間ごとに順番に調べる」という説明ならポーリングです。

一方、「優先度の高い処理のために実行中の処理を一時中断する」なら、割込みによる処理の切替えを説明しています。ポーリングそのものではありません。

## どんな場面で使う？

### 設備やセンサーの状態監視

例えば、装置の運転状態を1秒ごとに読み取り、異常フラグが立っていないか確認する方法はポーリングの例です。定期的な確認が目的なら、実装が単純で扱いやすいことがあります。

### 入出力の完了待ち

装置の処理完了がいつ起きるか分からない場合、確認を何度も繰り返すとCPUの仕事が増えることがあります。割込み方式なら、装置からの通知を利用して確認の繰返しを減らせます。

ただし、割込み処理にも負荷や切替えのコストがあります。**必ず割込みの方が高性能というわけではなく、確認頻度や処理量によって使い分けます。**

割込みがなぜ発生するかという分類は、[内部割込みと外部割込み](/fe/internal-external-interrupts/)で確認できます。

## よくある誤解・混同

### ポーリングならCPUは常に動き続ける？

必ずしもそうではありません。待ち時間を設けずに状態を調べ続ける方法はCPUを使いやすくなりますが、一定間隔で確認し、その間は別の処理や待機に回す方法もあります。

### 割込みなら遅れはゼロ？

違います。割込みにも通知の受付や処理の遅れがあります。「割込み＝必ず即時」「ポーリング＝必ず遅い」と決めつけません。

### ポーリングと排他制御は似ている？

目的が違います。ポーリングは**状態を知る方法**、排他制御は**共有資源の同時使用を防ぐ方法**です。

### ポーリングとタスク間通信は同じ？

違います。ポーリングは自ら状態を確認する動作です。タスク間通信は、タスク同士が情報をやり取りする仕組みを指します。

## まとめ（試験直前用）

- **CPUが状態レジスタ・ビジー信号を確認** → ポーリング制御
- **装置からCPUへ完了を通知** → 割込み制御
- 短い確認間隔は検知を早めやすいが、確認処理が増える
- ポーリングと割込みは性能の優劣を一律に決められない
- **状態確認・割込み・タスク間通信・排他制御**は、何をする仕組みかで切り分ける

参考：[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html)

<link rel="stylesheet" href="{{ '/assets/css/fe-visualizer.css' | relative_url }}?v=20261024-polling">
<script src="{{ '/assets/js/fe-visualizer.js' | relative_url }}?v=20261024-polling" defer></script>

{% include fe_article_footer.html %}
