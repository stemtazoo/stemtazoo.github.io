---
layout: page
title: 共有ロックと専有ロックとは？ロックの両立性の見分け方【基本情報技術者試験】
description: 共有ロックと専有ロックの違いを、読み取り・更新との対応、ロックの両立性、ロック待ち、デッドロックとの関係から整理し、基本情報技術者試験で選択肢を切る判断軸を解説します。
permalink: /fe/shared-exclusive-lock/
tags: [fe, fe-technology, database]
fe_section: テクノロジ系
fe_subsection: データベース
date: 2026-07-27
last_modified_at: 2026-11-02
---

## まず結論

**共有ロック**は主に読み取り用、**専有ロック**は主に更新用のロックです。

基本情報技術者試験では、次のように切り分けます。

```text
共有ロック同士
→ 共存できる

共有ロックと専有ロック
→ 共存できない

専有ロック同士
→ 共存できない
```

つまり、

> **共有ロック同士だけは両立し、専有ロックが関わる組合せは両立しない**

と覚えると判断しやすくなります。

---

## 直感的な説明

同じ資料を複数人で読む場面を考えます。

```text
読む人A
読む人B
```

読むだけなら、同じ資料を同時に見ても問題ありません。

これが共有ロック同士の状態です。

一方、誰かが資料を書き換えている途中に別の人が読んだり、同時に別の内容へ書き換えたりすると、内容が食い違う可能性があります。

```text
読む × 読む
→ 同時にできる

読む × 書く
→ 同時にできない

書く × 読む
→ 同時にできない

書く × 書く
→ 同時にできない
```

共有ロックを「読む」、専有ロックを「書く」と置き換えるとイメージしやすいです。

---


### 触って覚える：共有ロックと専有ロックの両立性

**T1がロックを保持している間に、T2もロックを取得できるでしょうか？** T1とT2のロック種別を選び、T2の結果を予想してください。その後、予想欄の下にある「T1がロック取得」→「T2がロック要求」→「T1がロック解放」の順にボタンを押し、1操作ずつ進めます。**共有＋共有だけが同時取得できる**ことを4パターンで確認します。

これは**同じ1件のデータに対し、異なるトランザクションT1・T2がロックを要求する単純化モデル**です。共有ロックをS、専有ロックをXとします。待機したT2はT1の解放後に自動で再試行するものとします。公平性・待ち行列・ロックの昇格・タイムアウト・MVCCなどのDBMS固有の処理は再現しません。

{% include study_demo_assets.html %}

<div class="fe-lock-compat-demo study-demo" id="fe-lock-compat-demo">
  <div class="fe-lock-compat-demo__controls study-demo__controls">
    <label for="fe-lock-t1">T1が先に取得するロック
      <select id="fe-lock-t1">
        <option value="S">共有ロック（S）：読み取り</option>
        <option value="X">専有ロック（X）：更新</option>
      </select>
    </label>
    <label for="fe-lock-t2">T2が要求するロック
      <select id="fe-lock-t2">
        <option value="S">共有ロック（S）：読み取り</option>
        <option value="X">専有ロック（X）：更新</option>
      </select>
    </label>
  </div>
  <div class="fe-lock-compat-demo__presets" aria-label="比較する組合せ">
    <button type="button" data-lock-case="SS" data-demo-choice="SS">S＋S</button>
    <button type="button" data-lock-case="SX" data-demo-choice="SX">S＋X</button>
    <button type="button" data-lock-case="XS" data-demo-choice="XS">X＋S</button>
    <button type="button" data-lock-case="XX" data-demo-choice="XX">X＋X</button>
  </div>
  <fieldset class="fe-lock-compat-demo__prediction">
    <legend>予想：T1が保持中、T2は取得できる？</legend>
    <label><input type="radio" name="fe-lock-guess" value="yes">取得できる</label>
    <label><input type="radio" name="fe-lock-guess" value="no">待機する</label>
  </fieldset>
  <p class="study-demo__guide" id="fe-lock-guide" role="status" aria-live="polite">予想したら、すぐ下の「T1がロック取得」を押してください。予想を選ばずに進めることもできます。</p>
  <div class="fe-lock-compat-demo__actions study-demo__actions">
    <button type="button" id="fe-lock-next" aria-describedby="fe-lock-guide">T1がロック取得</button>
    <button type="button" id="fe-lock-prev">1操作戻る</button>
    <button type="button" id="fe-lock-reset">最初から</button>
  </div>
  <div class="fe-lock-compat-demo__states" aria-label="ロックの現在状態">
    <section><h4>トランザクションT1</h4><p id="fe-lock-state-t1">まだロックを取得していません。</p></section>
    <section><h4>トランザクションT2</h4><p id="fe-lock-state-t2">まだロックを要求していません。</p></section>
  </div>
  <p id="fe-lock-feedback" role="status" aria-live="polite">まずロックの組合せを選んで予想してください。</p>
  <p id="fe-lock-reason" aria-live="polite">最初にT1がロックを取得し、次にT2が要求します。</p>
  <ol id="fe-lock-log" aria-label="ロック取得と解除の履歴"><li>まだ操作していません。</li></ol>
  <table>
    <caption>同じデータへのロック両立性（異なるトランザクション間）</caption>
    <thead><tr><th scope="col">T1の保持</th><th scope="col">T2の要求：共有（S）</th><th scope="col">T2の要求：専有（X）</th></tr></thead>
    <tbody>
      <tr><th scope="row">共有（S）</th><td>○ 取得できる</td><td>× 待機</td></tr>
      <tr><th scope="row">専有（X）</th><td>× 待機</td><td>× 待機</td></tr>
    </tbody>
  </table>
  <p class="fe-lock-compat-demo__note">ロック待ちが1つあるだけではデッドロックではありません。T1が解放できればT2は進めます。複数の資源を互いに待つデッドロックは<a href="/fe/deadlock/">デッドロックの記事</a>で確認できます。</p>
</div>
<noscript><p>JavaScript無効時は上の両立性表をご覧ください。T1が共有ロックならT2の共有ロックのみ取得可能、T1が専有ロックならT2のどちらの要求も待機します。</p></noscript>

<style>
.fe-lock-compat-demo{border:1px solid #94a3b8;border-radius:12px;padding:1rem;margin:1.2rem 0}
.fe-lock-compat-demo__controls,.fe-lock-compat-demo__states{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.65rem}
.fe-lock-compat-demo__controls label{display:flex;flex-direction:column;gap:.35rem}
.fe-lock-compat-demo select{padding:.45rem;min-width:0;width:100%;border:1px solid #64748b;border-radius:6px;background:var(--background-color,#fff);color:var(--text-color,#172033)}
.fe-lock-compat-demo__presets,.fe-lock-compat-demo__actions{display:flex;gap:.45rem;flex-wrap:wrap;margin:.8rem 0}
.fe-lock-compat-demo button{padding:.5rem .75rem;border:1px solid #64748b;border-radius:6px;background:#e2e8f0;color:#172033;cursor:pointer}
.fe-lock-compat-demo__presets{display:grid;grid-template-columns:repeat(4,minmax(0,1fr))}
.fe-lock-compat-demo button:disabled{opacity:.45;cursor:not-allowed}
.fe-lock-compat-demo__prediction{display:flex;flex-wrap:wrap;gap:.8rem;border:1px solid #94a3b8;border-radius:8px;padding:.65rem}
.fe-lock-compat-demo__prediction legend{font-weight:700}
.fe-lock-compat-demo__states section{border:1px solid #94a3b8;border-radius:8px;padding:.65rem;min-width:0}
.fe-lock-compat-demo__states h4{font-size:1rem;margin:0 0 .4rem}
.fe-lock-compat-demo__states p{margin:0}
.fe-lock-compat-demo table{border-collapse:collapse;width:100%;margin:.8rem 0}
.fe-lock-compat-demo th,.fe-lock-compat-demo td{border:1px solid #94a3b8;padding:.4rem;text-align:left}
.fe-lock-compat-demo__note{font-size:.9rem}
.fe-lock-compat-demo :focus-visible{outline:3px solid #2563eb;outline-offset:2px}
@media(max-width:560px){.fe-lock-compat-demo{padding:.65rem}.fe-lock-compat-demo__controls,.fe-lock-compat-demo__states{grid-template-columns:1fr}.fe-lock-compat-demo__presets{grid-template-columns:repeat(2,minmax(0,1fr))}.fe-lock-compat-demo__actions button{flex:1 1 43%}}
</style>
<script>
(function(){
  "use strict";
  const root=document.getElementById("fe-lock-compat-demo");if(!root)return;
  const $=id=>root.querySelector("#"+id);
  const t1=$("fe-lock-t1"),t2=$("fe-lock-t2");
  let step=0,feedback="";
  function compatible(){return t1.value==="S"&&t2.value==="S";}
  function label(mode){return mode==="S"?"共有ロック（S）":"専有ロック（X）";}
  function reset(message){
    step=0;feedback=message||"最初の状態です。予想したら、下のボタンで1操作ずつ進めましょう。";
    root.querySelectorAll('input[name="fe-lock-guess"]').forEach(r=>r.checked=false);
    render();
  }
  function render(){
    const yes=compatible(),picked=root.querySelector('input[name="fe-lock-guess"]:checked');
    $("fe-lock-state-t1").textContent=step===0?"未取得":step===3?"解放済み":label(t1.value)+"を保持";
    $("fe-lock-state-t2").textContent=step<2?"未要求":step===2?(yes?label(t2.value)+"を取得済み":"待機中："+label(t2.value)+"を要求"):(yes?"T1解放後も"+label(t2.value)+"を保持":"T1解放後に"+label(t2.value)+"を取得");
    $("fe-lock-next").disabled=step===3;$("fe-lock-prev").disabled=step===0;
    $("fe-lock-next").textContent=step===0?"T1がロック取得":step===1?"T2がロック要求":"T1がロック解放";
    const guides=[
      (picked?"予想を選びました。":"予想したら、")+"すぐ下の「T1がロック取得」を押してください。"+(picked?"":"予想を選ばずに進めることもできます。"),
      (picked?"予想を選びました。":"T2の結果を予想したら、")+"すぐ下の「T2がロック要求」を押して結果を確認してください。",
      "次は、すぐ下の「T1がロック解放」を押し、T2の状態がどうなるか確認してください。",
      "確認は完了です。別の組合せを選んで比べるか、「最初から」で同じ組合せを試せます。"
    ];
    StudyDemoUI.nextAction($("fe-lock-next"),$("fe-lock-guide"),guides[step]);
    root.querySelectorAll('input[name="fe-lock-guess"]').forEach(r=>r.disabled=step>=2);
    $("fe-lock-feedback").textContent=feedback;
    const reasons=[
      "T1が先にロックを取得し、T2が同じデータに要求します。",
      "T1が"+label(t1.value)+"を取得しました。次の「T2がロック要求」で結果を確認します。",
      yes?"共有（S）＋共有（S）なのでT2も取得できます。":"専有（X）が含まれるためT2は待機します。",
      yes?"T1は解放しましたがT2は共有ロックを保持中です。":"T1が解放したため、待機していたT2が取得できました。"
    ];
    $("fe-lock-reason").textContent=reasons[step];
    const items=["T1が"+label(t1.value)+"を取得","T2が"+label(t2.value)+"を要求 → "+(yes?"取得":"待機"),"T1が解除 → "+(yes?"T2は引き続き保持":"T2の待機を解除し取得")];
    const log=$("fe-lock-log");log.replaceChildren();
    (step?items.slice(0,step):["まだ操作していません。"]).forEach(item=>{
      const li=document.createElement("li");li.textContent=item;log.appendChild(li);
    });
    StudyDemoUI.selectChoice(root,t1.value+t2.value);
  }
  $("fe-lock-next").addEventListener("click",()=>{
    if(step>=3)return;
    if(step===1){
      const picked=root.querySelector('input[name="fe-lock-guess"]:checked'),yes=compatible();
      feedback=(picked?(picked.value===(yes?"yes":"no")?"予想正解！ ":"予想と異なりました。 "):"")+(yes?"共有ロック同士なので同時に取得できます。":"T2は取得できず待機します。");
      root.querySelectorAll('input[name="fe-lock-guess"]').forEach(r=>r.checked=false);
    }else if(step===0){feedback="T1がロックを取得しました。次の「T2がロック要求」で結果を確認します。";}
    else{feedback="T1がロックを解放しました。"+(compatible()?"T2は保持を続けます。":"待機していたT2が取得しました。");}
    step++;render();
  });
  root.querySelectorAll('input[name="fe-lock-guess"]').forEach(r=>r.addEventListener("change",render));
  $("fe-lock-prev").addEventListener("click",()=>{if(step>0)step--;feedback="1操作戻しました。";render();});
  $("fe-lock-reset").addEventListener("click",()=>reset());
  [t1,t2].forEach(el=>el.addEventListener("change",()=>reset("ロックの組合せを変更しました。結果を予想してください。")));
  root.querySelectorAll("[data-lock-case]").forEach(b=>b.addEventListener("click",()=>{
    t1.value=b.dataset.lockCase[0];t2.value=b.dataset.lockCase[1];
    reset("組合せ"+b.dataset.lockCase+"に切り替えました。");
  }));
  reset();
})();
</script>

## 定義・仕組み

### 共有ロック

共有ロックは、主にデータを読み取るときに使うロックです。

複数のトランザクションが同じデータを読むだけなら、同時に利用できます。

```text
T1：共有ロックを取得
T2：共有ロックを取得
→ 可能
```

ただし、共有ロック中のデータを別のトランザクションが更新することはできません。

### 専有ロック

専有ロックは、主にデータを更新するときに使うロックです。

対象データを更新している間は、ほかのトランザクションによる読み取りや更新を防ぎます。

```text
T1：専有ロックを取得
T2：共有ロックを取得
→ 不可

T2：専有ロックを取得
→ 不可
```

### ロックの両立性

| すでに掛かっているロック | 新たに共有ロック | 新たに専有ロック |
|---|---:|---:|
| 共有ロック | ○ | × |
| 専有ロック | × | × |

試験では、この表をそのまま覚えるよりも、次の1行を残すと便利です。

```text
共有＋共有だけ○
それ以外は×
```

### ロック待ち

必要なロックを取得できない場合、トランザクションは既存のロックが解除されるまで待ちます。

```text
T1が専有ロック中
↓
T2はロックを取得できない
↓
T1の終了まで待つ
```

この状態をロック待ちと呼びます。

このテーマは基本情報技術者試験のデータベース分野に含まれます。公式の出題範囲は、[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html)から確認できます。

---

## 科目Aでどう出る？

科目Aでは、共有ロックと専有ロックの両立性を問う選択問題がよく出ます。

### 選択肢を切る判断表

| 選択肢の表現 | 判断 |
|---|---|
| 共有ロック中に、別の共有ロックを取得できる | 正しい |
| 共有ロック中に、専有ロックを取得できる | 誤り |
| 専有ロック中に、共有ロックを取得できる | 誤り |
| 専有ロック中に、別の専有ロックを取得できる | 誤り |

試験中は、次の順番で判断します。

```text
1. 既に掛かっているロックを確認
2. 新たに取得したいロックを確認
3. 共有＋共有かどうかを見る
4. 共有＋共有なら可、それ以外は不可
```

### 読み取りと更新に置き換える

用語だけで迷ったら、次のように置き換えます。

```text
共有ロック
→ 読み取り

専有ロック
→ 更新
```

すると、

```text
読む × 読む
→ 可

書くが含まれる
→ 不可
```

と判断できます。

---

## どんな場面で使う？

### 同時実行時のデータ保護

複数の利用者が同じデータを同時に扱うシステムでは、ロックが必要です。

例えば、在庫数が10個の商品を2人が同時に購入するとします。

```text
T1：2個購入
T2：3個購入
```

適切なロックがなければ、片方の更新が上書きされ、在庫数が正しく反映されないことがあります。

更新時に専有ロックを使うことで、同時更新による矛盾を防ぎます。

### 検索と更新の制御

検索だけを行う処理では共有ロック、データを書き換える処理では専有ロックを使います。

```text
SELECT中心の処理
→ 共有ロック

UPDATE・DELETEなどの更新処理
→ 専有ロック
```

ただし、実際のDBMSでは分離レベルや実装方式によって挙動が異なるため、試験では問題文の前提を優先します。

---

## よくある誤解・混同

### 共有ロックなら更新もできる

できません。

共有ロックは読み取り用であり、更新には専有ロックが必要です。

### 専有ロック中でも、読み取りだけならよい

基本的にはできません。

専有ロック中は、そのトランザクションが対象資源を独占しています。

### 共有ロックは1つしか取得できない

違います。

複数のトランザクションが同じ資源に共有ロックを取得できます。

### ロック待ちとデッドロックは同じ

違います。

```text
ロック待ち
→ ほかのトランザクションの終了を待つ

デッドロック
→ 複数のトランザクションが互いのロック解除を待ち続ける
```

例えば、T1が資源A、T2が資源Bをロックしたまま、互いに相手の資源を待つとデッドロックになります。

### 二相ロックは共有ロックと専有ロックの2種類を使うこと

違います。

二相ロックは、

```text
ロックを獲得する段階
↓
ロックを解放する段階
```

の2段階に分ける方式です。

共有ロックと専有ロックの2種類を指す言葉ではありません。

---

## まとめ（試験直前用）

- 共有ロックは主に読み取り、専有ロックは主に更新に使う
- 共有ロック同士だけは同時に取得できる
- 専有ロックが関わる組合せは両立しない
- 迷ったら「読む×読むだけ可」と考える
- ロック待ちとデッドロックを混同しない

{% include fe_article_footer.html %}
