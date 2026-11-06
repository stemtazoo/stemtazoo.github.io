---
layout: page
title: アンチエイリアシングとは？ギザギザを滑らかにするCG技術【基本情報技術者試験】
description: アンチエイリアシングを「斜め線や曲線のギザギザを目立たなくする処理」として整理し、シェーディング・テクスチャマッピング・バンプマッピングとの違いをFE試験の選択肢で切れるように解説します。
permalink: /fe/anti-aliasing/
tags: [fe, fe-technology, multimedia, computer-graphics]
fe_section: テクノロジ系
fe_subsection: マルチメディア
fe_order: 32
date: 2026-08-21
last_modified_at: 2026-11-07
related_articles:
  - /fe/computer-graphics-overview/
  - /fe/raster-vector-graphics/
  - /fe/clipping/
---

## まず結論

アンチエイリアシングとは、**斜め線や曲線の輪郭に現れるギザギザを目立たなくし、滑らかに見せる処理**です。

FE試験では、次の言葉が出たらアンチエイリアシングを疑います。

```text
斜め線
曲線
輪郭
ギザギザ
滑らかに表示
→ アンチエイリアシング
```

重要なのは、**立体感・模様・凹凸ではなく、輪郭のギザギザを改善する技術**だと切り分けることです。

## 直感的な説明

ディスプレイの画面は、小さな点であるピクセルの集まりです。

水平線や垂直線は比較的きれいに表せますが、斜め線や曲線は、ピクセルを階段状に並べるためギザギザして見えることがあります。

### 同じ斜め線を比較：アンチエイリアシングなし・あり

<div class="fe-aa-compare" aria-label="同じ斜め線の描画前後比較">
  <figure class="fe-aa-compare__card">
    <figcaption><strong>処理なし：ギザギザが目立つ</strong></figcaption>
    <svg viewBox="0 0 120 120" role="img" aria-label="斜め線の画素が階段状に並んでギザギザが見える模式図" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid meet">
<rect width="120" height="120" fill="#ffffff"/>
<rect x="110" y="0" width="10" height="10" fill="#18334a"/>
<rect x="100" y="10" width="10" height="10" fill="#18334a"/>
<rect x="90" y="20" width="10" height="10" fill="#18334a"/>
<rect x="80" y="30" width="10" height="10" fill="#18334a"/>
<rect x="70" y="40" width="10" height="10" fill="#18334a"/>
<rect x="60" y="50" width="10" height="10" fill="#18334a"/>
<rect x="50" y="60" width="10" height="10" fill="#18334a"/>
<rect x="40" y="70" width="10" height="10" fill="#18334a"/>
<rect x="30" y="80" width="10" height="10" fill="#18334a"/>
<rect x="20" y="90" width="10" height="10" fill="#18334a"/>
<rect x="10" y="100" width="10" height="10" fill="#18334a"/>
<rect x="0" y="110" width="10" height="10" fill="#18334a"/>
<rect width="120" height="120" fill="none" stroke="#a6b6c0" stroke-width="1"/>
</svg>
    <p>濃い画素だけで斜め線を表すと、輪郭が階段状になります。</p>
  </figure>
  <figure class="fe-aa-compare__card">
    <figcaption><strong>処理あり：滑らかに見える</strong></figcaption>
    <svg viewBox="0 0 120 120" role="img" aria-label="輪郭の隣の画素を中間の明るさにしてギザギザを目立たなくする模式図" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid meet">
<rect width="120" height="120" fill="#ffffff"/>
<rect x="100" y="0" width="10" height="10" fill="#b5c1cb"/>
<rect x="110" y="0" width="10" height="10" fill="#18334a"/>
<rect x="90" y="10" width="10" height="10" fill="#b5c1cb"/>
<rect x="100" y="10" width="10" height="10" fill="#18334a"/>
<rect x="110" y="10" width="10" height="10" fill="#b5c1cb"/>
<rect x="80" y="20" width="10" height="10" fill="#b5c1cb"/>
<rect x="90" y="20" width="10" height="10" fill="#18334a"/>
<rect x="100" y="20" width="10" height="10" fill="#b5c1cb"/>
<rect x="70" y="30" width="10" height="10" fill="#b5c1cb"/>
<rect x="80" y="30" width="10" height="10" fill="#18334a"/>
<rect x="90" y="30" width="10" height="10" fill="#b5c1cb"/>
<rect x="60" y="40" width="10" height="10" fill="#b5c1cb"/>
<rect x="70" y="40" width="10" height="10" fill="#18334a"/>
<rect x="80" y="40" width="10" height="10" fill="#b5c1cb"/>
<rect x="50" y="50" width="10" height="10" fill="#b5c1cb"/>
<rect x="60" y="50" width="10" height="10" fill="#18334a"/>
<rect x="70" y="50" width="10" height="10" fill="#b5c1cb"/>
<rect x="40" y="60" width="10" height="10" fill="#b5c1cb"/>
<rect x="50" y="60" width="10" height="10" fill="#18334a"/>
<rect x="60" y="60" width="10" height="10" fill="#b5c1cb"/>
<rect x="30" y="70" width="10" height="10" fill="#b5c1cb"/>
<rect x="40" y="70" width="10" height="10" fill="#18334a"/>
<rect x="50" y="70" width="10" height="10" fill="#b5c1cb"/>
<rect x="20" y="80" width="10" height="10" fill="#b5c1cb"/>
<rect x="30" y="80" width="10" height="10" fill="#18334a"/>
<rect x="40" y="80" width="10" height="10" fill="#b5c1cb"/>
<rect x="10" y="90" width="10" height="10" fill="#b5c1cb"/>
<rect x="20" y="90" width="10" height="10" fill="#18334a"/>
<rect x="30" y="90" width="10" height="10" fill="#b5c1cb"/>
<rect x="0" y="100" width="10" height="10" fill="#b5c1cb"/>
<rect x="10" y="100" width="10" height="10" fill="#18334a"/>
<rect x="20" y="100" width="10" height="10" fill="#b5c1cb"/>
<rect x="0" y="110" width="10" height="10" fill="#18334a"/>
<rect x="10" y="110" width="10" height="10" fill="#b5c1cb"/>
<rect width="120" height="120" fill="none" stroke="#a6b6c0" stroke-width="1"/>
</svg>
    <p>輪郭の周辺画素にも中間色を使い、階段状の境界を目立たなくします。</p>
  </figure>
</div>

<style>
.fe-aa-compare{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr));gap:1rem;margin:1rem 0 1.2rem}
.fe-aa-compare__card{margin:0;padding:1rem;border:1px solid #b8c5ce;border-radius:12px;background:#f7f9fb;min-width:0}
.fe-aa-compare__card figcaption{font-size:.95rem;line-height:1.5;color:#233747;min-height:2.8em}
.fe-aa-compare__card svg{display:block;width:100%;max-width:220px;height:auto;margin:0.6rem auto;background:#fff;image-rendering:pixelated}
.fe-aa-compare__card p{font-size:.92rem;line-height:1.7;color:#334957;margin:0}
</style>

この図は、元画像の引用ではなく、画素の塗り分けを独自に作った説明用の模式図です。中間色を使うことで**線の輪郭を滑らかに見せる**考え方を表しています。画素数そのものを増やしているわけではありません。

つまり、実際のピクセルの形を変えるのではなく、**境界付近の見え方を調整する**ことで滑らかに見せています。

## 定義・仕組み

デジタル画像では、連続した形状を離散的なピクセルで表現します。

そのため、斜め線や曲線では本来なめらかな輪郭が階段状に見えることがあります。このギザギザを一般に**エイリアシング**と呼びます。

アンチエイリアシングでは、輪郭付近のピクセルに中間的な色や明るさを与えることで、境界を滑らかに見せます。

FE試験では、細かなアルゴリズムよりも、**何を改善する技術なのか**を押さえるのが重要です。

| 技術 | 主に改善するもの | 試験での合図 |
|---|---|---|
| アンチエイリアシング | 輪郭のギザギザ | 斜め線、曲線、滑らか |
| [クリッピング](/fe/clipping/) | 表示範囲の外側を除外 | 範囲外、ウィンドウ |
| シェーディング | 明暗・立体感 | 光源、陰影、明るさ |
| テクスチャマッピング | 表面の模様・質感 | 画像を貼る、模様 |
| バンプマッピング | 表面の凹凸感 | 凹凸、細かな起伏 |

## 科目Aでどう出る？

科目Aでは、CG技術の名称と役割の対応を問う問題がよく出ます。

このタイプは、**どの見た目を変える技術か**を見ると切りやすいです。

```text
ギザギザを滑らかにする
→ アンチエイリアシング

光と影で立体感を出す
→ シェーディング

表面に模様を貼る
→ テクスチャマッピング

凹凸感を加える
→ バンプマッピング
```

### 「きれいに見せる」だけでは決めない

CG技術はどれも表示を自然にしたり、見栄えを良くしたりするために使われます。

そのため、問題文に「見た目を自然にする」とだけ書かれていても不十分です。

```text
輪郭を自然にする
→ アンチエイリアシング

表面の明暗を自然にする
→ シェーディング

表面の模様を自然にする
→ テクスチャマッピング

表面の凹凸感を自然にする
→ バンプマッピング
```

**どの部分を自然にするのか**を確認するのがコツです。

## どんな場面で使う？

アンチエイリアシングは、文字、アイコン、図形、3DCGの輪郭など、斜め線や曲線が多い表示で使われます。

例えば、次のような場面です。

- 斜めの線を滑らかに表示したい
- 円や曲線の輪郭をきれいに見せたい
- 文字の輪郭のギザギザを抑えたい
- 3DCGモデルのエッジを自然に見せたい

共通しているのは、**輪郭のジャギーを目立たなくする**ことです。

## よくある誤解・混同

### シェーディングと混同する

シェーディングは、光源と物体の位置関係などから明るさや陰影を計算し、立体感を出す処理です。

```text
輪郭のギザギザ
→ アンチエイリアシング

明暗・陰影
→ シェーディング
```

### テクスチャマッピングと混同する

テクスチャマッピングは、3DCGの表面に画像や模様を貼り付けて質感を表現する技術です。

アンチエイリアシングは模様を貼る技術ではありません。

### バンプマッピングと混同する

バンプマッピングは、表面に細かな凹凸があるように見せる技術です。

```text
表面の凹凸感
→ バンプマッピング

輪郭の滑らかさ
→ アンチエイリアシング
```

### 解像度を上げることと同じだと思う

解像度が高くなるとギザギザが目立ちにくくなる場合はありますが、アンチエイリアシングは単に解像度を上げることそのものではありません。

試験では、**輪郭付近の見え方を調整して滑らかにする処理**と理解しておけば十分です。

画像を作る工程と画素の関係を整理するなら、[CG技術の全体像](/fe/computer-graphics-overview/)に戻れます。

## まとめ（試験直前用）

- **斜め線・曲線のギザギザを滑らかにする → アンチエイリアシング**
- 光と影で立体感を出す → シェーディング
- 表面に模様を貼る → テクスチャマッピング
- 表面に凹凸感を出す → バンプマッピング
- 「きれいにする」ではなく、**何を改善する技術か**で選択肢を切る

試験直前は、次の4つをセットで覚えると便利です。

```text
ギザギザ → アンチエイリアシング
陰影       → シェーディング
模様       → テクスチャマッピング
凹凸       → バンプマッピング
```

{% include fe_article_footer.html %}
