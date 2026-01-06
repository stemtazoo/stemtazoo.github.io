---
layout: page
title: G検定 学習まとめ
permalink: /gk/
tags: [gk]

# 表示順はここで固定（/gk/〇〇/ ＝ pages/gk/〇〇.md）
gk_sections:
  - title: "人工知能（AI）とは"
    items:
      - /gk/ai-booms-cheatsheet/
      - /gk/second-ai-boom/
      - /gk/strong-vs-weak-ai/
      - /gk/big-data/
      - /gk/third-ai-boom/
      - /gk/ai-effect/
      - /gk/frame-problem/
      - /gk/symbol-grounding-problem/
      - /gk/toy-problem/
      - /gk/loebner-contest/

  - title: "人工知能をめぐる動向"
    items:
      - /gk/classical-ai/
      - /gk/knowledge-representation/
      - /gk/classical-ai-vs-ml/
      - /gk/concepts-final-cheatsheet/
      - /gk/torobo-kun/
      - /gk/mnasnet/
      - /gk/simple-perceptron/
      - /gk/xor-problem/
      - /gk/mlp-xor/
      - /gk/activation-functions-role/
      - /gk/neocognitron-to-cnn/
      - /gk/strips/

  - title: "機械学習の概要"
    subsections:
      - title: "代表的な手法"
        items:
          - /gk/supervised-learning/
          - /gk/unsupervised-learning/
          - /gk/reinforcement-learning/
          - /gk/learning-types-comparison/
          - /gk/distributed-reinforcement-learning/
          - /gk/reinforcement-learning-cheatsheet/
          - /gk/dendrogram/
          - /gk/hierarchical-clustering/
          - /gk/kmeans-vs-hierarchical/
          - /gk/clustering-vs-dimensionality-reduction/
          - /gk/pca-vs-svd/
          - /gk/supervised-unsupervised-reinforcement/
          - /gk/ensemble-learning/
          - /gk/gdpr-rights-erasure-rectification/
          - /gk/boosting/
          - /gk/bagging/
          - /gk/random-forest/
          - /gk/var/
          - /gk/time-series-ar-arma-arima/
          - /gk/var-vs-arima/
          - /gk/stationarity/
          - /gk/poisson-regression/
          - /gk/poisson-vs-binomial/
          - /gk/binomial-vs-logistic/
          - /gk/reinforce/
          - /gk/reinforce-vs-actor-critic/
          - /gk/gradient-boosting/

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
          - /gk/train-validation-test/
          - /gk/cross-validation/
          - /gk/time-series-cross-validation/
          - /gk/aic/
          - /gk/bic/
          - /gk/aic-bic/
          - /gk/bias-variance/
          - /gk/cross-validation-with-search/
          - /gk/occams-razor/
          - /gk/ai-philosophy-cheatsheet/

      - title: "よくあるつまずき（過学習など）"
        items:
          - /gk/overfitting/
          - /gk/underfitting/
          - /gk/learning-curve/
          - /gk/bias-variance-tradeoff/

  - title: "ディープラーニングの概要"
    subsections:
      - title: "ニューラルネットワークとディープラーニング"
        items:
          - /gk/perceptron/
          - /gk/mlp/
          - /gk/activation-functions/
          - /gk/backpropagation/
          - /gk/optimizers/
          - /gk/batch-epoch/
          - /gk/leaky-relu/
          - /gk/relu-family-cheatsheet/
          - /gk/activation-derivative/
          - /gk/gradient-vanishing-exploding/
          - /gk/learning-rate-scheduling/
          - /gk/pruning/
          - /gk/model-compression/
          - /gk/loss-function/
          - /gk/vanishing-gradient/
          - /gk/gpgpu/
            
      - title: "誤差関数"
        items:
          - /gk/contrastive-loss/
          - /gk/contrastive-vs-triplet-loss/
                        
      - title: "正則化"
        items:
          - /gk/regularization/
          - /gk/regularization-l1-l2/
          - /gk/dropout/
          - /gk/early-stopping/
    
      - title: "最適化手法"
        items:
          - /gk/gradient-descent/
          - /gk/adagrad/
          - /gk/rmsprop/
          - /gk/adam/
          - /gk/adabound/
          - /gk/momentum/
          - /gk/optimizer-compare-4/
          - /gk/optimization-cheatsheet/
          - /gk/optimization-cheatsheet-2/
          - /gk/double-descent/
          - /gk/grid-vs-random-search/
          - /gk/bayesian-optimization/
          - /gk/cross-validation-with-search/
          - /gk/hyperparameter-vs-parameter/
          - /gk/optimizer-lineage/
          - /gk/adadelta/
            
  - title: "ディープラーニングの要素技術"
    subsections:
      - title: "ネットワークの構成要素"
        items:
          - /gk/cnn/
          - /gk/convolution/
          - /gk/pooling/
          - /gk/cnn-models/
          - /gk/dilated-convolution/
          - /gk/pooling-stride-dilation/
          - /gk/global-average-pooling/
          - /gk/vanishing-exploding-gradient/
          - /gk/embedding-word2vec/
          - /gk/instance-normalization/
          - /gk/normalization-cheatsheet/

      - title: "リカレントニューラルネットワーク (RNN)"
        items:
          - /gk/rnn/
          - /gk/lstm/
          - /gk/gru/
          - /gk/encoder-decoder/
          - /gk/rnn-encoder-decoder/
          - /gk/attention/
          - /gk/seq2seq-attention-transformer/
          - /gk/lstm-nonstationary/
          - /gk/bptt/
          
      - title: "トランスフォーマー (Transformer)"
        items:
          - /gk/transformer/
            
      - title: "オートエンコーダ"
        items:
          - /gk/vae/
          - /gk/dae/
          - /gk/cae/
                        
  - title: "ディープラーニングの応用例"
    subsections:
      - title: "画像認識"
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
          - /gk/instance-segmentation/
          - /gk/detection-vs-semantic-vs-instance/
          - /gk/mask-r-cnn/
          - /gk/ellipse-r-cnn/
          - /gk/detection-segmentation-map/
          - /gk/vit/
          - /gk/openpose/
          - /gk/fpn/
          - /gk/fpn-ssd-yolo/
          - /gk/deeplab/
          - /gk/segmentation-models-comparison/

      - title: "音声処理"
        items:
          - /gk/pcm/
          - /gk/timbre-mfcc/
          - /gk/formant/
          - /gk/speech-features/
          - /gk/speech-preprocessing/
          - /gk/vad/

      - title: "自然言語処理"
        items:
          - /gk/bert/
          - /gk/gpt/
          - /gk/bert-vs-gpt/
          - /gk/tf-idf/
          - /gk/bag-of-words/
          - /gk/word2vec/
          - /gk/distributed-representation/
          - /gk/word2vec-vs-bert/
          - /gk/embedding-layer/
          - /gk/self-attention/
          - /gk/transformer-architecture/
          - /gk/nlp-cheatsheet/
          - /gk/mlm/
          - /gk/cbow/
          - /gk/skip-gram/
          - /gk/local-vs-distributed-representation/
          - /gk/onehot-vs-embedding/
          - /gk/cbow-vs-skipgram/
          - /gk/embedding-vs-contextual-embedding/
          - /gk/bert-why-transformer/

      - title: "深層強化学習"
        items:
          - /gk/dueling-network/
          - /gk/dqn/
          - /gk/multi-agent-rl/
          - /gk/alphago-vs-alphastar/
          - /gk/rl-methods/
          - /gk/sim2real/
          - /gk/noisy-network/
          - /gk/dqn-advanced/
          - /gk/dqn-vs-policy-gradient/
            
      - title: "データ生成"
        items:
          - /gk/vae-vs-gan/
          - /gk/pix2pix/
          - /gk/cyclegan/
          - /gk/gan-vs-conditional-gan/
          - /gk/vae-vs-gan-vs-pix2pix/
            
      - title: "モデルの解釈性"
        items:
          - /gk/xai-explainability/
          - /gk/cam-grad-cam/
          - /gk/lime-vs-shap/
             
  - title: "AIの社会実装に向けて"
    items:
      - /gk/edge-ai/
      - /gk/edge-vs-cloud-ai/
      - /gk/crisp-dm/
      - /gk/crisp-dm-vs-ml-pipeline/
      - /gk/mlops/
      - /gk/mlops-process/
      - /gk/devops/
      - /gk/roles-in-ml/
      - /gk/ml-project-lifecycle/
      - /gk/data-leakage/

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
      - /gk/privacy-by-design/
      - /gk/limited-offer-data/
      - /gk/data-portability-gdpr/
      - /gk/gdpr-rights-erasure-rectification/
      - /gk/gdpr-vs-japan-pipa/
      - /gk/ai-patent/
      - /gk/ai-fake-news/
      - /gk/deepfake/
      - /gk/deepfake-detection/
      - /gk/ethical-assessment/
      - /gk/filter-bubble/
      - /gk/echo-chamber/
      - /gk/laws/

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
  見つからない場合は赤字で表示
{% endcomment %}

## まずどこから？

- はじめて：**人工知能とは → 機械学習の概要 → ディープラーニングの概要**
- 画像まわり：**ディープラーニングの要素技術 → 応用例（物体検出・セグメンテーション）**
- 試験直前：**チートシート → ひっかけ問題集**

---

## 目次

- [技術分野](#技術分野)
  - [人工知能とは](#人工知能とは)
  - [人工知能をめぐる動向](#人工知能をめぐる動向)
  - [機械学習の概要](#機械学習の概要)
  - [ディープラーニングの概要](#ディープラーニングの概要)
  - [ディープラーニングの要素技術](#ディープラーニングの要素技術)
  - [ディープラーニングの応用例](#ディープラーニングの応用例)
  - [AIの社会実装に向けて](#aiの社会実装に向けて)
- [法律・倫理分野](#法律倫理分野)
  - [AI倫理・AIガバナンス](#ai倫理aiガバナンス)
- [試験対策](#試験対策)
  - [チートシート（試験直前）](#チートシート試験直前)
  - [ひっかけ問題集](#ひっかけ問題集)

---

## 技術分野

## 人工知能とは
{% assign sec = page.gk_sections | where: "title", "人工知能（AI）とは" | first %}
{% include gk_section.html sec=sec %}

## 人工知能をめぐる動向
{% assign sec = page.gk_sections | where: "title", "人工知能をめぐる動向" | first %}
{% include gk_section.html sec=sec %}

## 機械学習の概要
{% assign sec = page.gk_sections | where: "title", "機械学習の概要" | first %}
{% include gk_section.html sec=sec %}

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

---

## 試験対策

## チートシート（試験直前）
{% assign sec = page.gk_sections | where: "title", "チートシート（試験直前）" | first %}
{% include gk_section.html sec=sec %}

## ひっかけ問題集
{% assign sec = page.gk_sections | where: "title", "ひっかけ問題集" | first %}
{% include gk_section.html sec=sec %}

