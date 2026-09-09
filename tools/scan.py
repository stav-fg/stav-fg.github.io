#!/usr/bin/env python3
"""
Check every tracked file for strings that must never be committed.

    env/bin/python tools/scan.py            macOS and Linux
    env\\Scripts\\python tools\\scan.py        Windows

Use the environment's interpreter, built by tools/setup.py. A bare `python` is
the Microsoft Store stub on Windows and exits 9009 without running anything,
which looks like a scan failure and is not one.

Reads the terms from .confidential-terms, which is gitignored so the list itself
never enters the repo.

Exit codes, because this gates a push and the caller has to tell these apart:
    0   scanned, nothing found
    1   scanned, found something. Do not push.
    2   could not scan. Says nothing about whether the repo is clean.
"""
import shutil, subprocess, sys
from pathlib import Path

def cannot(msg):
    """Exit 2. Never 1, which means a real hit."""
    print(f"\n  scan did not run: {msg}\n", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
TERMS = ROOT / ".confidential-terms"

if not TERMS.exists():
    cannot(f"no {TERMS.name}. See HANDOFF.md section 6.")

terms = [l.strip() for l in TERMS.read_text().splitlines()
         if l.strip() and not l.startswith("#")]
if not terms:
    cannot(f"{TERMS.name} is empty, so every file would pass")

if not shutil.which("git"):
    cannot("git is not on PATH. On Windows, open the shell that has PortableGit.")

r = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True)
if r.returncode != 0:
    cannot(f"git ls-files failed: {r.stderr.strip()[:160]}")

files = r.stdout.split()
if not files:
    cannot("git listed no tracked files, so there is nothing to check")

hits = []
for f in files:
    p = ROOT / f
    try:
        body = p.read_text(errors="ignore").lower()
    except Exception:
        continue
    for t in terms:
        if t.lower() in body:
            hits.append((f, t))

if hits:
    print(f"\n  {len(hits)} problem(s). Do not push.\n")
    for f, t in hits:
        print(f"    {f}  contains a blocked term")
    print()
    sys.exit(1)

print(f"\n  clean. {len(files)} tracked files checked against {len(terms)} terms.\n")
