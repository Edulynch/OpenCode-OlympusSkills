---
name: olympus-git-issue-create
description: Turn research, findings, or a work brief into GitHub issues. Use to file a standalone issue, group related work into an epic with native sub-issues, or publish several independent epics.
metadata:
  version: "1.0.0"
---

# Publish issues from findings

Use authenticated GitHub CLI (`gh`). Use the explicit repository or the GitHub repository for the current checkout; confirm the intended host and repository if ambiguous. Use the conversation and the sources the user identified. If there is no clear subject, ask what to file. If asked for a draft, show the proposed tree and issue bodies without writing to GitHub.

1. **Extract and group the work.** Separate distinct, actionable findings from ideas or unverified hypotheses. Write a standalone issue for an isolated item. For two or more tasks with a shared outcome or cause, write an epic with separately verifiable sub-issues. Create separate epics for separate outcomes with several tasks each. Keep isolated items standalone even when epics are also needed. Do not group findings solely because they share a component or label.
2. **Reconcile with existing issues.** Search the target repository, including recently closed matches where relevant, for the problem and existing parents, not only exact titles. Reuse a clearly matching open issue or epic instead of creating a duplicate. If a matching issue is closed, check whether this is a distinct recurrence before filing. Do not reopen, edit, or reparent existing issues without explicit authorization. When an existing match has a different parent, report the relationship conflict rather than creating a copy.
3. **Write useful issue bodies.** Use the repository's applicable templates, terminology, and existing labels or types. Give each epic a goal, scope, and success criteria; give each child or standalone issue its problem, evidence or reproduction steps, and testable acceptance criteria. Keep unverified claims marked as such. Include only information appropriate to publish in the target repository.
4. **Publish parents before children.** Use `gh issue create` with the verified repository. Use the `Epic` type when available; otherwise use an ordinary parent issue. Create each new child with `gh issue create --parent <number-or-url>` and verify its native parent. When an existing unparented issue may be linked and the user has authorized that change, use GitHub's native sub-issue API. The REST `sub_issue_id` is the issue's numeric database ID, not its `#number`; never use `replace_parent` here. A Markdown reference alone is not a native sub-issue link.
5. **Reconcile partial results.** Keep the URLs and confirmed links as each operation succeeds. If creation or linking fails or its result is unclear, re-read the issues and parent relationships before retrying: a child may already exist without its link. Do not create another copy to retry a failed link. Confirm the final tree and report newly created and reused issues, with anything still uncreated or unlinked and the reason.
