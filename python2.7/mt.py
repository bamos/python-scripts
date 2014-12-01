#!/usr/bin/env python2

import argparse
import multitail

parser = argparse.ArgumentParser()
parser.add_argument('files', type=str, nargs='+')
args = parser.parse_args()

for fn, line in multitail.multitail(args.files):
  print("{}: {}".format(fn,line.strip()))
