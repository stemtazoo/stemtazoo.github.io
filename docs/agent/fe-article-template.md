# FE Article Template

This file is written in English for Codex readability. However, FE article content must be written in Japanese unless the user explicitly requests otherwise.

Normal individual articles under `pages/fe` should cover one term or one concept per page.

## Standard Headings For Normal FE Articles

Use this standard structure for normal FE individual articles:

```md
## まず結論

## 直感的な説明

## 定義・仕組み

## 科目Aでどう出る？

## 科目Bでどう使う？

## よくある誤解・混同

## まとめ（試験直前用）
```

For topics that are not relevant to 科目B, such as some law, management, or strategy topics, it is acceptable to use:

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

- Explain the term or concept in one or two beginner-friendly sentences.
- State the exam judgment point the reader should remember first.
- Avoid starting with a broad textbook introduction.

### 直感的な説明

- Use an everyday, workplace, programming, data-structure, or exam-reading analogy.
- Explain the intuition before formal definitions or detailed mechanisms.
- For algorithms and data structures, show what the learner should picture when tracing data.

### 定義・仕組み

- Explain the definition and mechanism in plain Japanese.
- Use small examples, tables, or pseudocode-like snippets when they help beginners.
- For official-reference paragraphs, use clickable Markdown links and connect the topic to FE scope without boilerplate repetition.

### 科目Aでどう出る？

- Explain how the topic appears in multiple-choice knowledge questions.
- Focus on keywords, answer-choice judgment, and similar-term distinctions.
- Write so readers can eliminate plausible but wrong choices.

### 科目Bでどう使う？

- Explain how the concept is read or used in 科目B case questions, algorithms, data structures, pseudocode, or trace problems.
- For algorithms and programming topics, include what values, pointers, indexes, conditions, or loops to follow.
- If 科目B relevance is weak, use the alternate `## どんな場面で使う？` structure instead.

### どんな場面で使う？

- Use this instead of `## 科目Bでどう使う？` for law, management, strategy, service-management, audit, or other topics where 科目B use is not central.
- Explain practical or exam scenarios in which the concept matters.
- Keep the explanation connected to FE judgment rather than broad business theory.

### よくある誤解・混同

- Explain similar-term differences and common exam traps.
- Include at least one concrete confusion point when relevant.
- For algorithms and data structures, include mistakes such as off-by-one errors, confusing value and index, confusing stack and queue, or misreading loop conditions when applicable.

### まとめ（試験直前用）

- Summarize the key points in 3-5 lines or bullets.
- Focus on recall cues and exam judgment criteria.
- Do not simply repeat the meta description.

## Standard Footer / Related Articles Include

Normal FE articles should place the shared footer include at the end of the page:

```liquid
{% include fe_article_footer.html %}
```

Rules:

- Do not paste a large related-article Liquid block manually into new normal FE articles.
- Related-article filtering belongs in `_includes/fe_article_footer.html`.
- The footer must not show DS, SG, or GK articles as FE related articles.
- Preserve the `基本情報技術者トップに戻る` link.

## Comparison Or Summary Articles

Comparison and summary articles may use a slightly different structure, but they must still:

- state the difference or review purpose in `## まず結論`;
- include comparison tables or judgment lists when useful;
- avoid copying large sections from individual articles;
- use FE-specific front matter and tags;
- include `fe_section`, `fe_subsection`, and `fe_order` if the page should appear in `/fe/` as a normal listing item.
