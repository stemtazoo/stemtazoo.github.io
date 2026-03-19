---
layout: page
title: Web APIとは？HTTPでサービスとデータをやり取りする仕組み【DS検定】
permalink: /ds/web-api/
categories: [data-engineering]
tags: [ds, data-processing]
prev: /ds/spark/
next: /ds/yarn/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

Web APIとは、HTTP通信を使って外部のサービスやデータをプログラムから利用できる仕組みです。

DS検定では
「Web APIはHTTP通信を利用する」
「GETやPOSTなどのHTTPメソッドでデータをやり取りする」
という理解があるかを問われることが多いです。

特に試験では

Web APIはJSONだけを扱う

Web APIでは画像は取得できない


のような 誤った思い込みを狙った選択肢がよく出ます。



## 直感的な説明

Web APIは、
**「プログラムがWebサービスにお願いする窓口」**のようなものです。

例えば次のようなサービスがあります。

天気情報サービス

地図サービス

株価データ

生成AI

翻訳サービス


これらのサービスは、
ブラウザだけでなく プログラムからも利用できます。

例えばPythonから

天気データをください

とリクエストすると

今日の天気：晴れ
気温：25℃

のようなデータが返ってきます。

このように
プログラムがHTTP通信を使ってサービスとデータをやり取りする仕組み
がWeb APIです。



## 定義・仕組み

Web APIは次の仕組みで動きます。

① HTTP通信を利用する

Web APIは

HTTP

HTTPS


といった Web通信の仕組みを使います。

つまり、Webブラウザと同じ通信方式です。



② HTTPメソッドを使って操作する

Web APIでは
HTTPメソッドを使って操作を表現します。

代表例

メソッド	意味

GET	データを取得する
POST	データを送信する
PUT	データを更新する
DELETE	データを削除する


DS検定では

「Web APIのメソッドとしてGETやPOSTがある」

という選択肢がよく出ます。



③ さまざまな形式のデータを扱える

Web APIで扱うデータ形式は様々です。

代表例

JSON

XML

画像

音声

動画

バイナリデータ


DS検定では

「Web APIではJSONしか扱えない」

という誤った選択肢が出ることがあります。



④ RESTという設計思想がよく使われる

多くのWeb APIは
REST（Representational State Transfer）
という設計原則に基づいて作られています。

RESTは

URLでデータを表現する

HTTPメソッドを使う

シンプルな構造


という特徴があります。

ただし注意点として

RESTは通信プロトコルではなく設計思想です。



## どんな場面で使う？

Web APIは
データ取得やサービス連携で広く使われます。

代表例をいくつか紹介します。

データ取得

天気データ

株価

地理情報


データサイエンスでは
外部データ収集の手段としてよく利用されます。



AIサービス

翻訳API

生成AI API

画像認識API


AI機能をアプリに組み込むときは
Web API経由でAIサービスを利用することが多いです。



システム連携

企業システムでも

顧客管理

在庫管理

決済サービス


などをAPIで連携させています。



## よくある誤解・混同

誤解①

Web APIはJSONしか扱えない

これは誤りです。

Web APIは

JSON

XML

画像

音声


など様々なデータを扱えます。

DS検定では

「Web APIでは画像データは取得できない」

という選択肢が出ることがありますが
これは 誤りです。



誤解②

RESTは通信プロトコル

これもよくある混同です。

用語	意味

REST	APIの設計原則
HTTP	通信プロトコル


つまり

RESTは通信方法ではなく設計ルールです。



誤解③

Web APIはWebページ取得と同じ

似ていますが目的が違います。

用途	説明

Webページ	人が見る
Web API	プログラムが使う


データサイエンスでは
プログラムでデータを取得するためにAPIを使うことが多いです。



## まとめ（試験直前用）

Web APIは HTTP通信を使ってサービスやデータを利用する仕組み

GET・POSTなどの HTTPメソッドで操作する

JSONだけでなく 画像・音声なども送受信できる

RESTは APIの設計原則（通信プロトコルではない）

DS検定では
「Web APIでは画像取得できない」などの誤り選択肢に注意




【対応スキル項目（データエンジニアリング力シート）】

IT基盤

API

★ APIを利用したデータ取得・連携の基本的な仕組みを理解している

## 🔗 関連記事

<ul style="padding-left: 20px;">
{% assign current_tags = page.tags %}
{% assign count = 0 %}

{% for p in site.pages %}
  {% if p.url != page.url and p.tags %}
    {% assign matched = false %}

    {% for tag in current_tags %}
      {% if p.tags contains tag and tag != "ds" %}
        {% assign matched = true %}
      {% endif %}
    {% endfor %}

    {% if matched %}
      <li style="margin-bottom: 6px;">
        <a href="{{ p.url }}">{{ p.title }}</a>
      </li>
      {% assign count = count | plus: 1 %}
    {% endif %}

    {% if count >= 5 %}
      {% break %}
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

<hr>

<div style="margin-top: 16px;">
  🏠 <a href="/ds/">DS検定トップに戻る</a>
</div>

<div style="display:flex;justify-content:space-between;margin-top:12px;">

  {% if page.previous.url %}
    <a href="{{ page.previous.url }}">← {{ page.previous.title }}</a>
  {% endif %}

  {% if page.next.url %}
    <a href="{{ page.next.url }}">{{ page.next.title }} →</a>
  {% endif %}

</div>
