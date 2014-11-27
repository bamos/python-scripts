This is a collection of short Python scripts I have added to my
`PATH` variable to run from anywhere.
None are currently available in [pip][pip],
but I will add them if enough people are interested.

To add these to your `PATH`, clone the repo and add the following
to your `bashrc` or `zshrc`, replacing `<python-scripts>`
with the location of the cloned repository.
Furthermore, see my [dotfiles][dotfiles] repo for my
complete Mac and Linux system configurations.

```Bash
# Add additional directories to the path.
pathadd() {
  [ -d "$1" ] && [[ ":$PATH:" != *":$1:"* ]] && PATH="${PATH:+"$PATH:"}$1"
}

pathadd <python-scripts>/python2.7
pathadd <python-scripts>/python3
```

# Python 2.7
## music-organizer.py
This script organizes my music collection for iTunes
and [mpv][mpv] using tag information.
The directory structure is `<artist>/<track>`, where `<artist>` and `<track>`
are lower case strings separated by dashes.
See the [blog post][music-organizer-post] for a more detailed overview.

# Python 3
## EvalExpr.py
A module to evaluate a mathematical expression using Python's AST.
Tests are located in `EvalExprTest.py`.
See the [blog post][eval-post] for a more detailed overview.

```
$ EvalExpr.py '(((4+6)*10)<<2)'
(((4+6)*10)<<2) = 400
```

## github-repo-summary.py
Produces a Markdown table concisely summarizing a list of GitHub repositories.
See the [blog post][repo-summary-post] for a more detailed overview.
The following is an example from my [bamos/cv][cv] project.

```
$ github-repo-summary.py \
>   afriggeri/cv \
>   cies/resume \
>   deedydas/Deedy-Resume \
>   divad12/resume \
>   icco/Resume \
>   jsonresume/resume-schema \
>   kaeluka/cv \
>   mwhite/resume \
>   prat0318/json_resume \
>   qutebits/resume_42 \
>   raphink/CV \
>   sc932/resume \
>   terro/CV \
>   there4/markdown-resume \
>   zellux/resume

Generated on 2014-11-02, see the Markdown source of this file for more details.

Name | Stargazers | Description
----|----|----
[afriggeri/cv](https://github.com/afriggeri/cv) | 749 | CV, typesetted in Helvetica Neue, using XeTeX, TikZ and Biblatex
[cies/resume](https://github.com/cies/resume) | 184 | My resume as a PDF including the well commented Latex sources and build instructions.
[deedydas/Deedy-Resume](https://github.com/deedydas/Deedy-Resume) | 464 | A one page , two asymmetric column resume template in XeTeX that caters to an undergraduate Computer Science student
[divad12/resume](https://github.com/divad12/resume) | 22 | Yaml resume compiled into multiple formats (such as LaTeX, HTML (TODO), etc.)
[icco/Resume](https://github.com/icco/Resume) | 212 | A markdown port of my resume
[jsonresume/resume-schema](https://github.com/jsonresume/resume-schema) | 303 | JSON-Schema is used here to define and validate our proposed resume json
[kaeluka/cv](https://github.com/kaeluka/cv) | 64 | My CV.
[mwhite/resume](https://github.com/mwhite/resume) | 528 | Markdown -> PDF/HTML resumé generator
[prat0318/json_resume](https://github.com/prat0318/json_resume) | 1002 | Generates pretty HTML, LaTeX, markdown, with biodata feeded as input in JSON
[QuteBits/resume_42](https://github.com/QuteBits/resume_42) | 2 | It generates a beautiful resume from yaml data
[raphink/CV](https://github.com/raphink/CV) | 45 | My CV
[sc932/resume](https://github.com/sc932/resume) | 294 | My CV/resume in LaTeX.
[terro/CV](https://github.com/terro/CV) | 17 | My cv template
[there4/markdown-resume](https://github.com/there4/markdown-resume) | 353 | Generate a responsive CSS3 and HTML5 resume with Markdown, with optional PDF output.
[zellux/resume](https://github.com/zellux/resume) | 88 | My resume, generated with moderncv
```

Generated on 2014-11-02, see the Markdown source of this file for more details.

Name | Stargazers | Description
----|----|----
[afriggeri/cv](https://github.com/afriggeri/cv) | 749 | CV, typesetted in Helvetica Neue, using XeTeX, TikZ and Biblatex
[cies/resume](https://github.com/cies/resume) | 184 | My resume as a PDF including the well commented Latex sources and build instructions.
[deedydas/Deedy-Resume](https://github.com/deedydas/Deedy-Resume) | 464 | A one page , two asymmetric column resume template in XeTeX that caters to an undergraduate Computer Science student
[divad12/resume](https://github.com/divad12/resume) | 22 | Yaml resume compiled into multiple formats (such as LaTeX, HTML (TODO), etc.)
[icco/Resume](https://github.com/icco/Resume) | 212 | A markdown port of my resume
[jsonresume/resume-schema](https://github.com/jsonresume/resume-schema) | 303 | JSON-Schema is used here to define and validate our proposed resume json
[kaeluka/cv](https://github.com/kaeluka/cv) | 64 | My CV.
[mwhite/resume](https://github.com/mwhite/resume) | 528 | Markdown -> PDF/HTML resumé generator
[prat0318/json_resume](https://github.com/prat0318/json_resume) | 1002 | Generates pretty HTML, LaTeX, markdown, with biodata feeded as input in JSON
[QuteBits/resume_42](https://github.com/QuteBits/resume_42) | 2 | It generates a beautiful resume from yaml data
[raphink/CV](https://github.com/raphink/CV) | 45 | My CV
[sc932/resume](https://github.com/sc932/resume) | 294 | My CV/resume in LaTeX.
[terro/CV](https://github.com/terro/CV) | 17 | My cv template
[there4/markdown-resume](https://github.com/there4/markdown-resume) | 353 | Generate a responsive CSS3 and HTML5 resume with Markdown, with optional PDF output.
[zellux/resume](https://github.com/zellux/resume) | 88 | My resume, generated with moderncv

## link-checker.py
Builds upon linkchecker to hide warnings and to send a concise email
if bad links are found.
See the [blog post][link-checker-post] for a more detailed overview.

![Link checker screenshot](https://raw.githubusercontent.com/bamos/python-scripts/master/link-checker-screenshot.png?raw=true)

## merge-pdfs-printable.py
The printers in my office print a cover page before every job,
and I don't like printing many cover pages if I want to submit
multiple papers separately so that the papers don't overlap.
This script will merge PDF documents and insert blank pages
so that the printed pages won't overlap documents.
The `modulo` option is helpful to print 2 PDF pages per physical
page side.

The script uses [PyPDF2][pypdf2] to merge the documents
and to extract the number of pages
in the input documents and [ghostscript][gs]
to create a blank PDF page.

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
`PyPDF2.utils.PdfReadError: file has not been decrypted`.
My current workaround solution is to run `pdf2ps` on
the PDF and then `ps2pdf` on the PS file.

## ScrapeCountries.py
Scraping HTML tables with HTMLParser.
Tests are located in `ScrapeCountriesTest.py`.
See the [blog post][country-post] for a more detailed overview.

```
$ ScrapeCountries.py 'http://www.nationsonline.org/oneworld/countries_of_the_world.htm' countries.tsv
Parsing countries of the world.
Using 5 columns overall and extracting columns (1, 2, 3, 4).
Finished extracting. Data written to 'countries.tsv'

$ head -n 1 countries.tsv
Afghanistan	Afghanistan	Afghanistan	South-Central Asia
```

## phonetic.py
Obtain the NATO phonetic alphabet representation from short phrases.

```
$ phonetic.py github
g - golf
i - india
t - tango
h - hotel
u - uniform
b - bravo
```

## word-counter.py
Count work frequencies within a file.

```
$ word-counter.py README.md


=== Sliding Window: 1 ===
  15: 'resume'
  9: 'python'
  8: 'using'
  8: 'markdown'
  6: 'scripts'
  6: 'latex,'
  5: 'script'
  5: 'pages'
  5: 'generated'
  5: '[blog'

=== Sliding Window: 2 ===
  5: 'detailed overview.'
  4: 'sliding window:'
  3: 'neue, using'
  3: 'pretty html,'
  3: 'blank pages.'
  3: 'computer science'
  3: 'science student'
  3: 'resumé generator'
  3: 'python scripts'
  3: 'description ----|----|----'

=== Sliding Window: 3 ===
  2: 'pretty html, latex,'
  2: 'undergraduate computer science'
  2: 'html, latex, markdown,'
  2: 'pdf/html resumé generator'
  2: 'computer science student'
  2: 'generates pretty html,'
  2: 'multiple formats (such'
  2: 'commented latex sources'
  2: 'might interest somebody'
  2: 'neue, using xetex,'

=== Sliding Window: 4 ===
  2: 'helvetica neue, using xetex,'
  2: 'pretty html, latex, markdown,'
  2: 'undergraduate computer science student'
  2: 'asymmetric column resume template'
  2: 'generates pretty html, latex,'
  1: 'a.pdf b.pdf c.pdf --modulo'
  1: ''blank pages. merged output''
  1: 'this is a collection'
  1: ''generates pretty html, latex,''
  1: ''asymmetric column resume template''
```


[country-post]: http://bamos.github.io/2013/05/03/scraping-tables-python/
[eval-post]: http://bamos.github.io/2013/08/07/python-expression-evaluator/
[link-checker-post]: http://bamos.github.io/2014/02/06/link-checker-crontab/
[music-organizer-post]: http://bamos.github.io/2014/07/05/music-organizer/
[repo-summary-post]: http://bamos.github.io/2014/11/02/github-repo-summary/

[mpv]: http://mpv.io/
[pip]: http://pip.readthedocs.org/en/latest/
[dotfiles]: https://github.com/bamos/dotfiles

[gs]: http://www.ghostscript.com/doc/current/Use.htm
[pypdf2]: https://github.com/mstamy2/PyPDF2

[cv]: https://github.com/bamos/cv

# Similar Projects
There are many potpourri Python script repositories on GitHub.
The following list shows a short sampling of projects,
and I'm happy to merge pull requests of other projects.

<!--
To generate the following list, install https://github.com/jacquev6/PyGithub
and download the `github-repo-summary.py` script from
https://github.com/bamos/python-scripts/blob/master/python3/github-repo-summary.py.
Please add projects to the list in the comment and in the table below.

github-repo-summary.py \
  gpambrozio/PythonScripts \
  ClarkGoble/Scripts \
  gpambrozio/PythonScripts \
  realpython/python-scripts \
  averagesecurityguy/Python-Examples \
  computermacgyver/twitter-python
-->

Generated on 2014-11-06, see the Markdown source of this file for more details.

Name | Stargazers | Description
----|----|----
[averagesecurityguy/Python-Examples](https://github.com/averagesecurityguy/Python-Examples) | 13 | Example scripts for common python tasks
[ClarkGoble/Scripts](https://github.com/ClarkGoble/Scripts) | 24 | My scripts - primarily using python and appscript
[computermacgyver/twitter-python](https://github.com/computermacgyver/twitter-python) | 31 | Simple example scripts for Twitter data collection with Tweepy in Python
[gpambrozio/PythonScripts](https://github.com/gpambrozio/PythonScripts) | 40 | A bunch of Python scripts I made and that might interest somebody else
[gpambrozio/PythonScripts](https://github.com/gpambrozio/PythonScripts) | 40 | A bunch of Python scripts I made and that might interest somebody else
[realpython/python-scripts](https://github.com/realpython/python-scripts) | 29 | because i'm tired of gists
