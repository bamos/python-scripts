#!/usr/bin/env python3

import argparse
import re
from subprocess import Popen,PIPE

parser = argparse.ArgumentParser()
parser.add_argument('files',type=str, nargs='+')
args = parser.parse_args()

def call(cmd,in_f=None):
  if in_f:
    with open(in_f,'r') as f:
      p = Popen(cmd,stdout=PIPE,stderr=PIPE,stdin=f)
  else:
    p = Popen(cmd,stdout=PIPE,stderr=PIPE)
  out = p.communicate()[0].decode()
  if p.returncode != 0:
    raise Exception("Error running {}".format(cmd))
  return out

def getNumWriteGoodSuggestions(f_name):
  out = call(["write-good",f_name])
  return out.count("-------------")

def getNumDictionSuggestions(f_name):
  out = call(["diction","--suggest",f_name])
  r = re.search("(\S*) phrases? in (\S*) sentences? found.",out)
  if r:
    if r.group(1) == "No":
      return 0
    else:
      return int(r.group(1))

def getNumAspellSuggestions(f_name):
  out = call(["aspell","list"],in_f=f_name)
  return len(out.split())

def getSuggestions(f_name):
  suggestions = [
    getNumDictionSuggestions(f_name),
    getNumWriteGoodSuggestions(f_name),
    getNumAspellSuggestions(f_name)
  ]
  return (sum(suggestions), suggestions, f_name)

for tup in sorted(map(getSuggestions,args.files),reverse=True):
  print("\n=== {} ===".format(tup[2]))
  print("  Total: {}".format(tup[0]))
  print("  ├── diction: {}".format(tup[1][0]))
  print("  ├── write-good: {}".format(tup[1][1]))
  print("  └── aspell: {}".format(tup[1][2]))
