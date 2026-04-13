#!/usr/bin/env python3
"""
update_skill.py — 自动更新 yufree-style skill

从新博客文章里提取有价值的观察思考，更新 worldview_digest.md。
skill 源文件存在 cn/yufree-skill-src/，Mac 本地和 Cowork 都能访问。

用法:
  python update_skill.py            # 只处理上次运行后的新文章
  python update_skill.py --all      # 重新处理所有文章（重建摘要）
  python update_skill.py --dry-run  # 只打印会处理哪些文件，不修改任何东西

Mac 本地 Cron（每月1号9点，需要 ollama 在跑）:
  0 9 1 * * cd /path/to/blog/cn && python3 update_skill.py >> ~/skill_update.log 2>&1
"""

import os
import re
import sys
import json
import requests
import argparse
import subprocess
from pathlib import Path
from datetime import datetime, date

# ── 配置（路径均相对于 cn 目录，无需修改）──────────────────────────────
BLOG_DIR    = Path(__file__).parent                        # cn 目录
SKILL_SRC   = BLOG_DIR / "yufree-skill-src"                # skill 源文件（Mac 可访问）
DIGEST_FILE = SKILL_SRC / "references" / "worldview_digest.md"
STATE_FILE  = SKILL_SRC / ".last_update"                   # 记录上次处理时间

OLLAMA_URL  = "http://localhost:11434/api/generate"
MODEL       = "qwen3.5:latest"                             # 你本机的模型名

# 跳过这些文件夹/文件名中含有以下关键词的文章
SKIP_PATTERNS = ["research-paper", "精选语料库", "update_skill", "yufree-skill-src"]
# ────────────────────────────────────────────────────────────────────────


THEMES = [
    "知识与认知", "人性与个体", "生活哲学", "社会与制度",
    "经济与财富", "政治与国际", "教育与成长", "学术与职业", "科技与人工智能",
]

EXTRACT_PROMPT = """\
你在帮一个科研工作者维护他的个人博客"世界观摘要"。
下面是他博客的一篇文章：

---
{content}
---

任务：找出这篇文章里有没有值得加入世界观摘要的新观点或明确立场。

判断标准（必须同时满足）：
1. 有清晰的个人判断，不是泛泛介绍或步骤教程
2. 用了概率/量级思维、批判叙事逻辑、承认复杂性，或有独特视角
3. 不是纯粹的论文解读或技术记录

如果有，按以下格式输出（每条核心立场控制在40字以内，仿照示例风格简洁直接）：

主题: [从以下选一个：知识与认知/人性与个体/生活哲学/社会与制度/经济与财富/政治与国际/教育与成长/学术与职业/科技与人工智能]
- **关键词（3-5字）**：核心立场，一句话。

可以输出多条（不同主题）。如果这篇文章没有满足条件的内容，只输出：无

注意：宁可少提取也不要输出平庸的总结。"""


def call_ollama(prompt: str) -> str:
    """调用本地 ollama，返回模型输出文本。"""
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.3,
            "num_predict": 800,
        },
        # qwen3 系列关闭思维链，避免输出 <think>...</think>
        "system": "/no_think",
    }
    try:
        resp = requests.post(OLLAMA_URL, json=payload, timeout=120)
        resp.raise_for_status()
        text = resp.json().get("response", "").strip()
        # 清理 qwen3 可能残留的 <think> 块
        text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
        return text
    except requests.exceptions.ConnectionError:
        print("  ✗ 无法连接 ollama，请确认 ollama serve 已启动")
        sys.exit(1)
    except Exception as e:
        print(f"  ✗ ollama 调用失败: {e}")
        return ""


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """解析 YAML frontmatter，返回 (meta_dict, body)。"""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_text = text[4:end]
    body = text[end + 4:].strip()
    meta = {}
    for line in fm_text.splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip().strip("'\"")
    return meta, body


def find_md_files(since: date | None) -> list[Path]:
    """找出所有需要处理的中文博客 .md 文件。"""
    files = []
    for path in sorted(BLOG_DIR.rglob("*.md")):
        # 跳过黑名单
        if any(p in str(path) for p in SKIP_PATTERNS):
            continue
        # 只要文件名以日期开头（YYYY-MM-DD）的博客文章
        name = path.stem if path.name != "index.md" else path.parent.name
        if not re.match(r"^\d{4}-\d{2}-\d{2}", name):
            continue
        # 过滤 since 日期
        if since:
            try:
                post_date = date.fromisoformat(name[:10])
                if post_date <= since:
                    continue
            except ValueError:
                pass
        files.append(path)
    return files


def extract_entries(content: str, title: str) -> list[dict]:
    """
    调用 LLM 从文章里提取观点，返回 [{"theme": ..., "line": ...}, ...]。
    """
    prompt = EXTRACT_PROMPT.format(content=content[:4000])  # 限制上下文长度
    raw = call_ollama(prompt)

    if not raw or raw.strip() == "无":
        return []

    entries = []
    current_theme = None
    for line in raw.splitlines():
        line = line.strip()
        if line.startswith("主题:"):
            current_theme = line.split(":", 1)[1].strip()
        elif line.startswith("- **") and current_theme:
            entries.append({"theme": current_theme, "line": line})
    return entries


def update_digest(new_entries: list[dict], dry_run: bool = False) -> int:
    """把新条目插入 worldview_digest.md 对应主题下，返回实际插入数量。"""
    if not new_entries:
        return 0

    text = DIGEST_FILE.read_text(encoding="utf-8")
    added = 0

    for entry in new_entries:
        theme = entry["theme"]
        line  = entry["line"]

        # 简单去重：如果粗略匹配已在文件中，跳过
        # 取 ** 内的关键词来比较
        kw_match = re.search(r"\*\*(.+?)\*\*", line)
        keyword = kw_match.group(1) if kw_match else line[:10]
        if keyword in text:
            print(f"  跳过（已存在）: {line[:60]}")
            continue

        # 找到对应主题区块，在最后一条之后插入
        section_header = f"## {theme}"
        idx = text.find(section_header)
        if idx == -1:
            print(f"  ✗ 找不到主题 [{theme}]，跳过: {line[:60]}")
            continue

        # 找到这个 section 的末尾（下一个 ## 或文件末尾）
        next_section = text.find("\n## ", idx + len(section_header))
        insert_pos = next_section if next_section != -1 else len(text)

        # 在 insert_pos 前插入新行
        new_line = "\n" + line
        text = text[:insert_pos] + new_line + text[insert_pos:]
        added += 1
        print(f"  ✓ [{theme}] {line[:70]}")

    if added > 0 and not dry_run:
        DIGEST_FILE.write_text(text, encoding="utf-8")

    return added


def repackage_skill():
    """把 yufree-skill-src/ 打包成 cn/yufree-style.skill。

    打包逻辑很简单（不依赖 skill-creator），直接用 zipfile 实现，
    这样本地 Mac cron 跑时不需要 Cowork 环境也能打包。
    """
    import zipfile, shutil, tempfile

    dest = BLOG_DIR / "yufree-style.skill"
    tmp  = Path(tempfile.mktemp(suffix=".skill"))

    try:
        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zf:
            for f in sorted(SKILL_SRC.rglob("*")):
                if f.is_file() and not f.name.startswith("."):
                    zf.write(f, f.relative_to(SKILL_SRC.parent))
        shutil.move(str(tmp), str(dest))
        print(f"  ✓ {dest.name} 已更新（{dest.stat().st_size // 1024} KB）")
    except Exception as e:
        print(f"  ⚠ 打包失败: {e}")


# ── 主流程 ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--all",     action="store_true", help="重新处理所有文章")
    parser.add_argument("--dry-run", action="store_true", help="只打印，不修改文件")
    args = parser.parse_args()

    # 读取上次运行时间
    since = None
    if not args.all and STATE_FILE.exists():
        try:
            since = date.fromisoformat(STATE_FILE.read_text().strip())
            print(f"上次更新: {since}，只处理之后的新文章")
        except ValueError:
            pass
    else:
        print("处理所有文章" if args.all else "首次运行，处理所有文章")

    files = find_md_files(since)
    if not files:
        print("没有需要处理的新文章。")
        return

    print(f"找到 {len(files)} 篇文章待处理\n")

    total_added = 0
    for path in files:
        name = path.stem if path.name != "index.md" else path.parent.name
        print(f"→ {name}")
        if args.dry_run:
            continue

        raw = path.read_text(encoding="utf-8", errors="ignore")
        meta, body = parse_frontmatter(raw)

        # 跳过太短的文章（教程代码片段等）
        if len(body.strip()) < 300:
            print("  跳过（内容太短）")
            continue

        entries = extract_entries(body, meta.get("title", name))
        if not entries:
            print("  无值得提取的内容")
            continue

        added = update_digest(entries, dry_run=args.dry_run)
        total_added += added

    print(f"\n共新增 {total_added} 条观点到 worldview_digest.md")

    if total_added > 0 and not args.dry_run:
        repackage_skill()

    # 更新 state
    if not args.dry_run:
        STATE_FILE.write_text(date.today().isoformat())
        print(f"状态已更新: {date.today()}")


if __name__ == "__main__":
    main()
