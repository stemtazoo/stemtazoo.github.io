---
layout: page
title: インスペクションとは？ウォークスルー・ラウンドロビン・パスアラウンドとの違い【基本情報技術者試験】
description: ソフトウェアレビューの代表手法であるインスペクションを、ウォークスルー・ラウンドロビン・パスアラウンドとの違いから整理します。モデレータ、役割分担、チェックリスト、正式な記録という判断語をFE科目A向けに解説します。
permalink: /fe/software-review-inspection/
tags: [fe, fe-technology, software-engineering, review]
fe_section: テクノロジ系
fe_subsection: ソフトウェア開発管理技術
fe_order: 545
date: 2026-09-08
last_modified_at: 2026-11-04
---

## まず結論

**インスペクション**は、参加者の役割をあらかじめ明確にし、モデレータの進行の下で、チェックリストなどを使って成果物を確認し、正式な記録を残すレビュー手法です。

基本情報技術者試験では、次の判断語をセットで覚えると切り分けやすくなります。

```text
役割を明確にする
+ モデレータ
+ チェックリスト
+ 正式な記録
→ インスペクション
```

このページは、**インスペクション・ウォークスルー・ラウンドロビン・パスアラウンドを比較して見分ける記事**です。ウォークスルー単体の進め方や狙いは、[ウォークスルーとは？](/fe/walkthrough-review/) を参照してください。

## 直感的な説明

ソフトウェアレビューは、設計書やプログラムなどの成果物を複数人で確認し、欠陥や問題点を早い段階で見つける活動です。

レビュー手法によって、進め方の「正式さ」が異なります。

```text
作成者が説明しながら確認
→ ウォークスルー

参加者が順番に発言・司会
→ ラウンドロビン

役割を決めて正式に確認
→ インスペクション

成果物を回覧してコメント
→ パスアラウンド
```

インスペクションは、この中でも特に**形式的なレビュー**です。

## 定義・仕組み

インスペクションでは、レビュー参加者がそれぞれ明確な役割を持ちます。

代表的な役割には、次のようなものがあります。

- モデレータ：レビュー全体を進行・調整する
- オーナー／作成者：成果物の作成者
- インスペクタ／レビューア：問題点を確認する
- プレゼンタ：成果物の内容を説明する
- スクライブ：指摘事項や結果を記録する

実際の名称や役割分担は組織や手法によって異なることがありますが、FE試験では、**役割が明確に決められている**ことが重要な特徴です。

また、インスペクションでは、チェックリストなどの基準を使って成果物を確認し、レビュー結果を正式に記録します。

```text
事前準備
↓
役割分担
↓
チェックリスト等で確認
↓
指摘事項を記録
↓
修正・フォロー
```

## 科目Aでどう出る？

科目Aでは、複数のレビュー方法の説明から名称を選ばせる問題に注意します。

### インスペクション

```text
モデレータ
役割分担
チェックリスト
正式な記録
→ インスペクション
```

### ウォークスルー

ウォークスルーは、成果物の作成者が内容を説明しながら、参加者から質問やコメントを受けるレビューです。

```text
作成者が説明
+ 会議形式
+ 参加者が質問・コメント
→ ウォークスルー
```

### ラウンドロビン

ラウンドロビンは、参加者が順番に発言したり、司会・レビュー担当を交代しながら進める方法です。

```text
順番に回す
→ ラウンドロビン
```

### パスアラウンド

パスアラウンドは、レビュー対象となる成果物を複数のレビューアに配布・回覧し、コメントを集める方法です。

```text
成果物を回覧
→ パスアラウンド
```

試験中は、次の表で切り分けると分かりやすいです。

| 問題文の表現 | 判断 |
|---|---|
| 作成者が説明し、参加者が質問する | ウォークスルー |
| 順番に司会・発言を担当する | ラウンドロビン |
| モデレータ・明確な役割・チェックリスト・記録 | インスペクション |
| 成果物を回覧してコメントする | パスアラウンド |

特に迷いやすいのが、**ウォークスルーとインスペクション**です。

どちらも複数人で成果物を確認し、会議形式で実施されることがあります。したがって、**「会議をするかどうか」だけでは切り分けられません。**

試験では、次の2段階で見ると判断しやすくなります。

```text
1. 誰が中心かを見る
   作成者が説明する
   → ウォークスルー

   モデレータが進行する
   → インスペクションの可能性が高い

2. どれだけ形式的かを見る
   柔軟に質問・コメント
   → ウォークスルー

   明確な役割分担
   + チェックリスト
   + 正式な記録
   → インスペクション
```

つまり、**「作成者中心か、モデレータ中心か」→「柔軟か、形式的か」**の順に見るのがポイントです。


### 触って覚える：4つのレビュー方法を場面から見分ける

**見るポイント：**「会議形式かどうか」ではなく、**作成者の説明・順番交代・モデレータと正式な手順・成果物の回覧**のどれが中心かを読み取ります。

まず場面を読んで予想し、選択肢を押してください。選んだ後に正誤と理由が表示されます。4場面は何度でも練習でき、場面を移ると前の回答は消えます。

<div id="fe-review-method-quiz" class="fe-review-method-quiz">
  <div class="fe-review-method-quiz__interactive" hidden>
    <p class="fe-review-method-quiz__counter" data-counter>場面 1 / 4</p>
    <div class="fe-review-method-quiz__scenario">
      <strong>レビュー中の状況</strong>
      <p data-scenario></p>
    </div>
    <p class="fe-review-method-quiz__prompt">どのレビュー方法でしょうか？</p>
    <div class="fe-review-method-quiz__choices" role="group" aria-label="レビュー方法を選ぶ">
      <button type="button" data-answer="walkthrough" aria-pressed="false">ウォークスルー</button>
      <button type="button" data-answer="inspection" aria-pressed="false">インスペクション</button>
      <button type="button" data-answer="roundrobin" aria-pressed="false">ラウンドロビン</button>
      <button type="button" data-answer="passaround" aria-pressed="false">パスアラウンド</button>
    </div>
    <div class="fe-review-method-quiz__feedback" data-feedback role="status" aria-live="polite" aria-atomic="true" hidden></div>
    <div class="fe-review-method-quiz__nav">
      <button type="button" data-prev>前の場面</button>
      <button type="button" data-next>次の場面</button>
      <button type="button" data-reset>同じ場面をやり直す</button>
    </div>
  </div>
  <div class="fe-review-method-quiz__fallback">
    **JavaScriptなしでも復習できます：** 作成者が説明するのがウォークスルー、参加者が順番に進めるのがラウンドロビン、役割・チェックリスト・記録をそろえるのがインスペクション、成果物を回覧するのがパスアラウンドです。詳しい比較は直前の表も参照してください。
  </div>
</div>

<style>
.fe-review-method-quiz{max-width:740px;margin:1.2rem auto;padding:1rem;border:1px solid #93a9b7;border-radius:12px}
.fe-review-method-quiz [hidden]{display:none!important}
.fe-review-method-quiz__counter{font-size:.9rem;margin:0 0 .6rem;color:inherit}
.fe-review-method-quiz__scenario{padding:.85rem 1rem;border-radius:9px;background:#edf3f6;color:#203846}
.fe-review-method-quiz__scenario p{margin:.45rem 0 0}
.fe-review-method-quiz__prompt{font-weight:700;margin:.9rem 0 .55rem}
.fe-review-method-quiz__choices{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.55rem}
.fe-review-method-quiz button{min-height:44px;padding:.65rem .75rem;font:inherit;text-align:center;border:1px solid #698495;border-radius:8px;background:#fff;color:#243a49;cursor:pointer;overflow-wrap:anywhere}
.fe-review-method-quiz button[aria-pressed="true"]{background:#15567d;color:#fff;border-color:#15567d;font-weight:700}
.fe-review-method-quiz button:focus-visible{outline:3px solid #e19a39;outline-offset:2px}
.fe-review-method-quiz button:disabled{opacity:.48;cursor:not-allowed}
.fe-review-method-quiz__feedback{padding:.8rem 1rem;margin-top:.75rem;border:1px solid #8ba7b5;border-radius:8px;background:#f0f6f8;color:#203846}
.fe-review-method-quiz__feedback strong{display:block;margin-bottom:.3rem}
.fe-review-method-quiz__nav{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.9rem;justify-content:space-between}
@media(max-width:520px){.fe-review-method-quiz{padding:.7rem}.fe-review-method-quiz__choices{grid-template-columns:1fr}.fe-review-method-quiz__nav button{flex:1 1 45%}}
@media(prefers-color-scheme:dark){.fe-review-method-quiz__scenario,.fe-review-method-quiz__feedback{background:#293d47;color:#f3f6f7}.fe-review-method-quiz button{background:#263943;color:#f4f6f7}.fe-review-method-quiz button[aria-pressed="true"]{background:#36799f;color:#fff}}
</style>

<script>
(function(){
  function init(){
    var root=document.getElementById('fe-review-method-quiz');
    if(!root||root.dataset.ready==='true')return;
    var interactive=root.querySelector('.fe-review-method-quiz__interactive');
    var fallback=root.querySelector('.fe-review-method-quiz__fallback');
    var scenario=root.querySelector('[data-scenario]');
    var feedback=root.querySelector('[data-feedback]');
    var counter=root.querySelector('[data-counter]');
    var prev=root.querySelector('[data-prev]');
    var next=root.querySelector('[data-next]');
    var reset=root.querySelector('[data-reset]');
    var buttons=Array.prototype.slice.call(root.querySelectorAll('[data-answer]'));
    if(!interactive||!fallback||!scenario||!feedback||!counter||!prev||!next||!reset||buttons.length!==4)return;
    var cases=[
      {text:'成果物の作成者が設計書の処理を順に説明し、参加者がその場で質問やコメントをしている。',answer:'walkthrough',reason:'作成者が説明しながら確認することが中心なので、ウォークスルーです。会議形式というだけでは判断できません。'},
      {text:'モデレータが進行し、参加者には明確な役割がある。チェックリストに従って欠陥を確認し、結果を正式に記録する。',answer:'inspection',reason:'モデレータ・役割分担・チェックリスト・正式な記録という組合せがインスペクションの決め手です。'},
      {text:'参加者が順番にレビューの司会や発言を担当し、全員に順番が回るように進めている。',answer:'roundrobin',reason:'順番に担当や発言を回すことがラウンドロビンの特徴です。成果物の回覧とは異なります。'},
      {text:'作成した設計書を複数のレビューアに配布・回覧し、それぞれのコメントを集めている。',answer:'passaround',reason:'成果物を配布・回覧して意見を集めるので、パスアラウンドです。'}
    ];
    var labels={walkthrough:'ウォークスルー',inspection:'インスペクション',roundrobin:'ラウンドロビン',passaround:'パスアラウンド'};
    var index=0;
    function clearAnswer(){
      buttons.forEach(function(button){button.setAttribute('aria-pressed','false');});
      feedback.textContent='';
      feedback.hidden=true;
    }
    function render(){
      scenario.textContent=cases[index].text;
      counter.textContent='場面 '+(index+1)+' / '+cases.length;
      prev.disabled=index===0;
      next.textContent=index===cases.length-1?'最初の場面に戻る':'次の場面';
      clearAnswer();
    }
    buttons.forEach(function(button){
      button.addEventListener('click',function(){
        var chosen=button.getAttribute('data-answer');
        buttons.forEach(function(item){item.setAttribute('aria-pressed',String(item===button));});
        var correct=chosen===cases[index].answer;
        feedback.textContent='';
        var heading=document.createElement('strong');
        heading.textContent=correct?'正解です！':'正解は「'+labels[cases[index].answer]+'」です';
        var reason=document.createElement('span');
        reason.textContent=cases[index].reason;
        feedback.appendChild(heading);
        feedback.appendChild(reason);
        feedback.hidden=false;
      });
    });
    prev.addEventListener('click',function(){if(index>0){index--;render();}});
    next.addEventListener('click',function(){index=(index+1)%cases.length;render();});
    reset.addEventListener('click',clearAnswer);
    render();
    interactive.hidden=false;
    fallback.hidden=true;
    root.dataset.ready='true';
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);
  else init();
}());
</script>

※ 学習用に特徴を強調した例です。実際のレビューでは、複数の方法に共通する運営・記録が使われることもあります。


## どんな場面で使う？

インスペクションは、設計書や仕様書、プログラムなどの成果物について、重要な欠陥を早期に発見したい場面で使われます。

開発の後工程で欠陥が見つかるほど、修正の影響範囲やコストは大きくなりやすいため、レビューによって早めに問題を見つけることが重要です。

```text
実装後に欠陥発見
→ 修正範囲が大きくなりやすい

設計・レビュー段階で欠陥発見
→ 早い段階で修正できる
```

FE試験では、レビューの細かな運用手順よりも、**どのレビュー手法がどの特徴を持つか**を見分けられることが重要です。

## よくある誤解・混同

### インスペクションとウォークスルーは同じ？

違います。

ウォークスルーは、作成者が説明しながら進める比較的柔軟なレビューです。

一方、インスペクションは、役割分担や進行方法をあらかじめ決めて実施する、より形式的なレビューです。

```text
作成者の説明が中心
→ ウォークスルー

役割分担・モデレータ・記録
→ インスペクション
```

### 会議形式ならウォークスルー？

いいえ。

ウォークスルーもインスペクションも、複数人が集まってレビューすることがあります。

そのため、**「会議形式」という言葉だけでは判断しません。**

```text
会議形式
+ 作成者が説明
→ ウォークスルー

会議形式
+ モデレータ
+ 明確な役割
+ チェックリスト・正式記録
→ インスペクション
```

### モデレータがいれば必ずインスペクション？

モデレータという語は強い手掛かりですが、それだけで判断せず、**明確な役割分担、チェックリスト、正式な記録**と組み合わせて見ます。

### パスアラウンドは会議形式？

基本的には、成果物を回覧してコメントを集める方式です。

```text
会議で作成者が説明
→ ウォークスルー

成果物を回してコメント
→ パスアラウンド
```

### ラウンドロビンとパスアラウンドは同じ？

違います。

```text
人の順番を回す
→ ラウンドロビン

成果物を回す
→ パスアラウンド
```

この違いで覚えると整理しやすくなります。

## まとめ（試験直前用）

- 作成者が説明する → ウォークスルー
- 参加者が順番に発言・司会する → ラウンドロビン
- モデレータ・役割分担・チェックリスト・正式な記録 → インスペクション
- 成果物を回覧してコメントする → パスアラウンド
- 「会議形式」だけではウォークスルーとインスペクションを区別できない
- インスペクションは、他のレビュー手法より形式的

```text
説明する
→ ウォークスルー

順番に回す
→ ラウンドロビン

正式・役割・モデレータ
→ インスペクション

回覧する
→ パスアラウンド
```

> **「説明・順番・正式・回覧」で切り分ける。**

{% include fe_article_footer.html %}
