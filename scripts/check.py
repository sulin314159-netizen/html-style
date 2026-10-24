#!/usr/bin/env python3
"""html-style 静态自检。

用法:
    python -B scripts/check.py <file.html> [more.html ...]

只做机器能判断的检查；排版、留白、语义这些要靠 references/quality.md 人工过。
颜色数量只作提示，不判失败（撞色风格本来就多色）。
退出码 1 表示有硬问题。
"""
import re
import sys
import pathlib

EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F0FF\uFE0F]"
)
DINGBAT = re.compile("[\u2766\u2767\u2756\u2736\u2740\u274B\u2742]")
EXTERNAL = re.compile(
    r'<(?:img|script|link)\b[^>]*?(?:src|href)\s*=\s*"(https?://[^"]+)"',
    re.I,
)
CSS_URL = re.compile(r'@import\s+url\(\s*["\']?(https?://[^)"\']+)')
HEX = re.compile(r"#[0-9a-fA-F]{6}\b")


def check(path: pathlib.Path) -> tuple[list[str], list[str]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    issues: list[str] = []
    notes: list[str] = []

    if not re.search(r"<meta\s+charset", text, re.I):
        issues.append("缺少 <meta charset>")
    if not re.search(r"<html[^>]+lang=", text, re.I):
        issues.append("缺少 <html lang>")
    if not re.search(r"<title>[^<]+</title>", text, re.I):
        issues.append("缺少 <title>")

    for m in EXTERNAL.finditer(text):
        issues.append(f"外链资源（建议改内联/本地）: {m.group(1)}")
    for m in CSS_URL.finditer(text):
        issues.append(f"CSS 外链字体/资源: {m.group(1)}")

    for m in EMOJI.finditer(text):
        issues.append(f"出现 emoji（不要用 emoji 当图标）: {m.group(0)!r}")
        break
    for m in DINGBAT.finditer(text):
        issues.append(f"出现装饰符（不要当图标/分隔）: {m.group(0)!r}")
        break

    clean = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    clean = re.sub(r"<!--.*?-->", "", clean, flags=re.S)
    colors = {c.lower() for c in HEX.findall(clean)}
    if len(colors) > 14:
        notes.append(
            f"颜色数量偏多（{len(colors)} 个 hex）——单强调色风格应 ≤8，"
            "撞色/渐变风格确认每一色都来自风格卡"
        )

    return issues, notes


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    failed = False
    for arg in argv:
        p = pathlib.Path(arg)
        if not p.is_file():
            print(f"[skip] {arg} 不存在")
            failed = True
            continue
        issues, notes = check(p)
        if issues:
            failed = True
            print(f"[问题] {p}")
            for i in issues:
                print(f"  - {i}")
        else:
            print(f"[通过] {p}")
        for n in notes:
            print(f"  [提示] {n}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
