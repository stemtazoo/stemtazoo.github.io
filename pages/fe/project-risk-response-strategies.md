---
layout: page
title: プロジェクトのリスク対応戦略とは？脅威と好機の違い【基本情報技術者試験】
description: "プロジェクトのリスクには脅威と好機がある。回避・転嫁・軽減・受容と、活用・共有・強化・受容を比較し、FE科目Aで行動から戦略を見分ける方法を解説。"
permalink: /fe/project-risk-response-strategies/
tags: [fe, fe-management, project-management, risk-management]
fe_section: マネジメント系
fe_subsection: プロジェクトマネジメント
fe_order: 380
date: 2026-11-04
last_modified_at: 2026-11-04
related_articles:
  - /fe/risk-assessment-process/
  - /fe/risk-level/
---

## まず結論

**プロジェクトのリスクは、損失につながる「脅威」だけでなく、利益につながる「好機」も含みます。** リスク対応戦略は、脅威を避けたり小さくしたりする場合と、好機を確実にしたり大きくしたりする場合で異なります。

| 脅威（マイナス）への対応 | 好機（プラス）への対応 | 見分ける軸 |
|---|---|---|
| 回避（Avoid） | 活用（Exploit） | 不確実性を取り除く方向 |
| 転嫁（Transfer） | 共有（Share） | 第三者との関係 |
| 軽減（Mitigate） | 強化（Enhance） | 発生可能性や影響を変える |
| 受容（Accept） | 受容（Accept） | 積極的な変更を行わず引き受ける |

**科目Aでは「何が起きそうか（脅威か好機か）」→「対策は何を変えるか」の順に判断**しましょう。単語の暗記だけでなく、行動の目的を読むことが重要です。

## 直感的な説明

新しい設備監視システムを開発するプロジェクトを考えます。

- **脅威**：重要部品の納入が遅れて、開発が遅れるかもしれない。
- **好機**：新しい開発ツールが使えるようになり、開発期間を短縮できるかもしれない。

どちらも、まだ起きると確定していない事象です。前者には悪い結果を抑える対応、後者にはよい結果を実現・拡大する対応を検討します。

ここでいうリスクは、日常会話の「危険」という意味だけではありません。PMIは、プロジェクト目標に**正または負**の影響を及ぼす不確実な事象・状況をリスクとして説明しています。

## 定義・仕組み

### 脅威への4つの代表的な対応

| 戦略 | 何をするか | 設備監視システム開発の例 |
|---|---|---|
| **回避** | 脅威を取り除く、または影響を受けないようにする | 納期が不安定な部品の採用をやめる |
| **転嫁** | 契約や保険などで損失負担・対応責任の一部を第三者へ移す | 契約で納期遅延時の補償を定める |
| **軽減** | 発生可能性や悪影響を小さくする | 代替部品や予備日を確保する |
| **受容** | リスクを認識し、積極的な対応を取らずに引き受ける | 影響が小さい遅延を、判断のうえ許容する |

転嫁しても脅威そのものが消えるとは限らず、委託元の管理責任がすべてなくなるわけでもありません。

### 好機への4つの代表的な対応

| 戦略 | 何をするか | 設備監視システム開発の例 |
|---|---|---|
| **活用** | 好機が実現するように不確実性を取り除く | 新ツールを使える体制・利用条件を確保し、採用を確実にする |
| **共有** | 好機を活かす能力の高い第三者と協力し、便益を分け合う | 専門企業と共同開発し、短縮による成果を共有する |
| **強化** | 好機が起こる可能性やプラスの影響を増やす | 技術者の研修で新ツールの効果を高める |
| **受容** | 好機を積極的には追求せず、実現すれば利益を受け取る | 特別な投資はせず、利用可能になれば新ツールを取り入れる |

**活用と強化の違い**は、好機の実現を確実にしようとするのか、発生可能性や効果を高めようとするのかです。実務の施策は複数の戦略にまたがることもあるため、試験では設問が示す主目的に注目します。

### 触って覚える：脅威と好機を切り替えて比べる

同じ「設備監視システムの開発」を前提に、リスクの種類を切り替えて、対応が何を変えるか確認しましょう。

**見るポイント：** 脅威ではマイナスを避ける・減らす、好機ではプラスを実現・増やす、という方向の違いです。受容は両方にあります。

<div id="fe-risk-strategy-demo" class="fe-risk-strategy-demo" aria-label="プロジェクトのリスク対応戦略の比較">
  <div class="fe-risk-strategy-demo__controls" hidden>
    <span class="fe-risk-strategy-demo__prompt">① リスクの種類を選ぶ</span>
    <div class="fe-risk-strategy-demo__buttons" role="group" aria-label="リスクの種類">
      <button type="button" data-kind="threat" aria-pressed="true">脅威（マイナス）</button>
      <button type="button" data-kind="opportunity" aria-pressed="false">好機（プラス）</button>
    </div>
    <p class="fe-risk-strategy-demo__prompt">② 戦略を選んで、行動と目的を比べる</p>
    <div class="fe-risk-strategy-demo__buttons" role="group" aria-label="対応戦略">
      <button type="button" data-index="0" aria-pressed="true">回避</button>
      <button type="button" data-index="1" aria-pressed="false">転嫁</button>
      <button type="button" data-index="2" aria-pressed="false">軽減</button>
      <button type="button" data-index="3" aria-pressed="false">受容</button>
    </div>
    <div class="fe-risk-strategy-demo__result" role="status" aria-live="polite" aria-atomic="true">
      <p><strong>想定する事象：</strong><span data-event>重要部品の納入が遅れるかもしれない</span></p>
      <p><strong>選んだ戦略：</strong><span data-title>回避</span></p>
      <p><strong>行動例：</strong><span data-action>納期が不安定な部品の採用をやめる</span></p>
      <p><strong>判断ポイント：</strong><span data-reason>遅延の原因になる選択をやめ、脅威を避ける</span></p>
    </div>
  </div>
  <div class="fe-risk-strategy-demo__fallback">
    <p>以下は操作なしでも確認できる比較表です。JavaScriptが使える場合は、上の切替ボタンで同じ例を一つずつ確認できます。</p>
    <table>
      <thead><tr><th>脅威への対応</th><th>好機への対応</th><th>主な判断</th></tr></thead>
      <tbody>
        <tr><td>回避</td><td>活用</td><td>脅威を避ける／好機を確実にする</td></tr>
        <tr><td>転嫁</td><td>共有</td><td>負担を移す／便益を協力して得る</td></tr>
        <tr><td>軽減</td><td>強化</td><td>マイナスを小さく／プラスを大きく</td></tr>
        <tr><td>受容</td><td>受容</td><td>判断して引き受ける</td></tr>
      </tbody>
    </table>
  </div>
</div>

<style>
.fe-risk-strategy-demo{max-width:760px;margin:1rem auto 1.5rem;padding:1rem;border:1px solid #9aaeba;border-radius:12px}
.fe-risk-strategy-demo__controls{display:grid;gap:.65rem}
.fe-risk-strategy-demo__controls[hidden]{display:none}
.fe-risk-strategy-demo__prompt{font-weight:650;margin:.2rem 0}
.fe-risk-strategy-demo__buttons{display:flex;flex-wrap:wrap;gap:.5rem}
.fe-risk-strategy-demo button{font:inherit;min-height:44px;padding:.5rem .8rem;border:1px solid #657b8b;border-radius:8px;background:#fff;color:#233746;cursor:pointer}
.fe-risk-strategy-demo button[aria-pressed="true"]{background:#174b70;color:#fff;border-color:#174b70;font-weight:700}
.fe-risk-strategy-demo button:focus-visible{outline:3px solid #dc943c;outline-offset:3px}
.fe-risk-strategy-demo__result{padding:.7rem 1rem;border:1px solid #8da7b5;border-radius:8px;background:#eef4f8;color:#233746}
.fe-risk-strategy-demo__result p{margin:.45rem 0}
.fe-risk-strategy-demo__fallback p{margin-top:0}
@media(prefers-color-scheme:dark){.fe-risk-strategy-demo{border-color:#8397a5}.fe-risk-strategy-demo button{background:#24343e;color:#f1f4f5}.fe-risk-strategy-demo button[aria-pressed="true"]{background:#377eaa;color:#fff}.fe-risk-strategy-demo__result{background:#263844;color:#f1f4f5}}
</style>

<script>
(function () {
  function init() {
    const root = document.getElementById('fe-risk-strategy-demo');
    if (!root || root.dataset.ready === 'true') return;
    const controls = root.querySelector('.fe-risk-strategy-demo__controls');
    const fallback = root.querySelector('.fe-risk-strategy-demo__fallback');
    if (!controls || !fallback) return;
    const data = {
      threat: {
        event: '重要部品の納入が遅れるかもしれない',
        names: ['回避', '転嫁', '軽減', '受容'],
        actions: [
          '納期が不安定な部品の採用をやめる',
          '契約で納期遅延時の補償を定める',
          '代替部品や予備日を確保する',
          '小さな遅延の可能性を評価したうえで受け入れる'
        ],
        reasons: [
          '遅延の原因になる選択をやめ、脅威を避ける',
          '遅延の発生自体でなく、損失負担の一部を移す',
          '遅延の発生可能性や影響を小さくする',
          '追加対策をせず引き受ける。放置ではなく判断が必要'
        ]
      },
      opportunity: {
        event: '新しい開発ツールで開発期間を短縮できるかもしれない',
        names: ['活用', '共有', '強化', '受容'],
        actions: [
          '利用条件と体制を確保し、新ツールの採用を確実にする',
          '専門企業と共同開発して短縮の成果を分け合う',
          '研修を行い、新ツールによる短縮効果を高める',
          '追加投資はせず、利用可能になれば利点を得る'
        ],
        reasons: [
          '好機が実現するよう不確実性を取り除く',
          '第三者と協力し、得られる便益を共有する',
          '好機の発生可能性やプラスの影響を増やす',
          '積極的な追求はしないが、実現すれば利益を得る'
        ]
      }
    };
    let kind = 'threat';
    let index = 0;
    const kindButtons = Array.from(root.querySelectorAll('[data-kind]'));
    const indexButtons = Array.from(root.querySelectorAll('[data-index]'));
    function render() {
      const current = data[kind];
      kindButtons.forEach(function (button) {
        button.setAttribute('aria-pressed', String(button.dataset.kind === kind));
      });
      indexButtons.forEach(function (button, i) {
        button.textContent = current.names[i];
        button.setAttribute('aria-pressed', String(i === index));
      });
      root.querySelector('[data-event]').textContent = current.event;
      root.querySelector('[data-title]').textContent = current.names[index];
      root.querySelector('[data-action]').textContent = current.actions[index];
      root.querySelector('[data-reason]').textContent = current.reasons[index];
    }
    kindButtons.forEach(function (button) {
      button.addEventListener('click', function () { kind = button.dataset.kind; render(); });
    });
    indexButtons.forEach(function (button, i) {
      button.addEventListener('click', function () { index = i; render(); });
    });
    render();
    controls.hidden = false;
    fallback.hidden = true;
    root.dataset.ready = 'true';
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
}());
</script>

この教材は代表例を単純化して比較するものです。現実のプロジェクトでは、費用・責任・契約条件・残留リスクも考慮し、複数の対応を組み合わせることがあります。

## 科目Aでどう出る？

選択肢で「受け入れる」「外部に任せる」といった言葉だけを拾うのではなく、**その行動が何を変えるか**に注目します。

| 問題文の手掛かり | 判断 |
|---|---|
| 危険な作業を中止し、脅威を取り除く | 脅威の**回避** |
| 保険・契約で損失負担を移す | 脅威の**転嫁** |
| 発生可能性・悪影響を下げる | 脅威の**軽減** |
| 好機が確実に実現するようにする | 好機の**活用** |
| パートナーと好機の成果を分け合う | 好機の**共有** |
| 好機の発生可能性・効果を高める | 好機の**強化** |
| 積極策を取らず、評価のうえ引き受ける | **受容**（両方） |

### 確認問題

あるプロジェクトで、新技術を使えば成果物の品質が向上する可能性がある。実現する確率を高めるために技術者の研修を実施する。この対応戦略として最も適切なものはどれか。

- ア．活用
- イ．共有
- ウ．強化
- エ．受容

<details markdown="1">
<summary>正解と解説を見る（タップして開く）</summary>

**正解：ウ（強化）**

研修によって**好機の実現可能性や効果を高める**ことを狙っているため、強化です。

- ア：活用は、好機が実現するように不確実性を取り除く戦略です。
- イ：共有は、第三者と協力して好機の便益を得る戦略です。
- ウ：強化は、発生可能性やプラスの影響を高めます。
- エ：受容は、好機を積極的に追求する措置を取らずに引き受けます。

</details>

## どんな場面で使う？

ソフトウェア開発、設備導入、業務改善などで、予定外の出来事による損失を防ぎながら、技術革新や共同開発による利益を活かしたいときに使います。

例えば、納期遅延の可能性は脅威、性能改善につながる新技術の登場は好機です。両方をリスクとして把握し、対応を選びます。

なお、**リスクアセスメント（特定・分析・評価）**と**リスク対応（対策の選択・実行）**は別の活動です。流れの違いは[リスクアセスメントの記事](/fe/risk-assessment-process/)で確認できます。リスクの大きさを判断する概念は[リスクレベルの記事](/fe/risk-level/)を参照してください。

## よくある誤解・混同

### リスクは必ず悪い出来事である

プロジェクトマネジメントでは、好機もリスクに含まれます。**プラス・マイナス両方の不確実性**を考えます。一方、情報セキュリティ管理では脅威側の文脈でリスクを扱う場合が多いため、分野を確認しましょう。

### 活用と強化は同じ

**活用は好機の実現を確実にすること、強化は実現可能性や効果を高めること**です。「確実にする」と「高める」の違いに注目します。

### 転嫁と共有はどちらも外部委託である

転嫁では脅威による損失負担や対応責任の移動、共有では好機から得られる便益の共同獲得に注目します。「第三者と関わる」というだけで判断せず、**マイナスの負担かプラスの便益か**を読み取ります。

### 受容は、何も考えず放置すること

受容は、リスクを認識したうえで引き受ける戦略です。積極的な対応を行わなくても、必要に応じて監視・見直しや予備の準備を考えます。

### 四つの分類だけが、あらゆるPMBOK版の全戦略である

この表は、FEの学習で比較しやすい**代表的な戦略**を整理したものです。PMIの資料やPMBOKの版・対象によっては、ほかの対応や表現もあります。試験問題の指定や参照している版があれば、その前提を優先します。

## まとめ（試験直前用）

- **リスクには脅威（マイナス）と好機（プラス）がある。**
- 脅威：**回避・転嫁・軽減・受容**。
- 好機：**活用・共有・強化・受容**。
- **活用＝実現を確実にする、強化＝確率や効果を高める。**
- **受容は両方にある。** 「何が起きるか」「対策が何を変えるか」で判断する。

### 参考資料

- [PMI：Lexicon of Project Management Terms（2026年版、riskと各対応戦略の定義）](https://www.pmi.org/-/media/pmi/documents/registered/pdf/pmbok-standards/pmi-lexicon-pm-terms.pdf)
- [PMI：Collaborative tools and techniques to build the project risk plan（脅威と好機への対応戦略の対比）](https://www.pmi.org/learning/library/tools-techniques-build-project-risk-plan-7223)
- [PMI：Top Ten Mistakes made in Managing Project Risks（好機への対応戦略）](https://www.pmi.org/learning/library/mistakes-made-managing-project-risks-6239)

{% include fe_article_footer.html %}
