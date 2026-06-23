# FE Tag Rules

This file is written in English for Codex readability. However, FE article content must be written in Japanese unless the user explicitly requests otherwise.

Use these rules for `tags` in articles under `pages/fe`.

## Basic Rules

Use roughly 3 to 5 tags.

- Always include `fe`.
- Always include exactly one primary category tag:
  - `fe-technology`
  - `fe-management`
  - `fe-strategy`
- Add 1 to 3 concrete topic tags.
- Do not over-tag pages.
- Check nearby FE articles before introducing a new tag spelling.
- Prefer existing tag vocabulary over one-off synonyms.
- Do not use DS, SG, or GK-only category tags in FE articles.

## Concrete Tag Candidates

Common concrete tags include:

- `basic-theory`
- `algorithm`
- `data-structure`
- `programming`
- `pseudocode`
- `trace`
- `computer-system`
- `database`
- `network`
- `security`
- `project-management`
- `service-management`
- `system-audit`
- `system-strategy`
- `business-strategy`
- `law`

## Selection Examples

Algorithm article:

```yaml
tags: [fe, fe-technology, algorithm]
```

Data-structure article:

```yaml
tags: [fe, fe-technology, data-structure, algorithm]
```

Pseudocode / trace article:

```yaml
tags: [fe, fe-technology, pseudocode, trace]
```

Network article:

```yaml
tags: [fe, fe-technology, network]
```

Project-management article:

```yaml
tags: [fe, fe-management, project-management]
```

Law article:

```yaml
tags: [fe, fe-strategy, law]
```

## Related-Article Footer Implications

`_includes/fe_article_footer.html` uses tags to find related FE articles.

- Related articles must be limited to pages whose `tags` contain `fe`.
- Matching should ignore the base tag `fe` itself.
- Concrete tags such as `algorithm`, `data-structure`, `network`, or `law` should drive related-article matches.
- Because tags affect related links, avoid adding broad tags that would connect unrelated FE pages.
