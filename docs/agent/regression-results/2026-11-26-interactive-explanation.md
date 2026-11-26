# Interactive explanation instruction check — 2026-11-26

- Base: `fc417fc423f11302774b1dc3250dda8805685be4`. Candidate: the two additions to the existing interaction presentation guidance in this commit.
- Method: targeted same-session source review from AGENTS and the rule map through the shared interactive guide and all four theme content guides. This is a narrow presentation refinement; routing, article-creation criteria, and theme policies are unchanged. The review is not an independent agent-behavior test.

| Theme | Scenario and decision | Evidence |
| --- | --- | --- |
| FE | FE-2 (trace readability): keep the Hamming example's bit position, received bits, intermediate parity counts and next action visible. | Existing article source; Android feedback and PR #904. |
| DS | DS-1 (interpretation of changing values): for a code-based interaction, show the relevant code change together with its result. LEFT JOIN should show AND/WHERE and the same sample's matching rows. | Existing article source; Android feedback and PR #901. |
| GK | For the fixed random-split example, explain why pressing the action leaves month assignments unchanged. | Existing time-series cross-validation source; Android feedback and PR #903. |
| SG | For existing access-management guidance, the decision table and role examples are sufficient; no interactive aid or additional explanatory UI is needed. | Existing access-control article source; optional interaction rule preserved. |

No article, UI asset, or test scenario changes are needed for these decisions. The instruction-check workflow provides mechanical regression results; see the PR for the actual status.
