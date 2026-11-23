# Article image caption review

Base commit `caa06c5a581487a4ce17ba171186ce3a1194ee83`. Updated revision is the commit containing this record and the caption changes.

Started from `AGENTS.md` and the rule map. Consulted the article image, editorial, AI-search, editing and instruction-regression guides, the four themes' content, template, front matter and tag guides, and the SG example-question guide.

## Four-theme scenario

Same-session review of existing Markdown and image markup. The scenario was to choose whether to keep, shorten, or omit a caption when adding an image next to an established explanation.

| Theme | Evidence | Decision | Result |
| --- | --- | --- | --- |
| FE | The Stack caption from PR #874 asks readers to track the top element after each operation. The decimal conversion and UTF-8 articles already show the calculation steps and results. The Pareto article explains the chart elements and presents the 80% example. | Keep the revised Stack caption and omit the two conversion captions. Point to where the Pareto line reaches 80%. | Pass |
| GK | Teacher Forcing defines the two sources of next inputs in the text and comparison table. The diagram uses arrows for those inputs. | Keep a short prompt to compare the arrows' starting points. | Pass |
| DS | Primary Data defines direct collection immediately below its figure. The alt text identifies its three illustrated methods. | Omit the repeated definition. | Pass |
| SG | Message Digest explains deterministic hashes and the before/after comparison in the following section. The image depicts the SHA-256 flow. | Omit the generic integrity explanation under the figure. | Pass |

A disk scheduling figure provides a counterexample for deletion. Its caption identifies the LOOK-style turnaround condition and directs readers to the exact processing order in the following text. The condition matters when distinguishing it from strict SCAN.

## Verification

- Instruction reference check and existing instruction and rendered-content audit unit tests passed.
- For all six changes, parsed front matter and the source figure markup. Verified that the caption and applicable modification date were the only article changes. Image sources, dimensions, alt text and the remaining article text matched the base.
- Local Ruby was unavailable. Jekyll output and the updated pages in a browser are pending deployment verification.
