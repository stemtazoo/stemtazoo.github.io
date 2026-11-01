---
layout: page
title: 2相コミットとは？分散データベースで更新をそろえる仕組み【基本情報技術者試験】
description: 2相コミットを、複数サイトに更新可能かを確認し、全員が同意した場合だけ一斉に確定する方式として整理し、調停者・参加者、第1相・第2相、排他制御・ロールバック・ストアドプロシージャとの違いをFE試験向けに解説します。
permalink: /fe/two-phase-commit/
tags: [fe, fe-technology, database]
fe_section: テクノロジ系
fe_subsection: データベース
fe_order: 20
date: 2026-06-27
last_modified_at: 2026-11-01
---

## まず結論

2相コミットとは、**分散データベースで、複数サイトの更新を「全員で確定」または「全員で中止」にそろえる仕組み**です。

基本情報技術者試験では、次の表現が決め手になります。

```text
複数サイトへ更新可能か問い合わせる
＋
すべてのサイトが可能なら確定する
→ 2相コミット
```

いきなり更新を確定せず、まず全参加者へ確認し、その後に全体を確定または中止する点が重要です。

## 直感的な説明

2相コミットは、**全員に準備できたか確認してから、一斉に実行する仕組み**と考えると分かりやすいです。

例えば、複数の支店で同じ取引に関するデータを更新するとします。

```text
支店A：更新成功
支店B：更新失敗
```

このように一部だけ更新されると、データのつじつまが合わなくなります。

そこで、最初に全支店へ確認します。

```text
調停者：
「全員、更新を確定できる状態ですか？」
```

全員が「できます」と答えた場合だけ、確定を指示します。

```text
全員が可
→ 全員コミット
```

1つでも「できません」があれば、全体を中止します。

```text
1つでも不可
→ 全員ロールバック
```

### 送金の例：2つのデータベースで結果をそろえる

例えば、A銀行の口座からB銀行の口座へ1万円を送金する処理を考えます。

```text
A銀行のDB：残高を1万円減らす
B銀行のDB：残高を1万円増やす
```

A銀行だけ更新され、B銀行の更新が失敗すると、1万円が消えたような不整合が生じます。

そこで2相コミットでは、次の順番で判断します。

```text
【第1相：準備・確認】
調停者「A銀行、B銀行とも確定できますか？」
        ↓
A銀行：可       B銀行：可
        ↓
【第2相：確定】
調停者「両方ともコミットしてください」
```

一方、B銀行が「不可」と回答した場合は、**A銀行も含めて更新を中止**します。第1相の「可」は、更新をすでに確定したという意味ではありません。

```text
A銀行：可       B銀行：不可
        ↓
調停者「両方ともロールバックしてください」
```

**「確認する段階」と「確定・中止を指示する段階」を分ける**ことが、2相コミットの名前の由来です。


### 触って覚える：2相コミットの準備と最終決定

**「全員が準備OK」と「1人だけ準備NG」では、最終結果がどう変わるでしょうか？** 参加者A・B・Cの回答を切り替え、まず結論を予想してから第1相と第2相を順番に実行してください。

<div id="fe-2pc-demo" class="fe-2pc-demo">
  <div class="fe-2pc-demo__presets">
    <button type="button" data-preset="all">全員OKの例</button>
    <button type="button" data-preset="one">BだけNGの例</button>
  </div>
  <fieldset class="fe-2pc-demo__responses">
    <legend>各参加者の準備結果を設定する</legend>
    <label>参加者A <select data-participant="A"><option value="yes">準備OK</option><option value="no">準備NG</option></select></label>
    <label>参加者B <select data-participant="B"><option value="yes">準備OK</option><option value="no">準備NG</option></select></label>
    <label>参加者C <select data-participant="C"><option value="yes">準備OK</option><option value="no">準備NG</option></select></label>
  </fieldset>
  <fieldset class="fe-2pc-demo__prediction">
    <legend>予想：全体の最終結果は？</legend>
    <label><input type="radio" name="fe-2pc-guess" value="commit">全員コミット</label>
    <label><input type="radio" name="fe-2pc-guess" value="abort">全員中止</label>
  </fieldset>
  <div class="fe-2pc-demo__actions">
    <button type="button" id="fe-2pc-next">第1相へ：準備確認</button>
    <button type="button" id="fe-2pc-prev">1段階戻る</button>
    <button type="button" id="fe-2pc-reset">最初から</button>
  </div>
  <p id="fe-2pc-feedback" role="status" aria-live="polite">予想を選んで第1相へ進めてください。</p>
  <ol class="fe-2pc-demo__phases" aria-label="2相コミットの処理段階">
    <li id="fe-2pc-phase-0">開始前：調停者はまだ問い合わせていません。</li>
    <li id="fe-2pc-phase-1">第1相：各参加者に準備できるか問い合わせる。</li>
    <li id="fe-2pc-phase-2">第2相：全員OKならCOMMIT、1人でもNGならABORTを指示する。</li>
  </ol>
  <div class="fe-2pc-demo__cards" aria-label="参加者ごとの状態">
    <section><h4>参加者A</h4><p id="fe-2pc-status-A">未確認</p></section>
    <section><h4>参加者B</h4><p id="fe-2pc-status-B">未確認</p></section>
    <section><h4>参加者C</h4><p id="fe-2pc-status-C">未確認</p></section>
  </div>
  <p id="fe-2pc-decision" class="fe-2pc-demo__decision" aria-live="polite">調停者の決定：まだありません。</p>
  <p class="fe-2pc-demo__note">第1相の「準備OK」は、まだコミット完了ではありません。第2相で調停者が最終決定を送り、全参加者の処理を確定または中止します。ケースを変えるとシミュレーションを最初からやり直します。</p>
</div>
<noscript><p>JavaScriptが使えない場合：全員OKなら「準備確認 → 全員コミット」、BだけNGなら「準備確認 → 全員中止」です。上の本文にも同じ例を掲載しています。</p></noscript>

<style>
.fe-2pc-demo{border:1px solid #94a3b8;border-radius:12px;padding:1rem;margin:1rem 0}
.fe-2pc-demo__presets,.fe-2pc-demo__actions{display:flex;gap:.5rem;flex-wrap:wrap;margin:.7rem 0}
.fe-2pc-demo button{border:1px solid #64748b;border-radius:6px;background:#e2e8f0;color:#172033;padding:.5rem .7rem;cursor:pointer}
.fe-2pc-demo button:disabled{opacity:.45;cursor:not-allowed}
.fe-2pc-demo fieldset{border:1px solid #94a3b8;border-radius:8px;margin:.8rem 0;padding:.7rem}
.fe-2pc-demo legend{font-weight:700}
.fe-2pc-demo__responses{display:flex;flex-wrap:wrap;gap:.75rem}
.fe-2pc-demo__responses label{display:flex;flex-direction:column;gap:.3rem;flex:1 1 130px}
.fe-2pc-demo select{width:100%;padding:.45rem;border:1px solid #64748b;border-radius:6px;background:var(--background-color,#fff);color:var(--text-color,#172033)}
.fe-2pc-demo__prediction{display:flex;gap:1rem;flex-wrap:wrap}
.fe-2pc-demo__phases{padding-left:1.5rem}
.fe-2pc-demo__phases li{padding:.35rem;margin:.3rem 0;border-left:3px solid #94a3b8}
.fe-2pc-demo__phases li.is-current{border-color:#2563eb;background:rgba(59,130,246,.1);font-weight:700}
.fe-2pc-demo__cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.6rem}
.fe-2pc-demo__cards section{border:1px solid #94a3b8;border-radius:8px;padding:.5rem;min-width:0}
.fe-2pc-demo__cards h4{font-size:1rem;margin:0 0 .4rem}
.fe-2pc-demo__cards p{margin:0;overflow-wrap:anywhere}
.fe-2pc-demo__decision{padding:.6rem;border-left:4px solid #2563eb;background:rgba(59,130,246,.08);font-weight:700}
.fe-2pc-demo__note{font-size:.9rem}
.fe-2pc-demo :focus-visible{outline:3px solid #2563eb;outline-offset:2px}
@media(max-width:560px){.fe-2pc-demo{padding:.65rem}.fe-2pc-demo__cards{grid-template-columns:1fr}.fe-2pc-demo__actions button{flex:1 1 45%}}
</style>
<script>
(function(){
  "use strict";
  const root=document.getElementById("fe-2pc-demo");if(!root)return;
  const $=id=>root.querySelector("#"+id),names=["A","B","C"];
  const selects=names.map(n=>root.querySelector('[data-participant="'+n+'"]'));
  const next=$("fe-2pc-next"),prev=$("fe-2pc-prev");
  let phase=0,guess=null,answer="";
  function outcome(){return selects.every(s=>s.value==="yes")?"commit":"abort";}
  function reset(message){
    phase=0;guess=null;answer=message||"予想を選んで第1相へ進めてください。";
    root.querySelectorAll('input[name="fe-2pc-guess"]').forEach(r=>r.checked=false);
    render();
  }
  function render(){
    const result=outcome();
    for(let i=0;i<3;i++){
      const name=names[i],status=$("fe-2pc-status-"+name);
      status.textContent=phase===0?"未確認":phase===1?(selects[i].value==="yes"?"準備OK（未確定）":"準備NG（未確定）"):(result==="commit"?"コミット確定":"中止・ロールバック");
      $("fe-2pc-phase-"+i).classList.toggle("is-current",phase===i);
    }
    $("fe-2pc-decision").textContent=phase===0?"調停者の決定：まだありません。":phase===1?"調停者の決定：全員の回答を確認中。まだ最終決定していません。":"調停者の決定："+(result==="commit"?"全員にCOMMITを指示":"全員にABORTを指示");
    $("fe-2pc-feedback").textContent=answer;
    next.textContent=phase===0?"第1相へ：準備確認":"第2相へ：最終決定";
    next.disabled=phase===2;prev.disabled=phase===0;
    selects.forEach(s=>s.disabled=phase!==0);
    root.querySelectorAll('input[name="fe-2pc-guess"]').forEach(r=>r.disabled=phase!==0);
  }
  next.addEventListener("click",()=>{
    if(phase===0){
      const selected=root.querySelector('input[name="fe-2pc-guess"]:checked');
      guess=selected?selected.value:null;phase=1;
      answer="第1相：参加者の準備結果を集めました。『準備OK』はコミット済みではありません。";
    }else if(phase===1){
      phase=2;const result=outcome();
      const verdict=result==="commit"?"全員コミット":"全員中止";
      answer=(guess?(guess===result?"予想正解！ ":"予想と違いました。 "):"")+"第2相：調停者は「"+verdict+"」を指示しました。"+(result==="commit"?"全員が準備OKだったためです。":"準備NGが1人以上いたためです。");
    }
    render();
  });
  prev.addEventListener("click",()=>{
    if(phase>0)phase--;
    answer="1段階戻しました。最終確定前と確定後の違いを確認しましょう。";
    render();
  });
  $("fe-2pc-reset").addEventListener("click",()=>reset("最初からやり直します。"));
  root.querySelectorAll("[data-preset]").forEach(button=>button.addEventListener("click",()=>{
    selects.forEach((s,i)=>s.value=button.dataset.preset==="one"&&i===1?"no":"yes");
    reset(button.dataset.preset==="one"?"Bだけ準備NGの例です。最終結果を予想してください。":"全員準備OKの例です。最終結果を予想してください。");
  }));
  selects.forEach(s=>s.addEventListener("change",()=>reset("準備結果を変更しました。最終結果を予想してください。")));
  reset();
})();
</script>

## 定義・仕組み

2相コミットでは、中心となる**調停者**と、更新に参加する**参加者**が登場します。

| 役割 | すること |
|---|---|
| 調停者 | 各参加者へ可否を問い合わせ、最終指示を出す |
| 参加者 | 更新を確定できるか回答し、最終指示に従う |

処理は2段階に分かれます。

### 第1相：準備・確認

調停者が、各参加者にコミット可能か問い合わせます。

参加者は、更新を確定できる状態なら「可」、できない場合は「不可」と回答します。

この段階では、まだ最終確定しません。

```text
調停者
→ 参加者A：コミット可能？
→ 参加者B：コミット可能？
→ 参加者C：コミット可能？
```

### 第2相：確定・中止

すべての参加者が「可」なら、調停者は全員へコミットを指示します。

```text
A：可
B：可
C：可
→ 全員コミット
```

1つでも「不可」がある場合は、全員へロールバックを指示します。

```text
A：可
B：不可
C：可
→ 全員ロールバック
```

2相コミットは、この仕組みによって、分散環境でもトランザクションの原子性を保とうとします。

```text
全サイト更新
または
全サイト未更新
```

のどちらかにそろえます。

公式の出題範囲やシラバスは、[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html)から確認できます。

## 科目Aでどう出る？

科目Aでは、問題文の表現から方式を選ばせる問題が中心です。

| 問題文の表現 | 選ぶ用語 |
|---|---|
| 複数サイトに更新可能か問い合わせる | 2相コミット |
| 全参加者の合意後に一斉に確定する | 2相コミット |
| 同じデータへの同時アクセスを制限する | 排他制御 |
| 未確定の更新を処理前へ戻す | ロールバック |
| ログを使って更新を再実行し復旧する | ロールフォワード |
| SQLや処理手順をDBMS側に保存する | ストアドプロシージャ |

試験では、次の3つを見つけます。

```text
複数サイト
全参加者へ確認
全員可なら確定
```

この3つがそろえば、2相コミットを疑います。

### 調停者と参加者を読み分ける

```text
問い合わせる側
→ 調停者

可否を回答する側
→ 参加者
```

調停者は、全参加者から「可」を受け取ったときだけコミットを指示します。

### 第1相と第2相を読み分ける

```text
第1相
→ コミット可能か確認する

第2相
→ コミットまたはロールバックを指示する
```

「確認」と「確定」を混同しないことがポイントです。

## どんな場面で使う？

2相コミットは、1つのトランザクションが複数のデータベースやサイトにまたがる場合に使います。

例えば、次のような処理です。

```text
拠点Aの在庫を減らす
＋
拠点Bの配送情報を登録する
＋
本部の売上を記録する
```

一部だけ成功すると不整合が起こるため、全体の結果をそろえる必要があります。

ただし、複数サイトとの通信や応答待ちが必要になるため、単一サイトの通常のコミットより処理は複雑になります。

## よくある誤解・混同

### 2相コミットと排他制御

どちらもデータの整合性を守りますが、**防ぐ問題が異なります**。

| 用語 | 防ぎたいこと | 問題文の手掛かり |
|---|---|---|
| **2相コミット** | 複数サイトで一部だけ更新が確定する | 全サイトに問い合わせる・全員が可なら確定 |
| **排他制御** | 複数の処理が同じデータを同時更新して矛盾する | ロックする・他の処理を待たせる |

例えば、2相コミットは「A銀行では送金額を減らしたのに、B銀行では増えていない」という**サイト間の確定結果の食い違い**を防ぎます。

一方、排他制御は「同じ口座残高を2つの処理が同時に更新し、片方の変更が失われる」という**処理同士の衝突**を防ぎます。

```text
複数サイトで全員の合意を取る
→ 2相コミット

同じデータを更新中、他の処理を待たせる
→ 排他制御
```

2相コミットの処理中にロックを使う場合もあります。**両者は対立する方式ではなく、目的が違う仕組み**です。

### 2相コミットとロールバック

ロールバックは、処理を取り消して開始前の状態へ戻す操作です。

2相コミットでは、1つでも「不可」があればロールバックを指示しますが、2相コミットそのものは**全参加者へ確認して、全体の最終結果を決める方式**です。

```text
更新前ログで元に戻す
→ ロールバック

複数サイトへ可否を確認する
→ 2相コミット
```

### 2相コミットとロールフォワード

ロールフォワードは、更新後ログを使って、バックアップ取得後の更新を再実行する復旧方法です。

| 用語 | 向き |
|---|---|
| ロールバック | 更新を取り消して戻す |
| ロールフォワード | ログで更新を進めて復旧する |
| 2相コミット | 複数サイトの確定・中止をそろえる |

### 2相コミットと通常のコミット

```text
通常のコミット
→ 1つのトランザクション結果を確定する

2相コミット
→ 複数サイトの合意を確認して全体を確定する
```

「コミット」という名前だけで判断せず、複数サイトと可否確認があるかを見ます。

### 2相コミットとストアドプロシージャ

[ストアドプロシージャ](/fe/stored-procedure/)は、SQLやデータベース処理をDBMS側に保存し、クライアントからまとめて呼び出す仕組みです。

| 用語 | 判断の中心 |
|---|---|
| 2相コミット | 複数サイトの更新結果をそろえる |
| ストアドプロシージャ | DBMS側に処理を保存して呼び出す |

```text
全参加者へ更新可能か確認する
→ 2相コミット

よく使う命令群をDBMS側に保存する
→ ストアドプロシージャ
```

## まとめ（試験直前用）

- 2相コミットは、分散DBで複数サイトの更新結果をそろえる方式
- 第1相でコミット可能か確認する
- 第2相でコミットまたはロールバックを指示する
- 全参加者が可ならコミット、1つでも不可ならロールバック
- SQLや処理手順をDBMS側に保存するのはストアドプロシージャ

{% include fe_article_footer.html %}
