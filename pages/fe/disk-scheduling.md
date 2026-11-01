---
layout: page
title: ディスクスケジューリングとは？FCFS・SSTF・SCAN方式の違い【基本情報技術者試験】
description: 磁気ディスクのヘッド移動を効率化するディスクスケジューリングを、FCFS・SSTF・SCAN方式の違いから整理します。現在位置と移動方向からアクセス順と総移動シリンダ数を判断する方法をFE科目A向けに図解します。
permalink: /fe/disk-scheduling/
tags: [fe, fe-technology, computer-system]
fe_section: テクノロジ系
fe_subsection: コンピュータシステム
fe_order: 52
date: 2026-10-05
last_modified_at: 2026-11-01
---

<style>
.disk-track {
  margin: 1.2rem 0;
  padding: 1rem;
  border: 1px solid #d8dee4;
  border-radius: 10px;
}
.disk-route {
  display: flex;
  align-items: center;
  gap: .35rem;
  flex-wrap: wrap;
  justify-content: center;
  margin: .7rem 0;
}
.disk-point {
  min-width: 3rem;
  padding: .45rem .55rem;
  border: 1px solid #8c959f;
  border-radius: 7px;
  text-align: center;
  background: #f6f8fa;
}
.disk-current {
  font-weight: 700;
  border-width: 2px;
}
.disk-turn {
  font-weight: 700;
}
@media (max-width: 600px) {
  .disk-route { gap: .2rem; }
  .disk-point { min-width: 2.6rem; padding: .4rem; }
}
</style>

## まず結論

ディスクスケジューリングは、**磁気ディスクへの複数のアクセス要求を、ヘッドの移動がなるべく少なくなるように処理する順序を決める仕組み**です。

FE科目Aでは、方式名だけでなく、**「次にヘッドがどこへ動くか」**で切り分けると分かりやすくなります。

| 方式 | 次に処理する要求 | 判断の合図 |
|---|---|---|
| FCFS | 到着した順 | 要求順をそのまま処理 |
| SSTF | 現在位置から最も近い要求 | 一番近いシリンダ |
| SCAN | 現在の方向にある要求を順番に処理 | 一方向に進み、必要なところで折り返す |

このページは**FCFS・SSTF・SCANの方式比較**が中心です。SCAN方式だけを取り出して、要求の処理順やヘッド移動距離を練習したい場合は、[SCAN方式の詳しい解き方](/fe/disk-scheduling-scan/) を参照してください。

## 直感的な説明

SCAN方式は、**エレベータ**をイメージすると理解しやすい方式です。

上へ進んでいる途中なら、上方向の要求を順番に処理します。上方向に処理すべき要求がなくなったら、方向を変えて下へ進みます。

例えば、現在位置が100で、要求が次のようにあるとします。

~~~text
120, 90, 70, 80, 140, 110, 60
~~~

現在はシリンダ番号が増える方向へ移動しているなら、今回の条件では次の順になります。

<div class="disk-track">
  <div class="disk-route">
    <span class="disk-point disk-current">100</span><span>→</span>
    <span class="disk-point">110</span><span>→</span>
    <span class="disk-point">120</span><span>→</span>
    <span class="disk-point disk-turn">140</span>
  </div>
  <div style="text-align:center"><strong>140で方向転換</strong></div>
  <div class="disk-route">
    <span class="disk-point">140</span><span>→</span>
    <span class="disk-point">90</span><span>→</span>
    <span class="disk-point">80</span><span>→</span>
    <span class="disk-point">70</span><span>→</span>
    <span class="disk-point">60</span>
  </div>
</div>

ポイントは、問題文に**要求の並べ替えができる**とあれば、最初に書かれた要求順のまま処理する必要はないことです。


### 触って覚える：同じ要求列でFCFS・SSTF・SCANを比較する

**次にヘッドが移動するシリンダを予想**してから「1要求進める」を押してみましょう。初期位置100、要求列 **120, 90, 70, 80, 140, 110, 60** で3方式を比較します。要求と現在位置を変更しても試せます。

この教材では**全要求が最初から待機している**とし、同じシリンダ番号の要求はまとめて1件扱い、SSTFの距離が同じ場合は**小さいシリンダ番号を優先**します。SCANの例は、本文と同じく「進行方向に要求がなくなったら最後の要求位置で反転する」という**LOOK型の折返し条件**です。ディスクの物理端まで移動する厳密なSCANとは区別してください。移動距離はシリンダ番号の差の絶対値で計算します。

<div id="fe-disk-demo" class="fe-disk-demo">
  <div class="fe-disk-demo__controls">
    <label for="fe-disk-method">方式
      <select id="fe-disk-method">
        <option value="fcfs">FCFS：要求順</option>
        <option value="sstf">SSTF：現在位置から最短</option>
        <option value="scan">SCAN：進行方向優先（最後の要求で反転）</option>
      </select>
    </label>
    <label for="fe-disk-start">初期ヘッド位置（0〜199）
      <input id="fe-disk-start" type="number" min="0" max="199" step="1" value="100">
    </label>
    <label for="fe-disk-direction">SCANの初期方向
      <select id="fe-disk-direction">
        <option value="up">増加方向</option>
        <option value="down">減少方向</option>
      </select>
    </label>
    <label for="fe-disk-requests">要求列（カンマ区切り、0〜199）
      <input id="fe-disk-requests" type="text" value="120,90,70,80,140,110,60">
    </label>
  </div>
  <fieldset class="fe-disk-demo__prediction">
    <legend>予想：次に処理するシリンダ番号は？</legend>
    <label for="fe-disk-guess">番号を入力（0〜199）</label>
    <input id="fe-disk-guess" type="number" min="0" max="199" step="1" placeholder="例：120">
  </fieldset>
  <div class="fe-disk-demo__buttons">
    <button type="button" id="fe-disk-next">1要求進める</button>
    <button type="button" id="fe-disk-prev">1要求戻る</button>
    <button type="button" id="fe-disk-all">最後まで実行</button>
    <button type="button" id="fe-disk-reset">最初から</button>
  </div>
  <p id="fe-disk-feedback" role="status" aria-live="polite">次に移動するシリンダを予想してください。</p>
  <div class="fe-disk-demo__stats" aria-live="polite">
    <div>現在位置<strong id="fe-disk-current">100</strong></div>
    <div>総移動量<strong id="fe-disk-distance">0</strong></div>
    <div>処理済み要求<strong id="fe-disk-count">0 / 7</strong></div>
  </div>
  <div class="fe-disk-demo__scroll" tabindex="0" aria-label="ヘッド移動の履歴、横スクロール可能">
    <div id="fe-disk-route" class="fe-disk-demo__route">開始：100</div>
  </div>
  <p id="fe-disk-pending">未処理：120, 90, 70, 80, 140, 110, 60</p>
  <div class="fe-disk-demo__scroll">
    <table>
      <caption>同じ条件での全方式比較（最後まで実行した場合）</caption>
      <thead><tr><th scope="col">方式</th><th scope="col">処理順</th><th scope="col">総移動量</th></tr></thead>
      <tbody id="fe-disk-comparison"><tr><td colspan="3">JavaScript有効時に比較を表示します。</td></tr></tbody>
    </table>
  </div>
  <p class="fe-disk-demo__note">FCFSは入力順、SSTFは現在位置から最も近い要求、SCAN（この教材ではLOOK型条件）は指定方向を優先します。比較表の総移動量には、開始位置から最初の要求への移動も含みます。入力を変更すると履歴が初期化されます。</p>
</div>
<noscript><p>JavaScriptが無効の場合は、本文のSCAN例を確認してください。開始100・増加方向では 100 → 110 → 120 → 140 → 90 → 80 → 70 → 60 で、総移動量は120です。</p></noscript>

<style>
.fe-disk-demo{border:1px solid #94a3b8;border-radius:12px;padding:1rem;margin:1.2rem 0}
.fe-disk-demo__controls{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.75rem}
.fe-disk-demo__controls label{display:flex;flex-direction:column;gap:.3rem}
.fe-disk-demo input,.fe-disk-demo select{min-height:2.35rem;max-width:100%;min-width:0;box-sizing:border-box;padding:.45rem;border:1px solid #64748b;border-radius:6px;background:var(--background-color,#fff);color:var(--text-color,#172033)}
.fe-disk-demo__prediction{border:1px solid #94a3b8;border-radius:8px;margin:1rem 0;padding:.65rem;display:flex;gap:.5rem;flex-wrap:wrap;align-items:center}
.fe-disk-demo__prediction legend{font-weight:700}
.fe-disk-demo__prediction input{width:6rem}
.fe-disk-demo__buttons{display:flex;gap:.5rem;flex-wrap:wrap}
.fe-disk-demo button{padding:.5rem .75rem;border-radius:6px;border:1px solid #64748b;background:#e2e8f0;color:#172033;cursor:pointer}
.fe-disk-demo button:disabled{opacity:.45;cursor:not-allowed}
.fe-disk-demo__stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.5rem;margin:.85rem 0}
.fe-disk-demo__stats div{border:1px solid #94a3b8;border-radius:8px;padding:.5rem;font-size:.85rem}
.fe-disk-demo__stats strong{display:block;font-size:1.15rem}
.fe-disk-demo__scroll{overflow-x:auto;max-width:100%;margin:.8rem 0}
.fe-disk-demo__route{display:flex;align-items:center;gap:.4rem;min-height:48px;width:max-content;min-width:100%}
.fe-disk-demo__node{padding:.5rem .7rem;border:1px solid #64748b;border-radius:6px;background:#dbeafe;color:#1e3a8a;font-weight:700;white-space:nowrap}
.fe-disk-demo__leg{white-space:nowrap;font-size:.85rem}
.fe-disk-demo table{width:100%;min-width:470px;border-collapse:collapse}
.fe-disk-demo th,.fe-disk-demo td{border:1px solid #94a3b8;padding:.45rem;text-align:left}
.fe-disk-demo__note{font-size:.9rem}
.fe-disk-demo :focus-visible{outline:3px solid #2563eb;outline-offset:2px}
@media(max-width:560px){.fe-disk-demo{padding:.65rem}.fe-disk-demo__controls{grid-template-columns:1fr}.fe-disk-demo__stats{grid-template-columns:1fr}.fe-disk-demo__buttons button{flex:1 1 42%}}
</style>
<script>
(function(){
  "use strict";
  const root=document.getElementById("fe-disk-demo");if(!root)return;
  const $=id=>root.querySelector("#"+id);
  const methods=["fcfs","sstf","scan"],labels=["FCFS","SSTF","SCAN（最後の要求で反転）"];
  let data=null,trace=[],step=0,feedback="";
  function valid(){
    const raw=$("fe-disk-requests").value.trim();
    const parts=raw.split(/[,，\s]+/).filter(Boolean);
    if(!parts.length||parts.length>15)throw new Error("要求は1〜15個入力してください。");
    const nums=parts.map(p=>{
      if(!/^\d+$/.test(p))throw new Error("要求は0〜199の整数で入力してください。");
      const n=Number(p);if(n>199)throw new Error("要求は0〜199の範囲で入力してください。");
      return n;
    });
    if(new Set(nums).size!==nums.length)throw new Error("同じ番号の要求は重複させないでください。");
    const rawStart=$("fe-disk-start").value;
    if(!/^\d+$/.test(rawStart)||Number(rawStart)>199)throw new Error("初期位置は0〜199の整数で入力してください。");
    return {start:Number(rawStart),requests:nums,direction:$("fe-disk-direction").value};
  }
  function route(method,settings){
    const {start,requests,direction}=settings;
    if(method==="fcfs")return requests.slice();
    if(method==="scan"){
      const same=requests.filter(x=>x===start);
      const higher=requests.filter(x=>x>start).sort((a,b)=>a-b);
      const lower=requests.filter(x=>x<start).sort((a,b)=>b-a);
      return direction==="up"?same.concat(higher,lower):same.concat(lower,higher);
    }
    const remaining=requests.slice(),result=[];let current=start;
    while(remaining.length){
      remaining.sort((a,b)=>Math.abs(a-current)-Math.abs(b-current)||a-b);
      current=remaining.shift();result.push(current);
    }
    return result;
  }
  function calc(sequence,start){
    let current=start,total=0;
    for(const point of sequence){total+=Math.abs(point-current);current=point;}
    return total;
  }
  function rebuild(){
    try{
      data=valid();trace=route($("fe-disk-method").value,data);step=0;feedback="次に処理するシリンダを予想してください。";
      const body=$("fe-disk-comparison");body.replaceChildren();
      methods.forEach((method,i)=>{
        const seq=route(method,data),tr=document.createElement("tr");
        [labels[i],data.start+" → "+seq.join(" → "),String(calc(seq,data.start))].forEach(value=>{
          const td=document.createElement("td");td.textContent=value;tr.appendChild(td);
        });body.appendChild(tr);
      });
      $("fe-disk-next").disabled=false;$("fe-disk-all").disabled=false;
      render();
    }catch(error){
      data=null;trace=[];step=0;feedback="入力を確認してください："+error.message;
      $("fe-disk-comparison").replaceChildren();render();
    }
  }
  function render(){
    const current=data?(step?trace[step-1]:data.start):"―";
    const previous=data?[data.start,...trace.slice(0,step)]:[];
    const total=data?calc(trace.slice(0,step),data.start):0;
    $("fe-disk-current").textContent=String(current);
    $("fe-disk-distance").textContent=String(total);
    $("fe-disk-count").textContent=step+" / "+trace.length;
    const routeEl=$("fe-disk-route");routeEl.replaceChildren();
    previous.forEach((p,i)=>{
      if(i){
        const move=document.createElement("span");move.className="fe-disk-demo__leg";
        move.textContent="→ "+Math.abs(p-previous[i-1])+" →";routeEl.appendChild(move);
      }
      const node=document.createElement("span");node.className="fe-disk-demo__node";node.textContent=String(p);
      routeEl.appendChild(node);
    });
    if(!previous.length)routeEl.textContent="有効な要求列を入力してください。";
    $("fe-disk-pending").textContent=data?"未処理："+(trace.slice(step).join(", ")||"なし"):"未処理：入力エラー";
    $("fe-disk-feedback").textContent=feedback;
    $("fe-disk-prev").disabled=step===0;
    $("fe-disk-next").disabled=!data||step>=trace.length;
    $("fe-disk-all").disabled=!data||step>=trace.length;
  }
  $("fe-disk-next").addEventListener("click",()=>{
    if(!data||step>=trace.length)return;
    const guess=$("fe-disk-guess").value.trim(),actual=trace[step];
    const correct=/^\d+$/.test(guess)&&Number(guess)===actual;
    const distance=Math.abs(actual-(step?trace[step-1]:data.start));
    feedback=(guess===""?"":correct?"予想正解！ ":"予想と異なりました。 ")+
      "次の要求は"+actual+"、移動量は"+distance+"です。";
    step++;$("fe-disk-guess").value="";render();
  });
  $("fe-disk-prev").addEventListener("click",()=>{if(step>0)step--;feedback="1要求戻しました。次の要求を予想してください。";render()});
  $("fe-disk-all").addEventListener("click",()=>{step=trace.length;feedback="全要求の処理が終了しました。総移動量を比較してください。";render()});
  $("fe-disk-reset").addEventListener("click",()=>{rebuild()});
  ["fe-disk-method","fe-disk-direction","fe-disk-start","fe-disk-requests"].forEach(id=>$(id).addEventListener("change",rebuild));
  rebuild();
})();
</script>

## 定義・仕組み

### なぜ順番を変えるのか

磁気ディスクでは、目的のトラックへヘッドを移動する時間が必要です。

要求順のままヘッドを何度も往復させるより、近い要求や同じ方向の要求をまとめて処理した方が、ヘッド移動を減らせる場合があります。

ディスクスケジューリングは、このアクセス順を決める考え方です。

### FCFS

FCFS（First Come First Served）は、**要求が到着した順番に処理する方式**です。

~~~text
要求：120 → 90 → 70 → 140
      ↓
その順番のまま処理
~~~

考え方は単純ですが、ヘッドが大きく往復する場合があります。

### SSTF

SSTF（Shortest Seek Time First）は、**現在位置から最も近い要求を優先する方式**です。

例えば現在位置が100なら、90と140では90の方が近いので、90を先に処理します。

> SSTFの合図は **「今いる場所から一番近い」** です。

ただし、遠い位置への要求が長く待たされる可能性があります。

### SCAN

SCAN方式は、**ヘッドを一方向へ動かしながら、その方向にある要求をシリンダ番号順に処理し、条件を満たしたところで方向を反転する方式**です。

エレベータの動きに似ているため、エレベータ方式と説明されることもあります。

ここで注意したいのは、**どこで折り返すかは問題文の条件を読む**ことです。

今回のように、

> 現在の方向に要求がないとき、ヘッドの移動方向を変える

という条件なら、物理的なディスクの端まで行く必要はありません。最後の要求位置で折り返します。

## 総移動シリンダ数の求め方

先ほどの例を計算します。

~~~text
現在位置：100
増加方向の最後の要求：140
減少方向の最後の要求：60
~~~

同じ方向に進んでいる途中の差を一つずつ足す必要はありません。

増加方向は、

~~~text
100 → 140 = 40
~~~

折り返した後は、

~~~text
140 → 60 = 80
~~~

したがって、

~~~text
40 + 80 = 120
~~~

**総移動シリンダ数は120**です。

このように、方向転換が1回なら、

> **現在位置 → 今の方向の端 → 反対方向の端**

と見ると計算を短くできます。

## 科目Aでどう出る？

問題文を読んだら、まず次の順で確認します。

1. **現在のヘッド位置**はどこか
2. **現在の移動方向**はどちらか
3. その方向にある要求を**番号順に並べる**
4. **どの条件で方向転換するか**を確認する
5. 最後に移動距離を計算する

特に、要求が

~~~text
120, 90, 70, 80, 140, 110, 60
~~~

とバラバラに書かれていても、SCAN方式ならこの並びに引っ張られないことが重要です。

## どんな場面で使う？

ディスクスケジューリングは、複数のディスクアクセス要求があるときに、磁気ディスクのヘッド移動を効率化する考え方です。

現在のSSDでは磁気ディスクのような機械的なヘッド移動はありません。したがってFEでは、**HDDなどの磁気ディスクを前提にした仕組み**として考えると整理しやすくなります。

## よくある混同

### 「要求された順番」で処理する？

それはFCFSの考え方です。

SCAN方式では、問題文の条件に従って要求を並べ替えます。

### 「一番近い要求」を選ぶ？

それはSSTFです。

SCANは、近さだけでなく**現在の移動方向**が重要です。

### 必ずディスクの端まで行く？

問題文の条件を確認します。

「現在の方向に要求がなくなったら方向転換」と指定されていれば、その条件に従います。**SCANという名前だけから折返し位置を決めない**ことが大切です。

### SCANとSSTFは同じ？

違います。

~~~text
FCFS → 到着順
SSTF → 今いる位置から近い順
SCAN → 今の移動方向を優先
~~~

この3行で切り分けると、選択肢をかなり絞れます。

## まとめ

FE試験では、方式名を丸暗記するより、**「ヘッドが次にどこへ動くか」**で判断します。

- **FCFS**：要求された順
- **SSTF**：現在位置から最も近い要求
- **SCAN**：現在の方向に進みながら順番に処理し、条件に従って折り返す

SCANの移動量を求める問題では、方向転換が1回なら、

> **現在位置 → 今の方向の端 → 反対方向の端**

と図にすると計算しやすくなります。

{% include fe_article_footer.html %}
