---
layout: page
title: アクティビティ図とは？処理の流れ・分岐を表すUML図【基本情報技術者試験】
description: UMLのアクティビティ図について、処理の実行順序や条件分岐、ワークフローを表す図という役割を整理し、オブジェクト図・クラス図・コンポーネント図との違いをFE科目Aで切り分ける視点から解説します。
permalink: /fe/uml-activity-diagram/
tags: [fe, fe-technology, software-engineering, uml]
fe_section: テクノロジ系
fe_subsection: ソフトウェア
fe_order: 70
date: 2026-10-05
last_modified_at: 2026-10-05
---

<style>
.activity-flow {
  margin: 1.2rem 0;
  padding: 1rem;
  border: 1px solid #d8dee4;
  border-radius: 10px;
  text-align: center;
}
.activity-start,
.activity-end {
  width: 1.25rem;
  height: 1.25rem;
  margin: .45rem auto;
  border-radius: 50%;
  background: #24292f;
}
.activity-end {
  box-sizing: border-box;
  border: 4px solid #24292f;
  background: #fff;
}
.activity-action {
  display: inline-block;
  min-width: 11rem;
  padding: .55rem .8rem;
  border: 1px solid #8c959f;
  border-radius: 12px;
  background: #f6f8fa;
}
.activity-arrow {
  margin: .2rem 0;
  font-size: 1.25rem;
}
.activity-branch {
  display: inline-block;
  margin: .2rem auto;
  padding: .55rem .9rem;
  border: 1px solid #8c959f;
  transform: rotate(45deg);
  background: #fff;
}
.activity-branch span {
  display: block;
  transform: rotate(-45deg);
}
.activity-options {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: .7rem;
  max-width: 32rem;
  margin: .7rem auto;
}
.activity-option {
  padding: .65rem;
  border: 1px solid #d8dee4;
  border-radius: 8px;
}
.uml-judge {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: .7rem;
  margin: 1rem 0;
}
.uml-card {
  padding: .8rem;
  border: 1px solid #d8dee4;
  border-radius: 8px;
}
@media (max-width: 600px) {
  .activity-options,
  .uml-judge {
    grid-template-columns: 1fr;
  }
}
</style>

## まず結論

**アクティビティ図（activity diagram）**は、処理や業務の**実行順序・条件分岐・並行処理などの流れ**を表すUML図です。

FEの科目Aでは、問題文に次のような表現があれば有力候補になります。

> **「処理の流れ」「実行順序」「条件による分岐」「ワークフロー」→ アクティビティ図**

図の名前だけを暗記するより、**何を表したい図なのか**で判断するのがポイントです。

## 直感的な説明

アクティビティ図は、処理の流れを追う図です。

例えば、注文を受けて在庫を確認する業務を考えてみます。

<div class="activity-flow">
  <div class="activity-start" aria-label="開始"></div>
  <div class="activity-arrow">↓</div>
  <div class="activity-action">注文を受ける</div>
  <div class="activity-arrow">↓</div>
  <div class="activity-branch"><span>在庫？</span></div>
  <div class="activity-options">
    <div class="activity-option"><strong>あり</strong><br>↓<br>出荷する</div>
    <div class="activity-option"><strong>なし</strong><br>↓<br>入荷を待つ</div>
  </div>
  <div class="activity-arrow">↓</div>
  <div class="activity-end" aria-label="終了"></div>
</div>

見るべきなのは、

~~~text
何をする？
↓
次に何をする？
↓
条件によってどちらへ進む？
~~~

という**動き**です。

フローチャートに似ていますが、アクティビティ図はUMLで処理や業務の流れをモデル化するときに使います。

## 定義・仕組み

アクティビティ図はUML（Unified Modeling Language）の図の一つで、アクティビティの流れを表します。

代表的な要素として、

- 開始
- アクション（処理）
- 制御フロー
- 判断・分岐
- 合流
- 終了

などがあります。

例えば、

~~~text
開始
 ↓
申請を受け付ける
 ↓
内容を確認する
 ↓
承認できる？
 ├─ Yes → 承認する
 └─ No  → 差し戻す
 ↓
終了
~~~

のように、処理の順序と条件による進み方を表せます。

### ビジネスでもプログラムでも使える

アクティビティ図は、プログラム内部の処理だけを表す図ではありません。

~~~text
業務プロセス
  → 申請 → 審査 → 承認

プログラム処理
  → 入力 → 判定 → 出力
~~~

どちらも「処理の流れ」という共通点があります。

そのため、**ビジネスモデリングでワークフローを表したい**という場面でも候補になります。

## 科目Aでどう出る？

科目Aでは、複数のUML図から目的に合うものを選ばせる問題に注意します。

まず、図の見た目より**何を表すか**を読み取ります。

<div class="uml-judge">
  <div class="uml-card"><strong>処理・業務の流れ</strong><br>→ アクティビティ図</div>
  <div class="uml-card"><strong>ある時点の具体的なオブジェクト</strong><br>→ オブジェクト図</div>
  <div class="uml-card"><strong>クラス・属性・クラス間の関係</strong><br>→ クラス図</div>
  <div class="uml-card"><strong>ソフトウェア部品・依存関係</strong><br>→ コンポーネント図</div>
</div>

| 問題文で注目する表現 | 選ぶ図 |
|---|---|
| 実行順序、条件分岐、ワークフロー | **アクティビティ図** |
| 特定時点のインスタンス間の関係 | オブジェクト図 |
| クラス、属性、クラス間の関係 | クラス図 |
| コンポーネント、部品、依存関係 | コンポーネント図 |

試験中は、

> **「何という図か？」ではなく「何を表したいのか？」**

と考えると選択肢を切りやすくなります。

## どんな場面で使う？

アクティビティ図は、処理や業務の流れを整理したい場面に向いています。

例えば、

- 注文から出荷までの業務フロー
- 申請から承認までのワークフロー
- ユーザー登録処理
- 条件によって処理が変わるプログラム
- 複数の処理が並行して進む流れ

などです。

「誰が何を持っているか」という静的な構造よりも、**時間とともに処理がどう進むか**を見たいときに使う、と考えると分かりやすいです。

## よくある誤解・混同

### 誤解1：クラス図も矢印があるので処理の流れを表す

クラス図の線や矢印は、基本的にクラス間の関係を表します。

~~~text
アクティビティ図
→ 処理がどう進むか

クラス図
→ システムがどんなクラスで構成されるか
~~~

**動きか、構造か**で切り分けます。

### 誤解2：オブジェクト図はオブジェクトの動きを表す

名前に「オブジェクト」とありますが、オブジェクト図は主に**ある時点での具体的なインスタンスとその関係**を表す静的な図です。

~~~text
処理の流れ
→ アクティビティ図

ある時点の具体例
→ オブジェクト図
~~~

### 誤解3：コンポーネント図は処理を部品ごとに並べる図

コンポーネント図の中心は、処理順序ではなく**ソフトウェアを構成する部品とその依存関係**です。

~~~text
順番・分岐
→ アクティビティ図

部品・依存関係
→ コンポーネント図
~~~

### 誤解4：アクティビティ図はプログラム専用

アクティビティ図は、プログラムの制御フローだけでなく**ビジネスプロセスや業務ワークフロー**のモデル化にも利用できます。

問題文に「ビジネスモデリング」と書かれていても、それだけで候補から外さないようにします。

## まとめ（試験直前用）

- アクティビティ図は、**処理・業務の流れを表すUML図**
- **実行順序・条件分岐・ワークフロー**が重要なキーワード
- オブジェクト図は具体的なインスタンス、クラス図はクラス構造、コンポーネント図は部品と依存関係
- 試験では図の名前より、**「何を表したい？」で選ぶ**
- ビジネスプロセスにもプログラムの処理にも利用できる

公式の出題範囲やシラバスは、[IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html) から確認できます。

{% include fe_article_footer.html %}
