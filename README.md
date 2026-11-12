# Hongmou Skills

一个以 `SKILL.md` 为入口的 Agent Skills 集合。每个技能独立维护，可按需安装。

## 技能目录

| 技能 | 用途 |
| --- | --- |
| [cn-gov-policy-index](skills/cn-gov-policy-index/SKILL.md) | 采集中国党政机关官网政策文件与公告，生成可追溯原文的索引表 |

## 使用技能

一键安装：

```bash
npx skills add Craun718/hongmou
```

```bash
# 安装指定技能
npx skills add Craun718/hongmou --skill cn-gov-policy-index

# 安装到指定 Agent
npx skills add Craun718/hongmou -a codex -a claude-code -a cursor

# 全局安装全部技能，无需交互
npx skills add Craun718/hongmou --all -g -y
```

在支持技能的 Agent 中使用 `$cn-gov-policy-index`，并说明采集范围，例如：

```text
$cn-gov-policy-index 帮我收集国务院最近一个月发布的政策文件，列出标题、发布日期和官方原文链接。
```

该技能需要联网检索和 HTTP 请求能力；遇到动态页面时还需可用的浏览器自动化工具。它提供采集流程与判断依据，不附带固定抓取脚本；交付政策文件索引，不抓取正文或下载附件。

也可以直接阅读对应的 `SKILL.md`。安装后使用 `npx skills check` 检查更新，使用 `npx skills update` 更新已安装的技能。

## 新增技能

1. 在 `skills/<skill-name>/` 下创建 `SKILL.md`，以 YAML frontmatter 声明 `name` 和 `description`。
2. 在 `description` 中写明能力和触发场景，在正文中说明任务特有的判断依据、执行流程和完成标准。
3. 按需添加 `scripts/`、`references/` 或 `assets/`，在入口中说明它们何时使用。
4. 在上方目录中添加技能链接，并运行校验。

名称使用小写字母、数字和连字符，长度不超过 64 个字符，与目录名保持一致。面向使用者的说明默认使用中文，技术标识保留原文。技能应能独立理解；说明需要的运行环境和工具，使用相对路径引用随技能分发的资源。仅部分场景需要的详细内容放入 `references/`，并在入口注明读取条件。

## 本地校验

需要 Python 3.10 或以上版本：

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate_skills.py
```

校验单个技能：

```bash
.venv/bin/python scripts/validate_skills.py skills/cn-gov-policy-index
```

脚本检查 YAML 元数据、目录命名、正文与模板占位符；技能的实际行为及其附带脚本仍需按用途验证。提交和拉取请求会自动运行相同校验。
