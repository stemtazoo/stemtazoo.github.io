---
layout: page
title: 情報セキュリティ対策まとめ
description: "認証、ネットワーク、マルウェア、脆弱性、IoT、物理対策など、SG試験の情報セキュリティ対策を目的別の入口とタグ連動の全記事一覧で整理します。新規記事も主分類タグから自動で一覧へ反映されます。"
permalink: /sg/category/security-measures/
last_modified_at: 2026-09-09
---

[SGトップへ戻る](/sg/)

## SG試験での見方

情報セキュリティ対策は、技術名だけを暗記するより、**何を守るための対策か**で整理すると判断しやすくなります。

- 本人確認や権限を管理する → 認証・アクセス制御
- 不要な通信を止める、通信を守る → ネットワーク対策
- 不正なプログラムへの感染や被害を防ぐ → マルウェア対策
- 弱点を見つけて修正する → 脆弱性対策
- 機器・通信・クラウド・運用をまとめて守る → IoTセキュリティ
- 入退室や盗難を防ぐ → 物理的セキュリティ対策

選択肢では、**対策名ではなく「目的と対象が合っているか」**を先に確認します。

## まず読むまとめ記事

全体像から学びたい場合は、次のまとめ記事から読むと整理しやすくなります。

- [技術的セキュリティ対策まとめ](/sg/security-measures-overview/)
- [セキュリティ対策の違いまとめ](/sg/security-measures-comparison/)
- [認証・アクセス制御まとめ｜主要用語を整理](/sg/auth-access-control-summary/)
- [ネットワーク防御と通信保護まとめ｜主要用語を整理【SG試験】](/sg/network-defense-summary/)
- [DNS・メールなりすまし対策まとめ｜SPF・DKIM・S/MIMEを整理](/sg/dns-mail-security-summary/)
- [Webアプリ攻撃まとめ｜SQLインジェクション・XSS・CSRFを整理](/sg/web-application-attacks-summary/)
- [マルウェアまとめ｜種類・感染後の動き・解析方法を整理](/sg/malware-threats-summary/)
- [脆弱性対策まとめ｜JVN・CVSS・検査・ペンテスト・ファジングの違い](/sg/vulnerability-cheatsheet/)
- [物理的セキュリティ対策まとめ｜出題パターンと切り分け一覧](/sg/physical-security-summary/)

## テーマ別の入口

### 認証・アクセス制御

「本人確認」なのか「操作できる範囲を決める」のかで切り分けます。

- [認証・認可・アクセス制御の違いとは？役割の切り分けを整理](/sg/authentication-authorization-access-control/)
- [多要素認証（MFA）とは？認証強化の仕組みと判断ポイント](/sg/multi-factor-authentication/)
- [最小権限の原則とは？権限管理の基本を理解](/sg/least-privilege/)
- [ゼロトラストとは？境界防御との違いを整理](/sg/zero-trust/)

### ネットワーク・通信

「通信を遮断する」のか「通信内容を保護する」のかで切り分けます。

- [ファイアーウォールとは？通信を制御する基本対策](/sg/firewall/)
- [IPSとは？不正侵入を検知して遮断する仕組み](/sg/ips/)
- [VPNとは？安全な通信を実現する仕組み](/sg/vpn/)
- [SSL/TLSとは？通信を守る暗号化の仕組み](/sg/ssl-tls/)

### マルウェア・不正プログラム

感染方法だけでなく、**感染後に何をするか**を見ると判断しやすくなります。

- [マルウェアとは？種類と見分け方を整理](/sg/malware/)
- [ランサムウェアとは？身代金要求型攻撃の仕組み](/sg/ransomware/)
- [ボットネットとは？踏み台化とDDoSの関係を理解する](/sg/botnet/)

### 脆弱性・検知・分析

「弱点そのもの」「深刻度」「検査」「対応」を混同しないことが重要です。

- [脆弱性対策まとめ｜JVN・CVSS・検査・ペンテスト・ファジングの違い](/sg/vulnerability-cheatsheet/)
- [CVSSとは？脆弱性の深刻度を共通スコアで判断する](/sg/cvss/)
- [JVNとは？脆弱性情報の見方とJVN iPediaとの違い](/sg/jvn/)
- [脆弱性スキャンとは？自動検査で弱点を見つける仕組み](/sg/vulnerability-scan/)

### IoT・ネットワーク機器

IoTでは、機器だけでなく通信・クラウド・運用まで含めて考えます。

- [IoTセキュリティとは？IoT機器特有のリスクと対策を整理【SG試験】](/sg/iot-security/)
- [Telnetとは？安全でない遠隔操作の仕組み【SG試験】](/sg/telnet/)

### 物理・可用性

情報だけでなく、人の入退室、機器の盗難、停電や故障への対策も確認します。

- [物理的セキュリティ対策まとめ｜出題パターンと切り分け一覧](/sg/physical-security-summary/)
- [遠隔バックアップとは？災害時のデータ保護の基本](/sg/remote-backup/)
- [UPSとは？停電時の業務継続を支える仕組み](/sg/ups/)
- [稼働率とは？可用性の考え方とSLAでの判断基準](/sg/availability/)

## 全記事一覧（タグから自動更新）

以下は、主分類タグ `sg-security-measures` が付いた記事をタイトル順に自動表示しています。

**今後は新規記事に正しい主分類タグを付ければ、このカテゴリページへの手動追記は不要です。**

{% assign security_measure_pages = site.pages | where: "tags", "sg-security-measures" | sort: "title" %}
{% assign security_measure_count = 0 %}
{% for p in security_measure_pages %}
  {% if p.permalink %}
- [{{ p.title }}]({{ p.permalink }})
    {% assign security_measure_count = security_measure_count | plus: 1 %}
  {% endif %}
{% endfor %}
{% if security_measure_count == 0 %}
- 現在、該当記事はありません。
{% endif %}

{% include sg_article_footer.html %}
