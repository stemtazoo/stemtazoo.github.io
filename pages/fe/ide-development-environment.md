---
layout: page
title: 統合開発環境（IDE）とは？Eclipse・GCC・Tomcat・Linuxの違い【基本情報技術者試験】
description: 統合開発環境（IDE）をEclipseを例に整理し、GCC（コンパイラ）、Apache Tomcat（Webアプリケーション実行環境）、Linux（OS）との役割の違いをFE試験の判断基準で解説します。
permalink: /fe/ide-development-environment/
tags: [fe, fe-technology, programming]
fe_section: テクノロジ系
fe_subsection: ソフトウェア
fe_order: 23
date: 2026-10-05
last_modified_at: 2026-10-05
---

## まず結論

統合開発環境（IDE：Integrated Development Environment）は、**プログラム開発に必要な機能を一つの環境にまとめたソフトウェア**です。

基本情報技術者試験では、製品名を丸暗記するより、**何をするソフトウェアか**で切り分けます。

| 用語 | 役割 | 試験での判断 |
|---|---|---|
| Eclipse | 統合開発環境（IDE） | **開発作業をまとめる** |
| GCC | コンパイラ群 | **ソースコードを翻訳する** |
| Apache Tomcat | Servletコンテナを備えたWebサーバ／Webコンテナ | **Java Webアプリを動かす** |
| Linux | OS | **コンピュータを管理する土台** |

> **IDE → Eclipse。コンパイラ → GCC。Java Web実行環境 → Tomcat。OS → Linux。**

## 直感的な説明

「プログラム開発に関係する」というだけでは、4つを区別できません。

役割を見ると整理できます。

<div class="fe-role-flow">
  <div><strong>Eclipse</strong><span>書く・管理する・デバッグする</span><b>IDE</b></div>
  <span class="fe-arrow">→</span>
  <div><strong>GCC</strong><span>ソースコードを翻訳する</span><b>コンパイラ群</b></div>
</div>
<div class="fe-role-base">
  <strong>Linux</strong>：これらのソフトウェアが動作できるOSの一つ
</div>

Tomcatはこの一直線上に無理に並べず、**JavaのWebアプリケーションをサーバ側で実行する環境**として別に考えると混乱しにくくなります。

## 定義・仕組み

### Eclipse：統合開発環境

IDEは、コードの編集、実行、デバッグ、プロジェクト管理など、開発で使う機能を一つの環境にまとめたものです。

Eclipseは代表的なIDEです。Java開発でよく知られていますが、プラグインなどによってさまざまな開発用途に利用できます。

試験では細かな機能より、

```text
統合開発環境
→ IDE
→ Eclipse
```

と結び付ければ十分です。

### GCC：コンパイラ群

GCC（GNU Compiler Collection）は、Cなど複数の言語に対応するコンパイラ群です。

ソースコードをコンピュータが実行できる形へ翻訳する役割を担います。

```text
ソースコード
    ↓
   GCC
    ↓
実行可能なコード
```

EclipseもGCCも開発に使えますが、**「開発環境」か「翻訳する道具」か**が違います。

### Apache Tomcat：Java Webアプリの実行環境

Apache Tomcatは、ServletやJSPなどのJava Web技術を実行するためのServletコンテナを備えています。

```text
ブラウザ
  ↓ HTTPリクエスト
Tomcat
  ↓
Servletなどを実行
  ↓
レスポンス
```

したがって、**統合開発環境ではありません**。

Servlet自体については、[Java Servletとは？Webサーバ側で動くJavaプログラム]({{ '/fe/java-servlet/' | relative_url }})で詳しく整理しています。

### Linux：OS

LinuxはOSです。

CPU、メモリ、ファイル、入出力装置などのコンピュータ資源を管理し、アプリケーションが動くための土台を提供します。

Eclipse、GCC、Tomcatのようなソフトウェアと、OSであるLinuxは**階層が違う**と考えると切り分けやすくなります。

## 科目Aでどう出る？

このタイプの問題では、選択肢がすべて「ITで聞いたことのある名前」になっていることがあります。

そこで、名前ではなく問題文の**役割を表す語**を先に探します。

```text
統合開発環境
→ Eclipse

コンパイル・翻訳
→ GCC

Servlet・JSP・Java Web
→ Tomcat

OS・基本ソフトウェア
→ Linux
```

特に注意したいのがEclipseとGCCです。

どちらもプログラム開発で使いますが、

> **開発作業をまとめる → IDE**
>
> **ソースコードを翻訳する → コンパイラ**

という違いがあります。

## どんな場面で使う？

たとえばJavaのWebアプリケーションを開発するとき、Eclipseでコードを書き、Tomcat上でServletを動かす、といった組合せがあります。

一方、CのプログラムならGCCでソースコードをコンパイルできます。これらをLinux上で利用することもできます。

重要なのは、**同じ開発作業に登場しても役割は別**という点です。

## よくある誤解・混同

### OSSならEclipseと判断する

これは危険です。

Eclipseだけでなく、GCC、Linux、Apache Tomcatもオープンソースのソフトウェアです。

問題文にOSSと書かれていても、それだけでは選べません。**「統合開発環境」という役割**を見ます。

### 開発に使うソフトウェアは全部IDE

違います。

GCCは開発で使いますが、IDEそのものではなくコンパイラ群です。

### TomcatはIDE

違います。

TomcatはJava Webアプリケーションを実行する側です。コードを編集・デバッグ・管理する機能をまとめたIDEとは役割が異なります。

### Linuxは開発環境だからIDE

Linux上に開発環境を構築することはできますが、Linux自体の分類はOSです。

## まとめ（試験直前用）

- **統合開発環境（IDE） → Eclipse**
- **コンパイラ → GCC**
- **Java Webアプリの実行環境 → Apache Tomcat**
- **OS → Linux**
- 「OSSかどうか」ではなく、**何をするソフトウェアか**で選択肢を切る

試験直前は、次の一行で整理します。

> **Eclipse＝作る環境、GCC＝翻訳、Tomcat＝Web実行、Linux＝土台。**

<style>
.fe-role-flow{display:flex;align-items:stretch;justify-content:center;gap:.7rem;flex-wrap:wrap;margin:1.2rem 0}
.fe-role-flow div{border:1px solid #c9d2d8;border-radius:10px;padding:.8rem 1rem;min-width:190px;text-align:center;background:#f7f9fa}
.fe-role-flow strong,.fe-role-flow span,.fe-role-flow b{display:block}
.fe-role-flow span{margin:.35rem 0;font-size:.92em}
.fe-role-flow b{font-size:.85em}
.fe-arrow{align-self:center;font-weight:bold}
.fe-role-base{max-width:500px;margin:.5rem auto 1.4rem;padding:.7rem 1rem;border-top:2px solid #aeb9bf;text-align:center}
@media(max-width:600px){.fe-role-flow{display:block}.fe-role-flow div{margin:.5rem 0}.fe-arrow{display:block;text-align:center;transform:rotate(90deg)}}
</style>

{% include fe_article_footer.html %}
