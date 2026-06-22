# DS Tag Rules

This file is written in English for Codex readability. However, DS article content must be written in Japanese unless the user explicitly requests otherwise.

Use these rules for `tags` in articles under `pages/ds`.

## Basic Rules

- Always include `ds` on every DS page.
- Select a small number of concrete tags, usually 2-5 total including `ds`.
- Check nearby DS articles before introducing a new tag spelling.
- Prefer existing tag vocabulary over one-off synonyms.
- Do not over-tag pages with every related keyword.
- Keep `categories` and `tags` consistent with the current DS index behavior.

## Common Topic Areas

Existing DS content covers areas such as:

- statistics and probability;
- data analysis methods;
- machine learning and evaluation;
- Python, SQL, and practical data handling;
- data engineering and data management;
- AI utilization;
- business analysis and decision-making;
- ethics, law, governance, and security.

Common tag candidates may include values such as these, but always confirm current usage first:

```yaml
statistics
machine-learning
data-analysis
sql
python
data-engineering
ai-utilization
business
ethics
security
governance
```

## Selection Examples

Statistics article:

```yaml
tags: [ds, statistics]
```

SQL article:

```yaml
tags: [ds, sql, data-engineering]
```

AI utilization article:

```yaml
tags: [ds, ai-utilization]
```

Governance / ethics article:

```yaml
tags: [ds, governance, ethics]
```

## Cautions

- Do not use SG or GK-only category tags in DS articles.
- Do not change tags across many existing articles only for cosmetic consistency in a content-rule task.
- If a tag appears inconsistent but is already used by indexes, investigate before changing it.
- Avoid creating separate tags for singular/plural or hyphen/underscore variants unless the site already uses them intentionally.
