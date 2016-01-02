#!/usr/bin/env python2

__author__ = ['[Brandon Amos](http://bamos.github.io)']
__date__ = '2015.12.30'

"""
This script (fix-music-tags.py) mass-removes unwanted music tags.
"""

from mutagen.easyid3 import EasyID3
import argparse
import glob


def fixTags(fname, keep):
    audio = EasyID3(fname)

    delKeys = []
    for k, v in audio.items():
        if k not in keep:
            delKeys.append(k)

    for k in delKeys:
        del audio[k]
    audio.save()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='Directory with mp3 files to fix.')
    parser.add_argument('--keep', default=['title', 'artist', 'album', 'genre'],
                        type=str, nargs='+', metavar='TAG',
                        help="Tags to keep. Default: title, artist, album, genre")
    args = parser.parse_args()

    for fname in glob.glob("{}/*.mp3".format(args.directory)):
        print("Fixing tags for {}".format(fname))
        fixTags(fname, args.keep)
