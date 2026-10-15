---
layout: page
title: バイオメトリクス認証とは？身体的特徴と行動的特徴の違い【基本情報技術者試験】
description: バイオメトリクス認証（生体認証）を、身体的特徴と行動的特徴の違いから整理します。指紋・虹彩・静脈と、署名の速度・筆圧・キーストロークをFE試験で切り分ける判断基準を解説します。
permalink: /fe/biometric-authentication/
tags: [fe, fe-technology, security, authentication]
fe_section: 情報セキュリティ
fe_subsection: 認証
fe_order: 32
date: 2026-10-03
last_modified_at: 2026-10-15
---

## まず結論

バイオメトリクス認証（生体認証）は、**人の身体や行動に現れる特徴を使って本人を認証する方式**です。

FE試験では、まず次の2つに分けます。

```text
体の形・模様
→ 身体的特徴

動かし方・クセ
→ 行動的特徴
```

特に重要なのは、**署名の速度や筆圧は行動的特徴**という点です。

「署名」という言葉だけではなく、**何を特徴として取り出しているか**を見て判断します。

<div class="bio-split">
  <div class="bio-card">
    <strong>身体的特徴</strong>
    <span>体の形・模様</span>
    <small>指紋・虹彩・静脈など</small>
  </div>
  <div class="bio-card">
    <strong>行動的特徴</strong>
    <span>動作・クセ</span>
    <small>署名・キーストロークなど</small>
  </div>
</div>

## 直感的な説明

「本人らしさを、どこから取り出しているか」で考えます。

たとえば指紋認証は、指紋の模様という**体にある特徴**を見ています。

一方、署名認証で「書く速度」「筆圧」などを見る場合は、完成した文字だけではなく、**その人がどう書くか**を見ています。

```text
指紋の模様を見る
→ 体そのもの
→ 身体的特徴

署名するときの速度・筆圧を見る
→ 動かし方
→ 行動的特徴
```

試験では、この「体そのものか、動作か」という切り分けが有効です。

## 定義・仕組み

バイオメトリクス認証では、個人に固有の身体的・行動的な特徴を取り出し、あらかじめ登録した情報と照合して本人かどうかを確認します。

代表例を整理すると次のようになります。

| 特徴 | 分類 | 見ているもの |
|---|---|---|
| 指紋 | 身体的特徴 | 指紋の隆線や特徴点 |
| 虹彩 | 身体的特徴 | 虹彩の模様 |
| 静脈 | 身体的特徴 | 血管の形や分岐 |
| 顔 | 身体的特徴 | 顔の形状や特徴 |
| 署名 | 行動的特徴 | 書く速度・筆圧など |
| キーストローク | 行動的特徴 | キー入力の間隔や速度など |

### マニューシャとは？

指紋認証では、**マニューシャ（minutiae）**という言葉が出ることがあります。

これは、指紋の隆線にある端点や分岐点などの**特徴点**です。

```text
指紋の隆線
   ↓
端点・分岐点など
   ↓
マニューシャ
```

マニューシャという用語を忘れていても、「指紋の隆線」「紋様」などと書かれていれば、**身体的特徴**だと判断できます。

## 科目Aでどう出る？

科目Aでは、具体例を見て「身体的特徴か、行動的特徴か」を選ばせる問題に注意します。

判断するときは、方式名よりも**特徴として何を測っているか**を確認します。

| 問題文の手掛かり | 判断 |
|---|---|
| 血管の分岐や形 | 身体的特徴 |
| 虹彩の模様 | 身体的特徴 |
| 指紋の隆線・マニューシャ | 身体的特徴 |
| 署名するときの速度・筆圧 | **行動的特徴** |
| キーを押す間隔・速度 | **行動的特徴** |

覚え方はシンプルです。

> **形・模様 → 身体、速度・時間・圧力 → 行動**

もちろん実際の方式にはさまざまな特徴量がありますが、FEの選択肢を切るときの最初の判断軸として使えます。

## 本人拒否率（FRR）と他人受入率（FAR）

生体認証では、登録した特徴と入力された特徴が完全に一致するとは限りません。そこで、どの程度似ていれば本人と判定するかという**しきい値**を設定します。

このとき重要なのが、次の2種類の誤りです。

| 指標 | 意味 | 試験でのイメージ |
|---|---|---|
| FRR（本人拒否率） | 本人なのに拒否する割合 | 厳しすぎて本人までNG |
| FAR（他人受入率） | 他人なのに本人として受け入れる割合 | 緩すぎて他人までOK |

<div class="bio-threshold">
  <div><strong>判定を厳しくする</strong><br><span>FRR ↑</span><br><small>本人も拒否されやすい</small><br><span>FAR ↓</span><br><small>他人は通りにくい</small></div>
  <div class="bio-arrow">⇄</div>
  <div><strong>判定を緩くする</strong><br><span>FRR ↓</span><br><small>本人は通りやすい</small><br><span>FAR ↑</span><br><small>他人も通りやすい</small></div>
</div>

### しきい値を動かして確かめる

次のスライダーで「どのくらい似ていれば本人と認めるか」を変えてみましょう。

<div class="bio-sim" id="bio-sim">
  <label for="bio-match-threshold"><strong>本人と判定する一致度の基準</strong>：<output id="bio-match-value">60</output>％</label>
  <input id="bio-match-threshold" type="range" min="20" max="90" step="5" value="60" aria-describedby="bio-sim-explanation">
  <div class="bio-sim-scale"><span>緩い ← 許可しやすい</span><span>厳しい → 拒否しやすい</span></div>
  <div class="bio-sim-cards">
    <div class="bio-sim-card"><strong>FRR（本人拒否率）</strong><span id="bio-frr-value" aria-live="polite">—</span><small>本人なのに拒否する割合</small></div>
    <div class="bio-sim-card"><strong>FAR（他人受入率）</strong><span id="bio-far-value" aria-live="polite">—</span><small>他人なのに通してしまう割合</small></div>
  </div>
  <p id="bio-sim-explanation" class="bio-sim-explanation" aria-live="polite">基準を動かすと、本人拒否率と他人受入率の変化を確認できます。</p>
  <p class="bio-sim-note">※ 学習用の架空データです。登録者と他人の一致度の分布を仮定した概念モデルであり、実際の認証装置の性能や推奨しきい値を示すものではありません。</p>
</div>

つまり、**FRRだけを下げればよい、FARだけを下げればよい、という関係ではありません**。認証システムを導入するときは、用途に応じて両方を考慮しながらしきい値を調整します。

試験では次のように切り分けます。

```text
本人なのに拒否
→ FRR（本人拒否率）

他人なのに通過
→ FAR（他人受入率）

FRRとFARを両方考慮して調整
→ 適切
```

「生体認証システムを導入するときに考慮すべきこと」と聞かれたら、**FRRとFARのトレードオフ**は強い候補です。

## どんな場面で使う？

バイオメトリクス認証は、本人確認が必要な場面で利用されます。

たとえば、スマートフォンのロック解除、入退室管理、端末やシステムへのログインなどです。

パスワードのように「知っている情報」を入力する方式とは異なり、本人の身体や行動の特徴を利用します。

ただし、生体情報だから必ず安全という意味ではありません。認証方式は用途やリスクに応じて組み合わせて考える必要があります。

## よくある誤解・混同

### 「署名」だから身体的特徴？

ここが今回の重要なひっかけです。

```text
署名という完成物だけを見る
        ↓
これだけでは判断しない

速度・筆圧を測る
        ↓
書き方のクセを見る
        ↓
行動的特徴
```

**名詞ではなく、測っている特徴を見る**のがポイントです。

### 指紋と署名を同じ「形」と考えない

指紋は、本人の体に存在する隆線や特徴点を利用します。

一方、署名の速度や筆圧は、本人が行動したときに現れる特徴です。

```text
指紋
→ 体にある特徴

署名の速度・筆圧
→ 動いたときに現れる特徴
```

### マニューシャという難しい用語に引っ張られない

知らない用語が出ても、問題文の周囲を見ます。

「指紋」「隆線」「紋様」といった語があれば、少なくとも**行動的特徴ではない**と切ることができます。

## まとめ（試験直前用）

- バイオメトリクス認証＝身体や行動の特徴を使う本人認証
- **体の形・模様 → 身体的特徴**
- **動かし方・クセ → 行動的特徴**
- 指紋・虹彩・静脈は身体的特徴
- 署名の速度・筆圧、キーストロークは行動的特徴
- マニューシャは指紋の特徴点
- 方式名ではなく、**何を測っているか**を見る
- FRR＝本人を拒否、FAR＝他人を受入れ。**両方を考慮してしきい値を調整する**

{% include fe_article_footer.html %}

<style>
.bio-split {
  display:grid;
  grid-template-columns:repeat(2,minmax(0,1fr));
  gap:1rem;
  max-width:680px;
  margin:1.5rem auto;
}
.bio-card {
  padding:1rem;
  border:1px solid #bbb;
  border-radius:10px;
  text-align:center;
  background:#fafafa;
}
.bio-card strong,
.bio-card span,
.bio-card small {
  display:block;
}
.bio-card span {
  margin:.55rem 0;
  font-size:1.05rem;
}
.bio-card small {
  line-height:1.6;
}
@media (max-width:520px) {
  .bio-split {
    grid-template-columns:1fr;
  }
}
.bio-threshold {
  display:flex;
  align-items:center;
  justify-content:center;
  gap:1rem;
  margin:1.5rem auto;
  max-width:680px;
}
.bio-threshold > div:not(.bio-arrow) {
  flex:1;
  padding:1rem;
  border:1px solid #bbb;
  border-radius:10px;
  text-align:center;
  background:#fafafa;
}
.bio-threshold span {font-weight:bold;}
.bio-arrow {font-size:1.5rem;font-weight:bold;}
@media (max-width:520px) {
  .bio-threshold {flex-direction:column;}
  .bio-arrow {transform:rotate(90deg);}
}
.bio-sim {border:1px solid #aab8c3;border-radius:12px;padding:1rem;margin:1.5rem auto;max-width:680px;background:rgba(120,145,160,.07)}
.bio-sim label {display:block;margin-bottom:.65rem}
.bio-sim input[type=range] {display:block;width:100%;accent-color:#668fa2}
.bio-sim-scale {display:flex;justify-content:space-between;gap:.5rem;font-size:.82rem;margin:.3rem 0 1rem}
.bio-sim-cards {display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.7rem}
.bio-sim-card {display:flex;flex-direction:column;align-items:center;gap:.4rem;border:1px solid #aab8c3;border-radius:9px;padding:.8rem;text-align:center}
.bio-sim-card span {font-size:1.4rem;font-weight:700;font-variant-numeric:tabular-nums}
.bio-sim-card small {line-height:1.5}
.bio-sim-explanation {font-weight:600;margin:.9rem 0}
.bio-sim-note {font-size:.82rem;opacity:.8;margin-bottom:0}
@media(max-width:420px){.bio-sim-cards{grid-template-columns:1fr}.bio-sim-scale{font-size:.72rem}}
</style>
<script>
(function(){
  function initBiometricSimulator(){
    var root=document.getElementById('bio-sim');
    if(!root || root.dataset.initialized) return;
    root.dataset.initialized='1';
    var input=document.getElementById('bio-match-threshold');
    var val=document.getElementById('bio-match-value');
    var frr=document.getElementById('bio-frr-value');
    var far=document.getElementById('bio-far-value');
    var message=document.getElementById('bio-sim-explanation');
    if(!input||!val||!frr||!far||!message)return;
    function normalCdf(x,mean,sd){
      // Logistic approximation used only for an intuitive educational model.
      return 1/(1+Math.exp(-1.7*(x-mean)/sd));
    }
    function update(){
      var threshold=Number(input.value);
      var rejection=normalCdf(threshold,72,13)*100;
      var acceptance=(1-normalCdf(threshold,38,13))*100;
      val.textContent=String(threshold);
      frr.textContent=rejection.toFixed(1)+'%';
      far.textContent=acceptance.toFixed(1)+'%';
      message.textContent=threshold>=70
        ?'厳しい判定：他人は通りにくい一方、本人も拒否されやすくなります。'
        :threshold<=40
        ?'緩い判定：本人は通りやすい一方、他人も通りやすくなります。'
        :'中間の判定：本人の使いやすさと、他人を通さない安全性の両方を考えます。';
    }
    input.addEventListener('input',update);
    update();
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',initBiometricSimulator);
  else initBiometricSimulator();
})();
</script>
