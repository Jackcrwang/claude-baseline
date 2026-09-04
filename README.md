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

## 结构(2026-09 轻重构:三层核+单源双渲染+证据横切+病例按需)

```
core/src/合同.md          常驻·协作合同(沟通/决策权/效力档/诚实红线/资源路由/压缩协作法/汇报节奏/回环句)
core/src/原理.md          上任通读·判断原理库 17 条(每条:原则/保护什么/新伤;出生案例见 cases/)
core/src/机制.md          按档·任务分档/加载四档/模块地图/渲染与维护
core/CLAUDE.md           渲染件(Claude 宿主机制段+三层)——render.py 生成,勿手改
core/AGENTS.md           渲染件(Codex 宿主机制段+三层)——同上;两家族判据零漂移
render.py                单源双渲染脚本(改源后运行)
cases/病例.md            原理的出生案例(去项目化,按需读)
modules/evidence/        证据规范(唯一定义:模态×问题/成色/样本量/舆情/收敛/台账)
modules/workflow/        中重档工作流(工单制/交接/多代理/验收分级/规则收敛)
modules/research/        调研流程(立案/推进/行动/收口;证据条款引 evidence)
modules/game-dev/        游戏设计守则(+成熟参考的设计层逆向节)
modules/codex-collab/    Claude 主导时用 Codex(派单纪律/异源审查/档位二)
modules/claude-collab/   Codex 主导时用 Claude
modules/migration/       换总窗/跨家族迁移判据
templates/               方向日志/工单/回执/恢复块
BOOTSTRAP.md / BOOTSTRAP-codex.md   装载协议
```

## 三条不变式

1. **隔离＞一切**：永不写 `~/.claude/` 或 `~/.codex/`；隔离项目（当前为 `E:\A`）拒绝安装模式；唯一入口=你手动粘贴的激活句。
2. **自动判断，不自动生效**：装载器按项目简介拟清单，复述后等你确认。
3. **更新自由**：任何窗口受你指示可提交改进（项目结项沉淀等）；条款修改保住原效力等级；两份渲染同步。
