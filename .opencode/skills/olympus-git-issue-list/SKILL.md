---
name: olympus-git-issue-list
description: List and prioritize all open GitHub issues in a repository. Use to review a backlog, identify blockers, or choose which issues to work on next.
metadata:
  version: "1.0.0"
---

# Prioritize open GitHub issues

Use authenticated GitHub CLI (`gh`). This workflow is read-only: do not change issues, labels, assignments, or project fields.

1. **Find the repository.** Use the user's explicit repository or the GitHub repository for the current checkout. Confirm the host and `owner/repo` before querying. If the checkout has a fork and the intended repository is ambiguous, ask which backlog to use.
2. **Fetch every open issue.** For GitHub.com, `gh api --paginate --slurp 'repos/OWNER/REPO/issues?state=open&per_page=100'` returns pages of issues and PRs; flatten the pages and exclude entries with a `pull_request` key. Use the verified host when querying an Enterprise instance. Do not rely on the default `gh issue list` limit. Read parent, sub-issue, dependency, and project priority data where available, using `gh issue list` or `gh issue view` as needed. Distinguish unavailable data from an empty backlog or a confirmed lack of blockers.
3. **Rank the issues.** Honor the repository's documented priority order and use its designated Projects field or priority labels where available. If priority is missing, suggest a rank based on demonstrated impact, urgency, and work it unblocks, in that order. Flag conflicting priority signals or missing evidence instead of inventing an official priority. Break remaining ties by oldest creation date, then issue number. Keep blocked and in-progress issues visible and distinguish them from actionable work.
4. **Present the backlog.** Give the repository, total open issues, and prioritized entries with issue link, priority source or suggested rank, a short reason, and any known blocker or work already in progress. Show open children under their parent, in priority order; retain each child's own priority and avoid listing it twice. When a parent is outside the listing, link to it as context. Report incomplete reads or unavailable priority and relationship data explicitly.
