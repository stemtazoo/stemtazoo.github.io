---
layout: page
title: 個人関連情報とは？個人情報との違いを整理【DS検定】
permalink: /ds/personally-related-information/
categories: [business]
tags: [ds, design]
prev: /ds/paper-structure/
next: /ds/polymorphism/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

- **個人関連情報とは、単体では個人を特定できないが、個人と関連する可能性のある情報です。**
- DS検定では **「個人情報との違い」や「Cookie・閲覧履歴の扱い」** がよく問われます。

ポイントは次の一行です。

**個人関連情報は「単体では個人を特定できない情報」です。**


## 直感的な説明

例えば次のようなデータがあります。

- Webサイトの閲覧履歴  
- Cookie  
- IPアドレス  
- 位置情報  

これらの情報は

**それだけでは「誰か」を特定できません。**

しかし、

- 会員情報
- 名前
- メールアドレス

などと組み合わせると  
**特定の個人を識別できる可能性があります。**

このような情報を

**個人関連情報**

と呼びます。

DS検定では

**「単体では個人特定できない」**

という点が重要です。


## 定義・仕組み

個人関連情報とは

**個人情報ではないが、  
個人に関連する可能性がある情報**

です。

日本の個人情報保護法で定義されています。

代表例は次の通りです。

### 代表例

- Cookie  
- IPアドレス  
- 位置情報  
- 購買履歴  
- 閲覧履歴  

これらは単体では

**特定の個人を識別できません。**

そのため  
通常は **個人情報には該当しません。**


### 個人情報になる場合

重要なのはここです。

これらの情報が

- 名前
- 会員ID
- メールアドレス

などと結びつくと

**個人情報として扱われる可能性があります。**

つまり

**状況によって扱いが変わる情報**

ということです。


## どんな場面で使う？

個人関連情報は主に

### Webサービス

例えば

- Web広告
- アクセス解析
- レコメンド

などです。

このとき使われる

- Cookie
- 行動履歴

などが個人関連情報になります。


### データ分析

企業が

- 行動分析
- マーケティング分析
- 利用ログ分析

を行うときにも使われます。

DS検定では

**データ活用とプライバシー保護**

のバランスとして出題されることがあります。


## よくある誤解・混同

### 誤解①  
**Cookie = 個人情報**

これは必ずしも正しくありません。

Cookieは

**単体では個人を特定できない**

ため  
通常は **個人関連情報**です。


### 誤解②  
**個人関連情報は規制がない**

これも誤りです。

第三者提供などの場面では  
一定のルールがあります。


### 誤解③  
**個人情報との違い**

整理すると次の通りです。

|種類|特徴|
|---|---|
|個人情報|個人を識別できる|
|個人関連情報|単体では個人識別できない|

DS検定では

**識別できるかどうか**

が判断ポイントになります。


## まとめ（試験直前用）

- 個人関連情報は **単体では個人を特定できない情報**
- Cookie・閲覧履歴・IPアドレスなどが代表例
- 他の情報と結びつくと **個人情報になる可能性**
- DS検定では **個人識別できるかどうか** が判断基準

整理すると

**個人情報 → 個人を識別できる  
個人関連情報 → 単体では識別できない**

この違いを押さえることが重要です。


【対応スキル項目（ビジネス力シート）】

- ビジネスにおけるデータ活用  
- 法律・倫理  

★ 個人情報保護やプライバシー保護に関する法制度を理解している

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
