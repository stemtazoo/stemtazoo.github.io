---
layout: page
title: 情報セキュリティ関連法規まとめ
description: "個人情報保護法・不正アクセス禁止法・著作権法・電子署名法など、SG試験で頻出の関連法規を適用対象と責任範囲の観点で整理するまとめページです。 選択肢で問われる目的・対象・責任範囲を押さえ、似た用語や対策との違いを判断できるようにします。"
permalink: /sg/category/law/
---

[SGトップへ戻る](/sg/)

## SG試験での見方

- 法令名だけでなく、何を守る法律かで判断する
- 似た制度の適用対象を切り分ける
- 実務上の責任範囲とセットで理解する

## 関連するまとめページ

このカテゴリに関連する学習まとめページです。  
法令・知財・契約の全体像を先につかみたい場合は、こちらから読むと理解しやすくなります。

- [委託契約の責任分界まとめ｜成果物・再委託・権利帰属を整理【SG試験】](/sg/legal-contract-ip-summary/)
  委託契約での成果物責任、再委託管理、秘密保持、著作権の権利帰属を、試験での責任分界の判断軸で整理したまとめページです。

- [法令・知的財産・委託契約まとめ｜責任と保護対象で整理【SG試験】](/sg/law-ip-contract-summary/)
  法令・知財・契約実務を「何を守る制度か」「誰が責任を負うか」で切り分け、試験で迷いやすい論点を一気に整理できます。

## 関連記事一覧

{% assign sg_pages = site.pages | sort: "title" %}
{% assign has_items = false %}
<ul>
{% for p in sg_pages %}
  {% if p.path contains "pages/sg/" %}
    {% unless p.path contains "pages/sg/category/" %}
      {% if p.url != "/sg/" and p.url != "/sg/all/" %}
        {% if p.tags %}
          {% if p.tags contains 'law' or p.tags contains 'security_law' or p.tags contains 'sg-security-law' or p.tags contains 'compliance' or p.tags contains 'personal_information' or p.tags contains 'privacy_law' or p.tags contains '法務' %}
            {% assign has_items = true %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
          {% endif %}
        {% endif %}
      {% endif %}
    {% endunless %}
  {% endif %}
{% endfor %}
</ul>
{% if has_items == false %}
該当記事は今後追加予定です。
{% endif %}
