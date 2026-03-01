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
    subsections:
      - title: "数学的理解"
        items:
            - /ds/vector-dot-product/
            - /ds/e-calculus/
            - /ds/matrix-multiplication/
            - /ds/inverse-matrix/
            - /ds/eigenvalue/
            - /ds/symmetric-difference/
            - /ds/euclidean-norm/
      - title: "科学的解析の基礎"
        items:
            - /ds/quartile/
            - /ds/sample-variance-unbiased-variance/
            - /ds/pearson-correlation/
            - /ds/covariance-and-correlation/
            - /ds/variance-and-standard-deviation/

  - title: "データエンジニアリング力"
    subsections:
      - title: "環境構築"
        items:
          - /ds/mean-median-mode/
          - /ds/variance-standard-deviation/
          - /ds/distribution/
          - /ds/histogram-boxplot/

      - title: "データ構造"
        items:
          - /ds/probability-basics/
          - /ds/conditional-probability/
          - /ds/bayes-theorem/
          - /ds/normal-distribution/
          - /ds/binomial-distribution/
          - /ds/poisson-distribution/

      - title: "データ蓄積"
        items:
          - /ds/sampling/
          - /ds/hypothesis-testing/
          - /ds/p-value/
          - /ds/confidence-interval/
          - /ds/correlation-vs-causation/

  - title: "AI利活用スキル"
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

## DS検定 公式リンク

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin-top:12px;">
  <a href="https://www.datascientist.or.jp/dscertification/what/#summary" target="_blank" rel="noopener noreferrer" style="display:block;padding:18px;border-radius:14px;text-decoration:none;background:linear-gradient(135deg,#0f172a,#1d4ed8);color:#fff;box-shadow:0 10px 25px rgba(15,23,42,.18);transition:transform .2s ease,box-shadow .2s ease;">
    <div style="font-size:12px;opacity:.8;letter-spacing:.06em;">OFFICIAL</div>
    <div style="margin-top:8px;font-size:18px;font-weight:700;line-height:1.45;">DS検定とは（概要）</div>
    <div style="margin-top:10px;font-size:14px;opacity:.92;">試験の目的・対象者・出題範囲を公式情報で確認できます。</div>
  </a>

  <a href="https://www.datascientist.or.jp/news/n-pressrelease/post-1757/" target="_blank" rel="noopener noreferrer" style="display:block;padding:18px;border-radius:14px;text-decoration:none;background:linear-gradient(135deg,#0b3b2e,#0ea5a5);color:#fff;box-shadow:0 10px 25px rgba(11,59,46,.18);transition:transform .2s ease,box-shadow .2s ease;">
    <div style="font-size:12px;opacity:.8;letter-spacing:.06em;">PRESS RELEASE</div>
    <div style="margin-top:8px;font-size:18px;font-weight:700;line-height:1.45;">DS検定 関連ニュース</div>
    <div style="margin-top:10px;font-size:14px;opacity:.92;">最新の発表内容や公式アナウンスをチェックできます。</div>
  </a>
</div>

---

## 目次

- [基礎理解](#基礎理解)
- [統計・確率](#統計確率)
- [可視化・分析](#可視化分析)
- [ビジネス・倫理](#ビジネス倫理)
- [試験対策](#試験対策)

---

## 基礎理解

## データサイエンス力
{% assign sec = page.ds_sections | where: "title", "データサイエンス力" | first %}
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

## 未分類（ds_sections未登録）

{% assign classified_urls = "" | split: "" %}
{% for sec in page.ds_sections %}
  {% if sec.items %}
    {% for item_url in sec.items %}
      {% assign classified_urls = classified_urls | push: item_url %}
    {% endfor %}
  {% endif %}

  {% if sec.subsections %}
    {% for subsection in sec.subsections %}
      {% if subsection.items %}
        {% for item_url in subsection.items %}
          {% assign classified_urls = classified_urls | push: item_url %}
        {% endfor %}
      {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}

<ul>
  {% for p in site.pages %}
    {% if p.url contains '/ds/' %}
      {% unless classified_urls contains p.url or p.url == page.url %}
        <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a>（{{ p.url }}）</li>
      {% endunless %}
    {% endif %}
  {% endfor %}
</ul>
