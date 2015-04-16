#!/usr/bin/env python2

__author__ = ['[Brandon Amos](http://bamos.github.io)']
__date__ = '2014.11.30'

"""
This script implements the simple
[multitail](https://pypi.python.org/pypi/multitail)
example to tail multiple files and append the filename to the beginning
of the output.
"""

import argparse
import multitail
import sys


# http://stackoverflow.com/questions/107705
class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        self.stream.write(data)
        self.stream.flush()

    def __getattr__(self, attr):
        return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

parser = argparse.ArgumentParser()
parser.add_argument('files', type=str, nargs='+')
args = parser.parse_args()

for fn, line in multitail.multitail(args.files):
    print("{}: {}".format(fn, line.strip()))
