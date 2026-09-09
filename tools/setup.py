#!/usr/bin/env python3
"""
Prepare a machine to continue this project. Works on Windows, macOS and Linux.

    python tools/setup.py          (Windows: py tools\\setup.py)

Safe to run more than once. It checks what is present, builds the Python
environment the tools need, and tells you what is still missing.
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIN = os.name == "nt"
VENV = ROOT / "env"
VPY = VENV / ("Scripts/python.exe" if WIN else "bin/python")

ok = warn = 0


def good(msg):
    global ok
    ok += 1
    print(f"  ok    {msg}")


def todo(msg, *hints):
    global warn
    warn += 1
    print(f"  todo  {msg}")
    for h in hints:
        print(f"          {h}")


def have(cmd):
    return shutil.which(cmd) is not None


def run(args, **kw):
    return subprocess.run(args, capture_output=True, text=True, **kw)


def section(title):
    print(f"\n{title}\n")


def check_git():
    if not have("git"):
        todo(
            "git is not installed",
            "Windows: https://git-scm.com/download/win  (installs Git Bash too)",
            "macOS:   xcode-select --install",
        )
        return
    r = run(["git", "--version"])
    if r.returncode != 0:
        todo(
            "git is present but not working",
            "macOS: xcode-select --install. If that seems to do nothing, a stale lock",
            "is the usual cause. See HANDOFF.md.",
        )
        return
    good(r.stdout.strip())


def check_python():
    v = sys.version_info
    if v < (3, 8):
        todo(f"python {v.major}.{v.minor} is too old, need 3.8 or newer")
    else:
        good(f"python {v.major}.{v.minor}.{v.micro}")


def check_env():
    if VPY.exists():
        r = run([str(VPY), "-c", "import zstandard, fitz, PIL; print('ok')"])
        if r.returncode == 0:
            good("python environment ready")
            return
        print("  ...  environment exists but is missing packages, installing")
    else:
        print("  ...  creating env/")
        r = run([sys.executable, "-m", "venv", str(VENV)])
        if r.returncode != 0:
            todo("could not create env/", r.stderr.strip()[:200])
            return

    pip = VENV / ("Scripts/pip.exe" if WIN else "bin/pip")
    r = run([str(pip), "install", "--quiet", "--disable-pip-version-check",
             "-r", str(ROOT / "requirements.txt")])
    if r.returncode == 0:
        good("python environment ready")
    else:
        todo("could not install requirements",
             f"try: {pip} install -r requirements.txt",
             r.stderr.strip()[:200])


def check_sources():
    missing = []
    for d in ("carbonmade-originals", "deck-slides", "github-export", "fig-extracts"):
        (good if (ROOT / "source-material" / d).is_dir() else missing.append)(
            f"source-material/{d}" if (ROOT / "source-material" / d).is_dir() else f"source-material/{d}"
        )
    for f in ("handoff-brief-v3.txt", "portfolio-panel-deck.pdf", "carbonmade-copy-pulled.md"):
        p = ROOT / "source-material" / f
        if p.is_file():
            good(f"source-material/{f}")
        else:
            missing.append(f"source-material/{f}")
    for m in missing:
        todo(f"{m} missing")
    if missing:
        print("          All of it is listed in HANDOFF.md section 4, with where to fetch each one.")


def check_site():
    try:
        from urllib.request import urlopen
        with urlopen("https://stav-fg.github.io", timeout=10) as r:
            (good if r.status == 200 else todo)(f"site responding ({r.status})")
    except Exception as e:
        todo(f"could not reach https://stav-fg.github.io ({type(e).__name__})")


def main():
    print(f"\nSetting up in {ROOT}")
    print(f"Platform: {sys.platform}")

    section("Tools")
    check_git()
    check_python()

    section("Python environment")
    check_env()

    section("Source material, gitignored and fetched separately")
    check_sources()

    section("Live site")
    check_site()

    print(f"\n  {ok} ready, {warn} to do\n")
    print("  Next: read HANDOFF.md, then the four files it lists.\n")
    if VPY.exists():
        rel = VPY.relative_to(ROOT)
        print(f"  Run the Figma extractor with:\n    {rel} tools/figextract.py <file.fig> source-material/fig-extracts\n")


if __name__ == "__main__":
    main()
