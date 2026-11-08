---
layout: page
title: ソーシャルメディアとは？利用者同士で情報を発信・共有する仕組み【基本情報技術者試験】
description: ソーシャルメディアを利用者同士の投稿・交流・共有を支えるメディアとして整理し、SNS・CGM・UGCやアフィリエイト・検索連動型広告との違いをFE科目A向けに解説します。
permalink: /fe/social-media/
tags: [fe, fe-strategy, business-strategy, marketing]
fe_section: ストラテジ系
fe_subsection: 経営戦略
fe_order: 57
date: 2026-11-08
last_modified_at: 2026-11-08
related_articles:
  - /fe/cgm/
  - /fe/relationship-marketing/
---

## まず結論

**ソーシャルメディア（Social Media）**とは、利用者が情報を投稿し、ほかの利用者との交流・共有・反応を通じて情報が広がるインターネット上のメディアです。

基本情報技術者試験の科目Aでは、**「利用者同士のつながり」「投稿」「共有・拡散」ならソーシャルメディア**と考えます。広告の配信方法や、商品を紹介して報酬を受け取る仕組みとは区別しましょう。

この記事は**利用者同士の情報のつながり**を主題にします。投稿を作る主体に注目するCGMの説明は[CGMとは？](/fe/cgm/)で確認できます。

## 直感的な説明

たとえば、ある人が「工場の設備保全で役立った工夫」をSNSへ投稿したとします。

その投稿を見た別の人がコメントし、さらに別の人が共有すると、投稿者だけでは届かなかった人にも情報が伝わる可能性があります。

<div class="fe-social-flow" role="group" aria-label="利用者Aが投稿し、BとCが反応・共有すると、ほかの利用者にも情報が伝わる様子を表した模式図">
  <div class="fe-social-flow__person"><strong>利用者A</strong><span>情報を投稿する</span></div>
  <div class="fe-social-flow__arrow" aria-hidden="true">↓</div>
  <div class="fe-social-flow__middle">
    <div class="fe-social-flow__person"><strong>利用者B</strong><span>コメントする</span></div>
    <div class="fe-social-flow__person"><strong>利用者C</strong><span>共有する</span></div>
  </div>
  <div class="fe-social-flow__arrow" aria-hidden="true">↓</div>
  <div class="fe-social-flow__person fe-social-flow__person--end"><strong>別の利用者へ届く</strong><span>閲覧・交流が広がる場合がある</span></div>
</div>

<style>
.fe-social-flow{margin:1rem 0;padding:1rem;border:1px solid #aebbc7;border-radius:10px;display:flex;flex-direction:column;align-items:center;gap:.4rem;color:#253748;background:#f7f9fc}
.fe-social-flow__person{box-sizing:border-box;max-width:100%;width:230px;display:flex;flex-direction:column;align-items:center;gap:.3rem;background:#fff;border:1px solid #a9bdce;border-radius:8px;padding:.7rem .6rem;text-align:center}
.fe-social-flow__person span{font-size:.88rem;line-height:1.5}
.fe-social-flow__middle{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:.7rem;width:100%;max-width:480px}
.fe-social-flow__middle .fe-social-flow__person{width:auto}
.fe-social-flow__arrow{font-size:1.25rem;font-weight:700;line-height:1.1;color:#345e7c}
.fe-social-flow__person--end{background:#eaf5ef;border-color:#76a48a}
@media(max-width:420px){.fe-social-flow{padding:.7rem}.fe-social-flow__middle{gap:.4rem}.fe-social-flow__person{padding:.65rem .35rem;font-size:.92rem}}
</style>

この図は情報の伝わり方を単純化したものです。**すべての投稿が必ず拡散されるわけではありません。**

大切なのは、発信者と受信者が固定されず、利用者が**読む側にも発信する側にもなれる**ことです。

## 定義・仕組み

ソーシャルメディアでは、利用者による投稿を、ほかの利用者が閲覧・返信・共有できる仕組みが提供されます。代表例にはSNS、ブログ、動画投稿サービス、コミュニティ型のサービスなどがあります。

### SNS・CGM・UGCとの関係

これらは関連しますが、注目するポイントが異なります。

| 用語 | 注目するもの | イメージ |
|---|---|---|
| **ソーシャルメディア** | 利用者同士の情報発信・交流・共有の仕組み | 投稿を読んで返信・共有する |
| SNS（Social Networking Service） | 人と人のつながりを支援するサービス | フォロー・交流する |
| CGM（Consumer Generated Media） | 消費者・利用者の投稿を中心に成り立つメディア | 口コミサイトなど |
| UGC（User Generated Content） | 利用者が作成したコンテンツそのもの | 投稿した口コミ・画像・動画 |

例えば、利用者が作成したレビューは**UGC**で、それを中心に成り立つレビューサイトは**CGM**の例です。SNS上でレビューを共有し意見交換するなら**ソーシャルメディア**の特徴も表れます。

これらは**重なり合う概念**です。SNSがソーシャルメディアの代表例であっても、すべての投稿がCGMに分類されるとは限りません（企業の公式広告なども含まれるため）。

投稿の作り手に注目したい場合は、[CGMの記事](/fe/cgm/)を参照してください。

## 科目Aでどう出る？

科目Aでは、情報がどのように広がるのか、広告がどの条件で表示されるのか、紹介者にどのように報酬が発生するのかを見分けます。

| 用語 | 仕組みを見分ける手掛かり |
|---|---|
| **ソーシャルメディア** | **利用者同士のつながり、投稿、交流、共有** |
| アフィリエイト | 商品やサービスを紹介し、購入などの成果に応じて報酬を受け取る |
| 位置情報連動型広告 | 利用者の位置情報などを利用して近隣店舗などの広告を表示する |
| 検索連動型広告 | 検索されたキーワードに関連する広告を表示する |

例えば、利用者が写真を投稿し、別の利用者が感想を返信したり共有したりする仕組みは**ソーシャルメディア**です。一方、商品を紹介して購入成果に応じた報酬を得るなら**アフィリエイト**であり、情報の共有と収益化の仕組みは別です。

**「広告が出るSNS」もありますが、SNS＝広告方式ではありません。** メディアの性質と広告の配信方法を分けて考えると選択肢を判断しやすくなります。

### 独自の確認問題

あるWebサービスでは、利用者が自分の作った料理の写真を投稿でき、ほかの利用者がコメントしたり、その投稿を共有したりできる。最もよく表している特徴はどれか。

- A. 検索キーワードに応じて広告を表示する
- B. 利用者が投稿し、交流・共有を通して情報が広がる
- C. 購入などの成果に応じて紹介者へ報酬を支払う
- D. 利用者の現在地に応じて近くの店舗の広告を配信する

<details markdown="1">
<summary>答えと解説を見る</summary>

**正解：B**

利用者が情報を発信し、コメント・共有を通じて交流する点が、ソーシャルメディアの特徴です。

- Aは検索連動型広告
- Cはアフィリエイト
- Dは位置情報連動型広告

です。設問の料理写真は独自の例であり、元の過去問の選択肢を転載していません。

</details>

## どんな場面で使う？

### 利用者による情報発信

技術情報や趣味の記事をSNSで紹介すると、興味を持った利用者が閲覧し、コメントや共有を行うことがあります。企業や自治体も公式アカウントを使って情報を発信できます。

### 企業のマーケティング

企業はSNSなどを通じて顧客の意見を把握したり、製品への反応を確かめたりできます。ただし、**ソーシャルメディア自体と、有料広告を配信する手法は別の概念**です。

また、利用者が投稿した内容が常に正しいとは限りません。口コミや共有された情報は、発信者・根拠・日付などを確認して扱いましょう。

## よくある誤解・混同

### SNSに広告があるので、ソーシャルメディアは広告手法？

違います。SNSというサービス上で広告が配信される場合はありますが、**利用者同士の交流を支える仕組み**と、**広告を表示する条件**は分けて考えます。

### ソーシャルメディアは必ず大人数に拡散される？

違います。共有・拡散が可能な仕組みでも、実際の到達範囲はサービスの設定や利用状況などに左右されます。

### ソーシャルメディアとCGMは同じ？

重なる範囲はありますが、比較する観点が違います。**ソーシャルメディアは交流・共有、CGMは投稿の作り手**に注目すると整理しやすくなります。

## まとめ（試験直前用）

- **ソーシャルメディア＝利用者が情報を投稿し、交流・共有できるメディア**
- **SNS＝利用者同士のつながりを支えるサービス**
- **CGM＝利用者の投稿を中心にしたメディア、UGC＝投稿されたコンテンツ**
- **アフィリエイト＝成果報酬、検索連動型広告＝検索語、位置情報連動型広告＝位置情報**
- **情報共有の仕組み**と**広告・収益化の仕組み**を区別する

{% include fe_article_footer.html %}
