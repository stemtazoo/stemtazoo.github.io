# Rendered article text audit verification

- Base site commit: `476a76835703fa5cad06fbd1cf8818b653dec68f`.
- Change: standard-library HTML text candidate detector, Pages integration, PR preview build/check, and verification workflow documentation.
- Method: same-session code review, fixture execution, command-line scan of downloaded public HTML. No browser operation or visual-layout verification.

## Detector cases

`python -m unittest discover -s tests -p 'test_rendered_content.py' -v`
passes seven test methods, covering escaped newline sequences (including split inline
markup), metadata leakage, escaped HTML/doctype, unresolved Liquid, exclusion of
code and non-content regions, block boundaries, all four themes, fallback output
paths, and missing build output. Real line endings are not treated as escape text.

## Four-theme smoke check

The following deployed pages returned HTTP 200 and were downloaded as HTML for
the exact same CLI scan. Four pages scanned, zero review candidates. This is a
sample only, not an assertion that every published article is free of defects.

| Theme | Deployed URL | Result |
| --- | --- | --- |
| FE | https://stemtazoo.github.io/fe/cloud-deployment-models/ | No text candidates |
| GK | https://stemtazoo.github.io/gk/confusion-matrix/ | No text candidates |
| DS | https://stemtazoo.github.io/ds/sql-ddl-dml/ | No text candidates |
| SG | https://stemtazoo.github.io/sg/isms-security-policy-summary/ | No text candidates |

The deployed responses do not prove the server's source SHA. The commit above
identifies the reviewed source, not an independently verified deployed version.

## Instruction and deployment limits

The existing AGENTS → rule map → editing-workflow route applies equally to FE,
GK, DS, and SG. It now gives the build-output check command, candidate review,
normal-code exclusions, and separate reporting for browser verification. No
article-writing, source-selection, metadata, or navigation policy was changed.
This narrow verification change was checked with the four-theme fixture and
deployed HTML cases above; the unrelated editorial scenario matrix was not rerun.

The instruction-reference checker and its four tests pass. Local Jekyll execution
was unavailable because Ruby is not installed. The PR workflow builds with the
existing Jekyll Pages action and uploads a preview audit without deploying. The
main Pages workflow will run the audit before publishing after merge. Check
Actions for that result; neither this record nor a commit proves deployment.
