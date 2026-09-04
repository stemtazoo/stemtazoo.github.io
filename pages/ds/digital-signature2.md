---
layout: page
title: 電子署名と暗号化の鍵の使い方の違い【DS検定】
description: "電子署名と暗号化では秘密鍵・公開鍵の使い方が逆に見えるため混同しやすいです。署名は秘密鍵で作成し公開鍵で検証する、という試験上の判断軸に絞って整理します。"
permalink: /ds/digital-signature2/
categories: [business]
tags: [ds, security, design]
ds_area: foundation
ds_section: security
prev: /ds/digital-signature/
next: /ds/hash-function/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

電子署名は、**送信者本人が作成したこと**と**途中で改ざんされていないこと**を確認する仕組みです。

DS検定では、電子署名と暗号化で鍵の使い方を混同しないことが重要です。

| 目的 | 使い方 |
|---|---|
| 電子署名 | **送信者の秘密鍵で署名 → 公開鍵で検証** |
| 公開鍵暗号による暗号化 | **受信者の公開鍵で暗号化 → 秘密鍵で復号** |

## 直感的な説明

紙の契約書では、署名や印鑑によって「本人が作成した」と確認します。

デジタルでは、電子署名によって主に次の2点を確認します。

- **本人性**：その送信者が作成したこと
- **完全性**：途中で改ざんされていないこと

> **判断ポイント：** 「署名」は送信者側の秘密鍵、「検証」は送信者の公開鍵です。

## 定義・仕組み

電子署名は公開鍵暗号の考え方を利用します。

### ① メッセージのハッシュ値を作る

送信者はメッセージからハッシュ値を計算します。

ハッシュ値は、内容が変わると値も変わるため、**メッセージの指紋**のように使えます。

### ② 秘密鍵を使って署名を生成する

送信者は、自分の**秘密鍵**を使って電子署名を生成します。

### ③ 公開鍵で検証する

受信者は、送信者の**公開鍵**を使って署名を検証し、受信したメッセージから計算したハッシュ値と対応することを確認します。

一致すれば、

- 送信者本人が署名した
- 内容が途中で改ざんされていない

と判断できます。

## どんな場面で使う？

電子署名は、信頼性が重要な場面で使われます。

- 電子契約
- ソフトウェア配布
- メール署名
- 電子証明書を利用する仕組み

例えばソフトウェア配布では、**公式の配布物か、改ざんされていないか**を確認するために署名が利用されます。

## よくある誤解・混同

### ❌ 公開鍵で署名する

電子署名では、**送信者の秘密鍵で署名を生成**します。

### ❌ 電子署名と暗号化は鍵の使い方が同じ

| 処理 | 鍵の流れ |
|---|---|
| 電子署名 | 秘密鍵 → 署名 / 公開鍵 → 検証 |
| データ暗号化 | 公開鍵 → 暗号化 / 秘密鍵 → 復号 |

### ❌ 電子署名は内容を秘密にする仕組み

電子署名の主目的は、**本人性と完全性の確認**です。

内容を第三者から読めなくすることが主目的なのは暗号化です。

## まとめ（試験直前用）

- **署名 = 送信者の秘密鍵**
- **検証 = 送信者の公開鍵**
- 電子署名は本人性・完全性を確認する
- 暗号化とは目的と鍵の使い方を分けて考える

DS検定では、**「署名＝秘密鍵」「検証＝公開鍵」**を軸に選択肢を切りましょう。

## 対応スキル項目（AI利活用スキルシート）

- AI利活用
- データ・AI利活用におけるリスク管理
- ★ データ・AI利活用に伴うリスク（情報漏洩・セキュリティ等）を理解している

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
