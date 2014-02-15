#!/usr/bin/env python3.3
#
# phonetic.py
# Obtain the NATO phonetic alphabet representation from short phrases.
#
# Brandon Amos <http://bamos.io>
# 2014.02.14

import sys

phonetic_table = {
  'a': 'alpha',
  'b': 'bravo',
  'c': 'charlie',
  'd': 'delta',
  'e': 'echo',
  'f': 'foxtrot',
  'g': 'golf',
  'h': 'hotel',
  'i': 'india',
  'j': 'juliet',
  'k': 'kilo',
  'l': 'lima',
  'm': 'mike',
  'n': 'november',
  'o': 'oscar',
  'p': 'papa',
  'q': 'quebec',
  'r': 'romeo',
  's': 'sierra',
  't': 'tango',
  'u': 'uniform',
  'v': 'victor',
  'w': 'whiskey',
  'x': 'x-ray',
  'y': 'yankee',
  'z': 'zulu',
}

for word in sys.argv[1:]:
  for char in word:
    if char not in phonetic_table: print(char.lower())
    else: print(char.lower() + ' - ' + phonetic_table[char])
  print()
