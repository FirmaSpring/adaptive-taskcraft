# Adaptive Taskcraft

一个可移植的 AI Agent `SKILL.md`：依据任务的真实风险，动态调整规划、工具、测试、安全与验证强度。

它不让所有请求都走同一套沉重流程，而是采用三档严谨度和五阶段执行循环：

`ALIGN -> FRAME -> ACT -> PROVE -> DELIVER`

它整合并重新设计了自然表达、任务规划、TDD、根因调试、CI 修复、前端与 Figma 实现、浏览器测试、CLI 与 MCP 设计、外部服务连接、威胁建模，以及渐进式工具披露等思想。

## 为什么需要它

Agent 常在两个极端之间失败：

- 流程不足：静默假设、危险写入、未验证就宣称完成；
- 流程过量：小事写长计划、上下文过载、无关工具全量加载、执行迟缓。

Adaptive Taskcraft 会选择足以产出可信证据的最小流程。

## 安装

把仓库中的 `SKILL.md` 复制到 Agent 的技能目录，并命名为 `adaptive-taskcraft/`。

常见目录：

```text
~/.hermes/skills/adaptive-taskcraft/SKILL.md
~/.agents/skills/adaptive-taskcraft/SKILL.md
<project>/.agents/skills/adaptive-taskcraft/SKILL.md
```

不同宿主的技能发现规则不同；如果宿主会缓存技能，安装后请重启或新建会话。

先加载核心 `SKILL.md`，只有任务需要专业领域模块时才读取 `references/capability-modules.md`，让渐进披露真正减少上下文负担。

## 使用

在需要可靠回答、软件开发、调试、审查、外部集成或多步骤执行时加载 `adaptive-taskcraft`。技能会自行判断任务应当直接处理、引导式执行，还是进入工程化控制。

## 核心原则

- 直接自然地回答，不堆空话；
- 用结果和验收标准规划，而非罗列动作；
- 渐进加载工具和专业指令；
- 以纵向行为切片推进，并按需要使用 TDD；
- 最小权限、明确同意、可回滚和威胁意识；
- 所有完成声明都要有新鲜证据。

## 范围

本仓库包含技能说明、结构不变量测试、来源致谢和 MIT 许可证，不捆绑第三方代码，也不绑定某个模型或 Agent 宿主。

思想来源和归属见 [SOURCES.md](SOURCES.md)。领域模块位于 [`references/capability-modules.md`](references/capability-modules.md)，只在任务需要时加载。

## 测试

```bash
python -m pytest tests/test_skill.py -q
```

## 许可证

MIT。Copyright 2026 MoonsvnLyn and FirmamentalSpring。
