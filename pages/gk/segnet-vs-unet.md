---
layout: page
title: SegNetとU-Netの違い｜Decoderへの情報の渡し方【G検定】
description: "SegNetとU-Netの復元を、Encoderで保持する情報、Decoderへの受渡し、アップサンプリング後の処理という3段階で比較します。位置インデックスと特徴マップの結合を区別し、「SegNetのDecoderには位置しか渡らない」という誤解を防ぎます。"
permalink: /gk/segnet-vs-unet/
tags: [gk, cnn, cheatsheet]
gk_section: ディープラーニングの応用例/画像認識/セグメンテーションタスク
gk_order: 4
last_modified_at: 2026-10-19
---

## まず結論

SegNetとU-Netは、**対応するEncoder段からDecoder段へ、復元を助ける何の情報を渡すか**で区別します。

- SegNet：Max Poolingで最大値があった**位置のインデックス**
- U-Net：Encoderで得た**特徴マップ**をスキップ接続で結合

ここでは、縮小前の情報が復元側へ届く経路を横並びに追います。3モデルの位置付けだけ確認したい場合は、[FCN・U-Net・SegNetの一覧](/gk/segmentation-cheatsheet/)を使ってください。

## 直感的な説明

SegNetは「代表値があった場所のメモ」、U-Netは「その段で計算した特徴の中身」を渡すイメージです。

ただし、SegNetのDecoderに**位置しか入力されない**という意味ではありません。両者とも、深い層から来た低解像度の特徴を復元に使います。比較しているのは、それに加えて対応するEncoder側から渡す情報です。

## 定義・仕組み

### 同じ段に注目して追う

| 手順 | SegNet | U-Net |
| --- | --- | --- |
| 1. Encoderで解像度を下げる | Max Pooling時の最大値の位置を記録 | 対応する段の特徴マップを保持 |
| 2. Decoderへ補助情報を渡す | 位置インデックス | Encoderの特徴マップ |
| 3. Decoderで解像度を上げる | Decoder側の値を保存した位置に配置し、畳み込みで処理 | アップサンプリングした特徴とEncoderの特徴を結合し、畳み込みで処理 |

たとえばEncoderで最大値が「下段左」にあった場合、SegNetはその位置を使ってDecoder側の値を配置します。**元の4つの値を丸ごとコピーする処理ではありません。** 数値を追う例は[SegNetの2×2の復元例](/gk/segnet/)で確認できます。

U-Netでは、対応するEncoder側の特徴マップをDecoder側の特徴とチャネル方向に結合します。「位置インデックスだけを渡す」とは異なります。構造全体は[U-Net](/gk/u-net/)を参照してください。

## いつ使う？（得意・不得意）

どちらもセマンティックセグメンテーションのモデルです。設計を比べるときは、保持する情報やメモリの使い方を確認します。

ただし、**精度なら必ずU-Net、リアルタイムなら必ずSegNet**とは断定しません。入力サイズ・構成・データ・実装によって結果が変わるため、試験では構造上の違いを優先します。

## G検定ひっかけポイント

- 「Max Poolingの位置を再利用」→ SegNet
- 「対応するEncoderの特徴マップを結合」→ U-Net
- 「SegNetのDecoderは位置情報だけで動く」→ 誤り。復元する特徴も必要
- 「skip connectionがある」だけでは、他の構造にもあるためU-Netと即断しない
- 「Encoder-Decoderである」だけでは両者を区別できない

## まとめ（試験直前用）

- SegNet：**位置を使って配置する**
- U-Net：**特徴マップを結合する**
- 共通の深い特徴の経路と、Encoderからの補助情報の経路を分けて見る
- 精度・速度の固定順位で判断しない

## 参考資料（原論文）

- [SegNet: A Deep Convolutional Encoder-Decoder Architecture for Image Segmentation｜IEEE](https://doi.org/10.1109/TPAMI.2016.2644615)
  - SegNetの原論文です。Max PoolingのインデックスをDecoder側で再利用する設計を示しています。
- [U-Net: Convolutional Networks for Biomedical Image Segmentation｜Springer](https://doi.org/10.1007/978-3-319-24574-4_28)
  - U-Netの原論文です。Encoder側の特徴マップをDecoder側へ直接渡すskip connectionを用います。

{% include gk_article_footer.html %}
