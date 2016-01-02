#!/bin/sh
set -x -e # Show commands being executed and exit nonzero upon errors.

./python2.7/music-organizer.py --help
./python2.7/mt.py --help

for F in python2.7/*; do
  flake8 --ignore=E402,E501 $F
done
