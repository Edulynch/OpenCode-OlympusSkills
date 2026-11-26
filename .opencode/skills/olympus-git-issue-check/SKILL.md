---
name: olympus-git-issue-check
description: Verify current changes against a GitHub issue or the agreed task. Use to report evidence-backed PASS results, gaps, explicitly accepted exceptions, and completion percentages for the original and current scope.
metadata:
  version: "1.0.0"
---

# Verify issue and task completion

Use `git` to inspect the target checkout and authenticated GitHub CLI (`gh`) when issue or PR details are needed. Review changes and run permitted checks. Do not fix files, change Git history, publish, or modify issues or PRs as part of verification.

## Establish the scope and revision

1. Resolve the target repository and issue or PR from the user's reference, the current task, or a clearly linked PR. Read the issue's requirements and acceptance criteria, relevant scope decisions, and applicable project instructions. If there is no linked issue, use the original requirements and decisions agreed in the conversation. Do not infer the scope from the diff alone. Report inaccessible or ambiguous requirements rather than guessing or issuing a definitive score from an incomplete baseline.
2. Identify the changes that belong to the task: the relevant base and head revisions and any in-scope staged, unstaged, or untracked changes. State exactly what was reviewed. Leave unrelated work out; if it makes a check inconclusive, explain why.
3. List distinct, independently verifiable criteria. Deduplicate repeated requests and keep multiple tests for the same criterion as evidence, not extra points. Record which criteria originally applied, which are still mandatory, and any criteria added by a later scope agreement. An originally applicable criterion stays in the original baseline if it was later waived, limited, or excluded. Only treat a scope exception as accepted when the user or an authorized decision-maker explicitly agreed to it; cite the decision and its conditions. Silence or an implementer's assumption is not approval.

## Verify and classify

Inspect the diff and relevant behavior, run the smallest checks that cover the criteria, and reuse earlier evidence only when it covers the same relevant code and conditions. Report the check, observed result, and applicable revision. CI from a PR head does not verify additional local changes. Check required repository gates separately, including any pending CI or review. Record missing or unavailable evidence.

| Status | Use when |
| --- | --- |
| `PASS` | The full criterion is satisfied and supported by evidence. |
| `FAIL` | Evidence shows the criterion is not met. |
| `PARTIAL` | Evidence shows some of the criterion is met; specify the gap. |
| `UNVERIFIED` | There is insufficient evidence to decide. |
| `BLOCKED` | A concrete obstacle prevents completion or verification; name it. |
| `ACCEPTED LIMITATION` | An authorized decision accepts a specific remaining gap; describe the actual result and link or quote the decision. |
| `EXCLUDED BY AGREEMENT` | An authorized decision removes or defers the criterion for this task; cite it. |
| `N/A` | A conditional criterion does not apply; explain why. Do not use this for something that was merely waived or not tested. |

If a decision accepts a narrower outcome, record the original gap as `ACCEPTED LIMITATION` and verify the narrower obligation separately if it still has to be delivered. Do not use technical `PASS` for an exception, and do not treat acceptance as overriding a required repository gate.

## Report completion

Give the target issue or task, the reviewed revision or working-tree scope, and a table with each criterion, status, and evidence, gap, or approval reference. Use equal weight per criterion and show both percentages with the counts:

- **Original completion:** `100 × PASS among originally applicable criteria / originally applicable criteria`. The denominator includes subsequently accepted limitations and exclusions; later additions do not count here.
- **Agreed-scope completion:** `100 × PASS among currently mandatory applicable criteria / currently mandatory applicable criteria`. Exclude only approved exceptions and proven non-applicability; include later agreed obligations still required. Failed, partial, blocked, and unverified mandatory criteria remain in the denominator.

For example, seven passes, one failure, one accepted limitation, and one agreed exclusion give **70% (7/10)** original and **87.5% (7/8)** agreed-scope completion. A zero, unknown, or unreliable denominator is `N/A`, not `100%`; report what is known.

End with **Complete**, **Complete with accepted exceptions**, or **Pending**, and list any remaining required gate or decision separately. Use **Pending** if the scope is unresolved or a mandatory criterion or applicable completion gate is unmet or unverified, regardless of the score.
