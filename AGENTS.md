# Repository guide

This repository hosts independent OpenCode skills and optional shortcuts for future distribution with OlympusAgents. Keep project-wide maintainer instructions here and folder-specific rules in the relevant `AGENTS.md`. Write repository content in English except `README.ES.md`, which uses neutral Latin American Spanish with wording natural in Mexico.

## Where information belongs

- Keep user-facing project purpose and status in `README.md` and its Spanish counterpart, `README.ES.md`. Keep facts aligned between them.
- Keep workflow instructions in the relevant skill's `SKILL.md`. Store skill-specific references, examples, templates, assets, and any necessary scripts beside that skill. Create supporting directories only when needed.
- Keep shared maintainer references in a root `references/` directory and maintenance scripts in a root `scripts/` directory if they become necessary.
- Keep optional command source in `commands/`, outside OpenCode's command-discovery directory. Copy only a deliberately selected command into `.opencode/commands/`; never copy this guide.
- Keep shared OpenCode layout rules in `.opencode/AGENTS.md`. Before changing a skill or its shortcut, read `docs/skills/<id>/AGENTS.md`. Keep these guides outside `.opencode/skills/` so installers do not copy them.

## Maintenance

Keep documentation factual about what exists, what is planned, and what has actually been tested. Verify the skill's entry point and any optional command independently.

## Skill versions

- Put each skill's SemVer string in its `SKILL.md` YAML frontmatter as `metadata.version`; this is the sole version source. New skills start at `"1.0.0"`.
- When a released skill's instructions, bundled resources, or optional command's user-facing behavior changes, bump that skill's version: patch for backward-compatible corrections, minor for additions, and major for incompatibilities.
- Do not bump a skill version for maintainer documentation that is not distributed with the skill.
