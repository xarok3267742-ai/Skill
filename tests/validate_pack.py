#!/usr/bin/env python3
"""Static integrity and packaging checks for the Android skill pack."""

from __future__ import annotations

import re
import sys
from pathlib import Path


EXPECTED_SKILLS = {
    "android-product-pipeline",
    "android-app-developer",
    "mobile-ui-ux-designer",
    "android-qa-engineer",
    "google-play-policy-reviewer",
    "google-play-aso-expert",
    "android-release-manager",
}

FORBIDDEN_FILE_NAMES = {
    ".env",
    "keystore.properties",
    "credentials.json",
    "service-account.json",
}

FORBIDDEN_SUFFIXES = {".jks", ".keystore", ".p12", ".pfx"}

SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    "Google API key": re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b"),
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_frontmatter(text: str, path: Path, errors: list[str]) -> dict[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail(errors, f"{path}: missing YAML frontmatter")
        return {}

    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def validate_skill(root: Path, name: str, errors: list[str]) -> None:
    skill_dir = root / name
    skill_path = skill_dir / "SKILL.md"
    agent_path = skill_dir / "agents" / "openai.yaml"

    if not skill_path.is_file():
        fail(errors, f"{name}: missing SKILL.md")
        return
    if not agent_path.is_file():
        fail(errors, f"{name}: missing agents/openai.yaml")
        return

    skill_text = skill_path.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(skill_text, skill_path, errors)
    if frontmatter.get("name") != name:
        fail(errors, f"{name}: frontmatter name does not match folder")
    if not frontmatter.get("description"):
        fail(errors, f"{name}: missing frontmatter description")

    for relative_ref in re.findall(r"\]\((references/[^)#]+)(?:#[^)]+)?\)", skill_text):
        if not (skill_dir / relative_ref).is_file():
            fail(errors, f"{name}: missing linked reference {relative_ref}")

    agent_text = agent_path.read_text(encoding="utf-8")
    prompt_match = re.search(r'^\s*default_prompt:\s*"([^"]+)"\s*$', agent_text, re.MULTILINE)
    if not prompt_match:
        fail(errors, f"{name}: default_prompt must be a quoted string")
    elif f"${name}" not in prompt_match.group(1):
        fail(errors, f"{name}: default_prompt does not invoke ${name}")

    short_match = re.search(r'^\s*short_description:\s*"([^"]+)"\s*$', agent_text, re.MULTILINE)
    if not short_match:
        fail(errors, f"{name}: short_description must be a quoted string")
    elif not 25 <= len(short_match.group(1)) <= 64:
        fail(errors, f"{name}: short_description length must be 25-64 characters")

    if not re.search(r"^\s*allow_implicit_invocation:\s*true\s*$", agent_text, re.MULTILINE):
        fail(errors, f"{name}: implicit invocation is not explicitly enabled")


def validate_package(root: Path, errors: list[str]) -> None:
    present_skills = {
        path.name
        for path in root.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    }
    if present_skills != EXPECTED_SKILLS:
        missing = sorted(EXPECTED_SKILLS - present_skills)
        extra = sorted(present_skills - EXPECTED_SKILLS)
        fail(errors, f"skill set mismatch; missing={missing}, extra={extra}")

    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if relative.parts and relative.parts[0] == ".git":
            continue
        if ".git" in relative.parts:
            fail(errors, f"embedded Git metadata: {relative}")
        if path.is_file() and (
            path.name in FORBIDDEN_FILE_NAMES or path.suffix.lower() in FORBIDDEN_SUFFIXES
        ):
            fail(errors, f"forbidden secret-like file: {relative}")
        if not path.is_file() or path.suffix.lower() not in {".md", ".yaml", ".yml", ".py"}:
            continue
        text = path.read_text(encoding="utf-8")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                fail(errors, f"{relative}: contains {label} material")
        if relative != Path("tests/validate_pack.py") and re.search(r"\b(TODO|TBD|FIXME)\b", text):
            fail(errors, f"{relative}: contains unfinished placeholder")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    validate_package(root, errors)
    for skill_name in sorted(EXPECTED_SKILLS):
        validate_skill(root, skill_name, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(EXPECTED_SKILLS)} skills; metadata, links, and secret boundaries pass.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
