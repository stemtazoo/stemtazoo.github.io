---
layout: page
title: MLOpsとは？DevOps・CRISP-ML(Q)との違い【G検定対策】
description: "MLOpsを、機械学習システムを継続的・再現可能に開発・デプロイ・監視・改善するための実践として整理します。DevOpsやCRISP-ML(Q)との違い、CI/CD・継続学習・モデル監視をG検定向けに確認します。"
permalink: /gk/mlops/
tags: [gk, mlops, devops]
gk_section: AIの社会実装に向けて/開発・運用（MLOps）
gk_order: 2
last_modified_at: 2026-09-04
---

## まず結論

**MLOps（Machine Learning Operations）**は、機械学習システムを**継続的・再現可能・安定的に開発、デプロイ、運用、改善するための実践や仕組み**です。

G検定では、**DevOpsの考え方に加えて、データ・モデル・学習そのものも継続管理する**点を押さえます。

## 直感的な説明

普通のソフトウェアでは、主にコードの変更を管理します。

機械学習システムでは、それに加えて、

- 学習データが変わる
- モデルが更新される
- 本番データの傾向が変わる
- モデル性能が変化する

といった要素があります。

そのため、**コードだけでなく、データ・モデル・学習・デプロイ・監視まで継続して管理する**必要があります。

これを実践する考え方がMLOpsです。

## 定義・仕組み

MLOpsでは、たとえば次のような要素を扱います。

- データ・モデル・コードの版管理
- 学習・評価の再現性
- CI/CDによるテストやデプロイの自動化
- **Continuous Training（継続学習）**
- モデルのデプロイ
- 本番環境の監視
- データドリフト・性能変化の確認
- 必要に応じた再学習・再デプロイ

重要なのは、MLOpsが**固定された1つの工程表ではない**ことです。

機械学習のライフサイクルを安定して回すために、プロセス・自動化・管理・監視などを組み合わせます。

### CRISP-ML(Q)との違い

[CRISP-ML(Q)]({{ '/gk/crisp-ml/' | relative_url }})は、機械学習プロジェクトをどのフェーズで進め、各フェーズでどう品質を確保するかを整理する**プロセスモデル**です。

一方、MLOpsは、そのライフサイクルを実際に継続運用するための**実践・自動化・管理の仕組み**に重点があります。

- **CRISP-ML(Q)**：どう進め、どう品質を確保するか
- **MLOps**：どう継続的・再現可能に回すか

両者は競合するものではなく、組み合わせて考えられます。

機械学習プロジェクト全体の入口は、[機械学習プロジェクトの全体像]({{ '/gk/ml-project-lifecycle/' | relative_url }})も参照してください。

## いつ使う？（得意・不得意）

### 特に重要になる場面

- 機械学習モデルを本番で継続利用する
- 複数人でモデルを開発・運用する
- 再学習や再デプロイが発生する
- モデルやデータの履歴を追跡したい
- 手作業による学習・評価・配備のばらつきを減らしたい

### 注意点

MLOpsはモデル精度を直接上げるアルゴリズムではありません。

また、**すべてを自動化することがMLOpsの条件でもありません**。システムやリスクに応じて、自動化する範囲を決めます。

## G検定ひっかけポイント

### DevOpsとの違い

❌ MLOpsとDevOpsは完全に同じ  
⭕ MLOpsでは**データ・モデル・継続学習・モデル性能監視**が特に重要

### CRISP-ML(Q)との違い

❌ CRISP-ML(Q)＝MLOps  
⭕ CRISP-ML(Q)は**プロセスと品質保証の枠組み**、MLOpsは**継続的に開発・運用する実践や仕組み**

### Continuous Training

❌ MLOpsはCI/CDだけ考えればよい  
⭕ MLでは、データやモデルが変わるため**継続学習（CT）**も重要

### 再学習

❌ MLOpsでは必ず自動再学習する  
⭕ 必要に応じて再学習できる仕組みを整える。自動化の程度はシステムによる

## まとめ（試験直前用）

- MLOps＝**MLシステムを継続的・再現可能に開発・運用する実践**
- DevOpsに加え、**データ・モデル・学習**を管理する
- **CI/CD + 継続学習（CT）+ 監視**が重要
- CRISP-ML(Q)はプロセスモデル、MLOpsは実践・仕組み
- 再学習は「必ず自動」ではない

### 参考資料（一次情報）

- Google Cloud, [Practitioners Guide to Machine Learning Operations (MLOps)](https://cloud.google.com/resources/mlops-whitepaper)
- Google Cloud, [MLOps: Continuous delivery and automation pipelines in machine learning](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)

{% include gk_article_footer.html %}
