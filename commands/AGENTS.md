# Optional command sources

Keep command sources here, outside OpenCode's native `.opencode/commands/` discovery directory. A command should be a thin, optional prompt that invokes an existing workflow rather than duplicating its instructions.

- Name Olympus shortcuts `olympus.<topic>.md`. Refer to the exact skill ID and forward the request with `$ARGUMENTS`.
- Do not include shell commands or scripts in a shortcut.
- Do not override the selected model or agent.
- Do not copy this guide into `.opencode/commands/`; only copy a specifically chosen command file when a maintainer intentionally opts in.
- Update both root READMEs when an installed command's name or usage changes.
- A user-facing change to an optional command bumps the corresponding released skill's SemVer version in that skill's `SKILL.md`; do not add command-local versions. Maintenance-only documentation changes that do not ship with the skill do not require a version bump.
- Keep existing `olympus.<topic>.md` names, including `olympus.skill-author.md`; for future related commands, use `olympus.<group>.<action>.md`.
