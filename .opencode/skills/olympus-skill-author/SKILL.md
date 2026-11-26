---
name: olympus-skill-author
description: Create or revise a reusable Agent Skill for OpenCode V2. Use when asked to turn a workflow into a SKILL.md, improve an existing skill, or add an optional slash command for that skill.
metadata:
  version: "1.0.0"
---

# Author an Agent Skill

1. Identify the task, when the skill should be used, what it needs as input, and what result it should produce. Inspect the target project's instructions and any existing skill or command before choosing paths or editing. Ask only about missing details that materially change the workflow. If asked for a draft or plan, show the proposed files without writing them.
2. Choose a unique skill ID of 1–64 characters using lowercase ASCII letters, digits, and single hyphens between words. Use the project's conventions; for new skills in OpenCode Olympus Skills, use the `olympus-` prefix. Keep the ID stable when revising an existing skill unless the user requests a rename.
3. Write `.opencode/skills/<id>/SKILL.md`, or update the existing entry point. Use YAML frontmatter with `name` equal to the folder name and a nonempty `description` of at most 1,024 characters that says what the skill does and when to use it. For a new skill, set `metadata.version` to the quoted string `"1.0.0"`. Preserve an existing skill's version; when changing a released skill's distributed instructions, bundled resources, or optional command's user-facing behavior, bump it using SemVer: patch for backward-compatible corrections, minor for additions, and major for incompatibilities. Keep the version only in the skill's `SKILL.md` frontmatter, not in a command. Do not bump it for maintainer documentation that is not distributed with the skill. Put the workflow and expected result in the Markdown body. Document any real requirements and approval boundaries, and add only examples or supporting files the workflow needs. Keep those files beside the skill under appropriate subdirectories and link to them with relative paths.
4. Add a command only when the user wants an explicit shortcut. Follow the project's command layout: use `commands/olympus.<topic>.md` for an optional source in OpenCode Olympus Skills, or `.opencode/commands/<name>.md` for a project-local shortcut in a project without its own layout. Make it a thin prompt that requests loading the skill by its exact ID and passes `$ARGUMENTS`. Keep the current agent and model; leave out embedded shell blocks.
5. Check that the folder, `name`, and any command's skill ID agree, that local references exist, and that there are no filename collisions. Walk through a representative request and check that the workflow can deliver its stated result. Report the files and how to invoke the skill with `@<id>`; mention any actual runtime checks separately from the file checks.

Keep the skill usable in plain OpenCode V2 unless the request explicitly needs an Olympus-specific feature. Preserve unrelated files and existing project settings.
