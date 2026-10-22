---
layout: page
title: 排他的資源を使うタスクの実行時間とは？待ち時間をタイムチャートで求める【基本情報技術者試験】
description: 複数CPUで並列実行するタスクが共通資源を排他的に使うときの実行時間を、CPU処理と資源待ちを分けたタイムチャートで整理し、FE試験で待ち時間を見落とさない判断手順を解説します。
permalink: /fe/exclusive-resource-task-timing/
tags: [fe, fe-technology, operating-system, scheduling]
fe_section: テクノロジ系
fe_subsection: オペレーティングシステム
fe_order: 90
date: 2026-08-11
last_modified_at: 2026-10-22
related_articles:
  - /fe/task-scheduling/
  - /fe/cpu-scheduling-idle-time/
  - /fe/deadlock/
---

## まず結論

複数のタスクが同時に動けるシステムでも、**共通の資源を排他的に使用する区間では、同時にその資源を使えません。**

基本情報技術者試験では、次の順番で考えると実行時間を求めやすくなります。

```text
1. CPUはいくつあるか確認する
2. 各タスクが共有資源を要求する時刻を求める
3. 共有資源を使う時間帯が重なるか確認する
4. 重なったら、後から来たタスクに待ち時間を加える
5. 最後に終了するタスクの時刻を答える
```

特に大切なのは、**CPUが空いていても、必要な共有資源が使用中ならタスクは先へ進めない**という点です。

## 直感的な説明

CPUを「作業する人」、共有資源を「1台しかない機械」と考えてみます。

作業者が2人いれば、別々の作業は同時にできます。

```text
作業者A → 作業中
作業者B → 作業中
```

しかし、途中で2人とも同じ1台の機械を使う必要があるとします。

```text
共有機械R
→ 1人ずつしか使えない
```

Aが先に使っている間にBが来ても、Bは待たなければなりません。

```text
CPUが2台
→ CPU処理は同時に進められる

共有資源Rが1つ
→ Rを使う処理は同時に進められない
```

この**待ち時間**が、全体の終了時刻を遅らせます。

## 定義・仕組み

### 排他的に使用するとは

「排他的」とは、ある資源を1つのタスクが使用している間、他のタスクが同じ資源を使用できないことです。

```text
タスクAが資源Rを使用中
↓
タスクBも資源Rを要求
↓
タスクBは待つ
```

このような制御は、複数の処理が同じ資源を同時に変更して矛盾した状態になることを防ぐために使われます。

### CPUの数と資源の数は分けて考える

ここが最も重要です。

CPUが2台あっても、共有資源Rが1つなら、Rを使う部分は並列にはできません。

```text
CPU1 ── タスクA
CPU2 ── タスクB

共有資源R ── 1タスクずつ
```

したがって、問題では次の2点を別々に確認します。

| 確認するもの | 見るポイント |
|---|---|
| CPU | 同時に何タスクがCPU処理できるか |
| 共有資源 | 同時に何タスクがその資源を使えるか |

### タイムチャートで考える

例として、次の2タスクを考えます。

```text
タスクA
CPU 20ms → 資源R 40ms → CPU 30ms

タスクB
CPU 30ms → 資源R 40ms → CPU 20ms
```

CPUが2台なら、最初のCPU処理は同時に開始できます。ただし、資源Rを使えるのは一度に1タスクだけです。

<div style="max-width:100%; overflow-x:auto;" role="region" tabindex="0" aria-label="タスクと資源Rのタイムチャート。小さい画面では横にスクロールできます。">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 228" width="760" height="228" role="img" aria-labelledby="fe-r-timing-title fe-r-timing-desc" style="display:block;max-width:none;">
  <title id="fe-r-timing-title">CPU2台と排他的な資源Rのタイムチャート</title>
  <desc id="fe-r-timing-desc">タスクAは0から20ミリ秒までCPU、20から60まで資源R、60から90までCPU。タスクBは0から30までCPU、30から60までR待ち、60から100まで資源R、100から120までCPU。資源Rは20から60をA、60から100をBが使い、全体は120ミリ秒で終了します。</desc>
  <rect x="0" y="0" width="760" height="228" rx="8" fill="#f7f9fb"/>
  <text x="13" y="27" font-size="13" fill="#30475d">経過時間（ms）</text>
  <line x1="105" y1="36" x2="105" y2="188" stroke="#d6dee6" stroke-width="1"/>
  <text x="105" y="27" text-anchor="middle" font-size="13" fill="#30475d">0</text>
  <line x1="205" y1="36" x2="205" y2="188" stroke="#d6dee6" stroke-width="1"/>
  <text x="205" y="27" text-anchor="middle" font-size="13" fill="#30475d">20</text>
  <line x1="255" y1="36" x2="255" y2="188" stroke="#d6dee6" stroke-width="1"/>
  <text x="255" y="27" text-anchor="middle" font-size="13" fill="#30475d">30</text>
  <line x1="405" y1="36" x2="405" y2="188" stroke="#d6dee6" stroke-width="1"/>
  <text x="405" y="27" text-anchor="middle" font-size="13" fill="#30475d">60</text>
  <line x1="555" y1="36" x2="555" y2="188" stroke="#d6dee6" stroke-width="1"/>
  <text x="555" y="27" text-anchor="middle" font-size="13" fill="#30475d">90</text>
  <line x1="605" y1="36" x2="605" y2="188" stroke="#d6dee6" stroke-width="1"/>
  <text x="605" y="27" text-anchor="middle" font-size="13" fill="#30475d">100</text>
  <line x1="705" y1="36" x2="705" y2="188" stroke="#d6dee6" stroke-width="1"/>
  <text x="705" y="27" text-anchor="middle" font-size="13" fill="#30475d">120</text>
  <text x="12" y="81" font-size="15" font-weight="bold" fill="#203d51">タスクA</text>
  <rect x="105" y="58" width="100" height="32" rx="3" fill="#c8d9eb" stroke="#e3ebf0" stroke-width="1"/>
  <text x="155" y="79" text-anchor="middle" font-size="14" fill="#183244">CPU</text>
  <rect x="205" y="58" width="200" height="32" rx="3" fill="#95cdbd" stroke="#e3ebf0" stroke-width="1"/>
  <text x="305" y="79" text-anchor="middle" font-size="14" fill="#183244">資源R</text>
  <rect x="405" y="58" width="150" height="32" rx="3" fill="#c8d9eb" stroke="#e3ebf0" stroke-width="1"/>
  <text x="480" y="79" text-anchor="middle" font-size="14" fill="#183244">CPU</text>
  <text x="12" y="132" font-size="15" font-weight="bold" fill="#203d51">タスクB</text>
  <rect x="105" y="109" width="150" height="32" rx="3" fill="#c8d9eb" stroke="#e3ebf0" stroke-width="1"/>
  <text x="180" y="130" text-anchor="middle" font-size="14" fill="#183244">CPU</text>
  <rect x="255" y="109" width="150" height="32" rx="3" fill="#f1d2a2" stroke="#e3ebf0" stroke-width="1"/>
  <text x="330" y="130" text-anchor="middle" font-size="14" fill="#183244">R待ち</text>
  <rect x="405" y="109" width="200" height="32" rx="3" fill="#95cdbd" stroke="#e3ebf0" stroke-width="1"/>
  <text x="505" y="130" text-anchor="middle" font-size="14" fill="#183244">資源R</text>
  <rect x="605" y="109" width="100" height="32" rx="3" fill="#c8d9eb" stroke="#e3ebf0" stroke-width="1"/>
  <text x="655" y="130" text-anchor="middle" font-size="14" fill="#183244">CPU</text>
  <text x="12" y="179" font-size="15" font-weight="bold" fill="#203d51">資源R</text>
  <rect x="205" y="158" width="200" height="30" rx="3" fill="#95cdbd" stroke="#e3ebf0" stroke-width="1"/>
  <text x="305" y="178" text-anchor="middle" font-size="14" fill="#183244">Aが使用</text>
  <rect x="405" y="158" width="200" height="30" rx="3" fill="#95cdbd" stroke="#e3ebf0" stroke-width="1"/>
  <text x="505" y="178" text-anchor="middle" font-size="14" fill="#183244">Bが使用</text>
  <text x="105" y="214" font-size="13" fill="#30475d">Aは90msで完了、Bは120msで完了 → 全体は120ms</text>
</svg>
</div>

見るポイントは、**Bが30msで資源Rを要求しても、Aが60msまで使っているため30ms待つ**ことです。図の「R待ち」はCPUを使用している時間ではありません。

- **タスクA：** CPU（0〜20ms）→ 資源R（20〜60ms）→ CPU（60〜90ms）→ **90msで完了**
- **タスクB：** CPU（0〜30ms）→ R待ち（30〜60ms）→ 資源R（60〜100ms）→ CPU（100〜120ms）→ **120msで完了**

資源Rの使用区間は、Aが20〜60ms、Bが60〜100msで、重なっていません。

したがって、Bの待ち時間は **60 − 30 = 30ms**、全体の終了時刻は **120ms** です。

### 待ち時間を速く求める方法

タイムチャートを全部描かなくても、次の計算で求められることがあります。

```text
先のタスクが資源を使い終わる時刻
-
後のタスクが資源を要求する時刻
=
待ち時間
```

先ほどの例なら、

```text
60 - 30 = 30ms
```

です。

ただし、結果が0以下なら待ち時間はありません。

このテーマは、OSのタスク管理や排他制御と関係する内容です。公式の出題範囲は、[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html)から確認できます。

## 科目Aでどう出る？

科目Aでは、複数のタスクについて

- CPU使用時間
- 入出力や共有資源の使用時間
- CPUの台数
- 共有資源が排他的かどうか

などが与えられ、全処理が終わるまでの時間を求める問題があります。

### 試験中の判断手順

まず、各タスク単独の処理時間を合計します。

```text
CPU時間
＋
資源使用時間
＋
CPU時間
```

次に、共有資源の取り合いがあるかを確認します。

```text
待ちがなければ
→ 単独処理時間のまま

資源使用が重なれば
→ 後のタスクに待ち時間を追加
```

特に問題文に次の表現があれば注意します。

```text
共通の資源
排他的に使用
同時に開始
CPUが複数台
```

「CPUが複数台だから全部並列」と考えず、**共有資源だけは別に確認する**のがポイントです。

### 最後に見るのは「両方が終わった時刻」

問題が「二つのタスクの処理が完了するまでの時間」を聞いている場合は、早く終わる方ではなく、**最後に終了するタスクの終了時刻**を答えます。

先ほどのタイムチャートでは、AとBの処理時間（待ち時間を除く）は、どちらも90msです。

```text
A終了：20 + 40 + 30 = 90ms
B終了：30 + 40 + 20 + 待ち30 = 120ms

全体終了
→ 120ms
```

Bの待ち時間30msを加え、**最後に終了するBの120ms**を答えます。

## どんな場面で使う？

### 複数タスクの実行時間を求める問題

この考え方は、複数のタスクが並列に動く問題で使います。

特に、途中で共通資源を使う場合は、単純に各処理時間を足すだけでは正しい終了時刻を求められません。

### OSの排他制御を理解する前提

排他的な共有資源の考え方は、ミューテックスやセマフォなどの排他制御を理解する前提にもなります。

まずは、

```text
1つの資源を同時には使えない
→ 後から来た処理は待つ
```

という基本を押さえることが重要です。

### タスクスケジューリングとのつながり

CPUをどのタスクへ割り当てるかという考え方は、[タスクスケジューリング方式とは？](/fe/task-scheduling/)で整理しています。

今回のテーマでは、それに加えて

```text
CPUを使えるか
＋
必要な共有資源を使えるか
```

の両方を確認します。

## よくある誤解・混同

### CPUが2台なら、二つのタスクは最後まで同時に進める

違います。

CPU処理を同時に進められても、1つしかない共有資源を排他的に使う部分では待ち時間が発生します。

```text
CPUは空いている
でも
資源Rは使用中
↓
タスクは待つ
```

### 各タスクの処理時間を足せば全体時間になる

タスクが並列に動く場合、単純に全タスクの時間を足すわけではありません。

一方で、各タスク単独の時間だけを見て「両方同じ時間で終わる」とも限りません。

**共有資源による待ち時間を加味する**必要があります。

### 排他的とは、CPUを一つのタスクしか使えないという意味

排他的なのは、問題文で指定された資源です。

```text
CPUが2台
→ CPUは同時使用可能

資源Rは排他的
→ Rだけは1タスクずつ
```

何が排他的なのかを確認します。

### 待ち時間は資源使用時間と同じになる

必ずしも同じではありません。

後のタスクが資源を要求した時点で、先のタスクがどれだけ資源を使い終えているかによって待ち時間は変わります。

```text
先の資源使用終了時刻 - 後の要求時刻
→ 実際の待ち時間
```

## まとめ（試験直前用）

- CPUが複数台でも、排他的な共有資源は同時に使えない
- 共有資源を後から要求したタスクには待ち時間が発生することがある
- 「資源使用終了時刻 − 後の要求時刻」で待ち時間を求める
- 全体の終了時間は、最後に終了するタスクの時刻を見る
- 迷ったら「CPU」と「共有資源」を別々の時間軸で確認する

{% include fe_article_footer.html %}
