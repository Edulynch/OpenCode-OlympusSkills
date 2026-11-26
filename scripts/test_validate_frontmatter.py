#!/usr/bin/env python3
"""Focused in-memory tests for the frontmatter validator."""

import unittest
from pathlib import Path

from validate_frontmatter import parse_frontmatter, validate_command, validate_skill


SKILL_PATH = Path(".opencode/skills/olympus-example/SKILL.md")
COMMAND_PATH = Path("commands/olympus.example.md")
SKILL_IDS = {"olympus-example"}


def skill_text(
    *,
    name: str = "olympus-example",
    version: str = '"1.2.3"',
    description: str = "An example workflow.",
    body: str = "# Example\n\nA nonempty skill body.",
) -> str:
    return (
        "---\n"
        f"name: {name}\n"
        f"description: {description}\n"
        "metadata:\n"
        f"  version: {version}\n"
        "---\n"
        f"{body}\n"
    )


def command_text(
    *,
    description: str = "Run the example workflow",
    body: str = (
        "Load `olympus-example` with the skill tool and follow its workflow.\n"
        "$ARGUMENTS"
    ),
    extra_frontmatter: str = "",
) -> str:
    return (
        "---\n"
        f"description: {description}\n"
        f"{extra_frontmatter}"
        "---\n"
        f"{body}\n"
    )


class FrontmatterValidatorTests(unittest.TestCase):
    def test_accepts_valid_skill_and_command(self) -> None:
        self.assertEqual(validate_skill(SKILL_PATH, skill_text()), [])
        self.assertEqual(validate_command(COMMAND_PATH, command_text(), SKILL_IDS), [])

    def test_rejects_malformed_yaml_and_broken_delimiters(self) -> None:
        malformed = skill_text().replace(
            "description: An example workflow.", "description: ["
        )
        self.assertTrue(
            any("invalid YAML" in error for error in validate_skill(SKILL_PATH, malformed))
        )

        unclosed = "---\nname: olympus-example\ndescription: Example\n"
        _, _, errors = parse_frontmatter(unclosed, "skill.md")
        self.assertTrue(any("closing '---'" in error for error in errors))

        bad_opening = "name: olympus-example\n---\n# Body\n"
        _, _, errors = parse_frontmatter(bad_opening, "skill.md")
        self.assertTrue(any("start with '---'" in error for error in errors))

    def test_rejects_duplicate_yaml_keys(self) -> None:
        duplicate = (
            "---\n"
            "name: olympus-example\n"
            "description: first\n"
            "description: second\n"
            "metadata:\n"
            '  version: "1.0.0"\n'
            "---\n# Body\n"
        )
        self.assertTrue(
            any("duplicate key" in error for error in validate_skill(SKILL_PATH, duplicate))
        )

    def test_rejects_invalid_folder_name_and_version(self) -> None:
        mismatched = skill_text(name="olympus-other")
        self.assertTrue(
            any("name must match folder" in error for error in validate_skill(SKILL_PATH, mismatched))
        )

        invalid_version = skill_text(version='"01.2.3"')
        self.assertTrue(
            any("valid SemVer" in error for error in validate_skill(SKILL_PATH, invalid_version))
        )

        invalid_folder = Path(".opencode/skills/Bad-Name/SKILL.md")
        self.assertTrue(
            any("kebab-case ID" in error for error in validate_skill(invalid_folder, skill_text(name="Bad-Name")))
        )

        long_id = "olympus-" + "a" * 57
        long_path = Path(f".opencode/skills/{long_id}/SKILL.md")
        self.assertTrue(
            any("1-64 character" in error for error in validate_skill(long_path, skill_text(name=long_id)))
        )

    def test_rejects_description_over_limit_and_empty_skill_body(self) -> None:
        too_long = skill_text(description="x" * 1025)
        self.assertTrue(
            any("at most 1024" in error for error in validate_skill(SKILL_PATH, too_long))
        )

        empty_body = skill_text(body=" \n ")
        self.assertTrue(
            any("body must not be empty" in error for error in validate_skill(SKILL_PATH, empty_body))
        )

    def test_rejects_unknown_skill_and_missing_or_duplicate_arguments(self) -> None:
        unknown = command_text(body="Load `olympus-missing` with the skill tool.\n$ARGUMENTS")
        self.assertTrue(
            any("does not exist" in error for error in validate_command(COMMAND_PATH, unknown, SKILL_IDS))
        )

        missing_arguments = command_text(body="Load `olympus-example` with the skill tool.")
        self.assertTrue(
            any("exactly one literal $ARGUMENTS" in error for error in validate_command(COMMAND_PATH, missing_arguments, SKILL_IDS))
        )

        duplicate_arguments = command_text(body="Load `olympus-example` with the skill tool.\n$ARGUMENTS\n$ARGUMENTS")
        self.assertTrue(
            any("exactly one literal $ARGUMENTS" in error for error in validate_command(COMMAND_PATH, duplicate_arguments, SKILL_IDS))
        )

    def test_rejects_frontmatter_and_body_overrides_or_inline_shell(self) -> None:
        frontmatter_override = command_text(extra_frontmatter="model: example/model\n")
        self.assertTrue(
            any("must not override model" in error for error in validate_command(COMMAND_PATH, frontmatter_override, SKILL_IDS))
        )

        body_override = command_text(body="Set the agent to another-agent.\n$ARGUMENTS")
        self.assertTrue(
            any("overrides are not allowed" in error for error in validate_command(COMMAND_PATH, body_override, SKILL_IDS))
        )

        subagent = command_text(body="Spawn a subagent to do this.\n$ARGUMENTS")
        self.assertTrue(
            any("overrides are not allowed" in error for error in validate_command(COMMAND_PATH, subagent, SKILL_IDS))
        )

        shell_block = command_text(body="Run this: !`echo unsafe`\n$ARGUMENTS")
        self.assertTrue(
            any("shell blocks are not allowed" in error for error in validate_command(COMMAND_PATH, shell_block, SKILL_IDS))
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
