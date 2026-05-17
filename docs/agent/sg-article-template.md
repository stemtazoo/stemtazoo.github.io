# SG Article Template

This file is written in English for Codex readability. However, SG article content must be written in Japanese unless the user explicitly requests otherwise.

Normal articles under `pages/sg` must cover one term or one concept per page and use the following six fixed Japanese headings.

```md
## まず結論

## 直感的な説明

## 定義・仕組み

## どんな場面で使う？

## よくある誤解・混同

## まとめ（試験直前用）
```

## Role Of Each Heading

### まず結論

- Explain the term or concept in one sentence.
- State what the SG exam expects the reader to judge about the topic.

### 直感的な説明

- Explain using an everyday example or workplace example.
- Help readers intuitively understand why the topic matters.

### 定義・仕組み

- Explain the definition in plain language.
- For systems, standards, and countermeasures, focus on the purpose and basic flow.
- When official information exists from sources such as laws, IPA, NISC, JPCERT/CC, CRYPTREC, 個人情報保護委員会, e-Gov法令検索, or JIS / ISO / IEC, place the official link here naturally.

### どんな場面で使う？

- Explain when the concept should be used.
- Also explain situations where it is easy to misuse or misunderstand.
- Keep 科目B case-question judgment in mind.

### よくある誤解・混同

- Explain differences from terms that are easy to confuse.
- Include typical SG exam traps.
- Write so the reader can judge that a specific expression is wrong.

### まとめ（試験直前用）

- Summarize the key points in 3-5 lines.
- Make the summary help readers recall judgment criteria, not just memorize wording.

## Footer

At the end of the article body, always add this single line:

```liquid
{% include sg_article_footer.html %}
```

Unless the user explicitly asks otherwise, do not add unnecessary related-article sections inside the article body. Leave related-article behavior to the footer include.
