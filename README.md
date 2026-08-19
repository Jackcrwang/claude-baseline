# claude-baseline：跨项目协作基线（Claude + Codex 双家族）

个人协作守则库：工作习惯、跨家族协作模式、通用工作流、调研纪律、游戏设计守则、项目迁移方法论。同一套**判据**，两份**渲染**（Claude 语域 `core/CLAUDE.md` / GPT 语域 `core/AGENTS.md`）；改一份必查另一份，差异只许来自语域或宿主机制。**零全局钩子**——任何窗口只有在你亲口说激活句时才会接触本仓库；不装载的项目（尤其隔离项目）物理上不存在被加载的路径。仓库名沿用 `claude-baseline`（不改旧激活句与旧项目引用）。

## 三个入口句（复制粘贴，替换尖括号）

1. **Claude 新项目装载**
   > 读取 `<本仓库路径>/BOOTSTRAP.md`，按其流程为本项目装载守则。项目简介：<一两句：做什么、预期规模、是否用 Codex>
2. **Codex 新项目装载**
   > 读取 `<本仓库路径>/BOOTSTRAP-codex.md`，按其流程为本项目装载守则。项目简介：<一两句：做什么、预期规模、是否启用 Claude 跨家族审查>
3. **把现有项目迁到另一家族/换总窗**（在当前主导窗口里说）
   > 读取 `<本仓库路径>/modules/migration/SKILL.md`，按其判据把本项目迁移到 <Codex/Claude> 主导。

本机路径示例：`E:\workflows\claude-baseline\`。新电脑先 `git clone <仓库URL>` 到任意位置，激活句里的路径换成 clone 位置即可。

## 结构

```
core/CLAUDE.md           薄核·Claude 渲染（沟通协议/诚实底线/方法论/任务分档；装载后每会话生效）
core/AGENTS.md           薄核·Codex 渲染（同一判据，决策合同式：使命/默认姿态/硬边界/决策规则/交付/档位/地图）
modules/workflow/        中重档工作流：工单制/交接/多代理/验收分级/证据纪律（两家族共用）
modules/research/        调研纪律：假设穷尽/证据分层/台账-残差/收口（两家族共用）
modules/game-dev/        游戏设计通用守则（两家族共用）
modules/codex-collab/    Claude 主导时用 Codex（派单纪律/跨家族异源审查）
modules/claude-collab/   Codex 主导时用 Claude 非 Fable 模型（启用判据/claude -p 调用纪律/跨家族盲审）
modules/migration/       项目主导权跨家族/换窗迁移方法论（判据版：可迁性/分层迁/四件交接物/自检题/影子期）
templates/               方向日志/工单/回执/恢复块 四模板（重档项目用）
BOOTSTRAP.md             Claude 装载协议（判定表/护栏/临时vs安装）
BOOTSTRAP-codex.md       Codex 装载协议（同上；模块装为 .agents/skills/<name>/SKILL.md）
```

## 三条不变式

1. **隔离＞一切**：永不写 `~/.claude/` 或 `~/.codex/`；隔离项目（当前为 `E:\A`）拒绝安装模式；唯一入口=你手动粘贴的激活句。
2. **自动判断，不自动生效**：装载器按项目简介拟清单，复述后等你确认。
3. **更新自由**：任何窗口受你指示可提交改进（项目结项沉淀等）；条款修改保住原效力等级；两份渲染同步。
