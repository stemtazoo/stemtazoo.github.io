---
layout: page
title: 直流給電とは？データセンターで電力変換の損失を減らす仕組み【基本情報技術者試験】
description: 直流給電の利点を、交流給電との電力経路の比較図と変換効率の数値例で理解し、UPSや電圧変換に関するFE科目Aの誤答を見分けます。
permalink: /fe/dc-power-feeding/
tags: [fe, fe-technology, computer-system]
fe_section: テクノロジ系
fe_subsection: コンピュータシステム
fe_order: 46
date: 2026-10-11
last_modified_at: 2026-10-11
related_articles:
  - /fe/ups/
  - /fe/electric-power-energy-wh/
---

## まず結論

**直流給電（DC給電）は、サーバなどに直流で電力を供給し、交流と直流の変換回数を減らして電力損失を抑える方式**です。

基本情報技術者試験（FE）の科目Aでは、次の対応で判断します。

> **交流↔直流の変換回数を減らす → 変換に伴う電力損失を減らせる**

ただし、**直流給電なら電圧変換もUPSも不要になる**という意味ではありません。

## 直感的な説明

サーバの内部回路は、基本的に直流で動作します。一方、一般的な商用電源は交流です。

そこで、給電経路に交流と直流を変換する装置が入ります。変換するたびに、入力した電力の一部が熱などになって失われます。

### 交流給電と直流給電を見比べる

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:1rem;margin:1rem 0;">
  <section style="border:1px solid #a7b7c6;border-radius:12px;padding:1rem;">
    <h4 style="margin:0 0 .8rem;">交流給電の一例</h4>
    <div style="background:#e9f0f6;padding:.65rem;border-radius:8px;text-align:center;">商用電源（交流）</div>
    <p style="text-align:center;margin:.45rem 0;">↓ <strong>AC → DC</strong></p>
    <div style="background:#f7e9df;padding:.65rem;border-radius:8px;text-align:center;">UPS（直流で蓄電）</div>
    <p style="text-align:center;margin:.45rem 0;">↓ <strong>DC → AC</strong></p>
    <div style="background:#e9f0f6;padding:.65rem;border-radius:8px;text-align:center;">交流で給電</div>
    <p style="text-align:center;margin:.45rem 0;">↓ <strong>AC → DC</strong></p>
    <div style="background:#e6efe7;padding:.65rem;border-radius:8px;text-align:center;">サーバ内部（直流）</div>
    <p style="font-size:.88rem;margin:.8rem 0 0;">例では交流・直流の変換が3回あります。</p>
  </section>
  <section style="border:1px solid #a7b7c6;border-radius:12px;padding:1rem;">
    <h4 style="margin:0 0 .8rem;">直流給電の一例</h4>
    <div style="background:#e9f0f6;padding:.65rem;border-radius:8px;text-align:center;">商用電源（交流）</div>
    <p style="text-align:center;margin:.45rem 0;">↓ <strong>AC → DC</strong></p>
    <div style="background:#f7e9df;padding:.65rem;border-radius:8px;text-align:center;">直流給電設備・蓄電池</div>
    <p style="text-align:center;margin:.45rem 0;">↓ <strong>直流のまま給電</strong></p>
    <div style="background:#e6efe7;padding:.65rem;border-radius:8px;text-align:center;">直流対応サーバ</div>
    <p style="font-size:.88rem;margin:.8rem 0 0;">交流へ戻す変換を省ける構成です。</p>
  </section>
</div>

**見るポイント：** 直流給電の利点は、電源の種類そのものよりも、途中で繰り返す変換を減らせることです。

※ どちらも説明用の構成例です。UPSの方式や電源設備によって実際の変換経路は異なり、直流給電でもDC-DC変換などが必要になる場合があります。

## 定義・仕組み

### なぜ変換回数が少ないとよいのか

電力変換装置の効率が100%でない場合、変換のたびに電力の一部が失われます。

たとえば、**各変換の効率を90%と仮定**すると、100Wを入力したときの電力は次のようになります。

| 変換 | 残る電力 |
|---|---:|
| 入力時 | 100W |
| 1回目 | 90W |
| 2回目 | 81W |
| 3回目 | 72.9W |

<div style="border:1px solid #a7b7c6;border-radius:12px;padding:1rem;margin:1rem 0;">
  <p style="font-weight:600;margin:0 0 .75rem;">変換を重ねたときの電力（仮定例）</p>
  <div style="margin:.5rem 0;">入力 100W<div style="background:#e7edf3;border-radius:6px;overflow:hidden;"><div style="background:#718da6;width:100%;height:18px;"></div></div></div>
  <div style="margin:.5rem 0;">1回後 90W<div style="background:#e7edf3;border-radius:6px;overflow:hidden;"><div style="background:#718da6;width:90%;height:18px;"></div></div></div>
  <div style="margin:.5rem 0;">2回後 81W<div style="background:#e7edf3;border-radius:6px;overflow:hidden;"><div style="background:#718da6;width:81%;height:18px;"></div></div></div>
  <div style="margin:.5rem 0;">3回後 72.9W<div style="background:#e7edf3;border-radius:6px;overflow:hidden;"><div style="background:#718da6;width:72.9%;height:18px;"></div></div></div>
  <p style="font-size:.88rem;margin:.75rem 0 0;">各回の効率を90%と仮定した模式例。実際の設備の効率を示すものではありません。</p>
</div>

計算は「100 × 0.9 × 0.9 × 0.9 = 72.9」です。

同じ効率の変換を何度も通ると、損失が積み重なります。ただし、**実際にどちらの方式が高効率かは、装置の性能・電圧・配線損失なども含めて判断**します。

### 直流でも電圧変換は必要

サーバの内部では、CPUなどの部品ごとに必要な電圧が異なります。

直流給電を採用しても、DC-DCコンバータなどで電圧を調整する場合があります。

**交流・直流の変換を減らすこと**と、**すべての電圧変換をなくすこと**は別です。

## 科目Aでどう出る？

科目Aでは、直流給電の利点を選ばせる問題で、次のように判断します。

| 選択肢にある説明 | 判断 |
|---|---|
| 交流・直流の変換回数を減らし、変換損失を低減する | **正しい** |
| 受電設備からCPUまで同じ電圧で給電できる | 誤り。電圧変換が必要な場合がある |
| 停電の危険がなくなり、蓄電池が不要になる | 誤り。停電対策は別に必要 |
| トランスだけで直流を簡単に昇圧・降圧できる | 誤り。通常の変圧器は交流の変圧に用いる |

**「変換損失の削減」は利点ですが、「変換が一切不要」は言い過ぎ**と覚えます。

## どんな場面で使う？

データセンターでは、多数のサーバやネットワーク機器へ電力を供給します。

1台あたりの変換損失が小さくても、機器が多い環境では全体の電力消費や発熱に影響します。

直流給電は、設備全体の給電効率を改善するための選択肢の一つです。

一方、停電や瞬断への対応は給電方式とは別の課題です。電源を一時的に確保する装置の役割は、[UPSとは？](/fe/ups/)で確認できます。

## よくある誤解・混同

### 誤解1：直流給電なら電力損失がゼロになる

直流給電でも配線や電圧変換などで損失が発生します。

**変換損失を減らせることと、損失がなくなることは違います。**

### 誤解2：直流給電ならUPSは不要

直流給電は**電力の供給方式**、UPSは**停電・瞬断時に一時的に電力を供給する装置**です。

直流給電でも、必要な可用性に応じて蓄電池やバックアップ電源を用意します。

### 誤解3：直流はトランスで簡単に変圧できる

一般的なトランス（変圧器）は交流を利用します。

直流の電圧を変えるには、DC-DCコンバータなどの電子回路を使います。

### 誤解4：直流給電は必ず交流給電より高効率

変換回数を減らせる利点はありますが、設備の構成や各装置の効率、配線条件によって結果は変わります。

FE試験ではまず、**変換回数を減らすことが狙い**だと判断します。

## まとめ（試験直前用）

- **直流給電の利点：** 交流・直流の変換回数を減らし、変換損失を抑える
- **電圧変換：** 直流給電でも必要な場合がある
- **停電対策：** 直流給電とUPSは役割が異なる

> **「変換を減らす」は正しい。「変換もUPSも全部不要」は誤り。**

{% include fe_article_footer.html %}
