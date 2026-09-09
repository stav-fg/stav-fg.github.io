#!/usr/bin/env python3
"""
Check every tracked file for strings that must never be committed.

    python tools/scan.py

Reads the terms from .confidential-terms, which is gitignored so the list itself
never enters the repo. Exits non-zero if anything is found, so it can gate a push.
"""
import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TERMS = ROOT / ".confidential-terms"

if not TERMS.exists():
    sys.exit(f"no {TERMS.name}. See HANDOFF.md section 6.")

terms = [l.strip() for l in TERMS.read_text().splitlines()
         if l.strip() and not l.startswith("#")]
files = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True,
                       text=True).stdout.split()

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
