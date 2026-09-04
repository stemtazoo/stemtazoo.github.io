---
layout: page
title: YARNとは？Hadoopクラスタのリソース管理の仕組み【DS検定】
description: "YARNを、HadoopクラスタのCPU・メモリを管理し、複数の処理へ実行資源を割り当てる基盤として整理します。HDFSは保存、YARNはリソース管理、SparkやMapReduceは処理という役割の違いを押さえ、DS検定で選択肢を切る判断基準を確認します。"
permalink: /ds/yarn/
categories: [data-engineering]
tags: [ds, data-storage, data-processing]
ds_area: dataengineering
ds_section: data-storage
prev: /ds/web-api/
next: /ds/docker/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

YARN（Yet Another Resource Negotiator）とは、**Hadoopクラスタ全体のCPU・メモリなどの計算資源を管理し、処理へ割り当てる仕組み**です。

DS検定では、次の役割分担で切り分けると迷いにくくなります。

| 技術 | 主な役割 |
|---|---|
| HDFS | データを分散保存する |
| YARN | CPU・メモリなどのリソースを管理する |
| Spark / MapReduce | 実際のデータ処理を行う |

**保存 = HDFS / 管理 = YARN / 処理 = Spark・MapReduce** が基本です。

## 直感的な説明

複数のサーバーでビッグデータを処理すると、次のような調整が必要になります。

- どのサーバーが空いているか
- どの処理へCPUやメモリを割り当てるか
- 複数の処理が同時に走るとき、どう競合を避けるか

この「クラスタの交通整理」を担当するのがYARNです。

> YARN = 計算資源の割り当てを管理する司令塔

と考えるとイメージしやすくなります。

## 定義・仕組み

YARNは、Hadoopクラスタで**計算リソースとジョブ実行を管理する基盤**です。

### ① リソースを管理する

クラスタ全体のCPUやメモリを把握し、処理へ割り当てます。

### ② ジョブを実行できる場所へ割り当てる

SparkやMapReduceなどの処理が送られると、利用可能な計算資源を確保して実行を調整します。

### ③ クラスタの状態を監視する

各ノードの状態や実行中の処理を監視し、クラスタ全体を管理します。

YARNを構成する代表的な役割も押さえておくと整理しやすくなります。

| 構成要素 | 役割 |
|---|---|
| ResourceManager | クラスタ全体のリソースを管理 |
| NodeManager | 各ノードのリソースや処理を管理 |
| ApplicationMaster | アプリケーション単位で実行を調整 |

## どんな場面で使う？

YARNは、Hadoopクラスタ上で複数の処理を動かすときに使われます。

- MapReduceのジョブを実行する
- Sparkの処理へ計算資源を割り当てる
- 複数のジョブでCPUやメモリを共有する

重要なのは、**YARN自身がデータを保存したり、分析計算そのものを行ったりするわけではない**ことです。

## よくある誤解・混同

### ❌ YARNはデータを保存する

データ保存はHDFSの役割です。

### ❌ YARNがデータ処理を実行する

YARNは実行資源を管理します。実際の処理を担当するのはSparkやMapReduceなどです。

### ❌ HDFS・YARN・Sparkは同じ役割

| 問題文のキーワード | 判断 |
|---|---|
| 分散保存・ブロック・レプリケーション | HDFS |
| CPU・メモリ・資源割当て・ジョブ管理 | YARN |
| 集計・変換・計算・データ処理 | Spark / MapReduce |

## まとめ（試験直前用）

- **YARN = Hadoopクラスタのリソース管理**
- CPU・メモリなどを処理へ割り当てる
- HDFSはデータ保存
- Spark / MapReduceはデータ処理
- 問題文に「資源割当て」「ジョブ管理」があればYARNを疑う

## 対応スキル項目（データエンジニアリング力シート）

- スキルカテゴリ名：データ蓄積
- サブカテゴリ名：分散技術
- ★ Hadoop・Sparkの分散技術の基本的な仕組みと構成を理解している

{% include ds_article_footer.html %}
