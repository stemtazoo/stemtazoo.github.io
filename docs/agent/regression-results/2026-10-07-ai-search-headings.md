# AI-search fixed-heading clarification — 2026-10-07

- Base commit: `3269d9efd4819e185c1ef16f0f2f5c42d0ea36fd`.
- Updated revision: uncommitted working-tree change.
- Scope: clarify the practical heading check to match the existing fixed-heading preservation rule. No routing, article structure, source, metadata, or navigation policy changes.
- Method: same-session manual dry run, limited to the affected heading decisions across all four themes. This is not a full execution of the regression scenario matrix or an independent agent-behavior test.
- Guides read: `AGENTS.md`, `docs/agent/README.md`, `docs/agent/ai-search-content-rules.md`, `docs/agent/instruction-regression.md`, `docs/agent/editing-workflow.md`, and all four theme article templates.

## Affected scenario checks

| Scenario | Evidence and decision | Result |
| --- | --- | --- |
| FE-2, heading aspect | FE template retains `まず結論` and the applicable Subject A/B headings. The revised check requires explicit topic wording in the text below fixed headings; it does not require renaming them or adding Subject B. | Pass, scoped manual review |
| SG-1, heading aspect | SG template requires six fixed headings. Preserve them during a definition edit and check the text immediately below for an explicit topic or comparison. | Pass, scoped manual review |
| DS-1, heading aspect | DS template uses six fixed headings for standard articles. Preserve them for the variance explanation; freely worded subheadings can name the denominator comparison. | Pass, scoped manual review |
| GK-1, heading aspect | GK template retains its six fixed headings, including `G検定ひっかけポイント`. State the model or concept in the text below rather than renaming the heading. | Pass, scoped manual review |

## Verification and limits

- `git diff --check`: passed for the instruction change.
- Reference checker and `test_agent_instructions.py`: blocked. `python` is unavailable and `py` reports no installed Python. These checks must run in an environment with Python; no automatic pass is claimed.
- No test articles or navigation edits were made.
- Jekyll build, GitHub Actions, and deployment status were not checked. No commit or deployment was performed.
