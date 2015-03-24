#!/usr/bin/env python3
# 2014.10.17

"""The printers in my office print a cover page before every job, and
I don't like printing many cover pages if I want to submit multiple
papers separately so that the papers don't overlap. This script will
merge PDF documents and insert blank pages so that the printed pages
won't overlap documents. The modulo option is helpful to print 2 PDF
pages per physical page side.

The script uses PyPDF2 to merge the documents and to extract the
number of pages in the input documents and ghostscript to create a
blank PDF page.

    $ merge-pdfs-printable.py a.pdf b.pdf c.pdf --modulo 4
    a.pdf
     + Pages: 6
     + Added 2 blank pages.
    b.pdf
     + Pages: 13
     + Added 3 blank pages.
    c.pdf
     + Pages: 13
     + Added 3 blank pages.
    Merged output is in '/tmp/tmpm2n5g0mh-merge.pdf'.

Note: Some of my decrypted PDF documents have resulted in
PyPDF2.utils.PdfReadError: file has not been decrypted. My current
workaround solution is to run pdf2ps on the PDF and then ps2pdf on the
PS file.
"""

__author__ = ['Brandon Amos <http://bamos.github.io>']

import argparse
import os
import re
import subprocess
import tempfile

from PyPDF2 import PdfFileMerger,PdfFileReader

# Make sure executables are in PATH.
executables_used = ['ps2pdf']
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
  with open(f_path,'rb') as f:
    fr = PdfFileReader(f)
    return fr.numPages

def merge_pdfs(f_names):
  merger = PdfFileMerger()
  fps = [open(f,'rb') for f in f_names]
  for f in fps:
    try:
      merger.append(f)
    except:
      print("Error merging {}".format(f))
      raise
  out_file = "merged.pdf" #tempfile.mktemp("-merge.pdf")
  with open(out_file,'wb') as f:
    merger.write(f)
  [f.close() for f in fps]
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
    if args.modulo != 0 and pages % args.modulo != 0:
      result_f_names = result_f_names + [blank_file]*(args.modulo-pages%args.modulo)
      print(" + Added {} blank pages.".format(args.modulo-pages%args.modulo))

  merge_pdfs(result_f_names)
