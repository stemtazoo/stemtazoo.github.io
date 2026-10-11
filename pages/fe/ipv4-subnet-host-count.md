---
layout: page
title: IPv4のサブネットとは？CIDR表記とホスト数の計算【基本情報技術者試験】
description: IPv4の/23や/24を32ビットの色分け図で理解し、サブネットマスク、ネットワークアドレス、ブロードキャストアドレスと使用可能ホスト数を計算する手順を整理します。
permalink: /fe/ipv4-subnet-host-count/
tags: [fe, fe-technology, network]
fe_section: テクノロジ系
fe_subsection: ネットワーク
fe_order: 72
date: 2026-10-11
last_modified_at: 2026-10-11
---

## まず結論

IPv4のサブネットでは、**32ビットのうち何ビットをネットワーク部に使うか**によって、ホストに割り当てられるIPアドレス数が決まります。

試験では、まず次の順番で考えます。

1. `/23` なら、ネットワーク部は23ビット
2. ホスト部は `32 - 23 = 9` ビット
3. アドレス総数は `2^9 = 512` 個
4. 通常のサブネットでは、ホストに割り当てられるのは `512 - 2 = 510` 個

**「/の後ろはネットワーク部」「ホスト数を聞かれたら通常は2を引く」**が判断基準です。

## 直感的な説明

IPアドレスを、住所の「町名」と「家の番号」に分けるイメージです。

- **ネットワーク部**：どのネットワーク（町）かを示す
- **ホスト部**：そのネットワーク内のどの機器（家）かを示す

IPv4は全部で32ビット。色分けすると、`/23` の意味が見えます。

<div style="border:1px solid #d2d9de;border-radius:12px;padding:14px;margin:1em 0;background:#f8fafb;color:#24313b;">
  <p style="margin:0 0 10px;font-weight:700;">192.168.0.0/23 の32ビット</p>
  <div style="display:flex;gap:3px;width:100%;font-size:12px;line-height:1.4;text-align:center;">
    <div style="flex:23;background:#477c94;color:#fff;border-radius:7px 0 0 7px;padding:10px 2px;">ネットワーク部<br><strong>23ビット</strong></div>
    <div style="flex:9;background:#e5b978;color:#292b30;border-radius:0 7px 7px 0;padding:10px 2px;">ホスト部<br><strong>9ビット</strong></div>
  </div>
  <p style="text-align:center;margin:10px 0 0;"><strong>32 - 23 = 9ビット</strong></p>
</div>

ホスト部が1ビット増えると、表現できるアドレスの総数は**2倍**になります。

<div style="border:1px solid #d2d9de;border-radius:12px;padding:14px;margin:1em 0;background:#f8fafb;color:#24313b;">
  <p style="margin:0 0 10px;font-weight:700;">/24 と /23 の比較</p>
  <div style="display:grid;grid-template-columns:40px 1fr;gap:9px;align-items:center;">
    <strong>/24</strong><div style="display:flex;height:38px;gap:2px;"><div style="flex:24;background:#477c94;border-radius:5px 0 0 5px;"></div><div style="flex:8;background:#e5b978;border-radius:0 5px 5px 0;"></div></div>
    <strong>/23</strong><div style="display:flex;height:38px;gap:2px;"><div style="flex:23;background:#477c94;border-radius:5px 0 0 5px;"></div><div style="flex:9;background:#e5b978;border-radius:0 5px 5px 0;"></div></div>
  </div>
  <p style="margin:10px 0 0;font-size:0.9em;">青：ネットワーク部　黄：ホスト部</p>
  <p style="margin:6px 0 0;">/24 → 256個（使用可能254個）<br>/23 → 512個（使用可能510個）</p>
</div>

## 定義・仕組み

### CIDR表記とサブネットマスク

`192.168.0.0/23` の `/23` は、先頭23ビットがネットワーク部であることを示す**プレフィックス長**です。

`/23` のサブネットマスクは `255.255.254.0` です。

```text
サブネットマスク（2進数）
11111111.11111111.11111110.00000000
|---------- 23ビット --------|-- 9 --|
```

マスクの `1` がネットワーク部、`0` がホスト部です。

### 512個のうち、なぜ510個なのか

`192.168.0.0/23` は、`192.168.0.0` から `192.168.1.255` までを含みます。

<div style="border:1px solid #d2d9de;border-radius:12px;padding:14px;margin:1em 0;background:#f8fafb;color:#24313b;">
  <p style="font-weight:700;margin:0 0 10px;">アドレス範囲の見取り図</p>
  <div style="display:grid;grid-template-columns:minmax(0,1fr) auto;gap:0;border:1px solid #cbd5db;border-radius:8px;overflow:hidden;font-size:0.88em;">
    <div style="padding:10px;background:#dfe8ee;">192.168.0.0<br><strong>ネットワークアドレス</strong></div><div style="padding:10px;background:#dfe8ee;align-content:center;">使用不可</div>
    <div style="padding:10px;background:#e4f1e9;">192.168.0.1 ～ 192.168.1.254<br><strong>ホストに割り当て可能</strong></div><div style="padding:10px;background:#e4f1e9;align-content:center;"><strong>510個</strong></div>
    <div style="padding:10px;background:#f3e6d7;">192.168.1.255<br><strong>ブロードキャストアドレス</strong></div><div style="padding:10px;background:#f3e6d7;align-content:center;">使用不可</div>
  </div>
  <p style="margin:10px 0 0;text-align:center;"><strong>512個 - 2個 = 510個</strong></p>
</div>

ネットワークアドレスはネットワークそのものを表し、ブロードキャストアドレスは同じサブネット内の機器へ一斉送信するために使います。

※この「2を引く」計算は、通常のIPv4サブネットのホスト数を求める場合のルールです。ポイントツーポイントリンクの `/31` や単一アドレスの `/32` は例外です。

## 科目Aでどう出る？

出題されやすいのは、CIDR表記から**ホスト部のビット数と使用可能なアドレス数**を求める問題です。

| プレフィックス | ホスト部 | アドレス総数 | 通常の使用可能数 |
|---|---:|---:|---:|
| /25 | 7ビット | 128 | 126 |
| /24 | 8ビット | 256 | 254 |
| /23 | 9ビット | 512 | 510 |
| /22 | 10ビット | 1,024 | 1,022 |

計算手順は `32 - プレフィックス長 → 2の累乗 → 2を引く` です。

たとえば `/26` なら、`32 - 26 = 6`、`2^6 - 2 = 62` 個です。

**選択肢を切るポイント**：`/23` に対して「254個」を選ぶのは、`/24` のホスト数との混同です。また「512個」はアドレス総数であり、通常のホスト割当可能数ではありません。

## どんな場面で使う？

社内LANや機器ネットワークを設計するとき、必要な端末数に合わせてサブネットを分けます。

たとえば、300台の機器にIPv4アドレスを割り当てる場合、`/24` の254個では足りませんが、`/23` なら510個を割り当てられます。

実務では機器の増設余地やネットワーク構成も考慮しますが、FE試験ではまず**必要なホスト数を収容できるか**を判断します。

## よくある誤解・混同

- **誤解：`/23` はホスト部が23ビット。** → 23ビットはネットワーク部。ホスト部は9ビットです。
- **誤解：`/23` は512台に割り当てられる。** → 通常のサブネットでは2アドレスを除くので510台分です。
- **誤解：`/23` は `192.168.0.x` だけを含む。** → `192.168.0.0/23` は `192.168.1.x` も含みます。
- **誤解：プレフィックス長が大きいほどホスト数が増える。** → 逆です。ネットワーク部が増えるほどホスト部は減ります。

### 確認問題

通常のIPv4サブネットで、`10.0.0.0/25` に割り当て可能なホストアドレスは何個でしょうか。

<details markdown="1">
<summary>▶ 答えと計算手順を見る</summary>

**126個**です。

`32 - 25 = 7` ビット、`2^7 = 128` 個。ネットワークアドレスとブロードキャストアドレスを除いて `128 - 2 = 126` 個です。

</details>

## まとめ（試験直前用）

- `/n` の `n` は**ネットワーク部のビット数**
- ホスト部は `32 - n`、総数は `2^(32-n)`
- 通常の使用可能ホスト数は**総数から2を引く**

```text
/23 → 32 - 23 = 9
    → 2^9 = 512
    → 512 - 2 = 510個
```

{% include fe_article_footer.html %}
