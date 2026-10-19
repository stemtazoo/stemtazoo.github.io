# Audit migration routing review — 2026-10-19

Base site commit: `38d031ceb36bc7b4e401d7be5eee705c577f14b5`. Updated version: this migration PR.

Method: same-session dry walkthrough of the full instruction-regression matrix, from AGENTS.md and the rule map. This is evidence about routing and the preservation of boundaries, not an independent end-to-end article-writing test. No test articles were published, no current official-source claims were newly verified, and no article or navigation was changed.

| Scenario | Decision / route after migration | Result for changed routing |
|---|---|---|
| FE-1 | Read editorial rules, consult relevant audit decisions if present, search all themes; the existing binary-search role must be compared before creating another page. | pass |
| FE-2 | FE content/template/front matter/tags and interactive-learning rules remain local; an audit record does not replace standalone examples or Subject B requirements. | pass |
| FE-3 | Copyright follows local FE and source guides; no Subject B section is authorized merely by an audit finding. | pass |
| FE-4 | Necessity-only request stays at new/update/no-change analysis after four-theme search; missing external history does not block that search. | pass |
| FE-5 | Local stubs route to the migrated FE audit and full-audit guides; special-page classification and report-only boundary remain in the moved text. | pass |
| SG-1 | SG content and shared source rules remain local; audit history does not authorize prev/next edits. | pass |
| SG-2 | Explicit series work still follows local series/navigation rules and verifies actual neighbors. | pass |
| SG-3 | Summary-only work still permits body learning maps, without automatically editing individual-article navigation. | pass |
| DS-1 | DS writing bundle and visual-aid route remain local; migrating flat-Markdown reporting changes no statistical explanation requirement. | pass |
| GK-1 | GK content and shared primary-source guide remain local; named-model provenance and broad concepts keep their separate source decisions. | pass |
| GK-2 | GK index route still points to the actual Index.md; migration does not change grouping or deployment verification. | pass |
| SHARED-1 | Source freshness and metadata rules remain local; low traffic is not a merge rule; audit history supplements current learning-purpose comparison. | pass |

Evidence inspected: AGENTS.md; docs/agent/README.md; editorial-rules.md; instruction-regression.md; FE/SG/DS/GK content-rule routing; SG navigation authorization; editing-workflow.md; the migrated FE audit/full-audit procedures. The added rule is a ledger lookup plus explicit fallback; it does not change the underlying writing or navigation policies.

Mechanical checks: instruction reference checker and its four regression tests pass. Dedicated FE/DS audit tests and report parity run in study-site-audit. Pages/Actions result is checked on the PR separately; a local commit is not a deployment. Remaining limit: fresh-session behavioral evaluation of actual future authoring tasks.
