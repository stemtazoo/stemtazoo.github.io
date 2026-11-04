---
layout: page
title: ファシリテータとは？会議で議論を促す進行支援の役割【基本情報技術者試験】
description: "ファシリテータは中立的な立場で発言を促し、論点を整理して合意形成を支える役割。議長・専門家・書記・事務局との違いを具体例と会議シミュレーションで判断できるよう解説します。"
permalink: /fe/facilitator/
tags: [fe, fe-management, project-management]
fe_section: マネジメント系
fe_subsection: プロジェクトマネジメント
fe_order: 390
date: 2026-11-04
last_modified_at: 2026-11-04
related_articles:
  - /fe/stakeholder-analysis/
  - /fe/project-management-subject-groups/
---

## まず結論

**ファシリテータ（Facilitator）は、会議やグループの話合いが円滑に進むよう支援する進行役**です。参加者の発言を促し、論点を整理し、話合いによる合意形成を助けます。

基本情報技術者試験の科目Aでは、次の違いが判断ポイントになります。

- **議論を進めやすくする**：ファシリテータの役割
- **自分の専門的な意見を述べる**：専門家・助言者の役割
- **決定権に基づいて結論を決める**：意思決定者の役割
- **議事録や日程調整を担当する**：書記・事務局の役割

ファシリテータは会議の目的に向かって進行を支えますが、**自分の好みや上司の意向へ議論を誘導することが仕事ではありません。**

## 直感的な説明

新しい設備監視システムの仕様を決める会議を考えます。開発担当は「機能を増やしたい」、現場担当は「操作を簡単にしたい」、保守担当は「点検しやすくしたい」と考えています。

会議で一人が話し続けると、ほかの人の意見が拾われません。また、「機能の数」と「使いやすさ」の話が混ざると、何を決めるべきか見失います。

このとき進行役が、

1. まだ発言していない人にも考えを尋ねる
2. 出された意見を「機能」「操作性」「保守性」に分ける
3. 共通点と対立点を確認する
4. 判断基準と次に決めることを参加者に確かめる

と働きかけると、参加者自身が比較・議論しやすくなります。**意見の中身を一方的に決めるのではなく、話合いの進め方を支援する**のがファシリテーションです。

## 定義・仕組み

ファシリテーション（facilitation）は、集団の活動や対話を円滑に進め、問題解決や合意形成を促す働きです。それを担う人を**ファシリテータ（ファシリテーター）**と呼びます。日本ファシリテーション協会は、会議の進行だけでなく、場づくり、意見の引き出し、整理、合意形成の支援を説明しています。

| 支援の観点 | ファシリテータの行動例 |
|---|---|
| 場づくり | 話合いの目的と進め方を確認し、発言しやすい場をつくる |
| 発言促進 | 発言の偏りに気づき、ほかの参加者にも意見を求める |
| 論点整理 | 出た意見をまとめ、何が一致・対立しているか示す |
| 合意形成支援 | 判断基準や未決事項を確認し、参加者の納得を助ける |

### 議長・専門家・書記・事務局との違い

| 役割 | 主な仕事 | 試験での着眼点 |
|---|---|---|
| **ファシリテータ** | 意見を引き出し、話合いの過程を支える | 中立・発言促進・論点整理 |
| 議長 | 会議を統括し、議事を進める | 議事運営や会議上の権限 |
| 専門家・助言者 | 専門知識に基づく情報や助言を提供する | 内容に対する専門的判断 |
| 書記 | 発言内容、決定事項などを記録する | 議事録・記録 |
| 事務局 | 日程調整、資料準備、開催連絡などを支える | 事務運営 |

これは**仕事の中心を見分けるための比較**です。議長とファシリテータを同じ人が兼ねたり、進行役が資料準備を手伝ったりすることもあります。「誰という肩書か」よりも、問題文に示された**行動の目的**を見て判断します。

## 科目Aでどう出る？

試験では、「どの役割が何をするか」を文章から読み取る形が基本です。

| 行動の手掛かり | まず考える役割 |
|---|---|
| 中立的に発言を促す、話題を整理する | **ファシリテータ** |
| 議事の手続きを進める、会議を統括する | 議長 |
| 法律・技術面で専門的に助言する | 専門家 |
| 会議の日程・資料を準備する | 事務局 |
| 議事録や決定事項を記録する | 書記 |

「進行役」と書かれていても、**特定の結論に誘導する**のであれば、ファシリテータの中立的な支援としては適切ではありません。

### 触って覚える：会議でどう声をかける？

次の3場面について「自分が会議のファシリテータなら、何をするか」を考えてから行動を選んでください。選択後に理由を表示します。

**見るポイント：**「自分が答えを出す」のか「参加者が話し合えるようにする」のかを区別します。

<div class="fe-facilitator-demo" id="fe-facilitator-demo">
  <div class="fe-facilitator-demo__interactive" hidden>
    <p class="fe-facilitator-demo__label">① 会議の状況を選ぶ</p>
    <div class="fe-facilitator-demo__scenes" role="group" aria-label="会議の状況">
      <button type="button" data-scene="0" aria-pressed="true">発言が偏る</button>
      <button type="button" data-scene="1" aria-pressed="false">議論が脱線</button>
      <button type="button" data-scene="2" aria-pressed="false">意見が対立</button>
    </div>
    <p class="fe-facilitator-demo__scenario" data-scenario></p>
    <p class="fe-facilitator-demo__label">② 適切と思う行動を選ぶ</p>
    <div class="fe-facilitator-demo__choices" role="group" aria-label="ファシリテータの対応"></div>
    <div class="fe-facilitator-demo__feedback" data-feedback role="status" aria-live="polite" aria-atomic="true" hidden></div>
  </div>
  <div class="fe-facilitator-demo__fallback">
    <p>会議での支援の例は次のとおりです。JavaScriptが有効な場合、ここに場面を切り替えて判断できる教材が表示されます。</p>
    <table>
      <thead><tr><th>会議の状況</th><th>進行支援の例</th></tr></thead>
      <tbody>
        <tr><td>発言が一人に偏る</td><td>ほかの参加者にも意見を求める</td></tr>
        <tr><td>話題が本筋からそれる</td><td>目的と論点を確認し、話を整理する</td></tr>
        <tr><td>意見が対立する</td><td>双方の理由を確認し、判断基準を共有する</td></tr>
      </tbody>
    </table>
  </div>
</div>

<style>
.fe-facilitator-demo{max-width:760px;margin:1.25rem auto;padding:1rem;border:1px solid #91a6b4;border-radius:12px}
.fe-facilitator-demo__interactive[hidden],.fe-facilitator-demo__feedback[hidden],.fe-facilitator-demo__fallback[hidden]{display:none}
.fe-facilitator-demo__label{font-weight:700;margin:.35rem 0}
.fe-facilitator-demo__scenes,.fe-facilitator-demo__choices{display:grid;gap:.5rem}
.fe-facilitator-demo__scenes{grid-template-columns:repeat(3,minmax(0,1fr))}
.fe-facilitator-demo button{width:100%;min-height:44px;padding:.55rem .65rem;border:1px solid #617b8c;border-radius:8px;background:#fff;color:#183344;font:inherit;text-align:left;cursor:pointer}
.fe-facilitator-demo button[aria-pressed="true"]{background:#185477;color:#fff;border-color:#185477;font-weight:700}
.fe-facilitator-demo button:focus-visible{outline:3px solid #db9029;outline-offset:3px}
.fe-facilitator-demo__scenario{padding:.85rem;background:#eef4f8;border-radius:8px;color:#233744}
.fe-facilitator-demo__feedback{margin-top:.8rem;padding:.8rem;border:1px solid #7c9ead;border-radius:8px;background:#f1f7fa;color:#173544}
.fe-facilitator-demo__feedback strong{display:block;margin-bottom:.35rem}
@media(max-width:520px){.fe-facilitator-demo__scenes{grid-template-columns:1fr}.fe-facilitator-demo{padding:.75rem}}
@media(prefers-color-scheme:dark){.fe-facilitator-demo button{background:#263945;color:#f1f5f7}.fe-facilitator-demo button[aria-pressed="true"]{background:#36799f;color:#fff}.fe-facilitator-demo__scenario,.fe-facilitator-demo__feedback{background:#263c48;color:#f0f5f7}}
</style>

<script>
(function(){
  function init(){
    var root=document.getElementById('fe-facilitator-demo');
    if(!root||root.dataset.initialized==='true')return;
    var interactive=root.querySelector('.fe-facilitator-demo__interactive');
    var fallback=root.querySelector('.fe-facilitator-demo__fallback');
    var options=root.querySelector('.fe-facilitator-demo__choices');
    var feedback=root.querySelector('[data-feedback]');
    var scenario=root.querySelector('[data-scenario]');
    if(!interactive||!fallback||!options||!feedback||!scenario)return;
    var scenes=[
      {scene:'ある参加者だけが長く話し、ほかの人の意見が出ていません。',
       choices:[
         ['その人の意見を結論として採用する',false,'進行役が独断で結論を決めると、ほかの参加者の考えが反映されません。'],
         ['まだ話していない人にも考えを尋ねる',true,'発言の偏りを調整し、参加者が考えを出せるようにしています。'],
         ['専門的な正解を説明して議論を打ち切る',false,'専門知識の提示だけでは、参加者の議論を支えることになりません。']
       ]},
      {scene:'仕様の話合いなのに、関係の薄い話題へそれています。',
       choices:[
         ['会議の目的と論点を確認し、話を整理する',true,'目的を再確認して、参加者が何について話すかを共有できます。'],
         ['自分が希望する仕様をその場で採用する',false,'仕様の採否を進行役の好みだけで決めてはいけません。'],
         ['脱線を放置して時間切れまで待つ',false,'進行の整理や働きかけを行っていません。']
       ]},
      {scene:'現場担当と開発担当の意見が対立し、決定に進めません。',
       choices:[
         ['立場の強い人の意見へ誘導する',false,'特定の立場への誘導は、中立的な議論の支援とは異なります。'],
         ['対立する理由と判断基準を参加者に確認する',true,'論点を整理し、双方が納得できる判断へ進むのを支援しています。'],
         ['進行役だけで優先順位を決定する',false,'決定権を持たない進行役が結論を決めることと、合意形成の支援は別です。']
       ]}
    ];
    var current=0;
    function render(){
      var data=scenes[current];
      scenario.textContent=data.scene;
      options.textContent='';
      feedback.hidden=true;
      feedback.textContent='';
      Array.prototype.forEach.call(root.querySelectorAll('[data-scene]'),function(button){
        button.setAttribute('aria-pressed',String(Number(button.dataset.scene)===current));
      });
      data.choices.forEach(function(choice,i){
        var button=document.createElement('button');
        button.type='button';
        button.textContent=String(i+1)+'．'+choice[0];
        button.setAttribute('aria-pressed','false');
        button.addEventListener('click',function(){
          Array.prototype.forEach.call(options.querySelectorAll('button'),function(other){other.setAttribute('aria-pressed',String(other===button));});
          feedback.textContent='';
          var heading=document.createElement('strong');
          heading.textContent=choice[1]?'適切な行動です':'もう一度考えてみましょう';
          var detail=document.createElement('span');
          detail.textContent=choice[2];
          feedback.appendChild(heading);
          feedback.appendChild(detail);
          feedback.hidden=false;
        });
        options.appendChild(button);
      });
    }
    Array.prototype.forEach.call(root.querySelectorAll('[data-scene]'),function(button){
      button.addEventListener('click',function(){current=Number(button.dataset.scene);render();});
    });
    render();
    interactive.hidden=false;
    fallback.hidden=true;
    root.dataset.initialized='true';
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);
  else init();
}());
</script>

この教材は、複雑な会議を単純化した学習用の例です。実際には、ファシリテータが議長や専門家の役割を兼ねることもあり、会議の目的や決定権限に応じて進行方法を調整します。

### 確認問題

複数部門が参加する仕様検討会議で、意見が対立している。ファシリテータの行動として、最も適切なものはどれか。

- ア．最も経験の長い参加者の案を結論として採用する。
- イ．会議前に作成した議事録を全員へ配布することだけに徹する。
- ウ．互いの主張と判断基準を整理し、参加者の議論を促す。
- エ．経営層が望む案へ議論が向かうように誘導する。

<details markdown="1">
<summary>正解と解説を見る（タップして開く）</summary>

**正解：ウ**

- **ウ**：意見の整理と発言促進により、参加者の合意形成を支援します。
- **ア**：経験年数だけで結論を決めるのは進行支援とは異なります。
- **イ**：記録や資料の配布は書記・事務局に近い役割です。
- **エ**：特定の結論への誘導は中立的な支援ではありません。

</details>

## どんな場面で使う？

ファシリテーションは、システム開発の要件定義、設計レビュー、業務改善ワークショップなどで使われます。異なる立場の関係者から意見を集め、論点を整理し、次の判断へ進める際に役立ちます。

関係者の要求や影響力を事前に整理する活動は、[ステークホルダ分析](/fe/stakeholder-analysis/)です。**誰の意見を確認すべきかを把握すること**と、**会議でその意見を引き出すこと**は役割が異なります。

## よくある誤解・混同

### ファシリテータは必ず会議の最終決定者である

そうとは限りません。会議の決定権限は別途定められます。ファシリテータは、決定に向けて話合いの過程を支えます。

### ファシリテータは議長と必ず別の人である

役割は異なりますが、同一人物が兼ねる場合もあります。問題では肩書より行動に着目します。

### 中立とは、発言をせず何もしないことである

中立的でも、質問し、発言機会を調整し、議論を整理するなど積極的に働きかけます。中立とは、特定の意見を不当に優遇しないことです。

### 会議で専門知識を使う人はファシリテータではない

専門知識を持つこと自体は問題ではありません。**専門的な結論を主張する役割**と**議論の進行を支援する役割**を区別します。

## まとめ（試験直前用）

- ファシリテータは、参加者の話合いを円滑にする**進行支援役**。
- **発言を促す・論点を整理する・合意形成を支援する**のが主な仕事。
- 特定の結論への誘導や、進行役の独断での決定は基本的な役割ではない。
- 議長・専門家・書記・事務局とは**行動の目的**で見分ける。
- 科目Aでは「**中立的に議論の流れを整える**」が重要な判断軸。

参考：[日本ファシリテーション協会：ファシリテーションとは](https://www.faj.or.jp/facilitation/) ／ [経済産業省：ファシリテーションの基礎（PDF）](https://www.meti.go.jp/policy/mono_info_service/mono/human-design/20200420004-4.pdf)

{% include fe_article_footer.html %}
