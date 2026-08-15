---
layout: page
title: 畳み込み（Convolution）とは？画像フィルタ処理の基本【DS検定】
description: "畳み込み（Convolution）とは、画像上で小さなカーネルを移動させ、周囲の画素との積和から新しい値を計算する処理です。画像フィルタ、カーネル、CNNとの役割の違いと、DS検定での判断基準を整理します。"
permalink: /ds/convolution/
categories: [data-science]
tags: [ds, modeling]
prev: /ds/cnn/
next: /ds/curse-of-dimensionality/
last_modified_at: 2026-08-16
---
<div style="font-size: 14px; margin-bottom: 12px;">
  <a href="/ds/">DS検定トップ</a>
  ＞ {{ page.title }}
</div>

## まず結論

**畳み込み（Convolution）とは、小さな行列（カーネル）を画像上で動かし、周囲の画素から新しい値を計算する処理**です。

DS検定では、次の関係を切り分けることが重要です。

| 用語 | 役割 |
|---|---|
| カーネル | 計算に使う小さな行列 |
| 畳み込み | カーネルを使って値を計算する処理 |
| CNN | 畳み込みを利用して特徴を学習するモデル |

## 直感的な説明

画像のある1画素だけを見るのではなく、**その周囲も一緒に見て新しい値を決める**イメージです。

例えば、中央の画素を含む3×3の範囲を見ます。

```text
□ □ □
□ ■ □
□ □ □
```

この9個の画素に対して、カーネルの値を掛けて足し合わせます。

使うカーネルによって、

- ぼかし
- ノイズ除去
- シャープ化
- エッジ検出

など、得られる効果が変わります。

## 定義・仕組み

畳み込みの基本的な流れは次の通りです。

### ① カーネルを用意する

例えば3×3の小さな行列を使います。

```text
1 1 1
1 1 1
1 1 1
```

### ② 画像の一部分に重ねる

カーネルと画像の同じ位置の値を対応させます。

### ③ 対応する値を掛けて合計する

この積和が、新しい画素値のもとになります。

### ④ カーネルをずらして繰り返す

画像全体へ同じ計算を適用します。

### カーネルによって処理が変わる

| カーネルの役割 | 主な効果 |
|---|---|
| 周囲を平均する | ぼかし・平滑化 |
| 変化を強調する | エッジ検出 |
| 中央を強調する | シャープ化 |

**畳み込みは計算方法、カーネルはその計算ルール**と整理すると分かりやすくなります。

## どんな場面で使う？

### 画像フィルタ処理

- ノイズ除去
- ぼかし
- シャープ化
- エッジ検出

### CNN

CNNでは、カーネルの値を学習によって調整し、画像から有用な特徴を抽出します。

つまり、固定ルールで画像を変換するだけでなく、**特徴を見つけるためのカーネル自体を学習する**点がCNNの特徴です。

## よくある誤解・混同

### ❌ 畳み込み = ぼかし処理

ぼかしは畳み込みの利用例の1つです。カーネルを変えればエッジ検出やシャープ化にも使えます。

### ❌ カーネル = 畳み込み

| 用語 | 意味 |
|---|---|
| カーネル | 小さな行列・計算ルール |
| 畳み込み | カーネルを画像に適用する計算 |

### ❌ 畳み込みはCNNだけで使う

畳み込みは、CNNより前から画像処理・信号処理で使われている計算方法です。

## まとめ（試験直前用）

- **畳み込み = 周囲の値を使って新しい値を計算する処理**
- **カーネル = 畳み込みで使う小さな行列**
- カーネルを画像上で移動させて計算する
- ぼかし・エッジ検出などに使われる
- CNNではカーネルを学習して特徴を抽出する

DS検定では、**カーネル = ルール / 畳み込み = 計算 / CNN = モデル**と切り分けましょう。

## 対応スキル項目（AI利活用スキルシート）

- スキルカテゴリ名：AIの技術理解
- サブカテゴリ名：画像・音声処理
- ★ 画像・動画・音声などのデータに対する基本的な処理方法を理解している

## 🔗 関連記事

<ul style="padding-left: 20px;">
{% assign current_tags = page.tags %}
{% assign count = 0 %}
{% for p in site.pages %}
  {% if p.url != page.url and p.tags %}
    {% assign matched = false %}
    {% for tag in current_tags %}
      {% if p.tags contains tag and tag != "ds" %}
        {% assign matched = true %}
      {% endif %}
    {% endfor %}
    {% if matched %}
      <li style="margin-bottom: 6px;"><a href="{{ p.url }}">{{ p.title }}</a></li>
      {% assign count = count | plus: 1 %}
    {% endif %}
    {% if count >= 5 %}{% break %}{% endif %}
  {% endif %}
{% endfor %}
</ul>

<hr>
<div style="margin-top: 16px;">🏠 <a href="/ds/">DS検定トップに戻る</a></div>
<div style="display:flex;justify-content:space-between;margin-top:12px;">
  {% if page.previous.url %}<a href="{{ page.previous.url }}">← {{ page.previous.title }}</a>{% endif %}
  {% if page.next.url %}<a href="{{ page.next.url }}">{{ page.next.title }} →</a>{% endif %}
</div>
