# Sources and acknowledgements

Adaptive Taskcraft is an original synthesis. It does not copy or bundle third-party source code. The following projects informed specific design ideas; their authors retain all rights to their work.

## Primary influences

The source revisions below are the versions reviewed during synthesis. Only general workflow ideas were independently re-expressed; no third-party implementation files are distributed here.

- [hexiecs/talk-normal](https://github.com/hexiecs/talk-normal/tree/d89cf329e775e640181427fae071652198264c7e) at `d89cf329e`, MIT; reviewed `prompt.md`, `skill/SKILL.md`, and `skill-hermes/SKILL.md` — direct, natural responses and resistance to canned filler.
- [openai/skills](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431) at `49f948fa`, per-skill licensing; reviewed curated CLI creator, Figma implementation, CI repair, and threat-model skill files. No root-wide license is inferred.
- [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills/tree/0930e1373789d2eda449039f7ac154b33031de89) at `0930e137`, mixed per-skill licensing; reviewed `gh-fix-ci`, `webapp-testing`, `mcp-builder`, `connect`, and adjacent license files. No repository-wide license is inferred.
- [obra/superpowers](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797) at `b36e0829`, MIT; reviewed brainstorming, writing-plans, TDD, and systematic-debugging skill files.
- [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard/tree/0a38616c1b7ce4219b6d94d95c89f34a90741616) at `0a38616c`, MIT; reviewed `README.md`, `LICENSE`, `NOTICE`, `shared/anchor-turn.mjs`, `shared/dev-tool-search.mjs`, `shared/skill-search.mjs`, and `shared/zero-tool-bootstrap.mjs` — first-turn anchoring, bootstrapping, and progressive discovery. Its NOTICE pins adapted DeepSeek Harness material at `47f943859bef60e4160492346772ded9b24f765a`; Adaptive Taskcraft generalizes workflow ideas without bundling that implementation.

## Article that motivated the survey

- [2026最佳Codex Skills推荐：10个提升AI效率的必装技能（附链接）](https://zhuanlan.zhihu.com/p/2043020441187504517) — discovery list and suggested combinations. Its marketing and cross-agent compatibility claims were treated as leads, not as verified facts.

## Design differences introduced here

- A four-factor rigor gate: complexity, risk, reversibility, and uncertainty.
- Three adaptive lanes instead of one mandatory workflow.
- A shared five-state loop: ALIGN, FRAME, ACT, PROVE, DELIVER.
- Capability modules activated only when relevant.
- Explicit escalation and de-escalation rules.
- A stop condition against endless polishing and a two-failed-hypothesis debugging reset.
- A compact handoff contract that preserves evidence without chain-of-thought or transcript dumps.
- Progressive tool and context loading with safe fallback, without claiming universal model improvement.

If future changes incorporate substantial portions of third-party material, preserve the corresponding copyright and permission notice as required by that project's license.
