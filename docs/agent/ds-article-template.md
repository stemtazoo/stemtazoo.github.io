# DS Article Template

This file is written in English for Codex readability. However, DS article content must be written in Japanese unless the user explicitly requests otherwise.

Normal individual articles under `pages/ds` should cover one term, method, operation, or concept per page and use the following six fixed Japanese headings when the topic fits the standard article pattern.

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

- Explain the term or concept in one or two sentences.
- State what DS検定 or practical data analysis expects the reader to judge.

### 直感的な説明

- Use a business, data analysis, Python, statistics, AI utilization, or data-management example.
- Explain the intuition before formulas, code, or strict definitions.

### 定義・仕組み

- Explain the definition and mechanism in plain Japanese.
- For statistical concepts, explain what the number means before showing formulas.
- For Python / SQL / data-engineering topics, show the basic operation or flow.
- For governance, law, ethics, and security topics, explain what the rule or control protects.

### どんな場面で使う？

- Explain practical use cases.
- Include inappropriate or risky use cases when relevant.
- Connect use cases to DS検定 answer-choice judgment.

### よくある誤解・混同

- Explain similar-term differences and common mistakes.
- For practical articles, include typical coding, SQL, interpretation, or operation mistakes.
- Write so the reader can identify why a plausible answer choice is wrong.

### まとめ（試験直前用）

- Summarize the key points in 3-5 lines or bullets.
- Focus on recall cues and judgment criteria.

## Optional Skill Item Section

When useful and consistent with nearby DS articles, add this after the summary:

```md
## 対応スキル項目（データサイエンス力シート）

- （関連するスキル項目）
```

Choose the parenthetical label according to the topic and nearby articles, for example:

- `データサイエンス力シート`
- `データエンジニアリング力シート`
- `ビジネス力シート`
- `AI利活用スキルシート`

Do not invent overly specific skill labels when nearby DS pages use broader labels.

## Standard Footer / Related Articles Include

Normal DS articles that use the standard related-article/footer pattern should place the shared include after the optional skill item section:

```md
{% include ds_article_footer.html %}
```

Rules:

- Do not paste the large related-article Liquid block manually into new normal DS articles.
- Keep `## 対応スキル項目（...）` before the footer include when that section is present.
- Preserve an existing manual related/footer block only when the page has a special structure and the include would change behavior.
- For special manual related links, link only existing pages unless the user explicitly asks for planned links, and confirm the target `permalink` from front matter.

## Comparison Articles

Comparison articles may use a slightly different structure, but they must still:

- state the difference in `## まず結論`;
- include a comparison table when useful;
- explain when to use each term or method;
- include common misunderstandings;
- avoid copying large sections from individual articles.
