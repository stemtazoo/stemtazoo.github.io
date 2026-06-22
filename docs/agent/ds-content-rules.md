# DS Content Rules

This file is written in English for Codex readability. However, DS article content must be written in Japanese unless the user explicitly requests otherwise.

Use these rules when creating or editing Data Science / DS検定 articles under `pages/ds`.

Always check the related rule files as needed:

- Normal article structure: `docs/agent/ds-article-template.md`
- Front matter: `docs/agent/ds-frontmatter-rules.md`
- Tags: `docs/agent/ds-tag-rules.md`
- DS navigation and `prev` / `next`: `docs/agent/ds-navigation-rules.md`

## Basic Stance

- Write in beginner-friendly Japanese.
- Prioritize practical understanding for DS検定 and data analysis work.
- Explain intuition before formulas.
- Use formulas only when they help judgment or practical understanding.
- Use examples from business, data analysis, Python, statistics, AI utilization, security, governance, and data management when appropriate.
- Keep one normal article focused on one term, one method, one operation, or one concept.
- Match the structure, granularity, and wording style of existing `pages/ds` articles.

## DS検定 / Practical Explanation Policy

DS articles should help readers connect exam knowledge with practical data work.

- Explain what the concept is used for in real analysis, business decisions, or data systems.
- For statistics, explain the intuition and interpretation before formulas.
- For Python / SQL / practical data handling topics, include practical examples or code when appropriate.
- For ethics, law, governance, and security topics, explain the business or data-management decision point.
- Avoid deep academic explanations that do not help DS検定 judgment or beginner practice.
- Use article-facing Japanese phrases naturally when they fit, such as `DS検定では〜が問われやすい`, `実務では〜で使う`, `選択肢では〜に注意`, and `〜と〜を混同しない`.

## Confusion Prevention

Normal DS articles should include confusion-prevention content, usually in `## よくある誤解・混同`.

Include at least one of the following when relevant:

- Difference from similar terms or methods.
- Common misunderstanding in exam choices.
- Practical mistake in Python, SQL, statistics, or data handling.
- Which situation makes a method appropriate or inappropriate.
- Interpretation traps, such as confusing correlation with causation or accuracy with usefulness.

## Related Links And Skill Items

Existing DS articles often include `## 対応スキル項目（...）` and `## 🔗 関連記事`.

- Include `## 対応スキル項目（...）` when it is useful and consistent with nearby DS articles.
- Use a skill-sheet label that matches the topic, such as `データサイエンス力シート`, `データエンジニアリング力シート`, `ビジネス力シート`, or `AI利活用スキルシート`.
- Add related articles when they help readers distinguish similar terms or continue a learning path.
- Avoid repeating large Liquid or manual related-article blocks if a safer shared include exists. If no include exists, follow the current nearby DS convention rather than redesigning it in the same task.

## Markdown Rendering Rules

When creating or editing DS articles under `pages/ds`, keep Markdown safe for GitHub Pages.

- Insert blank lines before and after headings, lists, tables, code fences, and horizontal rules.
- Markdown tables must include a header separator row.
- Internal links must be clickable Markdown links, not plain code-formatted URLs.
- Do not duplicate `prev` / `next` as visible body text.
- Do not allow front matter keys such as `description`, `categories`, `tags`, `prev`, or `next` to leak into the article body.
- Preserve existing related-link style when editing a page, unless the user asks for a structural cleanup.

## Final Self-Check Before Saving

Before saving a DS article, check that:

- the body is Japanese unless the user explicitly requested another language;
- the article has a clear role compared with similar DS pages;
- intuition appears before formulas or code-heavy details;
- practical examples are accurate and beginner-friendly;
- `## よくある誤解・混同` helps readers avoid exam and practical mistakes;
- `## 対応スキル項目（...）` is present when useful and consistent with nearby pages;
- front matter is valid YAML and metadata is not visible in the body.
