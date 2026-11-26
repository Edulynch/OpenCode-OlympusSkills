# Issue check skill maintenance

- Keep the English verification workflow in `.opencode/skills/olympus-git-issue-check/SKILL.md`, the optional shortcut in `commands/olympus.git.issue-check.md`, and examples in both root READMEs. This guide does not ship with the skill.
- Keep `metadata.version` in `SKILL.md` as the sole version source. Bump it with SemVer when changing distributed instructions, resources, or shortcut behavior.
- Recheck both denominators, accepted limitations versus verified passes, a missing or empty baseline, and stale CI versus uncommitted changes. Keep repository gates independent of the percentages.
