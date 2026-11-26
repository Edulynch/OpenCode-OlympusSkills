#!/usr/bin/env python3
"""Validate frontmatter and command references in this repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml
from yaml.constructor import ConstructorError
from yaml.nodes import MappingNode


SKILL_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_RE = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-((?:0|[1-9]\d*|[0-9A-Za-z-]*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:\.(?:0|[1-9]\d*|[0-9A-Za-z-]*[A-Za-z-][0-9A-Za-z-]*))*))?"
    r"(?:\+([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?$"
)
SKILL_REFERENCE_RE = re.compile(
    r"\bLoad\s+`([a-z0-9]+(?:-[a-z0-9]+)*)`\s+with the skill tool\b"
)
SHELL_BLOCK_RE = re.compile(r"!\s*`")
OVERRIDE_LINE_RE = re.compile(
    r"(?im)^\s*(?:(?:please\s+)?(?:set|switch|change|override|select|choose|route|assign)"
    r"\s+(?:(?:the|current|selected|default|new|named)\s+)*(?:agent|model|subagents?)\b"
    r"|(?:agent|model|subagents?)\s*[:=])"
)
SUBAGENT_DIRECTIVE_RE = re.compile(
    r"(?im)^\s*(?:use|run|invoke|launch|spawn|call|delegate(?:\s+to)?)"
    r"\s+(?:a\s+|the\s+|another\s+)?subagents?\b"
)
OVERRIDE_FIELDS = {"agent", "model", "subagent", "subagents"}


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects repeated keys before merge expansion."""

    def construct_mapping(self, node: MappingNode, deep: bool = False) -> dict[Any, Any]:
        if isinstance(node, MappingNode):
            seen: set[Any] = set()
            for key_node, _ in node.value:
                key = self.construct_object(key_node, deep=deep)
                try:
                    duplicate = key in seen
                except TypeError:
                    duplicate = False
                if duplicate:
                    raise ConstructorError(
                        "while constructing a mapping",
                        node.start_mark,
                        "found duplicate key",
                        key_node.start_mark,
                    )
                try:
                    seen.add(key)
                except TypeError:
                    pass
        return super().construct_mapping(node, deep=deep)


def parse_frontmatter(
    text: str, label: str
) -> tuple[dict[str, Any] | None, str, list[str]]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return None, "", [f"{label}: frontmatter must start with '---'"]

    closing = next((index for index, line in enumerate(lines[1:], 1) if line == "---"), None)
    if closing is None:
        return None, "", [f"{label}: frontmatter is missing its closing '---'"]

    body = "\n".join(lines[closing + 1 :])
    source = "\n".join(lines[1:closing])
    try:
        data = yaml.load(source, Loader=UniqueKeyLoader)
    except yaml.YAMLError as error:
        problem = getattr(error, "problem", None) or error.__class__.__name__
        mark = getattr(error, "problem_mark", None)
        location = f" line {mark.line + 1}" if mark is not None else ""
        return None, body, [f"{label}: invalid YAML frontmatter{location}: {problem}"]

    if not isinstance(data, dict):
        return None, body, [f"{label}: frontmatter must be a YAML mapping"]
    return data, body, []


def validate_skill(path: Path, text: str) -> list[str]:
    label = path.as_posix()
    errors: list[str] = []
    folder = path.parent.name
    if (
        len(folder) > 64
        or not SKILL_ID_RE.fullmatch(folder)
        or not folder.startswith("olympus-")
    ):
        errors.append(
            f"{label}: skill folder must be a 1-64 character olympus-prefixed kebab-case ID"
        )

    data, body, parse_errors = parse_frontmatter(text, label)
    errors.extend(parse_errors)
    if not body.strip():
        errors.append(f"{label}: Markdown body must not be empty")
    if data is None:
        return errors

    name = data.get("name")
    if not isinstance(name, str) or name != folder:
        errors.append(f"{label}: frontmatter name must match folder {folder!r}")

    description = data.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append(f"{label}: description must be a nonempty string")
    elif len(description) > 1024:
        errors.append(f"{label}: description must be at most 1024 characters")

    metadata = data.get("metadata")
    if not isinstance(metadata, dict):
        errors.append(f"{label}: metadata must be a mapping containing a SemVer version")
    else:
        version = metadata.get("version")
        if not isinstance(version, str) or not SEMVER_RE.fullmatch(version):
            errors.append(f"{label}: metadata.version must be a valid SemVer string")
    return errors


def validate_command(path: Path, text: str, skill_ids: set[str]) -> list[str]:
    label = path.as_posix()
    errors: list[str] = []
    data, body, parse_errors = parse_frontmatter(text, label)
    errors.extend(parse_errors)
    if not body.strip():
        errors.append(f"{label}: Markdown body must not be empty")
    if text.count("$ARGUMENTS") != 1:
        errors.append(f"{label}: command must contain exactly one literal $ARGUMENTS")
    if SHELL_BLOCK_RE.search(body):
        errors.append(f"{label}: embedded OpenCode !` shell blocks are not allowed")
    if data is None:
        return errors

    description = data.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append(f"{label}: description must be a nonempty string")

    overridden = sorted(OVERRIDE_FIELDS.intersection(key.lower() for key in data if isinstance(key, str)))
    if overridden:
        errors.append(f"{label}: command frontmatter must not override {', '.join(overridden)}")
    if OVERRIDE_LINE_RE.search(body) or SUBAGENT_DIRECTIVE_RE.search(body):
        errors.append(f"{label}: agent, model, and subagent overrides are not allowed")

    references = SKILL_REFERENCE_RE.findall(body)
    if len(references) != 1:
        errors.append(f"{label}: body must contain exactly one unambiguous skill load reference")
    elif references[0] not in skill_ids:
        errors.append(f"{label}: referenced skill {references[0]!r} does not exist")
    return errors


def _read_text(path: Path) -> tuple[str | None, str | None]:
    try:
        return path.read_text(encoding="utf-8"), None
    except (OSError, UnicodeError) as error:
        return None, f"{path.as_posix()}: cannot read UTF-8 file ({error.__class__.__name__})"


def validate_repository(root: Path) -> tuple[list[str], int, int]:
    errors: list[str] = []
    skill_paths = sorted((root / ".opencode" / "skills").glob("*/SKILL.md"))
    if not skill_paths:
        errors.append(".opencode/skills: no skill entry points found")
    skill_ids = {path.parent.name for path in skill_paths}

    for path in skill_paths:
        text, error = _read_text(path)
        if error:
            errors.append(error)
        elif text is not None:
            errors.extend(validate_skill(path.relative_to(root), text))

    command_paths = sorted(
        path
        for path in (root / "commands").glob("*.md")
        if path.name != "AGENTS.md"
    )
    if not command_paths:
        errors.append("commands: no command sources found")

    for path in command_paths:
        text, error = _read_text(path)
        if error:
            errors.append(error)
        elif text is not None:
            errors.extend(
                validate_command(path.relative_to(root), text, skill_ids)
            )
    return errors, len(skill_paths), len(command_paths)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors, skill_count, command_count = validate_repository(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Validated {skill_count} skill(s) and {command_count} command(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
