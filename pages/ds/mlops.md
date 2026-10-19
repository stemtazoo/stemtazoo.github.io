---
layout: page
title: MLOpsとは？学習・評価・配備・監視の更新サイクル【DS検定】
description: "MLOpsを、需要予測モデルの更新サイクルで説明します。データ・コード・モデルの版管理、評価条件、配備と切り戻し、CI・CD・継続的トレーニングの役割を整理します。"
permalink: /ds/mlops/
categories: [ai-utilization]
tags: [ds, environment-setup, ai-use]
ds_area: dataengineering
ds_section: environment-setup
prev: /ds/llm-temperature/
next: /ds/sora-ame-kasa/
last_modified_at: 2026-10-19
---

<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**MLOpsは、機械学習システムの開発と運用をつなぎ、モデルを継続して評価・配備・維持管理する取り組み**です。「再学習する」だけでなく、何を使って作り、何を確かめて更新したかを追えることが大切です。

IT障害の分析との判別は、[AIOpsとMLOpsの場面比較](/ds/aiops-mlops-cheatsheet/)で確認できます。

## 直感的な説明

需要予測モデルv1が、新商品の増加で外れやすくなったとします。すぐに最新データで学習して上書きすると、「一部の商品だけ悪化した」「元に戻せない」という問題が起きます。

そこでデータとコードの版を記録し、候補v2を同じ条件で比較してから配備します。更新後も監視し、問題があればv1へ戻せるようにします。

## 定義・仕組み

| 段階 | 需要予測の例 | 残す情報・確認すること |
|---|---|---|
| データ管理 | 対象期間の売上を確定 | データの版、欠損、予測時点で使える項目 |
| 学習・実験 | 特徴量と設定を変えて候補を作る | コード・設定・モデルの版 |
| 評価 | 現行版と候補版の誤差を比較 | 同じ評価条件、商品群別の性能 |
| 配備 | 合格した候補をサービスへ反映 | 互換性、配備対象、切り戻し先 |
| 監視 | 入力分布と予測・実績を調べる | データ品質、誤差、応答時間 |
| 見直し | 必要なら再学習して再評価 | 劣化の原因と更新の根拠 |

正解が後で分かる場合、性能評価には時間差があります。入力分布が変わっただけで「性能が必ず低下した」とは断定しません。

### CI・CD・継続的トレーニング

- **CI**：コード変更時などに、テストやデータ・モデルの検証を行う。
- **CD**：検証したパイプラインやモデルを配備する流れを整える。
- **継続的トレーニング（CT）**：新しいデータなどをきっかけに再学習を回す。

自動化の程度は段階的に高められます。すべてを無人化しないとMLOpsではない、という意味ではありません。

## どんな場面で使う？

本番で使う需要予測、推薦、異常検知などを継続して更新するときに役立ちます。再現性や版管理は実験段階から有用ですが、一度だけの分析レポートに運用パイプライン一式が必要とは限りません。

予測サービスの基盤監視も管理対象です。IT障害の調査にAIを使うなら、[AIOpsの仕組み](/ds/aiops/)と併用できます。

## よくある誤解・混同

### 定期的に再学習すれば品質を維持できる？

不良データでの再学習や、全体平均だけの評価は危険です。再学習後も評価し、条件を満たした候補だけを配備します。

### オフライン評価で良ければ、そのまま全利用者へ公開？

実環境の入力・処理速度・接続先なども確認します。段階的な反映や切り戻しを用意し、本番の動作も見ます。

### 「モデル監視」はAIOps？

予測誤差やデータ品質からモデルの維持管理を行うのはMLOpsの文脈です。監視という語だけで分類しません。

## まとめ（試験直前用）

- MLOpsはMLシステムの開発と継続運用をつなぐ。
- データ・コード・モデルの版を追えるようにする。
- 学習だけでなく、評価・配備・監視・切り戻しを考える。
- 再学習と本番への採用は別の判断。

## 公式情報・参考リンク

- [Google Cloud：MLOpsの継続的デリバリーと自動化](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)
  - CI・CD・CTと、データ・モデルの検証を含む運用段階を確認できます。

## 対応スキル項目（ver.6 データエンジニアリング）

- **分類**：AIエンジニアリング
- **スキルカテゴリ**：AIシステム運用
- **サブカテゴリ**：MLOps
- **必須スキル**：—
- ★ MLOpsの概要を理解し、AIモデル性能の維持管理作業の基本的な流れを説明できる
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
