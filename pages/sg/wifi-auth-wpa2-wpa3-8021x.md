---
layout: page
title: "無線LAN認証の運用｜Personal・Enterprise・802.1Xを選ぶ【SG試験】"
description: "退職者一人の接続を止める例から、共通パスワード運用とEnterpriseの個別認証を比較します。WPA2-PersonalのPSKとWPA3-PersonalのSAEを区別し、802.1X・RADIUS・認証VLAN・DHCPの役割と機器の配置を整理します。"
permalink: /sg/wifi-auth-wpa2-wpa3-8021x/
tags: [sg, access_control, network, sg-security-measures]
prev: /sg/waf/
next: /sg/work-rules-vs-individual-agreement/
last_modified_at: 2026-10-21
---

## まず結論

無線LANの認証では、**WPA2・WPA3という世代と、Personal・Enterpriseという運用方式を分けます。** 利用者や端末ごとの認証・失効を管理したいなら、802.1Xを用いるEnterprise構成を検討します。

世代や暗号の違いは[Wi-Fiセキュリティ方式の比較](/sg/wifi-security-protocols/)へ進んでください。このページは「誰をどう接続させるか」という運用を扱います。

## 直感的な説明

全員に共通の接続パスワードを渡す運用と、一人ずつの認証情報や証明書を管理する運用では、退職者が出たときの作業が違います。新しい世代を選ぶだけで、個別の利用者管理まで実現するわけではありません。

## 定義・仕組み

| 組合せ | 認証・鍵共有で見るポイント | 運用上の確認 |
|---|---|---|
| WPA2-Personal | PSKを用いる | 共通パスワードを知る人の管理、漏えい時の変更 |
| WPA3-Personal | SAEを用いる | 共通パスワード運用なら利用者個別の失効を別途考える |
| WPA2／WPA3-Enterprise | 802.1X・EAP等を用いる | 利用者・端末ごとの認証情報や証明書、失効、認証サーバの管理 |

WPA3-Personalもパスワードを使えますが、**WPA2-Personalと同じPSK認証方式、と一括りにはしません。** 802.1X側も、必ずIDとパスワードだけを使うわけではなく、EAP-TLSのような証明書を使う構成があります。

### 802.1XとRADIUSを組み合わせた役割

| 役割 | 通常の配置 | 何をするか |
|---|---|---|
| サプリカント | 利用者端末 | 認証を受ける |
| オーセンティケータ | APやL2スイッチ | 認証通信を中継し、結果に基づき接続を制御する |
| RADIUSクライアント | APやL2スイッチ | 認証サーバへ要求を送る |
| RADIUSサーバ | 認証サーバ | 認証結果や認可に必要な情報を返す |

RADIUSは認証・認可・アカウンティングに使うプロトコルです。「RADIUS」という語と「RADIUSサーバ」という機器の役割を分けて読みます。

## どんな場面で使う？

### 退職した一人の接続を止めたい

共通パスワード運用では、その人だけに「知らなかったこと」にしてもらうことはできません。パスワード変更が他の利用者へ影響します。Enterprise構成で利用者・端末ごとの認証情報を管理すれば、対象のアカウントや証明書の無効化を行いやすくなります。

認証を止めた後、既存セッションの扱いなど、機器の動作と運用手順も確認します。

### 接続先のネットワークを権限で分けたい

認証結果に応じて所属VLANを変えるのが、認証VLANの考え方です。802.1Xは認証の枠組み、VLANはネットワーク分離の仕組みとして分けます。実際に接続を制御するのはAPやスイッチ側です。

### 契約者だけに公衆無線LANを使わせたい

SSIDやIPアドレスを変えるだけでは、契約者の本人確認にはなりません。接続時の認証やWeb画面での認証等、サービスの要件に合う認証を確認します。キャプティブポータルは802.1Xと同じ仕組みではありません。

## よくある誤解・混同

- WPA3なら必ず個人ごとの管理ができる → PersonalかEnterpriseか、認証情報の運用まで見る。
- 802.1Xは暗号アルゴリズム → ネットワークへの認証・接続制御の枠組み。
- L2スイッチやAPが出たら、必ず認証VLAN → 認証結果でVLANを変える説明があるか確認する。
- DHCPが利用者を認証する → DHCPの中心はIP設定の配布。
- 社内は必ずEnterprise、会場は必ずPersonal → 規模や場所だけでなく、個別失効・本人確認等の要件で選ぶ。

## まとめ（試験直前用）

- 世代とPersonal／Enterpriseを別の軸で読む。
- WPA2-PersonalはPSK、WPA3-PersonalはSAE。
- Enterpriseの個別管理と、端末・AP・認証サーバの役割を確認する。
- 認証、VLANによる分離、DHCPのIP配布を混同しない。

## 公式情報・参考リンク

- [Cisco：WPA3導入ガイド](https://www.cisco.com/c/ja_jp/td/docs/wireless/controller/9800/technical-reference/wpa3-dg.html)
  - PersonalのSAEとEnterpriseの802.1X等の違いを確認できます。

{% include sg_article_footer.html %}
