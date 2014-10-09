#!/usr/bin/env python2.7
#
# music-organizer.py
# Brandon Amos <http://bamos.io/>
# 2014.4.19

import argparse
import os
import re
import shutil
import sys
from mutagen.easyid3 import EasyID3

parser = argparse.ArgumentParser(
  description='''Organizes a music collection using tag information.
    The directory format is that the music collection consists of
    artist subdirectories, and there are 2 modes to operate on
    the entire collection or a single artist.
    All names are made lowercase and separated by dashes for easier
    navigation in a Linux filesystem.'''
)
parser.add_argument('--delete-conflicts', action='store_true',
    dest='delete_conflicts',
    help='''If an artist has duplicate tracks with the same name,
    delete them. Note this might always be best in case an artist
    has multiple versions. To keep multiple versions,
    fix the tag information.''')
parser.add_argument('--ignore-multiple-artists', action='store_true',
    dest='ignore_multiple_artists',
    help='''This script will prompt for confirmation if an artist
    directory has songs with more than 2 different tags.
    This flag disables the confirmation and won't perform this check.''')
parser.add_argument('--collection', action='store_true',
    help='''Operate in 'collection' mode and run 'artist' mode on
    every subdirectory.''')
parser.add_argument('--artist',  action='store_true',
    help='''Operate in 'artist' mode and copy all songs to the
    root of the directory and cleanly format the names to
    be easily typed and navigated in a shell.''')
args = parser.parse_args()

if args.collection and args.artist:
  print("Error: Only provide 1 of '--collection' or '--artist'.")
  sys.exit(-1)
elif not (args.collection or args.artist):
  print("Error: Mode '--collection' or '--artist' not provided.")
  sys.exit(-1)

# Maps a string such as 'The Beatles' to 'the-beatles'.
def toNeat(s):
  s = s.lower().replace("&","and")
  s = re.sub(r"[()\[\],.'\"\\\?\#/\!\$\:]", "", s)
  s = re.sub(r"[ \*\_]", "-", s)
  s = re.sub("-+", "-", s)
  search = re.search("[^0-9a-z\-\=]", s)
  if search:
    print("Error: Unrecognized character in '" + s + "'")
    sys.exit(-42)
  return s

def artist(artistDir):
  print("Organizing artist '" + artistDir + "'.")
  if not args.ignore_multiple_artists:
    artists = set()
    for dirname, dirnames, filenames in os.walk(artistDir):
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
        print("Warning: More than 2 artists found in '" + artistDir + "'.")
        print("This will move all songs to the '" + artistDir + "' directory.")
        print("Continue? yes/no")
        choice = raw_input().lower()
        valid = {"yes":True, "y":True, "no":False, "n":False}
        if choice in valid:
          if valid[choice]: break
          else:
            print("Exiting.")
            sys.exit(-1)

  delete_dirs = []
  for dirname, dirnames, filenames in os.walk(artistDir):
    # Move all the files to the root directory.
    for filename in filenames:
      ext = os.path.splitext(filename)[1]
      if ext == ".mp3":
        fullPath = os.path.join(dirname, filename)
        print("file: " + str(fullPath))

        try:
          audio = EasyID3(fullPath)
          title = audio['title'][0].encode('ascii', 'ignore')
          print("  title: " + title)
        except: title = None

        if not title:
          print("Error: title not found for '" + filename + "'")
          sys.exit(-42)

        neatTitle = toNeat(title)
        print("  neatTitle: " + neatTitle)

        newFullPath = os.path.join(artistDir, neatTitle + ext)
        print("  newFullPath: " + newFullPath)

        if newFullPath != fullPath:
          if os.path.isfile(newFullPath):
            if args.delete_conflicts:
              os.remove(fullPath)
              print("File exists: '" + newFullPath + "'")
              print("Deleted: '" + fullPath + "'")
            else:
              print("Error: File exists: '" + newFullPath + "'")
              sys.exit(-42)
          else:
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
    shutil.rmtree(os.path.join(artistDir,d),ignore_errors=True)

def song(filename):
  print("Organizing song '" + filename + "'.")
  ext = os.path.splitext(filename)[1]
  try:
    audio = EasyID3(filename)
    artist = audio['artist'][0].encode('ascii', 'ignore')
    title = audio['title'][0].encode('ascii', 'ignore')
    print("  artist: " + artist)
    print("  title: " + title)
  except:
    artist = None
    title = None
  neatArtist = toNeat(artist)
  neatTitle = toNeat(title)
  print("  neatArtist: " + neatArtist)
  print("  neatTitle: " + neatTitle)
  if not os.path.isdir(neatArtist):
    os.mkdir(neatArtist)
  newFullPath = os.path.join(neatArtist,neatTitle+ext)
  os.rename(filename, newFullPath)
  os.chmod(newFullPath, 0644)

def collection():
  for f in os.listdir("."):
    if os.path.isdir(f):
      if f != 'iTunes' and f != 'playlists':
        artist(f)
    elif os.path.isfile(f): song(f)

if args.artist:
  artist('.')
else:
  collection()
print("\nComplete!")
