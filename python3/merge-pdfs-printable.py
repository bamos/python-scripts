#!/usr/bin/env python3
#
# Brandon Amos <http://bamos.github.io>
# 2014.10.17

import argparse
import os
import re
import subprocess
import tempfile

# Make sure executables are in PATH.
executables_used = ['ps2pdf', 'gs', 'pdfinfo']
def exe_exists(program):
  def is_exe(fpath): return os.path.isfile(fpath) and os.access(fpath, os.X_OK)
  for path in os.environ["PATH"].split(os.pathsep):
    path = path.strip('"')
    exe_file = os.path.join(path, program)
    if is_exe(exe_file): return
  raise Exception("Unable to find program on PATH: '{}'.".format(program))
[exe_exists(e) for e in executables_used]

def create_blank_pdf(f_path):
  with open(f_path, 'w'):
    os.utime(f_path)
  p = subprocess.Popen(['ps2pdf', '-sPAPERSIZE=letter', f_path, f_path])
  p.communicate()
  if p.returncode != 0:
    raise Exception("create_blank_pdf return code nonzero.")


def get_pages_in_pdf(f_path):
  p = subprocess.Popen(['pdfinfo', f_path],stdout=subprocess.PIPE)
  p_out = p.communicate()[0].decode()
  if p.returncode != 0:
    raise Exception("get_pages_in_pdf return code nonzero.")
  m = re.search('Pages: *(\d*)', p_out)
  if m: return int(m.group(1))
  else: raise Exception(
      "Error running 'pdfinfo' to get the number of pages in {}".format(
        f_path
      )
    )

def merge_pdfs(f_names):
  out_file = tempfile.mktemp("-merge.pdf")
  p = subprocess.Popen(['gs', '-dBATCH', '-dNOPAUSE', '-q', '-sDEVICE=pdfwrite',
    '-sOutputFile={}'.format(out_file)] + f_names)
  p.communicate()
  if p.returncode != 0:
    raise Exception("merge_pdfs return code nonzero.")
  print("Merged output is in '{}'.".format(out_file))

if __name__=='__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--modulo', type=int, default=2)
  parser.add_argument('pdf_files', type=str, nargs='+')
  args = parser.parse_args()

  blank_file = tempfile.mktemp("-merge.pdf")
  create_blank_pdf(blank_file)

  result_f_names = []
  for f_path in args.pdf_files:
    result_f_names.append(f_path)
    pages = get_pages_in_pdf(f_path)
    print(f_path)
    print(" + Pages: {}".format(pages))
    if pages % args.modulo != 0:
      result_f_names = result_f_names + [blank_file]*(args.modulo-pages%args.modulo)
    print(" + Added {} blank pages.".format(args.modulo-pages%args.modulo))

  merge_pdfs(result_f_names)
