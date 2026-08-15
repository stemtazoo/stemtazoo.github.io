---
layout: page
title: SSL/TLSとは？公開鍵暗号と共通鍵暗号の役割を整理【DS検定】
description: "SSL/TLSとは、通信の最初に公開鍵暗号で安全に鍵を共有し、その後は共通鍵暗号で高速にデータを守る仕組みです。DS検定で問われる定義、具体例、似た概念との違い、選択肢の見分け方を整理します。"
permalink: /ds/ssl-tls/
categories: [business]
tags: [ds, security, design]
prev: /ds/rbac/
next: /ds/vpn-ssh/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

SSL/TLSは、**安全性と速度を両立するために、公開鍵暗号と共通鍵暗号を役割分担させる仕組み**です。

DS検定では、次の対応を切り分けられることが重要です。

| 場面 | 主な役割 |
|---|---|
| 通信開始・鍵共有 | 公開鍵暗号などを使って安全に共有する |
| 実際のデータ通信 | 共通鍵暗号で高速に暗号化する |

> **判断ポイント：** 「最初は安全に鍵を共有、その後は共通鍵で高速通信」と覚えると整理しやすいです。

## 直感的な説明

SSL/TLSは、ネット上で安全に会話するための**二段構え**と考えると分かりやすいです。

### ① 最初に安全な通信を確立する

相手が正しい相手かを確認し、安全に通信を始めます。

### ② その後の通信を高速に暗号化する

実際のデータ通信では、共通鍵暗号を使って効率よく暗号化します。

| 重視すること | 適した仕組み |
|---|---|
| 安全な鍵共有・認証 | 公開鍵暗号や証明書 |
| 高速な大量通信 | 共通鍵暗号 |

## 定義・仕組み

TLSは、Webサイトとブラウザなどの間の通信を保護するためのプロトコルです。

### 通信開始時

TLSでは、証明書や公開鍵暗号技術などを使って、

- 相手の確認
- 安全な鍵共有

を行います。

### データ通信時

通信に使う共通鍵（セッション鍵）が決まった後は、**共通鍵暗号**でデータを暗号化します。

共通鍵暗号は高速なので、大量のデータ通信に向いています。

## どんな場面で使う？

- WebサイトのHTTPS通信
- クレジットカード情報の送信
- ログイン情報の送信
- API通信

DS検定では、SSL/TLSを単なる「暗号化技術」ではなく、**通信の安全性を確保する仕組み**として理解しておくと判断しやすくなります。

## よくある誤解・混同

### ❌ SSL/TLSは最初から最後まで公開鍵暗号だけで通信する

これは誤りです。

実際のデータ通信では、速度に優れる**共通鍵暗号**を使います。

### ❌ 共通鍵暗号は公開鍵暗号より弱い

単純に強弱で比べるものではありません。

- 公開鍵暗号 → 鍵共有や署名などに向く
- 共通鍵暗号 → 高速なデータ暗号化に向く

という役割の違いがあります。

### ❌ 暗号化 = 認証

| 用語 | 目的 |
|---|---|
| 暗号化 | 通信内容を第三者に読まれにくくする |
| 認証 | 相手が正しい相手か確認する |

TLSでは両方が関係しますが、役割は別です。

## まとめ（試験直前用）

- **SSL/TLS = 通信を安全にする仕組み**
- 通信開始時は公開鍵暗号技術や証明書を利用
- 実際のデータ通信は共通鍵暗号で高速化
- **公開鍵暗号 = 鍵共有・認証側**
- **共通鍵暗号 = データ通信側**

DS検定では、**「最初は公開鍵、その後は共通鍵」**という役割分担を軸に選択肢を切りましょう。

## 対応スキル項目（AI利活用スキルシート）

- AIの社会実装
- セキュリティ・リスク管理
- ★ AIを活用する際のセキュリティリスクを理解している

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
