# FE Full Audit Prompt for Codex

This prompt is for auditing all 基本情報技術者試験 (FE) articles under `pages/fe/`.

## Purpose

Audit the entire FE article collection without editing articles.

The goal is to identify candidate problems mechanically and consistently, then hand the candidates to a human/LLM reviewer for semantic judgment before any repair is made.

**Do not modify FE articles in this task.**
**Do not auto-fix detected problems.**
**Do not create commits that change article content.**

Create only the audit report described below.

## Rules to read first

Before auditing, read the latest versions of:

- `AGENTS.md`
- `docs/agent/fe-content-rules.md`
- `docs/agent/fe-article-template.md`
- `docs/agent/fe-frontmatter-rules.md`
- `docs/agent/fe-tag-rules.md`
- `docs/agent/ai-search-content-rules.md`
- `docs/agent/github-pages-compat.md`
- `docs/agent/theme-consistency.md`

Treat these files as the source of truth.

## Scope

Audit all Markdown files under:

```text
pages/fe/**/*.md
```

Exclude index/navigation/helper pages only when their role clearly differs from a normal FE article. Record excluded files separately with the exclusion reason.

## Audit policy

Separate findings into two categories.

### A. Mechanical findings

These are findings that can be detected with high confidence from file structure or exact rules.

Check every normal FE article for:

1. **Front matter validity**
   - starts and ends with `---`
   - `layout: page`
   - `title`
   - `description`
   - `permalink`
   - `tags`
   - `fe_section`
   - `fe_subsection`
   - `fe_order`
   - `date`
   - `last_modified_at`
   - valid `YYYY-MM-DD` dates
   - no accidental front-matter keys leaked into visible body text

2. **Permalink rules**
   - `/fe/english-slug/` format
   - duplicate permalinks
   - obviously malformed slugs

3. **Title rules**
   - normal articles should normally include `【基本情報技術者試験】`
   - flag inconsistent variants such as `【基本情報技術者】`
   - flag duplicate titles

4. **Tag rules**
   - includes `fe`
   - exactly one primary category tag from:
     - `fe-technology`
     - `fe-management`
     - `fe-strategy`
   - roughly 3 to 5 tags
   - no SG/DS/GK-only category tags
   - flag rare one-off tag spellings and likely synonyms for manual review

5. **FE index metadata**
   - valid `fe_section`
   - non-empty `fe_subsection`
   - numeric `fe_order`
   - duplicate `fe_order` values within the same `fe_section` + `fe_subsection` group should be flagged as candidates, not automatically considered errors

6. **Standard article headings**
   For normal articles, check for the expected core headings:
   - `## まず結論`
   - `## 直感的な説明`
   - `## 定義・仕組み`
   - `## 科目Aでどう出る？`
   - either `## 科目Bでどう使う？` or `## どんな場面で使う？` where appropriate
   - `## よくある誤解・混同`
   - `## まとめ（試験直前用）`

   Flag:
   - missing headings
   - old numbered headings such as `## 1. まず結論`
   - obvious old/alternate heading names
   - duplicate standard headings

   Do **not** mechanically declare a missing `科目B` heading to be an error. Subject B relevance requires semantic review.

7. **Footer include**
   Normal FE articles should end with:

   ```liquid
   {% include fe_article_footer.html %}
   ```

   Flag:
   - missing footer
   - wrong include name
   - manual large related-article Liquid blocks in place of the shared footer
   - any include target that does not exist under `_includes/`

8. **Deprecated navigation fields**
   - flag `prev` / `next` in front matter
   - flag visible body text that appears to duplicate prev/next navigation

9. **Markdown/Jekyll safety**
   - malformed tables
   - unclosed fenced code blocks
   - suspicious Liquid include syntax
   - raw front-matter fragments in article body
   - raw official URLs where Markdown links should be used

10. **Internal links**
    - inspect local links beginning with `/fe/`, `/sg/`, `/ds/`, `/gk/`, and relative Markdown links
    - flag destinations that do not appear to exist in the repository
    - do not treat intentional external URLs as internal links

11. **Description quality candidates**
    Mechanically flag for review:
    - exact duplicate descriptions
    - very short descriptions
    - obvious boilerplate phrases repeated across many pages
    - description identical to a visible body sentence

12. **Potential duplicate articles**
    Identify candidate pairs/groups using:
    - same or nearly same title term
    - very similar slug
    - highly overlapping headings/keywords

    Do not decide deletion or merge automatically. Report as semantic-review candidates.

## B. Semantic-review candidates

The following require judgment. Codex should identify candidates and explain why they need review, but must not automatically rewrite them.

### 1. Subject B relevance

For every article containing `## 科目Bでどう使う？`, check whether the section appears to provide a concrete solving skill consistent with `docs/agent/fe-content-rules.md`.

Flag articles where the Subject B section only says things like:

- this may appear in a long scenario
- this is useful background knowledge
- it is related to system design in general
- it may be useful for understanding a problem

High-value Subject B sections should contain concrete guidance such as:

- what variable/index/condition to trace
- what data-structure operation occurs
- how recursion terminates
- how to detect a bug/correction
- which security control should be selected and why

Also identify articles that **do not** have a Subject B section but are strong Subject B candidates, especially:

- pseudocode
- recursion
- stacks/queues
- arrays
- trees/graphs/linked lists
- sorting/searching
- string processing
- program tracing
- debugging
- information-security controls, logs, access management, backups, vulnerabilities, malware protection, and secure transfer

Do not auto-add the section.

### 2. Classification quality

Flag articles whose `fe_section` or `fe_subsection` appears inconsistent with the article topic or nearby articles.

Examples:

- algorithm/data-structure article placed outside `科目B対策` without clear reason
- law article placed in a technology subsection
- network article placed in an unrelated subsection

Do not change classification automatically.

### 3. Exam judgment quality

Flag articles where:

- `科目Aでどう出る？` is mostly a generic definition instead of answer-choice judgment
- `よくある誤解・混同` has no actual confusion/distractor distinction
- `まとめ（試験直前用）` is generic and lacks reusable judgment criteria
- the article appears to explain the source example question rather than the reusable concept

### 4. Standalone readability

Flag articles that depend on unseen source material, including phrases such as:

- `この問題`
- `この例題`
- `上の図`
- `設問の表`
- answer letters such as `アが正解`, `ウが正解`

Only flag when the surrounding article does not reproduce all necessary context.

### 5. Cross-article role overlap

Identify candidate articles whose roles overlap heavily enough that a reviewer should consider:

- keeping both with clearer role division
- adding mutual internal links
- merging
- converting one to a comparison/summary page

Do not merge or delete anything.

## Severity

Use these severity levels:

- **P0 — Build risk**: can break Jekyll/GitHub Pages build, such as nonexistent include targets, malformed Liquid, broken front matter
- **P1 — Structural**: normal article missing required metadata, footer, core headings, duplicate permalink
- **P2 — Classification / exam-role review**: Subject B mismatch, wrong section/subsection, likely duplicate/overlap, weak exam judgment structure
- **P3 — Quality improvement**: description quality, wording consistency, minor tag cleanup, non-critical link or formatting improvement

## Required output

Create one report:

```text
docs/audits/fe-full-audit-YYYY-MM-DD.md
```

Use the actual audit date.

The report must contain these sections in this order:

### 1. Summary

Include:

- total Markdown files scanned
- normal articles audited
- excluded/non-normal pages
- count of findings by P0/P1/P2/P3
- count of articles with no findings

### 2. P0 Build risks

Table columns:

| File | Finding | Evidence | Suggested next step |

### 3. P1 Structural findings

Same table format.

### 4. P2 Semantic/classification candidates

Table columns:

| File | Review topic | Why it needs semantic review | Suggested reviewer question |

### 5. P3 Quality candidates

Table columns:

| File | Finding | Evidence | Suggested next step |

### 6. Subject B review list

Split into:

- Existing `科目Bでどう使う？` sections that should be reviewed
- Articles without a Subject B section that may deserve one

For each article, give a one-sentence reason.

### 7. Duplicate / overlap candidates

Group likely overlapping articles and explain the suspected overlap in one or two sentences.

### 8. Excluded files

List files excluded from normal-article checks and why.

### 9. Clean articles

List normal FE articles for which no audit issue was detected.

### 10. Recommended repair batches

Group repair candidates into small batches of about 5 to 15 articles, prioritizing:

1. P0
2. P1
3. P2
4. P3

Keep semantically risky fixes separate from mechanical fixes.

## Important execution rules

- Audit first; **do not repair articles in this task**.
- Do not rewrite large groups just to make formatting uniform.
- Do not infer missing classifications solely from filenames when the body gives better evidence.
- Do not create new tags without checking existing tag vocabulary.
- Do not remove unusual pages merely because they differ from normal articles.
- When uncertain, report a candidate instead of making a confident error claim.
- Include exact file paths in every finding.
- Keep evidence concise and specific.
- Avoid flooding the report with one row per trivial style issue when several identical findings can be grouped without losing file-level traceability.

## Final self-check

Before finishing the report, verify that:

- no FE article content was edited;
- no article was deleted or renamed;
- the report distinguishes mechanical errors from semantic-review candidates;
- all P0/P1 findings have concrete evidence;
- Subject B findings follow the current official-scope rules in `fe-content-rules.md`;
- the report is useful for a second-stage reviewer to decide what to fix.