---
layout: page
title: DoS攻撃とDDoS攻撃の違いを整理【SG試験】
description: DoS攻撃とDDoS攻撃はどちらもサービス停止を狙う攻撃ですが、攻撃元の数が異なります。本記事では違いと見分け方を整理し、SG試験で迷わない判断基準を解説します。
permalink: /sg/dos-vs-ddos/
tags: [sg, threat_vulnerability, unauthorized_access, network]
prev: /sg/dos-attack-difference/
next: /sg/employment-type-comparison/
---

## まず結論
DoS攻撃は「**1つの攻撃元からのサービス妨害**」、DDoS攻撃は「**複数の攻撃元からの分散攻撃**」です。  
SG試験では「**攻撃元が1つか複数か**」で切り分けます。

---

## 直感的な説明
同じ「サービスを止める攻撃」でも、やり方が違います。

- DoS攻撃  
  → 1人が大量にアクセスしてサーバを止める

- DDoS攻撃  
  → 大人数で一斉にアクセスしてサーバを止める

👉 **人数の違い＝攻撃の違い**

---

## 定義・仕組み

### DoS攻撃（Denial of Service）
- 単一の攻撃元から攻撃
- 通信や処理を集中させる
- 規模は比較的小さい

---

### DDoS攻撃（Distributed Denial of Service）
- 複数の攻撃元から同時攻撃
- ボットネットなどを利用
- 大規模で防御が難しい

👉 インターネット上の多数の端末が使われる

---

## どんな場面で使う？

### DoS攻撃
- 小規模な攻撃
- 単純な負荷試験の延長のようなケース

---

### DDoS攻撃
- 大規模サービス停止
- 社会的影響を狙う攻撃

👉 実務ではほぼDDoSが問題になる

---

## よくある誤解・混同

### ❌ DoSとDDoSは同じ意味
→ ⭕ D（Distributed）がつくと「分散攻撃」

---

### ❌ 通信量が多ければDDoS
→ ⭕ 攻撃元が複数かどうかが本質

---

### ❌ SYNフラッド＝DDoS
→ ⭕ 手法の話であり、DoSにもDDoSにもなり得る

---

### SG試験のひっかけ
- 「複数の端末」「ボットネット」 → DDoS
- 「単一の攻撃元」 → DoS

👉 攻撃手法ではなく“構成”で判断

---

## まとめ（試験直前用）


- DoS＝**単一攻撃元**
- DDoS＝**複数攻撃元（分散）**
- 「ボットネット」が出たらDDoS
- 手法（SYNなど）ではなく構成で判断
- SG試験では「誰が攻撃しているか」で切る

{% include sg_article_footer.html %}
