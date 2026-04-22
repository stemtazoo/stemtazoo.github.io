---
layout: page  
title: SOC・CSIRT・JPCERT/CCの違いとは？役割と関係を図で整理【情報セキュリティマネジメント】  
description: SOC・CSIRT・JPCERT/CCの違いと関係を整理。監視・対応・外部連携の役割分担を理解し、SG試験でのひっかけポイントを解説します。  
permalink: /sg/soc-csirt-jpcert/  
tags: [sg, sg-security-management]  
prev: /sg/csirt/  
next: /sg/csrf/  
---

## まず結論  
- **SOC＝監視・検知**  
- **CSIRT＝対応・復旧**  
- **JPCERT/CC＝外部連携・調整**  

👉 SG試験は  
**「誰が何をやるか」で切る問題が中心**

---

## 直感的な説明  

セキュリティ対応は、1つの組織で全部やるわけではありません。  

役割ごとに分かれています👇  

- SOC：異常を見つける  
- CSIRT：実際に対応する  
- JPCERT/CC：外部とつなぐ  

👉 イメージ  

- SOC＝監視カメラ  
- CSIRT＝現場の対応班  
- JPCERT/CC＝警察や他組織との連絡役  

---

## 定義・仕組み  

### 全体の流れ（超重要）  

1. SOCが異常を検知  
2. CSIRTが対応・調査  
3. 必要に応じてJPCERT/CCと連携  

👉 **この流れを覚えるだけでかなり解ける**

---

## どんな場面で使う？  

### 正しい流れ  
- SOCがアラートを検知  
- CSIRTが原因調査・封じ込め  
- 外部影響があればJPCERT/CCと連携  

---

### 間違いやすい流れ  
- ❌ SOCが対応までやる  
- ❌ JPCERT/CCが現場対応する  
- ❌ CSIRTが監視専門  

---

## よくある誤解・混同  

### ① SOCとCSIRTの違い  
- SOC：監視・検知  
- CSIRT：**対応・復旧**  

👉 判断基準  
**「実際に対処するか？」**

---

### ② CSIRTとJPCERT/CCの違い  
- CSIRT：自社対応  
- JPCERT/CC：**外部調整・支援**  

👉 判断基準  
**「自社のためか、社会全体か？」**

---

### ③ JPCERT/CCの役割の誤解  
- ❌ 現場で復旧作業する  
- ⭕ 情報共有・調整・支援  

👉 **直接対応しないのがポイント**

---

## まとめ（試験直前用）  

- SOC＝監視・検知  
- CSIRT＝対応・復旧  
- JPCERT/CC＝外部連携  

---

### 切り分けルール（これだけ覚える）  

- 「異常を見つける」→SOC  
- 「対応・復旧する」→CSIRT  
- 「外部と連携する」→JPCERT/CC  

👉 **「誰が動くか」で判断する**

{% include sg_article_footer.html %}
