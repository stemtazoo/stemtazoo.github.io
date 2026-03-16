---
layout: page
title: REST API のメソッドとは？データ操作の役割を整理【DS検定】
permalink: /ds/rest-api-methods/
tags: [ds, business]
---

まず結論

REST API のメソッドとは、API を通じてデータに対してどのような操作（取得・作成・更新・削除）を行うかを表す HTTP の命令です。
DS検定では 「GET＝取得」「POST＝作成」「PUT/PATCH＝更新」「DELETE＝削除」 を正しく切り分けられるかがよく問われます。

直感的な説明

REST API は、**「データを外部システムとやり取りするための窓口」**です。

そして メソッドは「その窓口で何をするか」を示す動詞です。

例えばECサイトを考えてみます。

操作	REST APIメソッド	イメージ

商品情報を見る	GET	データを読む
新しい商品を登録	POST	データを作る
商品情報を更新	PUT / PATCH	データを書き換える
商品を削除	DELETE	データを消す


つまり REST API は データベース操作（CRUD）を HTTP で行う仕組み と考えると理解しやすくなります。

DS検定では「外部システムからデータを取得するAPI」などの問題で GET を選ばせる問題がよく出ます。

定義・仕組み

REST API（Representational State Transfer API）は HTTP通信を使ってシステム間でデータをやり取りする仕組みです。

そのとき、HTTPには メソッド（method） があり、これによって どんな操作をしたいか をサーバーに伝えます。

代表的なメソッドは次の通りです。

メソッド	役割	典型用途

GET	データ取得	データ参照
POST	データ作成	新規登録
PUT	データ更新（置き換え）	全体更新
PATCH	データ部分更新	一部更新
DELETE	データ削除	レコード削除


この対応関係は CRUD（Create / Read / Update / Delete） と対応しています。

CRUD	RESTメソッド

Create	POST
Read	GET
Update	PUT / PATCH
Delete	DELETE


DS検定では 「データ取得＝GET」 の判断ができることが重要です。

どんな場面で使う？

REST API メソッドは システム間のデータ連携で広く使われます。

例えば次のような場面です。

Webサービス連携

ECサイトの商品データ取得

天気APIからの天気情報取得

地図APIからの位置情報取得


データ分析

外部APIからデータ収集

SNSデータの取得

オープンデータの取得


例えば Python ではよく次のように使います。

import requests

response = requests.get("https://api.example.com/data")
data = response.json()

この場合は GET メソッドでデータ取得しています。

データサイエンスでは APIを使ってデータ収集する場面が多いため、REST APIの基本理解は重要です。

よくある誤解・混同

① GET と POST の混同

DS検定では GET と POST を混同させる問題がよく出ます。

メソッド	役割

GET	データ取得
POST	データ作成


選択肢で「外部システムからデータを取得する」と書かれていたら GET を選ぶのが基本です。

② PUT と PATCH の違い

実務では更新に PUT / PATCH の両方が使われます。

メソッド	更新範囲

PUT	データ全体を置き換える
PATCH	一部だけ更新


ただし DS検定では 「更新＝PUT」程度の理解で十分な場合が多いです。

③ REST API と HTTP の混同

REST API は、HTTP・URL・JSON などを組み合わせた API設計のスタイルです。

つまり REST API = HTTPメソッドを使ったデータ操作 と理解しておくと問題を解きやすくなります。

まとめ（試験直前用）

REST API メソッドは データ操作の種類を表す HTTP命令

基本対応は CRUD

DS検定では特に次を押さえる


操作	メソッド

取得	GET
作成	POST
更新	PUT / PATCH
削除	DELETE


試験では 「外部システムからデータ取得」→ GET と判断できれば正解できます。


---

【対応スキル項目（データエンジニアリング力シート）】

データエンジニアリング力

データ収集・蓄積

★ 外部データ（オープンデータ、API 等）を取得し、分析に利用できる