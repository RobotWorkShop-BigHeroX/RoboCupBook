# RoboCupBook 写作规范检查器，规则见 docs/style-guide.md
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TARGETS = ["docs", "latex/chapters"]
SKIP = {"superpowers", "style-guide.md", "node_modules", ".git"}

# word -> (级别, 规则)
BANNED: dict[str, tuple[str, str]] = {
    # 5 不过度断言
    "最好": ("error", "5 最高级没有比较标准"),
    "最强": ("error", "5 最高级没有比较标准"),
    "最快": ("error", "5 最高级没有比较标准"),
    "最优": ("error", "5 最高级没有比较标准"),
    "唯一": ("error", "5 最高级没有比较标准"),
    "零缺陷": ("error", "5 无法验证的承诺"),
    "确保": ("error", "5 说不出验证方法就用它代替了证据"),
    "保证": ("error", "5 说不出验证方法就用它代替了证据"),
    "皇冠明珠": ("error", "5 宣传语"),
    "倾力打造": ("error", "5 宣传语"),
    "里程碑": ("error", "5 宣传语"),
    "划时代": ("error", "5 宣传语"),
    "重磅": ("error", "5 宣传语"),
    "赋能": ("error", "5 空词"),
    "助力": ("error", "5 空词"),
    "全方位": ("error", "5 空词"),
    "闭环生态": ("error", "5 空词"),
    # 4 不预告
    "欢迎来到": ("error", "4 章节开场三件套"),
    "本章将": ("error", "4 章节开场三件套"),
    "接下来我们": ("error", "4 章节开场三件套"),
    "值得一提": ("warn", "4 填充句"),
    "众所周知": ("warn", "4 填充句"),
    "不难发现": ("warn", "4 填充句"),
    "显而易见": ("warn", "4 填充句"),
    # 9 时间锚点
    "目前": ("warn", "9 时间锚点"),
    "当前": ("warn", "9 时间锚点"),
    "最新": ("warn", "9 时间锚点"),
    "即将": ("warn", "9 时间锚点"),
    "近期": ("warn", "9 时间锚点"),
    # 2 动词虚化
    "进行": ("warn", "2 动词虚化，换成具体动词"),
    "具备": ("warn", "2 动词虚化"),
    "具有": ("warn", "2 动词虚化"),
    "开展": ("warn", "2 动词虚化"),
    # 语言禁令
    "不是": ("error", "禁止否定对比句式"),
    "而是": ("error", "禁止否定对比句式"),
    "而不是": ("error", "禁止否定对比句式"),
    "栈": ("error", "禁用词，直接说明具体事物"),
    "落地": ("error", "禁用词，换成具体说法"),
    "钉死": ("error", "禁用词，换成具体说法"),
    "对齐": ("error", "禁用词，换成具体说法"),
    "总结": ("error", "禁止总结与总起"),
    "上述": ("error", "禁止总结与总起"),
    "一句话": ("warn", "禁止总结与总起"),
}

# 允许的组合（误报豁免）
ALLOW = ["最好成绩", "最优方程", "完全自主", "最后一次", "进一步", "改进", "进行时", "目前已知"]
BARE_URL = re.compile(r"(?<![(<\[])\bhttps?://[^\s)\]>]+")
IGNORE_MARK = "lint:ignore"


def targets(argv: list[str]) -> list[Path]:
    paths: list[Path] = []
    for raw in argv or DEFAULT_TARGETS:
        p = (ROOT / raw).resolve()
        if p.is_dir():
            paths.extend(sorted(p.rglob("*.md")) + sorted(p.rglob("*.tex")))
        elif p.exists():
            paths.append(p)
        else:
            print(f"找不到: {raw}", file=sys.stderr)
    return [p for p in paths if not (SKIP & set(p.parts))]


def strip_code(line: str) -> str:
    """把行内代码替换成等长空格，保持列号不变。"""
    return re.sub(r"`[^`]*`", lambda m: " " * len(m.group()), line)


def check(path: Path) -> list[dict]:
    hits: list[dict] = []
    fenced = False
    for no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.rstrip("\n")
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if fenced or IGNORE_MARK in line:
            continue
        text = strip_code(line)
        for word, (level, rule) in BANNED.items():
            start = 0
            while (i := text.find(word, start)) != -1:
                start = i + 1
                if any(
                    (pos := text.find(a)) != -1
                    and pos <= i
                    and i + len(word) <= pos + len(a)
                    for a in ALLOW
                ):
                    continue
                hits.append({
                    "file": str(path.relative_to(ROOT)).replace("\\", "/"),
                    "line": no,
                    "col": i + 1,
                    "level": level,
                    "rule": rule,
                    "word": word,
                    "text": line.strip()[:70],
                })
        if "file:///" in text:
            hits.append({
                "file": str(path.relative_to(ROOT)).replace("\\", "/"),
                "line": no, "col": text.find("file:///") + 1,
                "level": "error", "rule": "10 绝对路径在 Pages/PDF 里会失效",
                "word": "file:///", "text": line.strip()[:70],
            })
        if path.suffix == ".md":
            for m in BARE_URL.finditer(text):
                hits.append({
                    "file": str(path.relative_to(ROOT)).replace("\\", "/"),
                    "line": no, "col": m.start() + 1,
                    "level": "warn", "rule": "10 裸 URL，改成带说明的链接文字",
                    "word": m.group()[:40], "text": line.strip()[:70],
                })
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description="RoboCupBook 写作规范检查器")
    ap.add_argument("paths", nargs="*", help="文件或目录，默认 docs/ 与 latex/main.tex")
    ap.add_argument("--strict", action="store_true", help="警告也视为失败")
    ap.add_argument("--json", action="store_true", help="输出 JSON")
    args = ap.parse_args()

    hits = [h for p in targets(args.paths) for h in check(p)]
    hits.sort(key=lambda h: (h["file"], h["line"], h["col"]))

    if args.json:
        print(json.dumps(hits, ensure_ascii=False, indent=2))
    else:
        current = None
        for h in hits:
            if h["file"] != current:
                current = h["file"]
                print(f"\n{current}")
            tag = "ERROR" if h["level"] == "error" else " warn"
            print(f"  {h['line']:>4}:{h['col']:<3} {tag}  {h['word']:<8} {h['rule']}")
            print(f"        | {h['text']}")

    errs = sum(h["level"] == "error" for h in hits)
    warns = len(hits) - errs
    print(f"\n共 {errs} 处违规，{warns} 处提示。规则见 docs/style-guide.md", file=sys.stderr)
    failed = errs > 0 or (args.strict and warns > 0)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())