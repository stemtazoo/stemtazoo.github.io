# GK Article Template

This file is written in English for Codex readability. However, GK article content must be written in Japanese unless the user explicitly requests otherwise.

Normal individual articles under `pages/gk` should cover one term or one concept per page and use the following six fixed Japanese headings when the topic fits the standard article pattern.

```md
## まず結論

## 直感的な説明

## 定義・仕組み

## いつ使う？（得意・不得意）

## G検定ひっかけポイント

## まとめ（試験直前用）
```

## Role Of Each Heading

### まず結論

- Explain the concept in one or two sentences.
- State the main G検定 judgment point.
- Avoid starting with a formula or historical detail.

### 直感的な説明

- Use an intuitive analogy or simple AI/data example.
- Help beginners understand why the concept exists.
- Avoid making the analogy longer than the explanation itself.

### 定義・仕組み

- Explain the definition and mechanism in plain Japanese.
- For models and architectures, explain the main components and flow.
- For machine learning methods, explain what is learned, what input/output is expected, and what assumption is important.
- For metrics, explain what the metric rewards or penalizes before any formula.

### いつ使う？（得意・不得意）

- Explain typical use cases and limitations.
- Separate `得意なこと` and `苦手・注意点` with subheadings when useful.
- Connect the explanation to answer-choice judgment.

### G検定ひっかけポイント

- Explain common traps and similar-term confusion.
- Include `正誤を切る判断基準` when it helps.
- Use short bullets or tables for comparisons.

### まとめ（試験直前用）

- Summarize the key points in 3-5 lines or bullets.
- Prioritize recall cues for exam judgment.

## Footer

At the end of normal GK article bodies, use the existing GK footer convention when nearby normal articles do so:

```liquid
{% include gk_article_footer.html %}
```

Do not replace this footer with large manual related-link blocks unless the existing nearby GK article type already uses that pattern or the user explicitly requests it.

## Comparison Articles

Comparison articles may use a slightly different structure, but they must still:

- state the difference in `## まず結論`;
- include a comparison table when it improves clarity;
- explain which description belongs to which concept;
- include exam traps or confusion-prevention content;
- avoid duplicating large sections from individual articles.
