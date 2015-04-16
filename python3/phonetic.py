#!/usr/bin/env python3

__author__ = ['[Brandon Amos](http://bamos.github.io)']
__date__ = '2014.02.14'

"""
Obtain the NATO phonetic alphabet representation from short phrases.

```
$ phonetic.py github
g - golf
i - india
t - tango
h - hotel
u - uniform
b - bravo
```
"""

import sys

phonetic_table = {
    'a': 'alpha', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliet',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray',
    'y': 'yankee', 'z': 'zulu',
}

for word in sys.argv[1:]:
    for char in word:
        char = char.lower()
        if char not in phonetic_table:
            print(char)
        else:
            print(char + ' - ' + phonetic_table[char])
    print()
