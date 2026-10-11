---
layout: page
title: エンタープライズアーキテクチャとは？4つの体系を整理【基本情報技術者試験】
description: EAの4体系を、業務・データ・システム機能・技術基盤の視点で比較します。同じ販売業務の図解と代表的な成果物の対応表で、アプリケーションとテクノロジの違い、ソフトウェア構成図やDFDの分類、As-Is・To-Beから移行計画につなげる考え方を整理します。
permalink: /fe/enterprise-architecture/
tags: [fe, fe-strategy, system-strategy, enterprise-architecture]
fe_section: ストラテジ系
fe_subsection: システム戦略
fe_order: 95
date: 2026-08-14
last_modified_at: 2026-10-11
---

<link rel="stylesheet" href="{{ '/assets/css/fe-ea-diagram.css' | relative_url }}">

## まず結論

**エンタープライズアーキテクチャ（EA）**は、企業や組織全体の業務と情報システムを、**全体最適の視点で整理・設計し、改善する手法**です。

FE試験では、4体系を**「業務・データ・システム機能・技術基盤」**で切り分けます。

| 体系 | 見る対象 | 判断の手掛かり |
|---|---|---|
| ビジネス | 何の業務を、誰が、どう進めるか | 業務フロー、業務機能 |
| データ | どんな情報を使い、どう関連するか | データ項目、ER図 |
| アプリケーション | 業務を支えるシステムの機能・関係 | 情報システム関連図 |
| テクノロジ | システムを何で実現するか | ハード・ソフト・ネットワークの構成図 |

**「業務機能を担うシステム」と「そのシステムを動かす技術基盤」**を区別するのが、特に大切です。

EAを考える上位方針は[情報戦略](/fe/information-strategy/)、IT全体を経営目標に沿って統制する考え方は[ITガバナンス](/fe/it-governance/)で整理しています。

## 直感的な説明

EAは、会社全体を複数の視点から見る設計図のようなものです。同じ販売業務でも、何に注目するかで整理する内容が変わります。

**見るポイント：4枚のカードは、すべて同じ販売業務を別の視点から見ています。**

<div class="fe-ea-diagram">
<p class="fe-ea-diagram__title">販売業務を4つの視点で見る</p>
<div class="fe-ea-diagram__grid">
<section class="fe-ea-diagram__card" aria-labelledby="fe-ea-business">
<h3 id="fe-ea-business">1. ビジネス：業務</h3>
<p class="fe-ea-diagram__question">何を、誰が、どう進める？</p>
<ul><li>営業担当が注文を受け付ける</li><li>倉庫担当が商品を出荷する</li></ul>
<p class="fe-ea-diagram__artifact">成果物例：業務流れ図</p>
</section>
<section class="fe-ea-diagram__card" aria-labelledby="fe-ea-data">
<h3 id="fe-ea-data">2. データ：情報</h3>
<p class="fe-ea-diagram__question">どんな情報が関連する？</p>
<ul><li>顧客・注文・商品</li><li>注文番号、注文日、顧客番号</li></ul>
<p class="fe-ea-diagram__artifact">成果物例：ER図・データ定義表</p>
</section>
<section class="fe-ea-diagram__card" aria-labelledby="fe-ea-application">
<h3 id="fe-ea-application">3. アプリケーション：機能</h3>
<p class="fe-ea-diagram__question">どのシステムが何を担う？</p>
<ul><li>販売管理が受注を処理する</li><li>在庫管理と出荷情報を連携する</li></ul>
<p class="fe-ea-diagram__artifact">成果物例：情報システム関連図</p>
</section>
<section class="fe-ea-diagram__card" aria-labelledby="fe-ea-technology">
<h3 id="fe-ea-technology">4. テクノロジ：技術基盤</h3>
<p class="fe-ea-diagram__question">何を使って動かす？</p>
<ul><li>サーバ・OS・ミドルウェア</li><li>本社と倉庫を結ぶネットワーク</li></ul>
<p class="fe-ea-diagram__artifact">成果物例：ソフトウェア構成図・ネットワーク構成図</p>
</section>
</div>
<p class="fe-ea-diagram__note">番号は見分けるための整理順です。4体系は互いに関係し、検討を行き来します。</p>
</div>

「販売管理システムが何をするか」はアプリケーション、「どのサーバやOSで動かすか」はテクノロジです。

## 定義・仕組み

### 4体系と代表的な成果物

成果物は、検討した内容を図や表、説明書として表したものです。試験では、成果物の名前から体系を選ぶこともあります。

| 体系 | 別の呼び方 | 代表的な成果物 |
|---|---|---|
| ビジネス（Business Architecture） | 政策・業務体系 | 業務説明書、機能構成図（DMM）、機能情報関連図（DFD）、業務流れ図 |
| データ（Data Architecture） | データ体系 | 実体関連図（ERD・ER図）、データ定義表、情報体系整理図 |
| アプリケーション（Application Architecture） | 適用処理体系 | 情報システム関連図、情報システム機能構成図 |
| テクノロジ（Technology Architecture） | 技術体系 | ネットワーク構成図、ソフトウェア構成図、ハードウェア構成図 |

例えば、データ定義表ではデータ項目の意味や形式を整理します。ソフトウェア構成図では、各機器に実装するソフトウェアの種類や配置を整理します。

### アプリケーションとテクノロジの違い

両方にソフトウェアが関係するため、**「ソフトウェアが出てきたらアプリケーション」とは判断できません。**

| 比較する点 | アプリケーション | テクノロジ |
|---|---|---|
| 中心となる問い | 業務をどのシステム・機能で支えるか | システムをどの技術で実現するか |
| 販売業務の例 | 販売管理、在庫管理、会計の機能と連携 | サーバ、OS、ミドルウェアの種類と配置 |
| 成果物の例 | 情報システム機能構成図 | ソフトウェア構成図 |

データベースについても、**顧客・注文のデータ項目や関係**ならデータ体系、**DBMSという製品やその配置**なら技術体系、と見る対象を分けます。

### As-Is・To-Beと移行計画

EAでは、現状と目指す姿を整理し、その差を埋める改善を考えます。

| 段階 | 意味 | 販売業務の例 |
|---|---|---|
| As-Is | 現状 | 部門ごとに顧客データを持ち、受注情報を転記している |
| To-Be | あるべき姿 | 顧客データを共有し、受注・在庫・会計を連携する |
| 移行計画 | 現状から目指す姿へ進む計画 | 顧客項目をそろえ、データ移行とシステム連携を段階的に進める |

**4体系は「何を見るか」、As-Is・To-Beは「現状か、目指す姿か」**という別の軸です。現状とあるべき姿の両方を、4体系の視点で整理します。

EAは、[IPA：基本情報技術者試験シラバス Ver.9.2](https://www.ipa.go.jp/shiken/syllabus/omgdg50000005kpe-att/syllabus_fe_ver9_2.pdf)の「システム戦略」で扱われています。4体系の説明と、ソフトウェア構成図・ネットワーク構成図などの用語例を確認できます。最新版の掲載先は[IPA：試験要綱・シラバス](https://www.ipa.go.jp/shiken/syllabus/gaiyou.html)です。

## 科目Aでどう出る？

### 成果物が何を表すかで選ぶ

次の順で読むと、名前の似た図を区別しやすくなります。

1. **業務の内容や手順**を表すか → ビジネス
2. **データの内容や関係**を表すか → データ
3. **情報システムの業務機能や関係**を表すか → アプリケーション
4. **機器・ソフトウェア・ネットワークの構成**を表すか → テクノロジ

「機能構成図」と「情報システム機能構成図」は名前が似ています。EAの成果物として、前者は業務機能、後者は情報システムが実装する機能、と対象を区別します。

### 4体系の名称を選ぶ

4体系は、**Business / Data / Application / Technology**です。

「システムアーキテクチャ」「ソフトウェアアーキテクチャ」「バスアーキテクチャ」は一般的なIT用語として使われますが、この4体系の名称そのものではありません。

### 具体例で4体系を判断する練習

同じ会社の取り組みでも、**何を整理しているか**で体系が変わります。事例を読んで4つの体系から選び、判断理由を確認しましょう。

<div class="fe-ea-practice" data-ea-practice>
  <p class="fe-ea-practice__progress" data-progress aria-live="polite">事例 1 / 4</p>
  <p class="fe-ea-practice__question" data-question>受注情報と顧客情報の関連を整理する。</p>
  <div class="fe-ea-practice__choices" role="group" aria-label="EAの体系を選ぶ">
    <button type="button" data-choice="business">ビジネス</button>
    <button type="button" data-choice="data">データ</button>
    <button type="button" data-choice="application">アプリケーション</button>
    <button type="button" data-choice="technology">テクノロジ</button>
  </div>
  <p class="fe-ea-practice__feedback" data-feedback role="status" aria-live="polite">体系を選ぶと判断理由が表示されます。</p>
  <div class="fe-ea-practice__nav">
    <button type="button" data-prev disabled>前の事例</button>
    <button type="button" data-next>次の事例</button>
  </div>
</div>

<noscript>JavaScriptなしでの答え：事例1は情報同士の関連を整理しているため、データアーキテクチャです。</noscript>

<style>
.fe-ea-practice{border:1px solid #b8c6cb;border-radius:12px;padding:1rem;margin:1.2rem 0;background:#f7f9f9;color:#263b43}
.fe-ea-practice__progress{font-size:.88rem;color:#536a73;margin:0 0 .6rem}
.fe-ea-practice__question{font-weight:650;line-height:1.7;min-height:3.4em}
.fe-ea-practice__choices{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.6rem}
.fe-ea-practice button{border:1px solid #8ca4ad;border-radius:8px;background:#fff;color:#263b43;padding:.8rem .4rem;min-height:44px;cursor:pointer;font:inherit;font-size:.9rem;overflow-wrap:anywhere}
.fe-ea-practice button:focus-visible{outline:3px solid #527e90;outline-offset:2px}
.fe-ea-practice button[aria-pressed="true"]{background:#dcebed;border-color:#527e90;font-weight:700}
.fe-ea-practice button:disabled{opacity:.45;cursor:default}
.fe-ea-practice__feedback{background:#eaf0f1;border-radius:8px;padding:.8rem;line-height:1.7;min-height:4em}
.fe-ea-practice__nav{display:flex;justify-content:space-between;gap:.6rem}
</style>
<script>
(function(){
  function init(){
    document.querySelectorAll('[data-ea-practice]').forEach(function(root){
      if(root.dataset.initialized)return;
      root.dataset.initialized='true';
      var examples=[
        {question:'受注情報と顧客情報の関連を整理する。',answer:'data',why:'情報の内容や関係を整理するため、データ体系です。'},
        {question:'在庫管理システムに必要な機能を整理する。',answer:'application',why:'業務を支えるシステムの機能を整理するため、アプリケーション体系です。'},
        {question:'工場の受注から出荷までの業務手順を見直す。',answer:'business',why:'業務そのものの流れを整理するため、ビジネス体系です。'},
        {question:'システムを動かすサーバとネットワークの構成を整理する。',answer:'technology',why:'システムを実現する技術基盤を整理するため、テクノロジ体系です。'}
      ];
      var index=0,selected={};
      var progress=root.querySelector('[data-progress]');
      var question=root.querySelector('[data-question]');
      var feedback=root.querySelector('[data-feedback]');
      var buttons=root.querySelectorAll('[data-choice]');
      var prev=root.querySelector('[data-prev]');
      var next=root.querySelector('[data-next]');
      function render(){
        var ex=examples[index],choice=selected[index];
        progress.textContent='事例 '+(index+1)+' / '+examples.length;
        question.textContent=ex.question;
        buttons.forEach(function(b){b.setAttribute('aria-pressed',String(b.dataset.choice===choice));});
        feedback.textContent=choice ? (choice===ex.answer?'正解です。':'整理する対象に注目しましょう。')+ex.why : '体系を選ぶと判断理由が表示されます。';
        prev.disabled=index===0;
        next.disabled=index===examples.length-1;
      }
      buttons.forEach(function(b){b.addEventListener('click',function(){selected[index]=b.dataset.choice;render();});});
      prev.addEventListener('click',function(){if(index>0){index--;render();}});
      next.addEventListener('click',function(){if(index<examples.length-1){index++;render();}});
      render();
    });
  }
  if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',init);}else{init();}
})();
</script>

## どんな場面で使う？

EAは、部門ごとの業務や複数のシステムを、組織全体として整理したい場面で使います。

- 部門ごとに異なる業務手順を標準化する
- 重複しているシステムを整理する
- 顧客や商品のデータの持ち方をそろえる
- 経営目標に合わせて、将来のシステムと技術基盤を検討する

一つのシステムだけを便利にするのではなく、**ほかの業務やシステムとの関係も含めて最適化する**ことが目的です。

## よくある誤解・混同

### ソフトウェア構成図はアプリケーション体系？

EAの成果物分類では、**ソフトウェア構成図はテクノロジ体系**です。

ソフトウェアの種類や配置という技術的な構成を見るためです。一方、情報システム機能構成図は、業務を担うシステムの機能を見るアプリケーション体系です。

### DFDはデータ体系？

DFDはデータの流れを描きますが、**EAの代表的な成果物分類ではビジネス体系**です。業務で情報がどのように受け渡され、処理されるかを整理します。

データそのものの構成や関係を整理するER図・データ定義表と区別しましょう。DFDという図法の一般的な用途と、EAでの成果物分類を混同しないことがポイントです。

### EAはシステム構成図のこと？

EAは、業務・データ・アプリケーション・技術基盤を含む全体の設計・管理手法です。ネットワーク構成図などは、その一部を表す成果物です。

### 4体系は必ず順番どおりに検討する？

業務から技術基盤へ考えると理解しやすくなりますが、4体系は互いに関係します。技術上の制約を踏まえて業務やシステムを見直すこともあるため、固定の作業順ではありません。

## 確認問題（基本情報技術者試験対策）

販売管理システムを動かすために、サーバ上のOS・ミドルウェアの種類と配置を図にまとめた。EAの4体系のうち、この成果物を分類する体系として最も適切なものはどれか。

- ア. ビジネスアーキテクチャ
- イ. データアーキテクチャ
- ウ. アプリケーションアーキテクチャ
- エ. テクノロジアーキテクチャ

<details markdown="1">
<summary>▶ 答えと解説を見る</summary>

**正解：エ**

OSやミドルウェアの種類・配置は、システムを実現する技術基盤の構成なので、テクノロジ体系です。

アは業務の内容や手順、イはデータの内容や関係、ウは業務を支えるシステムの機能や関係を整理します。ソフトウェアが登場しても、今回の対象は業務機能ではなく技術基盤です。

</details>

## まとめ（試験直前用）

- EAは、組織全体の業務とシステムを**全体最適**の視点で整理・改善する手法
- **業務＝ビジネス、情報＝データ、システム機能＝アプリケーション、技術基盤＝テクノロジ**
- ソフトウェア構成図・ネットワーク構成図・ハードウェア構成図はテクノロジ
- DFDは業務の流れ、ER図・データ定義表はデータの構成や関係、と区別する
- As-Isは現状、To-Beはあるべき姿。差を埋めるために移行計画を考える

{% include fe_article_footer.html %}
