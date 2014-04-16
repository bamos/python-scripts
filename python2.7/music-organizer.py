#!/usr/bin/env python2.7

import os
import re
import shutil
import sys
from mutagen.easyid3 import EasyID3

emptyChars = re.compile(r"[(),.'\\\?\#]")
def toNeat(s):
  s = s.lower().replace(" ","-").replace("&","and").replace("*","-")
  s = emptyChars.sub("", s)
  search = re.search("[^0-9a-z\-]", s)
  if search:
    print("Error: Unrecognized character in '" + s + "'")
    sys.exit(-42)
  return s

artists = set()
valid = {"yes":True, "y":True, "no":False, "n":False}
for dirname, dirnames, filenames in os.walk('.'):
  # Make sure there aren't a lot of different artists
  # in case this was called from the wrong directory.
  for filename in filenames:
    try:
      audio = EasyID3(os.path.join(dirname, filename))
      artist = audio['artist'][0].decode()
      artists.add(artist)
    except:
      pass

if len(artists) > 2:
  while True:
    print("Warning: More than 2 artists found.")
    print("This will move all songs to the current directory.")
    print("Continue? yes/no")
    choice = raw_input().lower()
    if choice in valid:
      if valid[choice]: break
      else:
        print("Exiting.")
        sys.exit(-1)

delete_dirs = []
for dirname, dirnames, filenames in os.walk('.'):
  # Move all the files to the root directory.
  for filename in filenames:
    ext = os.path.splitext(filename)[1]
    if ext == ".mp3":
      fullPath = os.path.join(dirname, filename)
      print("file: " + str(fullPath))

      try:
        audio = EasyID3(fullPath)
        title = audio['title'][0].decode()
        print("  title: " + title)
      except: title = None

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
    delete_dirs.append(subdirname)

for d in delete_dirs:
  shutil.rmtree(d,ignore_errors=True)

print("\nComplete!")
