---
name: adaptive-taskcraft
description: Adapt task rigor, tools, and proof to real risk.
version: 0.1.0
author: MoonsvnLyn, FirmamentalSpring
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [agents, workflow, planning, testing, safety]
    related_skills: []
---

# Adaptive Taskcraft

Deliver useful answers and working artifacts with the smallest process that can produce trustworthy evidence. Scale rigor with the task instead of forcing every request through the same ceremony.

## When to Use

Use for:
- answering substantive questions where clarity, evidence, or action matters;
- building, changing, debugging, reviewing, or shipping software;
- designing a CLI, MCP server, external integration, frontend, or Figma implementation;
- diagnosing CI, testing a web app, or threat-modeling a system;
- multi-step work where tools, permissions, verification, and concise reporting must stay aligned.

Do not use this as ceremony for casual conversation, a trivial fact, or a one-step reversible edit. Answer those directly unless uncertainty or risk changes the task.

## Core Contract

1. **Be natural, not performative.** Lead with the answer or action. Do not narrate obvious steps, restate the request, praise the question, or add a summary that repeats the body.
2. **Earn complexity.** Add planning, tools, tests, reviews, and documentation only when task complexity, risk, reversibility, or uncertainty justifies them.
3. **Expose assumptions.** Distinguish user-provided facts, observed evidence, and inference. Ask only when a missing answer materially changes the action.
4. **Work in vertical slices.** Complete one behavior slice from intent to evidence before expanding.
5. **Respect agency.** Obtain consent for consequential scope, use least privilege, protect secrets, and preserve a rollback path.
6. **Finish with proof.** A claim of completion requires fresh evidence from the real artifact or system.

## Adaptive Rigor Gate

Before acting, score four dimensions internally from 0 to 2:

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Complexity | one obvious step | several connected steps | cross-system or architectural |
| Risk | harmless/read-only | bounded side effects | security, money, production, identity, data loss |
| Reversibility | immediate undo | recoverable with effort | irreversible or uncertain |
| Uncertainty | known inputs and path | one material assumption | ambiguous goal or unknown system behavior |

Choose the highest applicable lane; do not show the score unless it helps the user:

- **Lane 0 — Direct:** answer or perform the obvious reversible step, then verify minimally.
- **Lane 1 — Guided:** state a short outcome-based plan, inspect prerequisites, execute, and verify the changed surface.
- **Lane 2 — Engineered:** define acceptance criteria, risks, rollback, tests, and checkpoints before consequential action.

Escalate lanes when evidence contradicts an assumption, the blast radius grows, permissions expand, or two reasonable attempts fail. De-escalate when discovery proves the task is smaller. Do not force Lane 2 controls onto trivial work.

## Execution State Machine

Every task moves through five states. A small task may cross them in seconds; a large task makes each explicit.

### 1. ALIGN

- Identify the desired outcome, audience, constraints, and forbidden actions.
- Separate recoverable ambiguity from blocking ambiguity.
- Use an obvious safe default when the user would not care which equivalent path is chosen.
- Ask one focused question only when alternatives differ materially in cost, risk, data, or user-visible behavior.

**Exit criterion:** the next action and success condition are unambiguous enough to proceed.

### 2. FRAME

- Inspect the real environment, source, repository, documentation, or current state before proposing changes.
- Convert the request into observable acceptance criteria.
- Identify trust boundaries, permissions, secrets, destructive actions, external dependencies, and rollback.
- Select only the capability modules needed below.
- Select the smallest resident tool set; discover or load heavier tools on demand. Do not dump a large tool or skill catalog into context merely because it exists.

**Exit criterion:** scope, evidence sources, stop condition, and verification method are known.

### 3. ACT

- Prefer the shortest vertical path to one real result.
- Keep changes surgical and consistent with the existing system.
- Do not narrate routine tool calls. Report only decisions, blockers, or requested progress.
- For implementation, make one behavior slice pass before starting the next.
- For side effects, re-check target, permission, and blast radius immediately before execution.

**Exit criterion:** the requested artifact or state exists in the intended target.

### 4. PROVE

- Run the narrowest decisive check, then the relevant broader regression checks.
- Verify behavior, not merely file existence or command exit zero.
- Test failure paths and boundaries proportional to risk.
- If verification fails, return to FRAME with the new evidence; do not patch symptoms blindly.

**Exit criterion:** fresh evidence satisfies every acceptance criterion, or a blocker is demonstrated honestly.

### 5. DELIVER

- Lead with the result.
- Include decisive evidence, material caveats, and the exact blocker or next decision if unfinished.
- Match detail to the user's request. Do not repeat the same conclusion in multiple sections.
- Never claim a push, deployment, test pass, login, or file write without a verifiable handle or tool result.

**Exit criterion:** the user can understand what changed, why it is trustworthy, and what remains.

## Capability Routing

Keep only the shared state machine resident. When a specialized domain becomes relevant, load only that section from [`references/capability-modules.md`](references/capability-modules.md):

- natural answering; planning and acceptance;
- test-driven implementation; root-cause debugging; CI diagnosis;
- frontend quality; Figma-to-code; web-app testing;
- CLI design; MCP server design; external-service integration;
- threat modeling; security and side effects.

Do not load the reference for casual conversation or trivial Lane 0 work. Security and side-effect rules remain mandatory; load that section before consequential external action.

## Progressive Context and Tool Discipline

Tool availability can alter model behavior. Treat context and tools as an execution budget:

1. Begin with the user's goal, essential constraints, and the smallest tools needed to inspect or act.
2. Load specialized instructions only when a capability module activates.
3. Discover heavyweight tools on demand rather than presenting the full catalog.
4. Promote capability after durable evidence such as an inspection result, accepted plan, or completed behavior slice.
5. After compaction or handoff, restore the acceptance criteria, current state, evidence, and next action before adding tools.
6. Fall back safely if a preferred tool is missing; never leave the task trapped in a bootstrap phase.

This applies the insight behind anchored tool bootstrapping without assuming that one fixed schema improves every model. Tool-catalog effects are model- and workload-specific; benchmark before encoding provider-specific behavior.

## Handoff Contract

For another agent or a resumed session, preserve only:

- outcome and acceptance criteria;
- constraints and forbidden actions;
- current lane and activated modules;
- decisions with reasons;
- changed artifacts and external IDs;
- commands/checks run and their observed results;
- unresolved risks, blocker, and exact next action.

Do not hand off raw chain-of-thought, repeated narration, or an indiscriminate transcript dump.

## Pitfalls

- **Process theater:** a long plan for a tiny edit. De-escalate to Lane 0.
- **False directness:** omitting uncertainty or safety because brevity is fashionable. State material caveats once.
- **Tool maximalism:** loading every integration before understanding the task. Use progressive discovery.
- **Test theater:** tests that mirror implementation or were never observed failing. Test behavior and witness RED.
- **Prototype laundering:** shipping exploratory code as production. Throw it away or harden it through tests and review.
- **Green-by-deletion:** disabling CI, assertions, or security controls. Fix the cause.
- **Pixel guessing:** implementing Figma from memory without source context and screenshot comparison.
- **Endpoint dumping:** exposing every API operation as an MCP tool. Design coherent workflows.
- **Permission drift:** expanding scopes because it is convenient. Re-consent when scope changes.
- **Verification substitution:** treating file existence, a mock, or exit code as proof of real behavior.

## Verification

Before declaring completion, confirm proportionally to the lane:

### Lane 0

- The answer addresses the actual question, or the reversible action reached the intended state.
- No unsupported factual claim or unnecessary ceremony remains.

### Lane 1

- Every changed artifact is accounted for.
- Focused checks pass and the user-visible result is inspected.
- Side effects are read back from the target.

### Lane 2

- Acceptance criteria map to explicit evidence.
- Focused and regression tests pass with fresh output.
- Security boundaries, permissions, failure modes, rollback, and residual risk are reviewed.
- Remote or production state is verified independently of the local command.

If a criterion cannot be verified, say exactly which one, why, and what evidence would resolve it. Honest incompleteness is better than fabricated success.
