---
layout: page
title: RDBとNoSQLの選び方：注文・ログの要件から比較【DS検定】
description: "RDBとNoSQLを、注文確定・ログ検索・顧客プロフィールの要件から比較します。更新の整合性、検索パターン、拡張性、運用負荷を確認し、データ量や形式だけで決めない選択と併用を説明します。"
permalink: /ds/rdb-vs-nosql/
categories: [data-engineering]
tags: [ds, database]
ds_area: dataengineering
ds_section: database
prev: /ds/primary-key/
next: /ds/referential-integrity/
last_modified_at: 2026-10-19
---

<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**RDBかNoSQLかは、データ量や形式だけでなく、必要な更新・検索・整合性・運用から比較します。** このページは要件から選ぶための教材です。

保存モデルの基本は、[NoSQLの四つのデータモデル](/ds/nosql-datastore/)で確認できます。

## 直感的な説明

ECサイトで「注文確定」と「アクセスログ検索」を考えます。

- 注文では、注文・在庫・決済状態の更新をどう整合させるかが大切。
- ログでは、時刻や利用者IDから何を探すか、書込み量や保存期間が大切。

同じサイトでも要件が違います。注文をRDB、セッションをキーバリュー型、検索用データを別基盤に置くなど、併用も選択肢です。

## 定義・仕組み

RDBは表と関係を扱い、NoSQLは文書・キーと値・グラフなどのモデルを扱います。製品名を選ぶ前に、次の順で条件を整理します。

| 確認する要件 | 質問の例 | 比較時の注意 |
|---|---|---|
| 更新の単位 | 複数の記録をまとめて確定する必要があるか | トランザクションの対応範囲を確認 |
| 検索 | 結合・集計を柔軟に行うか、決まったキーで読むか | データモデルと索引・クエリを確認 |
| 整合性 | 書込み直後にどの読取りで何を保証するか | 製品・構成・設定を確認 |
| 負荷・拡張 | 読み書き量、遅延、分散配置はどうか | RDBにも分散構成があり、NoSQLも一律ではない |
| 運用 | チームの知識、障害対応、費用はどうか | データ移行・バックアップも含める |

RDBの例はPostgreSQL、MySQL、Oracle、SQL Server、NoSQLの例はMongoDB、Redis、Cassandra、HBaseなどです。同じ分類でも機能は異なります。

## どんな場面で使う？

| 要件の例 | 検討の入口 | 採用前に確かめること |
|---|---|---|
| 注文・在庫の更新と、多様な結合検索 | RDBを候補にする | トランザクション、競合、性能 |
| セッションIDで状態を高速に読み書き | キーバリュー型などを候補にする | 有効期限、永続化、障害時の動作 |
| 顧客ごとに異なるプロフィール項目 | 文書型などを候補にする | 項目の検証、検索、更新保証 |
| 大量ログを利用者IDと時刻で検索 | キー設計の合うDBやログ基盤を比較する | 書込み量、検索条件、保存費用 |

これは唯一の正解を示す表ではありません。構造化データをNoSQLで扱うことも、大量データをRDBで扱うこともできます。画像本体などを必ずNoSQLに保存する必要もありません。

## よくある誤解・混同

### ACIDが必要ならNoSQLはすべて不可？

MongoDBのようにACIDトランザクションへ対応する製品もあります。逆に、対応と書かれていても、更新範囲や構成による制約を確認します。

### NoSQLはSQLもスキーマも使わない？

SQLに似た問い合わせや、項目の検証を備える製品もあります。「Not Only SQL」は、全製品に同じ操作や自由度を保証する意味ではありません。

### NoSQLはRDBの後継・上位互換？

全面的に置き換える技術ではありません。併用する場合も、正本をどこに置き、複製先へいつ反映するかを設計します。

## まとめ（試験直前用）

- 更新単位・検索・整合性・拡張・運用を比較する。
- 大量ならNoSQL、正確性ならRDBという一律の判断を避ける。
- 機能は製品と設定で確認する。
- 併用では正本と同期方法も決める。

## 公式情報・参考リンク

- [MongoDB：Transactions](https://www.mongodb.com/docs/manual/core/transactions/)
  - NoSQLにもACIDトランザクションがあり、構成・制約を確認すべきことが分かります。

## 対応スキル項目（ver.6 データエンジニアリング）

- **分類**：データエンジニアリング
- **スキルカテゴリ**：データ蓄積
- **サブカテゴリ**：分散技術
- **必須スキル**：—
- ★ NoSQLデータストア（Cassandra、Mongo DB、CouchDB、Amazon DynamoDB、Azure Cosmos DB、Google Cloud Firestoreなど）にAPIを介してアクセスし、新規データを登録できる
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
