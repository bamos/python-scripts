#!/usr/bin/env python2.7

import os
import re
import sys
from mutagen.easyid3 import EasyID3

emptyChars = re.compile(r"[(),.'\\\?]")
def toNeat(s):
  s = s.lower()
  s = s.replace(" ", "-")
  s = s.replace("&", "and")
  s = emptyChars.sub("", s)
  search = re.search("[^0-9a-z\-]", s)
  if search:
    print("Error: Unrecognized character in '" + s + "'")
    sys.exit(-42)
  return s

for dirname, dirnames, filenames in os.walk('.'):
  # Move all the files to the root directory.
  for filename in filenames:
    ext = os.path.splitext(filename)[1]
    if ext == ".mp3":
      fullPath = os.path.join(dirname, filename)
      print("file: " + str(fullPath))
      audio = EasyID3(fullPath)
      title = audio['title'][0].decode()
      print("  title: " + title)

      if not title:
        print("Error: title not found for '" + filename + "'")
        sys.exit(-42)

      neatTitle = toNeat(title)
      print("  neat-title: " + neatTitle)

      newFullPath = os.path.join(".", neatTitle + ext) # Remove subdirectories.
      print("  newFullPath: " + newFullPath)

      if newFullPath != fullPath:
        if os.path.isfile(newFullPath):
          print("Error: File exists: '" + newFullPath + "'")
          sys.exit(-42)

        os.rename(fullPath, newFullPath)
      os.chmod(newFullPath, 0644)
    elif ext == ".pdf":
      pass
    else:
      print("Error: Unrecognized file extension in '" + filename + "'")
      sys.exit(-42)

  # Delete all subdirectories.
  for subdirname in dirnames:
    os.rmdir(subdirname)

print("\nComplete!")
