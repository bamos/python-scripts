#!/usr/bin/env python3

from collections import Counter
import argparse
import re
from itertools import islice
import operator

parser = argparse.ArgumentParser()
parser.add_argument('--numWords',type=int,default=10)
parser.add_argument('--maxTuples',type=int,default=4)
parser.add_argument('--minWordLength',type=int,default=5)
parser.add_argument('file',type=str)
args = parser.parse_args()

# Inspired by http://stackoverflow.com/questions/6822725
def window(seq, n):
  it = iter(seq)
  result = tuple(islice(it, n))
  if len(result) == n:
    yield result
  for elem in it:
    result = result[1:] + (elem,)
    containsShortWord = False
    for i in result:
      if len(i) < args.minWordLength:
        containsShortWord = True
        break
    if not containsShortWord:
      yield result

with open(args.file,'r') as f:
  content = f.read().replace('\n',' ')
  words = re.findall(r'\S+', content)
  for i in range(1,args.maxTuples+1):
    print("\n=== Sliding Window: {} ===".format(i))
    for tup in Counter(window(words,i)).most_common(args.numWords):
      print("  {}: '{}'".format(tup[1]," ".join(tup[0])))
