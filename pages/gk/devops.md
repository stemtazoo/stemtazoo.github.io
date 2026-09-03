---
layout: page
title: DevOpsとは？MLOpsとの違い【G検定対策】
description: "DevOpsを、ソフトウェア開発と運用の連携によって継続的に改善・提供する考え方として整理します。MLOpsとの違いを、データ・モデル管理、継続学習（CT）、モデル監視の観点からG検定向けに確認します。"
permalink: /gk/devops/
tags: [gk, devops, mlops]
gk_section: AIの社会実装に向けて/開発・運用（MLOps）
gk_order: 1
last_modified_at: 2026-09-04
---

## まず結論

**DevOps**は、ソフトウェアの開発と運用が連携し、継続的に改善・提供していくための考え方や実践です。

G検定では、まず

- **DevOps**＝ソフトウェア開発と運用を継続的につなぐ
- **MLOps**＝その考え方を踏まえつつ、機械学習特有の**データ・モデル・再学習・性能監視**まで扱う

と切り分けます。

## 直感的な説明

DevOpsは、

- 開発チームが作る
- 運用チームへ渡して終わり

ではなく、**開発と運用が一緒に改善を回す**考え方です。

一方、機械学習システムでは、コードだけでなく**学習データやモデルそのものも変化する**ため、通常のソフトウェア運用とは違う管理が必要になります。

そこを扱うのが[MLOps](/gk/mlops/)です。

## 定義・仕組み

DevOpsでは、次のような要素が重視されます。

- 開発と運用の連携
- 自動テスト
- CI（継続的インテグレーション）
- CD（継続的デリバリー／デプロイ）
- 監視とフィードバック

DevOpsは特定の1つのツールや固定手順ではなく、**文化・考え方・実践の集合**として捉えるのが適切です。

### MLOpsでは何が増える？

MLOpsでは、DevOpsで扱うコードやシステムに加えて、

- 学習データ
- データスキーマ
- モデル
- 実験結果
- モデル性能

なども継続的に管理します。

また、CI/CDだけでなく、必要に応じてモデルを再学習する**CT（Continuous Training：継続学習）**や、入力データ・モデル性能を確認する**継続的な監視**も重要になります。

つまり、**MLOpsはDevOpsを単純に名前だけ置き換えたものではなく、MLシステム特有の変化を扱えるようにした実践**と理解すると分かりやすいです。

## いつ使う？（得意・不得意）

### DevOpsが中心になる場面

- Webサービス
- 業務システム
- 継続的な更新が必要なソフトウェア

### MLOpsが特に重要になる場面

- 学習データが更新される
- モデルを再学習・再デプロイする
- データドリフトやモデル性能を監視する
- データやモデルの変更履歴を追跡する

なお、MLOpsの流れそのものは[MLOpsの流れ](/gk/mlops-process/)で整理しています。

## G検定ひっかけポイント

### DevOps＝MLOps？

❌ 同じもの  
⭕ **MLOpsはDevOpsの考え方を踏まえつつ、ML特有のデータ・モデル管理まで扱う**

### CI/CDだけで十分？

❌ MLOpsもCI/CDだけ考えればよい  
⭕ MLOpsでは**CT（継続学習）やモデル・データの監視**も重要

### 機械学習固有の要素

❌ モデル再学習やデータドリフトはDevOps固有の中心概念  
⭕ **MLOpsで特に重要になる**

## まとめ（試験直前用）

- DevOps＝**開発と運用の連携**
- CI/CDや監視・フィードバックが代表的
- 特定のツール名ではない
- MLOpsではさらに**データ・モデル・CT・性能監視**を扱う
- **DevOpsとMLOpsは同じではないが、無関係でもない**

### 参考資料（一次情報）

- [Google Cloud - DevOps](https://cloud.google.com/devops?hl=ja)
- [Google Cloud - MLOps: Continuous delivery and automation pipelines in machine learning](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)

{% include gk_article_footer.html %}
