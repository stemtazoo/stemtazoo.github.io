---
layout: page
title: CPUスケジューリング方式とは？到着順・ラウンドロビン・処理時間順・優先度方式の違い【基本情報技術者試験】
description: CPUスケジューリング方式を、到着順、ラウンドロビン、処理時間順、優先度方式に分けて整理し、I/O中心・CPU中心タスクの組合せ、スループット、スタベーションやエージングとの関係、FE試験での選択肢の切り方を解説します。
permalink: /fe/cpu-scheduling/
tags: [fe, fe-technology, operating-system, scheduling]
fe_section: テクノロジ系
fe_subsection: オペレーティングシステム
fe_order: 50
date: 2026-08-27
last_modified_at: 2026-11-01
related_articles:
  - /fe/task-scheduling/
  - /fe/preemptive-scheduling/
  - /fe/round-robin-scheduling/
  - /fe/shortest-job-first-scheduling/
  - /fe/cpu-scheduling-idle-time/
---

## まず結論

CPUスケジューリングとは、**実行可能な複数のタスクの中から、どのタスクにCPUを割り当てるか、その順番を決める仕組み**です。

基本情報技術者試験では、次の対応で切り分けると判断しやすくなります。

| 方式 | 何を優先する？ | 試験での合図 |
|---|---|---|
| 到着順方式 | 先に来たタスク | 到着した順、FIFO |
| ラウンドロビン方式 | 順番に一定時間ずつ | タイムクォンタム、一定時間で交代 |
| 処理時間順方式 | 処理時間が短いタスク | 短い処理を優先、長いタスクが後回し |
| 優先度方式 | 優先度が高いタスク | 優先順位、優先度 |

さらに、**入出力処理が主体のタスクとCPU処理が主体のタスクを同時に実行し、システム全体のスループットを高める**問題では、次の考え方が重要です。

> **I/O中心のタスクを先に動かしてI/O待ちへ送り、その待ち時間にCPU中心のタスクを動かす。**

こうすると、CPUとI/O装置を並行して働かせやすくなります。

また、**短いタスクを優先し続けた結果、長いタスクがCPUを割り当ててもらえない可能性がある**なら、処理時間順方式を疑います。

> **短いもの優先 → 長いものが後回し → スタベーションに注意**

このページでは、**到着順・ラウンドロビン・処理時間順・優先度方式など、CPUスケジューリング方式全体の比較**を中心に扱います。優先度とI/O待ちをタイムチャートで追い、CPUの遊休時間を求める計算は、[CPUスケジューリングと遊休時間](/fe/cpu-scheduling-idle-time/)で整理しています。 ラウンドロビンの終了時刻計算は[ラウンドロビンスケジューリング](/fe/round-robin-scheduling/)、処理時間順方式は[処理時間順方式](/fe/shortest-job-first-scheduling/)、プリエンプティブ/ノンプリエンプティブの基本は[タスクスケジューリング方式](/fe/task-scheduling/)で確認できます。

## 直感的な説明

CPUを「1つしかない受付窓口」と考えてみます。

複数のタスクが待っているとき、誰から処理するかを決めるのがスケジューリングです。

```text
タスクA
タスクB
タスクC
   ↓
どれを次に実行する？
   ↓
スケジューリング
```

方式によって、順番の決め方が変わります。

```text
先に来た人から
→ 到着順

全員を少しずつ順番に
→ ラウンドロビン

短く終わる人から
→ 処理時間順

重要な人から
→ 優先度方式
```

この違いをイメージできると、方式名を丸暗記しなくても選択肢を切りやすくなります。

### I/O中心とCPU中心は「同時に働かせる」と考える

タスクには、入出力処理が多いものと、CPUによる計算処理が多いものがあります。

```text
I/O中心のタスク
→ 少しCPUを使う
→ I/O待ちになる
→ また少しCPUを使う

CPU中心のタスク
→ CPUを長く使う
```

ここで、I/O中心のタスクを早めに動かしてI/O待ちへ進ませると、その待ち時間にCPU中心のタスクを実行できます。

```text
I/O中心：CPU → I/O待ち ─────→ CPU → I/O待ち
CPU中心：      CPU CPU CPU       CPU CPU CPU
```

つまり、狙いは**CPUを1つのタスクに長く使わせることではなく、CPUとI/O装置の両方をできるだけ遊ばせないこと**です。


### 触って覚える：同じタスクを4方式で比較する

次の3タスクの到着時刻・CPU処理時間・優先度を変更して、**次に動くタスクを予想**しましょう。そのあと「1単位進める」でCPUの動きと待ち時間を確かめます。方式を切り替えても入力条件は保持されます。

この教材ではCPUは1個、各タスクのCPU処理は1回だけ、I/O待ち・切替え時間・エージングは扱いません。FCFS・SJF・優先度は**非プリエンプティブ**（実行中は完了まで継続）、ラウンドロビンだけタイムクォンタムで交代します。**優先度は数字が小さいほど高い**とします。同時刻の到着はA→B→C、同順位では到着時刻→A/B/Cの順で決めます。ラウンドロビンでは、時刻境界で新たに到着したタスクを待ち行列に追加してから、時間切れのタスクを末尾へ戻します。

<div class="fe-cpu-demo" id="fe-cpu-demo">
  <div class="fe-cpu-demo__controls">
    <label>方式
      <select id="fe-cpu-kind">
        <option value="fcfs">到着順（FCFS）</option>
        <option value="sjf">処理時間順（SJF）</option>
        <option value="priority">優先度順</option>
        <option value="rr">ラウンドロビン（RR）</option>
      </select>
    </label>
    <label>タイムクォンタム（RRのみ）
      <select id="fe-cpu-quantum"><option value="1">1</option><option value="2" selected>2</option><option value="3">3</option><option value="4">4</option></select>
    </label>
  </div>
  <div class="fe-cpu-demo__scroll">
    <table>
      <caption>タスクの条件（値を変更できます）</caption>
      <thead><tr><th scope="col">タスク</th><th scope="col">到着時刻</th><th scope="col">CPU処理時間</th><th scope="col">優先度</th></tr></thead>
      <tbody>
        <tr><th scope="row">A</th><td><input aria-label="Aの到着時刻" data-job="0" data-field="arrival" type="number" min="0" max="12" step="1" value="0"></td><td><input aria-label="Aの処理時間" data-job="0" data-field="burst" type="number" min="1" max="12" step="1" value="5"></td><td><input aria-label="Aの優先度" data-job="0" data-field="priority" type="number" min="1" max="9" step="1" value="2"></td></tr>
        <tr><th scope="row">B</th><td><input aria-label="Bの到着時刻" data-job="1" data-field="arrival" type="number" min="0" max="12" step="1" value="1"></td><td><input aria-label="Bの処理時間" data-job="1" data-field="burst" type="number" min="1" max="12" step="1" value="2"></td><td><input aria-label="Bの優先度" data-job="1" data-field="priority" type="number" min="1" max="9" step="1" value="1"></td></tr>
        <tr><th scope="row">C</th><td><input aria-label="Cの到着時刻" data-job="2" data-field="arrival" type="number" min="0" max="12" step="1" value="2"></td><td><input aria-label="Cの処理時間" data-job="2" data-field="burst" type="number" min="1" max="12" step="1" value="3"></td><td><input aria-label="Cの優先度" data-job="2" data-field="priority" type="number" min="1" max="9" step="1" value="3"></td></tr>
      </tbody>
    </table>
  </div>
  <fieldset class="fe-cpu-demo__predict">
    <legend>予想：次の1単位でCPUを使うのは？</legend>
    <label><input type="radio" name="fe-cpu-prediction" value="A">A</label>
    <label><input type="radio" name="fe-cpu-prediction" value="B">B</label>
    <label><input type="radio" name="fe-cpu-prediction" value="C">C</label>
    <label><input type="radio" name="fe-cpu-prediction" value="-">待機</label>
  </fieldset>
  <div class="fe-cpu-demo__buttons">
    <button type="button" id="fe-cpu-next">1単位進める</button>
    <button type="button" id="fe-cpu-prev">1単位戻る</button>
    <button type="button" id="fe-cpu-reset">最初から</button>
    <button type="button" id="fe-cpu-all">最後まで実行</button>
  </div>
  <p id="fe-cpu-status" role="status" aria-live="polite">初期状態：実行するタスクを予想してください。</p>
  <p id="fe-cpu-feedback" aria-live="polite">予想を選択してから進めると、答え合わせができます。</p>
  <div class="fe-cpu-demo__scroll" tabindex="0" aria-label="CPU実行ガントチャート（横スクロール可）">
    <div id="fe-cpu-timeline" class="fe-cpu-demo__timeline" aria-label="ガントチャート">まだ実行していません。</div>
  </div>
  <div id="fe-cpu-remaining">残りCPU時間：A=5、B=2、C=3</div>
  <div class="fe-cpu-demo__scroll">
    <table>
      <caption>各方式を最後まで実行した場合の比較（入力を変えると更新）</caption>
      <thead><tr><th scope="col">方式</th><th scope="col">平均待ち時間</th><th scope="col">平均ターンアラウンド時間</th></tr></thead>
      <tbody id="fe-cpu-comparison"><tr><td colspan="3">JavaScript有効時に結果を表示します。</td></tr></tbody>
    </table>
  </div>
  <p class="fe-cpu-demo__note">待ち時間 = 完了時刻 − 到着時刻 − CPU処理時間。ターンアラウンド時間 = 完了時刻 − 到着時刻。方式を変更したときは操作履歴が初期化されます。各方式を比較するための教育用モデルであり、実際のOSの全機能は再現しません。</p>
</div>

<style>
.fe-cpu-demo{border:1px solid #94a3b8;border-radius:12px;padding:1rem;margin:1rem 0}
.fe-cpu-demo__controls{display:flex;gap:1rem;flex-wrap:wrap}
.fe-cpu-demo__controls label{display:flex;flex-direction:column;gap:.3rem;flex:1 1 180px}
.fe-cpu-demo select,.fe-cpu-demo input[type=number]{max-width:100%;min-height:2.3rem;border:1px solid #64748b;border-radius:6px;background:var(--background-color,#fff);color:var(--text-color,#172033);padding:.3rem}
.fe-cpu-demo input[type=number]{width:4.3rem;box-sizing:border-box}
.fe-cpu-demo__scroll{max-width:100%;overflow-x:auto;margin:.75rem 0}
.fe-cpu-demo table{width:100%;min-width:410px;border-collapse:collapse}
.fe-cpu-demo th,.fe-cpu-demo td{padding:.4rem;border:1px solid #94a3b8;text-align:center}
.fe-cpu-demo__predict{display:flex;gap:.8rem;flex-wrap:wrap;border:1px solid #94a3b8;border-radius:6px;margin:1rem 0;padding:.6rem}
.fe-cpu-demo__predict legend{font-weight:700}
.fe-cpu-demo__predict label{white-space:nowrap}
.fe-cpu-demo__buttons{display:flex;gap:.5rem;flex-wrap:wrap}
.fe-cpu-demo button{border:1px solid #64748b;border-radius:6px;background:#e2e8f0;color:#172033;padding:.5rem .75rem;cursor:pointer}
.fe-cpu-demo button:disabled{opacity:.45;cursor:not-allowed}
.fe-cpu-demo__timeline{display:flex;min-height:55px;align-items:stretch;width:max-content;min-width:100%}
.fe-cpu-demo__slot{width:42px;flex:0 0 42px;text-align:center;background:#dbeafe;color:#1e3a8a;border:1px solid #64748b;padding:.3rem 0;box-sizing:border-box;font-weight:700}
.fe-cpu-demo__slot small{display:block;font-size:.7rem;font-weight:400}
.fe-cpu-demo__slot[data-task="B"]{background:#dcfce7;color:#14532d}
.fe-cpu-demo__slot[data-task="C"]{background:#ffedd5;color:#9a3412}
.fe-cpu-demo__slot[data-task="-"]{background:#e2e8f0;color:#334155}
.fe-cpu-demo__note{font-size:.9rem}
.fe-cpu-demo :focus-visible{outline:3px solid #2563eb;outline-offset:2px}
@media(max-width:560px){.fe-cpu-demo{padding:.65rem}.fe-cpu-demo__buttons button{flex:1 1 43%}}
</style>
<script>
(function(){
  "use strict";
  const root=document.getElementById("fe-cpu-demo");
  if(!root)return;
  const $=id=>root.querySelector("#"+id);
  const kind=$("fe-cpu-kind"),quantum=$("fe-cpu-quantum");
  const next=$("fe-cpu-next"),prev=$("fe-cpu-prev"),reset=$("fe-cpu-reset"),all=$("fe-cpu-all");
  const names=["A","B","C"];
  let trace=[],step=0,feedback="";
  function jobs(){
    const fields=[...root.querySelectorAll("input[data-job]")];
    const result=names.map((name,id)=>({name,id,arrival:0,burst:1,priority:1}));
    for(const field of fields){
      const min=Number(field.min),max=Number(field.max);
      let value=Number(field.value);
      if(!Number.isFinite(value))value=min;
      value=Math.max(min,Math.min(max,Math.trunc(value)));
      field.value=String(value);
      result[Number(field.dataset.job)][field.dataset.field]=value;
    }
    return result;
  }
  function simulate(tasks,method,q){
    const remaining=tasks.map(t=>t.burst),finish=tasks.map(()=>null);
    const total=remaining.reduce((a,b)=>a+b,0);
    const limit=total+Math.max(...tasks.map(t=>t.arrival))+1;
    let time=0,running=-1,used=0,queue=[],queued=new Set();
    const slots=[];
    function enqueueArrivals(t){
      tasks.filter(j=>j.arrival===t&&remaining[j.id]>0&&!queued.has(j.id)&&j.id!==running)
        .sort((a,b)=>a.id-b.id).forEach(j=>{queue.push(j.id);queued.add(j.id)});
    }
    for(;time<limit && remaining.some(n=>n>0);time++){
      enqueueArrivals(time);
      if(method==="rr"){
        if(running!==-1 && used>=q){
          queue.push(running);queued.add(running);running=-1;used=0;
        }
        if(running===-1&&queue.length){running=queue.shift();queued.delete(running);used=0;}
      }else if(running===-1){
        const eligible=tasks.filter(j=>j.arrival<=time&&remaining[j.id]>0);
        eligible.sort((a,b)=>{
          if(method==="sjf")return a.burst-b.burst||a.arrival-b.arrival||a.id-b.id;
          if(method==="priority")return a.priority-b.priority||a.arrival-b.arrival||a.id-b.id;
          return a.arrival-b.arrival||a.id-b.id;
        });
        running=eligible.length?eligible[0].id:-1;
      }
      const current=running;
      slots.push(current===-1?"-":names[current]);
      if(current!==-1){
        remaining[current]--;used++;
        if(remaining[current]===0){finish[current]=time+1;running=-1;used=0;}
      }
    }
    const avgWait=tasks.reduce((sum,j)=>sum+finish[j.id]-j.arrival-j.burst,0)/tasks.length;
    const avgTurn=tasks.reduce((sum,j)=>sum+finish[j.id]-j.arrival,0)/tasks.length;
    return {slots,avgWait,avgTurn,finish};
  }
  function rebuild(){
    const tasks=jobs(),q=Number(quantum.value);
    trace=simulate(tasks,kind.value,q).slots;step=0;feedback="";
    const keys=["fcfs","sjf","priority","rr"];
    const labels=["到着順","処理時間順","優先度順","ラウンドロビン"];
    const tbody=$("fe-cpu-comparison");tbody.replaceChildren();
    keys.forEach((key,index)=>{
      const result=simulate(tasks,key,q),tr=document.createElement("tr");
      [labels[index],result.avgWait.toFixed(2),result.avgTurn.toFixed(2)].forEach(value=>{
        const td=document.createElement("td");td.textContent=value;tr.appendChild(td);
      });tbody.appendChild(tr);
    });
    render();
  }
  function render(){
    const tasks=jobs(),remaining=tasks.map(j=>j.burst);
    trace.slice(0,step).forEach(name=>{const id=names.indexOf(name);if(id>=0)remaining[id]--});
    const timeline=$("fe-cpu-timeline");timeline.replaceChildren();
    if(!step)timeline.textContent="まだ実行していません。";
    trace.slice(0,step).forEach((name,index)=>{
      const cell=document.createElement("div");cell.className="fe-cpu-demo__slot";cell.dataset.task=name;
      cell.textContent=name==="-"?"待機":name;
      const mark=document.createElement("small");mark.textContent=index+"–"+(index+1);cell.appendChild(mark);
      timeline.appendChild(cell);
    });
    $("fe-cpu-remaining").textContent="残りCPU時間："+names.map((n,i)=>n+"="+remaining[i]).join("、");
    $("fe-cpu-status").textContent=step===trace.length?"完了：時刻"+step+"。全タスクが終了しました。":"時刻"+step+"：次に実行するタスクを予想してください。";
    $("fe-cpu-feedback").textContent=feedback||"予想を選択してから進めると、答え合わせができます。";
    prev.disabled=step===0;next.disabled=step===trace.length;all.disabled=step===trace.length;
    quantum.disabled=false;
  }
  next.addEventListener("click",()=>{
    if(step===trace.length)return;
    const selected=root.querySelector('input[name="fe-cpu-prediction"]:checked');
    const actual=trace[step];
    feedback=selected?(selected.value===actual?"正解！":"予想と違いました。")+" 時刻"+step+"で実行したのは"+(actual==="-"?"待機":actual)+"です。":"時刻"+step+"で実行したのは"+(actual==="-"?"待機":actual)+"です。次は先に予想してみましょう。";
    step++;root.querySelectorAll('input[name="fe-cpu-prediction"]').forEach(r=>r.checked=false);render();
  });
  prev.addEventListener("click",()=>{if(step>0)step--;feedback="1単位戻しました。次を予想してください。";render();});
  reset.addEventListener("click",()=>{step=0;feedback="初期状態に戻しました。";render();});
  all.addEventListener("click",()=>{step=trace.length;feedback="全タスクの実行が終了しました。方式を変えて比較しましょう。";render();});
  kind.addEventListener("change",rebuild);
  quantum.addEventListener("change",rebuild);
  root.querySelectorAll("input[data-job]").forEach(field=>field.addEventListener("change",rebuild));
  rebuild();
})();
</script>

## 定義・仕組み

### 到着順方式

到着順方式は、**実行可能待ち行列に入った順番でCPUを割り当てる方式**です。

FCFS（First Come, First Served）とも呼ばれます。

```text
Aが到着
↓
Bが到着
↓
Cが到着

実行順：A → B → C
```

先に来たタスクから順番に処理するため、後から来たタスクが先に追い越すことは基本的にありません。

### ラウンドロビン方式

ラウンドロビン方式は、**各タスクに一定時間ずつCPUを割り当て、時間を使い切ったら待ち行列の最後に回す方式**です。

```text
A → B → C → A → B → C → …
```

1回に使えるCPU時間を **タイムクォンタム** と呼びます。

1つのタスクが長時間CPUを占有しにくいため、複数タスクへ比較的公平にCPUを割り当てられます。

### 処理時間順方式

処理時間順方式は、**予定される処理時間が短いタスクから優先して実行する方式**です。

SJF（Shortest Job First）と呼ばれる考え方に近いものです。

例えば、次のタスクが待っているとします。

| タスク | 処理時間 |
|---|---:|
| A | 10 |
| B | 2 |
| C | 3 |

短い順に実行するなら、

```text
B → C → A
```

となります。

平均待ち時間を短くしやすい一方、短いタスクが次々と入ってくると、長いタスクが後回しになり続けることがあります。

### 優先度方式

優先度方式は、**タスクごとに設定された優先度に従ってCPUを割り当てる方式**です。

```text
高優先度
↓
低優先度
```

高優先度タスクを早く処理できる一方、低優先度タスクが長時間待たされる可能性があります。

この問題を軽減するため、待ち時間が長くなるほど優先度を上げる考え方があります。

これを **エージング（aging）** と呼びます。

### I/O-bound と CPU-bound

入出力処理が主体のタスクは **I/O-bound task**、CPUによる演算処理が主体のタスクは **CPU-bound task** と呼ばれます。

| タスクの性質 | 特徴 | CPUスケジューリングでの見方 |
|---|---|---|
| I/O-bound | CPUを使う時間が短く、I/O待ちが多い | 早めにCPUを使わせてI/O待ちへ進ませたい |
| CPU-bound | CPUを長く使う | I/O-boundが待っている間にCPUを使わせたい |

I/O-boundを先に動かすと、次のようにCPU処理とI/O処理を重ねやすくなります。

```text
I/O-boundを実行
↓
I/O待ちへ進む
↓
その間にCPU-boundを実行
↓
CPUとI/O装置を並行利用
↓
システム全体の処理量を増やしやすい
```

このテーマは、基本情報技術者試験の「オペレーティングシステム」「タスク管理」と関係します。公式の出題範囲やシラバスは、[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html) から確認できます。

## 科目Aでどう出る？

科目Aでは、方式名そのものだけでなく、**どのタスクが待ち続ける可能性があるか**、**一定時間でCPUを交代するか**、**CPUとI/O装置をどう並行して働かせるか**といった特徴から方式を選ぶ問題が出ます。

次の判断表が使いやすいです。

| 問題文の表現 | 第一候補 |
|---|---|
| 到着した順に実行する | 到着順方式 |
| 一定時間ごとに実行を中断し、待ち行列の最後へ回す | ラウンドロビン方式 |
| 予定処理時間が短いタスクを優先する | 処理時間順方式 |
| 優先度の高いタスクを先に実行する | 優先度方式 |
| 待ち時間に応じて優先度を上げる | エージングを使う優先度方式 |
| I/O主体とCPU主体を同時に実行し、スループットを高める | I/O主体を先に動かし、I/O待ち中にCPU主体を実行 |

### I/O主体とCPU主体が出たらどう考える？

例えば、次の2種類のタスクがあるとします。

```text
タスクA：入出力処理が主体
タスクB：CPU処理が主体
```

スループットを高めたいなら、タスクAを早めにCPUで処理して、I/O待ちへ進ませます。

```text
Aを優先してCPUで少し処理
↓
AがI/O待ちになる
↓
その間にBがCPUを使用
```

このとき、優先度方式を使うなら、基本的な判断は次の通りです。

```text
I/O主体のA：高優先度
CPU主体のB：低優先度
```

ここで重要なのは、**Aを長時間CPUで処理したいから高優先度にするのではない**ということです。

Aは早くI/O待ちへ送り出すために先に動かします。その後、AがI/Oしている間にBがCPUを使えるため、CPUとI/O装置を同時に働かせやすくなります。

> **I/O主体を先に動かしてI/O待ちへ送り、待っている間にCPU主体を動かす。**

### 「待ち続ける可能性が高い」をどう読む？

処理時間順方式では、長いタスクより短いタスクを優先します。

```text
長いタスクAが待っている
↓
短いタスクBが到着
→ Bを先に実行
↓
短いタスクCが到着
→ Cを先に実行
↓
Aがさらに後回し
```

このように、新しい短いタスクが入り続ければ、長いタスクAはCPUを割り当ててもらえない可能性があります。

この状態を **スタベーション（starvation、飢餓状態）** と呼びます。

## どんな場面で使う？

OSは、複数のタスクを効率よく実行するためにスケジューリングを行います。

目的によって、重視する点が変わります。

| 重視したいこと | 向いている考え方 |
|---|---|
| 先着順の分かりやすさ | 到着順方式 |
| 公平にCPU時間を分ける | ラウンドロビン方式 |
| 平均待ち時間を短くしたい | 処理時間順方式 |
| 重要処理を優先したい | 優先度方式 |
| CPUとI/O装置を並行して働かせたい | I/O-boundを早めにI/O待ちへ進ませる |

実際のOSでは、これらを単純に1つだけ使うのではなく、目的に応じて複数の考え方を組み合わせることがあります。

FEでは、実装の細部よりも、**各方式が何を優先するか**、そして**CPUやI/O装置の遊休時間をどう減らすか**を押さえることが大切です。

システム全体で単位時間当たりの処理量を見る場合は、[スループットとは？処理件数・応答時間との違い](/fe/throughput/)も合わせて確認すると、今回の「なぜCPUとI/Oを並行させるのか」がつながります。

## よくある誤解・混同

### I/O中心タスクには長いタイムクォンタムを与えればよい

そうとは限りません。

I/O中心タスクは、もともとCPUを長時間使い続けるタスクではありません。

狙いは、**CPUを長く占有させることではなく、早めにI/O待ちへ進ませること**です。

```text
I/O中心だから長時間CPUを使わせる
→ ×

I/O中心を先に動かしてI/O待ちへ送る
→ ○
```

### CPU中心タスクの優先度を上げればスループットも上がる

必ずしもそうではありません。

CPU中心タスクがCPUを使い続けると、I/O中心タスクがI/O処理へ進めず、I/O装置が遊んでしまうことがあります。

```text
CPUだけ忙しい
I/O装置は待機
```

よりも、

```text
CPUはCPU-boundを処理
I/O装置はI/O-boundを処理
```

と並行して働ける状態を作る方が、システム全体の処理量を高めやすくなります。

### 処理時間順方式なら全タスクが早く終わる

そうとは限りません。

短いタスクを先に処理するため、平均待ち時間は短くしやすいですが、長いタスクは後回しになる可能性があります。

```text
平均的には効率がよい
≠
全タスクに公平
```

### ラウンドロビンは到着順と同じ

最初は到着順で待ち行列に入ることがありますが、ラウンドロビンでは一定時間ごとにCPUを交代します。

```text
到着順
→ 原則、先に来たタスクをそのまま処理

ラウンドロビン
→ 一定時間で交代し、末尾へ回す
```

### 優先度方式なら低優先度タスクは必ず実行されない

必ずではありません。

ただし、高優先度タスクが次々と現れると低優先度タスクが待たされる可能性があります。

その対策の一つがエージングです。

```text
長く待つ
↓
優先度を少しずつ上げる
↓
いずれ実行されやすくする
```

### スタベーションとデッドロックは同じ

違います。

| 用語 | 状態 |
|---|---|
| スタベーション | 他のタスクが優先され続け、自分にCPUが回ってこない |
| デッドロック | 複数の処理が互いの資源解放を待ち、誰も進めない |

スタベーションは **「自分だけ進めない」**、デッドロックは **「互いに待って進めない」** と整理すると分かりやすいです。

デッドロックとの違いをもう少し整理したい場合は、[デッドロックとは？ロック待ち・排他制御との違い](/fe/deadlock/)も合わせて読むと、待ち状態の違いがつながります。

### スケジューリングとディスパッチは同じ

役割が違います。

```text
次に誰を実行するか決める
→ スケジューリング

決まったタスクへCPUを渡す
→ ディスパッチ
```

この違いを整理したい場合は、[タスクのディスパッチとは？実行可能なタスクへCPUを割り当てる仕組み](/fe/task-dispatch/)を読むと、OS内部の流れが理解しやすくなります。

また、CPUを強制的に取り上げて別タスクへ切り替える仕組みまで理解したい場合は、[プリエンプティブスケジューリングとは？優先度とタスク状態の切り替わり](/fe/preemptive-scheduling/)へ進むと、今回の内容を一段深く理解できます。

## まとめ（試験直前用）

- CPUスケジューリングは、次にどのタスクへCPUを割り当てるかを決める仕組み
- 到着順方式は、先に来たタスクから実行する
- ラウンドロビン方式は、一定時間ずつ順番にCPUを割り当てる
- 処理時間順方式は、短いタスクを優先し、長いタスクが後回しになることがある
- 優先度方式は、高優先度タスクを先に実行する
- I/O主体とCPU主体の組合せでは、**I/O主体を先に動かしてI/O待ちへ送り、その間にCPU主体を動かす**
- CPUとI/O装置を並行して働かせると、スループットを高めやすい
- 長く待つタスクの優先度を上げる考え方がエージング
- **短いタスクが優先され続け、長いタスクが待ち続ける → スタベーション**

{% include fe_article_footer.html %}
