---
layout: page
title: 情報セキュリティ関連法規まとめ
description: "個人情報保護法、不正アクセス禁止法、著作権法、電子署名法などを、何を守る法律か・どの行為が問題になるかという入口とタグ連動の全記事一覧で整理します。新規記事は主分類タグから自動反映し、旧タグの記事も移行期間中は拾います。"
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

- [個人情報保護法とJIS Q 15001の違い【SG試験】](/sg/privacy-law-vs-jis-q-15001/)
- [個人情報保護マネジメントシステムとは？JIS Q 15001の役割を整理【SG試験】](/sg/personal-information-protection-management-system/)
- [個人情報保護法（要配慮個人情報）とは？同意要件と実務上の注意点【SG試験】](/sg/personal-information-protection-law-sensitive-data/)

### 不正アクセス

- [不正アクセス禁止法とは？禁止される行為を整理](/sg/unauthorized-access-law/)
- [識別符号とは？ID・パスワードとの関係を整理](/sg/identification-code/)

### 知的財産・契約

- [著作権の帰属とは？委託開発との違いを理解する【SG試験】](/sg/copyright-ownership/)
- [著作者人格権とは？公表権・氏名表示権・同一性保持権を整理【SG試験】](/sg/copyright-moral-rights/)
- [委託先管理とは？](/sg/vendor-management/)

## 全記事一覧（タグから自動更新）

新規記事では主分類タグ `sg-security-law` を正とします。既存記事には旧タグだけのものが残っているため、移行期間中は `law`、`security_law`、`compliance`、`personal_information`、`privacy_law`、`法務` も自動的に拾います。

{% assign sg_pages = site.pages | sort: "title" %}
{% assign category_count = 0 %}
{% for p in sg_pages %}
  {% if p.path contains "pages/sg/" and p.tags %}
    {% unless p.path contains "pages/sg/category/" %}
      {% if p.tags contains "sg-security-law" or p.tags contains "law" or p.tags contains "security_law" or p.tags contains "compliance" or p.tags contains "personal_information" or p.tags contains "privacy_law" or p.tags contains "法務" %}
- [{{ p.title }}]({{ p.url }})
        {% assign category_count = category_count | plus: 1 %}
      {% endif %}
    {% endunless %}
  {% endif %}
{% endfor %}
{% if category_count == 0 %}
- 現在、該当記事はありません。
{% endif %}

{% include sg_article_footer.html %}
