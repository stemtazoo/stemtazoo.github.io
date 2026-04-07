---
layout: page
title: 参照整合性とは？外部キーとデータ整合性を理解【DS検定】
description: 参照整合性は外部キーとデータ整合性を理解するための用語です。この記事では仕組み・役割・使いどころを押さえ、DS検定で問われる判断ポイントとひっかけポイントを解説します。
permalink: /ds/referential-integrity/
categories: [data-engineering]
tags: [ds, database]
prev: /ds/rdb-vs-nosql/
next: /ds/star-schema/
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

参照整合性（Referential Integrity）とは、外部キーが参照する値が必ず参照先テーブルに存在することを保証するルールです。

DS検定では **「存在しないデータを参照してしまう問題を防ぐ仕組み」**として理解できるかが重要です。




## 直感的な説明

データベースでは、テーブル同士が関係を持っています。

例えば、ECサイトを考えてみます。

顧客テーブル

顧客ID	名前

1	田中
2	鈴木


注文テーブル

注文ID	顧客ID

100	1


このとき、もし次のようなデータが登録されたらどうでしょう。

注文ID	顧客ID

101	99


顧客ID「99」は顧客テーブルに存在しません。

つまり

存在しない顧客の注文

という矛盾したデータができてしまいます。

このような問題を防ぐ仕組みが

参照整合性です。



## 定義・仕組み

参照整合性とは

> 外部キーの値は、参照先テーブルの主キーに存在する値でなければならない



というルールです。

つまり

外部キー ⊆ 主キー

という関係になります。

例えば

顧客テーブル（主キー）

顧客ID

1
2


注文テーブル（外部キー）

注文ID	顧客ID

100	1
101	2


この場合は問題ありません。

しかし

注文ID	顧客ID

102	99


のようなデータは

参照整合性違反

となります。

そのためデータベースは

登録を拒否します。



更新・削除時のルール

参照整合性は、更新や削除のときにも重要になります。

例えば

顧客テーブル

顧客ID

1


注文テーブル

注文ID	顧客ID

100	1


この状態で

顧客ID「1」を削除すると

注文テーブルは

顧客ID = 1

を参照できなくなります。

この問題を防ぐために

削除を禁止

自動削除（CASCADE）

NULLに変更


などのルールを設定することがあります。



## どんな場面で使う？

参照整合性は

リレーショナルデータベースの基本ルールです。

例えば

ECサイト

顧客 → 注文

学校データ

学生 → 履修

会社データ

社員 → 部署

このように

テーブル同士の関係がある場合は必ず必要になります。



## よくある誤解・混同

外部キー = 参照整合性ではない

DS検定ではこの違いが重要です。

用語	意味

外部キー	他テーブルを参照する列
参照整合性	参照関係が正しいことを保証するルール


つまり

外部キー → 構造

参照整合性 → ルール

です。



主キーとは役割が違う

用語	役割

主キー	レコードを識別
外部キー	他テーブル参照
参照整合性	参照関係の正しさを保証


この3つの関係を整理できることが重要です。



DS検定の典型的なひっかけ

選択肢で次のように書かれていたら注意です。

❌ 「参照整合性は重複データを防ぐ」

これは誤りです。

重複を防ぐのは

主キーや一意制約です。

参照整合性は

存在しないデータ参照を防ぐ仕組みです。



## まとめ（試験直前用）

参照整合性は 外部キーの整合性ルール

外部キーの値は参照先の主キーに存在する必要がある

存在しないデータ参照を防ぐ

更新や削除時の整合性も管理する


DS検定では

主キー = 識別
外部キー = 関係
参照整合性 = ルール

と整理して覚えると選択肢を切りやすくなります。



## 対応スキル項目（データエンジニアリング力シート）

データ管理

データベース


★ データベースの基本概念（テーブル、主キー、外部キーなど）を理解している ★ データの整合性や品質を保つ仕組みを理解している

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
