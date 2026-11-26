# OpenCode-local guidance

This file holds shared maintainer guidance for OpenCode-specific project files. Before editing a skill, read its guide at `docs/skills/<id>/AGENTS.md` relative to the repository root.

## Native discovery boundaries

- Put each skill in `skills/<id>/SKILL.md`. Use a unique `olympus-` prefixed, kebab-case ID, set the YAML `name` to that ID, and include a nonempty `description`.
- OpenCode discovers command Markdown from `.opencode/commands/`. Keep optional command source in the top-level `commands/` directory so it is not discovered until a maintainer intentionally copies the chosen file.
- Do not place unrelated documentation or command sources in native discovery directories. Markdown in discovery locations may be interpreted as a skill or command.
- Keep only distributed files in each skill folder: the Skills CLI copies the whole folder. Keep shared guidance here because OpenCode can discover loose Markdown directly under `.opencode/skills/` as a skill.

Copy only `SKILL.md` and any resources it uses when distributing a skill. Leave the maintainer `AGENTS.md` files in this repository.

Keep a skill's SemVer version in its `SKILL.md` YAML frontmatter as `metadata.version`; it is the sole version source, not a command-local field. Bump that version when a released skill's instructions, bundled resources, or an optional command's user-facing behavior changes.
