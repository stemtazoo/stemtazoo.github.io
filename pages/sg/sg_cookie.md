---
layout: page
title: Cookieとは？HTTPヘッダで扱う状態管理の基本
description: Cookieの保存場所・送信方法・属性（Secure/HttpOnly/SameSite）を、HTTPSとの違いとあわせて整理し、SG試験で誤答選択肢を切る判断軸を解説します。
permalink: /sg/cookie/
tags: [sg, sg-technology, web, network, authentication]
date: 2026-05-13
last_modified_at: 2026-05-29
---

# Cookieとは？HTTPヘッダで扱う状態管理の基本

Cookieは、Webサイトがブラウザに小さな情報を保存させ、次回以降の通信でその情報を送り返してもらう仕組みです。

SG試験では、

- Cookieはどこに保存されるのか
- どのHTTPヘッダで送られるのか
- Secure、HttpOnly、SameSiteは何を守るのか
- Cookie自体が暗号化するのか

を切り分けられることが大切です。

---

## まず結論

Cookieは、**HTTPのような状態を持たない通信で、ログイン状態などを維持するための仕組み**です。

重要なのは、次の2つのHTTPヘッダです。

| ヘッダ | 向き | 役割 |
|---|---|---|
| `Set-Cookie` | サーバ → ブラウザ | Cookieをブラウザに保存させる |
| `Cookie` | ブラウザ → サーバ | 保存済みCookieをサーバへ送る |

つまり、Cookieは

> サーバがブラウザに保存させ、ブラウザが次回以降のリクエストで送り返す情報

と考えると分かりやすいです。

ただし、ここで注意したいのは、**Cookieそのものが通信を暗号化するわけではない**という点です。

通信内容を暗号化するのは、Cookieではなく **HTTPS** です。

---

## 直感的な説明

Webページを見るとき、HTTP通信は基本的に「1回ごとのやり取り」です。

たとえば、店員さんに毎回はじめて会うようなイメージです。

- 1回目：ログインする
- 2回目：マイページを見る
- 3回目：購入履歴を見る

このとき、何も目印がなければ、サーバは

> この人はさっきログインした人かな？

と判断できません。

そこで使われるのがCookieです。

Cookieは、ブラウザに保存される「会員証」や「整理券」のようなものです。

サーバはブラウザに対して、

> 次からこの情報を持ってきてね

という形でCookieを渡します。

その後、ブラウザは同じサイトへアクセスするときにCookieを添えて送ります。

この仕組みによって、ログイン状態やカートの情報などを維持できます。

---

## 定義・仕組み

Cookieは、HTTPヘッダを使ってやり取りされます。

### Set-Cookie：サーバからブラウザへ送る

`Set-Cookie` は、サーバがブラウザにCookieを保存させるためのレスポンスヘッダです。

例：

```http
Set-Cookie: session_id=abc123; Secure; HttpOnly; SameSite=Lax
```

この例では、サーバがブラウザに対して、`session_id=abc123` というCookieを保存させています。

あわせて、`Secure`、`HttpOnly`、`SameSite` などの属性を指定しています。

### Cookie：ブラウザからサーバへ送る

`Cookie` は、ブラウザが保存済みCookieをサーバへ送るためのリクエストヘッダです。

例：

```http
Cookie: session_id=abc123
```

ブラウザは、対象のドメインやパスなどの条件に合うCookieを、自動的にリクエストへ付けて送ります。

SG試験では、

- `Set-Cookie` はサーバからブラウザ
- `Cookie` はブラウザからサーバ

という向きをまず押さえると、選択肢を切りやすくなります。

---

## Cookieの主な属性

Cookieには、有効期限や送信条件を制御する属性があります。

### 有効期限：Expires / Max-Age

Cookieには、有効期限を設定できます。

代表的な属性は次の2つです。

| 属性 | 意味 |
|---|---|
| `Expires` | いつまで有効かを日時で指定する |
| `Max-Age` | 何秒間有効かを秒数で指定する |

有効期限がないCookieは、一般にブラウザを閉じるまでのセッションCookieとして扱われます。

有効期限があるCookieは、ブラウザを閉じても残ることがあります。

### Secure

`Secure` は、Cookieを **HTTPS通信のときだけ送信する** ための属性です。

ここで大事なのは、

> SecureはCookieを暗号化する属性ではない

という点です。

Secureは、Cookieの送信先をHTTPSに限定する属性です。
通信を暗号化するのはHTTPSです。

### HttpOnly

`HttpOnly` は、JavaScriptからCookieを読み取れないようにする属性です。

これにより、XSS攻撃などで悪意あるスクリプトがCookieを盗むリスクを下げられます。

ただし、HttpOnlyを付けても、ブラウザはHTTPリクエストにはCookieを送信します。

つまり、HttpOnlyは

> JavaScriptから読ませないための設定

です。

通信を暗号化する設定ではありません。

### SameSite

`SameSite` は、別サイトからのリクエストにCookieを送るかどうかを制御する属性です。

CSRF対策と関係します。

代表的には、次のように考えます。

| 値 | イメージ |
|---|---|
| `Strict` | 同じサイトからのリクエストだけにかなり厳しく制限する |
| `Lax` | 通常のページ遷移などでは送るが、危険な送信を抑える |
| `None` | 別サイトからのリクエストにも送る。通常はSecureも必要 |

SG試験では、SameSiteは

> Cookieを別サイトからのリクエストに送るかどうかを制御する属性

と覚えるとよいです。

---

## どんな場面で使う？

Cookieは、Webサービスでよく使われます。

代表例は次のとおりです。

| 場面 | Cookieの使われ方 |
|---|---|
| ログイン状態の維持 | セッションIDなどを保存する |
| ショッピングカート | カート情報や識別情報を保持する |
| 表示設定 | 言語設定やテーマ設定を保存する |
| アクセス解析 | 利用者の再訪問などを識別する |

特にSG試験では、ログイン状態の維持やセッション管理と関連して出題されやすいです。

ただし、Cookieにパスワードそのものを保存するような設計は危険です。

一般的には、CookieにはセッションIDなどを保存し、実際のログイン情報や権限情報はサーバ側で管理します。

---

## よくある誤解・混同

### 誤解1：Cookieは通信を暗号化する

これは誤りです。

Cookieは、状態を管理するための仕組みです。
通信を暗号化する仕組みではありません。

通信内容を暗号化するのはHTTPSです。

| 項目 | 役割 |
|---|---|
| Cookie | 状態管理 |
| HTTPS | 通信の暗号化 |
| Secure属性 | HTTPSのときだけCookieを送る |

試験では、

> Cookieによって通信内容を暗号化する

という選択肢は切る候補になります。

### 誤解2：Secureを付けるとCookieの中身が暗号化される

これも誤りです。

`Secure` は、CookieをHTTPS通信時にだけ送信するための属性です。

Cookieの値そのものを暗号化する機能ではありません。

Cookieの中身を安全に扱うには、

- HTTPSで通信する
- 不要な情報をCookieに入れない
- 必要に応じてサーバ側で署名や暗号化を行う

といった設計が必要です。

### 誤解3：HttpOnlyを付けるとCookieは送信されない

これも誤りです。

`HttpOnly` は、JavaScriptからCookieを読めないようにする属性です。

ブラウザは、条件に合えばHTTPリクエストにはCookieを送信します。

| 属性 | 何を制御するか |
|---|---|
| Secure | HTTPSのときだけ送信 |
| HttpOnly | JavaScriptからの読み取りを制限 |
| SameSite | 別サイトからのリクエスト時の送信を制限 |

### 誤解4：Cookieは必ずサーバに保存される

Cookieは、基本的にブラウザ側に保存されます。

ただし、Cookieに入っているセッションIDに対応するログイン状態や権限情報は、サーバ側で管理されることが多いです。

試験では、

- Cookie自体の保存場所：ブラウザ側
- セッション情報の実体：サーバ側で管理されることが多い

という切り分けが大切です。

---

## 保存場所・暗号化主体・設定主体の切り分け

Cookieの問題では、次の3つを分けると考えやすいです。

| 観点 | 答え |
|---|---|
| Cookieを保存する場所 | ブラウザ側 |
| Cookieを設定する主体 | 主にサーバ側。`Set-Cookie`で指示する |
| Cookieを送り返す主体 | ブラウザ側。`Cookie`ヘッダで送る |
| 通信を暗号化する主体 | HTTPS |
| Cookie送信をHTTPSに限定する属性 | Secure |
| JavaScriptからの読み取りを防ぐ属性 | HttpOnly |
| 別サイト経由の送信を制御する属性 | SameSite |

特に、

> 暗号化はCookie機能ではなくHTTPS

という点は、試験でひっかけになりやすいです。

---

## 確認問題（SG試験対策）

Cookieに関する説明として、適切なものはどれか。

- 1. Cookieは、通信内容を暗号化するためのHTTPの仕組みである。
- 2. `Set-Cookie` は、ブラウザがサーバへCookieを送信するためのリクエストヘッダである。
- 3. `HttpOnly` 属性を付けると、JavaScriptからCookieを読み取りにくくできる。
- 4. `Secure` 属性を付けると、Cookieの値そのものが暗号化される。

<details markdown="1">
<summary>▶ クリックして答えと解説を見る（ここを開く）</summary>

**正解：3**

### 解説

- 1：誤りです。Cookieは状態管理の仕組みであり、通信を暗号化する仕組みではありません。通信を暗号化するのはHTTPSです。
- 2：誤りです。`Set-Cookie` は、サーバがブラウザにCookieを保存させるためのレスポンスヘッダです。ブラウザがサーバへ送るときは `Cookie` ヘッダを使います。
- 3：適切です。`HttpOnly` は、JavaScriptからCookieを読み取れないようにする属性です。XSSによるCookie窃取リスクを下げる目的で使われます。
- 4：誤りです。`Secure` は、CookieをHTTPS通信時にだけ送信する属性です。Cookieの値そのものを暗号化する機能ではありません。

判断ポイント：Cookieは状態管理の仕組みです。暗号化、送信方向、JavaScriptからの読み取り制限を分けて判断します。

</details>

---

## まとめ（試験直前用）

Cookieは、HTTPで状態管理を行うための仕組みです。

試験直前は、次の3点で切り分けましょう。

- `Set-Cookie` は **サーバ → ブラウザ**、`Cookie` は **ブラウザ → サーバ**
- `Secure` は **HTTPS時だけ送信**、暗号化そのものではない
- `HttpOnly` は **JavaScriptから読ませない**、`SameSite` は **別サイト経由の送信制御**

Cookieの問題では、

> 状態管理なのか、暗号化なのか、アクセス制限なのか

を分けて考えると、誤答選択肢を切りやすくなります。

---

## 参考リンク

- [RFC 6265: HTTP State Management Mechanism](https://www.rfc-editor.org/rfc/rfc6265)
- [Cookies: HTTP State Management Mechanism（rfc6265bis draft）](https://datatracker.ietf.org/doc/draft-ietf-httpbis-rfc6265bis/)
- [HTTP Cookie の使用 - MDN Web Docs](https://developer.mozilla.org/ja/docs/Web/HTTP/Guides/Cookies)

{% include sg_article_footer.html %}
