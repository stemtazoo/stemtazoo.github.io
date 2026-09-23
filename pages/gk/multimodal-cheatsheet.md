---
layout: page
title: マルチモーダルモデル総まとめ｜CLIP・BLIP・Flamingo・PaLM-E【G検定】
description: "マルチモーダルモデルを、CLIPは画像・テキストの共同埋め込み、BLIPは理解と生成、Flamingoはfew-shot in-context、PaLM-Eはembodiedなセンサ統合という役割で比較します。生成するかだけでなく、入力・出力・学習目的からG検定の選択肢を切ります。"
permalink: /gk/multimodal-cheatsheet/
tags: [gk, cheatsheet, multimodal, attention]
gk_section: ディープラーニングの応用例/マルチモーダル/基礎・全体像
gk_order: 1
last_modified_at: 2026-09-23
---

## まず結論

マルチモーダルモデルは、**「生成できる / できない」だけではなく、何を入力し、何を学び、何を出力するか**で切り分けます。

| モデル | 中心となる役割 | 判断キーワード |
|---|---|---|
| CLIP | 画像・テキストの共同埋め込み | 対照学習、ゼロショット |
| BLIP | 画像言語の理解＋生成 | キャプション、VQA、CapFilt |
| Flamingo | 画像・テキストのfew-shot in-context応答 | Perceiver、Cross-Attention |
| PaLM-E | 実世界の連続入力を言語モデルへ統合 | Embodied、ロボット、センサ |
| DALL·E | テキスト条件の画像生成 | Text-to-Image |

## 直感的な説明

まず問題文で、

1. 入力は何か
2. 出力は何か
3. 何を学習しているか

を確認します。

「画像がある」というだけではモデルを決められません。

## 定義・仕組み

### CLIP

[CLIP](/gk/clip/)は、画像とテキストを同じ埋め込み空間へ写し、正しいペアを近づけます。

### BLIP

[BLIP](/gk/blip/)は、画像・テキスト検索だけでなく、キャプション生成やVQAなど理解・生成の両方を扱います。

### Flamingo

[Flamingo](/gk/flamingo/)は、画像とテキストが混在する文脈へ少数例を与えて応答するfew-shot in-context能力を重視します。

### PaLM-E

[PaLM-E](/gk/palm-e/)は、画像やロボット状態など連続的な実世界入力を言語モデルへ統合します。

## いつ使う？（得意・不得意）

問題文のキーワードから次のように切ります。

- **対照学習・類似度・ゼロショット分類** → CLIP
- **キャプション・VQA・CapFilt** → BLIP
- **画像＋テキスト＋few-shot in-context** → Flamingo
- **ロボット・センサ・Embodied** → PaLM-E
- **テキストから画像そのものを生成** → DALL·EなどText-to-Imageモデル

## G検定ひっかけポイント

### CLIPは生成AIと無関係？

❌ 生成モデルではないので生成システムに使われない  
⭕ **CLIP自体は共同埋め込みモデルだが、生成システムの構成要素に使われることがある**

### BLIP＝Text-to-Image？

❌ テキストから画像を生成する  
⭕ **画像理解・キャプション生成・VQAなど**

### FlamingoのFew-shot

❌ 数例だけでモデルを再学習することが本質  
⭕ **少数例を入力文脈として使うin-context対応**

### PaLM-E

❌ E＝Environment  
⭕ **Embodied Multimodal Language Model**

## まとめ（試験直前用）

- CLIP＝**対応付け・共同埋め込み**
- BLIP＝**理解＋テキスト生成**
- Flamingo＝**few-shot in-context**
- PaLM-E＝**Embodied・センサ統合**
- DALL·E＝**Text-to-Image**
- **生成可否だけでなく、入力・出力・学習目的を見る**

{% include gk_article_footer.html %}
