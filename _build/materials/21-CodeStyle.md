---
interact_link: content/materials/21-CodeStyle.ipynb
download_link: assets/downloads/21-CodeStyle.ipynb.zip
pdf_link: assets/pdf/21-CodeStyle.pdf
layout: materials
title: '21-CodeStyle'
prev_page:
  url: /materials/20-Documentation
  title: '20-Documentation'
next_page:
  url: /materials/22-CodeTesting
  title: '22-CodeTesting'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Code Style

Or: How to be Pythonic

## Style Guides

<div class="alert alert-success">
Coding style refers to a set of conventions for how to write good code. 
</div>

## The Zen of Python



{:.input_area}
```python
import this
```


### Program Errors vs. Stylistic Issues

- Programmatic Error: something that breaks the code
- Stylistic Issue: something that doesn't break the code, but is considered bad style

## Picking a Style Guide

- Code style is (at least partly) subjective
- Consistency is key. It's easier to recognize & read consistent style

## Python Enhancement Proposals

<div class="alert alert-success">
Python `PEP`'s are proposals for how something should be / work in the Python programming language. 
</div>

## PEP8

<div class="alert alert-info">
[PEP8](https://www.python.org/dev/peps/pep-0008/) is an accepted proposal that outlines the style guide for Python.
</div>

## General Concepts

- Be Explicit & Clear.
    - Prioritize Readability over 'Cleverness'
- There should be specific, standard ways to do things.
    - Use them
- Coding Style are guidelines, designed to help the code.
    - They are not laws

## Specific Guidelines - Structure

### Blank Lines

- Use 2 blank lines between functions & classes, and 1 between methods
- Use 1 blank line between segments to indicate logical structure



{:.input_area}
```python
# Badness
def my_func():
    my_nums = '123'
    output = ''
    for num in my_nums:
        output += str(int(num) + 1)
    return output
```




{:.input_area}
```python
# Goodness
def my_func():
    
    my_nums = '123'
    output = ''
    
    for num in my_nums:
        output += str(int(num) + 1)
    
    return output
```


### Indentation

Use spaces to indicate indentation levels, with each level defined as 4 spaces. 



{:.input_area}
```python
# Badness
if True:
  print('Words.')
```




{:.input_area}
```python
# Goodness
if True:
    print('Words.')
```


### Spacing

- Put one (and only one) space between each element
- Index and assignment don't have a space between opening & closing '()' or '[]'



{:.input_area}
```python
# Badnesses
my_var=1+2==3
my_list = [1,2,3,4]
el = my_list [1]
```




{:.input_area}
```python
# Goodnesses
my_var = 1 + 2 == 3
my_list = [1, 2, 3, 4]
el = my_list[1]
```


### Line Length

- PEP8 recommends that each line be at most 79 characters long

### One Statement Per Line

- While you 'can' condense multiple statements into one line, you usually shouldn't.



{:.input_area}
```python
# Badness
for i in [1, 2, 3]: print(i**2 + i%2)
```




{:.input_area}
```python
# Goodness
for i in [1, 2, 3]:
    print(i**2 + i%2)
```


### Multi-Line



{:.input_area}
```python
my_long_list = [1, 2, 3, 4, 5,
                6, 7, 8, 9, 10]
```




{:.input_area}
```python
# Note: you can explicitly indicate a new line with '\'
my_string = 'Python is ' + \
            'a pretty great language.'
```


### Imports

- Import one module per line
- Avoid `*` imports
- Use the import order: standard library; 3rd party packages; local / custom code



{:.input_area}
```python
# Badness
from numpy import *

import os, sys
```




{:.input_area}
```python
# Goodness
import os
import sys

import numpy as np
```


## Specific Guidelines - Naming

### Valid Names

- Use descriptive names for all modules, variables, functions and classes, that are longer than 1 character



{:.input_area}
```python
# Badnesses
a = 12
b = 24
```




{:.input_area}
```python
# Goodnesses
n_filters = 12
n_freqs = 24
```


### Naming Style

- CamelCase (leading capitals, no separation) for Classes
- snake_case (all lowercase, underscore separator) for variables, functions, and modules



{:.input_area}
```python
# Badnesses
def MyFunc():
    pass
    
class my_class():
    def __init__():
        pass
```




{:.input_area}
```python
# Goodnesses
def my_func():
    pass

class MyClass():
    def __init__():
        pass
```


### Indicating Scope

- Leading underscores indicate a 'private' attribute or method of the class, meaning it is an internal value, not expected to be accessed by the user.



{:.input_area}
```python
class MyClass():
    def __init__():
        self.public = None
        self._private = None
```


## Specific Guidelines - Documentation

- Write a descriptive docstring for all functions & classes

## Linters

<div class="alert alert-success">
A linter is a tool that analyzes code for both programmatic erros and stylistic issues. 
</div>

### Clicker Question #1

How many PEP8 violations can you find in this code?



{:.input_area}
```python
def MyFunction(input_num):
    
    my_list = [0,1,2,3]
    if 1 in my_list: ind = 1
    else:
      ind = 0
    qq = []
    for i in my_list [ind:]:
        qq.append(input_num/i)
    return qq
```


A) None | B) 1 or 2 | C) 3 or 4 | D) 5 or 6 | E) 7 or more



{:.input_area}
```python
# Let's fix this code
def MyFunction(input_num):
    
    my_list = [0,1,2,3]
    if 1 in my_list: ind = 1
    else:
      ind = 0
    qq = []
    for i in my_list [ind:]:
        qq.append(input_num/i)
    return qq
```

