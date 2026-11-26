# Issue list skill maintenance

- Keep the read-only listing, ranking rules, and output format in English in `SKILL.md`. Keep the optional shortcut in `commands/olympus.git.issue-list.md` and its examples in both root READMEs.
- Keep `metadata.version` in `SKILL.md` as the sole version. Bump it with SemVer in the same change whenever distributed instructions, resources, or shortcut behavior change.
- When changing ranking, keep the standalone selection rules in `olympus-git-issue-work` consistent. Check pagination, PR exclusion, explicit and inferred priority, and blocked children.
