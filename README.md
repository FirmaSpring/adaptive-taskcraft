# Adaptive Taskcraft

A portable `SKILL.md` for AI agents that scales planning, tools, testing, safety, and proof to the task's real risk.

Instead of making every request follow a heavyweight ritual, Adaptive Taskcraft uses three rigor lanes and a five-state execution loop:

`ALIGN -> FRAME -> ACT -> PROVE -> DELIVER`

It integrates and refines lessons from natural-response prompting, planning, TDD, root-cause debugging, CI repair, frontend and Figma implementation, browser testing, CLI and MCP design, external-service integration, threat modeling, and progressive tool disclosure.

## Why

Agent failures often come from opposite extremes:

- too little process: assumptions, unsafe writes, unverified claims;
- too much process: verbose plans, context overload, tools loaded without need, and slow trivial work.

Adaptive Taskcraft chooses the smallest workflow that can still produce trustworthy evidence.

## Install

Copy this repository's `SKILL.md` into your agent's skill directory under `adaptive-taskcraft/`.

Common layouts include:

```text
~/.hermes/skills/adaptive-taskcraft/SKILL.md
~/.agents/skills/adaptive-taskcraft/SKILL.md
<project>/.agents/skills/adaptive-taskcraft/SKILL.md
```

Exact discovery rules vary by host. Restart or begin a new session after installation if your agent caches skills.

Load the core `SKILL.md` first. Read `references/capability-modules.md` only when the task needs a specialized domain module; this keeps progressive disclosure operational rather than merely aspirational.

## Use

Load `adaptive-taskcraft` for substantive answers, software changes, debugging, reviews, integrations, and multi-step execution. The skill itself decides whether the task needs direct action, a guided workflow, or engineered controls.

## Language Support

English, Simplified/Traditional Chinese, and Japanese are supported. The agent matches the user's language and register while preserving identifiers, commands, logs, and exact error text. Multilingual rules live in [`references/language-adaptation.md`](references/language-adaptation.md).

## Principles

- natural answers without filler;
- outcome-based plans with acceptance criteria;
- progressive loading of tools and specialized instructions;
- vertical behavior slices and proportional TDD;
- least privilege, consent, rollback, and threat awareness;
- completion claims backed by fresh evidence.

## Scope

This repository contains instructions, tests for structural invariants, source acknowledgements, and an MIT license. It does not bundle third-party code or provider-specific plugins.

See [SOURCES.md](SOURCES.md) for influences and attribution. Domain-specific modules live in [`references/capability-modules.md`](references/capability-modules.md) and are loaded only when relevant.

## Test

```bash
python -m pytest tests/test_skill.py -q
```

## License

MIT. Copyright 2026 MoonsvnLyn and FirmamentalSpring.
