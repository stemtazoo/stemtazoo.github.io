---
layout: page
title: HTTPのBasic認証とDigest認証とは？Authorizationヘッダの違いを整理【SG試験】
description: "HTTPのBasic認証とDigest認証について、Authorizationヘッダで扱う認証情報、Base64とハッシュ値の違い、SG試験での判断軸を整理します。 選択肢で問われる目的・対象・責任範囲を押さえ、似た用語や対策との違いを判断できるようにします。"
permalink: /sg/http-basic-digest-auth/
tags: [sg, sg-technology, access_control, network, crypto_auth]
date: 2026-06-01
last_modified_at: 2026-06-01
---

## まず結論

HTTPの認証機能では、代表的に**Basic認証**と**Digest認証**を切り分けます。

SG試験で最も重要なのは、次の違いです。

| 認証方式 | クライアント側で送る情報の作り方 | 判断ポイント |
|---|---|---|
| Basic認証 | `利用者ID:パスワード` をBase64でエンコードしてAuthorizationヘッダに入れる | Base64は暗号化ではない |
| Digest認証 | 利用者ID、パスワード、サーバからのnonceなどを使ってハッシュ値を作りAuthorizationヘッダに入れる | パスワードそのものをそのまま送らない |

選択肢では、**「IDとパスワードをコロンで連結し、Base64でエンコード」ならBasic認証**です。

## このページで切り分けること（先にここだけ）

このページは、**Basic認証とDigest認証の違い**を中心に整理します。

- Basic認証：`ID:パスワード` をBase64でエンコードする
- Digest認証：nonceなどを使ってハッシュ値を送る
- Authorizationヘッダ：クライアントが認証情報を送るHTTPヘッダ

> 迷ったら、
> **「Base64か、ハッシュ値か」** を見ます。

## 直感的な説明

Basic認証は、IDとパスワードを書いた紙を、読める文字だけに変換して封筒に入れるようなものです。

Base64は、バイナリや記号をHTTPヘッダで扱いやすい文字列にするための**エンコード**です。暗号化ではありません。

そのため、Basic認証の認証情報は、通信経路を保護しないと盗聴されたときに復元されやすいです。

一方、Digest認証は、サーバから渡されたランダムな値（nonce）などを使って、パスワードそのものではなくハッシュ値を送る方式です。

SG試験では、深い計算式よりも、次の対応を覚えるのが有効です。

- Basic認証 → `ID:パスワード` + Base64
- Digest認証 → ID、パスワード、nonceなどからハッシュ値

## 定義・仕組み

HTTP認証では、クライアントはAuthorizationヘッダを使って認証情報を送ります。

Basic認証とDigest認証は、IETFのRFCで定義されています。Basic認証はRFC 7617、Digest認証はRFC 7616で確認できます。

- [RFC 7617：The 'Basic' HTTP Authentication Scheme](https://www.rfc-editor.org/rfc/rfc7617)
- [RFC 7616：HTTP Digest Access Authentication](https://www.rfc-editor.org/rfc/rfc7616)

### Basic認証

Basic認証では、利用者IDとパスワードを次の形でつなげます。

```text
利用者ID:パスワード
```

この文字列をBase64でエンコードし、Authorizationヘッダに指定します。

```text
Authorization: Basic Base64でエンコードした文字列
```

大切なのは、Base64が暗号化ではないことです。Base64でエンコードしても、元の文字列へ戻せます。

### Digest認証

Digest認証では、利用者ID、パスワード、サーバが提示するnonce、HTTPメソッド、URIなどを使ってハッシュ値を作り、Authorizationヘッダに指定します。

古い説明やSG試験の基本問題では、Digest認証のハッシュ関数としてMD5が取り上げられることがあります。

ただし、現在の仕様ではSHA-256なども扱われます。SG試験では、細かいアルゴリズム差よりも、**BasicはBase64、Digestはハッシュ値**と切り分けることが重要です。

## どんな場面で使う？

Basic認証は、簡易なアクセス制限で使われることがあります。

たとえば、次のような場面です。

- 管理画面の簡易保護
- 検証環境のアクセス制限
- Webサーバ設定による簡易認証

ただし、Basic認証は認証情報をBase64にしただけなので、HTTPのまま使うと盗聴に弱くなります。実務ではHTTPSと組み合わせることが重要です。

Digest認証は、パスワードそのものを送らない点でBasic認証より安全性を高める考え方です。

しかし、現在の実務では、HTTPS、フォーム認証、多要素認証、トークン認証などと組み合わせて認証・認可を設計する場面が多くあります。

関連する認証方式全体は、[認証方式とは？知識・所持・生体の違いを整理【SG試験】](/sg/authentication-methods/)や[トークン認証とは？SAML・OAuth・OIDCの前提を整理【SG試験】](/sg/token-authentication/)でも確認できます。

## よくある誤解・混同

### 誤解1：Base64は暗号化である

これは誤りです。

Base64は、データをHTTPヘッダなどで扱いやすい文字列に変換するエンコード方式です。

暗号化のように秘密鍵がないと戻せない仕組みではありません。

SG試験では、**Basic認証はBase64でエンコードするが、暗号化ではない**と押さえます。

### 誤解2：Digest認証はIDとパスワードをBase64にする

これはBasic認証の説明です。

Digest認証では、利用者ID、パスワード、nonceなどを使ってハッシュ値を作ります。

「Base64でエンコード」とあれば、まずBasic認証を疑います。

### 誤解3：Digest認証では必ずSHAだけを使う

SG試験の基本問題では、Digest認証をMD5のハッシュ値として説明することがあります。

一方、現在の仕様ではSHA-256なども扱われます。

試験では、MD5かSHAかだけで判断するより、**パスワードそのものではなくハッシュ値を送る方式か**を見ます。

### 誤解4：Authorizationヘッダはサーバが認証要求を送るヘッダである

Authorizationヘッダは、クライアントが認証情報を送るために使います。

サーバが認証方式や領域などを知らせるときは、WWW-Authenticateヘッダが使われます。

## SG試験で選択肢を切る判断軸（HTTP認証編）

- 「利用者IDとパスワードを `:` で連結し、Base64でエンコード」と書かれている
  → **Basic認証**です。

- 「利用者ID、パスワード、nonceなどからハッシュ値を作る」と書かれている
  → **Digest認証**です。

- 「Base64なので安全に暗号化される」と書かれている
  → 誤りです。Base64は暗号化ではありません。

- 「Authorizationヘッダで認証情報を送る」と書かれている
  → クライアント側の処理として自然です。

## 確認問題（SG試験対策）

WebサーバからBasic認証を求められたクライアントの処理として、最も適切なものはどれか。

- ア. 利用者IDとパスワードを `:` でつないだ文字列をBase64化し、Authorizationヘッダに入れて送る。
- イ. Base64化された認証情報は復号できないため、HTTPSを使わなくても盗聴対策は十分である。
- ウ. Authorizationヘッダはサーバが認証方式を通知するためだけに使い、クライアントは送信しない。
- エ. Digest認証では、サーバから渡されるnonceを使わず、パスワードを平文のまま送る。

<details markdown="1">
<summary>▶ クリックして答えと解説を見る（ここを開く）</summary>

**正解：ア**

### 解説

- ア：適切。Basic認証では、`ID:パスワード` に相当する文字列をBase64でエンコードし、Authorizationヘッダで送ります。
- イ：不適切。Base64は暗号化ではなく、元の文字列へ戻せます。通信路保護にはHTTPSを使います。
- ウ：不適切。Authorizationヘッダは、クライアントが認証情報を送るために使います。
- エ：不適切。Digest認証はnonceなどを使ってハッシュ値を送る方式で、パスワード平文送信ではありません。

👉 判断ポイント
**Basic認証＝Base64で表現した認証情報、Digest認証＝nonce等を使ったハッシュ値**で切り分けます。

</details>

## まとめ（試験直前用）

HTTP認証では、Basic認証とDigest認証の違いを押さえます。

- Basic認証：`ID:パスワード` をBase64でエンコードする
- Digest認証：ID、パスワード、nonceなどからハッシュ値を作る
- Authorizationヘッダはクライアントが認証情報を送るヘッダ
- Base64は暗号化ではない
- SG試験では、**Base64ならBasic、ハッシュ値ならDigest**と切り分ける

{% include sg_article_footer.html %}
