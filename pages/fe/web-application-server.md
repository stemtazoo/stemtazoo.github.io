---
layout: page
title: Webサーバとアプリケーションサーバの違い｜なぜ大規模Webシステムでは分ける？【基本情報技術者試験】
description: Webサーバとアプリケーションサーバの役割の違いを整理し、大規模Webシステムで分離する理由を「できる・できない」ではなく変更・増強のしやすさから解説します。
permalink: /fe/web-application-server/
tags: [fe, fe-technology, system-architecture, web-system]
fe_section: テクノロジ系
fe_subsection: システム構成要素
fe_order: 71
date: 2026-10-04
last_modified_at: 2026-10-04
---

<style>
.webapp-stack {
  max-width: 560px;
  margin: 1.2rem auto;
  display: grid;
  gap: 8px;
}
.webapp-stack .layer {
  border: 1px solid #cbd5e1;
  border-radius: 10px;
  padding: 14px;
  text-align: center;
  background: #f8fafc;
}
.webapp-stack .arrow {
  text-align: center;
  font-weight: 700;
}
.scale-compare {
  display: grid;
  gap: 12px;
  margin: 1rem 0;
}
.scale-box {
  border: 1px solid #d1d5db;
  border-radius: 10px;
  padding: 14px;
}
@media (min-width: 720px) {
  .scale-compare { grid-template-columns: 1fr 1fr; }
}
</style>

## まず結論

大規模なWebシステムでWebサーバとアプリケーションサーバを分ける主な理由は、**Webサーバに業務処理が「できない」からではなく、役割を分離して変更・増強しやすくするため**です。

試験では、まず次のように整理します。

```text
Webサーバ
→ Webの要求受付・コンテンツ配信など

アプリケーションサーバ
→ 業務ロジック・アプリケーション処理

データベース
→ データの保存・検索
```

> **「できる／できない」ではなく、「分けると変更・増強しやすい」で判断する。**

## 直感的な説明

ECサイトをイメージします。

<div class="webapp-stack">
  <div class="layer"><strong>ブラウザ</strong><br>商品を検索・注文する</div>
  <div class="arrow">↓</div>
  <div class="layer"><strong>Webサーバ</strong><br>Webからの要求を受け付ける</div>
  <div class="arrow">↓</div>
  <div class="layer"><strong>アプリケーションサーバ</strong><br>在庫確認・金額計算・注文処理</div>
  <div class="arrow">↓</div>
  <div class="layer"><strong>データベース</strong><br>商品・在庫・注文データを保存</div>
</div>

小規模なら複数の役割を同じサーバで担当する構成も可能です。

大規模になると役割を分けることで、アクセスが増えた部分や処理が重い部分を個別に増強しやすくなります。

## 定義・仕組み

### Webサーバ

Webサーバは、HTTPなどを使ってクライアントからの要求を受け、Webコンテンツや応答を返す役割を担います。

典型的には、HTML・CSS・画像などの静的コンテンツを配信したり、必要に応じてアプリケーション側へ処理を渡したりします。

### アプリケーションサーバ

アプリケーションサーバは、Webアプリケーションの業務処理を担当します。

例えば、

- 入力内容の検証
- 商品価格の計算
- 在庫確認
- 注文処理
- トランザクション管理
- データベースとの連携

などです。

JavaのWebアプリケーションではServletなどのサーバ側処理が関係します。詳しくは[Java Servletとは？](/fe/java-servlet/)で整理しています。

### データベース層

データベースは、商品・利用者・注文などのデータを保存・検索・更新します。

```text
Web
→ 入口・Web配信

Application
→ 業務処理

Database
→ データ
```

この役割分担は、[3層クライアントサーバシステム](/fe/three-tier-client-server/)の考え方ともつながります。

## 科目Aでどう出る？

今回のような問題では、「Webサーバだけでは○○できない」という強い表現に注意します。

| 選択肢の考え方 | 判断 |
|---|---|
| Webサーバだけでは業務処理を実行できない | 「できない」と断定しているので注意 |
| Webサーバだけでは動的コンテンツを作れない | 「できない」と断定しているので注意 |
| 分離すると変更・増強しやすい | 適切 |
| Webサーバには認証機能がない | 「ない」と断定しているので注意 |

### 「できない」ではなく「分けるメリット」を見る

Webサーバとアプリケーションサーバを分ける理由を、

```text
Webサーバには機能がない
→ だから別サーバが必要
```

と覚えるのは危険です。

試験では、

```text
役割を分離
↓
必要な部分を変更しやすい
必要な部分を増強しやすい
↓
大規模化に対応しやすい
```

と考える方が安全です。

## どんな場面で使う？

### Web側の負荷が大きい

<div class="scale-compare">
  <div class="scale-box"><strong>Web側を増強</strong><br><br>Web 1<br>Web 2<br>Web 3<br>↓<br>Application<br>↓<br>DB</div>
  <div class="scale-box"><strong>業務処理側を増強</strong><br><br>Web<br>↓<br>Application 1<br>Application 2<br>Application 3<br>↓<br>DB</div>
</div>

役割が分かれていれば、負荷の大きい部分を中心に構成を見直せます。

### 業務ロジックだけ変更したい

業務ルールの変更なら、アプリケーション層を中心に変更できます。

```text
画面・Web配信
→ Web側

業務ルール
→ アプリケーション側

保存方法・データ
→ DB側
```

これは、保守や変更の影響範囲を整理しやすくする考え方でもあります。

## よくある誤解・混同

### Webサーバでは業務処理ができない？

そうとは限りません。

Webサーバとアプリケーションサーバの機能を同じ環境に持たせる構成もあります。

FEでは、**役割を分離するメリット**と、特定製品で何が実行できるかを分けて考えます。

### Webサーバでは動的コンテンツを生成できない？

これも「絶対にできない」と覚えるのは適切ではありません。

サーバ側プログラムを使って動的な応答を生成する構成があります。

「Webサーバ＝静的ファイルしか返せない」と固定して覚えないようにします。

### Webサーバには認証機能がない？

Webサーバでも、基本認証やダイジェスト認証などを扱えるものがあります。

したがって、

```text
認証したい
→ 必ずアプリケーションサーバが必要
```

とは判断できません。

### 役割を分ければ必ず安くなる？

必ずしもそうではありません。

分離すると拡張や保守をしやすくなる一方、構成や運用が複雑になる場合もあります。

試験では、**変更・増強しやすい**という利点を中心に押さえます。

### Servletの記事との関係

Servletはサーバ側でHTTP要求を処理するJavaのAPIです。

[Java Servletの記事](/fe/java-servlet/)でいう「サーバ側」と、今回の「Webサーバとアプリケーションサーバを物理的・論理的に分けるか」は別の論点です。

```text
Servlet
→ どこで処理する技術か

Web/APサーバ分離
→ システムの役割をどう分けるか
```

過去問の「Webサーバ上だけで動作」という表現を、現代のWebシステム全般に広げて解釈しないようにします。

## まとめ（試験直前用）

- Webサーバ → Web要求の受付・コンテンツ配信など
- アプリケーションサーバ → 業務ロジック・アプリケーション処理
- DB → データの保存・検索
- 大規模システムでは、役割を分けると変更・増強しやすい
- 「Webサーバでは○○できない」という断定に注意
- 3層構成は「必ず3台」という意味ではなく、論理的な役割分担
- Servletの「サーバ側実行」と、Web/APサーバの分離は別の論点

試験では、

> **Web＝入口、AP＝業務処理、DB＝データ。分ける理由は拡張・変更しやすくするため。**

と整理すると選択肢を切りやすくなります。

{% include fe_article_footer.html %}
