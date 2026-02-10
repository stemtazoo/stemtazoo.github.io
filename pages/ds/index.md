---
layout: page
title: DS検定 リテラシー 学習まとめ
permalink: /ds/
tags: [ds]

# 表示順はここで固定（/ds/〇〇/ ＝ pages/ds/〇〇.md）
ds_sections:
  - title: "ビジネス力"
    items:
      - /ds/data-science-overview/
      - /ds/data-driven-decision/
      - /ds/descriptive-predictive-prescriptive/
      - /ds/ds-role/

  - title: "データサイエンス力"
    items:
      - /ds/vector-dot-product/
      - /ds/structured-vs-unstructured/
      - /ds/missing-values/
      - /ds/outliers/
      - /ds/data-cleaning/
      - /ds/normalization-standardization/
      - /ds/train-test-split/

  - title: "統計・確率の基礎"
    subsections:
      - title: "記述統計"
        items:
          - /ds/mean-median-mode/
          - /ds/variance-standard-deviation/
          - /ds/distribution/
          - /ds/histogram-boxplot/

      - title: "確率と分布"
        items:
          - /ds/probability-basics/
          - /ds/conditional-probability/
          - /ds/bayes-theorem/
          - /ds/normal-distribution/
          - /ds/binomial-distribution/
          - /ds/poisson-distribution/

      - title: "推測統計"
        items:
          - /ds/sampling/
          - /ds/hypothesis-testing/
          - /ds/p-value/
          - /ds/confidence-interval/
          - /ds/correlation-vs-causation/

  - title: "データ可視化"
    items:
      - /ds/visualization-purpose/
      - /ds/bar-line-scatter/
      - /ds/when-to-use-which-graph/
      - /ds/misleading-visualization/

  - title: "分析手法の理解"
    items:
      - /ds/regression-overview/
      - /ds/linear-regression/
      - /ds/logistic-regression/
      - /ds/clustering-overview/
      - /ds/k-means/
      - /ds/classification-vs-regression/

  - title: "評価と解釈"
    items:
      - /ds/confusion-matrix/
      - /ds/accuracy-precision-recall/
      - /ds/f1-score/
      - /ds/overfitting-underfitting/
      - /ds/bias-variance/

  - title: "ビジネス活用・プロセス"
    items:
      - /ds/crisp-dm/
      - /ds/problem-definition/
      - /ds/kpi-metric/
      - /ds/eda/
      - /ds/communication/

  - title: "法律・倫理・データリテラシー"
    items:
      - /ds/personal-data/
      - /ds/privacy/
      - /ds/data-ethics/
      - /ds/bias-fairness/
      - /ds/security/

  - title: "試験対策"
    items:
      - /ds/skillcheck/
      - /ds/business-skillcheck/
      - /ds/engineering-skillcheck/
      - /ds/ai-utilization-skillcheck/
      - /ds/cheatsheet/
      - /ds/trick-questions/
---

{% comment %}
  ds_sections に書いた URL から対応する page を引く
  見つからない場合は赤字で表示
{% endcomment %}

## まずどこから？

- はじめて：**データサイエンスとは → 統計・確率の基礎**
- 実務視点：**データ前処理 → 可視化 → 分析**
- 試験直前：**チートシート → ひっかけ問題集**

---

## 目次

- [基礎理解](#基礎理解)
- [統計・確率](#統計確率)
- [可視化・分析](#可視化分析)
- [ビジネス・倫理](#ビジネス倫理)
- [試験対策](#試験対策)

---

## 基礎理解

## データサイエンスとは
{% assign sec = page.ds_sections | where: "title", "データサイエンスとは" | first %}
{% include ds_section.html sec=sec %}

## データの扱いと前処理
{% assign sec = page.ds_sections | where: "title", "データの扱いと前処理" | first %}
{% include ds_section.html sec=sec %}

---

## 統計・確率

## 統計・確率の基礎
{% assign sec = page.ds_sections | where: "title", "統計・確率の基礎" | first %}
{% include ds_section.html sec=sec %}

---

## 可視化・分析

## データ可視化
{% assign sec = page.ds_sections | where: "title", "データ可視化" | first %}
{% include ds_section.html sec=sec %}

## 分析手法の理解
{% assign sec = page.ds_sections | where: "title", "分析手法の理解" | first %}
{% include ds_section.html sec=sec %}

---

## ビジネス倫理

## ビジネス活用・プロセス
{% assign sec = page.ds_sections | where: "title", "ビジネス活用・プロセス" | first %}
{% include ds_section.html sec=sec %}

## 法律・倫理・データリテラシー
{% assign sec = page.ds_sections | where: "title", "法律・倫理・データリテラシー" | first %}
{% include ds_section.html sec=sec %}

---

## 試験対策

## チートシート（試験直前）
{% assign sec = page.ds_sections | where: "title", "試験対策" | first %}
{% include ds_section.html sec=sec %}

---

## 未分類（ds_section未設定）

<ul>
  {% for p in site.pages %}
    {% if p.url contains '/ds/' and p.ds_section == nil %}
      {% unless p.url == page.url %}
        <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a>（{{ p.url }}）</li>
      {% endunless %}
    {% endif %}
  {% endfor %}
</ul>
