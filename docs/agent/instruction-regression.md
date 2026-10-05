# Instruction Regression Checks

Use this suite when changing agent instructions. FE is exercised frequently through example questions; SG/DS/GK must still be tested at shared-policy changes so infrequent use does not delay discovery.

## Two different checks

1. **Mechanical:** run `python scripts/check_agent_instructions.py` and `python -m unittest discover -s tests -p 'test_agent_instructions.py'`. The dedicated Actions workflow checks missing/case-mismatched rule references on instruction changes. It does not judge article correctness or agent behavior.
2. **Behavioral:** start from AGENTS and the rule map, follow each affected scenario below, and record the decision, guides actually read, evidence, and result. For shared routing/editorial/source/metadata changes, cover every theme, not only FE. Prefer a fresh conversation for a later independent check; same-session dry runs are limited evidence.

Behavioral dry runs produce decisions/outlines, not published test articles. Do not invent current official-source verification, force updates to sufficient articles, or change real navigation just to test a rule.

## Scenarios and acceptance criteria

| ID | Input / prompt | Expected observable behavior |
| --- | --- | --- |
| FE-1 | Example describes repeatedly halving sorted search data; consider a new article. | Search all themes, read existing FE binary-search article and nearby roles, choose update/no change when sufficient; do not create a second article just from different wording. |
| FE-2 | Approved example-derived array/trace article using an unseen screenshot. | Title names the reusable concept; explanation includes required values, index convention and trace independently; 科目B section gives a concrete solving skill; check FE classification, footer, FE-only related links and no unsolicited prev/next. |
| FE-3 | Copyright example; consider an FE article. | Search existing copyright pages; strengthen 科目A distinctions; no forced 科目B section from merely appearing in a long scenario. |
| FE-4 | A term appears absent and the user asks only for article necessity analysis. | Search all themes and compare learning roles before recommending new/update/comparison/no change; do not publish an article at the proposal-only stage. |
| FE-5 | Read-only full FE audit; a redirect helper lacks normal article headings. | Load FE audit and full-audit guides; classify helper first, check its target, report candidates; do not normalize helper or auto-repair articles. |
| SG-1 | Correct one definition and refresh a source on an ordinary SG article. | Load SG bundle and source guide; preserve structure; no prev/next addition or series reorganization. |
| SG-2 | Explicitly reorganize an authentication/access-control series; no target URLs supplied. | Verify articles/roles/permalinks; agent may choose individual-article neighbors within that request; update the learning map; no unrelated sequence. |
| SG-3 | Create only an authentication summary page; no footer-style entry requested. | Provide body learning order and category link; no summary prev/next and no unsolicited edits to individual-article prev/next. A separately requested next-only entry is the explicit exception. |
| DS-1 | Revise a sample/unbiased variance explanation. | Load DS bundle, metadata and visual-aid route; intuition before formulas, denominator distinction, no invented publication date or forced learning sequence; keep existing footer/category conventions. |
| GK-1 | Refresh a Transformer article; then review a broad mathematical concept. | Named model gets a conscious original-paper decision; generic concept does not get a forced paper section; preserve GK headings/group/order/footer. |
| GK-2 | Reorganize one GK portal branch. | Load GK index guide, use actual `pages/gk/Index.md`, inspect sibling/direct-parent placements, distinguish committed and deployed, check rendered visibility before completion. |
| SHARED-1 | A cited RFC is superseded; a description is generic; low-traffic overlapping pages exist. | Shared source guide controls current/historical handling and repository-wide sweep; metadata guide controls specific description; evaluate learning purpose rather than automatic merge/deletion, and surface early judgment only if needed. |

## Record results

Keep dated run records under `docs/agent/regression-results/` (excluded from public site output). Record the base/updated commit, scenario IDs, evidence, pass/fail/blocked, execution method, unresolved concerns and deployment result. Avoid asserting a numeric score proves future agent reliability.

An automatic pass does not replace behavioral review. A behavioral dry run does not replace Jekyll/Pages checks for changes that affect rendering. Re-run only affected scenarios for a narrow theme change; shared policy/routing changes require the full matrix.
