---
layout: page
title: トランザクションの状態遷移とは？コミットとアボートを図で理解【基本情報技術者試験】
description: トランザクションのアクティブ、コミット処理中、コミット済、アボート処理中、アボート済の状態遷移を図で整理し、FE試験で「あり得ない遷移」を切る判断基準を解説します。
permalink: /fe/transaction-state-transition/
tags: [fe, fe-technology, database]
fe_section: テクノロジ系
fe_subsection: データベース
fe_order: 31
date: 2026-09-22
last_modified_at: 2026-10-29
---

## まず結論

トランザクションの状態遷移では、**正常に確定する「コミット側」と、失敗して取り消す「アボート側」**を分けて考えると理解しやすくなります。

~~~text
                         成功
アクティブ → コミット処理中 → コミット済
    │              │
    │ 失敗         │ 失敗
    ↓              ↓
アボート処理中 ───────→ アボート済
~~~

基本情報技術者試験で特に重要なのは、次の判断です。

~~~text
コミット処理中 → アボート処理中  ：あり得る
アボート処理中 → コミット処理中  ：通常は考えない
~~~

**成功させようとして失敗し、取り消す側へ進むことはある。しかし、取り消し処理に入ったトランザクションが、そのままコミット側へ戻るわけではない**と考えると、選択肢を切りやすくなります。

## 直感的な説明

銀行振込で考えてみます。

~~~text
Aさんの残高を1万円減らす
Bさんの残高を1万円増やす
~~~

この一連の処理を1つのトランザクションとして扱います。すべて正常に終われば、結果を確定します。

~~~text
処理中 → 正常終了 → コミット → 確定
~~~

一方、途中で障害などが起きれば、そのまま中途半端な状態を残してはいけません。

~~~text
処理中 → 失敗 → アボート → 変更を取り消す
~~~

**commit は「確定する方向」、abort は「中止して取り消す方向」**とイメージすると分かりやすいです。

## 定義・仕組み

トランザクションとは、データベースに対する複数の処理を、ひとまとまりとして扱う単位です。

| 状態 | 意味 |
|---|---|
| アクティブ | トランザクションを実行している |
| コミット処理中 | 正常終了させ、結果を確定しようとしている |
| コミット済 | 結果の確定が完了した |
| アボート処理中 | トランザクションを中止し、取り消し処理をしている |
| アボート済 | 中止・取り消しが完了した |

**アボート（abort）**は、トランザクションを途中で中止することです。

~~~text
アボート     ＝ トランザクションを中止する
ロールバック ＝ 更新内容を取り消して以前の状態へ戻す
~~~

試験では厳密な内部実装よりも、**正常終了する方向か、失敗して取り消す方向か**を追うことが大切です。

この考え方は、[ACID特性](/fe/acid-properties/) の原子性ともつながります。「全部成功する、または全部取り消す」という原子性を、状態の変化として細かく見たものだと考えると理解しやすくなります。

## 科目Aでどう出る？

科目Aでは、複数の状態を示して「起こることのない状態遷移」を選ばせる形があります。

まず2本のルートに分けます。

~~~text
【成功ルート】
アクティブ → コミット処理中 → コミット済

【失敗ルート】
アクティブ → アボート処理中 → アボート済
~~~

さらに、コミット処理中に問題が起これば、正常終了できないのでアボート側へ移ることがあります。

~~~text
コミット処理中 → 失敗 → アボート処理中
~~~

しかし逆方向の「アボート処理中 → コミット処理中」は考えません。すでに「このトランザクションを中止する」と判断して取り消し処理へ進んでいるからです。

### 選択肢を切る判断基準

~~~text
1. 今は成功側か、失敗側か
2. 矢印は処理の進行方向か
3. 失敗側から成功側へ戻ろうとしていないか
~~~

特に3番が、このタイプの問題で強い判断材料になります。


### 実際に触ってみる：状態遷移を判定

次の「遷移前」と「遷移後」を選ぶと、その遷移が起こり得るかと理由を確認できます。今回の科目Aの選択肢4つをそのまま試せます。

<div id="fe-transaction-state-demo" class="fe-transaction-demo">
  <div class="fe-transaction-inputs">
    <label>遷移前
      <select id="fe-transaction-from">
        <option value="aborting">アボート処理中</option>
        <option value="committing">コミット処理中</option>
      </select>
    </label>
    <span aria-hidden="true">→</span>
    <label>遷移後
      <select id="fe-transaction-to">
        <option value="aborted">アボート済</option>
        <option value="committing">コミット処理中</option>
        <option value="aborting">アボート処理中</option>
        <option value="committed">コミット済</option>
      </select>
    </label>
  </div>
  <p id="fe-transaction-result" class="fe-transaction-result" role="status" aria-live="polite"></p>
  <p id="fe-transaction-reason" aria-live="polite"></p>
  <button type="button" id="fe-transaction-next">次の例を確認</button>
  <p class="fe-transaction-note">※同じトランザクション内での遷移を扱います。中止後に新しいトランザクションを開始する操作は含みません。</p>
</div>

<style>
.fe-transaction-demo{border:1px solid #94a3b8;border-radius:12px;padding:1rem;margin:1rem 0}
.fe-transaction-inputs{display:flex;align-items:end;flex-wrap:wrap;gap:.7rem}
.fe-transaction-inputs label{display:grid;gap:.35rem;font-weight:600}
.fe-transaction-inputs select{max-width:100%;padding:.55rem;border:1px solid #64748b;border-radius:6px;background:var(--background-color,#fff);color:var(--text-color,#172033)}
.fe-transaction-result{font-weight:700;font-size:1.08rem;margin-bottom:.3rem}
.fe-transaction-demo button{padding:.55rem .9rem;background:#e2e8f0;color:#172033;border:1px solid #64748b;border-radius:6px;cursor:pointer}
.fe-transaction-note{font-size:.85rem}
</style>
<script>
(function(){
  const root=document.getElementById('fe-transaction-state-demo');
  if(!root)return;
  const from=root.querySelector('#fe-transaction-from');
  const to=root.querySelector('#fe-transaction-to');
  const result=root.querySelector('#fe-transaction-result');
  const reason=root.querySelector('#fe-transaction-reason');
  const cases=[
    ['aborting','aborted','取り消しが完了してアボート済になります。'],
    ['aborting','committing','取り消し処理に入った同じトランザクションは、コミット処理へ戻りません。'],
    ['committing','aborting','コミットが確定する前に失敗した場合、アボート処理へ進むことがあります。'],
    ['committing','committed','コミットが正常に完了するとコミット済になります。']
  ];
  function render(){
    const row=cases.find(c=>c[0]===from.value&&c[1]===to.value);
    if(!row){
      result.textContent='この組み合わせは例題の4つの遷移には含まれません';
      reason.textContent='まずは上の説明にある成功・失敗ルートを確認してください。';
      return;
    }
    const ok=!(row[0]==='aborting'&&row[1]==='committing');
    result.textContent=ok?'○ 起こり得る遷移':'× 起こり得ない遷移（今回の正解）';
    reason.textContent=row[2];
  }
  function next(){
    const index=cases.findIndex(c=>c[0]===from.value&&c[1]===to.value);
    const c=cases[(index+1)%cases.length];
    from.value=c[0];to.value=c[1];render();
  }
  from.addEventListener('change',render);
  to.addEventListener('change',render);
  root.querySelector('#fe-transaction-next').addEventListener('click',next);
  render();
})();
</script>

## どんな場面で使う？

例えば注文処理を考えます。

~~~text
在庫を減らす
↓
注文履歴を登録
↓
支払情報を登録
~~~

すべて成功すれば「アクティブ → コミット処理中 → コミット済」と進みます。途中で問題が起きれば、中途半端な更新を残さないため「アボート処理中 → アボート済」の方向へ進みます。

この流れが分かると、ACID特性の**原子性**も「全部成功か、全部取り消す」という処理の流れとして理解しやすくなります。

## よくある誤解・混同

### 誤解1：アボートとロールバックは全く同じ言葉

密接に関係しますが、見るポイントが少し違います。

~~~text
アボート     → トランザクションを中止する
ロールバック → 変更を取り消して戻す
~~~

FE試験では、アボートが出てきたらまず**失敗・中止側の処理**と判断します。

### 誤解2：コミット処理中なら必ずコミット済になる

コミットを進めている途中でも、正常に完了できなければアボート側へ進むことがあります。

~~~text
コミット処理中
   ├─ 成功 → コミット済
   └─ 失敗 → アボート処理中
~~~

### 誤解3：コミットとアボートは自由に行き来できる

自由には行き来しません。成功側から失敗側へ進むことは障害によって起こり得ますが、**失敗側から成功側へそのまま戻る**とは考えません。

### 誤解4：状態名を全部暗記しないと解けない

暗記よりも方向を見る方が有効です。

~~~text
成功 → コミット
失敗 → アボート
~~~

まずこの2方向に分けてから矢印を追えば、初見の状態名が含まれていても判断しやすくなります。

## まとめ（試験直前用）

- **コミット**は正常終了して結果を確定する方向
- **アボート**はトランザクションを中止して取り消す方向
- コミット処理中に失敗して、アボート処理中へ進むことはある
- **アボート処理中からコミット処理中へ戻る遷移は考えない**
- 状態遷移問題では「成功側か失敗側か」を先に見る
- ACID特性の**原子性（全部成功か、全部取り消す）**とつなげると理解しやすい

{% include fe_article_footer.html %}
