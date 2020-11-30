# Open Source

- Open Source Software
- History of Python
- Zen of Python
- GitHub
- PyPI, PIP, Conda

**Note** We are skipping the vast majority of the notes included in this one, to spend more time on code style, documentation, etc. But, I wanted you to have them for your reference!

This I'm covering during lecture:
- Zen of Python (briefly)
- Package Installation

<div class="alert alert-success">
Open source software is software for which the source code is openly available.
</div>

The Source Code for Python (which is actually written in C) is all available.

Open Source Software is free. (free = freedom)

Open source software is software that the user can:

- use and install the software
- view the source code of the project
- distribute the software
- change the source code of the project

Scientific research is often done in an exclusively open source environment.

## Aside: Brief History of Python

First conceptualized by **Guido van Rossum** in the late 1980s: 
- ABC is a general-pupose programming language that influenced Python
- goal: simple scripting language
    - basic syntax
    - indentation rather than cruly braces or begin-end blocks
    - developed certain data types (dictionary, list, strings, numbers)
- he was the BDFL (benevolent dictator for life) until July 2018

### Basic Timeline
- 1991: Python 0.9.0 was first released 
- 1994: Python 1.0 (lambda, map, filter, and reduce)
- 2000: Python 2.0 (list comprehensions, full garbage collector, supported unicode)
- 2008: Python 3.0 released (print function; not backwards-compatible, fulfilling the 13th law of the Zen of Python)

### For Context:

- 1842: Ada Lovelace - first published computer program
- 1940s: first high level programming language
- 1956: FORTRAN - first commercially available
- 1972: C
- 1980s: Consolidation, modules, & performance
    - 1987: Perl
- 1990s: Age of the Internet
    - 1991: Python
    - 1993: R
    - 1995: Java

### Zen of Python

- 20 guidelines (the 20th is missing)
- sometimes contradictory in favor of flexibility

# a hidden easter egg
import this

Tim Peters -- the author of the Zen of Python -- is a software developer and was a major contributor to the Python Programming language.

#### Clicker Question #1

Read through and think about the statements in the Zen of Python Which do you think is the most important? 

The one I think is most important is in...

- A) 1-5
- B) 6-10
- C) 11-15
- D) 16-19
- E) ¯\\_(ツ)_\/¯

### Beautiful is better than ugly. Readability counts.

- readability prioritized
- Python prides itself on ease to work with
- code is read more often than it's written
- documentation matters.

### Simple is better than complex. Complex is better than complicated.

- There's more than one approach to solving a problem
- Something that is overly-complicated should be reconsidered - a different approach? A simpler solution?

### There should be one - and preferably only one - obvious way to do it

- A slight shot at other programming languages
- With more than one way, reading is harder and writing is easier. Flexibility not worth it to Pythonistas.

### Namespaces are one honking great idea - let's do more of those

- Namespaces and global/local scopes prevent names in one module/scope from conflicting with names in another
- Namespaces are for avoiding naming conflicts (_not_ unecessary categorization - b/c flat is better than nested)

## A Final Note 

The Zen of Python is a set of guidelines for Python.

There are arguments for and against any of these.

Different languages take different approaches.

Language Wars are stupid.

**Fun fact**: Python is named after the British TV show Monty Python (not the snake).



## Licenses

<div class="alert alert-success">
The details of how an open-source project can be used are detailed in its `license`, which explicitly states its terms of use. 
</div>

- Open Source projects still have a license:
    - sometimes it says: go do whatever you want with this
    - other times it says: if you're not a company/going to make money, you can use this
    - and other times it says: you can use it but you have to attribute the original developers

## Open Source Developers

<div class="alert alert-success">
Open source software is often developed in an collaborative, public manner, through open collaboration.
</div>

Many are community-driven:
- open, public, & collaborative
- `pandas` was intially written by Wes McKinney

https://soundcloud.com/dataframed/data-science-tool-building

How open source packages are maintained and updated:
- support from foundations
- grant funding
- out of the kindness of individual's or the community's heart(s)

## Software Management & Distribution

- Jupyter
- GitHub
- PyPI
- PIP
- Conda

## Aside: Project Jupyter

- Spun off from IPython in 2014 (Fernando Perez)
- originally called "IPython Notebooks" (this is where .ipynb comes from)
- intended for use by those who program in Julia, Python, and R 
- developed to support those who use interactive computing

This document (.ipynb) IS a JSON document
- {'key' : 'value'}
- nested & hierarchical
- operating unit is the cell (Markdown, code, LaTeX, ...)

### IPython

- Interactive Python
- Initial release: 2001
- Command Shell for interactive computing in the shell

- 1991: Python 0.9.0 was first released 
- 1994: Python 1.0 (lambda, map, filter, and reduce)
- 2000: Python 2.0 (list comprehensions, full garbage collector, supported unicode)
- 2001: IPython released
- 2008: Python 3.0 released (print function; not backwards-compatible, fulfilling the 13th law of the Zen of Python)
- 2014: Jupyter notebooks spun off

### GitHub

<div class="alert alert-success">
<b>GitHub</b> is a software development platform, which is used to host and develop open source projects.
</div>

Similar to Dropbox or Google Drive...but for code.

## Benefits of GitHub

- Share code
- Work collaboratively
- See others' code 
- Contribute to others' code

<div class="alert alert-info">
If you create a GitHub account and add your final project to a public repository on GitHub, you will receive extra credit on your final project.
</div>

But...what if you just want to _use_ what's available to you in Python...

### PyPI: Python Package Index

<div class="alert alert-success">
The Python Package Index is a software repository for the Python programming language.
</div>

Where packages are hosted. You can search and use packages from Python.

### PIP: Python Installer

<div class="alert alert-success">
PIP is a Python tool for installing Python packages. 
</div>

It searches PyPi for you and allows you to install new python packages from the terminal.

The format for this is:

`pip install package_name`

On Datahub, you have to use the `--user` flag

`pip install --user package_name`


# for example 
!pip install neruodsp

### Dependencies

<div class="alert alert-success">
Packages can have dependencies on each other, meaning they require (use) other packages to work.
</div>

## A Note on Conda

<div class="alert alert-success">
Conda is a package management and environment management system. 
</div>

`pip` manages single installs. `Conda` manages the whole system / environment and interactions between packages.