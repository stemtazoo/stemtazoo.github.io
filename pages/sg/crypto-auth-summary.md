---
layout: page
title: 暗号・認証まとめ｜主要用語を整理【SG試験】
description: 暗号・認証は、機密性・完全性・真正性をどう実現するかを見分ける分野です。SG試験で頻出の用語の違い、選択肢を切る判断基準、学習順序を一つに整理します。
permalink: /sg/crypto-auth-summary/
tags: [sg, sg-security-measures, crypto_auth]
last_modified_at: 2026-06-12
---

## まず結論

- このシリーズでは、**「何を守る技術か」**で暗号・認証用語を切り分けられるようになることを目標にします。
- SG試験では、暗号（秘密にする）、ハッシュ（改ざん検知）、署名（送信者証明）を混同しないことが得点の鍵です。
- 丸暗記ではなく、**復号の要否・鍵の使い方・確認したい性質（機密性/完全性/真正性）**の3観点で判断します。

## 全体像

暗号・認証分野は、次の3階層で整理すると理解しやすくなります。

1. **基礎技術層**：共通鍵暗号・公開鍵暗号・ハッシュ
2. **適用技術層**：デジタル署名・MAC・電子証明書・TLS
3. **運用層**：多要素認証、失効管理（CRL/OCSP）、鍵管理

試験では「この場面で欲しいのは何か」を先に決めると、選択肢を切りやすくなります。

- 通信内容を読まれたくない → 暗号
- 改ざん有無を確認したい → ハッシュ/MAC/署名
- 本人性を確認したい → 認証方式・証明書

## 主要用語の整理

| 用語 | 判断基準 |
|---|---|
| [共通鍵暗号方式](/sg/symmetric-key-cryptography/) | 同じ鍵で暗号化・復号する方式。高速だが鍵配送が課題。 |
| [公開鍵暗号方式](/sg/public-key-cryptography/) | 公開鍵と秘密鍵を使い分ける方式。鍵配送問題を緩和。 |
| [ハイブリッド暗号方式](/sg/hybrid-cryptography/) | 通信本体は共通鍵、鍵配送は公開鍵で行う実運用型。 |
| [ハッシュ関数](/sg/hash-function/) | 復号しない要約値で整合性を確認。改ざん検知に使う。 |
| [メッセージ認証コード（MAC）](/sg/message-authentication-code/) | 共通鍵を使って改ざん・なりすましを検知。送信者共有鍵前提。 |
| [デジタル署名](/sg/digital-signature/) | 秘密鍵で署名し、公開鍵で検証。真正性・否認防止に強い。 |
| [電子証明書](/sg/digital-certificate/) | 公開鍵が誰のものかを第三者（認証局）が証明する。 |
| [SSL/TLS](/sg/ssl-tls/) | 通信路の暗号化とサーバ認証を提供するプロトコル。 |
| [多要素認証](/sg/multi-factor-authentication/) | 知識・所持・生体の異なる要素を組み合わせる認証強化。 |
| [秘密分散法](/sg/secret-sharing/) | 秘密鍵を分散片に分け、一定数以上で復元できるようにする。 |
| [CRL](/sg/crl/) | 失効した証明書一覧。証明書がまだ有効かを確認する観点。 |

## SG試験でのひっかけポイント

| 迷いやすい組合せ | 切り分けのポイント |
|---|---|
| 共通鍵暗号 vs 公開鍵暗号 | 「同じ鍵か、鍵ペアか」「速度重視か、鍵配送容易性重視か」で判断。 |
| ハッシュ vs 暗号化 | ハッシュは復号しない。暗号化は元データに戻す前提。 |
| MAC vs デジタル署名 | MACは共有鍵、署名は秘密鍵/公開鍵。否認防止は署名。 |
| デジタル署名 vs 電子証明書 | 署名は改ざん・真正性確認の仕組み、証明書は公開鍵の身元証明。 |
| SSL/TLS vs IPsec | TLSは主にアプリ層通信、IPsecはIP層で保護。適用層で判断。 |
| 多要素認証 vs 多段階認証 | 要素の種類が増えるのがMFA。段階が増えるだけではMFAとは限らない。 |
| 秘密分散法 vs 秘密鍵一覧表 | 分散片で復元条件を満たす仕組みか、漏えい時の影響が大きい一覧管理か。 |

## おすすめの学習順序

1. [共通鍵暗号方式](/sg/symmetric-key-cryptography/)
2. [公開鍵暗号方式](/sg/public-key-cryptography/)
3. [ハイブリッド暗号方式](/sg/hybrid-cryptography/)
4. [ハッシュ関数](/sg/hash-function/)
5. [メッセージ認証コード（MAC）](/sg/message-authentication-code/)
6. [デジタル署名](/sg/digital-signature/)
7. [電子証明書](/sg/digital-certificate/)
8. [SSL/TLS](/sg/ssl-tls/)
9. [多要素認証](/sg/multi-factor-authentication/)
10. [秘密分散法](/sg/secret-sharing/)
11. [CRL](/sg/crl/)

## 記事一覧

### 暗号アルゴリズムの基礎

- [共通鍵暗号方式とは？公開鍵暗号方式との違いを整理【SG試験】](/sg/symmetric-key-cryptography/)
- [公開鍵暗号方式とは？共通鍵暗号方式との違いを整理【SG試験】](/sg/public-key-cryptography/)
- [ハイブリッド暗号方式とは？公開鍵と共通鍵を組み合わせる理由【SG試験】](/sg/hybrid-cryptography/)
- [AESとは？鍵長とラウンド数も押さえる共通鍵暗号【SG試験】](/sg/aes/)

### 完全性・真正性の確認

- [ハッシュ関数とは？改ざん検知の基本をやさしく整理【SG試験】](/sg/hash-function/)
- [メッセージ認証コード（MAC）とは？改ざん検知の仕組み【SG試験】](/sg/message-authentication-code/)
- [デジタル署名とは？改ざん検知となりすまし防止の仕組み【SG試験】](/sg/digital-signature/)

### 証明書と通信路保護

- [デジタル証明書とは？公開鍵を証明する仕組みを整理【SG試験】](/sg/digital-certificate/)
- [ルート証明書とは？信頼の起点をやさしく解説【SG試験】](/sg/root-certificate/)
- [ルート証明書と中間証明書の違い【SG試験】](/sg/root-intermediate-certificate/)
- [CRLとは？失効証明書リストの役割【SG試験】](/sg/crl/)
- [証明書失効とは？CRLとOCSPの違いを整理【SG試験】](/sg/certificate-revocation-crl-ocsp/)
- [SSL/TLSとは？通信を守る暗号化の仕組み【SG試験】](/sg/ssl-tls/)
- [秘密分散法とは？秘密鍵を分割して保管する仕組み【SG試験】](/sg/secret-sharing/)

### 認証強化

- [認証方式とは？3要素と多要素認証を整理【SG試験】](/sg/authentication-methods/)
- [多要素認証（MFA）とは？認証強化の仕組みと判断ポイント【SG試験】](/sg/multi-factor-authentication/)
- [多要素認証と多段階認証の違いとは？混同しやすい認証方式を整理【SG試験】](/sg/mfa-vs-step-auth/)
- [チャレンジレスポンス認証とは？パスワードを送らない認証の仕組み【SG試験】](/sg/challenge-response-authentication/)

## まとめ（試験直前用）

- 暗号は「秘密にする」、ハッシュは「改ざんを見抜く」、署名は「誰が送ったかを証明する」。
- 共有鍵か公開鍵基盤かで、MACとデジタル署名を切り分ける。
- 証明書は暗号そのものではなく、公開鍵の身元を保証する仕組み。
- 秘密分散法は、秘密鍵を分割して保管し、一定数以上で復元できるようにする仕組み。
- 問題文で求められる性質（機密性・完全性・真正性）を先に確定すると、誤答を削りやすい。

{% include sg_article_footer.html %}
