# 单源双宿主·各两件:core/src/{合同,原理,机制}.md → 常驻件(CLAUDE.md/AGENTS.md=宿主机制+合同+指向)与按需件(原理与机制-<宿主>.md=原理+机制)。只改源,不手改渲染件。
import pathlib
root = pathlib.Path(__file__).parent
src = root / "core" / "src"
rd = lambda n: (src / n).read_text(encoding="utf-8").rstrip()
contract, principles, mech = rd("合同.md"), rd("原理.md"), rd("机制.md")

claude_head = """# 协作基线(薄核·Claude 常驻件;由 claude-baseline 装载,仅本项目生效;本文件由 render.py 生成,勿手改)

> 本文件只常驻**合同**。原理库与机制在 `原理与机制-Claude.md`(安装后为项目 `docs/基线-原理与机制.md`):**上任通读一次**,之后按档回读;模块按需。判据与 Codex 渲染完全一致,差异只在宿主机制段与文件形态。

## 宿主机制(Claude)
- 模块装在 `./.claude/skills/<name>/SKILL.md`,按 description 自动触发;可用子代理(Agent)承担并行检索/抽取/盲审,模型按判断密度选(轻档 sonnet 级、盲审换家族或 opus 级);机械活派子代理,主窗只做判断与综合。
- 项目记忆:`MEMORY.md` 索引每窗自动注入,记忆文件按需读。记忆不复述合同/现状页已有内容,索引行不写成规则摘要。
"""
codex_head = """# 协作基线(薄核·Codex 常驻件;由 claude-baseline 装载,仅本项目生效;本文件由 render.py 生成,勿手改)

> 使命:目标、约束、证据决定路径。完成=产物可用、主张可追溯、验证已运行、实质未知已说明。本文件只常驻**合同**。原理库与机制在 `原理与机制-Codex.md`(安装后为项目 `docs/基线-原理与机制.md`):**上任通读一次**,之后按档回读;模块按需。判据与 Claude 渲染完全一致,差异只在宿主机制段与文件形态。

## 宿主机制(Codex)
- 模块装在 `./.agents/skills/<name>/SKILL.md`;更近目录的 `AGENTS.md` / `AGENTS.override.md` 可覆盖局部默认,冲突须报告。
- 写 `.agents/` 用 shell 复制+逐字节比对,不用 `apply_patch`(0.147 实测误拒为项目外);后台调用关 stdin;沙箱联网需显式开启;能力结论前先查配置档位(沙箱/权限/网络/路径),再谈能力边界。
- 外部发送、破坏性动作、购买、凭据或扩范围须先授权;本地、可逆、范围内动作默认推进,不反复请示。
- Codex 无自动记忆层;跨会话状态只在项目文件里。
"""
ondemand_head = "# 协作基线·原理库与机制({host} 按需件;上任通读一次,之后按档回读;由 render.py 生成,勿手改)\n\n"
(root / "core" / "CLAUDE.md").write_text(claude_head + "\n" + contract + "\n", encoding="utf-8")
(root / "core" / "AGENTS.md").write_text(codex_head + "\n" + contract + "\n", encoding="utf-8")
(root / "core" / "原理与机制-Claude.md").write_text(ondemand_head.format(host="Claude") + principles + "\n\n" + mech + "\n", encoding="utf-8")
(root / "core" / "原理与机制-Codex.md").write_text(ondemand_head.format(host="Codex") + principles + "\n\n" + mech + "\n", encoding="utf-8")
print("rendered: contract", len(contract), "principles+mech", len(principles) + len(mech))
