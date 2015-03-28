#!/bin/sh
set -x -e # Show commands being executed and exit nonzero upon errors.

./generate-readme.py
./python3/github-repo-summary.py bamos/python-scripts
# Requires customization: ./python3/link-checker.py
./python3/phonetic.py github
./python3/rank-writing.py --help
# OSX only: ./python3/get-osx-wallpaper.py
./python3/word-counter.py README.md
./python3/eval-expr.py '(((4+6)*10)<<2)'
./python3/merge-mutt-contacts.py --help

for F in generate-readme.py python3/*; do
  pep8 --ignore=E402,E501 $F
done
