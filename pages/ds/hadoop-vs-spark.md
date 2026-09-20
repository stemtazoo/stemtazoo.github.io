---
layout: page
title: HadoopとSparkの違いとは？（分散処理基盤の比較）【DS検定リテラシー】
description: "HadoopとSparkの違いを、Hadoop MapReduceの分散バッチ処理と、Sparkのデータ再利用・インメモリ処理の特徴から整理します。DS検定で問われる用途、反復処理、HDFSとの関係、選択肢の見分け方を解説します。"
permalink: /ds/hadoop-vs-spark/
categories: [data-engineering]
tags: [ds, data-storage, data-processing]
ds_area: dataengineering
ds_section: data-storage
prev: /ds/hadoop/
next: /ds/hdfs/
last_modified_at: 2026-09-20
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

DS検定では、**Hadoop MapReduceは大規模なバッチ処理、Sparkはデータを保持・再利用する反復処理や高速な分散処理に強い**と整理すると判断しやすくなります。

ただし、

```text
Hadoop ＝ ディスクだけ
Spark ＝ メモリだけ
```

と覚えるのは正確ではありません。

Sparkはデータをメモリに保持して再利用できますが、ストレージも利用できます。また、SparkはHDFS上のデータを読み込んで処理することもできます。


## 直感的な説明

イメージで考えましょう。

### Hadoop（MapReduce）
処理の区切りごとに結果を受け渡しながら、大量データを複数台で処理するイメージです。

### Spark
一度作った分散データを保持して、次の処理でも再利用できるイメージです。

たとえるなら、

```text
MapReduce
→ 処理のたびに資料を棚へ戻しながら進める

Spark
→ よく使う資料を机に置いたまま次の作業へ進める
```

という違いです。

DS検定では、**反復して同じデータを使う処理かどうか**に注目すると切り分けやすくなります。


## 定義・仕組み

### Hadoop（MapReduce）

- HDFSなどに保存された大量データを分散処理する
- MapとReduceの段階で処理を分ける
- 大規模なバッチ処理に向く

### Spark

- 分散データを複数ノードで並列処理する
- RDDなどをメモリへ保持して再利用できる
- 同じデータを何度も使う反復処理に向く
- HDFSなど、Hadoopが対応するストレージのデータも扱える

Apache Sparkの公式RDD Programming Guideでも、RDDはクラスタ上に分散されたデータ集合であり、メモリへ保持して効率よく再利用できることが説明されています。

### 1次情報

- [Apache Hadoop：MapReduce Tutorial](https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)
- [Apache Hadoop：HDFS Architecture](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html)
- [Apache Spark：RDD Programming Guide](https://spark.apache.org/docs/latest/rdd-programming-guide.html)
- [Apache Spark：Structured Streaming Programming Guide](https://spark.apache.org/docs/latest/streaming/index.html)

この公式資料からも、Sparkは単純に「Hadoopの代わりの保存基盤」ではなく、HDFSなどの外部ストレージ上のデータを処理できる分散処理エンジンとして理解する方が安全です。


## どんな場面で使う？

### Hadoop MapReduceが向く場面

- 夜間の大量ログ一括集計
- 大規模なバッチ処理
- MapとReduceで表現しやすい集計処理


### Sparkが向く場面

- 機械学習の学習処理
- 反復計算
- ストリーミング処理
- 低レイテンシ処理

DS検定では、**「反復計算」「インメモリ」「データを保持して再利用」**と書いてあればSpark寄りです。


## よくある誤解・混同

### ① Hadoop＝古いから使われない？

そうとは限りません。

HadoopはHDFSやYARNなども含むエコシステムです。SparkはHDFS上のデータを扱ったり、YARN上で動作したりすることもできるため、「HadoopかSparkか」の二者択一だけで考えない方が安全です。


### ② HadoopとSparkは競合？

実際には組み合わせることもあります。  
HDFS上でSparkを動かすことも可能です。


### ③ MapReduceとSparkを「ディスク対メモリ」だけで覚える

試験では分かりやすい対比ですが、厳密には単純化しすぎです。

```text
MapReduce
→ MapとReduceを中心に段階的に処理する

Spark
→ 分散データを保持・再利用しながら処理できる
```

**何を保存するかではなく、処理の進め方とデータ再利用のしやすさ**を見ると混同しにくくなります。


## まとめ（試験直前用）

- Hadoop MapReduceは、大規模なバッチ処理で使われる分散処理モデル  
- Sparkは、分散データを保持・再利用しやすい分散処理エンジン  
- 反復計算やデータ再利用が多い処理はSparkと相性が良い  
- HDFSとSparkは組み合わせて使える  
- **「Hadoop＝ディスクだけ、Spark＝メモリだけ」と丸暗記しない**  
- 「反復」「インメモリ」「再利用」→ Sparkを疑う


## 対応スキル項目（ver.6 データエンジニアリング）

- **分類**：データエンジニアリング
- **スキルカテゴリ**：データ蓄積
- **サブカテゴリ**：分散技術
- **必須スキル**：—
- ★ HadoopやSparkの分散技術の基本的な仕組みと構成を理解している
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
