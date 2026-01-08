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
      - /gk/turing-test/
      - /gk/chinese-room/
      - /gk/symbol-grounding/
      - /gk/singularity/

  - title: "人工知能をめぐる動向"
    items:
      - /gk/classical-ai/
      - /gk/knowledge-representation/
      - /gk/classical-ai-vs-ml/
      - /gk/concepts-final-cheatsheet/
      - /gk/torobo-kun/
      - /gk/simple-perceptron/
      - /gk/xor-problem/
      - /gk/mlp-xor/
      - /gk/activation-functions-role/
      - /gk/neocognitron-to-cnn/
      - /gk/strips/
      - /gk/ilsvrc/
      - /gk/curse-of-dimensionality/
      - /gk/dendral/
      - /gk/mycin/
      - /gk/expert-system-limitations/

  - title: "機械学習の概要"
    subsections:
      - title: "代表的な手法"
        subsections:
          - title: "学習の種類"
            items:
              - /gk/supervised-learning/
              - /gk/unsupervised-learning/
              - /gk/reinforcement-learning/
              - /gk/learning-types-comparison/
              - /gk/supervised-unsupervised-reinforcement/

          - title: "教師あり学習"
            items:
              - /gk/ensemble-learning/
              - /gk/boosting/
              - /gk/bagging/
              - /gk/random-forest/
              - /gk/var/
              - /gk/time-series-ar-arma-arima/
              - /gk/var-vs-arima/
              - /gk/poisson-regression/
              - /gk/poisson-vs-binomial/
              - /gk/binomial-vs-logistic/
              - /gk/softmax/

          - title: "教師なし学習"
            items:
              - /gk/k-means/
              - /gk/kmeans-vs-hierarchical/
              - /gk/hierarchical-clustering/
              - /gk/clustering-vs-dimensionality-reduction/
              - /gk/dendrogram/
              - /gk/pca-vs-svd/
              - /gk/k-means-vs-knn/
              - /gk/cold-start-problem/
              - /gk/mds/
              - /gk/tsne/
              - /gk/umap/
              - /gk/svd/
              - /gk/evd/
              - /gk/lda/
              - /gk/pca/

          - title: "強化学習"
            items:
              - /gk/distributed-reinforcement-learning/
              - /gk/reinforcement-learning-cheatsheet/
              - /gk/stationarity/
              - /gk/reinforce/
              - /gk/reinforce-vs-actor-critic/
              - /gk/gradient-boosting/
              - /gk/actor-critic/
              - /gk/a2c-a3c/
              - /gk/multi-armed-bandit/
              - /gk/discount-factor/
              - /gk/state-value-function/
              - /gk/td-learning/

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
          - /gk/sigmoid-function/
          - /gk/vanishing-gradient-sigmoid/
            
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
          - /gk/sgd/
          - /gk/mini-batch/
          - /gk/adagrad/
          - /gk/rmsprop/
          - /gk/adam/
          - /gk/adabound/
          - /gk/momentum/
          - /gk/adadelta/
          - /gk/amsbound/
          - /gk/optimizer-compare-4/
          - /gk/optimization-cheatsheet/
          - /gk/optimization-cheatsheet-2/
          - /gk/double-descent/
          - /gk/grid-vs-random-search/
          - /gk/bayesian-optimization/
          - /gk/cross-validation-with-search/
          - /gk/hyperparameter-vs-parameter/
          - /gk/optimizer-lineage/
          - /gk/optimizer-comparison/
          - /gk/optimizer-trick-questions/

      - title: "誤差逆伝播法（Backpropagation）"
        items:
          - /gk/gradient-descent/
          - /gk/credit-assignment-problem/
            
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
          - /gk/atrous-convolution/
          - /gk/atrous-vs-pooling/
          - /gk/whitening/
          - /gk/standardization/
          - /gk/normalization/

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
          - /gk/jordan-network/
          - /gk/elman-network/
          - /gk/jordan-vs-elman/
          - /gk/vanishing-gradient-2/
          - /gk/teacher-forcing/
          
      - title: "トランスフォーマー (Transformer)"
        items:
          - /gk/transformer/
          - /gk/positional-encoding/
          - /gk/multi-head-attention/
            
      - title: "オートエンコーダ"
        items:
          - /gk/vae/
          - /gk/ae-vs-vae/
          - /gk/anomaly-detection-ae/
          - /gk/vae-anomaly-detection/
          - /gk/anomaly-detection-methods/
          - /gk/dae/
          - /gk/cae/
                        
  - title: "ディープラーニングの応用例"
    subsections:
      - title: "画像認識"
        subsections:
          - title: "画像データの入力"
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
              - /gk/pspnet/
              - /gk/segnet-2/
              - /gk/segnet-vs-unet/
              - /gk/brightness/
              - /gk/contrast-saturation-hue/
              - /gk/data-augmentation-cheatsheet/
              - /gk/image-terms-check/
              - /gk/randaugment/
              - /gk/auto-rand-trivial-augment/
              - /gk/data-augmentation-vs-normalization/
              - /gk/regularization-vs-augmentation-vs-normalization/
              - /gk/random-flip/
              - /gk/random-crop-vs-translation/
              - /gk/cutmix/
              - /gk/image-augmentation-cheatsheet/
              - /gk/panoptic-segmentation/
          - title: "物体認識タスク"
            items:
              - /gk/mobilenet/
              - /gk/mnasnet/
              - /gk/senet/

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
          - /gk/rlhf/
          - /gk/sentiment-analysis/
          - /gk/tfidf-word2vec-bert/
          - /gk/attention-transformer-bert/
          - /gk/word-embedding/
          - /gk/word2vec-fasttext-glove/
          - /gk/n-gram/
          - /gk/paraphrasing/

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
          - /gk/agent57/
          - /gk/dqn-alphago-alphastar-agent57/
          - /gk/ape-x/
          - /gk/dqn-family/
          - /gk/on-policy-off-policy/
          - /gk/openai-five/
          - /gk/ai-project-comparison/
          - /gk/domain-randomization/
          - /gk/td-learning/
            
      - title: "データ生成"
        items:
          - /gk/vae-vs-gan/
          - /gk/pix2pix/
          - /gk/cyclegan/
          - /gk/gan-vs-conditional-gan/
          - /gk/vae-vs-gan-vs-pix2pix/
          - /gk/gan-anomaly-detection/
          - /gk/nerf/

      - title: "転移学習・ファインチューニング"
        items:
          - /gk/catastrophic-forgetting/
          - /gk/catastrophic-forgetting-solution/
          - /gk/transfer-vs-forgetting/
          - /gk/pretraining-finetuning-transfer/
          - /gk/self-supervised-learning/
          - /gk/continual-learning/
          - /gk/few-shot-learning/
          - /gk/few-shot-vs-zero-shot-vs-transfer/
          - /gk/one-shot-learning/

      - title: "マルチモーダル"
        items:
          - /gk/flamingo/
          - /gk/palm/
          - /gk/palm-e/
          - /gk/clip/
          - /gk/blip/
          - /gk/unified-io/
          - /gk/dall-e/
          - /gk/multimodal-cheatsheet/
          - /gk/visual-question-answering/
            
      - title: "モデルの解釈性"
        items:
          - /gk/xai-explainability/
          - /gk/cam-grad-cam/
          - /gk/lime-vs-shap/
          - /gk/permutation-importance/
          - /gk/permutation-importance-vs-shap/

      - title: "モデルの軽量化"
        items:
          - /gk/lottery-ticket-hypothesis/
          
  - title: "AIの社会実装に向けて"
    items:
      - /gk/edge-ai/
      - /gk/edge-vs-cloud-ai/
      - /gk/crisp-dm/
      - /gk/crisp-dm-vs-ml-pipeline/
      - /gk/crisp-ml/
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
      - /gk/human-centered-ai-principles/
      - /gk/inclusion/
      - /gk/gdpr-rights-erasure-rectification/
      - /gk/skill-loss/

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

