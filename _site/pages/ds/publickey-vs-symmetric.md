---
layout: page
title: 公開鍵暗号方式と共通鍵暗号方式の違いとは？【DS検定】
description: 公開鍵暗号方式と共通鍵暗号方式の違いは関連概念を切り分けるための考え方です。この記事では仕組み・役割・使いどころを押さえ、DS検定で問われる判断ポイントとひっかけポイントを解説します。
permalink: /ds/publickey-vs-symmetric/
categories: [business]
tags: [ds, security, design]
prev: /ds/primary-secondary-data/
next: /ds/rainbow-table-attack/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

共通鍵暗号方式は「同じ鍵で暗号化と復号を行う方式」

公開鍵暗号方式は「公開鍵と秘密鍵の2つの鍵を使う方式」


DS検定では

「共通鍵暗号＝高速」「公開鍵暗号＝鍵共有問題を解決」

という役割の違いを理解しているかが問われます。



## 直感的な説明

暗号を「鍵付きの箱」で考えてみます。

共通鍵暗号

送る人と受け取る人が

同じ鍵を持っている箱

を使います。

送信者：鍵で箱をロック

受信者：同じ鍵で箱を開ける


仕組みはシンプルで

処理が速いのが特徴です。

しかし問題があります。

その鍵をどうやって安全に相手へ渡すか

です。



公開鍵暗号

公開鍵暗号では鍵が2つあります。

公開鍵

秘密鍵


公開鍵は

誰にでも公開してよい鍵です。

送信者は公開鍵で暗号化します。

すると

秘密鍵を持つ本人しか復号できません。

つまり

安全に鍵を共有する問題を解決できる

のが公開鍵暗号です。



## 定義・仕組み

共通鍵暗号方式（Symmetric Key Cryptography）

暗号化と復号に

同じ鍵を使う方式です。

特徴

処理が高速

大量データの暗号化に向いている


代表例

AES

DES


しかし

鍵を安全に共有する必要がある

という課題があります。



公開鍵暗号方式（Public Key Cryptography）

2つの鍵を使う暗号方式です。

公開鍵：暗号化に使う

秘密鍵：復号に使う


特徴

鍵配送問題を解決

安全な鍵共有が可能


代表例

RSA


ただし

計算が重く処理が遅い

という弱点があります。



現実のインターネット

実際の通信では

両方を組み合わせて使います。

例：SSL / TLS

1. 公開鍵暗号で共通鍵を安全に交換


2. その後は共通鍵暗号で通信



こうすることで

安全

高速


の両方を実現しています。



## どんな場面で使う？

共通鍵暗号

大量データ通信

SSL通信

VPN

データ保存


などで使われます。



公開鍵暗号

鍵交換や認証

電子署名

PKI

SSLの鍵交換


などで利用されます。



## よくある誤解・混同

誤解①

公開鍵暗号の方が安全だから常に使う

これは誤りです。

公開鍵暗号は

処理が重く速度が遅い

ため

通信全体の暗号化には向きません。



誤解②

公開鍵は秘密にする必要がある

公開鍵は

公開してよい鍵です。

秘密にするのは

秘密鍵です。



DS検定の典型問題

DS検定では

❌ 公開鍵暗号方式は高速な暗号方式である

⭕ 共通鍵暗号方式の方が高速

という選択肢がよく出ます。

試験では

共通鍵暗号 → 高速

公開鍵暗号 → 鍵交換


と覚えておくと選択肢を切りやすくなります。



## まとめ（試験直前用）

共通鍵暗号 → 同じ鍵 / 高速 / 大量データ向き

公開鍵暗号 → 公開鍵＋秘密鍵 / 鍵共有問題を解決

公開鍵暗号は処理が遅い

SSL/TLSでは 公開鍵暗号＋共通鍵暗号を併用

DS検定では 高速＝共通鍵暗号 を覚えておく




## 対応スキル項目（データエンジニアリング力シート）

ITセキュリティ

暗号化技術

★ 共通鍵暗号方式と公開鍵暗号方式の違いを理解している

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
