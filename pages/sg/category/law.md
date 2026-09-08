---
layout: page
title: 情報セキュリティ関連法規まとめ
description: "個人情報保護法、不正アクセス禁止法、著作権法、電子署名法などを、何を守る法律か・どの行為が問題になるかという入口とタグ連動の全記事一覧で整理します。新規記事も主分類タグから自動で反映されます。"
permalink: /sg/category/law/
last_modified_at: 2026-09-09
---

[SGトップへ戻る](/sg/)

## SG試験での見方

法規では、法律名を暗記するより、**何を守る制度か・どの行為を規制するか**で判断します。

- 個人情報を守る → 個人情報保護法
- 不正ログインや識別符号の不正利用を規制する → 不正アクセス禁止法
- 著作物や権利帰属を見る → 著作権法
- 電子署名の法的な扱いを見る → 電子署名法
- 委託や契約上の責任を見る → 契約・法務関連

## まず読むまとめ記事

- [法令・知的財産・委託契約まとめ｜責任と保護対象で整理【SG試験】](/sg/law-ip-contract-summary/)
- [委託契約の責任分界まとめ｜成果物・再委託・権利帰属を整理【SG試験】](/sg/legal-contract-ip-summary/)

## テーマ別の入口

### 個人情報・プライバシー

- [個人情報保護法とは？](/sg/personal-information-protection-law/)
- [個人情報保護マネジメントシステム（PMS）とは？](/sg/personal-information-protection-management-system/)

### 不正アクセス

- [不正アクセス禁止法とは？禁止される行為を整理](/sg/unauthorized-access-law/)
- [識別符号とは？ID・パスワードとの関係を整理](/sg/identification-code/)

### 知的財産・契約

- [著作権とは？](/sg/copyright/)
- [委託先管理とは？](/sg/vendor-management/)

## 全記事一覧（タグから自動更新）

以下は、主分類タグ `sg-security-law` が付いた記事をタイトル順に自動表示しています。

**今後は新規記事に正しい主分類タグを付ければ、このカテゴリページへの手動追記は不要です。**

{% assign category_pages = site.pages | where: "tags", "sg-security-law" | sort: "title" %}
{% assign category_count = 0 %}
{% for p in category_pages %}
  {% if p.permalink %}
- [{{ p.title }}]({{ p.permalink }})
    {% assign category_count = category_count | plus: 1 %}
  {% endif %}
{% endfor %}
{% if category_count == 0 %}
- 現在、該当記事はありません。
{% endif %}

{% include sg_article_footer.html %}
