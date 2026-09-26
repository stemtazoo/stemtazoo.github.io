---
layout: page
title: REST API のメソッドとは？データ操作の役割を整理【DS検定】
description: "REST APIでよく使うHTTPメソッドを、GETは取得、POSTは処理依頼・作成、PUTは置換、PATCHは部分変更、DELETEは削除という代表的な使い方で整理します。HTTP仕様とCRUDの対応を混同しない判断軸も確認します。"
permalink: /ds/rest-api-methods/
categories: [data-engineering]
tags: [ds, data-collection, data-processing]
ds_area: dataengineering
ds_section: data-collection
prev: /ds/rest-api/
next: /ds/soap/
last_modified_at: 2026-09-26
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

REST APIでは、**HTTPメソッドを使ってリソースに対する要求の意味を表す**のが一般的です。

DS検定では、まず次の対応を切り分けます。

| 代表的な使い方 | メソッド |
|---|---|
| 取得 | `GET` |
| 処理依頼・作成 | `POST` |
| 全体の置換 | `PUT` |
| 部分変更 | `PATCH` |
| 削除 | `DELETE` |

## 直感的な説明

REST APIを「データを操作する窓口」と考えると分かりやすいです。

ECサイトなら、

| やりたいこと | REST APIメソッド | イメージ |
|---|---|---|
| 商品情報を見る | `GET` | 読む |
| 新しい商品を登録 | `POST` | 作る |
| 商品情報を更新 | `PUT` / `PATCH` | 書き換える |
| 商品を削除 | `DELETE` | 消す |

という対応になります。

## 定義・仕組み

REST APIでは、HTTPメソッドを使ってサーバーに操作内容を伝えます。

### CRUDとの対応

CRUDとHTTPメソッドは、実務では次のように対応づけることが多いです。

| CRUD | 代表的なHTTPメソッド |
|---|---|
| Create | `POST` |
| Read | `GET` |
| Update | `PUT` / `PATCH` |
| Delete | `DELETE` |

ただし、**HTTP仕様そのものが「POST = Create」と固定しているわけではありません**。POSTはリソース固有の処理を依頼する汎用的なメソッドです。

DS検定では、まず**「データ取得 = GET」**を確実に判断できることが重要です。

## どんな場面で使う？

### 外部データの取得

- 天気API
- 地図API
- 株価・オープンデータAPI

Pythonでは、例えば次のように `GET` でデータを取得します。

```python
import requests

response = requests.get("https://api.example.com/data")
data = response.json()
```

### システム間連携

- 商品情報の登録・更新
- 顧客情報の参照
- 外部サービスとのデータ連携

## よくある誤解・混同

### ❌ `GET` と `POST` は同じ

違います。

- `GET` → **取得**
- `POST` → **作成・送信**

### ❌ `PUT` と `PATCH` は完全に同じ

どちらも更新に使われますが、一般的には次のように整理されます。

| メソッド | 更新イメージ |
|---|---|
| `PUT` | 指定URIの状態を送信内容で置き換える |
| `PATCH` | リソースへ部分的な変更を適用する |

### ❌ RESTは通信プロトコル

RESTは**API設計の考え方**です。HTTPは通信プロトコルです。

## まとめ（試験直前用）

- **GET = 取得**
- **POST = 処理依頼・作成でよく使う**
- **PUT = 置換 / PATCH = 部分変更**
- **DELETE = 削除**
- RESTは設計の考え方、HTTPは通信プロトコル

試験で「外部システムからデータを取得する」とあれば、まず `GET` を疑いましょう。

## 公式情報・参考リンク

- [RFC 9110 - HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html)
  - GET・POST・PUT・DELETEなどのHTTP methodの意味を確認できるInternet Standardです。
- [RFC 5789 - PATCH Method for HTTP](https://www.rfc-editor.org/rfc/rfc5789.html)
  - PATCHを、既存リソースへ部分的な変更を適用するHTTPメソッドとして定義しています。

## 対応スキル項目（ver.6 データエンジニアリング）

- **分類**：データエンジニアリング
- **スキルカテゴリ**：データ共有
- **サブカテゴリ**：データ展開
- **必須スキル**：—
- ★ RESTなどのデータ取得用Web APIを用いて、必要なデータを取得できる
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
