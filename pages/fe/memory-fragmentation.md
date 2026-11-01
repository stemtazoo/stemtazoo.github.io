---
layout: page
title: フラグメンテーションとは？内部・外部とメモリコンパクションの違い【基本情報技術者試験】
description: メモリの内部フラグメンテーションと外部フラグメンテーションの違い、外部断片化を改善するメモリコンパクション、ページングとの関係をFE試験向けに整理します。
permalink: /fe/memory-fragmentation/
tags: [fe, fe-technology, computer-system]
fe_section: テクノロジ系
fe_subsection: コンピュータシステム
fe_order: 230
date: 2026-10-07
last_modified_at: 2026-11-01
related_articles:
  - /fe/memory-management-methods/
  - /fe/variable-partition-memory-allocation/
  - /fe/memory-compaction/
  - /fe/paging/
  - /fe/memory-leak/
---

## まず結論

フラグメンテーションは、**メモリを使う過程で無駄な領域が生じる現象**です。

FEでは、まず次の2種類を区別します。

```text
内部フラグメンテーション
→ 確保した領域の「中」に無駄ができる

外部フラグメンテーション
→ 確保した領域の「間」に細かな空きができる
```

そして、**外部フラグメンテーションで散らばった空き領域をまとめる操作がメモリコンパクション**です。

主記憶をどう分けて割り当てるかは[主記憶管理方式の全体像](/fe/memory-management-methods/)で確認できます。外部断片化を理解したら、[コンパクションの移動時間計算](/fe/memory-compaction/)へ進むと、現象と処理コストをつなげられます。

## 直感的な説明

外部フラグメンテーションは、空いている席がたくさんあるのに、まとまった席がない状態に似ています。

```text
使用中 | 空き | 使用中 | 空き | 使用中 | 空き
         2MB            3MB            4MB

空きは合計9MB
でも9MB連続した場所はない
```

そこで、使用中の領域を移動して詰めます。

```text
使用中 | 使用中 | 使用中 |        空き 9MB
                            ↑
                    コンパクション後
```

つまり、

```text
散らばった空きを
→ 詰めて
→ 大きな連続した空きにする
= メモリコンパクション
```

と考えると覚えやすくなります。


### 触って覚える：空きの合計と最大の連続領域を比べる

**予想 → 操作 → 結果** の順で確認しましょう。まず「断片化した例」で **60KBの割当てに成功するか**を予想し、「60KBを確保」で試してください。失敗したら、空き容量の合計と最大の連続空き領域を見比べ、「コンパクション」を押してもう一度試します。

この教材は **200KBの連続領域を使う可変長割当て**をモデル化します。先頭から最初に入る空き領域を使う *first-fit* 方式で、新規確保はD→E→Fの順に行います。解放した領域の両隣が空いていれば結合します。移動できるメモリを前提とし、コンパクションで使用中領域を左に詰めます。実際のOSによるアドレスの付け替えや移動時間は扱いません。

<div id="fe-fragment-demo" class="fe-fragment-demo">
  <label for="fe-fragment-case">初期状態を選ぶ</label>
  <select id="fe-fragment-case">
    <option value="fragmented">断片化した例（60KBを確保できる？）</option>
    <option value="packed">最初から順に確保する例</option>
  </select>
  <p class="fe-fragment-demo__hint">色付き：使用中の領域、灰色：空き領域。横幅は容量に比例します。</p>
  <div id="fe-fragment-memory" class="fe-fragment-demo__memory" aria-label="主記憶の配置"></div>
  <div class="fe-fragment-demo__stats" aria-live="polite">
    <div>空きの合計<strong id="fe-fragment-total">―</strong></div>
    <div>最大の連続空き<strong id="fe-fragment-largest">―</strong></div>
    <div>空き領域の数<strong id="fe-fragment-holes">―</strong></div>
  </div>
  <label for="fe-fragment-size">次に確保するサイズ（KB）</label>
  <input id="fe-fragment-size" type="number" min="1" max="200" step="1" value="60">
  <fieldset class="fe-fragment-demo__prediction">
    <legend>予想：このサイズを連続して確保できる？</legend>
    <label><input type="radio" name="fe-fragment-guess" value="yes">できる</label>
    <label><input type="radio" name="fe-fragment-guess" value="no">できない</label>
  </fieldset>
  <div class="fe-fragment-demo__buttons">
    <button type="button" id="fe-fragment-allocate">確保する</button>
    <button type="button" id="fe-fragment-compact">コンパクション</button>
    <button type="button" id="fe-fragment-reset">最初から</button>
  </div>
  <p id="fe-fragment-result" role="status" aria-live="polite">最初に確保できるか予想してください。</p>
  <p id="fe-fragment-reason" aria-live="polite">確保には連続した空きが必要です。</p>
  <div class="fe-fragment-demo__buttons" id="fe-fragment-release" aria-label="使用中の領域を解放する"></div>
  <p class="fe-fragment-demo__hint">使用中の領域は「解放」ボタンで空けられます。最大の連続空きが、確保したいサイズ以上であることを確認しましょう。最初からやり直すときは「最初から」を押します。</p>
  <div class="fe-fragment-demo__internal">
    <h4>内部フラグメンテーションは別の現象</h4>
    <label for="fe-fragment-needed">必要なサイズ（KB）</label>
    <input id="fe-fragment-needed" type="number" min="1" max="32" step="1" value="5">
    <label for="fe-fragment-unit">割当て単位（KB）</label>
    <select id="fe-fragment-unit"><option value="4">4</option><option value="8" selected>8</option><option value="16">16</option></select>
    <p id="fe-fragment-internal-result" aria-live="polite">必要5KBを8KB単位で確保すると3KB余ります。</p>
    <div id="fe-fragment-internal-bar" class="fe-fragment-demo__internal-bar" aria-label="確保領域内部の使用部分と余り"></div>
    <p class="fe-fragment-demo__hint">この余りは確保した領域の「内部」にあります。コンパクションでは取り除けません。固定単位で切り上げる簡易モデルです。</p>
  </div>
</div>
<noscript><p>操作機能はJavaScriptが必要です。JavaScriptが使えない場合は、本文の「空き合計9MBでも9MB連続していない」例と、内部フラグメンテーションの「3KBを4KBで確保して1KB余る」例で違いを確認できます。</p></noscript>

<style>
.fe-fragment-demo{border:1px solid #94a3b8;border-radius:12px;padding:1rem;margin:1.2rem 0}
.fe-fragment-demo select,.fe-fragment-demo input[type=number]{display:block;max-width:100%;padding:.45rem;margin:.4rem 0 .9rem;border:1px solid #64748b;border-radius:6px;background:var(--background-color,#fff);color:var(--text-color,#172033)}
.fe-fragment-demo input[type=number]{width:7rem}
.fe-fragment-demo__hint{font-size:.9rem}
.fe-fragment-demo__memory{display:flex;min-height:74px;border:1px solid #64748b;margin:.75rem 0;width:100%;overflow:hidden}
.fe-fragment-demo__block{display:flex;flex-direction:column;justify-content:center;align-items:center;min-width:0;box-sizing:border-box;border-right:1px solid #64748b;background:#bfdbfe;color:#172554;font-size:.8rem;overflow:hidden}
.fe-fragment-demo__block[data-free=true]{background:#e2e8f0;color:#334155}
.fe-fragment-demo__block span{white-space:nowrap}
.fe-fragment-demo__stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.5rem;margin:.8rem 0}
.fe-fragment-demo__stats div{border:1px solid #94a3b8;border-radius:8px;padding:.5rem;font-size:.85rem}
.fe-fragment-demo__stats strong{display:block;font-size:1.2rem}
.fe-fragment-demo__prediction{display:flex;gap:1rem;flex-wrap:wrap;padding:.65rem;border:1px solid #94a3b8;border-radius:8px}
.fe-fragment-demo__prediction legend{font-weight:700}
.fe-fragment-demo__buttons{display:flex;gap:.45rem;flex-wrap:wrap;margin:.7rem 0}
.fe-fragment-demo button{border:1px solid #64748b;border-radius:6px;background:#e2e8f0;color:#172033;padding:.5rem .75rem;cursor:pointer}
.fe-fragment-demo button:disabled{opacity:.45;cursor:not-allowed}
.fe-fragment-demo__internal{margin-top:1.5rem;border-top:1px solid #94a3b8;padding-top:.75rem}
.fe-fragment-demo__internal h4{margin:.3rem 0 .75rem}
.fe-fragment-demo__internal-bar{display:flex;min-height:35px;border:1px solid #64748b;width:100%;max-width:430px}
.fe-fragment-demo__internal-bar div{display:grid;place-items:center;box-sizing:border-box;padding:.25rem;font-size:.8rem}
.fe-fragment-demo__used{background:#bfdbfe;color:#172554}
.fe-fragment-demo__unused{background:#fde68a;color:#78350f}
.fe-fragment-demo :focus-visible{outline:3px solid #2563eb;outline-offset:2px}
@media(max-width:560px){.fe-fragment-demo{padding:.65rem}.fe-fragment-demo__stats{grid-template-columns:1fr}.fe-fragment-demo__block{font-size:.65rem}.fe-fragment-demo__buttons button{flex:1 1 42%}}
</style>
<script>
(function(){
  "use strict";
  const root=document.getElementById("fe-fragment-demo");if(!root)return;
  const $=id=>root.querySelector("#"+id);
  const presets={
    fragmented:[{id:"A",size:40},{id:null,size:30},{id:"B",size:40},{id:null,size:30},{id:"C",size:40},{id:null,size:20}],
    packed:[{id:null,size:200}]
  };
  let blocks=[],nextId=0;
  const totalSize=200;
  function stats(){
    const free=blocks.filter(b=>!b.id).map(b=>b.size);
    return {total:free.reduce((a,b)=>a+b,0),largest:Math.max(0,...free),holes:free.length};
  }
  function normalize(){
    const merged=[];
    for(const b of blocks){
      const last=merged[merged.length-1];
      if(!b.id&&last&&!last.id)last.size+=b.size;
      else merged.push({...b});
    }
    blocks=merged;
  }
  function reset(){
    blocks=presets[$("fe-fragment-case").value].map(b=>({...b}));nextId=0;
    $("fe-fragment-result").textContent="初期状態に戻しました。";
    $("fe-fragment-reason").textContent="まず空きの合計と最大の連続空きを比べてください。";
    root.querySelectorAll('input[name="fe-fragment-guess"]').forEach(r=>r.checked=false);
    render();
  }
  function render(){
    const memory=$("fe-fragment-memory");memory.replaceChildren();
    for(const b of blocks){
      const element=document.createElement("div");
      element.className="fe-fragment-demo__block";
      element.dataset.free=String(!b.id);
      element.style.flex="0 0 "+(100*b.size/totalSize)+"%";
      element.setAttribute("aria-label",(b.id||"空き")+" "+b.size+"KB");
      if(b.size>=15){
        const name=document.createElement("strong"),size=document.createElement("span");
        name.textContent=b.id||"空き";size.textContent=b.size+"KB";
        element.append(name,size);
      }else{element.title=(b.id||"空き")+" "+b.size+"KB";}
      memory.appendChild(element);
    }
    const s=stats();
    $("fe-fragment-total").textContent=s.total+"KB";
    $("fe-fragment-largest").textContent=s.largest+"KB";
    $("fe-fragment-holes").textContent=s.holes+"か所";
    memory.setAttribute("aria-label","200KBの主記憶："+blocks.map(b=>(b.id||"空き")+b.size+"KB").join("、"));
    const release=$("fe-fragment-release");release.replaceChildren();
    blocks.filter(b=>b.id).forEach(b=>{
      const button=document.createElement("button");button.type="button";
      button.textContent=b.id+"（"+b.size+"KB）を解放";
      button.addEventListener("click",()=>{
        const target=blocks.find(x=>x.id===b.id);if(!target)return;
        target.id=null;normalize();
        $("fe-fragment-result").textContent=b.id+"を解放しました。";
        $("fe-fragment-reason").textContent="隣接する空き領域は結合します。";
        render();
      });release.appendChild(button);
    });
    $("fe-fragment-allocate").disabled=!blocks.some(b=>!b.id);
  }
  function requestedSize(){
    const el=$("fe-fragment-size");let n=Number(el.value);
    if(!Number.isFinite(n))n=1;
    n=Math.min(200,Math.max(1,Math.trunc(n)));el.value=String(n);return n;
  }
  $("fe-fragment-allocate").addEventListener("click",()=>{
    const size=requestedSize(),before=stats();
    const success=before.largest>=size;
    const guess=root.querySelector('input[name="fe-fragment-guess"]:checked');
    const feedback=guess?(guess.value===(success?"yes":"no")?"予想正解！ ":"予想と異なりました。 "):"";
    if(success){
      const pos=blocks.findIndex(b=>!b.id&&b.size>=size);
      const target=blocks[pos],id=["D","E","F"][nextId]||"追加"+(nextId+1);nextId++;
      blocks.splice(pos,1,{id,size},...(target.size>size?[{id:null,size:target.size-size}]:[]));
      $("fe-fragment-result").textContent=feedback+id+"を"+size+"KB確保しました。";
      $("fe-fragment-reason").textContent="first-fitで最初に見つかった連続空き領域へ配置しました。";
    }else{
      $("fe-fragment-result").textContent=feedback+size+"KBの確保に失敗しました。";
      $("fe-fragment-reason").textContent=before.total>=size?"空きは合計"+before.total+"KBですが、最大の連続空きが"+before.largest+"KBしかありません。外部フラグメンテーションです。":"空き合計が"+before.total+"KBしかないため、容量そのものが足りません。";
    }
    root.querySelectorAll('input[name="fe-fragment-guess"]').forEach(r=>r.checked=false);render();
  });
  $("fe-fragment-compact").addEventListener("click",()=>{
    const before=stats(),used=blocks.filter(b=>b.id).map(b=>({...b}));
    blocks=[...used,...(before.total?[{id:null,size:before.total}]:[])];
    $("fe-fragment-result").textContent="コンパクションしました。";
    $("fe-fragment-reason").textContent="空き合計は"+before.total+"KBのまま、最大の連続空きは"+stats().largest+"KBになりました。使用中領域を移動する処理コストは別途発生します。";
    render();
  });
  $("fe-fragment-reset").addEventListener("click",reset);
  $("fe-fragment-case").addEventListener("change",reset);
  function internal(){
    const neededEl=$("fe-fragment-needed"),unit=Number($("fe-fragment-unit").value);
    let needed=Number(neededEl.value);if(!Number.isFinite(needed))needed=1;
    needed=Math.min(32,Math.max(1,Math.trunc(needed)));neededEl.value=String(needed);
    const allocated=Math.ceil(needed/unit)*unit,waste=allocated-needed;
    $("fe-fragment-internal-result").textContent="必要"+needed+"KBを"+unit+"KB単位で確保すると、割当て"+allocated+"KB、内部の余り"+waste+"KBです。";
    const bar=$("fe-fragment-internal-bar");bar.replaceChildren();
    [[needed,"使用 "+needed+"KB","fe-fragment-demo__used"],[waste,"余り "+waste+"KB","fe-fragment-demo__unused"]].forEach(([amount,label,klass])=>{
      if(amount===0)return;
      const part=document.createElement("div");part.className=klass;part.style.flex=String(amount);
      part.textContent=label;bar.appendChild(part);
    });
  }
  $("fe-fragment-needed").addEventListener("change",internal);
  $("fe-fragment-unit").addEventListener("change",internal);
  reset();internal();
})();
</script>

## 定義・仕組み

### 外部フラグメンテーション

可変長の領域を確保・解放していると、使用中領域の間に小さな空き領域が残ることがあります。

```text
確保 → 解放 → 確保 → 解放
              ↓
空き領域が細切れになる
```

空き容量の**合計**が十分でも、必要な大きさの**連続領域**がなければ割り当てられないことがあります。

### メモリコンパクション

メモリコンパクションは、使用中の領域を移動して一方へ詰め、散在する空き領域を連続した大きな空き領域へまとめる方法です。

```text
Before
[A][空][B][空空][C][空]

After
[A][B][C][空空空空]
```

外部フラグメンテーションを改善できますが、使用中データを移動する処理が必要なので、**処理コストがかかる**点にも注意します。

### 内部フラグメンテーション

内部フラグメンテーションは、割り当てた領域の中に使われない部分が残る現象です。

例えば4KB単位でしか割り当てられないとき、3KB必要な処理に4KBを割り当てると1KB余ります。

```text
割当て 4KB
┌────────────┐
│ 使用 3KB │ 空き1KB │
└────────────┘
              ↑
       割当て領域の内部
```

この無駄は領域同士の「間」が散らばっている問題ではないため、コンパクションで空きを寄せても解決しません。

### ページングとの関係

[ページング方式](/fe/paging/)では、仮想記憶を固定長のページ、主記憶を同じ大きさのページフレームに分けます。

```text
可変長の連続領域
→ 外部フラグメンテーションが起こりやすい

固定長のページ / ページフレーム
→ 離れたフレームにも配置できる
→ 外部フラグメンテーションを避けやすい
```

ただし固定長単位で割り当てるため、最後のページなどに未使用部分が残り、**内部フラグメンテーション**が生じることがあります。

仮想記憶全体の考え方は[仮想記憶](/fe/virtual-memory/)で確認できます。

## 科目Aでどう出る？

問題文では、無駄な領域が**どこにあるか**を見るのが最初の判断ポイントです。

| 問題文 | 判断 |
|---|---|
| 割当て領域の中に未使用部分 | 内部フラグメンテーション |
| 使用領域の間に小さな空きが散在 | 外部フラグメンテーション |
| 散在した空きを一つにまとめる | メモリコンパクション |
| 固定長のページとページフレーム | ページング |

特に、

```text
空き容量の合計は十分
しかし連続した空き領域が足りない
```

という説明は、外部フラグメンテーションを疑います。

## どんな場面で使う？

主記憶へ可変長の領域を割り当てる方式では、確保と解放を繰り返すほど空き領域が散らばる可能性があります。

このとき、

```text
外部フラグメンテーションが発生
        ↓
コンパクション
        ↓
使用中領域を詰める
        ↓
連続した空き領域を作る
```

という流れで理解します。

一方、ページングでは連続した物理領域へ置く必要がないため、外部フラグメンテーションへの考え方が変わります。

## よくある誤解・混同

### コンパクションは内部フラグメンテーションも解消する

違います。

```text
外部フラグメンテーション
→ 空きが散在
→ コンパクションが有効

内部フラグメンテーション
→ 割当て領域内部の余り
→ コンパクションでは解消しない
```

### 空き容量の合計が十分なら必ず割り当てられる

連続領域が必要な方式では、そうとは限りません。合計容量ではなく、必要な大きさの連続領域があるかが問題になります。

### コンパクションとページングは同じ対策

違います。コンパクションは**配置済み領域を移動して空きをまとめる**方法です。ページングは**固定長単位に分け、離れた物理領域にも配置できるようにする**記憶管理方式です。

## まとめ（試験直前用）

- フラグメンテーションは、メモリ利用によって無駄な領域が生じる現象
- **内部**：割当て領域の中に無駄ができる
- **外部**：使用領域の間に空きが散らばる
- **メモリコンパクション**：使用中領域を移動し、散在した空きをまとめる
- コンパクションは主に**外部フラグメンテーション**への対策
- ページングは外部フラグメンテーションを避けやすいが、内部フラグメンテーションは起こり得る

{% include fe_article_footer.html %}
