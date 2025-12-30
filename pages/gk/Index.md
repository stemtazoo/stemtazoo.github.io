---
layout: page
title: G検定 用語集
permalink: /gk/
tags: [gk]
# 表示順はここで固定（/gk/〇〇/ ＝ pages/gk/〇〇.md）
gk_sections:   
  - title: "人工知能（AI）とは"
    items:
      - /gk/ai-booms-cheatsheet/
      - /gk/second-ai-boom/
  
  - title: "人工知能をめぐる動向"
    items:
      - /gk/classical-ai/
      - /gk/knowledge-representation/
      - /gk/classical-ai-vs-ml/
      - /gk/concepts-final-cheatsheet/
      - /gk/perceptron/
      - /gk/mlp/
      - /gk/activation-functions/
      - /gk/backpropagation/
      - /gk/optimizers/
      - /gk/regularization/
      - /gk/batch-epoch/
  
  - title: "機械学習の概要"
    subsections:
      - title: "代表的な手法"
        items:
          - /gk/supervised-learning/
          - /gk/unsupervised-learning/
          - /gk/reinforcement-learning/
          - /gk/learning-types-comparison/
  
      - title: "モデルの選択・評価"
        items:
          - /gk/confusion-matrix/
          - /gk/accuracy/
          - /gk/precision/
          - /gk/recall/
          - /gk/f1-score/
          - /gk/roc-auc/
          - /gk/precision-recall-curve/
          - /gk/metrics-summary/
          - /gk/rmse-mae/
          - /gk/regression-metrics-cheatsheet/
          - /gk/regression-vs-classification/
  
      - title: "よくあるつまずき（過学習など）"
        items:
          - /gk/overfitting/
          - /gk/underfitting/
          - /gk/learning-curve/
          - /gk/bias-variance-tradeoff/
        
  - title: "ディープラーニングの概要"
    items:
      - /gk/leaky-relu/
      - /gk/relu-family-cheatsheet/
      - /gk/activation-derivative/
      - /gk/gradient-vanishing-exploding/
      - /gk/momentum/
      - /gk/adam/
      - /gk/optimization-cheatsheet/
      - /gk/learning-rate-scheduling/
      - /gk/regularization/
      - /gk/pruning/
      - /gk/model-compression/
        
  - title: "ディープラーニングの要素技術"
    items:
      - /gk/cnn/
      - /gk/convolution/
      - /gk/pooling/
      - /gk/cnn-models/
      - /gk/dilated-convolution/
      - /gk/pooling-stride-dilation/
      - /gk/encoder-decoder/
      - /gk/lstm-cec/
      - /gk/rnn/
      - /gk/vanishing-exploding-gradient/
      - /gk/lstm/
      - /gk/gru/
      - /gk/attention/
      - /gk/transformer/
      - /gk/embedding-word2vec/

  - title: "ディープラーニングの応用例"
    items:
      - /gk/ssd/
      - /gk/faster-r-cnn/
      - /gk/yolo/
      - /gk/rcnn-fast-rcnn/
      - /gk/anchor-defaultbox-rpn/
      - /gk/object-detection-summary/
      - /gk/segnet/
      - /gk/u-net/
      - /gk/fcn/
      - /gk/segmentation-cheatsheet/
      - /gk/xai-explainability/
      - /gk/efficientnet/
      - /gk/cam-grad-cam/
      - /gk/xai-summary/
      - /gk/lime-vs-shap/
      - /gk/image-open-datasets/
      - /gk/squad/
      - /gk/dcgan/
      - /gk/gan-variants/
      - /gk/gan-vs-vae/
      - /gk/diffusion-model/
      - /gk/stable-diffusion/
      - /gk/cnn-output-size/
      - /gk/cnn-calculation-cheatsheet/
      - /gk/cnn-trick-calculations/
      - /gk/pooling-trick-calculations/
      - /gk/cnn-cheatsheet/
      - /gk/cnn-vs-transformer/
      - /gk/cnn-architectures-comparison/
      - /gk/image-tasks-summary/
      - /gk/timbre-mfcc/
      - /gk/cnn-convolution/

  - title: "AIの社会実装に向けて"
    items:
      - /gk/edge-ai/
      - /gk/edge-vs-cloud-ai/
      - /gk/crisp-dm/
      - /gk/crisp-dm-vs-ml-pipeline/
        
  - title: "AIの法律と倫理"
    items:
      - /gk/fairness-bias/
      - /gk/privacy-data-protection/
      - /gk/safety-robustness/
      - /gk/ai-governance/
      - /gk/pseudonymized-information/
      - /gk/anonymized-information/
      - /gk/personal-information-law/
      - /gk/personal-information-protection-law-cheatsheet/
      - /gk/ai-ethics/
        
  - title: "チートシート（試験直前）"
    items:
      - /gk/nn-cheatsheet/
      - /gk/nn-final-cheatsheet/
      - /gk/search-vs-ml-cheatsheet/
      - /gk/ai-ethics-cheatsheet/
      - /gk/speech-recognition-cheatsheet/
        
  - title: "ひっかけ問題集"
    items:
      - /gk/trick-questions-1/
      - /gk/trick-questions-xai-1/
---

{% comment %}
  gk_sections に書いた URL から対応する page を引く
  見つからない場合は赤字で表示（permalink/url の不一致検出）
{% endcomment %}

## 技術分野

## 人工知能とは
{% assign sec = page.gk_sections | where: "title", "人工知能（AI）とは" | first %}
{% include gk_section.html sec=sec %}

## 人工知能をめぐる動向
{% assign sec = page.gk_sections | where: "title", "人工知能をめぐる動向" | first %}
{% include gk_section.html sec=sec %}

## 機械学習の概要
{% assign ml = page.gk_sections | where: "title", "機械学習の概要" | first %}
{% include gk_section.html sec=ml %}

## ディープラーニングの概要
{% assign sec = page.gk_sections | where: "title", "ディープラーニングの概要" | first %}
{% include gk_section.html sec=sec %}

## ディープラーニングの要素技術
{% assign sec = page.gk_sections | where: "title", "ディープラーニングの要素技術" | first %}
{% include gk_section.html sec=sec %}

## ディープラーニングの応用例
{% assign sec = page.gk_sections | where: "title", "ディープラーニングの応用例" | first %}
{% include gk_section.html sec=sec %}

## AIの社会実装に向けて
{% assign sec = page.gk_sections | where: "title", "AIの社会実装に向けて" | first %}
{% include gk_section.html sec=sec %}

---

## 法律・倫理分野

## AI倫理・AIガバナンス
{% assign sec = page.gk_sections | where: "title", "AIの法律と倫理" | first %}
{% include gk_section.html sec=sec %}

## チートシート（試験直前）
{% assign sec = page.gk_sections | where: "title", "チートシート（試験直前）" | first %}
{% include gk_section.html sec=sec %}

## ひっかけ問題集
{% assign sec = page.gk_sections | where: "title", "ひっかけ問題集" | first %}
{% include gk_section.html sec=sec %}

