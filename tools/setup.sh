#!/usr/bin/env bash
# Prepare a machine to continue this project. Safe to run more than once.
set -uo pipefail
cd "$(dirname "$0")/.."
ok=0; warn=0

say()  { printf "  %s\n" "$1"; }
good() { printf "  \033[32mok\033[0m    %s\n" "$1"; ok=$((ok+1)); }
bad()  { printf "  \033[33mtodo\033[0m  %s\n" "$1"; warn=$((warn+1)); }

echo
echo "Checking this machine"
echo

if git --version >/dev/null 2>&1; then
  good "git $(git --version | awk '{print $3}')"
else
  bad "git is not working. Run: xcode-select --install"
  say "      If that appears to do nothing, a stale lock is the usual cause:"
  say "      rm -f /tmp/.com.apple.dt.CommandLineTools.installondemand.in-progress"
  say "      then try again. See README for the full catch-22."
fi

if python3 -c 'import sys; sys.exit(0)' 2>/dev/null; then
  good "python3 $(python3 -V 2>&1 | awk '{print $2}')"
else
  bad "python3 missing. It ships with the Command Line Tools above."
fi

echo
echo "Figma extractor"
echo

if [ -x env/bin/python ] && env/bin/python -c 'import zstandard' 2>/dev/null; then
  good "environment ready"
else
  say "creating env/ and installing zstandard ..."
  if python3 -m venv env >/dev/null 2>&1 && ./env/bin/pip install --quiet --disable-pip-version-check zstandard >/dev/null 2>&1; then
    good "environment ready"
  else
    bad "could not build env/. Try: python3 -m venv env && ./env/bin/pip install zstandard"
  fi
fi

echo
echo "Source material (gitignored, has to be fetched separately)"
echo

for d in carbonmade-originals deck-slides github-export fig-extracts; do
  if [ -d "source-material/$d" ]; then good "source-material/$d"; else bad "source-material/$d missing. See HANDOFF.md section 4."; fi
done
for f in handoff-brief-v3.txt portfolio-panel-deck.pdf carbonmade-copy-pulled.md; do
  if [ -f "source-material/$f" ]; then good "source-material/$f"; else bad "source-material/$f missing. See HANDOFF.md section 4."; fi
done

echo
echo "Live site"
echo
code=$(curl -s -o /dev/null -w '%{http_code}' https://stav-fg.github.io 2>/dev/null || echo "000")
if [ "$code" = "200" ]; then good "https://stav-fg.github.io responding"; else bad "site returned $code"; fi

echo
echo "  $ok ready, $warn to do"
echo
echo "  Next: read HANDOFF.md, then the four files it lists."
echo
