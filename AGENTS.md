# AGENTS.md

This is the entry point for agents and collaborators modifying this Jekyll / GitHub Pages study site.
Detailed procedures have one canonical home under `docs/agent/`. Read only the guides relevant to the task, using `docs/agent/README.md`.

## Purpose

Provide correct, beginner-friendly Japanese study content under `pages/ds`, `pages/gk`, `pages/sg`, and `pages/fe`, while preserving GitHub Pages builds and a consistent reader experience.

## Core Priorities

When making changes, use this order of priority:

1. Keep GitHub Actions / GitHub Pages builds passing.
2. Preserve or improve content correctness.
3. Maintain layout consistency across themes.
4. Prefer simple, GitHub Pages-compatible Liquid over clever Liquid.
5. Avoid changes that create theme-by-theme drift unless explicitly requested.
6. Maintain coherent sitewide information architecture.
7. Avoid unnecessary duplicate or near-duplicate content.
8. Preserve or improve reader usefulness and original value.
9. Keep navigation clear across themes and category pages.

## Repository-wide MUSTs

- Before new articles or meaningful content edits, read `docs/agent/editorial-rules.md` and the theme's content, template, front-matter, and tag guides listed in `docs/agent/README.md`.
- Search all four themes before creating an article. Give each page a clear learning purpose; do not create near-duplicates or merge useful pages merely for sharing terms or having low traffic.
- Preserve the existing Japanese tone, heading conventions, beginner readability, exam judgment criteria, and confusion prevention. Treat examples and screenshots as input for a standalone explanation, not as unseen prerequisites.
- Current official rules are authoritative for current claims. Use `docs/agent/primary-source-audit-rules.md` for source selection, freshness, original-paper decisions, and supersession checks; distinguish historical exam assumptions from current rules.
- Do not add sources, headings, learning-path blocks, or interactive aids mechanically. Preserve reader usefulness and originality over search or monetization optimization.
- Preserve UTF-8, valid YAML, stable permalinks, and metadata/include dependencies. Set `last_modified_at` on new articles; follow the theme's rules for meaningful edits and publication-date provenance.
- Keep GitHub Pages-compatible Markdown and simple Liquid. For layout/include/index changes, use `docs/agent/github-pages-compat.md` and `docs/agent/theme-consistency.md` and verify rendered behavior.
- Do not present a commit as a successful deployment. Follow `docs/agent/editing-workflow.md` and report checks performed, build status, and material verification limits.

## Theme boundaries

- **FE:** prioritize 科目A judgment and concrete 科目B solving skills only when directly relevant. Normal articles require tags, `fe_section`, `fe_subsection`, `fe_order`, and the FE footer. Related articles stay within FE. Do not add prev/next without an explicit request. Example-driven article consideration must preserve standalone readability.
- **SG:** prioritize workplace/security decisions and bridge 科目A to 科目B. Read the example-question guide for SG article work. Prev/next authorization and series design are defined only in `docs/agent/sg-navigation-rules.md`.
- **GK:** prioritize intuition, similar-term distinctions, and answer-choice judgment; avoid unnecessary derivations. Preserve GK grouping, order, and footer conventions. Load carousel guidance only for carousel work.
- **DS:** prioritize intuition, practical Python/SQL/statistics use, and exam judgment. Preserve valid categories, tags, and related/navigation conventions unless cleanup is requested.

## Routing and rule ownership

- The task-to-guide map and canonical ownership table are in `docs/agent/README.md`. Follow conditional routes such as FE audits, GK index changes, SG series work, interactive aids, source reviews, and homepage updates.
- Detailed guides refine this file; an audit or optional enhancement never overrides article quality or current official facts.
- A guide owns its topic; other files link to it rather than repeating its full procedure. If guides conflict, resolve the conflicting definitions instead of adding another exception.
- When changing instructions, run `python scripts/check_agent_instructions.py` and the relevant scenarios in `docs/agent/instruction-regression.md`. Shared routing or policy changes require all four themes, even if actual editing is mostly FE.
- Keep fixes small and focused. Do not expand a requested review into unrelated article or navigation changes.
