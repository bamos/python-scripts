#!/usr/bin/env python3

__author__ = ['[Brandon Amos](http://github.com/bamos)']
__date__ = '2015.03.27'

"""
Generates the README for
[bamos/python-scripts](https://github.com/bamos/python-scripts).
Script descriptions are obtained by parsing the docstrings.
"""

import ast
import glob
import os
from jinja2 import Template
from subprocess import Popen, PIPE

readme = Template("""
[![Build Status](https://travis-ci.org/bamos/python-scripts.svg)](https://travis-ci.org/bamos/python-scripts)
[![Dependency Status](https://gemnasium.com/bamos/python-scripts.svg)](https://gemnasium.com/bamos/python-scripts)

This is a collection of short Python scripts use in Linux.
I have these added to my `PATH`
[variable](https://wiki.archlinux.org/index.php/Environment_variables)
to run from anywhere.
The script contents in this README have been
[automatically generated](https://github.com/bamos/python-scripts#generate-readmepy).

# Adding to your PATH
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
to ensure `requirements.txt` has all of the Python 2 and Python 3 scripts
and that there are no careless errors.
[pep8](https://github.com/jcrocholl/pep8) will fail the build
pep8 styling conventions aren't met.

# Scripts
{{descriptions}}

# Similar Projects
There are many potpourri Python script repositories on GitHub.
The following list shows a short sampling of projects,
and I'm happy to merge pull requests of other projects.

{{similar_projects}}
""")


def get_docstr(filename):
    print("  + get_docstr({})".format(filename))
    with open(filename) as f:
        script = ast.parse(f.read())
        try:
            authors, date, desc = map(lambda x: ast.literal_eval(x.value),
                                      script.body[0:3])
        except:
            print("    + Error reading (author, date, desc).")
            raise
        return """
## [{}](https://github.com/bamos/python-scripts/blob/master/{})
+ Authors: {}
+ Created: {}

{}
""".format(filename, filename, ", ".join(authors), date, desc)


def get_descriptions():
    print("# Getting project descriptions")
    return ("\n".join(map(get_docstr,
                          ['generate-readme.py'] + glob.glob("python*/*.py"))))


def get_similar_projects():
    print("# Getting similar projects")
    projs = ['gpambrozio/PythonScripts',
             'ClarkGoble/Scripts',
             'gpambrozio/PythonScripts',
             'realpython/python-scripts',
             'averagesecurityguy/Python-Examples',
             'computermacgyver/twitter-python']
    cmd = ['./python3/github-repo-summary.py'] + projs
    p = Popen(cmd, stdout=PIPE)
    out, err = p.communicate()
    return out.decode()


if __name__ == '__main__':
    # cd into the script directory.
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    with open("README.md", "w") as f:
        f.write(readme.render(
            descriptions=get_descriptions(),
            similar_projects=get_similar_projects()
        ))
