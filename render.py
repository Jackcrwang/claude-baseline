# 单源双渲染:core/src/{合同,原理,机制}.md → core/CLAUDE.md 与 core/AGENTS.md(只改源,不手改渲染件)
import io, pathlib
root = pathlib.Path(__file__).parent
src = root / "core" / "src"
parts = [(src / n).read_text(encoding="utf-8").rstrip() for n in ("合同.md", "原理.md", "机制.md")]
body = "\n\n".join(parts)

claude_head = """# 协作基线(薄核·Claude 渲染;由 claude-baseline 装载,仅本项目生效;本文件由 render.py 生成,勿手改)

> 结构:合同(常驻)/原理库(上任通读)/机制(按档)。项目专有内容不进本文件,放项目 docs。判据与 Codex 渲染完全一致,差异只在本段宿主机制。

## 宿主机制(Claude)
- 模块装在 `./.claude/skills/<name>/SKILL.md`,按 description 自动触发;可用子代理(Agent)承担并行检索/抽取/盲审,模型按判断密度选(轻档 sonnet 级、盲审换家族或 opus 级);机械活派子代理,主窗只做判断与综合。
"""
codex_head = """# 协作基线(薄核·Codex 渲染;由 claude-baseline 装载,仅本项目生效;本文件由 render.py 生成,勿手改)

> 使命:目标、约束、证据决定路径。完成=产物可用、主张可追溯、验证已运行、实质未知已说明。结构:合同(常驻)/原理库(上任通读)/机制(按档)。判据与 Claude 渲染完全一致,差异只在本段宿主机制。

## 宿主机制(Codex)
- 模块装在 `./.agents/skills/<name>/SKILL.md`;更近目录的 `AGENTS.md` / `AGENTS.override.md` 可覆盖局部默认,冲突须报告。
- 写 `.agents/` 用 shell 复制+逐字节比对,不用 `apply_patch`(0.147 实测误拒为项目外);后台调用关 stdin;沙箱联网需显式开启;能力结论前先查配置档位(沙箱/权限/网络/路径),再谈能力边界。
- 外部发送、破坏性动作、购买、凭据或扩范围须先授权;本地、可逆、范围内动作默认推进,不反复请示。
"""
(root / "core" / "CLAUDE.md").write_text(claude_head + "\n" + body + "\n", encoding="utf-8")
(root / "core" / "AGENTS.md").write_text(codex_head + "\n" + body + "\n", encoding="utf-8")
print("rendered", len(body))
