#!/usr/bin/env python3

__author__ = ['[Brandon Amos](http://bamos.github.io)']
__date__ = '2014.02.14'

"""
`rank-writing.py` ranks the writing quality of my
blog's Markdown posts and my project's Markdown README files.

The following programs should be on your `PATH`:
+ [aspell](http://aspell.net/)
+ [write-good](https://github.com/btford/write-good)
+ [diction](https://www.gnu.org/software/diction/)


```
$ rank-writing.py *.md

=== 2013-05-03-scraping-tables-python.md ===
Total: 53
├── aspell: 34
├── diction: 0
└── write-good: 19

...

=== 2013-04-16-pdf-from-plaintext.md ===
Total: 0
├── aspell: 0
├── diction: 0
└── write-good: 0
```
"""

import argparse
import re
from subprocess import Popen, PIPE
import shutil
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--aspell', action='store_true')
parser.add_argument('--diction', action='store_true')
parser.add_argument('--write-good', action='store_true')
parser.add_argument('files', type=str, nargs='+')
args = parser.parse_args()

# If no arguments are provided, show everything.
if not (args.aspell or args.diction or args.write_good):
    args.aspell = args.diction = args.write_good = True

programs = []
if args.aspell:
    programs.append("aspell")
if args.diction:
    programs.append("diction")
if args.write_good:
    programs.append("write-good")

for program in programs:
    if not shutil.which(program):
        print("Error: '{}' not found on PATH. Please install.".format(program))
        sys.exit(-1)


def call(cmd, in_f=None):
    if in_f:
        with open(in_f, 'r') as f:
            p = Popen(cmd, stdout=PIPE, stderr=PIPE, stdin=f)
    else:
        p = Popen(cmd, stdout=PIPE, stderr=PIPE)
    out = p.communicate()[0].decode()
    if p.returncode != 0:
        raise Exception("Error running {}".format(cmd))
    return out


def getNumSuggestions(program, f_name):
    if program == "write-good":
        out = call(["write-good", f_name])
        return out.count("-------------")
    elif program == "diction":
        out = call(["diction", "--suggest", f_name])
        r = re.search("(\S*) phrases? in (\S*) sentences? found.", out)
        if r:
            if r.group(1) == "No":
                return 0
            else:
                return int(r.group(1))
    elif program == "aspell":
        out = call(["aspell", "list"], in_f=f_name)
        return len(out.split())
    else:
        raise Exception("Unrecognized program: {}".format(program))


def getSuggestions(f_name):
    suggestions = list(map(lambda x: getNumSuggestions(x, f_name), programs))
    return (sum(suggestions), suggestions, f_name)

for tup in sorted(map(getSuggestions, args.files), reverse=True):
    print("\n=== {} ===".format(tup[2]))
    print("    Total: {}".format(tup[0]))
    div = ["├──"] * (len(programs) - 1) + ["└──"]
    for program_output in list(zip(div, programs, tup[1])):
        print("    {} {}: {}".format(*program_output))
