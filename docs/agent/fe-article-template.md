# FE Article Template

This file is written in English for Codex readability. However, FE article content must be written in Japanese unless the user explicitly requests otherwise.

Normal individual articles under `pages/fe` should cover one term or one concept per page.

## Standard Headings For Normal FE Articles

Use this standard structure when the topic has a direct and concrete connection to the official Subject B scope:

```md
## まず結論

## 直感的な説明

## 定義・仕組み

## 科目Aでどう出る？

## 科目Bでどう使う？

## よくある誤解・混同

## まとめ（試験直前用）
```

Use the following structure when Subject B relevance is weak, indirect, or limited to background knowledge:

```md
## まず結論

## 直感的な説明

## 定義・仕組み

## 科目Aでどう出る？

## どんな場面で使う？

## よくある誤解・混同

## まとめ（試験直前用）
```

For concise management, law, strategy, audit, or service-management articles, `## 科目Aでどう出る？` and `## どんな場面で使う？` may be combined when that better matches existing FE article style. Do not add a Subject B section merely to preserve heading symmetry.

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
- When Subject B relevance is weak, strengthen this section instead of forcing a Subject B section.

### 科目Bでどう使う？

This heading is optional.

Include it only when the topic has a direct and concrete connection to the official Subject B scope defined in `docs/agent/fe-content-rules.md`.

When included, explain at least one of the following:

- what must be traced in pseudocode;
- which variables, indexes, conditions, loops, pointers, or data structures must be followed;
- which algorithmic judgment is required;
- how a bug or correction should be identified;
- which information-security control should be selected and why.

For algorithms and programming topics, include concrete reading guidance rather than generic statements.

Good examples:

- explain how an index changes during a loop;
- identify which stack or queue operation occurs next;
- show which condition terminates recursion;
- explain how to detect an off-by-one error;
- explain which access-control or logging measure satisfies a security requirement.

Do not include this heading only to say:

- the topic may appear as background knowledge;
- it may help when reading a long question;
- it is loosely related to system structure;
- it might be useful someday.

If the connection is weak, use `## どんな場面で使う？` or strengthen `## 科目Aでどう出る？` instead.

### どんな場面で使う？

- Use this instead of `## 科目Bでどう使う？` for law, management, strategy, service-management, audit, general hardware, general OS terminology, or other topics where Subject B use is not central.
- Explain practical or exam scenarios in which the concept matters.
- Keep the explanation connected to FE judgment rather than broad business theory.
- For terminology questions, use this section to strengthen role, location, purpose, or similar-term distinctions.

### よくある誤解・混同

- Explain similar-term differences and common exam traps.
- Include at least one concrete confusion point when relevant.
- For algorithms and data structures, include mistakes such as off-by-one errors, confusing value and index, confusing stack and queue, or misreading loop conditions when applicable.
- For Subject A terminology, compare nearby terms that appear as plausible distractors.

### まとめ（試験直前用）

- Summarize the key points in 3-5 lines or bullets.
- Focus on recall cues and exam judgment criteria.
- Do not simply repeat the meta description.
- Do not mention Subject B when the article does not provide a concrete Subject B solving skill.

## Subject B Heading Decision

Before adding `## 科目Bでどう使う？`, confirm all of the following:

1. The topic belongs to one of the official Subject B areas.
2. The article can explain a concrete pseudocode, algorithm, debugging, or security judgment.
3. The section provides a usable solving skill rather than background knowledge.
4. The section remains useful without hypothetical wording such as `長文問題で出るかもしれない`.

If items 2 or 3 are not satisfied, omit the Subject B heading.

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
- include `fe_section`, `fe_subsection`, and `fe_order` if the page should appear in `/fe/` as a normal listing item;
- include a Subject B section only when the comparison directly supports a concrete Subject B solving skill.