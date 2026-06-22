# GK Content Rules

This file is written in English for Codex readability. However, GK article content must be written in Japanese unless the user explicitly requests otherwise.

Use these rules when creating or editing G検定 study articles under `pages/gk`.

Always check the related rule files as needed:

- Normal article structure: `docs/agent/gk-article-template.md`
- Front matter: `docs/agent/gk-frontmatter-rules.md`
- Tags: `docs/agent/gk-tag-rules.md`
- GK navigation and `prev` / `next`: `docs/agent/gk-navigation-rules.md`

## Basic Stance

- Write in beginner-friendly Japanese.
- Prioritize conceptual understanding over mathematical depth.
- Explain concepts so that readers can eliminate wrong answer choices, not only memorize definitions.
- Keep one normal article focused on one term, one model, one method, or one concept.
- Make each article understandable as a standalone page.
- Match the structure, granularity, and wording style of existing `pages/gk` articles.
- Preserve the current GK theme conventions instead of redesigning the article system.

## G検定 Explanation Policy

GK articles should help readers understand AI, machine learning, deep learning, NLP, image recognition, reinforcement learning, evaluation metrics, and social/legal topics at the level needed for G検定.

- Explain the role, intuition, and common use of the term before details.
- Avoid deep derivations unless they directly help judgment.
- If a formula is useful, explain its intuition first and keep the formula short.
- Emphasize differences between similar terms such as model families, architectures, training methods, evaluation metrics, and datasets.
- Use exam-facing phrases naturally when they fit, such as `G検定では〜と問われやすい`, `選択肢では〜と書かれていたら注意`, `〜と〜を混同しない`, and `判断するときは〜を見る`.
- Do not force official links when they are not natural for GK topics.

## Confusion Prevention

Normal GK articles should include confusion-prevention content, usually in `## G検定ひっかけポイント`.

Include at least one of the following when relevant:

- Differences from similar terms.
- Typical wrong descriptions in answer choices.
- Which keyword indicates the correct concept.
- Which feature belongs to a different model or method.
- A short table comparing concepts when the distinction is hard to hold in memory.

## Article Type Policy

- Normal individual articles explain one term or concept deeply enough for exam review.
- Comparison articles may compare two or more concepts, but must still prioritize confusion prevention and answer-choice judgment.
- Summary or cheatsheet pages should be maps or review pages, not copied collections of individual article paragraphs.
- Do not create a new GK article only because a term is a slight wording variation of an existing article. First search existing `pages/gk` titles, filenames, headings, permalinks, and tags.

## Markdown Rendering Rules

When creating or editing GK articles under `pages/gk`, keep Markdown safe for GitHub Pages.

- Insert blank lines before and after headings, lists, tables, and horizontal rules.
- Markdown tables must include a header separator row.
- Internal links must be clickable Markdown links, not plain code-formatted URLs.
- Do not allow front matter keys such as `description`, `tags`, `gk_section`, or `gk_order` to leak into the article body.
- Preserve `{% include gk_article_footer.html %}` when it is the existing convention for the article type.

## Final Self-Check Before Saving

Before saving a GK article, check that:

- the body is Japanese unless the user explicitly requested another language;
- the article has a clear role compared with similar GK pages;
- `## G検定ひっかけポイント` helps readers eliminate wrong choices;
- the article does not over-explain mathematics beyond what helps G検定 judgment;
- the footer include is present when expected;
- front matter is valid YAML and metadata is not visible in the body.
