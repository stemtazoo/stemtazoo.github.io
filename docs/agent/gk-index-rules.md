# GK Index Rules

This file is written in English for Codex readability. Use these rules when editing the G検定 portal, section hierarchy, or index-generation behavior.

Primary files:

- `pages/gk/Index.md`
- `_includes/gk_section.html`
- article front matter under `pages/gk`

## Source of Truth

- `gk_sections` in `pages/gk/Index.md` defines heading structure only.
- Individual articles define placement with `gk_section` and order with `gk_order`.
- Section-path strings must match the hierarchy exactly, including Japanese wording, punctuation, spaces, and `/`.
- Do not use stale GitHub code-search results to verify a write. Re-fetch the file from the default branch.

## Hierarchy Changes

- Before adding `subsections`, inspect current direct assignments for that parent.
- Do not assume parent-direct articles remain visible after nesting; verify `_includes/gk_section.html` behavior.
- When changing a multi-level hierarchy, test more than the first child. Verify sibling sections at the same level also resolve to the correct paths.
- Recursive Liquid variables must not leak path state from one sibling include call to the next.
- Prefer semantic learning-path grouping over filename grouping.
- Avoid unnecessary singleton subgroups unless the distinction materially improves the learning path.

## Public Rendering Verification

- Correct front matter is not proof that the public portal renders correctly.
- After index/include changes are deployed, check `/gk/` on the actual rendered site.
- Specifically check:
  - expected article links appear under each heading;
  - no unexpected `準備中です。` appears where articles exist;
  - sibling subsections all render;
  - heading depth is understandable on mobile;
  - long article titles remain usable.
- Treat “committed to GitHub” and “deployed to GitHub Pages” as separate states.
- If a change is not visible, check the Pages build/deployment status before rewriting content.

## Final Integrity Audit

Before declaring a large GK reorganization complete, check:

- GK articles with `tags` containing `gk` but no `gk_section`;
- `gk_section` without `gk_order`, and vice versa;
- section paths not represented by a leaf or supported direct-parent path in `Index.md`;
- articles left directly on a parent after nesting when that placement is unintended;
- duplicate `gk_order` values within the same leaf;
- empty leaf sections;
- semantically duplicate articles or duplicate learning-path entries.

Use direct default-branch file reads for final verification.

## Duplicate Article Handling

- Do not delete a duplicate page only to clean the portal.
- Choose a canonical article first.
- Preserve an established old permalink with a small legacy/guide page when link stability matters.
- Remove the legacy page from GK listing metadata; use `sitemap: false` when appropriate.
- Point readers clearly to the canonical article.
- If redirect support is not installed, do not assume `redirect_from` works.

## Official JDLA Information

- Keep a visible link from the GK portal to the official JDLA G検定 page:
  `https://www.jdla.org/certificate/general/`
- Use JDLA official material as the primary source for exam scope, syllabus, application information, and current exam details.
- Do not hardcode claims that a syllabus version is the latest without re-verifying the official source.
- Article organization may be optimized for learning, but should not silently contradict official syllabus terminology or scope.
- Learning-path subgroups may be more pedagogical than the official syllabus headings, but official names and scope should be preserved when describing the exam.

## Completion Rule

Only call a GK index reorganization structurally complete when:

1. metadata paths are internally consistent;
2. index/include rendering logic is correct;
3. the deployed `/gk/` page has been visually checked;
4. the final integrity audit has no unresolved visibility or classification errors.
