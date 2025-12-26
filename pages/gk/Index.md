---
layout: page
title: G検定 用語集
permalink: /gk/
tags: [gk]
# 表示順はここで固定（/gk/〇〇/ ＝ pages/gk/〇〇.md）
gk_sections:
  - title: "機械学習の基本"
    items:
      - /gk/supervised-learning/
      - /gk/unsupervised-learning/
      - /gk/reinforcement-learning/
      - /gk/learning-types-comparison/

  - title: "評価指標（基本）"
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

  - title: "ニューラルネットワーク基礎"
    items:
      - /gk/perceptron/
      - /gk/mlp/
      - /gk/activation-functions/
      - /gk/backpropagation/
      - /gk/optimizers/
      - /gk/regularization/
      - /gk/batch-epoch/

  - title: "CNN（画像認識）"
    items:
      - /gk/cnn/
      - /gk/convolution/
      - /gk/pooling/
      - /gk/cnn-models/

  - title: "RNN・系列モデル"
    items:
      - /gk/rnn/
      - /gk/vanishing-exploding-gradient/
      - /gk/lstm/
      - /gk/gru/

  - title: "Attention・Transformer・Embedding"
    items:
      - /gk/attention/
      - /gk/transformer/
      - /gk/embedding-word2vec/
        
  - title: "物体検出"
    items:
      - /gk/ssd/
      - /gk/faster-r-cnn/
      - /gk/yolo/
      - /gk/rcnn-fast-rcnn/
      - /gk/anchor-defaultbox-rpn/
      - /gk/object-detection-summary/

  - title: "セグメンテーションタスク"
    items:
      - /gk/segnet/
      - /gk/u-net/
      - /gk/fcn/
      - /gk/segmentation-cheatsheet/
        
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
  
  - title: "機械学習の具体的手法"
    items:
      - /gk/search-and-inference/
      - /gk/search-vs-rl/
        
  - title: "ディープラーニングの概要"
    items:
      - /gk/leaky-relu/
      - /gk/relu-family-cheatsheet/
        
  - title: "ディープラーニングの要素技術"
    items:
      - /gk/encoder-decoder/
      - /gk/lstm-cec/

  - title: "ディープラーニングの応用例"
    items:
      - /gk/xai-explainability/
      - /gk/efficientnet/

  - title: "AIの社会実装に向けて"
    items:
      - /gk/edge-ai/
      - /gk/edge-vs-cloud-ai/
      - /gk/crisp-dm/
        
  - title: "AIの法律と倫理"
    items:
      - /gk/fairness-bias/
      - /gk/privacy-data-protection/
      - /gk/safety-robustness/
      - /gk/ai-governance/
        
  - title: "チートシート（試験直前）"
    items:
      - /gk/nn-cheatsheet/
      - /gk/nn-final-cheatsheet/
      - /gk/search-vs-ml-cheatsheet/
      - /gk/ai-ethics-cheatsheet/
      - /gk/speech-recognition-cheatsheet/
      - 
  - title: "ひっかけ問題集"
    items:
      - /gk/trick-questions-1/
---

{% comment %}
  gk_sections に書いた URL から対応する page を引く
  見つからない場合は赤字で表示（permalink/url の不一致検出）
{% endcomment %}

## 機械学習 分野別まとめ

{% for sec in page.gk_sections %}
### {{ sec.title }}

<ul>
{% for url in sec.items %}
  {% assign p = site.pages | where: "url", url | first %}
  {% if p %}
    <li><a href="{{ p.url }}">{{ p.title }}</a></li>
  {% else %}
    <li><span style="color:#c00">{{ url }}（ページが見つかりません：permalink/url要確認）</span></li>
  {% endif %}
{% endfor %}
</ul>

{% endfor %}
