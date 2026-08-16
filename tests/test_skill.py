from pathlib import Path
import re

ROOT = Path(__file__).parents[1]
SKILL = ROOT / "SKILL.md"
README = ROOT / "README.md"
README_ZH = ROOT / "README.zh-CN.md"
SOURCES = ROOT / "SOURCES.md"
LICENSE = ROOT / "LICENSE"


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_required_files_exist():
    for path in (SKILL, README, README_ZH, SOURCES, LICENSE):
        assert path.exists(), path


def test_frontmatter_is_valid_and_compact():
    content = text(SKILL)
    assert content.startswith("---\n")
    match = re.match(r"---\n(.*?)\n---\n", content, re.S)
    assert match
    frontmatter = match.group(1)
    values = dict(
        line.split(":", 1) for line in frontmatter.splitlines()
        if ":" in line and not line.startswith(" ")
    )
    assert values["name"].strip() == "adaptive-taskcraft"
    description = values["description"].strip().strip('"')
    assert len(description) <= 60
    assert description.endswith(".")
    for key in ("version", "author", "license", "platforms"):
        assert key in values


def test_skill_covers_full_capability_matrix():
    content = text(SKILL).lower()
    required = {
        "natural response": ["natural", "answer"],
        "planning": ["plan", "acceptance"],
        "ci": ["ci", "log"],
        "frontend": ["frontend", "visual"],
        "web testing": ["web", "browser"],
        "mcp": ["mcp", "workflow"],
        "external integration": ["external", "permission"],
        "cli": ["cli", "json"],
        "threat modeling": ["threat", "trust boundar"],
        "figma": ["figma", "screenshot"],
        "tdd": ["test", "red"],
        "debugging": ["root cause", "reproduction"],
        "verification": ["verify", "evidence"],
        "progressive disclosure": ["progressive", "tool"],
    }
    for name, needles in required.items():
        assert all(needle in content for needle in needles), name


def test_state_machine_and_safety_invariants_present():
    content = text(SKILL)
    for token in (
        "ALIGN", "FRAME", "ACT", "PROVE", "DELIVER",
        "risk", "complexity", "reversibility", "uncertainty",
        "least privilege", "consent", "rollback", "stop condition",
    ):
        assert token.lower() in content.lower(), token


def test_adaptive_rules_avoid_process_theater():
    content = text(SKILL).lower()
    assert "trivial" in content and "do not force" in content
    assert "prototype" in content and "throw away" in content
    assert "one behavior slice" in content
    assert "do not dump" in content and "tool" in content
    assert "do not narrate" in content


def test_source_attribution_and_license_notices():
    sources = text(SOURCES)
    for project in (
        "talk-normal", "openai/skills", "awesome-codex-skills",
        "obra/superpowers", "dsh-anchored-standard",
    ):
        assert project in sources
    license_text = text(LICENSE)
    assert "MIT License" in license_text
    assert "MoonsvnLyn" in license_text
    assert "FirmamentalSpring" in license_text


def test_docs_describe_install_and_scope():
    for path in (README, README_ZH):
        content = text(path)
        assert "SKILL.md" in content
        assert "adaptive-taskcraft" in content
        assert "MIT" in content
