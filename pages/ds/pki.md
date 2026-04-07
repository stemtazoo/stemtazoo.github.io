---
layout: page
title: 公開鍵認証基盤（PKI）とは？電子署名の信頼を保証する仕組み【DS検定】
description: 公開鍵認証基盤（PKI）は電子署名の信頼を保証する仕組みを理解するための用語です。この記事では仕組み・役割・使いどころを押さえ、DS検定で問われる判断ポイントとひっかけポイントを解説します。
permalink: /ds/pki/
categories: [business]
tags: [ds, security, design]
prev: /ds/oauth/
next: /ds/rbac/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

公開鍵認証基盤（PKI：Public Key Infrastructure）とは、「公開鍵が本当にその人のものか」を証明する仕組みです。

DS検定では 電子署名の信頼性を保証する仕組みとしてPKIが必要になる理由を理解しているか が問われます。


電子署名だけでは 「その公開鍵が本当に本人のものか」は保証できません。

その問題を解決するのが 公開鍵認証基盤（PKI） です。



## 直感的な説明

電子署名はよく 印鑑 に例えられます。

例えば、契約書に印鑑が押されていたとしても、

その印鑑が本当に本人のものか

偽物ではないか


は別の問題です。

ここで必要になるのが 「印鑑証明」 です。

電子署名の世界でも同じで、

役割	現実世界	デジタル世界

本人確認	印鑑証明	電子証明書
証明する組織	市役所	認証局（CA）
本人確認の仕組み	住民登録	PKI


つまりPKIは

「公開鍵の持ち主が本当にその人である」と保証する仕組み

と考えると理解しやすくなります。



## 定義・仕組み

PKI（Public Key Infrastructure）は、

公開鍵と利用者の対応関係を証明するための仕組み全体

を指します。

中心になるのは次の要素です。

公開鍵

秘密鍵

電子証明書

認証局（CA）


電子証明書には、

「この公開鍵はこの人物・組織のものです」

という情報が含まれています。

そしてその証明書を発行するのが認証局です。

つまり

本人が鍵を作る
↓
認証局が本人確認する
↓
電子証明書を発行する
↓
他者がその公開鍵を信用できる

という流れになります。



## どんな場面で使う？

PKIは次のような場面で使われます。

電子署名

SSL/TLS通信

クライアント証明書認証

電子契約


例えばWebサイトのHTTPSでも、

サーバ証明書を通じて

その公開鍵が正しい相手のものだと確認

しています。



## よくある誤解・混同

混同①：電子署名だけで本人性が証明できる

電子署名は改ざん検知や署名確認に使えますが、

その公開鍵が誰のものか

までは単独では保証できません。

そこでPKIが必要になります。



混同②：PKIは暗号方式そのもの

PKIは暗号アルゴリズムではなく、

公開鍵を信頼して使うための運用基盤

です。



混同③：認証局が暗号化を行う

認証局の主な役割は、

公開鍵と本人の対応関係を証明すること

です。

実際の暗号化や署名は利用者が行います。



## まとめ（試験直前用）

PKI＝公開鍵が本当に本人のものかを証明する仕組み

中心要素は電子証明書と認証局（CA）

電子署名の信頼性を支える基盤

HTTPSや電子契約でも使われる



## 対応スキル項目（ビジネス力）

情報セキュリティ

認証・暗号の基礎

★ 電子証明書と認証局による信頼の仕組みを理解できる

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
