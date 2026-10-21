---
layout: page
title: 暗号・証明書・認証基盤まとめ｜証明書運用まで整理【SG試験】
description: "Webサーバ証明書の申請・発行、配備、期限監視、更新、秘密鍵漏えい時の失効を運用の流れで整理します。CRL・OCSPで分かる失効状態と、名前・有効期間・信頼連鎖の検証を区別し、鍵の保管や復旧を学ぶ記事へつなぎます。"
permalink: /sg/crypto-auth-platform-summary/
tags: [sg, sg-security-measures, crypto_auth]
last_modified_at: 2026-10-21
---

## まず結論

証明書の運用では、**発行して終わりにせず、配備・更新・秘密鍵の保護・事故時の失効まで管理する**ことが必要です。ここではWebサーバ証明書を例に、担当者がいつ何を確認するかを整理します。

技術を最初から選ぶ入口は[暗号と認証の基本まとめ](/sg/crypto-auth-summary/)、受信データの検証は[改ざん検知・電子署名・証明書まとめ](/sg/crypto-certificate-integrity-summary/)へ進めます。

## 全体像

公開Webサーバの証明書を管理する場面です。更新漏れならサービスの利用に支障が出ますし、有効期限が残っていても秘密鍵が漏れたら対応が必要です。

**申請・発行 → 配備 → 期限監視・更新 → 漏えい等の発覚時は失効・再発行**という一連の管理として考えます。失効は期限満了まで待つ処理ではありません。

## 主要用語の整理

| 運用場面 | 確認すること | 詳しく読む先 |
|---|---|---|
| 証明書の申請・発行 | 公開鍵と主体を結び付ける発行手続 | [電子証明書](/sg/digital-certificate/)、[認証局の役割](/sg/certificate-authority-role/) |
| サーバへの配備 | 適切な証明書・中間証明書と対応する秘密鍵 | [ルート証明書と中間証明書](/sg/root-intermediate-certificate/) |
| 定期的な更新 | 期限・担当者・更新手順・切替後の動作 | [PKI](/sg/pki/)、[TLS](/sg/ssl-tls/) |
| 秘密鍵の漏えい | 鍵の交換、証明書の失効と再発行 | [CRLとOCSP](/sg/certificate-revocation-crl-ocsp/) |
| 鍵の保管・復旧 | 端末での保護、復元条件と権限 | [TPM](/sg/tpm/)、[秘密分散法](/sg/secret-sharing/) |
| 暗号の見直し | 利用方式の安全性と移行対象 | [CRYPTREC暗号リスト](/sg/cryptrec-list/)、[暗号の危殆化](/sg/cryptographic-deprecation/) |

## SG試験でのひっかけポイント

| 状況 | 判断 |
|---|---|
| 有効期限が近い | 更新・配備・切替後確認を計画する |
| 秘密鍵の漏えいが判明した | 期限内でも失効と鍵交換を進める |
| OCSPで失効していないと分かった | 名前、有効期間、信頼連鎖などの検証も必要 |
| 証明書ファイルだけバックアップした | 秘密鍵の保護・復旧計画まで済んだことにはならない |

CRLやOCSPは**失効状態**を確認する手段です。失効していないという結果だけで、証明書や接続先についてすべての検証が済んだことにはなりません。

## おすすめの学習順序

1. 公開鍵と主体の結び付きを知る → [電子証明書](/sg/digital-certificate/)
2. 発行者と信頼の起点を確認する → [認証局](/sg/certificate-authority-role/)、[証明書の連鎖](/sg/root-intermediate-certificate/)
3. 鍵が漏れた後の扱いを学ぶ → [失効確認](/sg/certificate-revocation-crl-ocsp/)
4. 鍵の保管と復旧へ進む → [TPM](/sg/tpm/)、[秘密分散法](/sg/secret-sharing/)

## 記事一覧

- 発行と運用全体：[電子証明書](/sg/digital-certificate/)、[PKI](/sg/pki/)
- 接続時の検証：[TLS](/sg/ssl-tls/)、[ルート証明書](/sg/root-certificate/)
- 事故・更新時の見直し：[CRLとOCSP](/sg/certificate-revocation-crl-ocsp/)、[暗号の危殆化](/sg/cryptographic-deprecation/)
- 暗号モジュールの要求事項を確認する：[FIPS 140-2](/sg/fips-140-2/)

## まとめ（試験直前用）

- 更新は期限管理、失効は期限前でも必要になる無効化の運用。
- 証明書と、対応する秘密鍵を分けて管理する。
- CRL・OCSPだけで名前・期限・信頼連鎖の検証を代替しない。
- 担当者、期限、事故時の手順、切替後の確認まで考える。

{% include sg_article_footer.html %}
