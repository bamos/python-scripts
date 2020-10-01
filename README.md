
[![Build Status](https://travis-ci.org/bamos/python-scripts.svg)](https://travis-ci.org/bamos/python-scripts)
[![Dependency Status](https://gemnasium.com/bamos/python-scripts.svg)](https://gemnasium.com/bamos/python-scripts)

This is a collection of short Python scripts I use in Linux.
Portions of this README are automatically generated with
[generate-readme.py](https://github.com/bamos/python-scripts#generate-readmepy)
to insert the script-level comments as descriptions below.

# Adding to your PATH
I have these added to my `PATH`
[variable](https://wiki.archlinux.org/index.php/Environment_variables)
to run from anywhere.
Clone the repo and add the following
to your `bashrc` or `zshrc`, replacing `<python-scripts>`
with the location of the cloned repository.
See my [dotfiles](https://github.com/bamos/dotfiles)
repo for my complete Mac and Linux system configurations.

```Bash
# Add additional directories to the path.
pathadd() {
  [ -d "$1" ] && [[ ":$PATH:" != *":$1:"* ]] && PATH="${PATH:+"$PATH:"}$1"
}

pathadd <python-scripts>/python2.7
pathadd <python-scripts>/python3
```

# Dependencies
These scripts are written in Python 3 except when external
libraries don't support Python 3.
Dependencies for Python 2 and 3 for all scripts are
included in `requirements-{2,3}.txt` and can be installed
using `pip` with `pip3 install -r requirements-3.txt`.

# Travis CI
Continuous integration is provided by Travis CI
[here](https://travis-ci.org/bamos/python-scripts).
[.travis.yml](https://github.com/bamos/python-scripts/blob/master/.travis.yml)
calls
[.travis-script-2.sh](https://github.com/bamos/python-scripts/blob/master/.travis-script-2.sh)
and
[.travis-script-3.sh](https://github.com/bamos/python-scripts/blob/master/.travis-script-3.sh)
to ensure `requirements-{2,3}.txt` have all of the Python 2 and Python 3 scripts
and that there are no careless errors that cause the scripts to
not execute the help message.
[pep8](https://github.com/jcrocholl/pep8) will fail the build
if pep8 styling conventions aren't met.

# Scripts
The subheadings link to the script contents on GitHub.


## [generate-readme.py](https://github.com/bamos/python-scripts/blob/master/generate-readme.py)
+ Authors: [Brandon Amos](http://bamos.github.io)
+ Created: 2015.03.27


Generates the README for
[bamos/python-scripts](https://github.com/bamos/python-scripts)
so that the README and scripts contain synchronized documentation.
Script descriptions are obtained by parsing the docstrings
and inserted directly into the README as markdown.



## [python2.7/music-organizer.py](https://github.com/bamos/python-scripts/blob/master/python2.7/music-organizer.py)
+ Authors: [Brandon Amos](http://bamos.github.io)
+ Created: 2014.04.19


This script (music-organizer.py) organizes my music collection for
iTunes and [mpv](http://mpv.io) using tag information.
The directory structure is `<artist>/<track>`, where `<artist>` and `<track>`
are lower case strings separated by dashes.

See my blog post
[Using Python to organize a music directory](http://bamos.github.io/2014/07/05/music-organizer/)
for a more detailed overview of this script.



## [python2.7/mt.py](https://github.com/bamos/python-scripts/blob/master/python2.7/mt.py)
+ Authors: [Brandon Amos](http://bamos.github.io)
+ Created: 2014.11.30


This script implements the simple
[multitail](https://pypi.python.org/pypi/multitail)
example to tail multiple files and append the filename to the beginning
of the output.



## [python2.7/caffe-compute-image-mean.py](https://github.com/bamos/python-scripts/blob/master/python2.7/caffe-compute-image-mean.py)
+ Authors: [Brandon Amos](http://bamos.github.io)
+ Created: 2015.08.10


This script computes the mean of a directory of images for Caffe.



## [python2.7/fix-music-tags.py](https://github.com/bamos/python-scripts/blob/master/python2.7/fix-music-tags.py)
+ Authors: [Brandon Amos](http://bamos.github.io)
+ Created: 2015.12.30


This script (fix-music-tags.py) mass-removes unwanted music tags.



## [python3/github-repo-summary.py](https://github.com/bamos/python-scripts/blob/master/python3/github-repo-summary.py)
+ Authors: [Brandon Amos](http://bamos.github.io)
+ Created: 2014.11.02


Produces a Markdown table concisely summarizing a list of GitHub repositories.



## [python3/link-checker.py](https://github.com/bamos/python-scripts/blob/master/python3/link-checker.py)
+ Authors: [Brandon Amos](http://bamos.github.io)
+ Created: 2014.02.06


Script to be run by crontab to report broken links.

Builds upon linkchecker (Ubuntu: sudo apt-get install linkchecker)
to hide warnings and to send a concise email if bad links are found.

![Link checker screenshot](https://raw.githubusercontent.com/bamos/python-scripts/master/link-checker-screenshot.png?raw=true)



## [python3/phonetic.py](https://github.com/bamos/python-scripts/blob/master/python3/phonetic.py)
+ Authors: [Brandon Amos](http://bamos.github.io)
+ Created: 2014.02.14


Obtain the NATO phonetic alphabet representation from short phrases.

```
$ phonetic.py GitHub
g - golf
i - India
t - tango
h - hotel
u - uniform
b - bravo
```



## [python3/rank-writing.py](https://github.com/bamos/python-scripts/blob/master/python3/rank-writing.py)
+ Authors: [Brandon Amos](http://bamos.github.io)
+ Created: 2014.02.14


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



## [python3/get-osx-wallpaper.py](https://github.com/bamos/python-scripts/blob/master/python3/get-osx-wallpaper.py)
+ Authors: [Brandon Amos](http://bamos.github.io)
+ Created: 2015.03.25


This is a Python script that outputs the path of the current
OSX wallpaper.
This is helpful when the desktop wallpaper is randomized
across a large collection of pictures and you want to
delete the current wallpaper.


### Warning
+ This approach doesn't work with multiple monitors or virtual desktops.

### Tested On
+ OSX Yosemite 10.10.2 with a single desktop on a MBP.

### Usage
Ensure `db_path` and `wallpaper_dir` are correctly set below.

Assuming `get-osx-wallpaper.py` is on your path,
check the output with the following

```
$ get-osx-wallpaper.py
/Users/bamos/Pictures/wallpaper/nature/496.jpg
```

Please ensure this is correct before trying to remove it!

This can be paired with other commands such as `open` or `rm`.
Run `killall Dock` to refresh the changes after removing the file.
Note that the dock will be restarted and all windows will be
unminimized.

```
$ open $(get-osx-wallpaper.py)
$ rm $(get-osx-wallpaper.py) && killall Dock
```

Example alias definitions for bash and zsh are available in
https://github.com/bamos/dotfiles/blob/master/.funcs:

```
alias open-wallpaper='open $(get-osx-wallpaper.py)'
alias rm-wallpaper='rm $(get-osx-wallpaper.py) && killall Dock'
```



## [python3/merge-pdfs-printable.py](https://github.com/bamos/python-scripts/blob/master/python3/merge-pdfs-printable.py)
+ Authors: [Brandon Amos](http://bamos.github.io)
+ Created: 2014.10.17


The printers in my office print a cover page before every job, and
I don't like printing many cover pages if I want to submit multiple
papers separately so that the papers don't overlap. This script will
merge PDF documents and insert blank pages so that the printed pages
won't overlap documents. The modulo option is helpful to print 2 PDF
pages per physical page side.

The script uses PyPDF2 to merge the documents and to extract the
number of pages in the input documents and ghostscript to create a
blank PDF page.

```
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
```

Note: Some of my decrypted PDF documents have resulted in
PyPDF2.utils.PdfReadError: file has not been decrypted. My current
workaround solution is to run pdf2ps on the PDF and then ps2pdf on the
PS file.



## [python3/remove-duplicates.py](https://github.com/bamos/python-scripts/blob/master/python3/remove-duplicates.py)
+ Authors: [Brandon Amos](http://bamos.github.io)
+ Created: 2015.06.06


Detect and remove duplicate images using average hashing.

http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html



## [python3/word-counter.py](https://github.com/bamos/python-scripts/blob/master/python3/word-counter.py)
+ Authors: [Brandon Amos](http://bamos.github.io)
+ Created: 2014.11.7


Count work frequencies within a file.

```
$ word-counter.py shakespeare.md --numWords 4 --maxTuples 3

=== Sliding Window: 1 ===
    3473: 'shall'
    2238: 'would'
    2153: 'which'
    2074: 'their'

=== Sliding Window: 2 ===
    248: 'exeunt scene'
    117: 'second lord.'
    105: 'first lord.'
    102: 'queen elizabeth.'

=== Sliding Window: 3 ===
    36: 'william shakespeare dramatis'
    34: 'shakespeare dramatis personae'
    18: 'comes here? enter'
    14: 'duke's palace enter'
```



## [python3/eval-expr.py](https://github.com/bamos/python-scripts/blob/master/python3/eval-expr.py)
+ Authors: J. Sebastian, [Brandon Amos](http://bamos.github.io)
+ Created: 2013.08.01


A module to evaluate a mathematical expression using Python's AST.

+ Original by: J. Sebastian at http://stackoverflow.com/questions/2371436.
+ Modifications by: [Brandon Amos](http://bamos.github.io).

If you want a command-line expression evaluator, use
[Russell91/pythonpy](https://github.com/Russell91/pythonpy).


```
$ eval-expr.py '(((4+6)*10)<<2)'
(((4+6)*10)<<2) = 400
```



## [python3/merge-mutt-contacts.py](https://github.com/bamos/python-scripts/blob/master/python3/merge-mutt-contacts.py)
+ Authors: [Brandon Amos](http://bamos.github.io)
+ Created: 2014.01.08


Merges two mutt contact files.



# Similar Projects
There are many potpourri Python script repositories on GitHub.
The following list shows a short sampling of projects,
and I'm happy to merge pull requests of other projects.

Name | Stargazers | Description
----|----|----
[averagesecurityguy/Python-Examples](https://github.com/averagesecurityguy/Python-Examples) | 26 | Example scripts for common python tasks
[ClarkGoble/Scripts](https://github.com/ClarkGoble/Scripts) | 29 | My scripts - primarily using python and appscript
[computermacgyver/twitter-python](https://github.com/computermacgyver/twitter-python) | 66 | Simple example scripts for Twitter data collection with Tweepy in Python
[gpambrozio/PythonScripts](https://github.com/gpambrozio/PythonScripts) | 38 | A bunch of Python scripts I made and that might interest somebody else
[realpython/python-scripts](https://github.com/realpython/python-scripts) | 568 | because i'm tired of gists
