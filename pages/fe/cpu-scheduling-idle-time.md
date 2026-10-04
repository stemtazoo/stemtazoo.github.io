---
layout: page
title: CPUスケジューリングとは？優先度とI/O待ちから遊休時間を求める方法【基本情報技術者試験】
description: CPUスケジューリングを、優先度、実行可能状態、I/O待ち、CPUの遊休時間という観点から整理し、タイムチャート問題の解き方をわかりやすく解説します。
permalink: /fe/cpu-scheduling-idle-time/
tags: [fe, fe-technology, operating-system, scheduling]
fe_section: テクノロジ系
fe_subsection: ソフトウェア
fe_order: 40
date: 2026-07-13
last_modified_at: 2026-10-05
---

## まず結論

CPUスケジューリングとは、**複数のタスクのうち、次にどのタスクへCPUを割り当てるかを決める仕組み**です。

基本情報技術者試験では、次の順で考えると整理しやすくなります。

```text
1. CPUを使えるタスクを確認する
2. その中から優先度が高いタスクを選ぶ
3. I/O待ちのタスクはCPUを使えない
4. CPUを使えるタスクが1つもなければ遊休時間
```

特に大切なのは、**優先度が高くても、I/O待ち中ならCPUは使えない**という点です。

このページでは、**タスクの状態を時系列で追ってCPUの遊休時間を求める計算問題**を中心に扱います。到着順・ラウンドロビン・処理時間順・優先度方式の比較は、[CPUスケジューリング方式とは？](/fe/cpu-scheduling/) を参照してください。

## 直感的な説明

CPUを、1人しかいない作業者だと考えてみます。

複数の仕事が届いていても、作業者が同時に処理できるのは1件だけです。

一方、I/O装置は別の担当者のようなものです。

```text
CPU処理 → CPUが担当する
I/O処理 → 入出力装置が担当する
```

あるタスクがI/O処理をしている間、CPUは別の実行可能なタスクを処理できます。

## 定義・仕組み

タスクは、処理の進行に応じて状態が変わります。

| 状態 | 意味 |
|---|---|
| 実行状態 | 現在CPUを使っている |
| 実行可能状態 | CPUが空けば実行できる |
| 待ち状態 | I/O完了などを待っている |

CPUは、**実行可能状態のタスク**から次に実行するものを選びます。

優先度方式では、実行可能なタスクの中から、優先度が最も高いものを実行します。

```text
優先度が高い
＋
実行可能状態
→ CPUを使える
```

優先度が高くても、I/O待ちなら候補にはなりません。

## 科目Aでどう出る？

科目Aでは、CPU処理とI/O処理が交互に並ぶタスクをタイムチャートにして、CPUの遊休時間などを求めます。

たとえば、3つのタスクが次の処理を行うとします。

| 優先度 | 処理順序 |
|---|---|
| 高 | CPU 3 → I/O 5 → CPU 2 |
| 中 | CPU 2 → I/O 6 → CPU 2 |
| 低 | CPU 1 → I/O 5 → CPU 1 |

CPUの処理順は次のようになります。

```text
0〜3   高のCPU処理
3〜5   中のCPU処理
5〜6   低のCPU処理
6〜8   全タスクがI/O待ち → CPU遊休
8〜10  高のCPU処理
10〜11 全タスクがI/O待ち → CPU遊休
11〜13 中のCPU処理
13〜14 低のCPU処理
```

したがって、CPUの遊休時間は、

```text
6〜8   2ミリ秒
10〜11 1ミリ秒
合計   3ミリ秒
```

となります。

## 優先度とI/Oが同時に出るタイムチャートの解き方

優先度付きの問題では、**「最初に優先度順へ並べて終わり」ではありません**。

I/Oの開始・終了のたびに、CPUを使えるタスクが変わるため、その時点で実行可能なタスクを確認し直します。

例えば、3タスクが同時に実行可能になり、次の条件だったとします。

| タスク | 優先度 | 処理順序 |
|---|---|---|
| A | 高 | CPU 2 → I/O 2 → CPU 2 |
| B | 中 | CPU 3 → I/O 5 → CPU 2 |
| C | 低 | CPU 2 → I/O 2 → CPU 3 |

開始時刻を0として追うと、最初はAがCPUを使います。

<div class="sched-flow">
  <div><b>0〜2</b><span>A：CPU</span><small>B・Cは実行可能状態で待つ</small></div>
  <div><b>2〜4</b><span>A：I/O ／ B：CPU</span><small>AがCPUを手放すのでBを実行</small></div>
  <div><b>4〜6</b><span>A：CPU</span><small>AのI/O完了。AはBより高優先度なのでBを中断</small></div>
  <div><b>6〜7</b><span>B：CPU</span><small>A完了後、Bの残り1msを実行</small></div>
  <div><b>7〜9</b><span>B：I/O ／ C：CPU</span><small>BがI/Oへ進むのでCを実行</small></div>
</div>

ここで重要なのが **4ms時点** です。

```text
B：CPU実行中
A：I/O完了 → 実行可能状態へ戻る

優先度 A > B
        ↓
Bを中断
        ↓
AへCPUを割り当てる
```

つまり、I/Oが終わったタスクは「そのままCPU処理を再開する」のではなく、まず**実行可能状態へ戻ります**。その後、優先度に従ってCPUが割り当てられます。

このように実行中の低優先度タスクからCPUを取り上げ、高優先度タスクへ切り替える動作は、[プリエンプティブスケジューリング](/fe/preemptive-scheduling/)の考え方です。

### CPUとI/Oを別のレーンとして考える

タイムチャート問題では、CPUとI/Oを同じ処理装置だと思わないことが重要です。

<div class="cpu-io-lanes">
  <div class="lane-label">CPU</div>
  <div class="lane-cell">A</div><div class="lane-cell">B</div><div class="lane-cell">A</div><div class="lane-cell">B</div><div class="lane-cell">C</div>
  <div class="lane-label">I/O</div>
  <div class="lane-cell lane-empty">—</div><div class="lane-cell">A</div><div class="lane-cell lane-empty">—</div><div class="lane-cell lane-empty">—</div><div class="lane-cell">B</div>
</div>

```text
CPU中 → CPUを占有する
I/O中 → CPUを手放す
I/O終了 → 実行可能状態へ戻る
高優先度タスクが戻る → 必要なら実行中タスクを中断
```

問題文に**「I/Oは競合しない」**とあれば、I/O装置同士の取り合いは考えません。CPUの割当てとI/Oの進行を分けて追います。

### 試験中は「イベントが起きた時刻」だけ見る

1msごとに全タスクを書き直す必要はありません。次のイベントが起きた時刻だけ確認します。

```text
CPU処理が終了した
I/Oを開始した
I/Oが終了した
タスクが完了した
        ↓
実行可能なタスクを確認
        ↓
最も優先度の高いタスクへCPUを割り当てる
```

この手順なら、長いタイムチャートでも追いやすくなります。

<style>
.sched-flow{display:grid;gap:.65rem;margin:1.2rem 0}
.sched-flow>div{display:grid;grid-template-columns:5rem 1fr;gap:.2rem .8rem;border:1px solid #d6dde2;border-radius:10px;padding:.75rem 1rem;background:#f8fafb}
.sched-flow b{grid-row:1/3}
.sched-flow span{font-weight:600}
.sched-flow small{line-height:1.5}
.cpu-io-lanes{display:grid;grid-template-columns:4rem repeat(5,1fr);gap:.3rem;margin:1.2rem 0;overflow-x:auto}
.lane-label,.lane-cell{min-width:4.5rem;padding:.65rem .4rem;text-align:center;border-radius:7px}
.lane-label{font-weight:700;background:#eef1f3}
.lane-cell{border:1px solid #cbd5da;background:#f8fafb}
.lane-empty{opacity:.55}
@media(max-width:600px){.sched-flow>div{grid-template-columns:4rem 1fr}.cpu-io-lanes{font-size:.9rem}}
</style>

## どんな場面で使う？

複数タスクの実行順を追い、I/O待ちのタスクをCPUの実行候補から除外して、CPUの遊休時間や処理順を求めるタイムチャート問題で使います。

## タイムチャートの書き方

1. 最初に実行可能なタスクを確認する
2. その中から最も優先度が高いものを実行する
3. I/Oに入ったタスクを待ち状態にする
4. 残りの実行可能タスクを探す
5. I/O完了で高優先度タスクが戻ったら、実行中タスクを中断するか確認する
6. 実行可能タスクがなければ遊休時間として記録する

この順番で追えば、複雑な問題でも整理しやすくなります。

## よくある誤解・混同

### 誤解1：優先度が高いタスクは常にCPUを使う

優先度が高くても、I/O待ち中ならCPUは使えません。

### 誤解2：I/O中もCPUを使っている

I/O処理は入出力装置が担当します。その間、CPUは別のタスクを実行できます。

### 誤解3：CPU時間とI/O時間を全部足せばよい

CPU処理とI/O処理は並行して進むため、単純な合計では求められません。

### 誤解4：空白時間をすべて遊休時間と考える

遊休時間は、**CPUを使えるタスクが1つもない時間**です。各タスクが実行可能か待ち状態かを確認します。

## まとめ（試験直前用）

- CPUは、実行可能なタスクの中から次に実行するものを選ぶ
- 優先度方式では、実行可能な中で最も優先度が高いタスクを選ぶ
- I/O待ちのタスクはCPUを使えない
- I/Oが終わったタスクは実行可能状態へ戻る
- 高優先度タスクが戻れば、プリエンプティブ方式では低優先度タスクを中断する
- 全タスクがI/O待ちの時間がCPUの遊休時間
- タイムチャートを書いて、CPU処理とI/O処理を分けて追う

{% include fe_article_footer.html %}
