---
layout: page
title: バーンダウンチャートとは？バーンアップとの違いと進捗の読み方【基本情報技術者試験】
description: バーンダウンチャートの縦軸は残作業量、横軸は時間。バーンアップとの違い、予定線と実績線の読み方、残課題件数や延べ工数との混同をFE科目A向けに整理します。
permalink: /fe/burndown-chart/
tags: [fe, fe-management, project-management, agile]
fe_section: マネジメント系
fe_subsection: プロジェクトマネジメント
fe_order: 30
date: 2026-10-16
last_modified_at: 2026-10-16
---

## まず結論

**バーンダウンチャートは、時間の経過とともに残作業量がどれだけ減ったかを見るグラフ**です。

基本情報技術者試験では、まず縦軸と線の向きを確認します。

```text
縦軸：残作業量
横軸：時間
右下がり：残作業が減っている
→ バーンダウンチャート
```

一方、完了した作業量が増える様子を見るのは**バーンアップチャート**です。

## 直感的な説明

例えば、10日間で100時間分の作業を終える計画を考えます。

| 経過日数 | 予定の残作業量 | 実際の残作業量 |
|---|---:|---:|
| 0日 | 100時間 | 100時間 |
| 2日 | 80時間 | 90時間 |
| 4日 | 60時間 | 75時間 |
| 6日 | 40時間 | 55時間 |
| 8日 | 20時間 | 25時間 |
| 10日 | 0時間 | 0時間 |

4日目は、予定では60時間まで減っているはずですが、実際には75時間残っています。

**予定より15時間分の作業が多く残っているため、進捗が遅れている**と判断できます。

### 予定線と実績線を図で確認する

以下は学習用の例です。縦軸は残作業量、横軸は経過日数です。

<div class="fe-burndown-chart" role="img" aria-label="バーンダウンチャートの例。予定線は100時間から0時間へ減少し、実績線は途中で予定線より上にあり、作業が遅れていることを示す">
  <svg viewBox="0 0 640 320" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">
    <path d="M72 25 V268 H606" fill="none" stroke="currentColor" stroke-width="1.5"/>
    <g fill="currentColor" font-size="13" text-anchor="end">
      <text x="61" y="31">100</text><text x="61" y="89">75</text><text x="61" y="148">50</text><text x="61" y="207">25</text><text x="61" y="273">0</text>
    </g>
    <g stroke="currentColor" stroke-opacity=".13" stroke-width="1">
      <path d="M72 25 H606 M72 85 H606 M72 146 H606 M72 207 H606"/>
    </g>
    <g fill="currentColor" font-size="13" text-anchor="middle">
      <text x="72" y="291">0</text><text x="178" y="291">2</text><text x="284" y="291">4</text><text x="390" y="291">6</text><text x="496" y="291">8</text><text x="602" y="291">10</text>
      <text x="336" y="314">経過日数</text>
    </g>
    <text x="75" y="15" fill="currentColor" font-size="13">残作業量（時間）</text>
    <path d="M72 25 L178 73.6 L284 122.2 L390 170.8 L496 219.4 L602 268" fill="none" stroke="#7b9a95" stroke-width="3.5"/>
    <path d="M72 25 L178 49.3 L284 85.8 L390 134.4 L496 207.3 L602 268" fill="none" stroke="#a77962" stroke-width="3.5" stroke-linejoin="round"/>
    <g fill="#a77962"><circle cx="178" cy="49.3" r="4"/><circle cx="284" cy="85.8" r="4"/><circle cx="390" cy="134.4" r="4"/><circle cx="496" cy="207.3" r="4"/></g>
    <rect x="393" y="33" width="11" height="11" fill="#7b9a95"/><text x="411" y="43" fill="currentColor" font-size="13">予定線</text>
    <rect x="486" y="33" width="11" height="11" fill="#a77962"/><text x="504" y="43" fill="currentColor" font-size="13">実績線</text>
  </svg>
  <p class="fe-burndown-note">※数値とグラフは学習用の例です。作業の追加があれば実績線が上昇する場合もあります。</p>
</div>

<style>
.fe-burndown-chart{max-width:720px;margin:1.3rem auto;padding:.75rem;border:1px solid #aab8c3;border-radius:10px}
.fe-burndown-chart svg{width:100%;height:auto;display:block}
.fe-burndown-note{font-size:.82rem;opacity:.8;margin:.5rem 0 0}
</style>

## 定義・仕組み

バーンダウンチャートは、作業の進み具合を**残りの作業量**で示す進捗管理の手法です。

- **予定線**：計画どおりに進んだ場合の残作業量
- **実績線**：その時点で実際に残っている作業量

同じ時点で比較すると、次のように判断できます。

| 実績線の位置 | 意味 |
|---|---|
| 予定線より上 | 予定より残作業が多い → 遅れ |
| 予定線とほぼ同じ | おおむね予定どおり |
| 予定線より下 | 予定より残作業が少ない → 進み |

残作業量は時間、作業ポイントなどで表せます。**必ず時間単位でなければならないわけではありません。**

## 科目Aでどう出る？

科目Aでは、グラフの縦軸や変化の方向から、チャートの用途を選ぶ問題が考えられます。

```text
残作業量が減っていく
→ バーンダウン

完了作業量が増えていく
→ バーンアップ
```

「縦軸が残作業量」「横軸が時間」という組合せが、最も分かりやすい判断材料です。

## どんな場面で使う？

反復的に開発を進めるアジャイル開発などで、チームが進捗を共有するために使います。

例えば、毎日の終わりに残作業量を更新すると、遅れを早めに発見し、作業の分担や計画を見直せます。

ただし、**残作業量が減ったことだけで品質が保証されるわけではありません**。テストの結果や成果物の品質は別に確認する必要があります。

## よくある誤解・混同

### バーンダウンとバーンアップ

| 比較 | バーンダウン | バーンアップ |
|---|---|---|
| 縦軸 | 残作業量 | 完了した作業量 |
| 典型的な向き | 右下がり | 右上がり |
| 注目点 | あとどれだけ残るか | どれだけ終わったか |

### 残課題の件数と残作業量は同じではない

例えば、未完了の課題が3件あっても、所要時間が1時間・5時間・20時間なら、残作業量は合計26時間です。

```text
残課題の件数：3件
残作業量：26時間
```

課題の件数を数えるグラフと、作業量を測るバーンダウンチャートを混同しないようにします。

なお、チームが「残課題の件数」を作業量の代理指標として明示的に採用する場合もありますが、**試験では残作業量を示す選択肢を優先**します。

### バーンダウンと延べ工数

延べ工数は、これまで投入した作業時間などの累計です。通常は作業を進めるほど増えます。

```text
残作業量が減る
→ バーンダウン

投入した工数が積み上がる
→ 延べ工数
```

## まとめ（試験直前用）

- **残作業量 × 時間 × 減少** → バーンダウン
- **完了作業量 × 時間 × 増加** → バーンアップ
- **実績線が予定線より上** → 残作業が多く、遅れの可能性

## 公式情報・参考リンク

- [IPA：基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html)
- [Scrum.org：Burn-down Chart](https://www.scrum.org/resources/what-is-a-burndown-chart)

{% include fe_article_footer.html %}
