#!/usr/bin/env python2

import argparse
import multitail
import sys

# http://stackoverflow.com/questions/107705
class Unbuffered(object):
  def __init__(self, stream): self.stream = stream
  def write(self, data): self.stream.write(data); self.stream.flush()
  def __getattr__(self, attr): return getattr(self.stream, attr)
sys.stdout = Unbuffered(sys.stdout)

parser = argparse.ArgumentParser()
parser.add_argument('files', type=str, nargs='+')
args = parser.parse_args()

for fn, line in multitail.multitail(args.files):
  print("{}: {}".format(fn,line.strip()))
