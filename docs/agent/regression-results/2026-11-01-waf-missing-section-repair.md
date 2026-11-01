# WAF missing-section repair

Base commit: `a12f8fa5fc8475760c6e3a4d790c7af68212bd4b`.

The user's mobile screenshot showed a truncation marker and plain-text table rows.
Git history confirms that PR #574 unintentionally replaced part of WAF's article
with `…1196 tokens truncated…`. The prior verification checked a different table
and summary; it missed the deleted sections and malformed misconceptions table.
The earlier report of normal WAF rendering was therefore too broad.

Restore the complete article from `02bb4ace`, retaining PR #574's actual newline
repairs and the 2026-11-01 modification date. This restores the Subject B, usage,
and misconceptions sections and all seven misconceptions rows. No new teaching
claims are introduced. Search of study Markdown found no other token-truncation
markers at the reviewed main commit.

The detector now flags numeric tool-output truncation markers and unconverted
pipe-table rows outside code examples. Eleven detector tests pass. The WAF
post-build regression now requires the three restored headings and seven
two-column misconception rows, in addition to its earlier table/list checks.
Instruction references and whitespace checks pass.

Check the newly uploaded Git blob hashes against the local files before creating
the PR to ensure the committed content is complete. Local Ruby is unavailable;
Jekyll rendering is checked by the PR workflow. No new browser visual check or
deployed repaired-page verification is claimed in this record.
