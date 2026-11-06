---
layout: page
title: COCOMOとは？ソフトウェア規模から工数を見積もる考え方【基本情報技術者試験】
description: COCOMOを規模と係数から工数を推定するモデルとして説明。自社の開発実績による校正、工数と工期・生産性の違い、ファンクションポイント法との区別をFE科目A向けに整理します。
permalink: /fe/cocomo-effort-estimation/
tags: [fe, fe-management, project-management]
fe_section: マネジメント系
fe_subsection: プロジェクトマネジメント
fe_order: 45
date: 2026-11-07
last_modified_at: 2026-11-07
related_articles:
  - /fe/function-point-effort/
  - /fe/function-point-method/
---

## まず結論

**COCOMO（Constructive Cost Model）は、ソフトウェアの規模や開発条件をもとに、必要な開発工数を数式で推定するモデル**です。

基本情報技術者試験（FE）科目Aでは、**「開発規模」「工数」「補正係数」「過去の生産性・実績データ」**という言葉が判断の手掛かりになります。

特に重要なのは、**標準的な係数でも概算は可能だが、自社の開発実績で係数を校正すると、実態に合った見積りに近づけられる**という点です。

このページは、COCOMOの仕組みと見積りの考え方が中心です。機能数から規模（FP）を計算する方法は[ファンクションポイント法](/fe/function-point-method/)、FPを工数に換算する計算は[FPから工数を計算する方法](/fe/function-point-effort/)で説明しています。

## 直感的な説明

例えば、製造業向けの設備監視アプリを新しく開発するとします。

過去に作ったアプリの規模と開発にかかった工数を記録しておけば、新しいアプリがどれくらいの工数になりそうか予測する際に役立ちます。

ただし、同じ規模でも、開発環境、必要な信頼性、チームの経験などが異なれば工数も変わります。

```text
開発するソフトウェアの規模
             ↓
開発条件に応じた係数で調整
             ↓
        必要な工数を推定
```

この「規模から工数を数式で推定する」考え方がCOCOMOです。

**規模（どれくらい作るか）と工数（どれくらいの作業量が必要か）は別物**です。

## 定義・仕組み

### 規模・工数・工期・生産性を区別する

| 用語 | 意味 | 例 |
|---|---|---|
| 規模 | 作るソフトウェアの大きさ | 10 KLOC（約1万行） |
| 工数 | 開発に必要な作業の総量 | 30人月 |
| 工期 | 開始から完了までの期間 | 6か月 |
| 生産性 | 一定工数で開発できる規模 | 1人月あたりのKLOCなど |

例えば、30人月という工数は、**30人で必ず1か月で終わる**という意味ではありません。人数を増やすと連絡・教育・調整の負担も増えるため、工数と工期は区別します。

### COCOMOの計算モデル

初期の基本COCOMOの考え方は、概略として次の式で表せます。

```text
見積工数（人月） = a ×（開発規模［KLOC］）^b
```

- **KLOC**：プログラム約1,000行を単位とする規模
- **a・b**：モデルや開発特性に応じて定める係数
- **人月**：作業量の単位

COCOMOには複数のモデルがあり、COCOMO IIでは規模の指数や工数乗数（努力係数）などを使ってさらに調整します。**すべてのCOCOMOが同じ単純な式で計算するわけではありません。**

### 独自の数値例：係数が変わると見積りはどうなる？

仕組みを理解するため、上の式で指数 `b = 1` と仮定し、規模を10 KLOCとした単純な例を考えます。

| 仮定した係数a | 見積工数 |
|---:|---:|
| 2.0 | 20人月 |
| 2.5 | 25人月 |
| 3.0 | 30人月 |

例えば `a = 2.5` なら、

```text
2.5 × 10^1 = 25人月
```

となります。

**これは係数の影響を示すための説明用モデルで、実在するCOCOMOの標準係数や正式な見積結果ではありません。** 重要なのは、同じ規模でも係数の設定によって工数が変わることです。

### 標準係数と自社実績による校正

<figure class="fe-cocomo-diagram" aria-labelledby="fe-cocomo-diagram-title">
  <figcaption id="fe-cocomo-diagram-title"><strong>COCOMOの見積りと実績による見直し</strong></figcaption>
  <div class="fe-cocomo-diagram__steps">
    <div class="fe-cocomo-diagram__step"><strong>① 規模・開発条件</strong><span>新しいプロジェクトの規模や必要な信頼性など</span></div>
    <div class="fe-cocomo-diagram__arrow" aria-hidden="true">↓</div>
    <div class="fe-cocomo-diagram__step"><strong>② 係数を設定して見積り</strong><span>標準係数、または実績で校正した係数を使う</span></div>
    <div class="fe-cocomo-diagram__arrow" aria-hidden="true">↓</div>
    <div class="fe-cocomo-diagram__step"><strong>③ 工数の見積値</strong><span>必要な作業量を人月などで推定する</span></div>
    <div class="fe-cocomo-diagram__arrow" aria-hidden="true">↓</div>
    <div class="fe-cocomo-diagram__step"><strong>④ 実績を記録して次回に活用</strong><span>実際の規模・工数とのずれを調べ、モデルを見直す</span></div>
  </div>
</figure>

<style>
.fe-cocomo-diagram{max-width:620px;margin:1.2rem auto;padding:1rem;border:1px solid #b8c5ce;border-radius:12px;background:#f7f9fb;color:#223744}
.fe-cocomo-diagram figcaption{font-size:1rem;line-height:1.6;margin-bottom:.9rem}
.fe-cocomo-diagram__steps{display:flex;flex-direction:column;align-items:stretch;gap:0}
.fe-cocomo-diagram__step{background:#fff;border:1px solid #a7bdcd;border-radius:8px;padding:.8rem;display:flex;flex-direction:column;gap:.3rem;min-width:0}
.fe-cocomo-diagram__step strong{color:#214b68;font-size:.95rem}
.fe-cocomo-diagram__step span{font-size:.87rem;line-height:1.6;color:#344957}
.fe-cocomo-diagram__arrow{text-align:center;color:#225d8a;font-weight:bold;font-size:1.2rem;line-height:1.5}
</style>

実績データで係数を調整することを、**校正（calibration）**といいます。

COCOMO IIのモデルマニュアルには、組織の環境に合わせた係数の校正で推定精度を改善できることが示されています。

ここで注意したいのが「COCOMOには自社の生産性データが不可欠」という説明です。FEの用語問題では、**実績データを使って見積りを現場に合わせる**という考え方が正解の判断につながることがあります。しかし厳密には、**自社データがなければCOCOMOを一切計算できないわけではありません**。標準係数を使った概算と、蓄積データを用いた校正を区別しましょう。

### 見積工数と実績工数の差は何に役立つ？

見積りと実績の差が大きい場合、次のような点を確認できます。

- 要件変更などで作業が増えていなかったか
- 想定した生産性と実際の生産性が違わなかったか
- 手戻りや不具合修正が増えていなかったか
- 次回の見積モデルをどう補正するか

見積工数は進捗管理だけでなく、**品質や開発プロセスを調査する際の手掛かり**にもなります。ただし、工数の超過だけで品質不良だと断定はできません。

## 科目Aでどう出る？

### ほかの見積手法との違い

| 手法 | 主な着眼点 |
|---|---|
| **COCOMO** | **ソフトウェア規模・開発特性などから工数をモデルで推定** |
| ファンクションポイント（FP）法 | 入出力、ファイル、照会など利用者から見た機能量を測定 |
| プログラムステップ法 | ソースコードの行数・ステップ数を基準に規模を見積もる |
| 類推見積法 | 類似した過去のプロジェクトを参考にする |
| 標準タスク法 | 作業を分解し、個々の標準工数を積み上げる |

注意点として、**COCOMOでも過去の実績を活用します**。類推見積法は「過去の似た案件を直接参考にする」ことが中心で、COCOMOは「規模や係数を使う数理モデル」であることが違いです。

また、FP法で求めた機能規模を工数に換算するには、生産性などの情報が必要です。FP値そのものは人月ではありません。

### 判断するための確認問題（独自例）

ある開発部門では、新しい業務アプリケーションの工数を見積もる際、プログラム規模と開発条件を数式に代入して工数を推定した。さらに過去のプロジェクトについて、見積工数と実績工数を比較し、次回の推定に用いる係数を見直した。この方法の説明として適切なのはどれか。

- ア：機能の入出力数だけを数えれば、工数が自動的に確定する。
- イ：規模と開発条件を使ったモデルを、開発実績で校正している。
- ウ：過去の実績があっても、工数の予測には一切利用できない。
- エ：工数の見積りと実績を比べれば、品質の良否を必ず断定できる。

<details markdown="1">
<summary>答えと解説を見る（タップして開く）</summary>

**正解：イ**

規模と開発特性から工数を推定する数理モデルを使い、その係数を実績で校正する考え方です。

アはFP法の機能規模と工数を混同しています。ウは実績データの有用性を否定しており誤りです。エは、工数の差から品質を必ず断定できるわけではないため誤りです。

</details>

## どんな場面で使う？

開発の初期段階で、予算・要員数・スケジュールを検討するときに工数見積りを利用します。

例えば設備監視ソフトウェアの新規開発を計画する場合、開発規模、要求される信頼性、過去の類似開発の規模・工数などを整理して見積りに活用できます。

ただし、見積りはあくまで予測です。要件変更や未知の技術課題などによって実際の工数が変わるため、進捗に応じて再評価します。

## よくある誤解・混同

### COCOMOには必ず自社のデータが必要？

**標準係数でも概算はできます。** 自社実績に基づく校正は、組織固有の生産性や開発条件を反映して見積り精度の改善を目指すためのものです。「利用できるか」と「実務で精度を高められるか」を分けて理解します。

### 開発規模が同じなら、工数は同じ？

開発者の経験、要求される信頼性、開発環境などの条件が異なれば工数も変わります。規模だけで一意には決まりません。

### 20人月なら、20人で1か月で終わる？

工数は人員と期間の単純な掛け算として捉えられますが、実際の工程には依存関係や調整があるため、人数を増やしても工期が比例して短くなるとは限りません。

### FP法もCOCOMOと同じ？

**FP法はまず機能規模を測る方法、COCOMOは規模などから工数を推定するモデル**です。関係はありますが、目的を区別することが重要です。

### 見積りと実績の差が大きいと必ず品質が悪い？

そうとは限りません。要求変更、経験不足、予想外のトラブルなど、さまざまな理由があり得ます。差を分析し、改善につなげます。

## まとめ（試験直前用）

- **COCOMO：ソフトウェア規模や条件から工数を数式で推定するモデル**
- **規模・工数・工期・生産性は別の量**
- 標準係数でも計算可能。実績データで**校正**すると実態に合う見積りを目指せる
- 工数見積りは進捗管理のほか、品質やプロセス改善の手掛かりにもなる
- FP法は利用者から見た機能規模、プログラムステップ法はコード規模に着目する
- 同じ規模でも条件によって工数は変わる

## 一次情報・参考資料

- [IPA：ソフトウェア開発における見積り手法（COCOMO法を含む）](https://www.ipa.go.jp/archive/digital/iot-en-ci/teiryou/ent01-c.html)
- [COCOMO II Model Definition Manual, Version 2.1（USC Center for Software Engineering）](https://info.usherbrooke.ca/llavoie/enseignement/References/CocomoII_Model_Manual.pdf)
- [IPA：ソフトウェア開発データ白書シリーズのFAQ](https://www.ipa.go.jp/archive/publish/wp-sd/qa.html)
- [IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html)

{% include fe_article_footer.html %}
