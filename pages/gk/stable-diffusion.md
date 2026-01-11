---
layout: page
title: Stable Diffusion（拡散モデルの代表例）
permalink: /gk/stable-diffusion/
tags: [gk, neural_network, generative_model, diffusion]
gk_section: ディープラーニングの応用例/データ生成
gk_order: 5
---

## まず結論

* **Stable Diffusion は Diffusion Model をベースにした画像生成モデル**
* **テキストから画像を生成できる（Text-to-Image）**
* **潜在空間（Latent Space）で拡散を行うため高速・軽量**

👉 G検定では  
**「Diffusion × 潜在空間」** が最大のキーワード。

---

## 直感的な説明

Stable Diffusion は一言でいうと、

> **画像そのものではなく、圧縮した世界でノイズ除去を行う拡散モデル**

です。

普通の Diffusion Model は、

* 高画質
* でも重い・遅い

という弱点がありました。

Stable Diffusion では、

1. 画像を一度 **潜在表現に圧縮**
2. 潜在空間で拡散・逆拡散
3. 最後に画像として復元

👉  
**軽くて実用的** になっています。

---

## 定義・仕組み

### Stable Diffusion とは？

* **Latent Diffusion Model（LDM）** の一種
* Diffusion Model を **潜在空間** で実行
* テキスト条件付き生成が可能

---

### 主要コンポーネント

* **VAE**
  * 画像 ↔ 潜在空間の変換
* **U-Net**
  * ノイズ除去（逆拡散）
* **Text Encoder（CLIP など）**
  * テキスト条件を理解

👉  
**VAE + Diffusion + Text**

---

## Diffusion Model との違い（超重要）

| 項目 | Diffusion Model | Stable Diffusion |
|---|---|---|
| 拡散する空間 | 画像空間 | **潜在空間** |
| 計算コスト | 高い | **低い** |
| 実用性 | 研究向け | **実用向け** |
| テキスト生成 | 限定的 | **可能** |

---

## 何ができる？

* テキスト → 画像生成
* 画像 → 画像変換
* インペインティング（欠損補完）
* スタイル変換

---

## G検定ひっかけポイント

### ❌ よくある誤解

* ❌ 「Stable Diffusion は GAN」
* ❌ 「VAEだけで画像生成」
* ❌ 「CNNの分類モデル」

---

### ✅ 正しい理解

* ベースは **Diffusion Model**
* 潜在空間で拡散
* U-Netでノイズ除去

---

## 試験での即断キーワード

* 「拡散モデル」 → Diffusion / Stable Diffusion
* 「潜在空間」 → **Stable Diffusion**
* 「Text-to-Image」 → **Stable Diffusion**

---

## まとめ（試験直前用）

* Stable Diffusion = **Latent Diffusion**
* Diffusion Model の実用形
* 高品質かつ軽量
* GANではない

👉 次は  
**生成モデルひっかけ問題集（GAN / VAE / Diffusion）**  
に進むと、ここまでが完全に固まります。
