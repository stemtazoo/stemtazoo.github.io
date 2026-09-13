---
layout: page
title: "Wi-Fiのセキュリティ方式を比較！WEP・WPA・WPA2・WPA3の違い【SG試験】"
description: "WEP・WPA・WPA2・WPA3を、セキュリティ方式・暗号方式・認証方式に分けて整理します。WEPやTKIPを避ける理由、WPA2/WPA3、Personal/Enterprise、AES・CCMP・802.1Xなどを混同しないためのSG試験の判断基準を一次情報とともに確認します。"
permalink: /sg/wifi-security-protocols/
prev: /sg/secure-protocol/
next: /sg/compromise-crypto/
tags: [sg, sg-security-measures, unauthorized_access, network]
last_modified_at: 2026-09-14
---

## まず結論

Wi-Fiのセキュリティ方式は、**WEP → WPA → WPA2 → WPA3**と世代が進むにつれて強化されてきました。

SG試験では、まず次の3点で切り分けると判断しやすくなります。

- **WEPやTKIPを安全な方式として選ばない**
- WPA2・WPA3は、現在使われる代表的な安全性の高い方式
- **セキュリティ方式・暗号方式・認証方式を混同しない**

特に、単純に「WPA2＝AES」と覚えるのではなく、

> WPA2 / WPA3：Wi-Fiのセキュリティ規格  
> AES・CCMPなど：暗号化に関係する仕組み  
> PSK・SAE・802.1Xなど：認証や鍵共有に関係する仕組み

と分けて考えるのがポイントです。

---

## 直感的な説明

Wi-Fiの安全性は、「鍵」だけで決まるわけではありません。

建物の入口に例えると、

- **WPA2・WPA3**：入口全体のセキュリティ方式
- **AES・CCMPなど**：通信内容を守る仕組み
- **PSK・SAE・802.1Xなど**：入ってよい人かを確認する仕組み

というイメージです。

WEPは古く、長いパスワードを設定しても方式自体に弱点があります。

一方、WPA2やWPA3では、より強い暗号化や認証の仕組みを利用できます。

👉 **「パスワードが長いか」だけでなく、「どの方式を使っているか」を見る**ことが大切です。

---

## 定義・仕組み

### WEP・WPA・WPA2・WPA3の位置づけ

| 方式 | 試験での見方 | 注意点 |
|---|---|---|
| WEP | 古く、脆弱 | 選ばない |
| WPA | WEPを改善した過渡的な方式 | 古い方式として扱う |
| WPA2 | 長く広く使われている方式 | 設定・認証方式も確認する |
| WPA3 | WPA2をさらに強化した方式 | Personal / Enterpriseなどを区別する |

IPAの「政府機関等の対策基準策定のためのガイドライン」では、無線LANの暗号化方式としてWPA2 EnterpriseやWPA3 Enterpriseが例示され、**WEPやTKIPは利用すべきではない**とされています。

ここから、SG試験ではまず、

> **WEP・TKIPが安全な選択肢として出てきたら疑う**

と覚えておくと判断しやすくなります。

### 「WPA2＝AES」とだけ覚えない

WPA2の問題では、**AESを利用するCCMP**が代表的な組合せとして問われます。

そのため、

- AES + CCMP → WPA2の代表的な特徴
- RC4 + WEP → 古い無線LAN方式

という対応は試験で有効です。

ただし、AESは暗号アルゴリズム、CCMPは暗号化・完全性保護に使われる仕組み、WPA2はWi-Fiのセキュリティ規格です。

👉 **全部を同じ種類の用語として扱わない**ことが重要です。

### PersonalとEnterprise

WPA2やWPA3には、利用場面に応じた方式があります。

| 種類 | 主な考え方 |
|---|---|
| Personal | 家庭や小規模環境などで利用しやすい |
| Enterprise | 組織で利用者ごとに認証する構成に向く |

Enterpriseでは、IEEE 802.1XやEAPなどを使った利用者認証が重要になります。

IPAのガイドでも、組織の無線LANではWPA2 EnterpriseやWPA3 Enterpriseと、IEEE 802.1Xによる認証が例示されています。

### WPA3で押さえる点

WPA3-Personalでは、従来の事前共有鍵を使う方式から改善され、**SAE（Simultaneous Authentication of Equals）**が採用されています。

試験で

- WPA3-Personal
- SAE
- 辞書攻撃への耐性強化

がセットで出たら関連付けて考えます。

### 一次情報

- [IPA：政府機関等の対策基準策定のためのガイドライン（無線LAN対策を含む）](https://www.ipa.go.jp/security/vuln/scap/ug65p9000001994c-att/guider3_2.pdf)
- [IPA：JC-STAR 適合基準・ガイダンス関連資料](https://www.ipa.go.jp/security/jc-star/tekigou-kizyun-guide/)
- [IPA：試験問題・解答例](https://www.ipa.go.jp/shiken/mondai-kaiotu/index.html)

---

## どんな場面で使う？

### 家庭・小規模環境

Wi-Fiルータなどでは、機器が対応している安全な方式を選びます。

試験では、WEPのような古い方式を「互換性があるから」という理由だけで選ぶ選択肢に注意します。

### 組織の無線LAN

組織では、通信を暗号化するだけでなく、

- 誰が接続しているかを認証する
- 利用者ごとに適切にアクセスを管理する
- 来訪者用ネットワークと業務ネットワークを分ける

といった対策も重要です。

そのため、WPA2/WPA3だけでなく、**802.1XやEAPなどの認証方式**が一緒に問われることがあります。

---

## よくある誤解・混同

### 誤解1：パスワードを長くすればWEPでも安全

❌ WEPは方式自体に弱点があります。

⭕ 強いパスワードだけでなく、**安全なセキュリティ方式を選ぶこと**が必要です。

### 誤解2：WPA2とAESは同じ種類の用語

❌ 同じではありません。

- WPA2：Wi-Fiのセキュリティ規格
- AES：暗号アルゴリズム
- CCMP：暗号化・完全性保護の仕組み

SG試験では、用語の階層を分けて考えます。

### 誤解3：WPA3なら認証方式を考えなくてよい

❌ WPA3にもPersonalとEnterpriseなどがあり、利用場面や認証方式が異なります。

組織向けの問題では、**802.1Xなどによる利用者認証**も確認します。

### 誤解4：WPA3が書いてあれば必ず正解

WPA3は新しい世代の方式ですが、試験では問題文の目的を確認します。

例えば「企業内で利用者ごとに認証したい」という問題なら、単にWPA3という文字だけでなく、**WPA3-EnterpriseやIEEE 802.1X**といった要素まで見る必要があります。

### SG試験でのひっかけポイント

| 問題文のキーワード | 優先して考える用語 |
|---|---|
| RC4・IV・古い無線LAN | WEP |
| AES・CCMP | WPA2でよく問われる組合せ |
| SAE | WPA3-Personal |
| IEEE 802.1X・EAP | Enterprise系の利用者認証 |
| AH・ESP | IPsec |
| TLS Handshake | TLS |

👉 **「Wi-Fiの規格なのか、暗号なのか、認証なのか」**を先に見分けると選択肢を切りやすくなります。

---

## まとめ（試験直前用）

- WEP・TKIPは古く、**安全な方式として選ばない**
- WPA2・WPA3は現在使われる代表的なWi-Fiセキュリティ方式
- AES・CCMPはWPA2と関連して問われやすいが、WPA2そのものと同じ用語ではない
- WPA3-Personalでは**SAE**を押さえる
- 組織向けでは**WPA2/WPA3 Enterprise + IEEE 802.1X**という視点も重要
- SG試験では、**セキュリティ方式・暗号方式・認証方式を分けて読む**

{% include sg_article_footer.html %}
