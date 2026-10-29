# Lightweight interaction verification — 2026-10-30

- Base commit: `a810c01c7993dd4cb3fb050fd863880cd9c14c5d`.
- Updated revision: the PR revision containing this record and the adjacent instruction change; no self-referential commit hash is asserted.
- Scope: make the existing interaction verification checklist executable and its results reviewable. No article, asset, workflow, navigation, source-selection, or automation changes.
- Method: same-session manual instruction compatibility dry run across the full scenario matrix below. These are decisions about the instructions, not completed article audits, browser tests, or independent agent-behavior trials.
- Evidence read: `AGENTS.md`; `docs/agent/README.md`, `editorial-rules.md`, `interactive-learning-rules.md`, `instruction-regression.md`, `editing-workflow.md`, `metadata-rules.md`, `primary-source-audit-rules.md`, `sg-navigation-rules.md`, `sg-series-summary-rules.md`, `sg-example-question-rules.md`, `gk-index-rules.md`, and the FE audit routing stubs. Theme-specific content/template/front-matter/tag provisions were inspected for compatibility. Repository search covered all four article directories; representative bodies read included FE binary search, the DS variance legacy helper, and GK Transformer. No current external-source verification is claimed.

## Scenario compatibility decisions

Each result below is **Pass for instruction compatibility only**. The scenario's actual publication, audit, or rendered-site workflow was not executed.

| Scenario | Decision / evidence |
| --- | --- |
| FE-1 | Four-theme search still precedes creation. Existing `pages/fe/binary-search.md` explains halving sorted data and already embeds a visualizer; the new paragraph supplies operation checks if that aid is edited, not a reason for a duplicate article. |
| FE-2 | Keep standalone trace inputs, index conventions, concrete Subject B use, classification, footer and FE-only related links. Representative next/reset/last-step checks can verify a trace without changing those article requirements or adding prev/next. |
| FE-3 | Copyright remains a Subject A distinction unless a concrete Subject B solving skill exists. An operation-check rule does not require an interaction or a Subject B section. |
| FE-4 | Necessity analysis remains a proposal-only task; do not implement an article or demo just to satisfy verification. |
| FE-5 | Audit routing still points to study-site-audit. Classify a redirect helper before normal-article checks; the added rule does not authorize audit repairs. The DS legacy variance helper provides a concrete example of this distinct page role. |
| SG-1 | A definition/source correction preserves SG structure and navigation authorization. If no aid changes, no interaction report is needed; an adapted SG aid uses SG article rules. |
| SG-2 | Explicit series work still permits choosing verified individual-article neighbors and updating the map. Interaction verification grants no additional navigation scope. |
| SG-3 | A summary-only request still produces body guidance without unsolicited prev/next. No quiz or interactive block is forced. |
| DS-1 | Variance explanation remains intuition-first with the denominator distinction and valid date/footer/category handling. The legacy variance URL points to `population-sample-unbiased-variance.md`; do not treat the helper as the normal article. If an aid is changed, derive expected values from the explanation and report actual operation evidence. |
| GK-1 | `pages/gk/transformer.md` retains its GK grouping and conceptual distinctions. Named-model original-source evaluation remains separate from generic-concept handling; the new report does not require either a paper section or an aid. |
| GK-2 | `pages/gk/Index.md` remains the source of hierarchy. The existing index guide still requires sibling/direct-parent and deployed visibility checks; the new paragraph does not replace them with a single demo operation. |
| SHARED-1 | Supersession checks, specific descriptions, and learning-purpose comparison remain owned by their existing guides. Code inspection, browser operation and deployment checks are reported separately; a passing build is not runtime evidence. |

## Focused verification decisions

- FE trace: choose a next-step expectation, then reset and first/last states; verify the displayed state and explanation together.
- GK metrics: with positive TP fixed, raising FP from 2 to 12 must lower Precision. This is a prospective test expectation, not a claim that the browser test ran.
- DS parameter aid: select a known example from the explanation and compare numbers and interpretation; do not invent a measured result.
- SG adapted aid: preserve SG judgment criteria and article restrictions; no new requirement to add an aid.
- CSS-only diagram: inspect the intended relationship at desktop and narrow widths; no fictitious reset or boundary controls.
- Browser unavailable: continue useful implementation, mark code review only, and provide the concrete follow-up operation. Useful teaching aids are not removed solely for unavailable browser execution.
- Shared assets: include an existing consumer in addition to the changed article. Existing update audits remain follow-up safeguards; automation is optional and targeted to demonstrated need.

## Mechanical checks and limits

- `python scripts/check_agent_instructions.py`: passed.
- `python -m unittest discover -s tests -p 'test_agent_instructions.py'`: passed, 4 tests.
- `git diff --check`: passed.
- Article/CSS/JavaScript behavior was not changed or browser-tested in this documentation-only PR. No Jekyll build or deployment was performed locally. Check the PR's Actions status separately; no deployment success is claimed.
