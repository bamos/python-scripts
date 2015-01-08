#!/usr/bin/env python3
#
# Brandon Amos <http://bamos.github.io>
# 2015.01.08

import argparse
from collections import defaultdict
import re

def merge_files(contacts_filenames):
    contents = defaultdict(list)
    for filename in contacts_filenames:
        with open(filename,'r') as f:
            group = None
            for line in f.readlines():
                line = line.strip()
                if len(line) == 0:
                    continue
                r = re.search("^# (.*)$",line)
                if r:
                    group = r.group(1)
                else:
                    contents[group].append(line)
    for group in sorted(contents):
        print("# {}".format(group))
        print("\n".join(sorted(set(contents[group])))+"\n")

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('contacts_filenames', type=str, nargs='+')
    args = parser.parse_args()

    merge_files(args.contacts_filenames)
