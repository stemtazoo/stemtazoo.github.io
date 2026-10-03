---
layout: page
title: ASPとは？SaaS・ホスティング・ハウジングとの違い【基本情報技術者試験】
description: ASP（Application Service Provider）を、SaaS・ホスティング・ハウジング・アウトソーシングとの違いから整理します。FE試験で「何を提供しているか」を見て選択肢を切る判断基準を解説します。
permalink: /fe/asp-service/
tags: [fe, fe-strategy, system-strategy]
fe_section: ストラテジ系
fe_subsection: システム戦略
fe_order: 20
date: 2026-10-03
last_modified_at: 2026-10-03
---

## まず結論

ASP（Application Service Provider）は、**アプリケーションをネットワーク経由で利用者に提供する事業者、またはそのサービス形態**です。

FE試験では、細かな定義を丸暗記するより、**「何を提供しているのか」**を見ると選択肢を切りやすくなります。

<div class="service-map">
  <div><span>施設・場所</span><strong>ハウジング</strong></div>
  <div><span>サーバ</span><strong>ホスティング</strong></div>
  <div><span>アプリ</span><strong>ASP</strong></div>
  <div><span>業務そのもの</span><strong>アウトソーシング</strong></div>
</div>

**「ネットワーク経由でアプリを提供」ならASP**、これが最初の判断基準です。

## 直感的な説明

4つのサービスを「何を借りる・任せるのか」で考えてみます。

~~~text
場所を借りる
  → ハウジング

サーバを借りる
  → ホスティング

アプリを利用する
  → ASP

仕事を任せる
  → アウトソーシング
~~~

特に混同しやすいのが、**ハウジングとホスティング**です。

<div class="housing-hosting">
  <div>
    <strong>ハウジング</strong>
    <p>自分のサーバ<br>↓<br>業者の施設に置く</p>
  </div>
  <div>
    <strong>ホスティング</strong>
    <p>業者のサーバ<br>↓<br>自分が借りる</p>
  </div>
</div>

「ハウジング＝場所」「ホスティング＝サーバ」と切り分ければ迷いにくくなります。

## 定義・仕組み

### ASP

ASPは、サーバ側に用意された業務用などのアプリケーションを、ネットワーク経由で利用者に提供します。

利用者側では、自社ですべてのシステムを構築・管理する場合と比べて、アプリケーションをサービスとして利用しやすくなります。

~~~text
ASP事業者
└─ サーバ
   └─ アプリケーション
          ↓ ネットワーク
        利用者
~~~

試験では、**「汎用的なアプリケーション」「ネットワーク経由」「複数の顧客に提供」**などが手掛かりになります。

### ハウジング

事業者が、サーバなどを設置するための**施設・場所や設備**を提供するサービスです。

利用者側が所有する機器を、事業者の設備が整った施設に設置するイメージです。

### ホスティング

事業者が所有する**サーバの全部または一部を利用者に貸し出す**サービスです。

ハウジングとの違いは、「場所」ではなく**サーバを借りる**点です。

### アウトソーシング

総務、人事、経理など、組織内で行っていた**業務そのものを外部の事業者に委託する**ことです。

ASPのようにアプリを利用する話ではなく、**仕事を外部に任せる**点がポイントです。

## 科目Aでどう出る？

選択肢の文章から、提供対象を拾います。

| 問題文の手掛かり | 判断 |
|---|---|
| 施設、高速回線、耐震設備などを提供 | ハウジング |
| サーバを貸し出す | ホスティング |
| アプリケーションをネットワーク経由で提供 | ASP |
| 人事・経理などの業務を外部に任せる | アウトソーシング |

文章が長くても、まず**「場所・サーバ・アプリ・仕事のどれ？」**と考えると整理できます。

## どんな場面で使う？

ASPは、利用者がアプリケーションを自社ですべて構築・保有するのではなく、ネットワーク経由で利用する形を考えるときに登場します。

現在はSaaSという言葉を目にする機会が多いため、古い問題でASPが出ると戸惑うかもしれません。

FEではまず、ASPを**「ネットワーク経由でアプリを提供する」**という軸で押さえておけば十分です。

## よくある混同

### ASPとSaaSは同じ？

かなり似た形で使われますが、試験対策では無理に完全な同義語として覚えない方が安全です。

~~~text
ASP
→ アプリケーションをネットワーク経由で提供する
  事業者・サービス形態

SaaS
→ ソフトウェアをサービスとして利用する
  クラウドのサービスモデル
~~~

共通しているのは、**利用者がネットワーク経由でソフトウェアを利用する**点です。

IaaS・PaaSなどが並ぶ問題ではクラウドのサービスモデルとしてSaaSを判断し、「ASPとはどのような事業者か」と聞かれたらASPの説明を選びます。

### ハウジングとホスティング

ここは頻出の混同ポイントです。

**ハウジング＝自分の機器を置く場所を借りる。**

**ホスティング＝事業者のサーバを借りる。**

「何を借りるか」を確認しましょう。

### ASPとアウトソーシング

ASPでは**アプリを利用**します。

アウトソーシングでは**業務を外部に任せます**。

「アプリ」と「仕事」を区別すれば切り分けられます。

## まとめ

- **アプリをネットワーク経由で提供 → ASP**
- **施設・場所を提供 → ハウジング**
- **サーバを貸す → ホスティング**
- **業務そのものを外部に任せる → アウトソーシング**
- ASPとSaaSは似ているが、試験では問題文の文脈で判断する
- 迷ったら、**「何を提供している？」**を見る

<style>
.service-map {
  display:grid;
  grid-template-columns:repeat(2, minmax(0,1fr));
  gap:.7rem;
  max-width:620px;
  margin:1.5rem auto;
}
.service-map div {
  padding:1rem;
  border:1px solid #bbb;
  border-radius:8px;
  background:#f7f7f7;
  text-align:center;
}
.service-map span,
.service-map strong {
  display:block;
}
.service-map span {
  font-size:.9rem;
  margin-bottom:.35rem;
}
.housing-hosting {
  display:grid;
  grid-template-columns:repeat(2, minmax(0,1fr));
  gap:1rem;
  max-width:620px;
  margin:1.5rem auto;
}
.housing-hosting div {
  padding:1rem;
  border:1px solid #bbb;
  border-radius:8px;
  text-align:center;
  background:#fafafa;
}
.housing-hosting p {
  margin:.6rem 0 0;
}
@media (max-width:520px) {
  .service-map,
  .housing-hosting {
    grid-template-columns:1fr;
  }
}
</style>
