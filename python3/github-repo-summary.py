#!/usr/bin/env python3
#
# Brandon Amos <http://bamos.io>
# 2014.11.02

from github import Github
import argparse
import time
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument('repos',nargs="+",type=str)
args = parser.parse_args()
github = Github(os.getenv("GITHUB_TOKEN"))

def sanitize_for_md(s):
  s = s.replace("*","\*")
  return s

print(
  "Generated on {}, see the Markdown source of this file for more details.\n".format(
    time.strftime("%Y-%m-%d")
  )
)
print("Name | Stargazers | Description")
print("|".join(["----"]*3))
for r_name in sorted(args.repos, key=lambda v: v.upper()):
  try:
    r = github.get_repo(r_name)
  except:
    print("Error: Repository '{}' not found.".format(r_name),file=sys.stderr)
    sys.exit(-1)
  content = " | ".join([
    "[{}]({})".format(r.full_name,r.html_url),
    str(r.stargazers_count),
    sanitize_for_md(r.description)
  ])
  print(content)
