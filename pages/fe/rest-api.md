---
layout: page
title: REST APIとは？GET・POST・PUT・DELETEで資源を操作する考え方【基本情報技術者試験】
description: REST APIを「URLで資源を表し、HTTPメソッドで操作するWeb APIの設計スタイル」として整理し、Web API、CGI、JSON、SOAP、GET・POST・PUT・DELETEの違いをFE試験で切れるように解説します。
permalink: /fe/rest-api/
tags: [fe, fe-technology, network]
fe_section: テクノロジ系
fe_subsection: ネットワーク
fe_order: 55
date: 2026-07-10
last_modified_at: 2026-07-10
---

## まず結論

REST APIとは、**URLで資源を表し、HTTPメソッドで操作するWeb APIの設計スタイル**です。

RESTは、Representational State Transfer の略です。

基本情報技術者試験では、次のように判断すると選択肢を切りやすくなります。

| 用語 | 何を表す？ | 判断の合図 |
|---|---|---|
| Web API | Web経由で機能やデータを利用する窓口 | API、データ取得、サービス連携 |
| REST API | URLとHTTPメソッドで資源を操作するAPIの設計スタイル | リソース、GET、POST、PUT、DELETE |
| JSON | データ交換形式 | `{}`、キーと値、軽量なデータ |
| SOAP | XMLベースの通信仕様 | XML、厳格なメッセージ形式 |
| CGI | Webサーバと外部プログラムを連携させる仕組み | 外部プログラムを実行、ブラウザへ返す |

REST APIは、**APIそのものの名前**というより、Web APIを設計するときの考え方として押さえます。

```text
URL
→ 操作したい対象を表す

HTTPメソッド
→ その対象に何をするかを表す
```

## 直感的な説明

REST APIは、Web上のデータを「対象」と「操作」に分けて扱う考え方です。

例えば、利用者IDが1のユーザー情報を扱うとします。

```text
/users/1
```

このURLは、**どの資源を扱うか** を表します。

そこに、HTTPメソッドで **何をするか** を指定します。

```text
GET    /users/1  → ユーザー情報を取得する
PUT    /users/1  → ユーザー情報を更新する
DELETE /users/1  → ユーザー情報を削除する
```

つまり、REST APIは **URLが対象、HTTPメソッドが操作** と考えると分かりやすいです。

## 定義・仕組み

REST APIでは、Web上で扱うデータや機能を **リソース** として考えます。

リソースは、URLで表します。

| URLの例 | 表すリソース |
|---|---|
| `/users` | ユーザー一覧 |
| `/users/1` | IDが1のユーザー |
| `/orders` | 注文一覧 |
| `/orders/10` | IDが10の注文 |

そして、HTTPメソッドで操作を表します。

| HTTPメソッド | ざっくりした意味 | 例 |
|---|---|---|
| GET | 取得する | ユーザー情報を取得する |
| POST | 作成・送信する | 新しい注文を登録する |
| PUT | 全体を更新する | ユーザー情報を更新する |
| PATCH | 一部を更新する | メールアドレスだけ変更する |
| DELETE | 削除する | 注文を削除する |

REST APIで返すデータ形式としては、JSONがよく使われます。

```json
{
  "id": 1,
  "name": "sample"
}
```

ただし、REST APIとJSONは同じ意味ではありません。

```text
REST API
→ APIの設計スタイル

JSON
→ データの表し方
```

このテーマは、基本情報技術者試験の「ネットワーク」や「システム連携」と関係する内容です。公式の出題範囲やシラバスは、[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html) から確認できます。

## Web APIとの違い

REST APIは、Web APIの一種として考えると分かりやすいです。

| 用語 | 位置づけ | ざっくり |
|---|---|---|
| Web API | Web経由で機能やデータを使うための窓口全般 | 広い言葉 |
| REST API | URLとHTTPメソッドでリソースを操作する設計スタイル | Web APIの代表的な作り方 |

例えば、天気データを取得するAPIがあるとします。

```text
GET /weather/tokyo
```

このように、URLで対象を示し、GETで取得するならREST APIの文脈です。

一方、単に「Web経由で他システムにデータを提供する」とだけ説明されている場合は、より広い意味でWeb APIと判断します。

```text
Web経由で機能やデータを提供する
→ Web API

URLとHTTPメソッドでリソースを操作する
→ REST API
```

## 科目Aでどう出る？

科目Aでは、REST APIの特徴やHTTPメソッドの意味を問う形で出やすいです。

判断するときは、次の表で切ります。

| 問題文の表現 | 選びたい用語 |
|---|---|
| URLでリソースを表し、HTTPメソッドで操作する | REST API |
| Web経由で他システムに機能やデータを提供する | Web API |
| Web APIでよく使われる軽量なデータ交換形式 | JSON |
| XMLベースの厳格なメッセージ通信 | SOAP |
| Webサーバが外部プログラムを実行し、結果をブラウザへ返す | CGI |

HTTPメソッドは、次のように押さえます。

| メソッド | 試験での見方 |
|---|---|
| GET | 取得する |
| POST | 作成・送信する |
| PUT | 更新する |
| PATCH | 一部更新する |
| DELETE | 削除する |

FE試験では、すべての細かいHTTP仕様よりも、**GETは取得、POSTは送信・作成、PUTは更新、DELETEは削除** と切れることが大切です。

## 科目Bでどう使う？

科目Bでは、REST APIはシステム間連携の読み取りで役立ちます。

例えば、次のような処理です。

```text
販売管理システムが在庫管理システムに問い合わせる
↓
GET /items/100/stock
↓
在庫数のJSONデータを受け取る
```

この場合、ポイントは次の3つです。

1. どのシステムが呼び出しているか
2. どのリソースを扱っているか
3. 取得・作成・更新・削除のどれをしているか

REST APIでは、認証や権限管理も重要です。

| 観点 | 例 |
|---|---|
| 認証 | APIキー、OAuth、トークン |
| 通信の保護 | HTTPS |
| 権限 | 参照だけ、更新も可能、管理者のみ削除可 |
| エラー | 404、500などのステータスコード |
| データ形式 | JSON、XML |

科目Bでは、APIを呼び出せることだけでなく、**誰が、どのリソースに、どの操作をできるか** を読むと安全です。

## よくある誤解・混同

REST APIでは、次の混同がよく起こります。

| 混同 | 正しい切り分け |
|---|---|
| REST APIとWeb APIは完全に同じ | Web APIは広い言葉。REST APIは代表的な設計スタイル |
| REST APIとJSONは同じ | REST APIは設計スタイル。JSONはデータ形式 |
| REST APIは必ずJSONだけを返す | JSONが多いが、XMLなどを返すこともある |
| URLがあればすべてREST API | URLでリソースを表し、HTTPメソッドで操作する考え方を見る |
| POSTは必ず更新 | FEではPOSTは作成・送信、PUT/PATCHは更新と押さえる |
| CGIとREST APIが同じ | CGIはWebサーバが外部プログラムを呼ぶ仕組み。REST APIはリソース操作の設計スタイル |

特に、Web API、REST API、JSONは次のように分けます。

```text
Web API
→ Web経由で機能やデータを使う窓口

REST API
→ URLとHTTPメソッドでリソースを操作する設計スタイル

JSON
→ データを表す形式
```

## まとめ（試験直前用）

- REST APIは、URLでリソースを表し、HTTPメソッドで操作する設計スタイル
- Web APIは、Web経由で機能やデータを使うための窓口全般
- JSONは、Web APIでよく使われるデータ交換形式
- GETは取得、POSTは作成・送信、PUTは更新、PATCHは一部更新、DELETEは削除
- REST APIはプロトコル名そのものではなく、Web APIの設計スタイルとして押さえる
- CGIは、Webサーバが外部プログラムを呼び出して結果をブラウザへ返す仕組み
- 判断の合図は「リソース」「URL」「HTTPメソッド」

{% include fe_article_footer.html %}
