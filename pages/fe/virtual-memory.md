---
layout: page
title: 仮想記憶とは？主記憶・ページファイルとメモリ不足の切り分け【基本情報技術者試験】
description: 仮想記憶を、プログラムが使うアドレスと物理メモリを分けて管理する仕組みとして整理します。RAM増設、ページファイルの拡張、ディスクの空き容量確保で何が変わるかを比較し、メモリ不足への一時対応と高速化の違いを、FE科目Aの判断基準として確認します。
permalink: /fe/virtual-memory/
tags: [fe, fe-technology, computer-system]
fe_section: テクノロジ系
fe_subsection: コンピュータシステム
fe_order: 250
date: 2026-10-02
last_modified_at: 2026-11-01
related_articles:
  - /fe/memory-management-methods/
  - /fe/paging/
  - /fe/dynamic-address-translation/
  - /fe/overlay-paging-swapping/
  - /fe/thrashing/
---

## まず結論

**仮想記憶は、プログラムが使うアドレスと実際の主記憶上の位置を分けて管理する仕組み**です。補助記憶も利用することで、物理メモリより大きな記憶領域を扱えるようになります。

FE科目Aでは、**仮想記憶のための領域を増やすことと、RAMを増設することは別**と押さえます。ディスクの空き容量を増やすだけでも、RAMが増えるわけではありません。

## 直感的な説明

机の上で資料を使う場面を考えます。机が狭くても、今使わない資料を棚に置き、必要な資料だけ机へ持ってくれば、多くの資料を扱えます。

<div class="portal-card-grid">
  <section class="portal-card">
    <h3>机の上：主記憶（RAM）</h3>
    <p>今の処理で使う命令やデータを置く場所。容量は物理的に決まっています。</p>
  </section>
  <section class="portal-card">
    <h3>棚の一部：ページファイル</h3>
    <p>RAMから退避させたデータを置く、補助記憶上の領域。必要になったらRAMへ戻します。</p>
  </section>
</div>

見るポイントは、**棚の利用枠を増やしても、机の広さは変わらない**ことです。

棚を使えば扱える資料を増やせますが、出し入れには時間がかかります。仮想記憶も、容量面の助けになる一方、補助記憶との入替えが増えると処理が遅くなることがあります。

このたとえは、仮想記憶で補助記憶を利用する場面を表しています。仮想記憶そのものとページファイルは同じ意味ではありません。


### 触って覚える：RAMのページ枠とページフォールト

**「仮想ページを参照したとき、RAMにある？ ない？」**を予想してから1ステップ進めてください。同じページ参照列でも、RAMのページ枠数によってフォールトの回数が変わります。

これは6つの仮想ページ（0〜5）を持つプログラムの単純化モデルです。すべてのページは開始時点で補助記憶から読み込めるものとし、RAMは最初は空です。ページがRAMになければ**ページフォールト**が発生し、空き枠があれば読み込み、満杯なら例示用のFIFO順に1ページを置換します。ここでは書戻し不要のページだけを扱います。FIFOとLRUの比較・置換計算は[LRUページ置換の記事](/fe/lru-page-replacement/)へ進んでください。

<div id="fe-vmem-demo" class="fe-vmem-demo">
  <div class="fe-vmem-demo__controls">
    <label for="fe-vmem-frames">RAMのページ枠数
      <select id="fe-vmem-frames"><option value="2">2枠</option><option value="3" selected>3枠</option><option value="4">4枠</option></select>
    </label>
    <label for="fe-vmem-sequence">仮想ページの参照列（0〜5、カンマ区切り）
      <input id="fe-vmem-sequence" type="text" value="0,1,2,0,3,0,4,1">
    </label>
  </div>
  <p class="fe-vmem-demo__note">参照順序を変えたり、RAMのページ枠数を増減して違いを確かめられます。入力を変更すると初期状態に戻ります。</p>
  <fieldset class="fe-vmem-demo__predict">
    <legend>予想：次の参照は？</legend>
    <label><input type="radio" name="fe-vmem-guess" value="hit">ヒット（すでにRAMにある）</label>
    <label><input type="radio" name="fe-vmem-guess" value="fault">ページフォールト（RAMにない）</label>
  </fieldset>
  <div class="fe-vmem-demo__actions">
    <button type="button" id="fe-vmem-next">1ページ参照</button>
    <button type="button" id="fe-vmem-prev">1ステップ戻る</button>
    <button type="button" id="fe-vmem-all">最後まで実行</button>
    <button type="button" id="fe-vmem-reset">最初から</button>
  </div>
  <p id="fe-vmem-result" role="status" aria-live="polite">最初のページ0がRAMにあるか、予想してください。</p>
  <div class="fe-vmem-demo__stats" aria-live="polite">
    <div>ページフォールト<strong id="fe-vmem-faults">0回</strong></div>
    <div>ヒット<strong id="fe-vmem-hits">0回</strong></div>
    <div>ページ置換<strong id="fe-vmem-replacements">0回</strong></div>
  </div>
  <div class="fe-vmem-demo__two">
    <section>
      <h4>仮想ページ（プログラム側）</h4>
      <div id="fe-vmem-virtual" class="fe-vmem-demo__pages" aria-label="仮想ページ一覧">0 1 2 3 4 5</div>
    </section>
    <section>
      <h4>RAM（物理ページ枠）</h4>
      <div id="fe-vmem-ram" class="fe-vmem-demo__pages" aria-label="現在RAMにあるページ">空き</div>
    </section>
  </div>
  <p id="fe-vmem-pending">未処理：0, 1, 2, 0, 3, 0, 4, 1</p>
  <div class="fe-vmem-demo__two">
    <section>
      <h4>RAMを増やすと？</h4>
      <p>同時に置けるページが増えます。ページフォールトを減らせる場合があります。</p>
    </section>
    <section>
      <h4>ページファイルを増やすと？</h4>
      <p>補助記憶上の容量を確保する操作です。<strong>RAMのページ枠数は増えません。</strong></p>
    </section>
  </div>
  <p class="fe-vmem-demo__note">この操作例の結果は参照列とFIFOの条件に依存します。RAMを増やせばどんな条件でも必ずページフォールトが減る、という意味ではありません。実際の仮想記憶は、ページファイル以外のファイルやメモリにも対応付けられます。</p>
</div>
<noscript><p>操作教材はJavaScriptが必要です。例：RAMが3枠で参照列0,1,2,0の場合、0・1・2の最初の3回はページフォールト、最後の0はヒットです。ページファイルの容量を増やしてもRAMが3枠のままなら、枠数は変わりません。</p></noscript>

<style>
.fe-vmem-demo{border:1px solid #94a3b8;border-radius:12px;padding:1rem;margin:1rem 0}
.fe-vmem-demo__controls,.fe-vmem-demo__two{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.7rem;margin:.8rem 0}
.fe-vmem-demo__controls label{display:flex;flex-direction:column;gap:.35rem}
.fe-vmem-demo input[type=text],.fe-vmem-demo select{min-width:0;max-width:100%;padding:.45rem;border:1px solid #64748b;border-radius:6px;background:var(--background-color,#fff);color:var(--text-color,#172033)}
.fe-vmem-demo__predict{display:flex;flex-wrap:wrap;gap:.65rem;border:1px solid #94a3b8;border-radius:8px;padding:.65rem}
.fe-vmem-demo__predict legend{font-weight:700}
.fe-vmem-demo__actions{display:flex;flex-wrap:wrap;gap:.5rem;margin:.8rem 0}
.fe-vmem-demo button{padding:.5rem .75rem;border-radius:6px;border:1px solid #64748b;background:#e2e8f0;color:#172033;cursor:pointer}
.fe-vmem-demo button:disabled{opacity:.45;cursor:not-allowed}
.fe-vmem-demo__stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.5rem;margin:.8rem 0}
.fe-vmem-demo__stats div,.fe-vmem-demo__two section{border:1px solid #94a3b8;border-radius:8px;padding:.6rem;min-width:0}
.fe-vmem-demo__stats strong{display:block;font-size:1.15rem}
.fe-vmem-demo__two h4{margin:0 0 .5rem;font-size:1rem}
.fe-vmem-demo__two p{margin:.25rem 0}
.fe-vmem-demo__pages{display:flex;gap:.35rem;flex-wrap:wrap}
.fe-vmem-demo__page{padding:.5rem .65rem;border:1px solid #64748b;border-radius:6px;background:#dbeafe;color:#1e3a8a;font-weight:700}
.fe-vmem-demo__page.is-missing{background:#e2e8f0;color:#334155}
.fe-vmem-demo__page.is-current{outline:3px solid #b45309;outline-offset:2px}
.fe-vmem-demo__note{font-size:.9rem}
.fe-vmem-demo :focus-visible{outline:3px solid #2563eb;outline-offset:2px}
@media(max-width:560px){.fe-vmem-demo{padding:.65rem}.fe-vmem-demo__controls,.fe-vmem-demo__two,.fe-vmem-demo__stats{grid-template-columns:1fr}.fe-vmem-demo__actions button{flex:1 1 43%}}
</style>
<script>
(function(){
  "use strict";
  const root=document.getElementById("fe-vmem-demo");if(!root)return;
  const $=id=>root.querySelector("#"+id);
  let sequence=[],step=0,feedback="",valid=true;
  function readSequence(){
    const tokens=$("fe-vmem-sequence").value.trim().split(/[,，\s]+/).filter(Boolean);
    if(tokens.length<1||tokens.length>20||tokens.some(t=>!/^[0-5]$/.test(t)))throw new Error("ページ番号0〜5を1〜20個入力してください。");
    return tokens.map(Number);
  }
  function stateAt(count){
    const ram=[],fifo=[],capacity=Number($("fe-vmem-frames").value);
    let faults=0,hits=0,replacements=0,last=null;
    for(const page of sequence.slice(0,count)){
      if(ram.includes(page)){hits++;last={page,kind:"hit",removed:null};continue;}
      faults++;
      let removed=null;
      if(ram.length>=capacity){
        removed=fifo.shift();ram.splice(ram.indexOf(removed),1);replacements++;
      }
      ram.push(page);fifo.push(page);
      last={page,kind:"fault",removed};
    }
    return {ram,faults,hits,replacements,last};
  }
  function renderPages(container,pages,present,current){
    container.replaceChildren();
    pages.forEach(page=>{
      const node=document.createElement("span");node.className="fe-vmem-demo__page";
      if(page===null)node.classList.add("is-missing");
      if(present&&page!==null&&!present.includes(page))node.classList.add("is-missing");
      if(page===current)node.classList.add("is-current");
      node.textContent=page===null?"空き":String(page);
      container.appendChild(node);
    });
  }
  function render(){
    const state=stateAt(step),next=sequence[step],capacity=Number($("fe-vmem-frames").value);
    $("fe-vmem-faults").textContent=state.faults+"回";
    $("fe-vmem-hits").textContent=state.hits+"回";
    $("fe-vmem-replacements").textContent=state.replacements+"回";
    renderPages($("fe-vmem-virtual"),[0,1,2,3,4,5],state.ram,step?state.last.page:null);
    renderPages($("fe-vmem-ram"),state.ram.concat(Array(capacity-state.ram.length).fill(null)),null,step?state.last.page:null);
    $("fe-vmem-pending").textContent="未処理："+(sequence.slice(step).join(", ")||"なし");
    $("fe-vmem-result").textContent=feedback||(valid?(step===sequence.length?"参照列をすべて処理しました。":"次のページ"+next+"がRAMにあるか予想してください。"):"入力を修正してください。");
    $("fe-vmem-next").disabled=!valid||step>=sequence.length;
    $("fe-vmem-all").disabled=!valid||step>=sequence.length;
    $("fe-vmem-prev").disabled=step===0;
    root.querySelectorAll('input[name="fe-vmem-guess"]').forEach(r=>r.disabled=!valid||step>=sequence.length);
  }
  function reset(){
    try{sequence=readSequence();valid=true;feedback="ページ"+sequence[0]+"がRAMにあるか予想してください。";}
    catch(error){sequence=[];valid=false;feedback=error.message;}
    step=0;
    root.querySelectorAll('input[name="fe-vmem-guess"]').forEach(r=>r.checked=false);
    render();
  }
  $("fe-vmem-next").addEventListener("click",()=>{
    if(!valid||step>=sequence.length)return;
    const before=stateAt(step),page=sequence[step],hit=before.ram.includes(page);
    const chosen=root.querySelector('input[name="fe-vmem-guess"]:checked');
    const expected=hit?"hit":"fault";
    const after=stateAt(step+1);
    feedback=(chosen?(chosen.value===expected?"予想正解！ ":"予想と異なりました。 "):"")+
      "ページ"+page+"は"+(hit?"RAMにありヒットしました。":"RAMになくページフォールト。")+
      (hit?"置換えなし。":after.last.removed!==null?"ページ"+after.last.removed+"を置き換え、ページ"+page+"を読込みました。":"空き枠にページ"+page+"を読込みました。");
    step++;
    root.querySelectorAll('input[name="fe-vmem-guess"]').forEach(r=>r.checked=false);
    render();
  });
  $("fe-vmem-prev").addEventListener("click",()=>{if(step>0)step--;feedback="1ステップ戻しました。次の参照を予想してください。";render();});
  $("fe-vmem-all").addEventListener("click",()=>{step=sequence.length;feedback="全参照を処理しました。RAMの枠数を変えて比べてください。";render();});
  $("fe-vmem-reset").addEventListener("click",reset);
  ["fe-vmem-frames","fe-vmem-sequence"].forEach(id=>$(id).addEventListener("change",reset));
  reset();
})();
</script>

## 定義・仕組み

### 主記憶・仮想記憶・ページファイルの違い

| 用語 | 何を表す？ | 見分けるポイント |
|---|---|---|
| 主記憶・物理メモリ（RAM） | 命令やデータを保持する実際のメモリ | RAMの容量・増設 |
| 仮想アドレス空間 | プログラムが使えるアドレスの範囲 | 実際のRAM上の位置とは分けて管理する |
| 仮想記憶 | 仮想アドレスを物理メモリなどに対応付ける仕組み | OSとハードウェアによる管理 |
| ページファイル | Windowsがメモリ管理に利用する補助記憶上のファイル | RAMからのデータの退避など |
| ディスクの空き容量 | HDD・SSD上でまだ使われていない容量 | 文書・画像などの保存にも使える |

プログラムは仮想アドレスを使います。OSとハードウェアは、対応表などを使って実際の物理アドレスへ変換します。

代表的な方式が[ページング方式]({{ '/fe/paging/' | relative_url }})です。必要なページをRAMに置き、補助記憶にあるページが必要になればRAMへ読み込みます。**プログラム全体を、同時にRAMへ置かなければならないわけではありません。**

仮想アドレスと物理アドレスの関係は、[Microsoft Learn：Virtual Address Space](https://learn.microsoft.com/en-us/windows/win32/memory/virtual-address-space)で確認できます。

### 仮想記憶の設定を増やすと何が変わる？

過去問でいう「仮想記憶の大きさの設定値を増やす」は、一般的なPCの文脈では、ページファイルなどに使う補助記憶上の領域を広げる対応として読み取ります。

Windowsでは、RAMとページファイルが、システム全体で確保できるメモリの上限を支えます。この上限を**コミット上限**と呼びます。ページファイルを拡張すると、メモリ確保の上限を広げられる場合があります。

ただし、**ページファイルの拡張で物理RAMや、プログラムの仮想アドレス空間の上限が増えるわけではありません。** メモリ不足の原因によっては、別の対応が必要です。

ページファイルの役割とコミット上限は、[Microsoft Learn：Introduction to page files](https://learn.microsoft.com/en-us/troubleshoot/windows-client/performance/introduction-to-the-page-file)で説明されています。FEでは用語の細部より、**RAM・ページファイル・ディスクの空き容量を分ける**ことを優先します。

## 科目Aでどう出る？

問題文に「メモリ不足」とあったら、**どの容量を増やす操作なのか**を確認します。

| 操作 | 直接変わるもの | 判断 |
|---|---|---|
| RAMを増設する | 物理メモリの容量 | 実際にRAMを増やす |
| ページファイルの設定を増やす | メモリ確保を支える補助記憶上の領域 | 容量不足への一時対応になり得る |
| 不要な文書・画像を削除する | ディスクの空き容量 | それだけではRAMやメモリ確保の上限は増えない |
| 使用していないアプリを終了する | アプリが占有していたメモリなど | メモリ需要を減らす |
| 表計算の列を非表示にする | 画面に表示する範囲 | 非表示のデータは保持される |

「仮想記憶を備えたPCで、メモリ不足により追加のアプリを起動できない」「RAM増設までの対応」とあれば、仮想記憶の設定を増やす操作が候補になります。

一方、**起動できないという容量の問題と、ページ交換で遅いという性能の問題は分けます。** 「仮想記憶を増やせば必ず高速化する」という選択肢は不適切です。

## どんな場面で使う？

複数のアプリを使っているPCで、新しいアプリを起動しようとしてメモリ不足になる場面を考えます。

- 不要なアプリを終了する：必要なメモリ量を減らす。
- ページファイルの容量が不足しているなら、設定を見直す：メモリ確保の上限を広げる。
- RAMを増設する：物理メモリを増やし、補助記憶との入替えを減らせる場合がある。

入替えが頻発して本来の処理が進まなくなる状態は、[スラッシング]({{ '/fe/thrashing/' | relative_url }})です。仮想記憶の役割を理解したら、容量と性能の違いをつなげて確認できます。

## よくある誤解・混同

### 仮想記憶を増やせば、RAMが増える

RAMの容量は変わりません。ページファイルを広げるのは、補助記憶を利用したメモリ管理のための領域を増やす対応です。

### ディスクの空きを増やすことと、仮想記憶を増やすことは同じ

ディスクの空きは、ページファイルを広げるための条件になり得ます。しかし、不要なファイルを消す操作と、ページファイルの容量を増やす操作は別です。

OSがページファイルを自動拡張する設定なら、空き容量の確保が間接的に役立つことがあります。試験では、**自動拡張やディスク容量不足という条件が示されているか**も確認します。

### 仮想記憶があれば、容量も速度も無制限

容量にはOS・アプリ・アドレス空間・補助記憶などの制約があります。また、補助記憶はRAMよりアクセスが遅いため、頻繁なページ交換は性能低下につながります。

仮想記憶は、限られたRAMを補いながら記憶領域を管理する仕組みです。高速なRAMの増設と同じ効果があるとは考えません。

アドレスの対応付けを詳しく確認するなら、[ページング方式](/fe/paging/)から[動的アドレス変換（DAT）](/fe/dynamic-address-translation/)へ進むと、管理単位と変換機構を分けて理解できます。

## まとめ（試験直前用）

- 仮想記憶は、**プログラムのアドレスと物理メモリを分けて管理**する仕組み。
- 補助記憶を利用すれば、RAMより大きな記憶領域を扱える。
- **ページファイルの拡張とRAM増設は別**。
- ディスクの空き容量確保だけで、メモリ確保の上限が直接増えるわけではない。
- **容量不足への対応と高速化を分ける**。ページ交換の多発はスラッシングにつながる。

{% include fe_article_footer.html %}
