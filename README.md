# OpenCode Olympus Skills

Independent skills for OpenCode V2, with optional slash commands. They work without [OlympusAgents](https://github.com/Edulynch/OpenCode-OlympusAgents) and can later be offered as optional extras for the suite.

## Write an OpenCode goal

[`olympus-goal-writer`](.opencode/skills/olympus-goal-writer/SKILL.md) turns a prompt, issue, or conversation into a copy-ready `/goal` line of at most 4,000 characters. It tells the running agent to keep progressing on independent work when one step is blocked and pause for a person only when nothing else can advance. Paste the result yourself to start the goal.

```text
@olympus-goal-writer Turn what we agreed into an OpenCode goal.
/olympus.goal.write Turn the investigation above into an OpenCode goal.
```

The slash shortcut is optional and uses the same drafting workflow.

## Publish a pull request

[`olympus-git-pr-ready`](.opencode/skills/olympus-git-pr-ready/SKILL.md) creates or continues a GitHub PR, waits for CI, and tries to fix failures caused by the current task. It marks failures outside the task as blockers and leaves the PR open for you to merge unless you explicitly request a merge. It requires `git` and authenticated [GitHub CLI](https://cli.github.com/).

In OpenCode V2:

```text
@olympus-git-pr-ready Publish the current task and leave the PR ready for manual merge.
```

With the optional shortcut installed:

```text
/olympus.git.pr-ready Publish the current task and leave the PR ready for manual merge.
/olympus.git.pr-ready Publish the current task and merge the PR into develop once it passes all required checks and reviews.
```

## Work with GitHub issues

- [`olympus-git-issue-list`](.opencode/skills/olympus-git-issue-list/SKILL.md) ranks all open issues, explains their priority, and shows blockers and sub-issues without changing the backlog.
- [`olympus-git-issue-create`](.opencode/skills/olympus-git-issue-create/SKILL.md) turns findings into standalone issues or one or more epics with native sub-issues. Ask for a draft to see the issue tree before publishing.
- [`olympus-git-issue-work`](.opencode/skills/olympus-git-issue-work/SKILL.md) works on the issues you name or selects a batch by priority and relationship, implements and tests the changes, and leaves PRs for manual merge unless explicitly asked to merge.

These skills require authenticated GitHub CLI. Use `@` followed by the skill ID in a prompt, or install the optional shortcuts and use natural language:

```text
/olympus.git.issue-list
/olympus.git.issue-create Turn the research above into issues and group related findings into epics.
/olympus.git.issue-work Work on issues #42 and #57.
/olympus.git.issue-work Start with 3 issues.
```

## Verify task completion

[`olympus-git-issue-check`](.opencode/skills/olympus-git-issue-check/SKILL.md) checks the current changes against the issue or agreed task. It reports evidence-backed passes, gaps, and explicitly accepted exceptions, with separate percentages for original requirements and the scope that remains mandatory. It only reports results.

```text
@olympus-git-issue-check Verify the current changes against issue #42.
/olympus.git.issue-check Check what we agreed and show the accepted limitations.
```

## Author a skill

[`olympus-skill-author`](.opencode/skills/olympus-skill-author/SKILL.md) turns a workflow into a reusable Agent Skill or helps revise an existing skill. It can also write an optional slash command for the skill it creates.

Open this repository in OpenCode V2 and enter a prompt like:

```text
@olympus-skill-author Draft a skill that turns merged pull requests into release notes. Show the draft without writing files.
```

## Install in another project

1. Copy the chosen `SKILL.md` to `.opencode/skills/<id>/SKILL.md` in the destination project, keeping its skill folder name. OpenCode discovers it from that path.
2. To enable a shortcut, copy only the chosen command file to `.opencode/commands/` in the destination project, keeping its filename. It uses the same skill with your current agent.

| Skill file | Optional shortcut file |
| --- | --- |
| [`olympus-goal-writer/SKILL.md`](.opencode/skills/olympus-goal-writer/SKILL.md) | [`olympus.goal.write.md`](commands/olympus.goal.write.md) |
| [`olympus-git-issue-list/SKILL.md`](.opencode/skills/olympus-git-issue-list/SKILL.md) | [`olympus.git.issue-list.md`](commands/olympus.git.issue-list.md) |
| [`olympus-git-issue-create/SKILL.md`](.opencode/skills/olympus-git-issue-create/SKILL.md) | [`olympus.git.issue-create.md`](commands/olympus.git.issue-create.md) |
| [`olympus-git-issue-work/SKILL.md`](.opencode/skills/olympus-git-issue-work/SKILL.md) | [`olympus.git.issue-work.md`](commands/olympus.git.issue-work.md) |
| [`olympus-git-issue-check/SKILL.md`](.opencode/skills/olympus-git-issue-check/SKILL.md) | [`olympus.git.issue-check.md`](commands/olympus.git.issue-check.md) |
| [`olympus-git-pr-ready/SKILL.md`](.opencode/skills/olympus-git-pr-ready/SKILL.md) | [`olympus.git.pr-ready.md`](commands/olympus.git.pr-ready.md) |
| [`olympus-skill-author/SKILL.md`](.opencode/skills/olympus-skill-author/SKILL.md) | [`olympus.skill-author.md`](commands/olympus.skill-author.md) |

Copy only the selected files; the `AGENTS.md` guides are for maintaining this repository. To enable the shortcut here, use this repository as the destination in step 2.

## Documentation

Read this guide [in Spanish](README.ES.md). See [AGENTS.md](AGENTS.md) for repository conventions.

Official references: [OpenCode Skills](https://opencode.ai/docs/skills/), [OpenCode Commands](https://opencode.ai/docs/commands/), and the [Agent Skills specification](https://agentskills.io/specification).
