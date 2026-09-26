---
layout: page
title: REST APIとは？SOAPとの違いを整理【DS検定】
description: "REST APIを、RESTの設計制約を意識しながらHTTPでリソースを扱うWeb APIとして整理します。RESTは通信プロトコルではなくアーキテクチャスタイルであり、HTTPメソッドとの関係やSOAPとの違いをDS検定向けに確認します。"
permalink: /ds/rest-api/
categories: [data-engineering]
tags: [ds, data-collection, data-processing]
ds_area: dataengineering
ds_section: data-collection
prev: /ds/mapreduce/
next: /ds/rest-api-methods/
last_modified_at: 2026-09-26
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

REST APIとは、**RESTの設計制約を意識して、HTTPなどを使いリソースを扱うWeb API**です。  
DS検定では「RESTとSOAPの違いを判断できるか」が問われます。


## 直感的な説明

REST APIは、  
**「Web上のリソースをURIで識別し、HTTPの仕組みを活用して扱うAPI」**と考えると理解しやすいです。

たとえば、

- `/users/1` に  
- GETでアクセス → ユーザー情報を取得  
- DELETEでアクセス → ユーザー削除  

というように、  
**URL＝対象、HTTPメソッド＝操作内容**  
という考え方で動きます。

日常の業務で言えば、

- 顧客データを取得する
- 注文を登録する
- 在庫情報を更新する

こうした処理をWeb経由で行うのがREST APIです。

なぜ重要かというと、  
**多くのデータ連携はRESTで行われている**からです。


## 定義・仕組み

REST（Representational State Transfer）は、  
**分散システムのためのアーキテクチャスタイル**です。

Web APIではHTTPと組み合わせて実装されることが多いですが、**RESTそのものがHTTPという意味ではありません**。

特徴は次の通りです。

- リソースをURIで識別する
- HTTPを使うREST APIでは、HTTPメソッドで操作の意味を表す
  - GET（取得）
  - POST（作成）
  - PUT/PATCH（更新）
  - DELETE（削除）
- ステートレス（前回の状態を保持しない）

重要なのは、  
**「RESTはプロトコルではなく設計思想」**という点です。

一方、SOAPは

- XMLベースのメッセージ形式
- 独自の通信仕様を持つ

という特徴があります。

DS検定では  
**REST＝アーキテクチャスタイル**  
**SOAP＝XMLベースのメッセージ交換仕様**  
という切り分けができるかがポイントです。


## どんな場面で使う？

### 使うべき場面

- Webアプリとサーバー間通信
- スマホアプリとクラウドの連携
- データ分析基盤へのデータ取得

現在の多くのクラウドAPIはRESTです。

### 誤解しやすい場面

- 「XMLを使っている＝RESTではない」と思い込む  
  → RESTでもXMLを返すことはあります。

重要なのは  
**RESTの制約を意識したリソース指向の設計かどうか**です。


## よくある誤解・混同

### ① RESTとSOAPの混同

DS検定ではよく

- 「XMLを使う通信方式」
- 「HTTPメソッドでCRUD操作」

を入れ替えて出してきます。

判断基準は次の通りです。

| 特徴 | REST | SOAP |
|------|------|------|
| 位置づけ | アーキテクチャスタイル | XMLベースのメッセージ交換仕様 |
| Web APIでよく使う仕組み | HTTP | HTTPなど複数の転送方式を利用可能 |
| メッセージ形式 | JSONなどをよく利用 | XML |

選択肢で  
「XMLベースのメッセージ通信」と書かれていたら  
→ SOAP

「HTTPメソッドでリソース操作」と書かれていたら  
→ REST

これが切り分け基準です。


## まとめ（試験直前用）

- RESTは通信プロトコルではなくアーキテクチャスタイル
- REST APIではHTTPを使ってリソースを扱う実装が一般的
- SOAPはXMLベースのメッセージ交換仕様
- 「XML」と書いてあればSOAPの可能性が高い
- 「CRUDをHTTPで実行」と書いてあればREST


## 公式情報・参考リンク

- [Roy Fielding｜Architectural Styles and the Design of Network-based Software Architectures](https://ics.uci.edu/~fielding/pubs/dissertation/top.htm)
  - RESTを提案したFieldingの博士論文です。RESTは特定の通信プロトコルではなく、分散ハイパーメディアシステムのためのアーキテクチャスタイルとして整理されています。
- [RFC 9110 - HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html)
  - REST APIで広く使われるHTTPのmethod、request / response、status codeなどの意味論を定義するInternet Standardです。

## 対応スキル項目（ver.6 データエンジニアリング）

- **位置づけ**：REST API設計概念の補助学習
- **★1直接対応**：なし
- 旧ver.5では対応項目がありましたが、ver.6の★1一覧には同一テーマの直接項目として掲載されていません。試験理解を補う関連テーマとして整理します。
- [ver.6 ★1スキルチェックで確認する](/ds/engineering-skillcheck/)
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
