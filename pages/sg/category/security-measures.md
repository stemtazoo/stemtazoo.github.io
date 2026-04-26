---
layout: page
title: 情報セキュリティ対策まとめ
description: 認証、アクセス制御、マルウェア対策、ネットワーク対策、物理的対策などを整理するSG試験向けまとめページです。
permalink: /sg/category/security-measures/
---

## このページで学ぶこと

このページでは、情報セキュリティ対策に関する記事をまとめています。  
SG試験では、単なる用語暗記ではなく、どの場面で使う考え方か、どの選択肢を切れるかを意識して整理します。

## SG試験での見方

- 用語の定義だけでなく、役割で判断する
- 似た用語との違いを押さえる
- 実務上の目的とセットで理解する

## 関連記事一覧

{% assign sg_pages = site.pages | sort: "title" %}

### 認証・アクセス制御
{% assign has_auth = false %}
<ul>
{% for p in sg_pages %}
  {% if p.path contains "pages/sg/" %}
    {% unless p.path contains "pages/sg/category/" %}
      {% if p.url != "/sg/" and p.url != "/sg/all/" %}
        {% if p.tags and p.tags contains 'authentication' %}
          {% assign has_auth = true %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
        {% elsif p.tags and p.tags contains 'access_control' %}
          {% assign has_auth = true %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
        {% elsif p.title contains '認証' or p.title contains 'アクセス制御' or p.title contains '特権ID' or p.title contains '最小権限' or p.title contains 'ゼロトラスト' %}
          {% assign has_auth = true %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
        {% endif %}
      {% endif %}
    {% endunless %}
  {% endif %}
{% endfor %}
</ul>
{% if has_auth == false %}
該当記事は今後追加予定です。
{% endif %}

### ネットワーク対策
{% assign has_network = false %}
<ul>
{% for p in sg_pages %}
  {% if p.path contains "pages/sg/" %}
    {% unless p.path contains "pages/sg/category/" %}
      {% if p.url != "/sg/" and p.url != "/sg/all/" %}
        {% if p.tags and p.tags contains 'network' %}
          {% assign has_network = true %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
        {% elsif p.tags and p.tags contains 'network_security' %}
          {% assign has_network = true %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
        {% elsif p.title contains 'ファイアウォール' or p.title contains 'IDS' or p.title contains 'IPS' or p.title contains 'WAF' or p.title contains 'DMZ' or p.title contains 'VPN' or p.title contains 'Wi-Fi' or p.title contains 'TLS' or p.title contains 'SSL' %}
          {% assign has_network = true %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
        {% endif %}
      {% endif %}
    {% endunless %}
  {% endif %}
{% endfor %}
</ul>
{% if has_network == false %}
該当記事は今後追加予定です。
{% endif %}

### マルウェア・攻撃対策
{% assign has_malware = false %}
<ul>
{% for p in sg_pages %}
  {% if p.path contains "pages/sg/" %}
    {% unless p.path contains "pages/sg/category/" %}
      {% if p.url != "/sg/" and p.url != "/sg/all/" %}
        {% if p.tags and p.tags contains 'malware' %}
          {% assign has_malware = true %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
        {% elsif p.tags and p.tags contains 'unauthorized_access' %}
          {% assign has_malware = true %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
        {% elsif p.title contains 'マルウェア' or p.title contains 'ランサムウェア' or p.title contains 'スパイウェア' or p.title contains 'キーロガー' or p.title contains 'ルートキット' or p.title contains 'クリプトジャッキング' or p.title contains '標的型攻撃' %}
          {% assign has_malware = true %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
        {% endif %}
      {% endif %}
    {% endunless %}
  {% endif %}
{% endfor %}
</ul>
{% if has_malware == false %}
該当記事は今後追加予定です。
{% endif %}

### Web・メール対策
{% assign has_webmail = false %}
<ul>
{% for p in sg_pages %}
  {% if p.path contains "pages/sg/" %}
    {% unless p.path contains "pages/sg/category/" %}
      {% if p.url != "/sg/" and p.url != "/sg/all/" %}
        {% if p.title contains 'SPF' or p.title contains 'DKIM' or p.title contains 'DMARC' or p.title contains 'フィッシング' or p.title contains 'XSS' or p.title contains 'CSRF' or p.title contains 'SQLインジェクション' or p.title contains 'メール' %}
          {% assign has_webmail = true %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
        {% endif %}
      {% endif %}
    {% endunless %}
  {% endif %}
{% endfor %}
</ul>
{% if has_webmail == false %}
該当記事は今後追加予定です。
{% endif %}

### 物理的セキュリティ対策
{% assign has_physical = false %}
<ul>
{% for p in sg_pages %}
  {% if p.path contains "pages/sg/" %}
    {% unless p.path contains "pages/sg/category/" %}
      {% if p.url != "/sg/" and p.url != "/sg/all/" %}
        {% if p.title contains '入退室' or p.title contains 'アンチパスバック' or p.title contains 'セキュリティワイヤ' or p.title contains '監視カメラ' or p.title contains 'クリアデスク' or p.title contains 'クリアスクリーン' or p.title contains '物理' %}
          {% assign has_physical = true %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
        {% endif %}
      {% endif %}
    {% endunless %}
  {% endif %}
{% endfor %}
</ul>
{% if has_physical == false %}
該当記事は今後追加予定です。
{% endif %}

### バックアップ・可用性対策
{% assign has_backup = false %}
<ul>
{% for p in sg_pages %}
  {% if p.path contains "pages/sg/" %}
    {% unless p.path contains "pages/sg/category/" %}
      {% if p.url != "/sg/" and p.url != "/sg/all/" %}
        {% if p.title contains 'バックアップ' or p.title contains 'RAID' or p.title contains 'UPS' or p.title contains '冗長' or p.title contains 'BCP' or p.title contains 'DR' %}
          {% assign has_backup = true %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
        {% endif %}
      {% endif %}
    {% endunless %}
  {% endif %}
{% endfor %}
</ul>
{% if has_backup == false %}
該当記事は今後追加予定です。
{% endif %}

### 対策全体（タグベース）
{% assign has_items = false %}
<ul>
{% for p in sg_pages %}
  {% if p.path contains "pages/sg/" %}
    {% unless p.path contains "pages/sg/category/" %}
      {% if p.url != "/sg/" and p.url != "/sg/all/" %}
        {% if p.tags %}
          {% if p.tags contains 'security_measures' or p.tags contains 'sg-security-measures' or p.tags contains 'access_control' or p.tags contains 'authentication' or p.tags contains 'network_security' or p.tags contains 'malware' or p.tags contains 'it_security_operations' %}
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
