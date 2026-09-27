---
layout: page
title: Java Servletとは？Webサーバ側で動くJavaプログラム【基本情報技術者試験】
description: Java Servletを「クライアントからの要求を受けてWebサーバ側で実行されるJavaプログラム」として整理し、Javaアプレット・JavaScript・VBScript・JavaBeans・JVMとの違いを科目Aで選択肢を切れる形で解説します。
permalink: /fe/java-servlet/
tags: [fe, fe-technology, programming, java, web]
fe_section: テクノロジ系
fe_subsection: ソフトウェア
fe_order: 22
date: 2026-09-01
last_modified_at: 2026-09-28
---

## まず結論

Java Servlet（サーブレット）は、**クライアントからの要求を受けて、Webサーバ側で実行されるJavaプログラム**です。

基本情報技術者試験では、まず次の一言で判断します。

> **Servlet → Server側で実行**

ブラウザから要求を受け取り、サーバ側で処理した結果をHTMLなどとして返します。

## 直感的な説明

Webページで「検索」ボタンを押した場面を考えます。

```text
ブラウザ
  ↓ リクエスト
Webサーバ
  ↓
Servletが処理
  ↓
データベース検索など
  ↓
結果を生成
  ↓ レスポンス
ブラウザに表示
```

重要なのは、**Servletそのものは利用者のPC上ではなく、サーバ側で動く**ことです。

たとえば、利用者が検索条件を入力して送信すると、Servletがその要求を受け取り、必要な処理を行って結果を返します。

## 定義・仕組み

Java Servletは、JavaでWebアプリケーションのサーバ側処理を実装するための仕組みです。

代表的な役割は次のとおりです。

- ブラウザからのHTTPリクエストを受け取る
- 入力されたデータを取得する
- 必要な業務処理を呼び出す
- データベースなどと連携する
- HTMLなどのレスポンスを返す

処理の流れを整理すると、次のようになります。

```text
クライアントから要求
        ↓
Servletが受け取る
        ↓
サーバ側で処理
        ↓
結果をクライアントへ返す
```

Servletは通常、Webサーバやアプリケーションサーバ上のServletコンテナによって実行されます。

### Servletはどこで動く？

ここが試験で最重要です。

```text
Java Servlet
→ サーバ側

Javaアプレット
→ クライアント側
```

名前やJavaという共通点だけで判断せず、**実行される場所**を見るのがポイントです。

## 科目Aでどう出る？

科目Aでは、Java関連の用語やWeb技術を説明文から見分ける問題が出やすいです。

### 判断ワード

Servletを示す代表的な表現です。

- Webサーバ側で実行
- クライアントからの要求を処理
- 動的なWebページを生成
- Javaで記述
- サーバサイド

特に、古い過去問で

> **Webサーバ上だけで動作する**

のように実行場所を限定している場合は、Servletを強く疑います。

### 選択肢の切り分け

| 用語 | 判断基準 |
|---|---|
| Java Servlet | Webサーバ側で動くJavaプログラム |
| Javaアプレット | クライアント側で動く旧来のJavaプログラム |
| JavaScript | Webページの処理に使われるスクリプト言語。現在はサーバ側でも実行できる |
| VBScript | 旧来、クライアント側・サーバ側の両方で利用されたスクリプト言語 |
| JavaBeans | Javaの機能を部品化して再利用する仕組み |
| JVM | Javaバイトコードを実行する仮想マシン |

試験中は次の対応で切り分けます。

```text
Webサーバ側で動くJavaプログラム
→ Servlet

クライアント側で動く旧来のJavaプログラム
→ Applet

Webページのスクリプト
→ JavaScript

旧来のMicrosoft系スクリプト
→ VBScript

再利用できる部品
→ JavaBeans

バイトコードを実行
→ JVM
```

JavaBeansについては、[JavaBeansとは？再利用可能なJava部品の仕組み]({{ '/fe/java-beans/' | relative_url }})もあわせて確認すると整理しやすくなります。

### JavaScriptとの違いに注意

過去問では、JavaScriptを**ブラウザ側で動く技術**としてServletと対比することがあります。

ただし現在のJavaScriptは、Node.jsなどを使ってサーバ側でも実行できます。

そのため、現在の技術としては

```text
JavaScript
→ ブラウザ側だけとは限らない

Servlet
→ Javaで作るサーバ側Webプログラム
```

と理解しておくのが安全です。

試験では、**問題が作られた時代の技術背景**と、現在の技術事情を分けて考えます。

## どんな場面で使う？

Servletは、Webアプリケーションで利用者から受け取った要求を処理する場面で使われます。

たとえば次のような処理です。

- ログイン処理
- 商品検索
- 会員情報の登録
- 注文処理
- 入力フォームの内容確認

```text
商品検索ボタンを押す
        ↓
Servletが検索条件を受け取る
        ↓
データを検索する
        ↓
結果をブラウザへ返す
```

FEでは具体的な実装方法よりも、**「サーバ側で処理するJavaプログラム」**という役割を押さえることが重要です。

## よくある誤解・混同

### Servletはブラウザにダウンロードして実行する

違います。

ブラウザ側で動くJavaプログラムとして出てくるのは、旧来のJavaアプレットです。

Servletは**サーバ側で実行**されます。

### JavaScriptは必ずブラウザ側で動く

現在はそうとは限りません。

JavaScriptはブラウザで広く使われますが、Node.jsなどを利用してサーバ側で実行することもできます。

ただし、過去のFE問題ではJavaScriptをブラウザ側、Servletをサーバ側として対比している場合があります。

### VBScriptならWebサーバ上だけで動く

違います。

VBScriptは、旧来のInternet Explorerでクライアント側スクリプトとして使われたほか、ASPなどでサーバ側処理にも使われました。

したがって、**「Webサーバ上だけ」**という説明からVBScriptを選ぶのは適切ではありません。

### ServletはJavaBeansと同じ

違います。

JavaBeansは、Javaの機能を再利用しやすい部品として扱うための仕組みです。

Servletは、**Webサーバ側で要求を処理するプログラム**です。

### ServletはJavaを実行する仮想マシン

違います。

Javaバイトコードを実行するのはJVM（Java Virtual Machine）です。

ServletはJVM上で実行されるJavaプログラムの一種です。

### 動的Webページなら何でもServlet

そうとは限りません。

動的なWebページを作る技術はServlet以外にもあります。

FEでは、説明文に**「Java」「サーバ側」「クライアントの要求を処理」**がそろっているかを見るのが安全です。

## まとめ（試験直前用）

- Java ServletはWebサーバ側で動くJavaプログラム
- クライアントからの要求を受け取り、処理結果を返す
- **「Webサーバ上だけ」**はServletを疑う強い判断ワード
- Javaアプレットはクライアント側で動く旧来の技術
- JavaScriptは現在ではブラウザ側だけとは限らない
- VBScriptは旧来、クライアント側・サーバ側の両方で使われた
- JavaBeansは再利用できるJava部品
- JVMはJavaバイトコードを実行する仕組み

試験直前は、次の一文で整理します。

> **Servlet runs on the server.**

参考： [IPA：試験要綱・シラバスについて](https://www.ipa.go.jp/shiken/syllabus/index.html)

{% include fe_article_footer.html %}
