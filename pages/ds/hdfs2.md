---
layout: page
title: HDFS（Hadoop分散ファイルシステム）とは？大規模データを保存する仕組み【DS検定】
permalink: /ds/hdfs/
categories: [business]
tags: [ds, data-storage, design]
prev: /ds/filter/
next: /ds/hot-cool-archive/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

HDFS（Hadoop Distributed File System）とは、大量のデータを複数のコンピュータに分散して保存するためのファイルシステムです。

DS検定では
「大量データを分散保存する仕組み」
として Hadoop や Spark の文脈で理解できているかが問われます。



## 直感的な説明

普通のパソコンでは、データは 1台のコンピュータのディスク に保存されます。

しかし、ビッグデータになると次の問題が起きます。

1台のディスクに入りきらない

読み込みが遅い

故障するとデータが失われる


そこで使われるのが HDFS です。

イメージとしては

> 大きすぎるデータを
複数のコンピュータに分けて保存する巨大な倉庫



です。

例えば100TBのデータでも

サーバーA

サーバーB

サーバーC


のように 分割して保存することで扱えるようになります。



## 定義・仕組み

HDFSは Hadoopで使われる分散ファイルシステムです。

特徴は次の3つです。

① データを分割して保存する

大きなファイルは ブロック単位（例：128MB） に分割されます。

例

巨大ファイル ↓ ブロック1 ブロック2 ブロック3

それぞれが 別のサーバーに保存されます。



② データを複製して保存する

HDFSでは通常

同じデータを複数のサーバーにコピーして保存します。

これを レプリケーションといいます。

例

ブロック1 → サーバーA → サーバーB → サーバーC

そのため

サーバーが壊れてもデータを失わない

安定したデータ処理が可能


になります。



③ 分散処理と相性が良い

HDFSは 分散処理（MapReduceやSpark） と組み合わせて使われます。

特徴は

データを集めるのではなく、処理をデータのある場所へ送る

という考え方です。

これを

データローカリティ（Data Locality）

と呼びます。

その結果

ネットワーク転送が減る

大規模データでも高速処理できる


というメリットがあります。



## どんな場面で使う？

HDFSは次のような ビッグデータ環境で使われます。

大規模ログ分析

例

Webアクセスログ

IoTデータ

センサーデータ


数TB〜PBのデータでも保存できます。



データレイク

企業では

構造化データ

非構造化データ

半構造化データ


をまとめて保存する

データレイク

としてHDFSが使われることがあります。



AI・機械学習のデータ基盤

AIの学習では

画像

テキスト

センサーデータ


などの 巨大データを扱います。

その保存基盤として

Hadoop

Spark


と一緒にHDFSが利用されます。



## よくある誤解・混同

RDBMSと同じだと思う

これは誤りです。

項目	HDFS	RDBMS

用途	大規模データ保存	データ管理
構造	ファイル	テーブル
処理	分散処理	SQL


DS検定では

「HDFSはデータベースではない」

という点が重要です。



小さいファイル処理に向いていると思う

これも誤解です。

HDFSは

大きなファイル処理に最適化されています。

そのため

小さいファイルが大量

低レイテンシ処理


には向いていません。



Sparkだけでデータ保存できると思う

Sparkは

データ処理エンジン

であり、

データ保存はHDFSなどのストレージが担当

します。

DS検定では

この役割の違いを問われることがあります。



## まとめ（試験直前用）

HDFSは Hadoopの分散ファイルシステム

大量データを 複数サーバーに分割保存

レプリケーションで耐障害性を確保

ビッグデータ保存基盤として使われる

DS検定では RDBMSとの違いがよく問われる




## 対応スキル項目（データエンジニアリング力シート）

スキルカテゴリ名
データ蓄積

サブカテゴリ名
分散技術

★ Hadoop・Sparkの分散技術の基本的な仕組みと構成を理解している

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
