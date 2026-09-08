---
layout: page
title: テクノロジ系まとめ
description: "ネットワーク、データベース、システム構成、暗号技術を、何を実現する技術かという入口とタグ連動の全記事一覧で整理します。新規記事は主分類タグから自動反映し、旧タグの記事も移行期間中は拾います。"
permalink: /sg/category/technology/
last_modified_at: 2026-09-09
---

[SGトップへ戻る](/sg/)

## SG試験での見方

テクノロジ系では、技術名だけでなく、**どの層で何を実現する技術か**を見ると切り分けやすくなります。

- 通信や経路を扱う → ネットワーク
- データを保存・検索する → データベース
- システムの構成や冗長化を見る → システム構成
- 秘密性・完全性・認証を支える → 暗号・認証技術

## まず読む

- [ネットワーク防御と通信保護まとめ｜主要用語を整理【SG試験】](/sg/network-defense-summary/)
- [暗号と認証の基本まとめ｜秘密にする・確認するを整理【SG試験】](/sg/crypto-auth-summary/)
- [暗号・証明書・認証基盤まとめ｜証明書運用まで整理【SG試験】](/sg/crypto-auth-platform-summary/)

## テーマ別の入口

### ネットワーク

- [DNSとは？名前解決の仕組みとセキュリティのポイント](/sg/dns/)
- [VPNとは？安全な通信を実現する仕組み](/sg/vpn/)
- [ファイアーウォールとは？通信を制御する基本対策](/sg/firewall/)

### 暗号・認証

- [共通鍵暗号方式とは？高速だが鍵管理が課題の仕組み](/sg/symmetric-key-cryptography/)
- [公開鍵暗号方式とは？鍵の受け渡し問題を解決する仕組み](/sg/public-key-cryptography/)
- [PKIとは？公開鍵基盤の役割をやさしく整理](/sg/pki/)

### システム構成

- [RAIDとは？冗長化による信頼性向上の仕組み](/sg/raid/)
- [稼働率とは？可用性の考え方とSLAでの判断基準](/sg/availability/)

## 全記事一覧（タグから自動更新）

新規記事では主分類タグ `sg-technology` を正とします。既存記事には旧タグだけのものが残っているため、移行期間中は `technology`、`network`、`database`、`system_architecture`、`cryptography`、`crypto_auth` も自動的に拾います。

{% assign sg_pages = site.pages | sort: "title" %}
{% assign category_count = 0 %}
{% for p in sg_pages %}
  {% if p.path contains "pages/sg/" and p.tags %}
    {% unless p.path contains "pages/sg/category/" %}
      {% if p.tags contains "sg-technology" or p.tags contains "technology" or p.tags contains "network" or p.tags contains "database" or p.tags contains "system_architecture" or p.tags contains "cryptography" or p.tags contains "crypto_auth" %}
- [{{ p.title }}]({{ p.url }})
        {% assign category_count = category_count | plus: 1 %}
      {% endif %}
    {% endunless %}
  {% endif %}
{% endfor %}
{% if category_count == 0 %}
- 現在、該当記事はありません。
{% endif %}

{% include sg_article_footer.html %}
