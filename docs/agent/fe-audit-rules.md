# FE Audit Rules

This file defines the workflow for auditing existing 基本情報技術者試験 (FE) content under `pages/fe`.

Use it for repository-wide or multi-article reviews such as source audits, freshness audits, duplicate-content audits, syllabus-alignment audits, internal-link audits, structure audits, and content-gap audits.

This file does **not** replace the FE article-writing rules. When an audit results in an article edit, the edited article must still comply with:

- `AGENTS.md`
- `docs/agent/fe-content-rules.md`
- `docs/agent/fe-article-template.md`
- `docs/agent/fe-frontmatter-rules.md`
- `docs/agent/fe-tag-rules.md`
- other relevant shared rules under `docs/agent/`

## When To Use This File

Read this file before work whose main purpose is to evaluate existing FE content across one or more pages, including:

- checking whether official or primary sources should be added or refreshed;
- checking whether laws, standards, guidelines, or specifications have been superseded;
- checking duplicate or near-duplicate articles;
- checking whether articles still match the current FE syllabus and examination scope;
- checking article structure, metadata, tags, internal links, category placement, or learning flow;
- checking whether important FE topics are missing;
- deciding which existing articles should be updated and which should remain unchanged.

Do not require a full audit for a small typo fix or a narrowly requested wording change. For a new article, use the normal new-article decision workflow in `AGENTS.md` and the FE content rules first. If the request also asks for a broader review of existing content, use this audit file as well.

## Rule Precedence And Quality Guardrail

An audit is a **decision process**, not permission to weaken article quality.

When rules appear to pull in different directions, use this order:

1. Build safety and repository-wide requirements in `AGENTS.md`.
2. Current official facts, laws, standards, and FE examination scope.
3. FE content, article-template, front-matter, and tag rules.
4. The audit workflow in this file.
5. Optional audit improvements.

Therefore:

- Do not add a source merely because an audit found one.
- Do not add a new heading merely to hold a source.
- Do not make an article longer unless the added material improves correctness, freshness, exam judgment, or learner understanding.
- Do not replace beginner-friendly explanations with standards language.
- Do not force a Subject B section because a source mentions programming or security; use the Subject B relevance rules in `fe-content-rules.md`.
- Do not create a new article merely because a source audit reveals a related concept; content-gap review and source audit are separate decisions.
- Do not merge intentionally separate learning articles merely because their terminology overlaps.
- Preserve the site's core value: beginner-friendly explanations, answer-choice elimination criteria, confusion prevention, and useful learning flow.

## Audit Scope Before Editing

Before changing files:

1. Define the audit purpose and target area.
2. Search relevant FE pages by filename, title, front matter, headings, and body text.
3. When overlap may exist, also search `pages/sg`, `pages/ds`, and `pages/gk`.
4. Read the current target article before deciding to update it.
5. Check nearby articles so wording, granularity, metadata, and internal links remain consistent.
6. Separate findings into:
   - article correction/update;
   - source/freshness update;
   - duplicate/role clarification;
   - internal-link/navigation improvement;
   - content gap;
   - no change needed.

Do not treat every finding as an article edit.

## Primary And Official Source Audit

### Source Priority

Choose the source that best matches the claim being supported.

Typical priority:

1. Japanese official authorities for Japanese exams, laws, public systems, and government guidance:
   - IPA;
   - ministries and agencies;
   - e-Gov or other responsible public bodies.
2. International standards organizations:
   - ISO / IEC;
   - IEEE;
   - ITU.
3. Internet and web standards organizations:
   - IETF / RFC Editor;
   - W3C / WHATWG;
   - ECMA where applicable.
4. Technology originators, maintainers, or official projects:
   - OMG;
   - Apache;
   - GNU;
   - other responsible project or vendor documentation when it defines the technology.
5. Original papers or books by the proposer when the historical origin or original model matters.

Secondary explanations may be used for discovery or context, but they should not displace a stronger available primary source for normative or origin claims.

### Original Source And Current Source Are Different Roles

Do not confuse historical origin with current authority.

Use:

- an original paper or book to support who proposed a concept or how it was originally formulated;
- the latest standard or official documentation to support current specifications, requirements, terminology, or rules;
- the latest IPA material to support current FE examination scope.

An article may need one, both, or neither.

Example:

```text
History / origin
→ original paper or original book

Current specification
→ latest official standard or documentation

Current FE scope
→ latest IPA syllabus / examination guidelines
```

### Latest-Version Check

For laws, standards, official guidelines, audit criteria, specifications, and other versioned normative material:

- verify whether the cited version is still current;
- check for a successor, revision, replacement page, or superseding standard;
- keep the article body based on the current official rule by default;
- retain historical material only when it is necessary to understand a past question or the development of the concept;
- label historical rules clearly so they cannot be mistaken for current requirements.

This audit rule supplements, and never weakens, the Latest Official Version Policy in `fe-content-rules.md` and `AGENTS.md`.

## Source-Addition Decision

Classify each source finding before editing.

### 1. Add / Update Recommended

Update the article when the source materially improves at least one of:

- factual correctness;
- currentness;
- authority or traceability;
- an FE answer-choice judgment criterion;
- distinction from a commonly confused term;
- clarification of a material misconception.

### 2. Existing Article Is Sufficient

Do not edit when:

- an appropriate current primary source is already present;
- the proposed source would only duplicate an existing authority;
- the existing explanation is correct and sufficiently supported.

### 3. Source Exists But Addition Is Unnecessary

Do not edit when:

- the source is historically interesting but does not help FE learning;
- the source would add specialist detail beyond FE scope;
- adding it would make a concise article harder to read;
- the source does not improve the article's judgment criteria or correctness;
- a generic mathematical or computer-science fact does not need an origin citation to be useful.

The default is **not** "find a source, then add it." The default is "add only when it improves the article."

## Source Placement And Writing

When a source is worth adding:

- integrate it near the claim it supports when that is natural;
- a short dedicated source section is acceptable when provenance itself helps understanding;
- do not mechanically add a `## 一次情報` or `## 公式資料` heading to every article;
- keep source commentary short;
- use clickable Markdown links, never raw URLs;
- use clean canonical URLs without tracking parameters;
- explain the FE-relevant takeaway in beginner-friendly Japanese;
- do not copy long passages from the source;
- do not make source names, publication history, or standard numbers into memorization targets unless the FE scope genuinely requires them.

## Duplicate And Role Audit

When two or more pages overlap, compare:

- search intent;
- target learner;
- article role;
- headings and explanation scope;
- title / description / permalink;
- tags and FE category placement;
- exam judgment criteria;
- internal links.

Possible outcomes:

- keep both and clarify roles;
- update one page;
- create or improve a comparison/summary page;
- consolidate only when learning roles are genuinely redundant;
- improve internal links without changing article bodies;
- leave unchanged.

Do not merge pages solely because they share keywords. Similar terms may intentionally have separate pages for learning and comparison.

## Syllabus And Subject-B Audit

When auditing FE scope:

- use the latest official IPA examination guidance;
- distinguish current scope from older past-question assumptions;
- apply the Subject B decision process in `fe-content-rules.md`;
- remove or rewrite weak Subject B claims that are only indirect background;
- do not expand an article beyond its learning role just to mention Subject B.

A source audit must not silently become a scope-expansion audit.

## Content-Gap Audit

A missing topic is not automatically a new-article recommendation.

Before proposing a new article:

1. search FE and related SG / DS / GK content;
2. determine whether the concept is already sufficiently explained;
3. check whether an existing article should be expanded instead;
4. confirm that a new page has a distinct search intent and learning role;
5. apply the New Article Decision Workflow in `AGENTS.md`.

Keep source auditing and content-gap decisions separate.

## Internal Links And Learning Flow

When an audit changes article roles or reveals related concepts:

- check whether an internal link would improve confusion prevention or learning order;
- prefer links that help the reader move from prerequisite → concept → comparison / next concept;
- do not add links merely for SEO;
- do not create large manual related-link sections when the FE footer already handles related articles;
- preserve FE-only related-article behavior.

## Metadata And Edit Discipline

For every meaningful article edit produced by an audit:

- preserve the original `date`;
- update `last_modified_at`;
- follow `fe-frontmatter-rules.md`;
- keep title and description aligned with the article's actual role;
- do not change permalink casually;
- keep tags within `fe-tag-rules.md`;
- prefer small, focused commits.

If an audit finding does not require article changes, do not touch metadata merely to mark the audit as completed.

## Audit Reporting

At the end of an audit batch, report:

- what area was checked;
- which articles were updated;
- which important candidates were intentionally left unchanged and why;
- the authoritative sources added or refreshed when relevant;
- any separate content-gap or structural findings;
- commit hashes for repository edits.

Do not use completion percentages unless the audit scope is defined well enough for the percentage to be meaningful.

## Final Quality Check

Before finishing an audit-driven edit, confirm:

- the article remains understandable to an FE beginner;
- the main conclusion and exam judgment criterion are still easy to find;
- the source supports the claim actually made;
- a current source was used where current authority matters;
- an original source was used only where provenance/origin matters;
- no obsolete rule is presented as current;
- no unnecessary source or specialist detail was added;
- Subject B coverage still follows the FE content rules;
- headings still follow the FE article template;
- front matter and tags still follow their dedicated rules;
- internal links improve learning rather than merely increasing link count;
- no duplicate article was created as a side effect of the audit;
- GitHub Pages-compatible Markdown/Liquid is preserved;
- meaningful edits update `last_modified_at`;
- the article's beginner-friendly explanation, exam judgment, and confusion-prevention value did not get worse.
