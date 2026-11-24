# Interactive lesson instruction check — 2026-11-24

- Base: `b88cb10eae5c36decb822da1cfef85d75fd1f0a5`. Candidate: the guide and article changes in this commit.
- Method: same-session dry run from AGENTS and the rule map through the interactive, editorial, and relevant theme guides. Decisions below cover the changed instruction. This run provides no independent agent or usability-study evidence.

| Theme | Scenario and decision | Result |
| --- | --- | --- |
| FE | State-transition diagram: start stopped, press 起動, and watch the current state and arrow. Preserve optional prediction and the undefined-event explanation. CSMA/CD: reset keeps the selected scenario, so the label says 同じ条件で最初から. | Pass, guide and article source review |
| DS | DDL/DML: start with CREATE selected, then compare the column and row changes after INSERT. A zero-row UPDATE succeeds and a full reset restores CREATE. For sampling, start by comparing cluster and multistage draws. | Pass, guide and article source review |
| GK | Confusion matrix: keep the metric definitions before the demo. Guide the learner to change FP once and observe Precision; keep count-change and fixed-dataset comparisons distinct. Leave article unchanged for this dry run. | Pass, proposed first action fits the existing comparison |
| SG | SOC/CSIRT/JPCERT: keep the existing text-based decision table and role examples. The optional-interaction evaluation does not require JavaScript for this scenario. Leave article unchanged for this dry run. | Pass, static material fits the workplace decision |

The local instruction reference scan and four checker unit tests passed when the base rules and the updated guide were assembled from the repository. The PR reports browser outcomes separately. Android/iOS device, screen-reader, and post-deployment results remain open at authoring time.
