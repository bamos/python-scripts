#!/usr/bin/env python2.7

import os
import re
import sys
from mutagen.easyid3 import EasyID3

replaceChars = (
  (" ", "-"),
  ("(", ""),
  (")", ""),
  (",", ""),
  (".", ""),
  ("'", ""),
  ("?", "")
)
def toNeat(s):
  s = s.lower()
  for r in replaceChars: s = s.replace(r[0], r[1])
  search = re.search("[^0-9a-z\-]", s)
  if search:
    print("Error: Unrecognized character in '" + s + "'")
    sys.exit(-42)
  return s

for dirname, dirnames, filenames in os.walk('.'):
  for subdirname in dirnames:
    print("subdir:" + str(subdirname))
  for filename in filenames:
    fullPath = os.path.join(dirname, filename)
    print("file: " + str(fullPath))
    audio = EasyID3(fullPath)
    title = audio['title'][0].decode()
    print("  title: " + title)

    neatTitle = toNeat(title)
    print("  neat-title: " + neatTitle)

    ext = os.path.splitext(filename)[1]
    newFullPath = os.path.join(dirname, neatTitle + ext)
    print("  newFullPath: " + newFullPath)

    if newFullPath != fullPath:
      if os.path.isfile(newFullPath):
        print("Error: File exists: '" + newFullPath + "'")
        sys.exit(-42)

      os.rename(fullPath, newFullPath)

print("\nComplete!")
