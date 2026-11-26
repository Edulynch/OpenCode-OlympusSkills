# Goal writer maintenance

- Keep the English workflow in `.opencode/skills/olympus-goal-writer/SKILL.md`, the optional shortcut in `commands/olympus.goal.write.md`, and examples in both root READMEs. This guide does not ship with the skill.
- Keep `metadata.version` in `SKILL.md` as the sole version source. Bump it with SemVer when changing distributed instructions, resources, or shortcut behavior.
- Preserve drafting without activation, the 4,000 UTF-16 code unit limit for the complete line, and progress on independent work despite partial blockers. Check the exact limit, over-limit and non-BMP text, a partial blocker with remaining work, and a blocker that genuinely requires the user.
