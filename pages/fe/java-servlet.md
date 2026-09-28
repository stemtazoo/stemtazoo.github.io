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
last_modified_at: 2026-09-29
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

Java Servletは、JavaでWebアプリケーションのサーバ側処理を実装するためのAPIです。ServletコンテナがHTTPリクエストをServletに渡し、Servletが処理結果をレスポンスとして返します。現在のJakarta Servlet仕様も、HTTPリクエストとレスポンスを扱うサーバ側APIとして定義しています。

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
Servletコンテナが要求をServletへ渡す
        ↓
Servletがサーバ側で処理
        ↓
結果をクライアントへ返す
```

Servletは通常、Webサーバやアプリケーションサーバに組み込まれたServletコンテナによって実行されます。

### Servletはどこで動く？

ここが試験で最重要です。

```text
Java Servlet
→ サーバ側（Servletコンテナ上）

Javaアプレット
→ クライアント側（旧来の技術）
```

名前やJavaという共通点だけで判断せず、**実行される場所と役割**を見るのがポイントです。

## 科目Aでどう出る？

科目Aでは、Java関連の用語やWeb技術を説明文から見分ける問題が出やすいです。

### 判断ワード

Servletを示す代表的な表現です。

- Webサーバ側で実行
- クライアントからの要求を処理
- 動的なWebページを生成
- Javaで記述
- サーバサイド

過去問には、次のように「Webサーバ上だけで動作するもの」を問う設問があります。

> **Web環境での動的処理を実現するプログラムであって、Webサーバ上だけで動作するものはどれか。**

こうした**過去問の選択肢の中では**、Servletを選ぶ手掛かりになります。ただし、この文言だけを現代のWeb技術全般に通用する判定基準として覚えるのではなく、選択肢と問題の時代背景を含めて判断します。実際にJavaScriptはNode.jsなどで、VBScriptも旧来のClassic ASPでサーバ側実行が可能でした。

### 選択肢の切り分け

| 用語 | 判断基準 |
|---|---|
| Java Servlet | JavaでWebアプリケーションのサーバ側処理を実装するAPI。Servletコンテナ上で実行 |
| Javaアプレット | クライアント側で動く旧来のJavaプログラム |
| JavaScript | ブラウザで広く使われる。Node.jsなどの実行環境ではサーバ側でも動く |
| VBScript | 旧来、Internet Explorerのクライアント側スクリプトやClassic ASPのサーバ側スクリプトで使われた |
| JavaBeans | Javaの機能を部品化して再利用する仕組み |
| JVM | Javaバイトコードを実行する仮想マシン |

試験中は、説明文に出てくる**言語・役割・実行場所**を組み合わせて切り分けます。

```text
JavaでWeb要求をサーバ側処理
→ Servlet

旧来のJavaプログラムをブラウザ側で実行
→ Applet

ブラウザ上でページに動きを加えるスクリプト（代表的な使い方）
→ JavaScript
  ※Node.jsなどを使えばサーバ側でも実行できる

旧来のMicrosoft系スクリプト
→ VBScript
  ※クライアント側・Classic ASPのサーバ側の両方で使われた

再利用できるJava部品
→ JavaBeans

Javaバイトコードを実行
→ JVM
```

JavaBeansについては、[JavaBeansとは？再利用可能なJava部品の仕組み]({{ '/fe/java-beans/' | relative_url }})もあわせて確認すると整理しやすくなります。

### JavaScriptとの違いに注意

過去問では、JavaScriptを**ブラウザ側で動く技術**としてServletと対比することがあります。

JavaScriptはブラウザで広く使われますが、実行場所は言語だけでは決まりません。Node.jsのようなJavaScript実行環境をサーバ側に置けば、JavaScriptを使ったサーバ処理もできます。

```text
JavaScript
→ ブラウザでも、Node.jsなどの環境でも実行できる

Servlet
→ JavaでWebアプリケーションのサーバ側処理を実装するAPI
```

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

FEでは具体的な実装方法よりも、**「JavaでWeb要求をサーバ側処理する」**という役割を押さえることが重要です。

## よくある誤解・混同

### Servletはブラウザにダウンロードして実行する

違います。

ブラウザ側で動くJavaプログラムとして出てくるのは、旧来のJavaアプレットです。

Servletは**Servletコンテナ上でサーバ側実行**されます。

### JavaScriptは必ずブラウザ側で動く

現在はそうとは限りません。

JavaScriptはブラウザで広く使われますが、Node.jsなどの実行環境を使ってサーバ側で実行することもできます。

ただし、過去のFE問題ではJavaScriptをブラウザ側、Servletをサーバ側として対比している場合があります。

### VBScriptはサーバ側だけで動く、またはクライアント側だけで動く

どちらも正確ではありません。

旧来、VBScriptはInternet Explorerのクライアント側スクリプトとして使われたほか、Classic ASPではサーバ側スクリプトとしても使われました。どこで動くかは、そのスクリプトを実行する環境によります。

したがって、**「Webサーバ上だけ」**という表現は、VBScriptがサーバ側で動かなかったという意味ではありません。過去問では、提示された選択肢の中で、クライアント側でも使われた技術とServletを区別する材料として読まれています。

### ServletはJavaBeansと同じ

違います。

JavaBeansは、Javaの機能を再利用しやすい部品として扱うための仕組みです。

Servletは、**Webサーバ側で要求を処理するためのAPIと、そのAPIを使ったプログラム**です。

### ServletはJavaを実行する仮想マシン

違います。

Javaバイトコードを実行するのはJVM（Java Virtual Machine）です。

ServletはJVM上で動作するJavaプログラムであり、ServletのライフサイクルやHTTP処理はServletコンテナが扱います。

### 動的Webページなら何でもServlet

そうとは限りません。

動的なWebページを作る技術はServlet以外にもあります。

FEでは、説明文に**「Java」「サーバ側」「クライアントの要求を処理」**がそろっているかを見るのが安全です。

## まとめ（試験直前用）

- Java ServletはJavaでWebアプリケーションのサーバ側処理を実装するAPI
- Servletコンテナ上でHTTPリクエストを処理し、レスポンスを返す
- 過去問の**「Webサーバ上だけ」**は、その設問の選択肢内でServletを選ぶ手掛かりになる
- この表現だけで現代の技術全般を分類しない。JavaScriptやVBScriptもサーバ側で実行できる
- Javaアプレットはクライアント側で動く旧来の技術
- JavaScriptはブラウザのほか、Node.jsなどの環境でも実行できる
- VBScriptは旧来、クライアント側・Classic ASPのサーバ側の両方で使われた
- JavaBeansは再利用できるJava部品、JVMはJavaバイトコードを実行する仮想マシン

試験直前は、次の一文で整理します。

> **Servlet runs on the server.**

### 参考資料

- [Jakarta Servlet 6.1：サーバ側HTTPリクエスト・レスポンスAPI](https://jakarta.ee/specifications/servlet/6.1/)
- [Node.js公式サイト：JavaScriptランタイム](https://nodejs.org/en/download/current)
- [Microsoft Learn：VBScriptとクライアント側アプリケーション](https://learn.microsoft.com/en-us/windows/win32/com/translating-to-vbscript)
- [Microsoft Learn：ASP Overview（VBScriptとサーバ側スクリプト）](https://learn.microsoft.com/en-us/previous-versions/iis/6.0-sdk/ms524929(v=vs.90))
- [IPA掲載：基本情報技術者試験問題（Webサーバ上だけで動作するプログラムの設問例）](https://www.ipa.go.jp/shiken/about/ug65p90000001bq0-att/tokurei_Mondai_20180610_FE.pdf)
- [IPA：試験要綱・シラバスについて](https://www.ipa.go.jp/shiken/syllabus/index.html)

{% include fe_article_footer.html %}
