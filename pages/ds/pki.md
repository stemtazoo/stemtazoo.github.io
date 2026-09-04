---
layout: page
title: 公開鍵認証基盤（PKI）とは？電子署名の信頼を保証する仕組み【DS検定】
description: "公開鍵認証基盤（PKI：Public Key Infrastructure）とは、「公開鍵が本当にその人のものか」を証明する仕組みです。DS検定で問われる定義、具体例、似た概念との違い、選択肢の見分け方を整理します。主要な混同パターンや実務での読み取り方も確認します。"
permalink: /ds/pki/
categories: [business]
tags: [ds, security, design]
ds_area: foundation
ds_section: security
prev: /ds/oauth/
next: /ds/rbac/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**PKI（Public Key Infrastructure）とは、「その公開鍵が本当に本人・組織のものか」を証明する仕組み**です。

DS検定では、**電子署名だけでは公開鍵の持ち主までは保証できないため、電子証明書と認証局（CA）が必要**と理解しておくことが重要です。

## 直感的な説明

電子署名を「印鑑」に例えると分かりやすくなります。

印鑑が押されていても、**その印鑑が本当に本人のものか**は別に確認する必要があります。現実世界では印鑑証明がその役割を担います。

| 役割 | 現実世界 | デジタル世界 |
|---|---|---|
| 本人との対応を証明 | 印鑑証明 | 電子証明書 |
| 証明する組織 | 市役所など | 認証局（CA） |
| 信頼の仕組み | 公的な登録制度 | PKI |

PKIは、**公開鍵と本人の対応関係を信頼できる形で証明する基盤**です。

## 定義・仕組み

PKIは、公開鍵を安全に信頼して使うための仕組み全体を指します。

中心となる要素は次の通りです。

- 公開鍵
- 秘密鍵
- 電子証明書
- 認証局（CA）

### 電子証明書

電子証明書には、**「この公開鍵はこの人物・組織のものです」**という対応関係を確認するための情報が含まれます。

### 認証局（CA）

認証局は、本人・組織を確認したうえで電子証明書を発行します。

流れは次のように整理できます。

1. 利用者が鍵ペアを用意する
2. 認証局が本人・組織を確認する
3. 電子証明書を発行する
4. 他者が証明書を確認して公開鍵を信頼する

## どんな場面で使う？

PKIは、公開鍵の信頼性が必要な場面で使われます。

- 電子署名
- HTTPS（SSL/TLS）
- クライアント証明書認証
- 電子契約

例えばHTTPSでは、サーバ証明書を確認することで、接続先と公開鍵の対応を確認します。

## よくある誤解・混同

### ❌ 電子署名だけで「その公開鍵が本人のもの」と証明できる

電子署名は、署名の検証や改ざん検知に使えます。しかし、**検証に使う公開鍵そのものが誰のものか**を信頼する仕組みが別に必要です。

### ❌ PKIは暗号アルゴリズム

PKIは暗号方式そのものではなく、**公開鍵を信頼して利用するための運用・認証基盤**です。

### ❌ 認証局が利用者の代わりに暗号化・署名する

認証局の主な役割は、**公開鍵と本人・組織の対応関係を証明すること**です。

## まとめ（試験直前用）

- **PKI = 公開鍵の持ち主を信頼するための基盤**
- **電子証明書** = 公開鍵と本人・組織の対応を示す
- **認証局（CA）** = 証明書を発行する
- 電子署名やHTTPSの信頼性を支える
- **PKIは暗号方式そのものではない**

DS検定では、**「公開鍵が誰のものかを証明する」ならPKI**と判断しましょう。

## 対応スキル項目（ビジネス力）

- 情報セキュリティ
- 認証・暗号の基礎
- ★ 電子証明書と認証局による信頼の仕組みを理解できる

## 🔗 関連記事

<ul style="padding-left: 20px;">
{% assign current_tags = page.tags %}
{% assign count = 0 %}

{% for p in site.pages %}
  {% if p.url != page.url and p.tags %}
    {% assign matched = false %}

    {% for tag in current_tags %}
      {% if p.tags contains tag and tag != "ds" %}
        {% assign matched = true %}
      {% endif %}
    {% endfor %}

    {% if matched %}
      <li style="margin-bottom: 6px;">
        <a href="{{ p.url }}">{{ p.title }}</a>
      </li>
      {% assign count = count | plus: 1 %}
    {% endif %}

    {% if count >= 5 %}
      {% break %}
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

<hr>

<div style="margin-top: 16px;">
  🏠 <a href="/ds/">DS検定トップに戻る</a>
</div>

<div style="display:flex;justify-content:space-between;margin-top:12px;">

  {% if page.previous.url %}
    <a href="{{ page.previous.url }}">← {{ page.previous.title }}</a>
  {% endif %}

  {% if page.next.url %}
    <a href="{{ page.next.url }}">{{ page.next.title }} →</a>
  {% endif %}
</div>
