# Skill authoring guide

This file is maintainer guidance for `olympus-skill-author`. The runtime entry point is `.opencode/skills/olympus-skill-author/SKILL.md` relative to the repository root.

## When authoring the skill

- Write the actual skill instructions in English in `SKILL.md`.
- Use YAML frontmatter whose `name` is exactly `olympus-skill-author` to match this folder, and include a nonempty `description` that clearly states when the skill is useful.
- Keep the instructions focused on the requested authoring workflow. Do not put maintainer policy, repository history, or unrelated setup material into the user-facing skill.
- Add only supporting resources the instructions need: detailed references or examples under `references/`, reusable templates under `assets/`, and any necessary scripts under `scripts/`. Link to them from `SKILL.md` with relative paths.
- Keep maintainer-only notes here or in the appropriate repository guide; do not present them as runtime instructions or user-facing capabilities.
- New skills start with `metadata.version: "1.0.0"` in `SKILL.md` frontmatter. For an already released skill, preserve its version unless a change to distributed instructions, bundled resources, or optional-command user-facing behavior requires a SemVer bump: patch for backward-compatible corrections, minor for additions, and major for incompatibilities. `SKILL.md` is the sole version source; do not add command-local versions or bump for maintainer docs not distributed with the skill.

Keep the exact skill ID in sync with the optional command in `commands/olympus.skill-author.md` and the examples in both root READMEs.
