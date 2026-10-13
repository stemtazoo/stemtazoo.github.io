---
layout: page
title: リスクアセスメントとは？特定・分析・評価と対応の違い【FE試験】
description: "リスクアセスメントの3プロセス（特定・分析・評価）とリスク対応の違いを、設備故障の例と図解で整理。基本情報技術者試験の選択肢を切る判断基準を解説します。"
permalink: /fe/risk-assessment-process/
tags: [fe, fe-management, risk-management, risk-assessment]
fe_section: マネジメント系
fe_subsection: プロジェクトマネジメント
fe_order: 370
date: 2026-10-13
last_modified_at: 2026-10-13
---

## まず結論

**リスクアセスメントは「リスク特定 → リスク分析 → リスク評価」の3プロセス**です。

- **特定**：どんなリスクがあるか見つける
- **分析**：起こりやすさや影響を調べる
- **評価**：基準と比較し、対応が必要か判断する

**リスク対応はアセスメントに含まれません。** FE試験では「特定・分析・評価」と「対応・受容」を分けて考えると、選択肢を切れます。

---

## 直感的な説明

設備の故障リスクを例にします。

| プロセス | 考えること | 例 |
|---|---|---|
| リスク特定 | 何が起きる？ | 軸受が破損する可能性 |
| リスク分析 | どのくらい危険？ | 発生可能性と停止時の影響を調べる |
| リスク評価 | 対応が必要？ | 許容基準と比較して優先度を決める |
| リスク対応 | どう対処する？ | 振動監視や予防交換を実施する |

つまり、**危険を調べて判断するところまでがアセスメント、実際の対策はその次**です。

---

## 定義・仕組み

### 3つのプロセスを図で整理

<div class="fe-risk-flow" role="img" aria-label="リスク基準の確立の後、リスクアセスメントとして特定、分析、評価を実施し、その後にリスク対応を行う流れ">
  <div class="fe-risk-flow__step">リスク基準の確立<span>どこまで許容するかを決める</span></div>
  <div class="fe-risk-flow__arrow" aria-hidden="true">↓</div>
  <div class="fe-risk-flow__assessment">
    <strong>リスクアセスメント</strong>
    <div class="fe-risk-flow__step">① リスク特定<span>危険を見つける</span></div>
    <div class="fe-risk-flow__arrow" aria-hidden="true">↓</div>
    <div class="fe-risk-flow__step">② リスク分析<span>起こりやすさ・影響を調べる</span></div>
    <div class="fe-risk-flow__arrow" aria-hidden="true">↓</div>
    <div class="fe-risk-flow__step">③ リスク評価<span>基準と比較して判断する</span></div>
  </div>
  <div class="fe-risk-flow__arrow" aria-hidden="true">↓</div>
  <div class="fe-risk-flow__step fe-risk-flow__response">リスク対応<span>対策を選び、実施する（アセスメントの外）</span></div>
</div>

<style>
.fe-risk-flow{max-width:560px;margin:1.5rem auto;text-align:center;font-size:1rem;line-height:1.5}
.fe-risk-flow__assessment{padding:1rem;border:2px solid #648c96;border-radius:12px;background:#f1f7f8;color:#223b41}
.fe-risk-flow__assessment>strong{display:block;margin-bottom:.8rem}
.fe-risk-flow__step{padding:.7rem .8rem;border:1px solid #b4c6c9;border-radius:8px;background:#fff;color:#24363a;font-weight:650}
.fe-risk-flow__step span{display:block;margin-top:.2rem;font-size:.85rem;font-weight:400}
.fe-risk-flow__arrow{padding:.25rem 0;color:#597780;font-weight:700}
.fe-risk-flow__response{border-style:dashed;border-color:#9b866d;background:#f8f5ef}
@media(prefers-color-scheme:dark){.fe-risk-flow__assessment{background:#21363a;color:#edf3f3}.fe-risk-flow__step{background:#253136;color:#f1f4f4}.fe-risk-flow__response{background:#393329}}
</style>

※これは学習用の単純化した流れです。実務のリスクマネジメントでは、コミュニケーション、モニタリング、見直しなども並行・反復して行います。

### リスク分析とリスク評価は違う

- **分析**：発生可能性や影響などから、リスクの性質・大きさを理解する
- **評価**：分析結果を事前に定めたリスク基準と比較し、対応の必要性を判断する

「リスクの大きさを調べる」は分析、「許容できるか決める」は評価です。

### リスク受容はどこに入る？

**リスク受容**は、特定のリスクを引き受ける意思決定です。評価結果を踏まえた判断であり、アセスメントの3要素の一つではありません。リスクを受容する場合も、その後の監視・見直しが不要になるとは限りません。

---

## どんな場面で使う？

システム開発、設備保全、情報セキュリティなどで、リスクの優先順位を決めるときに役立ちます。

例えばサーバ停止のリスクを特定したら、停止頻度と業務への影響を分析し、許容基準と比較して評価します。必要と判断すれば、冗長化やバックアップなどの対応策を検討します。

---

## よくある誤解・混同

### ❌ リスク対応もアセスメントの一部

**対応は別のプロセス**です。選択肢に「特定・分析・評価」がそろっているかを最初に確認します。

### ❌ リスク分析とリスク評価は同じ

分析はリスクを理解する作業、評価は基準と比較して対応の必要性を判断する作業です。

### ❌ リスク受容はリスク評価と同じ

受容はリスクを引き受ける意思決定であり、分析結果と基準を比較する評価とは区別します。

---

## 確認問題（FE試験対策）

リスクアセスメントを構成するプロセスの組合せとして、最も適切なものはどれか。

- ア. リスク特定、リスク評価、リスク対応
- イ. リスク特定、リスク分析、リスク評価
- ウ. リスク分析、リスク対応、リスク受容
- エ. リスク分析、リスク評価、リスク対応

<details markdown="1">
<summary>▶ 答えと解説を見る</summary>

**正解：イ**

リスクアセスメントは**特定・分析・評価**です。ア・ウ・エはいずれも、アセスメントの外にある「対応」を含みます。

</details>

---

## まとめ（試験直前用）

- **特定**：何が危険か見つける
- **分析**：起こりやすさや影響を調べる
- **評価**：基準と比較し、対応が必要か判断する
- **対応**：対策を選び、実施する（アセスメントの外）

迷ったら、**「特定 → 分析 → 評価までがアセスメント」**で切り分けましょう。

情報セキュリティの文脈では、[SG：リスクアセスメントの手順とJISの考え方](/sg/risk-assessment/)も参照できます。

参考：[ISO 31000:2018 Risk management — Guidelines](https://www.iso.org/standard/65694.html)

{% include fe_article_footer.html %}
