---
layout: page
title: PKIと認証局（CA）とは？デジタル証明書・CRL・OCSPの役割【基本情報技術者試験】
description: PKIと認証局（CA）の役割を、デジタル証明書の発行・失効管理、CRL・OCSPとの関係から整理します。暗号化やデジタル署名との役割分担を押さえ、FE科目Aの選択肢を切る判断基準を解説します。
permalink: /fe/pki-certificate-authority/
tags: [fe, fe-technology, security]
fe_section: テクノロジ系
fe_subsection: セキュリティ
fe_order: 72
date: 2026-10-03
last_modified_at: 2026-10-03
---

<style>
.pki-flow {
  margin: 1.2rem 0;
  padding: 1rem;
  border: 1px solid #d8dee4;
  border-radius: 10px;
}
.pki-flow-row {
  display: flex;
  gap: .6rem;
  align-items: stretch;
  justify-content: center;
  flex-wrap: wrap;
}
.pki-card {
  flex: 1 1 150px;
  max-width: 220px;
  padding: .8rem;
  border: 1px solid #8c959f;
  border-radius: 8px;
  text-align: center;
  background: #f6f8fa;
}
.pki-arrow {
  display: flex;
  align-items: center;
  font-weight: 700;
}
@media (max-width: 600px) {
  .pki-flow-row { flex-direction: column; }
  .pki-card { max-width: none; }
  .pki-arrow { justify-content: center; transform: rotate(90deg); }
}
</style>

## まず結論

認証局（CA：Certification Authority / Certificate Authority）は、**公開鍵とその持ち主を結び付けるデジタル証明書を発行・管理する機関**です。

FEでは、まず次の役割分担で選択肢を切ります。

~~~text
公開鍵が誰のものかを証明
→ デジタル証明書

証明書を発行・管理
→ 認証局（CA）

失効した証明書を一覧で確認
→ CRL

証明書の状態をオンラインで照会
→ OCSP

これらを含む信頼の仕組み全体
→ PKI
~~~

> **CAは「通信データを暗号化する機関」ではなく、「公開鍵を信頼できるようにする機関」です。**

## 直感的な説明

PKIは「ネット上の身分証明の仕組み」と考えると分かりやすくなります。

<div class="pki-flow">
<div class="pki-flow-row">
  <div class="pki-card"><strong>利用者・サーバ</strong><br>公開鍵を用意</div>
  <div class="pki-arrow">→</div>
  <div class="pki-card"><strong>認証局（CA）</strong><br>確認して証明書を発行</div>
  <div class="pki-arrow">→</div>
  <div class="pki-card"><strong>デジタル証明書</strong><br>公開鍵と主体を結び付ける</div>
</div>
</div>

例えばWebサイトが公開鍵を提示しても、それだけでは、

> 「本当にそのWebサイトの公開鍵なのか？」

を判断できません。

そこで、信頼された認証局が発行した証明書を使って、公開鍵とWebサイトなどの主体との結び付きを確認します。

## 定義・仕組み

### PKIとは

PKI（Public Key Infrastructure：公開鍵基盤）は、公開鍵暗号、デジタル証明書、認証局などを使って、**公開鍵を安全に利用するための信頼の仕組み**です。

PKIは暗号方式そのものではありません。

~~~text
公開鍵暗号
→ 暗号技術

デジタル証明書
→ 公開鍵と主体を結び付けるデータ

認証局（CA）
→ 証明書を発行・管理する主体

PKI
→ それらを運用する仕組み全体
~~~

### 認証局（CA）の役割

認証局の代表的な役割は、デジタル証明書の発行と、そのライフサイクルの管理です。

~~~text
申請
↓
必要な確認
↓
証明書を発行
↓
利用
↓
必要なら失効
~~~

証明書の信頼性を支えるため、CA自身の秘密鍵も厳重に管理されます。

### デジタル証明書

デジタル証明書には、公開鍵、証明書の対象となる主体の情報、有効期間、発行者などが含まれ、CAの署名によって検証できる形になっています。

ポイントは、

> **証明書そのものが通信データを暗号化するわけではない**

ことです。

証明書は、利用しようとしている公開鍵を信頼できるか判断するために使われます。

### 証明書の失効

証明書には有効期限がありますが、期限内でも秘密鍵の漏えいなどが起きれば、信頼して使い続けるべきではありません。

そのため、証明書を期限前に失効させる仕組みがあります。

## CRLとOCSP

### CRL

CRL（Certificate Revocation List）は、**失効した証明書を示すリスト**です。

~~~text
複数の失効情報
↓
一覧として公開
↓
CRL
~~~

FEで、

> 「失効したデジタル証明書の一覧」

とあれば、CRLが強い手掛かりです。

### OCSP

OCSP（Online Certificate Status Protocol）は、証明書の状態をオンラインで問い合わせるためのプロトコルです。

~~~text
CRL
→ 一覧で失効情報を確認

OCSP
→ 対象の証明書の状態をオンライン照会
~~~

試験では、この違いを押さえておけば十分です。

## 科目Aでどう出る？

認証局の問題は、「何をする機関か」を他のセキュリティ技術と混ぜて出されます。

### 共通鍵を生成する

これだけでCAの役割とは判断しません。

認証局の中心は、**デジタル証明書の発行・管理と公開鍵への信頼の付与**です。

### 公開鍵を使って通信データを暗号化する

公開鍵暗号を利用する側の処理です。

~~~text
暗号化する
→ 暗号技術・通信処理

公開鍵が誰のものか保証する
→ 証明書・CA
~~~

「公開鍵」という単語だけでCAを選ばないようにします。

### 失効した証明書の一覧を扱う

これはCA・PKIの証明書管理に関係します。

~~~text
失効証明書の一覧
→ CRL
→ CAによる証明書管理
~~~

CAの役割を問う選択肢として適切です。

### データが改ざんされていないことを検証する

これは、デジタル署名やMACなどと関連する話です。

CAの中心的役割は、個々の通信データを直接検証することではありません。

## どんな場面で使う？

代表例はHTTPSです。

Webサイトから証明書を受け取ったブラウザは、証明書の署名や信頼の連鎖、有効期間などを検証し、必要に応じて失効状態も確認します。

~~~text
Webサイト
↓ 証明書
ブラウザ
↓
信頼できるCAにつながるか
有効期間内か
失効していないか
↓
公開鍵を信頼できるか判断
~~~

ここでもCAがWeb通信そのものを暗号化しているわけではありません。

## よくある誤解・混同

### CAが公開鍵暗号で通信データを暗号化する

違います。

~~~text
CA
→ 証明書を発行・管理

暗号化
→ 通信するシステム側で行う
~~~

「CA＝暗号化装置」と考えないことが重要です。

### CAがデータの改ざんを直接検証する

データの完全性や署名の検証は、ハッシュ、MAC、デジタル署名などの仕組みと関係します。

CAは、そこで利用される公開鍵を信頼できるようにする役割を担います。

### CRLは有効な証明書の一覧

逆です。

> **CRL＝失効した証明書に関するリスト**

と覚えます。

### 有効期限内なら証明書は必ず有効

有効期限内でも、秘密鍵の漏えいなどによって証明書が失効している可能性があります。

そのため失効状態の確認が必要になります。

### CRLとOCSPは同じ

目的はどちらも証明書の状態確認に関係しますが、方法が違います。

| 用語 | 判断ポイント |
|---|---|
| CRL | 失効情報を**一覧**で確認 |
| OCSP | 証明書の状態を**オンライン照会** |

「一覧」か「問い合わせ」かを見ると切り分けやすくなります。

## まとめ（試験直前用）

- PKI → 公開鍵を安全に利用するための**仕組み全体**
- CA → デジタル証明書を**発行・管理**
- デジタル証明書 → **公開鍵と主体を結び付ける**
- CRL → **失効情報を一覧で確認**
- OCSP → **証明書の状態をオンライン照会**
- CAは通信データを暗号化する機関ではない

> **「公開鍵が誰のものかを信頼させる」なら、証明書・CA・PKIの話。**

## 公式情報・参考リンク

- [IETF RFC 5280：Internet X.509 Public Key Infrastructure Certificate and CRL Profile](https://www.rfc-editor.org/rfc/rfc5280.html)
- [IETF RFC 6960：X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP](https://www.rfc-editor.org/rfc/rfc6960.html)

{% include fe_article_footer.html %}
