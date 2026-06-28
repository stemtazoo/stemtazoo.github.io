---
layout: page
title: 個人識別符号とは？個人情報になる条件を整理【DS検定】
description: "個人識別符号は、個人情報になる条件を理解するための基本テーマです。DS検定で問われる定義、具体例、似た概念との違い、選択肢の見分け方を整理します。主要な混同パターンや実務での読み取り方も確認します。初学者が迷いやすい判断ポイントも確認します。"
permalink: /ds/personal-identifier-code/
categories: [ai-utilization]
tags: [ds, ethics]
prev: /ds/opt-out/
next: /ds/sensitive-personal-information/
last_modified_at: 2026-06-28
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

- **個人識別符号とは、それ単体で特定の個人を識別できる番号やデータです。**
- DS検定では **「それだけで個人情報になるかどうか」** を判断させる問題が出ることがあります。

重要なポイントは次の一行です。

**個人識別符号は、それ単体で個人情報になります。**


## 直感的な説明

例えば次のような情報があるとします。

- マイナンバー  
- 指紋  
- 顔認証データ  
- 運転免許証番号  

これらは

**名前や住所がなくても  
特定の個人を識別できます。**

つまり

|情報|個人特定|
|---|---|
|電話番号|場合による|
|Cookie|通常は特定できない|
|マイナンバー|特定できる|

このように

**それだけで個人を識別できる情報**

を

**個人識別符号**

と呼びます。


## 定義・仕組み

個人識別符号とは

**それ単体で特定の個人を識別できる符号**

のことです。

個人情報保護法で定義されています。

代表例は次の通りです。

### 番号系

- マイナンバー  
- 運転免許証番号  
- パスポート番号  
- 健康保険証番号  


### 生体情報系

- 指紋  
- 顔認証データ  
- 虹彩  
- 声紋  

これらは

**身体の特徴から個人を識別できる情報**

です。


### 重要なポイント

通常のデータは

**他の情報と組み合わせて  
個人情報になる場合**

があります。

しかし

個人識別符号は

**単体で個人情報になります。**

ここが試験の重要ポイントです。


## どんな場面で使う？

個人識別符号は主に

### 本人確認

例えば

- 銀行口座開設
- 行政手続き
- 本人認証

などです。


### 生体認証

例えば

- スマートフォンの顔認証
- 指紋認証
- 入退室管理

などです。

DS検定では

**個人識別符号 = 個人情報**

という理解が重要です。


## よくある誤解・混同

### 誤解①  
**個人識別符号は名前がないと個人情報ではない**

これは誤りです。

個人識別符号は

**それ単体で個人情報**

になります。


### 誤解②  
**Cookieは個人識別符号**

これは誤りです。

Cookieは

**単体では個人特定できない**

ため

通常は

**個人関連情報**

です。


### 誤解③  
**要配慮個人情報との違い**

|概念|意味|
|---|---|
|要配慮個人情報|差別につながる可能性のある個人情報|
|個人識別符号|単体で個人識別できる情報|

DS検定では  
この違いを混同させることがあります。

個人識別符号の法令上の定義と具体例は、個人情報保護委員会の[個人情報の保護に関する法律についてのガイドライン（通則編）](https://www.ppc.go.jp/personalinfo/legal/guidelines_tsusoku/)で確認できます。


## まとめ（試験直前用）

- 個人識別符号は **それ単体で個人を識別できる情報**
- 例：マイナンバー・指紋・顔認証など
- 名前がなくても **個人情報になる**
- Cookieなどは通常 **個人関連情報**

DS検定では

**個人識別符号 → 単体で個人情報**

という判断ができれば  
選択肢を切ることができます。


## 対応スキル項目（ビジネス力シート）

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
