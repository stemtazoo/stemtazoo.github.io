---
layout: page
title: CPUの命令実行サイクルとは？フェッチ・解読・オペランド読出し・実行の順番【基本情報技術者試験】
description: CPUが1命令を実行する流れを、命令フェッチ、命令の解読、オペランド読出し、命令の実行の順に整理し、プログラムカウンタや命令レジスタとの関係、FE試験で順序問題を切る判断軸を解説します。
permalink: /fe/cpu-instruction-cycle/
tags: [fe, fe-technology, computer-architecture, cpu]
fe_section: テクノロジ系
fe_subsection: コンピュータ構成要素
fe_order: 20
date: 2026-08-09
last_modified_at: 2026-11-01
---

## まず結論

CPUが命令を実行するときは、基本的に次の順で考えます。

```text
命令フェッチ
↓
命令の解読
↓
オペランド読出し
↓
命令の実行
```

基本情報技術者試験では、順番だけを丸暗記するより、**前の処理が終わらないと次の処理ができない**と考えると判断しやすくなります。

```text
命令をまだ取っていない
→ 解読できない

命令をまだ解読していない
→ 必要なデータが分からない

必要なデータがそろっていない
→ 実行できない
```

迷ったら、**「指示を取る → 意味を理解する → 材料を用意する → 作業する」**の順で思い出します。

## 直感的な説明

CPUの命令実行は、料理の手順に置き換えると分かりやすいです。

```text
レシピを取ってくる
→ 命令フェッチ

レシピを読む
→ 命令の解読

必要な材料を用意する
→ オペランド読出し

実際に料理する
→ 命令の実行
```

例えば、「AとBを加算する」という命令をCPUが処理するとします。

CPUは、いきなり加算を始めるわけではありません。

まず命令を読み出し、その命令が「加算」だと解読し、次にAとBという演算対象のデータを読み出してから、加算を実行します。

この流れを理解しておけば、選択肢の順序が入れ替わっていても判断できます。


### 触って覚える：PC・IR・R0を1段階ずつ確認する

次の2命令を**フェッチ→解読→オペランド読出し→実行**の順に進めます。予想してから「次へ」を押し、PC（次の命令の番地）・IR（読み出した命令）・R0（演算結果）の変化を見てください。

この教材は命令が番地0、1に1語ずつ並ぶ単純化したCPUです。フェッチ時にPCを1増やし、解読とオペランド読出しではR0を変更せず、実行時にR0を更新します。データメモリの番地20・21から読み出します。命令パイプライン、キャッシュ、分岐、実際のクロック数は扱いません。

<div id="fe-cycle-demo" class="fe-cycle-demo">
  <div class="fe-cycle-demo__inputs">
    <label for="fe-cycle-m20">メモリ[20] <input id="fe-cycle-m20" type="number" min="0" max="20" step="1" value="3"></label>
    <label for="fe-cycle-m21">メモリ[21] <input id="fe-cycle-m21" type="number" min="0" max="20" step="1" value="5"></label>
  </div>
  <p><strong>命令列：</strong>番地0：LOAD R0, [20] ／ 番地1：ADD R0, [21]</p>
  <div class="fe-cycle-demo__stages" aria-label="命令実行の4段階">
    <span data-stage="fetch">① フェッチ</span><span data-stage="decode">② 解読</span><span data-stage="operand">③ データ読出し</span><span data-stage="execute">④ 実行</span>
  </div>
  <fieldset class="fe-cycle-demo__predict">
    <legend>予想：次に何をする？</legend>
    <label><input type="radio" name="fe-cycle-guess" value="fetch">PCを進め、IRに命令を格納</label>
    <label><input type="radio" name="fe-cycle-guess" value="decode">命令コードを解読</label>
    <label><input type="radio" name="fe-cycle-guess" value="operand">演算に使うデータを読出し</label>
    <label><input type="radio" name="fe-cycle-guess" value="execute">R0を書き換える</label>
  </fieldset>
  <div class="fe-cycle-demo__actions">
    <button type="button" id="fe-cycle-next">1段階進める</button>
    <button type="button" id="fe-cycle-prev">1段階戻る</button>
    <button type="button" id="fe-cycle-reset">最初から</button>
  </div>
  <div class="fe-cycle-demo__regs">
    <div>PC（次の命令番地）<strong id="fe-cycle-pc">0</strong></div>
    <div>IR（現在の命令）<strong id="fe-cycle-ir">未取得</strong></div>
    <div>R0（演算結果）<strong id="fe-cycle-r0">0</strong></div>
    <div>読出したデータ<strong id="fe-cycle-temp">なし</strong></div>
  </div>
  <p id="fe-cycle-feedback" role="status" aria-live="polite">次の処理を予想してください。</p>
  <p id="fe-cycle-explanation" aria-live="polite">PCは命令の場所、IRは命令そのものを保持します。</p>
  <ol id="fe-cycle-history" aria-label="実行した操作"><li>まだ実行していません。</li></ol>
  <p class="fe-cycle-demo__note">初期値なら1命令目の実行後R0=3、2命令目の実行後R0=8です。フェッチでPCが増えても、R0はまだ更新されません。</p>
</div>
<noscript><p>JavaScript無効時の例：番地0のLOADをフェッチ（PC=1、IR=LOAD）→解読→メモリ[20]の3を準備→実行（R0=3）。次に番地1のADDをフェッチ（PC=2、IR=ADD）→解読→メモリ[21]の5を準備→実行（R0=8）。</p></noscript>

<style>
.fe-cycle-demo{border:1px solid #94a3b8;border-radius:12px;padding:1rem;margin:1.2rem 0}
.fe-cycle-demo__inputs,.fe-cycle-demo__actions{display:flex;gap:.6rem;flex-wrap:wrap}
.fe-cycle-demo__inputs label{display:flex;flex-direction:column;gap:.3rem;flex:1 1 130px}
.fe-cycle-demo input[type=number]{width:7rem;max-width:100%;padding:.45rem;border:1px solid #64748b;border-radius:6px;background:var(--background-color,#fff);color:var(--text-color,#172033)}
.fe-cycle-demo__stages{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:.4rem;margin:.8rem 0}
.fe-cycle-demo__stages span{border:1px solid #94a3b8;border-radius:6px;padding:.5rem .2rem;text-align:center;font-size:.85rem}
.fe-cycle-demo__stages span.is-current{border:2px solid #2563eb;background:rgba(59,130,246,.12);font-weight:700}
.fe-cycle-demo__predict{border:1px solid #94a3b8;border-radius:8px;padding:.7rem;margin:.8rem 0;display:flex;flex-direction:column;gap:.4rem}
.fe-cycle-demo__predict legend{font-weight:700}
.fe-cycle-demo button{border:1px solid #64748b;border-radius:6px;background:#e2e8f0;color:#172033;padding:.5rem .8rem;cursor:pointer}
.fe-cycle-demo button:disabled{opacity:.45;cursor:not-allowed}
.fe-cycle-demo__regs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.5rem;margin:1rem 0}
.fe-cycle-demo__regs div{border:1px solid #94a3b8;border-radius:8px;padding:.65rem;min-width:0;font-size:.88rem}
.fe-cycle-demo__regs strong{display:block;margin-top:.3rem;font-size:1rem;overflow-wrap:anywhere}
.fe-cycle-demo__note{font-size:.9rem}
.fe-cycle-demo :focus-visible{outline:3px solid #2563eb;outline-offset:2px}
@media(max-width:560px){.fe-cycle-demo{padding:.65rem}.fe-cycle-demo__stages,.fe-cycle-demo__regs{grid-template-columns:repeat(2,minmax(0,1fr))}.fe-cycle-demo__actions button{flex:1 1 43%}}
</style>
<script>
(function(){
  "use strict";
  const root=document.getElementById("fe-cycle-demo");if(!root)return;
  const $=id=>root.querySelector("#"+id);
  const stages=["fetch","decode","operand","execute"];
  const labels=["フェッチ","解読","オペランド読出し","実行"];
  const program=[{command:"LOAD R0, [20]",op:"LOAD",addr:20},{command:"ADD R0, [21]",op:"ADD",addr:21}];
  let step=0,feedback="";
  function memory(id){
    const input=$(id);let value=Number(input.value);
    if(!Number.isFinite(value))value=0;
    value=Math.max(0,Math.min(20,Math.trunc(value)));
    input.value=String(value);return value;
  }
  function calc(count){
    const data={20:memory("fe-cycle-m20"),21:memory("fe-cycle-m21")};
    let pc=0,ir="未取得",r0=0,temp="なし";
    const log=[];
    for(let i=0;i<count;i++){
      const instruction=program[Math.floor(i/4)],stage=stages[i%4];
      if(stage==="fetch"){
        ir=instruction.command;pc=Math.floor(i/4)+1;temp="なし";
        log.push("フェッチ：IR="+ir+"、PC="+pc);
      }else if(stage==="decode"){
        log.push("解読："+instruction.op+"命令だと判定");
      }else if(stage==="operand"){
        temp=data[instruction.addr];
        log.push("オペランド読出し：メモリ["+instruction.addr+"]="+temp+"、R0は変更なし");
      }else{
        r0=instruction.op==="LOAD"?temp:r0+temp;
        log.push("実行：R0="+r0);
      }
    }
    return {pc,ir,r0,temp,log};
  }
  function render(){
    const state=calc(step),previous=step?stages[(step-1)%4]:null;
    $("fe-cycle-pc").textContent=state.pc;
    $("fe-cycle-ir").textContent=state.ir;
    $("fe-cycle-r0").textContent=state.r0;
    $("fe-cycle-temp").textContent=state.temp;
    root.querySelectorAll("[data-stage]").forEach(el=>el.classList.toggle("is-current",el.dataset.stage===previous));
    const explanations=[
      "命令フェッチ：PCの番地の命令をIRへ読み、PCを次の命令番地へ進めます。",
      "命令解読：IRにある命令の意味を調べます。R0はまだ変わりません。",
      "オペランド読出し：必要な値を一時的に用意します。R0はまだ変わりません。",
      "命令実行：用意した値を使ってR0を更新します。"
    ];
    $("fe-cycle-explanation").textContent=step?explanations[(step-1)%4]:"PCは命令の場所、IRは命令そのものを保持します。";
    $("fe-cycle-feedback").textContent=feedback||(step===8?"2命令の実行が完了しました。":"次の処理を予想してください。");
    const list=$("fe-cycle-history");list.replaceChildren();
    (state.log.length?state.log:["まだ実行していません。"]).forEach(item=>{
      const li=document.createElement("li");li.textContent=item;list.appendChild(li);
    });
    $("fe-cycle-next").disabled=step===8;$("fe-cycle-prev").disabled=step===0;
    root.querySelectorAll('input[name="fe-cycle-guess"]').forEach(r=>r.disabled=step===8);
  }
  $("fe-cycle-next").addEventListener("click",()=>{
    if(step===8)return;
    const chosen=root.querySelector('input[name="fe-cycle-guess"]:checked');
    const expected=stages[step%4];
    feedback=(chosen?(chosen.value===expected?"予想正解！ ":"予想と違いました。 "):"")+"ステップ"+(step+1)+"："+labels[step%4]+"を行いました。";
    step++;root.querySelectorAll('input[name="fe-cycle-guess"]').forEach(r=>r.checked=false);render();
  });
  $("fe-cycle-prev").addEventListener("click",()=>{if(step>0)step--;feedback="1段階戻しました。次の変化を予想してください。";render()});
  $("fe-cycle-reset").addEventListener("click",()=>{step=0;feedback="最初からやり直します。";root.querySelectorAll('input[name="fe-cycle-guess"]').forEach(r=>r.checked=false);render()});
  ["fe-cycle-m20","fe-cycle-m21"].forEach(id=>$(id).addEventListener("change",()=>{
    step=0;feedback="メモリの値を変えたので、最初から実行します。";
    root.querySelectorAll('input[name="fe-cycle-guess"]').forEach(r=>r.checked=false);render();
  }));
  render();
})();
</script>

## 定義・仕組み

CPUは、主記憶に格納された命令を1つずつ取り出して実行します。

FE試験では、次の4段階を基本として整理すると分かりやすいです。

| 段階 | 何をする？ | 初心者向けの言い換え |
|---|---|---|
| 命令フェッチ | 主記憶から命令を読み出す | 指示を取ってくる |
| 命令の解読 | 命令の意味を調べる | 何をする指示か読む |
| オペランド読出し | 演算に必要なデータを読み出す | 必要な材料を用意する |
| 命令の実行 | 演算や処理を実行する | 実際に作業する |

### 1. 命令フェッチ

まず、次に実行する命令を主記憶から読み出します。

```text
次の命令の場所を確認
↓
主記憶から命令を読み出す
```

このとき、次の命令の場所を示すのが**プログラムカウンタ**です。

読み出された命令は、**命令レジスタ**に保持されます。

```text
プログラムカウンタ
→ 次の命令のアドレス

命令レジスタ
→ 読み出した命令そのもの
```

レジスタの役割は、[プログラムカウンタとは？CPUレジスタの役割と割込み時の退避](/fe/cpu-registers/)で詳しく整理しています。

### 2. 命令の解読

次に、読み出した命令が何をする命令なのかを解読します。

例えば、

```text
加算する
比較する
データを移動する
分岐する
```

など、CPUが実行すべき処理を判断します。

この段階を**デコード**と呼ぶこともあります。

### 3. オペランド読出し

命令を実行するために必要なデータを読み出します。

**オペランド**とは、演算や処理の対象になるデータのことです。

命令中で操作と対象をどう指定するかは、[命令語の構成](/fe/instruction-format/)で整理しています。

例えば、

```text
3 + 5
```

という加算なら、`3` と `5` がオペランドです。

初心者のうちは、

```text
オペランド
→ 計算や処理に使うデータ
```

と理解すれば十分です。

### 4. 命令の実行

必要なデータがそろったら、演算装置などが実際の処理を行います。

```text
命令を理解した
＋
必要なデータがそろった
↓
命令を実行する
```

処理によっては、このあと結果をレジスタや主記憶へ書き込みます。

この一連の流れを繰り返すことで、CPUはプログラムを実行します。

このテーマは、基本情報技術者試験の「コンピュータ構成要素」と関係する内容です。公式の出題範囲やシラバスは、[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html) から確認できます。

## 科目Aでどう出る？

科目Aでは、命令実行の各段階を並べ替える問題が出ます。

試験中は、次の順序をそのまま思い出す方法もあります。

```text
フェッチ
↓
解読
↓
オペランド読出し
↓
実行
```

ただし、順番を忘れたときは**因果関係**で復元できます。

### まず「命令フェッチ」を探す

CPUは、命令を読み出さなければその内容を解読できません。

したがって、基本的には命令フェッチが先です。

```text
命令を取得
↓
命令を理解
```

「解読 → フェッチ」の順になっている選択肢は切りやすくなります。

### 「解読」と「オペランド読出し」を切り分ける

何の命令か分からなければ、どのデータが必要なのか判断できません。

```text
命令を解読
↓
必要なデータが分かる
↓
オペランドを読み出す
```

したがって、基本の整理では**解読が先、オペランド読出しが後**です。

### 最後は「実行」

命令を理解し、必要なデータを用意してから処理を実行します。

```text
指示を取得
→ 指示を理解
→ データを用意
→ 実行
```

この流れで、順序が不自然な選択肢を消していきます。

## どんな場面で使う？

CPUの命令実行サイクルは、CPU内部の各装置やレジスタの役割をつなげて理解するときに役立ちます。

例えば、次の用語がばらばらに見えていても、命令実行の流れに並べると関係が見えます。

```text
プログラムカウンタ
↓ 次の命令の場所を示す

主記憶
↓ 命令フェッチ

命令レジスタ
↓ 読み出した命令を保持

命令デコーダ
↓ 命令を解読

レジスタ・主記憶
↓ オペランドを読み出す

演算装置
↓ 命令を実行
```

そのため、命令実行サイクルを理解した後に[CPUレジスタの記事](/fe/cpu-registers/)を読むと、プログラムカウンタや命令レジスタの役割を流れの中で理解しやすくなります。

## よくある誤解・混同

### オペランドは命令そのもの？

違います。

```text
命令
→ CPUに何をするか指示するもの

オペランド
→ その処理で使うデータ
```

例えば、概念的に

```text
ADD 3, 5
```

と考えるなら、`ADD` が加算を指示する部分で、`3` と `5` が演算対象のオペランドです。

### 命令フェッチとオペランド読出しは同じ？

どちらも「読み出す」ため混同しやすいですが、読み出すものが違います。

```text
命令フェッチ
→ 命令を読み出す

オペランド読出し
→ 命令の実行に必要なデータを読み出す
```

**何を読み出しているか**で切り分けます。

### 命令フェッチの前に解読できる？

基本的にはできません。

まだ命令を読み出していないため、何の命令なのか解読できないからです。

```text
取ってくる
→ 読む
```

の順と考えます。

### オペランドを読み出してから命令を解読する？

FE試験の基本的な整理では、命令を解読してから必要なオペランドを読み出します。

```text
何をする命令か分かる
↓
何のデータが必要か分かる
```

順序問題では、この因果関係を判断軸にします。

### CPUは4段階だけで動く？

実際のCPU内部では、より細かな処理や並列化が行われることがあります。

ただしFE試験の基本問題では、まず

```text
命令フェッチ
→ 命令の解読
→ オペランド読出し
→ 命令の実行
```

という基本の流れを押さえることを優先します。

## まとめ（試験直前用）

- CPUの基本的な命令実行順序は、**フェッチ → 解読 → オペランド読出し → 実行**
- 命令フェッチは「命令を取ってくる」処理
- オペランドは「計算や処理に使うデータ」
- 順番を忘れたら、**指示を取る → 理解する → 材料を用意する → 作業する**で復元する
- CPUレジスタは、この命令実行の流れとつなげて理解する

{% include fe_article_footer.html %}
