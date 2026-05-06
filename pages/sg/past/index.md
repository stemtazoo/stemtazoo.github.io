---
layout: page
title: "SG公式過去問"
description: "情報セキュリティマネジメント試験（SG）のIPA公式公開問題を，PDFを見ながら回答・採点・解説確認できるページです。"
permalink: /sg/past/
tags: [sg, sg-past-exam]
last_modified_at: 2026-05-06
---

## SG公式過去問

IPAが公開している情報セキュリティマネジメント試験（SG）の公開問題を，公式PDFを見ながら解けるページです。

問題文・図表はIPA公式PDFを参照し，このサイトでは回答欄，正解表示，学習用の解説を用意しています。

## 年度別ページ

<div class="sg-past-year-list">
{% for exam in site.data.sg_past %}
  <article class="sg-past-year">
    <h3><a href="{{ exam.permalink | relative_url }}">{{ exam.short_label }} 公開問題</a></h3>
    <p>{{ exam.source_note }}</p>
    <p class="sg-past-links">
      <a href="{{ exam.official_page }}">公式ページ</a>
      <a href="{{ exam.question_pdf }}">問題冊子PDF</a>
      <a href="{{ exam.answer_pdf }}">解答例PDF</a>
    </p>
  </article>
{% endfor %}
</div>

## 出典と利用上の注意

本ページ群は，IPAが公開している情報セキュリティマネジメント試験の公開問題を学習しやすくするためのページです。問題冊子・解答例の著作権はIPAに帰属します。解説は当サイト独自の学習用説明です。

<p><a href="{{ '/sg/' | relative_url }}">SGトップへ戻る</a></p>
