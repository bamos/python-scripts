#!/usr/bin/env python2.7

__author__ = ['[Brandon Amos](http://bamos.github.io)']
__date__ = '2015.04.09'

"""
This script (music-autoplaylists.py) automatically creates
M3U playlists from the genre ID3 tags of songs in a directory.
"""

import argparse
import os
import re
import shutil
import sys
from mutagen.easyid3 import EasyID3
from collections import defaultdict


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--musicDir', type=str, default='.')
    parser.add_argument('--playlistDir', type=str, default='./playlists/auto')
    args = parser.parse_args()

    genres = defaultdict(list)
    for dpath, dnames, fnames in os.walk(args.musicDir):
        if '.git' in dpath:
            continue
        for fname in fnames:
            if os.path.splitext(fname)[1] != '.mp3':
                continue
            p = os.path.abspath(os.path.join(dpath, fname))
            audio = EasyID3(p)
            if 'genre' in audio:
                assert(len(audio['genre']) == 1)
                genre = toNeat(str(audio['genre'][0]))
            else:
                genre = 'Unknown'
            genres[genre].append(p)

    if os.path.exists(args.playlistDir):
        shutil.rmtree(args.playlistDir)
    os.makedirs(args.playlistDir)

    for genre, songs in genres.items():
        p = os.path.join(args.playlistDir, genre + '.m3u')
        print("Creating playlist: {}".format(p))
        with open(p, 'w') as f:
            f.write("#EXTM3U\n")
            f.write("\n".join(sorted(songs)) + "\n")

# Maps a string such as 'The Beatles' to 'the-beatles'.


def toNeat(s):
    s = s.lower().replace("&", "and")

    # Put spaces between and remove blank characters.
    blankCharsPad = r"()\[\],.\\\?\#/\!\$\:\;"
    blankCharsNoPad = r"'\""
    s = re.sub(r"([" + blankCharsPad + r"])([^ ])", "\\1 \\2", s)
    s = re.sub("[" + blankCharsPad + blankCharsNoPad + "]", "", s)

    # Replace spaces with a single dash.
    s = re.sub(r"[ \*\_]+", "-", s)
    s = re.sub("-+", "-", s)
    s = re.sub("^-*", "", s)
    s = re.sub("-*$", "", s)

    # Ensure the string is only alphanumeric with '-', '+', and '='.
    search = re.search("[^0-9a-z\-\+\=]", s)
    if search:
        print("Error: Unrecognized character in '" + s + "'")
        sys.exit(-42)
    return s

if __name__ == '__main__':
    main()
