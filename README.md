<div align="center">

# ⚡ OpenCode Olympus Skills

**Independent, installable workflows for OpenCode V2 that work without [OlympusAgents](https://github.com/Edulynch/OpenCode-OlympusAgents).**

🌐 [English](README.md) · [Español](README.ES.md)

[![CI](https://github.com/Edulynch/OpenCode-OlympusSkills/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/Edulynch/OpenCode-OlympusSkills/actions/workflows/ci.yml)
[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![OpenCode V2](https://img.shields.io/badge/OpenCode-V2-5964f2?style=flat-square)](https://opencode.ai/docs/)

**[⚡ Install](#install) · [🎯 Try](#try) · [🧩 Skills](#skills) · [⌨️ Shortcuts](#shortcuts) · [📚 Guides](#guides)**

</div>

## 🚀 Start here

<a id="install"></a>
### ⚡ Install

Install the goal-writing skill:

```text
npx skills add Edulynch/OpenCode-OlympusSkills --skill olympus-goal-writer --agent opencode
```

To install all skills in OpenCode from the target project's root:

```text
npx skills add Edulynch/OpenCode-OlympusSkills --skill "*" --agent opencode
```

Olympus slash shortcuts install separately; see [Shortcuts](#shortcuts).

<a id="try"></a>
### 🎯 Try

Then ask OpenCode:

```text
@olympus-goal-writer Turn what we agreed into an OpenCode goal.
```

It drafts a copy-ready `/goal` line of at most 4,000 UTF-16 code units; it does not start the goal. Paste the result yourself.

## 🧭 Choose a workflow

Use `@` plus a skill ID. GitHub workflows require authenticated [`gh`](https://cli.github.com/); Git publishing also requires `git`.

<a id="skills"></a>
### 🧩 Skills

| Skill | What it does | Optional shortcut source |
| --- | --- | --- |
| [`olympus-goal-writer`](.opencode/skills/olympus-goal-writer/SKILL.md) | Drafts a `/goal` of at most 4,000 UTF-16 code units, keeps independent work moving when blocked, and never runs it. | [`olympus.goal.write.md`](commands/olympus.goal.write.md) |
| [`olympus-git-issue-list`](.opencode/skills/olympus-git-issue-list/SKILL.md) | Ranks open issues and shows priorities, blockers, and sub-issues; read-only. | [`olympus.git.issue-list.md`](commands/olympus.git.issue-list.md) |
| [`olympus-git-issue-create`](.opencode/skills/olympus-git-issue-create/SKILL.md) | Turns findings into standalone issues or native epic/sub-issue trees; can show a draft first. | [`olympus.git.issue-create.md`](commands/olympus.git.issue-create.md) |
| [`olympus-git-issue-work`](.opencode/skills/olympus-git-issue-work/SKILL.md) | Works named issues or selects a prioritized batch, implements and tests, and leaves PRs open by default. | [`olympus.git.issue-work.md`](commands/olympus.git.issue-work.md) |
| [`olympus-git-issue-check`](.opencode/skills/olympus-git-issue-check/SKILL.md) | Reports evidence-based passes, gaps, accepted exceptions, and original/current completion percentages; read-only. | [`olympus.git.issue-check.md`](commands/olympus.git.issue-check.md) |
| [`olympus-git-pr-ready`](.opencode/skills/olympus-git-pr-ready/SKILL.md) | Opens or continues a PR, waits for CI, and fixes task-caused failures; leaves it open unless asked to merge. | [`olympus.git.pr-ready.md`](commands/olympus.git.pr-ready.md) |
| [`olympus-skill-author`](.opencode/skills/olympus-skill-author/SKILL.md) | Creates or revises an Agent Skill and can draft its optional shortcut. | [`olympus.skill-author.md`](commands/olympus.skill-author.md) |

<a id="shortcuts"></a>
### ⌨️ Shortcuts

The Skills CLI installs the selected skill. Shortcuts are optional source files: copy only a chosen `.md` from [`commands/`](commands/) to the destination project's `.opencode/commands/`. Each shortcut loads its matching skill and forwards `$ARGUMENTS`; it is not installed automatically.

## 🧪 Check locally

```text
python -m pip install -r scripts/requirements-ci.txt
python -B scripts/test_validate_frontmatter.py
python -B scripts/validate_frontmatter.py
```

The GitHub Actions workflow checks frontmatter and scans full available Git history with redacted Gitleaks output.

## 🤝 Help and policies

- [Contributing](CONTRIBUTING.md) · [Security reporting](SECURITY.md)
- [Open a non-sensitive issue](https://github.com/Edulynch/OpenCode-OlympusSkills/issues) · [MIT License](LICENSE)

<a id="guides"></a>
### 📚 Guides

- [OpenCode Skills](https://opencode.ai/docs/skills/) · [OpenCode Commands](https://opencode.ai/docs/commands/) · [Agent Skills specification](https://agentskills.io/specification)
