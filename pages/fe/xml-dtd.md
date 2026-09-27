---
layout: page
title: DTDとは？XML宣言・XML Schemaとの違い【基本情報技術者試験】
description: DTDを「XML文書で使える要素・属性・並び方などの文書型を定義する仕組み」として整理し、XML宣言・XML本文・XML Schemaとの違いをFE科目A向けに解説します。
permalink: /fe/xml-dtd/
tags: [fe, fe-technology, network, xml, dtd]
fe_section: テクノロジ系
fe_subsection: ネットワーク
fe_order: 57
date: 2026-09-27
last_modified_at: 2026-09-27
---

## まず結論

**DTD（Document Type Definition）は、XML文書で使える要素・属性・要素の並び方など、文書の構造を定義する仕組み**です。

基本情報技術者試験では、まず次の3つを切り分けます。

~~~text
version・encoding
→ XML宣言

実際のデータ
→ XML本文

要素・属性・並び方のルール
→ DTD
~~~

例えば、

~~~xml
<?xml version="1.0" encoding="UTF-8"?>
~~~

はXML宣言です。

一方、DTDは、

~~~text
book の中には
title と price を置く

title は文字データをもつ
price は文字データをもつ
~~~

のような、**XML文書の設計ルール**を定義します。

> **DTD → Document Type Definition → 文書型の定義**

と結び付けておくと、試験で判断しやすくなります。

## 直感的な説明

XML文書を「入力フォーム」に例えると分かりやすいです。

実際のXMLが、

~~~xml
<book>
  <title>Python入門</title>
  <price>2000</price>
</book>
~~~

だとします。

これは、実際に入力されたデータです。

一方、DTDは、

~~~text
book の中には
title
price
の順で置く
~~~

といった**フォームのルール**を決めます。

イメージすると、

~~~text
DTD
↓
書いてよい構造を決める

XML文書
↓
実際のデータを書く
~~~

という関係です。

つまり、

> **DTDはデータそのものではなく、データをどういう構造で書くかを決める**

ものです。

## 定義・仕組み

### XML宣言

XML宣言は、XML文書の先頭付近に書き、XMLのバージョンや文字エンコーディングなどを指定します。

~~~xml
<?xml version="1.0" encoding="UTF-8"?>
~~~

ここでは、

~~~text
version="1.0"
→ XMLのバージョン

encoding="UTF-8"
→ 文字エンコーディング
~~~

を表します。

試験では、

> **バージョン・文字コード → XML宣言**

と判断します。

### XML本文

XML本文には、実際のデータを要素や属性として記述します。

~~~xml
<book category="programming">
  <title>Python入門</title>
  <price>2000</price>
</book>
~~~

ここでは、

~~~text
book
title
price
→ 要素

category
→ 属性

Python入門
2000
→ 実データ
~~~

です。

### DTD

DTDでは、XML文書にどのような要素や属性を記述できるかを定義します。

例えば、

~~~text
book
├─ title
└─ price
~~~

という構造を定義したい場合、DTDでは次のような宣言を使います。

~~~xml
<!ELEMENT book (title, price)>
<!ELEMENT title (#PCDATA)>
<!ELEMENT price (#PCDATA)>
~~~

これは、

~~~text
book 要素の中には
title
price
の順で置く
~~~

という意味です。

属性についても定義できます。

~~~xml
<!ATTLIST book
  category CDATA #REQUIRED>
~~~

この例では、book 要素に category 属性を持たせるルールを定義しています。

FEではDTDの細かな記法を暗記するより、

~~~text
要素
属性
並び方
出現回数
↓
文書構造のルール
~~~

と理解することを優先します。

### DOCTYPEとの関係

XML文書では、DOCTYPE宣言を使ってDTDとの関係を示せます。

例えば外部DTDを使う場合は、

~~~xml
<!DOCTYPE book SYSTEM "book.dtd">
~~~

のように記述します。

イメージは、

~~~text
XML文書
↓
DOCTYPE宣言
↓
使用するDTDを指定
~~~

です。

DTDそのものとDOCTYPE宣言は同じものではありません。

~~~text
DTD
→ 文書構造のルール

DOCTYPE宣言
→ どのDTDを使うか示す
~~~

と切り分けます。

### 内部DTDと外部DTD

DTDは、XML文書内に直接書くことも、別ファイルに分けることもできます。

~~~text
XML文書の中に書く
→ 内部DTD

別ファイルに置く
→ 外部DTD
~~~

FEでは細かな文法より、**DTDが文書型を定義するもの**だと理解できれば十分です。

### XML Schemaとの違い

XML Schema（XSD）も、XML文書の構造を定義する仕組みです。

ただし、DTDよりもデータ型などを詳しく指定できます。

~~~text
DTD
→ 要素・属性・構造を定義

XML Schema
→ 要素・属性・構造
  ＋ データ型などを詳しく定義
~~~

XML SchemaはXML形式で記述されます。

例えば、

~~~text
年齢
→ 整数

日付
→ 日付型
~~~

のように、データ型を明確に指定できます。

試験では、

> **DTDもXML Schemaも構造を定義するが、XML Schemaは型をより詳細に扱える**

と切り分けます。

XMLの基本仕様は、[W3C：Extensible Markup Language (XML)](https://www.w3.org/TR/xml/) で確認できます。

XML Schemaは、[W3C：XML Schema Definition Language (XSD) 1.1](https://www.w3.org/TR/xmlschema11-1/) で確認できます。

## 科目Aでどう出る？

科目Aでは、

> 「DTDに記述するものはどれか」

のように、XML宣言やXML本文と混同させる問題が出ます。

### 判断表

| 記述内容 | どこに書く？ |
|---|---|
| XMLのバージョン | XML宣言 |
| 文字エンコーディング | XML宣言 |
| 実際のデータ | XML本文 |
| 要素名・属性名・要素の並び方 | **DTD** |
| 詳細なデータ型を含む構造定義 | XML Schema |

試験中は、

~~~text
version
encoding
→ XML宣言

実データ
→ XML本文

構造・文書型
→ DTD
~~~

と切れば十分対応しやすくなります。

### 「文書型」が強い手掛かり

DTDは、

~~~text
Document
Type
Definition
~~~

の略です。

そのため、

> **文書型の定義**

という表現が出たら、DTDを強く疑います。

### 「文字コード」はDTDではない

文字コードは、

~~~xml
<?xml version="1.0" encoding="UTF-8"?>
~~~

のようにXML宣言で指定します。

したがって、

~~~text
使用する文字コード
→ DTD
~~~

ではありません。

### 「データそのもの」はDTDではない

DTDは、どのような構造でデータを書いてよいかを定義します。

~~~text
DTD
→ ルール

XML本文
→ 実データ
~~~

です。

ここを逆にしないようにします。

## どんな場面で使う？

### XML文書の構造をそろえる

複数のシステムでXMLを交換するとき、

~~~text
システムA
→ 独自の要素名

システムB
→ 別の要素名
~~~

のように構造がばらばらでは扱いにくくなります。

DTDなどで、

~~~text
どの要素を使うか
どの順序で置くか
どの属性を使うか
~~~

を決めておけば、文書構造を統一できます。

### XML文書がルールに合っているか確認する

DTDで定義したルールに対してXML文書を検証すると、

~~~text
必要な要素がない
順番が違う
許可されていない要素がある
~~~

といった構造上の違いを見つけられます。

### システム間でデータを交換する

XMLは、構造化データをシステム間で交換するときに使われます。

現在はJSONがよく使われる場面も多いですが、FEではXMLとJSONの特徴を切り分けられることが重要です。

JSONとの違いは、[JSONとは？](/fe/json/)で整理しています。

## よくある誤解・混同

### DTDには実データを書く

違います。

~~~text
DTD
→ データの構造を定義

XML本文
→ 実データを書く
~~~

です。

### DTDで文字コードを指定する

違います。

文字エンコーディングはXML宣言で指定します。

~~~text
encoding="UTF-8"
→ XML宣言
~~~

です。

### DTDとDOCTYPEは同じ

完全には同じではありません。

~~~text
DTD
→ 文書型の定義そのもの

DOCTYPE宣言
→ 文書型を宣言し、DTDを指定するために使う
~~~

と考えます。

### DTDとXML Schemaはまったく同じ

どちらもXML文書の構造を定義できますが、機能や記述方法が異なります。

~~~text
DTD
→ 文書構造を定義

XML Schema
→ 文書構造
  ＋ 詳細なデータ型
~~~

と切り分けます。

### XML署名もDTDの一種

違います。

XML署名は、XML文書やその一部分にデジタル署名を付けて、改ざんの有無や署名者を確認する仕組みです。

DTDは、XML文書の構造を定義する仕組みです。

XML署名については、[XML署名とは？](/fe/xml-digital-signature/)で整理しています。

## まとめ（試験直前用）

- **DTD = Document Type Definition**
- DTDは、XML文書の**文書型・構造を定義する**
- 要素・属性・並び方・出現ルールなどを定義できる
- XMLのバージョンと文字コードは**XML宣言**
- 実際のデータは**XML本文**
- DOCTYPE宣言で使用するDTDを示すことができる
- XML Schemaも構造を定義するが、データ型などをより詳細に扱える
- 「文書型の定義」と出たらDTDを疑う

~~~text
version・encoding
→ XML宣言

実データ
→ XML本文

文書構造のルール
→ DTD
~~~

> **DTDは「データ」ではなく、「データを書くための構造ルール」。**

{% include fe_article_footer.html %}
