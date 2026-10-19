#!/usr/bin/env python3
"""
RoboCup HSL 新人入门手册 PDF 自动化编译构建脚本
支持一键检测本地 TeX 环境，调用 xelatex 进行双遍编译以生成完整目录、超链接和书签，
并将输出文件整理至项目根目录。
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def find_xelatex():
    """查找本地 xelatex 编译器路径"""
    cmd = shutil.which("xelatex")
    if cmd:
        return cmd
    
    # 针对 Windows 常见安装路径进行回退检查
    fallback_paths = [
        r"D:\soft\MiKTeX\miktex\bin\x64\xelatex.exe",
        r"C:\Program Files\MiKTeX\miktex\bin\x64\xelatex.exe",
        r"C:\texlive\2026\bin\windows\xelatex.exe",
        r"C:\texlive\2025\bin\windows\xelatex.exe",
        r"C:\texlive\2024\bin\windows\xelatex.exe",
    ]
    for path in fallback_paths:
        if os.path.exists(path):
            return path
    return None

def clean_auxiliary_files(latex_dir: Path):
    """清理 LaTeX 编译生成的中间临时文件"""
    exts = [".aux", ".log", ".out", ".toc", ".synctex.gz", ".fls", ".fdb_latexmk"]
    for f in latex_dir.iterdir():
        if f.suffix in exts:
            try:
                f.unlink()
            except Exception:
                pass

def build_pdf(clean: bool = False):
    root_dir = Path(__file__).resolve().parent.parent
    latex_dir = root_dir / "latex"
    main_tex = latex_dir / "main-v1.2.tex"
    output_pdf = root_dir / "RoboCup_HSL_Handbook_v1.2.0.pdf"

    if not main_tex.exists():
        print(f"[-] 错误: 未找到主排版文件 {main_tex}", file=sys.stderr)
        sys.exit(1)

    xelatex = find_xelatex()
    if not xelatex:
        print("[-] 错误: 未在系统路径或常见目录中检测到 xelatex 编译器！", file=sys.stderr)
        print("    请确保安装了 MiKTeX 或 TeXLive，并将 xelatex 添加至 PATH 环境变量。", file=sys.stderr)
        sys.exit(1)

    print(f"[+] 找到 XeLaTeX 编译器: {xelatex}")
    print(f"[+] 源码目录: {latex_dir}")
    print("[*] 开始第一遍编译（生成章节与目录引用元数据）...")

    cmd = [xelatex, "-interaction=nonstopmode", "-halt-on-error", "main-v1.2.tex"]
    result1 = subprocess.run(cmd, cwd=str(latex_dir), capture_output=True, text=True, encoding="utf-8", errors="replace")
    if result1.returncode != 0:
        print("[-] 第一遍编译失败！", file=sys.stderr)
        print(result1.stdout[-1500:], file=sys.stderr)
        sys.exit(1)

    print("[*] 开始第二遍编译（解析交叉引用与完整目录链接）...")
    result2 = subprocess.run(cmd, cwd=str(latex_dir), capture_output=True, text=True, encoding="utf-8", errors="replace")
    if result2.returncode != 0:
        print("[-] 第二遍编译失败！", file=sys.stderr)
        print(result2.stdout[-1500:], file=sys.stderr)
        sys.exit(1)

    generated_pdf = latex_dir / "main-v1.2.pdf"
    if not generated_pdf.exists():
        print(f"[-] 错误: 未检测到生成的 {generated_pdf}", file=sys.stderr)
        sys.exit(1)

    # 移动或复制到根目录交付物
    shutil.copy2(generated_pdf, output_pdf)
    size_mb = output_pdf.stat().st_size / (1024 * 1024)
    print(f"[OK] 编译成功！输出文件: {output_pdf.name} ({size_mb:.2f} MB)")
    print(f"    绝对路径: {output_pdf.resolve()}")

    if clean:
        print("[*] 清理中间辅助文件...")
        clean_auxiliary_files(latex_dir)

if __name__ == "__main__":
    clean_flag = "--clean" in sys.argv
    build_pdf(clean=clean_flag)
