# Sources and acknowledgements

Adaptive Taskcraft is an original synthesis. It does not copy or bundle third-party source code. The following projects informed specific design ideas; their authors retain all rights to their work.

## Primary influences

- [hexiecs/talk-normal](https://github.com/hexiecs/talk-normal), MIT — direct, natural responses; resistance to canned filler and repeated conclusions. Adaptive Taskcraft adds proportional detail, evidence, and safety so brevity does not erase necessary nuance.
- [openai/skills](https://github.com/openai/skills) — task planning, CI diagnosis, durable CLI design, security threat modeling, and Figma implementation workflows. Consult each skill's own license or notice before copying its text or code. Adaptive Taskcraft restates workflow concepts independently.
- [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) — browser-based web-app testing, MCP workflow design, and external-service connectivity. Consult the repository and individual files for current licensing before reuse; no code is bundled here.
- [obra/superpowers](https://github.com/obra/superpowers), MIT — requirements discovery, planning, TDD, systematic debugging, review, and verification discipline. Adaptive Taskcraft replaces always-on ceremony with risk-adaptive lanes and vertical behavior slices.
- [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard), MIT — evidence that API-visible tool catalogs and injected context can affect a model's initial trajectory; bootstrap, promotion, resident catalogs, durable phase state, and safe fallback. Adaptive Taskcraft generalizes this into model-neutral progressive context discipline and explicitly requires benchmarking before provider-specific anchoring.

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
