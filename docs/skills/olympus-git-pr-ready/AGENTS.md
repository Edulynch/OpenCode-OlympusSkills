# PR readiness skill maintenance

- Keep the English workflow and its safety boundaries in `SKILL.md`. Keep the optional prompt in `commands/olympus.git.pr-ready.md` and document usage in both root READMEs.
- Keep versioning in the `SKILL.md` YAML frontmatter as `metadata.version`. New skills start at `"1.0.0"`. On changes to distributed instructions, bundled resources, or shortcut behavior, bump the version in the same change using SemVer. This maintainer guide does not ship with the skill.
- Recheck the new-PR, existing-PR repair, out-of-scope blocker, manual handoff, and explicit merge paths when changing the workflow. Use an isolated test repository for live verification.
