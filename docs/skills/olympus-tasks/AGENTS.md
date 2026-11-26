# Tasks skill maintenance

- Keep the English planning workflow in `.opencode/skills/olympus-tasks/SKILL.md` and its optional shortcut in `commands/olympus.tasks.md`. Keep public examples aligned in both root READMEs. This guide does not ship with the skill.
- Keep `metadata.version` in `SKILL.md` as the sole version source. Bump it with SemVer when changing distributed instructions, resources, or shortcut behavior.
- Check that the plan preserves scope, keeps priorities separate from execution order, names only real dependencies, and preserves task numbers on revision. The skill returns a list without executing it.
