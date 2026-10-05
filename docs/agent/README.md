# Agent Rule Map

Start at [AGENTS.md](../../AGENTS.md). This map owns routing; each guide owns the detailed rules for its topic. Load guides for the current task rather than every file in this directory.

## Article work

Before creating or meaningfully editing an article, read [editorial rules](editorial-rules.md), [AI-search readability](ai-search-content-rules.md), and the relevant row below. A small isolated typo fix needs the affected guide, not an unrelated full audit.

| Theme | Required article guides | Focus |
| --- | --- | --- |
| FE | [content](fe-content-rules.md), [template](fe-article-template.md), [front matter](fe-frontmatter-rules.md), [tags](fe-tag-rules.md) | 科目A judgment; concrete 科目B relevance; independent explanation from example questions |
| SG | [content](sg-content-rules.md), [template](sg-article-template.md), [front matter](sg-frontmatter-rules.md), [tags](sg-tag-rules.md), [example/confirmation questions](sg-example-question-rules.md) | Workplace judgment; 科目A-to-B bridge; safe question rendering |
| DS | [content](ds-content-rules.md), [template](ds-article-template.md), [front matter](ds-frontmatter-rules.md), [tags](ds-tag-rules.md) | Intuition, interpretation, Python/SQL practice |
| GK | [content](gk-content-rules.md), [template](gk-article-template.md), [front matter](gk-frontmatter-rules.md), [tags](gk-tag-rules.md) | Concept roles, confusion prevention, exam judgment |

The front-matter guides refer to [shared metadata writing](metadata-rules.md). Source-dependent work follows [primary-source and freshness rules](primary-source-audit-rules.md). New or substantially updated FE/DS/GK articles must evaluate visual learning value using [interactive learning rules](interactive-learning-rules.md); implementation is optional.

## Conditional routes

| Task trigger | Also read |
| --- | --- |
| FE example-driven article consideration | FE article guides and editorial rules above; search all four themes before choosing new/update/no change. If approved for writing, preserve standalone examples and title independence. |
| FE existing-content audit, overlap, freshness, syllabus, or gap review | [FE audit](fe-audit-rules.md); [source rules](primary-source-audit-rules.md) when sources/freshness are involved |
| Read-only full FE audit | [full-audit prompt](fe-full-audit-prompt.md) together with the FE audit route; do not repair articles during the report task |
| SG series/summary creation or learning-sequence/navigation changes | [series summaries](sg-series-summary-rules.md), [SG navigation](sg-navigation-rules.md) (canonical authorization boundary) |
| SG early judgment/role blocks | [SG improvement guide](../../project_rules/sg_article_ai_search_improvement.md); do not add blocks mechanically |
| DS or GK prev/next/grouping changes | [DS navigation](ds-navigation-rules.md) or [GK navigation](gk-navigation-rules.md) |
| GK portal, hierarchy, classification visibility, or index includes | [GK index](gk-index-rules.md); its actual source is `pages/gk/Index.md` |
| GK Instagram carousel | [carousel rules](gk-carousel-rules.md) plus GK content; use the linked generation repository only for execution details |
| Laws, standards, RFCs, current software behavior, original papers, or source audits | [primary-source audit](primary-source-audit-rules.md); retain theme writing requirements |
| Layouts/includes/indexes/shared navigation/CSS | [Pages compatibility](github-pages-compat.md), [theme consistency](theme-consistency.md), [editing/verification](editing-workflow.md), and affected theme route |
| Homepage update list | [homepage updates](home-updates-rules.md) |
| IndexNow/deployment notification changes | [IndexNow](indexnow.md) |
| Metadata repair, troubleshooting, or repository verification | [editing workflow](editing-workflow.md), theme front matter, [metadata writing](metadata-rules.md) when descriptions change |
| Agent instruction changes | [instruction regression](instruction-regression.md); run automatic reference checks and affected scenario checks |

## Canonical ownership

| Topic | Canonical home |
| --- | --- |
| Always-on priorities, boundaries, MUSTs | `AGENTS.md` |
| Task routing / when to load a guide | This file |
| New article vs update, overlap, learning purpose, editorial roles, reader usefulness, learning paths | [editorial rules](editorial-rules.md) |
| Source selection, current vs original authority, freshness, supersession, source-addition decisions | [primary-source rules](primary-source-audit-rules.md) |
| Shared description-writing policy | [metadata rules](metadata-rules.md) |
| Theme-specific structure, metadata fields, dates, tags, exam focus | The corresponding theme guide |
| SG prev/next authorization and series order | [SG navigation](sg-navigation-rules.md) |
| Build troubleshooting, encoding, verification and reporting | [editing workflow](editing-workflow.md) |
| Instruction regression scenarios and limits | [instruction regression](instruction-regression.md) |

Other files may link to or briefly summarize a rule. Do not maintain another complete procedure there. If two guides conflict, correct their ownership/definitions; do not resolve drift by adding more exceptions.
