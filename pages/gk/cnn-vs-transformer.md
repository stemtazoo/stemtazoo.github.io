---
layout: page
title: CNNとTransformerの違い｜畳み込みとAttentionで切り分け【G検定】
description: "CNNは局所領域へ同じフィルタを適用し、TransformerはAttentionで入力要素間の関係を扱います。画像と文章のどちらにも応用できること、両者の組合せもあることを押さえ、出題形式だけでモデルを決めない判断軸を整理します。"
permalink: /gk/cnn-vs-transformer/
tags: [gk, cnn, transformer, cheatsheet]
gk_section: ディープラーニングの応用例/画像認識/ネオコグニトロンとLeNet
gk_order: 9
last_modified_at: 2026-09-25
---

## まず結論

**CNNは畳み込みによって近くの特徴を捉えるモデル、TransformerはAttentionによって入力要素同士の関係を捉えるモデル**です。G検定では、モデル名や計算問題の有無より、**何を使って関係を捉えるか**で切り分けます。

| 観点 | CNN | Transformer |
|---|---|---|
| 中心となる仕組み | 畳み込み | Attention |
| 基本的な着目点 | 近くの領域の特徴 | 入力要素間の関係 |
| 画像への応用 | 画像分類・検出など | 画像をパッチに分けるViTなど |
| 計算を問われたとき | 出力サイズやフィルタ数を確認 | Attentionや系列長などの条件を確認 |

## 直感的な説明

CNNは、画像の上を小さな窓で順に見て、輪郭や模様などを取り出すイメージです。層を重ねることで、より広い範囲の特徴も扱えます。

Transformerは、文章の単語や画像のパッチを要素として、それぞれが他の要素とどう関係するかを見るイメージです。

## 定義・仕組み

- **CNN**：同じフィルタを各位置に適用して特徴マップを作ります。ストライドやパディングは出力サイズに影響します。
- **Transformer**：Self-Attentionで要素間の関係を計算します。位置情報を扱う仕組みも重要です。
- **ViT**：画像をパッチの列としてTransformerへ入力する例です。Transformerが文章専用というわけではありません。

[Vision Transformer](/gk/vit/)と[Self-Attention](/gk/self-attention/)も合わせて見ると、画像への応用と仕組みの違いが整理できます。

## いつ使う？（得意・不得意）

画像の局所的な特徴を捉える説明ならCNN、要素間の関係をAttentionで扱う説明ならTransformerを疑います。ただし、どちらも画像に使えますし、両者を組み合わせたモデルもあります。**画像なら必ずCNN、文章なら必ずTransformer**とは決めません。

出力サイズを求める問題では、モデル名より**入力サイズ・カーネル・パディング・ストライド**など、与えられた条件を先に確認します。Transformerにも計算対象はあるため、「Transformerの計算問題は出ない」とは判断しません。

## G検定ひっかけポイント

- ❌ TransformerはCNNの改良版 → ⭕ **中心となる仕組みが異なる**
- ❌ CNNは離れた位置の情報を扱えない → ⭕ **層を重ねるなどして広い範囲の情報を扱える**
- ❌ Transformerは文章にしか使えない → ⭕ **ViTなど画像への応用もある**
- ❌ 計算問題なら必ずCNN → ⭕ **問題文の対象と条件を確認する**

## まとめ（試験直前用）

- CNN → **畳み込み・局所特徴**
- Transformer → **Attention・要素間の関係**
- ViT → **画像パッチをTransformerで扱う**
- 出題形式ではなく、**仕組みと入力の扱い**で切る

## 参考資料

- [Attention Is All You Need｜原著論文](https://arxiv.org/abs/1706.03762)
- [An Image is Worth 16x16 Words｜ViT原著論文](https://arxiv.org/abs/2010.11929)

{% include gk_article_footer.html %}
