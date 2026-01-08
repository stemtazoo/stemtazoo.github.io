---
layout: page
title: Random CropとRandom Translationの違いとは？【画像データ拡張｜G検定対策】
permalink: /gk/random-crop-vs-translation/
tags: [gk, cnn, neural_network]
---

## まず結論
- **Random Cropは「画像の一部を切り出す」データ拡張**、  
  **Random Translationは「画像全体を平行移動させる」データ拡張**である。
- G検定では「**切るか・動かすか**」で即座に判別する。

## 直感的な説明
2つは似ていますが、やっていることは違います。

- **Random Crop**  
  👉 写真の一部をランダムに切り抜く
- **Random Translation**  
  👉 写真全体を左右・上下にずらす

たとえると、
- Crop＝**トリミング**
- Translation＝**スライド**

です。

## 定義・仕組み
### Random Crop
- 元画像から **ランダムな位置・サイズの領域を切り出す**
- 切り出した後、元のサイズにリサイズすることが多い

目的：
- 部分的な特徴への頑健性向上
- 物体の位置ずれへの耐性

重要：
- **画像の一部が欠ける**
- 視野が狭くなる

### Random Translation
- 画像全体を **左右・上下に平行移動**
- 移動により端が欠ける場合は
  - 0埋め
  - パディング
  - 反射
などで補完される

目的：
- 位置ずれへの耐性向上

重要：
- **画像全体は保持される**
- 切り取りはしない

## いつ使う？（得意・不得意）
### Random Cropが得意な場面
- 物体検出・分類
- 部分特徴が重要なタスク
- 過学習を強く抑えたい場合

### Random Translationが得意な場面
- 位置ずれに強いモデルを作りたい
- 画像全体の構造を保ちたい場合

### 注意点（共通）
- 文字認識や医療画像では要注意
- 重要部分が欠けると性能低下の可能性

## G検定ひっかけポイント
ここが最重要です。

### よくある誤解
- ❌「Random Cropは移動である」
- ❌「Random Translationは切り取りである」
- ❌「Flipと同じ意味」
- ❌「色変換の手法」

### 正しい判断基準
- **切り出す → Random Crop**
- **ずらす → Random Translation**
- **反転 → Random Flip**
- **色 → Color Jitter**

問題文に  
「切り出す」「一部を抽出」  
とあれば **Random Crop**。

「平行移動」「左右・上下に移動」  
とあれば **Random Translation**。

## 最終比較表（これだけ見ればOK）
| 観点 | Random Crop | Random Translation |
|---|---|---|
| 操作内容 | 切り出し | 平行移動 |
| 画像の欠損 | あり | 端のみ |
| 視野 | 狭くなる | 変わらない |
| 主目的 | 部分頑健性 | 位置頑健性 |
| 混同注意 | Translation | Crop |

## まとめ（試験直前用）
- Crop＝切る
- Translation＝ずらす
- Flip＝反転
- 色は別カテゴリ
- 動詞で判断する
