# Contributing

Thanks for helping improve these independent OpenCode V2 skills.

## Keep changes focused

- Read the repository [maintainer guide](AGENTS.md) and the relevant skill guidance before changing a skill or shortcut.
- Skill entry points live in `.opencode/skills/<id>/SKILL.md`. Keep optional command sources in `commands/`; do not add them to `.opencode/commands/`.
- Keep repository content in English, except `README.ES.md`, which uses neutral Latin American Spanish natural in Mexico. Keep the English and Spanish quick starts and skill links aligned.
- Keep each skill's SemVer in `metadata.version` in its `SKILL.md`. Bump it when distributed instructions, resources, or shortcut behavior changes; maintainer-only documentation does not need a version bump.
- Keep shortcuts thin: load the matching skill, forward `$ARGUMENTS`, and do not embed shell blocks or override the selected agent or model.
- Do not include secrets or private information in issues, pull requests, examples, or test fixtures. Follow [SECURITY.md](SECURITY.md) for sensitive reports.

## Run the local checks

Python and the one pinned test dependency are sufficient:

```text
python -m pip install -r scripts/requirements-ci.txt
python -B scripts/test_validate_frontmatter.py
python -B scripts/validate_frontmatter.py
```

If Gitleaks 8.30.1 is available locally, scan all available Git history with redacted output:

```text
gitleaks git --redact=100 --no-banner --log-opts=--all .
```

CI runs the `Frontmatter` and `Gitleaks` checks on pull requests and pushes to `master`. Include the relevant local check results in your pull request; hosted checks still need to pass before merge.

## Pull requests

Explain the user-facing change and its scope, link related non-sensitive issues, and list the checks you ran. Update both READMEs when public install or shortcut guidance changes. Confirm relative links work and that only task-related files are included.
