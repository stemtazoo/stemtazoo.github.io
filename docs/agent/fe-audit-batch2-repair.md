# FE Audit Batch 2 Repair Instructions

Apply the reviewed Batch 2 fixes from `docs/audits/fe-full-audit-2026-08-29.md`.

## Important execution rules

- Read the latest FE rules before editing:
  - `AGENTS.md`
  - `docs/agent/fe-content-rules.md`
  - `docs/agent/fe-article-template.md`
  - `docs/agent/fe-frontmatter-rules.md`
  - `docs/agent/fe-tag-rules.md`
- Modify only the files explicitly listed below, except where this file explicitly says **no change**.
- Do not broadly rewrite article bodies.
- Preserve good examples, tables, internal links, and explanations already present.
- When adding `date`, use the article's actual initial creation date from Git history, not today's date. If the file was renamed or introduced through a move, use the earliest reliable article-origin date you can establish.
- For every article actually edited, set `last_modified_at: 2026-08-29`.
- For missing `fe_order`, inspect nearby articles in the same `fe_section` + `fe_subsection` and choose a sensible numeric position. Avoid changing other articles merely to create spacing.
- Normal FE articles must end with `{% include fe_article_footer.html %}`.
- Do not force a Subject B section unless it provides a direct solving skill under the current Subject B rules.

## Reviewed decisions

### 1. `pages/fe/business-impact-analysis.md`

Finding: missing standard `## 科目Aでどう出る？` heading.

Decision: **repair**.

- Keep the existing BIA / BCP / BCM / MTD / RTO explanation.
- Add `## 科目Aでどう出る？` between `## 定義・仕組み` and `## どんな場面で使う？`.
- Move or reuse existing exam-judgment content rather than duplicating it.
- The section should emphasize these reusable distinctions:
  - impact analysis / maximum tolerable downtime -> BIA;
  - continuity/recovery plan -> BCP;
  - ongoing training, exercises, review -> BCM;
  - MTD = limit, RTO = target.
- Do not add a Subject B section.

### 2. `pages/fe/capacity-management-analysis-methods.md`

Finding: missing `fe_order` and `date`.

Decision: **metadata repair only** unless validation reveals another mechanical rule violation.

- Add `date` from Git history.
- Add a sensible `fe_order` within `マネジメント系 / サービスマネジメント` by checking nearby articles.
- Preserve article body and headings.

### 3. `pages/fe/cell-production-system.md`

Finding: missing `date`.

Decision: **metadata repair only**.

- Add the actual creation `date` from Git history.
- Preserve all other metadata and body content.

### 4. `pages/fe/cia-triad.md`

Finding: primary FE category tag is invalid under the current tag rules (`fe-security` is not one of the three allowed primary category tags).

Decision: **tag repair**.

- Replace `fe-security` with `fe-technology`.
- Keep useful concrete tags such as `information-security` and `cia` unless they violate another explicit rule.
- Keep `fe_section: テクノロジ系` and the current article body.

### 5. `pages/fe/communication-encryption-eavesdropping.md`

Finding from automated audit: many normal-article fields/headings/footer appear missing.

Decision: **NO CHANGE — false positive**.

This file is an intentional redirect/helper page:

- `layout: null`
- `sitemap: false`
- `noindex,follow`
- meta refresh to `/fe/eavesdropping-encryption/`

Do not convert it into a normal article. Do not add FE article front matter, standard headings, tags, or footer.

### 6. `pages/fe/communication-paths-combination.md`

Finding: missing `date`.

Decision: **metadata repair only**.

- Add the actual creation `date` from Git history.
- Preserve the existing project-management classification and article body.

### 7. `pages/fe/competitive-position-strategy.md`

Finding: missing `fe_order`.

Additional reviewed inconsistency: `fe_subsection: 経営戦略マネジメント` does not match the current nearby FE strategy vocabulary used by related articles such as benchmarking, BPM, Ansoff, and business domain.

Decision: **classification metadata repair**.

- Change `fe_subsection` to `経営戦略`.
- Add a sensible `fe_order` by inspecting nearby `ストラテジ系 / 経営戦略` articles.
- Preserve the article body.

### 8. `pages/fe/compliance.md`

Finding: missing standard `## 科目Aでどう出る？` heading.

Decision: **repair**.

- Keep the existing explanation of compliance, CSR, governance, internal control, and core competence.
- Add `## 科目Aでどう出る？` between `## 定義・仕組み` and `## どんな場面で使う？`.
- Reuse/move existing judgment content rather than duplicating it.
- Focus on answer-choice elimination:
  - laws/rules/social norms -> compliance;
  - social/environmental responsibility -> CSR;
  - organizational governance -> governance;
  - internal mechanisms for proper operations -> internal control.
- Do not add a Subject B section.

### 9. `pages/fe/contingency-plan.md`

Finding: missing `fe_order` and `date`.

Decision: **metadata repair only** unless validation reveals another mechanical rule violation.

- Add actual creation `date` from Git history.
- Add a sensible `fe_order` within `マネジメント系 / プロジェクトマネジメント` near risk-management topics.
- Preserve article body.

### 10. `pages/fe/contract-for-work-vs-mandate.md`

Finding: missing `fe_order` and `date`.

Decision: **metadata repair only**.

- Add actual creation `date` from Git history.
- Add a sensible `fe_order` within `ストラテジ系 / 法務` near contract-related articles.
- Preserve body content.

### 11. `pages/fe/contract-nonconformity-liability.md`

Finding: missing `fe_order` and `date`.

Decision: **metadata repair only**.

- Add actual creation `date` from Git history.
- Add a sensible `fe_order` within `ストラテジ系 / 法務` near contract-related articles.
- Do not change the concrete `legal-affairs` tag in this batch; one-off/concrete tag vocabulary cleanup belongs to the later tag-quality review unless it causes a current hard-rule violation.
- Preserve body content.

### 12. `pages/fe/contract-types-outsourcing.md`

Findings:

- missing `date`;
- title suffix uses `【FE試験】` instead of the standard `【基本情報技術者試験】`;
- missing standard `## 科目Aでどう出る？` heading.

Decision: **repair**.

- Change only the title suffix from `【FE試験】` to `【基本情報技術者試験】`; keep the rest of the title wording.
- Add actual creation `date` from Git history.
- Add `## 科目Aでどう出る？` after the definition/mechanism material and before the practical-use section (or at the nearest standard-template position).
- Reuse/move existing exam-oriented distinctions instead of duplicating them.
- The section should emphasize:
  - completed deliverable / completion responsibility -> 請負;
  - proper performance of professional work -> 準委任;
  - direction and orders from the dispatch destination -> 派遣;
  - employment relationship -> パート等の雇用;
  - contract-nonconformity responsibility when a contracted deliverable does not match agreed content.
- Do not add a Subject B section.
- Preserve `fe_order: 100` unless inspection shows it is invalid for the current listing.

## Validation after editing

After the edits:

1. Confirm that only the 11 repair-target articles changed; `communication-encryption-eavesdropping.md` must remain unchanged.
2. Validate YAML front matter for all changed files.
3. Confirm each changed normal article has:
   - `layout: page`;
   - title/description/permalink/tags;
   - exactly one FE primary category tag (`fe-technology`, `fe-management`, or `fe-strategy`);
   - `fe_section`, `fe_subsection`, `fe_order`;
   - `date` and `last_modified_at`;
   - the shared FE footer.
4. Confirm newly added `date` values come from Git history, not from the repair date.
5. Confirm `business-impact-analysis.md`, `compliance.md`, and `contract-types-outsourcing.md` contain exactly one `## 科目Aでどう出る？` section.
6. Confirm no weak/forced `## 科目Bでどう使う？` section was added.
7. Run `git diff --check`.
8. Run the Jekyll build if dependencies are available. If the local environment cannot install dependencies, report that clearly and rely on GitHub Actions after merge for final build validation.

## PR / commit summary

In the PR description, explicitly report:

- which 11 articles were repaired;
- that `communication-encryption-eavesdropping.md` was intentionally left unchanged because it is a redirect page and the audit finding was a false positive;
- the creation dates derived from Git history;
- the chosen `fe_order` values and why they fit nearby articles;
- whether the Jekyll build was completed locally.