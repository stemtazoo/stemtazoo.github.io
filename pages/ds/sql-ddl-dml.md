---
layout: page
title: DDL文とDML文の違いとは？SQLの基本操作を整理【DS検定】
permalink: /ds/sql-ddl-dml/
categories: [data-engineering]
tags: [ds, sql]
---

## まず結論

**DDL文（Data Definition Language）**は「データベースの構造を定義するSQL」

**DML文（Data Manipulation Language）**は「テーブルに入っているデータを操作するSQL」


DS検定では、「テーブルを作るSQL」と「データを操作するSQL」の違いを理解しているかが問われることが多く、
DDL＝構造、DML＝データ操作と整理できるかが判断ポイントになります。



## 直感的な説明

データベースはよく「Excelの表」に例えられます。

まず、

表の列や構造を作る

どんなデータを入れるか決める


必要があります。

そのあとで、

データを追加する

データを修正する

データを削除する


といった操作を行います。

この2つの役割を分けたものがSQLの

DDL文：テーブルの構造を作る

DML文：テーブルのデータを操作する


という分類です。

つまり、

DDL → データの入れ物を作る
DML → 中に入っているデータを扱う

と覚えると理解しやすいです。



## 定義・仕組み

SQL（Structured Query Language）は
リレーショナルデータベースを操作するための言語です。

その中でも基本的な分類として、

DDL文（Data Definition Language）

データベースの構造を定義するSQL

代表例

SQL	意味

CREATE	テーブルやデータベースを作成
ALTER	テーブル構造を変更
DROP	テーブルを削除


例

CREATE TABLE employees (
  id INT,
  name VARCHAR(50)
);

これは

「employeesというテーブル構造を作る」

DDL文です。



DML文（Data Manipulation Language）

テーブルに格納されたデータを操作するSQL

代表例

SQL	意味

SELECT	データ取得
INSERT	データ追加
UPDATE	データ更新
DELETE	データ削除


例

SELECT * FROM employees;

これは

「employeesテーブルのデータを取得する」

DML文になります。



## どんな場面で使う？

実務では次のような流れになります。

システム開発の初期

データベースの構造を作る

CREATE TABLE

などの DDL文 を使う。



システム運用・分析

データを扱う

売上データ取得

顧客情報更新

ログデータ分析


などで

SELECT
INSERT
UPDATE
DELETE

などの DML文 を使います。

データ分析では特に

SELECT + WHERE + JOIN + GROUP BY

のようなDML操作が頻繁に使われます。



## よくある誤解・混同

① SELECTはDDLだと思ってしまう

これはよくある誤解です。

SELECTは

「データの参照」

なので DML文 に分類されます。



② SQLは全部同じ種類と思ってしまう

SQLには実は役割ごとに分類があります。

代表的には

DDL：構造定義

DML：データ操作


です。

DS検定では、

「次のうちDMLに該当するものはどれか」

という形で出題されることがあります。



③ JOINやWHEREはDDLと思ってしまう

これも注意ポイントです。

例えば

SELECT *
FROM sales
JOIN customers

のようなSQLは

データを取り出す操作なので
すべて DML文 の範囲です。



## まとめ（試験直前用）

DDL文 = データベースの構造を定義するSQL

DML文 = テーブルのデータを操作するSQL

CREATE / ALTER / DROP → DDL

SELECT / INSERT / UPDATE / DELETE → DML

DS検定では **「構造操作か、データ操作か」**を区別できることが重要


迷ったら

テーブルの形を作る → DDL
データを扱う → DML

で判断すると選択肢を切りやすくなります。



対応スキル項目

【対応スキル項目（データエンジニアリング力シート）】

スキルカテゴリ：プログラミング

サブカテゴリ：SQL


★ SQLの構文を一通り知っていて、記述・実行できる（DML・DDLの理解、各種JOINの使い分け、集計関数とGROUP BY、CASE文を使用した縦横変換、副問合せやEXISTSの活用など）
