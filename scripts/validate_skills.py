#!/usr/bin/env python3
"""Validate this repository's skill entrypoints (requires PyYAML)."""

from pathlib import Path
import re
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
PLACEHOLDER = re.compile(r"\b(?:TODO|TBD|FIXME)\b|replace-me", re.IGNORECASE)


def validate(folder: Path) -> list[str]:
    entry = folder / "SKILL.md"
    if not entry.is_file():
        return [f"{entry}: 缺少技能入口"]
    try:
        content = entry.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"{entry}: {exc}"]
    lines = content.splitlines()
    if not lines or lines[0] != "---":
        return [f"{entry}: 缺少 YAML frontmatter"]
    try:
        end = lines.index("---", 1)
        metadata = yaml.safe_load("\n".join(lines[1:end]))
    except (ValueError, yaml.YAMLError) as exc:
        return [f"{entry}: frontmatter 无效：{exc}"]
    if not isinstance(metadata, dict):
        return [f"{entry}: frontmatter 必须是映射"]
    errors = []
    name = metadata.get("name")
    if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) > 64:
        errors.append("name 必须为 1–64 字符的小写字母、数字和连字符名称")
    elif name != folder.name:
        errors.append("name 必须与技能目录名一致")
    description = metadata.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append("description 必须为非空字符串")
    if not "\n".join(lines[end + 1:]).strip():
        errors.append("缺少技能正文")
    if PLACEHOLDER.search(content):
        errors.append("包含未清理的模板占位符")
    return [f"{entry}: {error}" for error in errors]


def main() -> int:
    if sys.argv[1:]:
        folders = [Path(arg).resolve() for arg in sys.argv[1:]]
    else:
        skills = ROOT / "skills"
        if not skills.is_dir():
            print(f"ERROR: {skills}: 技能目录不存在", file=sys.stderr)
            return 1
        folders = sorted(path for path in skills.iterdir() if path.is_dir())
    if not folders:
        print("ERROR: 未找到技能", file=sys.stderr)
        return 1
    errors = [error for folder in folders for error in validate(folder)]
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print(f"校验通过：{len(folders)} 个技能")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
