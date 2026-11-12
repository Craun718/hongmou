# Hongmou Skills

一个以 `SKILL.md` 为入口的 Agent Skills 集合。每个技能独立维护，可按需安装。

## 技能目录

| 技能 | 用途 |
| --- | --- |
| [cn-gov-policy-index](skills/cn-gov-policy-index/SKILL.md) | 采集中国党政机关官网政策文件与公告，生成可追溯原文的索引表 |
| [skill-maintenance](skills/skill-maintenance/SKILL.md) | 在本仓库新增或修改技能，并完成校验 |

## 使用技能

将需要的技能目录复制到你的 Agent 支持的技能目录。例如，为 Codex 安装维护技能：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/skill-maintenance "${CODEX_HOME:-$HOME/.codex}/skills/"
```

在本仓库打开 Agent，使用 `$skill-maintenance`，并说明要创建或修改的技能。也可以直接阅读对应的 `SKILL.md`。已安装的副本需要在仓库更新后重新复制。

## 新增技能

1. 在 `skills/<skill-name>/` 下创建 `SKILL.md`，可从 [模板](templates/SKILL.md) 开始。
2. 填写名称、触发条件、执行流程和完成标准；删除模板中的占位内容。
3. 按需添加 `scripts/`、`references/` 或 `assets/`，在入口中说明它们何时使用。
4. 在上方目录中添加技能链接，并运行校验。

名称使用小写字母、数字和连字符，长度不超过 64 个字符，与目录名保持一致。技能应能独立理解；说明需要的运行环境和工具，使用相对路径引用随技能分发的资源。

## 本地校验

需要 Python 3.10 或以上版本：

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate_skills.py
```

校验单个技能：

```bash
.venv/bin/python scripts/validate_skills.py skills/skill-maintenance
```

脚本检查 YAML 元数据、目录命名、正文与模板占位符；技能的实际行为及其附带脚本仍需按用途验证。提交和拉取请求会自动运行相同校验。
