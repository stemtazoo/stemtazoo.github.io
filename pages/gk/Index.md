---
layout: page
title: G検定 学習まとめ
description: G検定対策の学習まとめページです。人工知能の歴史、機械学習、深層学習、画像認識、自然言語処理、強化学習、法律・倫理などの頻出論点を分野別に整理し、試験前の復習に使えます。 試験対策として重要語の定義・具体例・よくある誤解をまとめ、短時間で復習できるように整理しています。
permalink: /gk/
tags: [gk]

# 見出し構造だけをここで定義する。
# 記事一覧は _includes/gk_section.html が各記事の gk_section / gk_order から動的生成する。
gk_sections:
  - title: "人工知能（AI）とは"

  - title: "人工知能をめぐる動向"
    subsections:
      - title: "AIブーム"

  - title: "機械学習の概要"
    subsections:
      - title: "代表的な手法"
        subsections:
          - title: "学習の種類"
          - title: "教師あり学習"
            subsections:
              - title: "アンサンブル学習"
              - title: "時系列分析"
          - title: "教師なし学習"
            subsections:
              - title: "クラスタリング"
              - title: "次元削減"
              - title: "トピックモデル"
          - title: "強化学習"
            subsections:
              - title: "基礎概念"
              - title: "価値ベース・TD学習"
              - title: "方策勾配・Actor-Critic"
              - title: "バンディット"
              - title: "発展・大規模化"

      - title: "確率分布・統計モデル"

      - title: "特徴量・前処理"

      - title: "モデルの選択・評価"
        subsections:
          - title: "分類の評価指標"
          - title: "回帰の評価指標"
          - title: "データ分割・交差検証"
          - title: "ハイパーパラメータ探索"
          - title: "情報量規準（AIC・BIC）"

      - title: "よくあるつまずき（過学習など）"

  - title: "ディープラーニングの概要"
    subsections:
      - title: "ニューラルネットワークとディープラーニング"
      - title: "誤差関数"
      - title: "正則化"
      - title: "最適化手法"
      - title: "誤差逆伝播法（Backpropagation）"
      - title: "活性化関数"

  - title: "ディープラーニングの要素技術"
    subsections:
      - title: "ネットワークの構成要素"
      - title: "リカレントニューラルネットワーク (RNN)"
      - title: "トランスフォーマー (Transformer)"
      - title: "オートエンコーダ"
        subsections:
          - title: "基本・派生モデル"
          - title: "異常検知"

  - title: "ディープラーニングの応用例"
    subsections:
      - title: "画像認識"
        subsections:
          - title: "ネオコグニトロンとLeNet"
          - title: "データ拡張"
          - title: "物体認識タスク"
          - title: "物体検出タスク"
          - title: "セグメンテーションタスク"
          - title: "姿勢推定タスク"
          - title: "マルチタスク学習"

      - title: "音声処理"
        subsections:
          - title: "デジタル化・前処理"
          - title: "音響特徴・音素"
          - title: "音声認識・系列モデル"
      - title: "自然言語処理"
        subsections:
          - title: "基礎・前処理"
          - title: "分散表現"
          - title: "Transformer・言語モデル"
          - title: "タスク・評価"
      - title: "深層強化学習"
        subsections:
          - title: "DQN・改良手法"
          - title: "代表エージェント・プロジェクト"
          - title: "Sim-to-Real"
      - title: "データ生成"
        subsections:
          - title: "GAN・派生モデル"
          - title: "拡散モデル"
          - title: "生成モデル比較"
      - title: "転移学習・ファインチューニング"
        subsections:
          - title: "事前学習・少数例学習"
          - title: "継続学習・忘却"
      - title: "マルチモーダル"
        subsections:
          - title: "基礎・全体像"
          - title: "画像と言語の表現・理解"
          - title: "汎用マルチモーダルモデル"
          - title: "代表タスク・生成"
      - title: "モデルの解釈性"
        subsections:
          - title: "基礎・全体像"
          - title: "特徴量の重要度・寄与"
          - title: "画像モデルの可視化"
          - title: "比較・使い分け"
          - title: "ひっかけ問題"
      - title: "モデルの軽量化"
        subsections:
          - title: "モデル圧縮の基本・手法"
          - title: "関連理論・仮説"

  - title: "AIの社会実装に向けて"
    subsections:
      - title: "プロジェクト全体・役割"
      - title: "プロセス・方法論"
      - title: "開発・運用（MLOps）"
      - title: "エッジ・クラウド"

  - title: "AIの法律と倫理"
    subsections:
      - title: "AI倫理・ガバナンス"
        subsections:
          - title: "基礎・原則"
          - title: "ガバナンス・評価"
          - title: "公平性・包摂性"
          - title: "安全性・ロバスト性"
      - title: "プライバシー・個人情報保護"
        subsections:
          - title: "基礎・法制度"
          - title: "個人データの加工・提供"
          - title: "GDPRの本人権利"
          - title: "保護設計・技術"
      - title: "AIセキュリティ・プライバシー攻撃"
        subsections:
          - title: "学習データを狙う攻撃"
          - title: "モデルを狙う攻撃"
          - title: "比較・まとめ"
      - title: "知的財産・データ利用"
      - title: "社会的影響・悪用"
        subsections:
          - title: "偽・誤情報と合成コンテンツ"
          - title: "推薦・情報環境への影響"
          - title: "自動化・自律化の社会的リスク"

  - title: "チートシート（試験直前）"

  - title: "ひっかけ問題集"
last_modified_at: 2026-08-27
---

<div class="portal-card-grid">
  <section class="portal-card">
    <h3>はじめてのG検定</h3>
    <p>AIの歴史、探索・推論、機械学習の全体像から順番に学びます。</p>
    <a class="portal-card__button" href="/gk/ai-booms-cheatsheet/">学習開始</a>
  </section>
  <section class="portal-card">
    <h3>機械学習・深層学習</h3>
    <p>教師あり学習、評価指標、ニューラルネットワーク、CNN・Transformerを整理します。</p>
    <a class="portal-card__button" href="/gk/supervised-learning/">学習開始</a>
  </section>
  <section class="portal-card">
    <h3>試験直前チェック</h3>
    <p>チートシートとひっかけ問題で、頻出論点を短時間で復習します。</p>
    <a class="portal-card__button" href="/gk/concepts-final-cheatsheet/">学習開始</a>
  </section>
  <section class="portal-card">
    <h3>サイト内検索</h3>
    <p>SG試験、G検定、DS検定の記事をキーワードで横断検索できます。</p>
    <a class="portal-card__button" href="{{ '/search/' | relative_url }}">検索する</a>
  </section>
</div>

## まずどこから？

- はじめて：**人工知能とは → 機械学習の概要 → ディープラーニングの概要**
- 画像まわり：**ディープラーニングの要素技術 → 応用例（物体検出・セグメンテーション）**
- 試験直前：**チートシート → ひっかけ問題集**

---

## 目次

- [技術分野](#技術分野)
  - [人工知能とは](#人工知能とは)
  - [人工知能をめぐる動向](#人工知能をめぐる動向)
  - [機械学習の概要](#機械学習の概要)
  - [ディープラーニングの概要](#ディープラーニングの概要)
  - [ディープラーニングの要素技術](#ディープラーニングの要素技術)
  - [ディープラーニングの応用例](#ディープラーニングの応用例)
  - [AIの社会実装に向けて](#aiの社会実装に向けて)
- [法律・倫理分野](#法律倫理分野)
  - [AI倫理・AIガバナンス](#ai倫理aiガバナンス)
- [試験対策](#試験対策)
  - [チートシート（試験直前）](#チートシート試験直前)
  - [ひっかけ問題集](#ひっかけ問題集)

---

## 技術分野

## 人工知能とは
{% assign sec = page.gk_sections | where: "title", "人工知能（AI）とは" | first %}
{% include gk_section.html sec=sec %}

## 人工知能をめぐる動向
{% assign sec = page.gk_sections | where: "title", "人工知能をめぐる動向" | first %}
{% include gk_section.html sec=sec %}

## 機械学習の概要
{% assign sec = page.gk_sections | where: "title", "機械学習の概要" | first %}
{% include gk_section.html sec=sec %}

## ディープラーニングの概要
{% assign sec = page.gk_sections | where: "title", "ディープラーニングの概要" | first %}
{% include gk_section.html sec=sec %}

## ディープラーニングの要素技術
{% assign sec = page.gk_sections | where: "title", "ディープラーニングの要素技術" | first %}
{% include gk_section.html sec=sec %}

## ディープラーニングの応用例
{% assign sec = page.gk_sections | where: "title", "ディープラーニングの応用例" | first %}
{% include gk_section.html sec=sec %}

## AIの社会実装に向けて
{% assign sec = page.gk_sections | where: "title", "AIの社会実装に向けて" | first %}
{% include gk_section.html sec=sec %}

---

## 法律・倫理分野

## AI倫理・AIガバナンス
{% assign sec = page.gk_sections | where: "title", "AIの法律と倫理" | first %}
{% include gk_section.html sec=sec %}

---

## 試験対策

## チートシート（試験直前）
{% assign sec = page.gk_sections | where: "title", "チートシート（試験直前）" | first %}
{% include gk_section.html sec=sec %}

## ひっかけ問題集
{% assign sec = page.gk_sections | where: "title", "ひっかけ問題集" | first %}
{% include gk_section.html sec=sec %}

---

## 未分類（gk_section未設定）

{% assign gk_all = site.pages | sort: "title" %}
<ul>
  {% for p in gk_all %}
    {% if p.tags and p.tags contains "gk" %}
      {% if p.gk_section == nil or p.gk_section == "" %}
        {% unless p.url == page.url %}
          <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a>（{{ p.url }}）</li>
        {% endunless %}
      {% endif %}
    {% endif %}
  {% endfor %}
</ul>

---

<footer style="margin-top:24px; text-align:right;">
  <a href="{{ '/' | relative_url }}">🏠 AI・データサイエンス・IT学習ノート トップへ</a>
</footer>