---
layout: page
title: HadoopとSparkの違いとは？HDFS・MapReduce・Kafka・Stormまで整理【基本情報技術者試験】
description: HadoopとSparkを「どちらも分散処理」という共通点から一段深く整理し、HDFS・MapReduce・Kafka・Stormとの違いをFE試験で選択肢を切れる形で解説します。
permalink: /fe/hadoop-spark/
tags: [fe, fe-technology, database, big-data]
fe_section: テクノロジ系
fe_subsection: データベース
fe_order: 24
date: 2026-10-05
last_modified_at: 2026-10-05
---

## まず結論

HadoopとSparkは、どちらも**多数のコンピュータを使って大規模データを分散処理する技術**です。

そのため、「分散処理」という言葉だけでは切り分けられません。

基本情報技術者試験では、次の対応を最初に押さえます。

| キーワード | 判断する技術 |
|---|---|
| **HDFS・MapReduce** | **Hadoop** |
| メモリを活用した高速な分散処理 | Spark |
| 分散メッセージング・イベントストリーム | Kafka |
| リアルタイムのストリーム処理 | Storm |

> **HDFS ＋ MapReduce が見えたら、まずHadoop。**

## 直感的な説明

HadoopとSparkを「どちらが分散処理か」で比べると迷います。**どちらも分散処理だからです。**

一段下の役割を見ると整理できます。

<div class="fe-bigdata-map">
  <div class="fe-tech hadoop">
    <strong>Hadoop</strong>
    <span>大規模データを分散して扱う基盤</span>
    <div class="fe-inner">
      <b>HDFS</b><small>分散して保存</small>
      <b>MapReduce</b><small>分散して処理</small>
    </div>
  </div>
  <div class="fe-tech">
    <strong>Spark</strong>
    <span>高速な分散処理エンジン</span>
    <small>メモリを活用した処理が得意</small>
  </div>
</div>

つまり、試験では次のように考えます。

```text
大規模な分散処理
       ↓
Hadoop？ Spark？
       ↓
HDFS / MapReduce がある？
       ↓ YES
     Hadoop
```

## 定義・仕組み

### Hadoop：分散保存と分散処理の基盤

Apache Hadoopは、大規模なデータを複数のコンピュータに分散して保存・処理するためのソフトウェア群です。

FEで特に重要なのが、次の2つです。

```text
Hadoop
├─ HDFS
│   └─ データを複数ノードに分散して保存
│
└─ MapReduce
    └─ 大規模データを分散して処理
```

HDFS（Hadoop Distributed File System）は**保存**、MapReduceは**処理**と分けて覚えると混乱しにくくなります。

### Spark：高速な分散処理エンジン

Apache Sparkも、大規模データを複数のコンピュータで処理するための分散処理エンジンです。

Hadoop MapReduceとの比較では、Sparkは中間結果などをメモリ上で扱えるため、繰り返し処理などを高速化しやすい点が特徴です。

ここで注意したいのは、

> **HadoopとSparkは、完全な二者択一ではない**

ということです。

SparkはHDFS上のデータを処理することもできます。

したがって、

```text
Hadoop = 分散処理
Spark  = 分散処理ではない
```

という覚え方は誤りです。

### Kafka：データを受け渡す

Apache Kafkaは、イベントやメッセージを継続的に受け取り、複数のシステムへ受け渡すための分散イベントストリーミング基盤です。

試験では、

> **メッセージング・イベントの流れ → Kafka**

と切り分けます。

### Storm：流れてくるデータをリアルタイム処理

Apache Stormは、流れてくるデータを継続的に処理する分散リアルタイム計算システムです。

試験では、

> **リアルタイムのストリーム処理 → Storm**

が判断材料になります。

## 科目Aでどう出る？

今回のような問題では、「OSS」「大規模」「分散」という言葉だけでは選べません。

選択肢にHadoopとSparkが同時にある場合は、**固有のキーワード**を探します。

```text
「多数のサーバ」
       ↓
まだ決まらない

「大規模データの分散処理」
       ↓
HadoopもSparkも候補

「MapReduce」
       ↓
Hadoopが強い

「分散ファイルシステム」
       ↓
HDFS
       ↓
Hadoopで確定
```

この読み方なら、HadoopとSparkを細部まで暗記していなくても選択肢を切れます。

### 4つの選択肢を切る基準

| 問題文に出てきた言葉 | 選ぶ候補 |
|---|---|
| HDFS、MapReduce | **Hadoop** |
| インメモリ、高速な分散処理 | **Spark** |
| メッセージ、イベントの受け渡し | **Kafka** |
| リアルタイム、ストリーム処理 | **Storm** |

## どんな場面で使う？

大量のログデータを扱う場面を例にします。

```text
大量のログ
   ↓
Kafka
データを継続的に受け渡す
   ↓
Spark / Storm など
データを処理する
   ↓
HDFS など
大規模データを分散して保存
```

実際のシステムでは複数の技術を組み合わせることがあります。

そのため、試験でも**「どれが上位・下位か」より、それぞれが何を担当するか**を見る方が安全です。

## よくある誤解・混同

### HadoopとSparkは別カテゴリ

完全に別物として覚える必要はありません。

どちらも大規模データの分散処理に関係します。

まず同じ大きなカテゴリに置き、その後で、

```text
Hadoop → HDFS・MapReduceを含む分散処理基盤
Spark  → 高速な分散処理エンジン
```

と一段細かく分けます。

### SparkはHadoopの代わりだから一緒に使わない

これも正確ではありません。

SparkはHDFSなどHadoopエコシステムの仕組みと組み合わせて利用できます。

### HadoopはMapReduceだけ

HadoopをMapReduceだけだと考えるのも不十分です。

FEでは特に、**HDFSによる分散保存とMapReduceによる分散処理**をセットで押さえると判断しやすくなります。

### 「分散処理」と書いてあればHadoop

Sparkも分散処理を行います。

**分散処理だけでは決めず、HDFS・MapReduceなど追加のキーワードを探す**のが今回の重要な判断基準です。

## まとめ（試験直前用）

- HadoopとSparkは、どちらも大規模データの**分散処理**に関係する
- **HDFS＝分散保存、MapReduce＝分散処理 → Hadoop**
- **高速な分散処理・メモリ活用 → Spark**
- **メッセージ・イベントの受け渡し → Kafka**
- **リアルタイムのストリーム処理 → Storm**
- 「分散処理」だけで決めず、**固有キーワードまで読む**

試験直前は、まずこれだけ思い出します。

> **HDFS ＋ MapReduce → Hadoop**

<style>
.fe-bigdata-map{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1.2rem 0}
.fe-tech{border:1px solid #cbd5da;border-radius:12px;padding:1rem;text-align:center;background:#f8fafb}
.fe-tech>strong,.fe-tech>span,.fe-tech>small{display:block}
.fe-tech>strong{font-size:1.1rem;margin-bottom:.35rem}
.fe-tech>span{margin-bottom:.7rem}
.fe-inner{display:grid;grid-template-columns:auto 1fr;gap:.35rem .7rem;text-align:left;border-top:1px solid #dbe2e6;padding-top:.7rem;margin-top:.5rem}
.fe-inner small{align-self:center}
@media(max-width:600px){.fe-bigdata-map{grid-template-columns:1fr}}
</style>

{% include fe_article_footer.html %}
