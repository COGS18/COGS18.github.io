---
interact_link: content/materials/19-CodeStyle.ipynb
download_link: assets/downloads/19-CodeStyle.ipynb.zip
pdf_link: assets/pdf/19-CodeStyle.pdf
layout: materials
title: '19-CodeStyle'
prev_page:
  url: /materials/18-Documentation
  title: '18-Documentation'
next_page:
  url: /materials/20-CodeTesting
  title: '20-CodeTesting'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
## Course Announcements

- Final Project Due 6/12 (11:59 PM)
- E2 & A4 grades posted
- Calculating your final grade
    - Drop 2 (lowest) coding labs
    - Drop 1 of the "E1" scores
    - Add up your points

#### COGS 18 Extra Credit Opportunities

- Final project to public GitHub repo (0.15 pts; 1% on project)
- Final project Extra Credit (0.6 pts; *up to* 4% on project)
- CAPEs response rate >= 85% (0.5 pts to everyone)
- End-of-Course Survey (0.25 pts) - not yet available

#### Clicker Question #1
Do you have an idea of what you want to do for your **project**?

- A) absolutely no idea
- B) some idea, but not sure
- C) sort of
- D) fairly good idea
- E) I know exactly what I want to do.

Example Final Projects: https://github.com/COGS18/Projects

#### Clicker Question #2

Your final project is a chatbot that will discuss sports with you. How would you implement this?

- A) Jupyter Notebook only
- B) module only 
- C) module + Jupyter Notebook
- D) script only
- E) script + Jupyter Notebook

# Code Style

- PEP8
- spacing
- line length
- comments

Or: How to be Pythonic

Reasons to be Pythonic:
- user friendly for humans
- extra work up-front on the developers (pays off on the long run)
- best to practice this early on (I promise!)

## Style Guides

<div class="alert alert-success">
Coding style refers to a set of conventions for how to write good code. 
</div>

Consistency is the goal. Rules help us achieve consistency.

Much of this will apply to other programming languages, so it's good to learn...regardless of language.

Some of these Code Style notes will be more specific to Python, however.

## The Zen of Python



{:.input_area}
```python
import this
```


{:.output_stream}
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

```

### Program Errors vs. Stylistic Issues

- Programmatic Error: something that breaks the code
- Stylistic Issue: something that doesn't break the code, but is considered bad style - makes your code harder to understand

## Picking a Style Guide

- Code style is (at least partly) subjective
- Consistency is key. It's easier to recognize & read consistent style

## Python Enhancement Proposals (PEPs)

<div class="alert alert-success">
Python PEPs are proposals for how something should be / work in the Python programming language. 
</div>

These are written by the people responsible for the Python Programming language.

PEP are voted on before incorporation.

## PEP8

<div class="alert alert-info">
<b><a href="https://www.python.org/dev/peps/pep-0008/">PEP8</a></b> is an accepted proposal that outlines the style guide for Python.
</div>

Defines the style guide for Pythonistas (people who code in Python).

## General Concepts

- Be Explicit & Clear
    - Prioritize Readability over 'Cleverness'
- There should be specific, standard ways to do things
    - Use them
- Coding Style are guidelines, designed to help the code
    - They are not laws

## Specific Guidelines - Structure

- blank lines
- indentaion
- spacing 
- length
- imports

### Blank Lines

- Use 2 blank lines between functions & classes, and 1 between methods
- Use 1 blank line between segments to indicate logical structure

This allows you to - at a glance - identify what pieces of code are there.



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
my_func()
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


Note that documentation here is missing (as are comments). This is to highlight the spacing. You'll need documentation and comments.

I promise it's better to comment as you go along rather than coming along after you've written all the code and adding comments.

Similar to writing: write comments -> write code -> review code & comments

#### Clicker Question #3

Which of these is best - A, B, or C?



{:.input_area}
```python
# Option A
def squared(input_number):
    val = input_number
    power = 2    
    output = val ** power
    return output
```




{:.input_area}
```python
# Option B
def squared(input_number, power=2):
    
    output = input_number ** power
    
    return output
```




{:.input_area}
```python
# Option C
def squared(input_number):
    
    val = input_number
    power = 2
    
    output = val ** power
    
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


{:.output_stream}
```
Words.

```



{:.input_area}
```python
# Goodness
if True:
    print('Words.')
```


{:.output_stream}
```
Words.

```

### Spacing

- Put one (and only one) space between each element
- Index and assignment don't have a space between opening & closing '()' or '[]'



{:.input_area}
```python
# Badnesses
my_var=1+2==3
my_list  =  [ 1,2,3,4 ]
el = my_list [1]
```




{:.input_area}
```python
# Goodnesses
my_var = 1 + 2 == 3
my_list = [1, 2, 3, 4]
el = my_list[1]
```


#### Clicker Question #4

Which of the following uses PEP-approved spacing?

- A) `my_list=[1,2,3,4,5]`
- B) `my_list = [1,2,3,4,5]`
- C) `my_list  =  [1, 2, 3, 4, 5]`
- D) `my_list=[1, 2, 3, 4, 5]`
- E) `my_list = [1, 2, 3, 4, 5]`

### Line Length

- PEP8 recommends that each line be at most 79 characters long

Computers used to require this.

But, super long lines are hard to read at a glance.

### One Statement Per Line

- While you *can* condense multiple statements into one line, you usually shouldn't.



{:.input_area}
```python
# Badness
for i in [1, 2, 3]: print(i**2 + i%2)
```


{:.output_stream}
```
2
4
10

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


Note: If you don't know how to import a local/custom module, figure that out this week in Coding Lab or office hours.

## Specific Guidelines - Naming

### Valid Names

- Use descriptive names for all modules, variables, functions and classes, that are longer than 1 character



{:.input_area}
```python
# Badness
a = 12
b = 24
```




{:.input_area}
```python
# Goodness
n_filters = 12
n_freqs = 24
```


Find + Replace also works better when you have specific variable names 

### Naming Style

- CapWords (leading capitals, no separation) for Classes
- snake_case (all lowercase, underscore separator) for variables, functions, and modules



{:.input_area}
```python
# Badness
def MyFunc():
    pass
    
class my_class():
    def __init__():
        pass
```




{:.input_area}
```python
# Goodness
def my_func():
    pass


class MyClass():
    def __init__():
        pass
```


Note: snake_case is easier to read than CapWords, so we use snake_case for the things (variables, functions) that we name more frequently.

#### Clicker Question #5

If you were reading code and came cross the following, which of the following would you expect to be a class?

- A) `Phillies_Game`
- B) `PhilliesGame`
- C) `phillies_game`
- D) `philliesgame`
- E) `PhIlLiEsGaMe`

#### Clicker Question #6

If you were reading code and came cross the following, which of the following would you expect to be a function or variable name?

- A) `Phillies_Game`
- B) `PhilliesGame`
- C) `phillies_game`
- D) `philliesgame`
- E) `PhIlLiEsGaMe`

### Indicating Scope

- Leading underscores indicate a 'private' attribute or method of the class, meaning it is an internal value, not expected to be accessed by the user.



{:.input_area}
```python
class MyClass():
    def __init__():
        self.public = None
        self._private = None
```


The leading underscore indicates to the user that this attribute shouldn't be changed/modified by the user.

`import *` will not import underscored attributes (private attributes).

## Specific Guidelines - String Quotes

In Python, single-quoted strings and double-quoted strings are the same. 

This PEP does not make a recommendation for this. **Pick a rule and stick to it.** 

When a string contains single or double quote characters: use the other one to avoid backslashes in the string. It improves readability.





{:.input_area}
```python
# Badness
my_string = 'Prof\'s Project'
```




{:.input_area}
```python
# Goodness
my_string = "Prof's Project"
```


#### Clicker Question #7

Which of the following would not cause an error in Python and would store the string *You're so close!*  ?

- A) `my_string = "You're so close!"`
- B) `my_string = "You"re so close!"`
- C) `my_string = 'You''re so close!'`
- D) `my_string = "You\\'re so close"`
- E) `my_string = 'You're so close!'`



{:.input_area}
```python
#my_string = "You're so close!"
#my_string = "You"re so close!"
#my_string = 'You''re so close!'
#my_string = "You\\'re so close!"
#my_string = 'You're so close!'
#my_string
```


## Specific Guidelines - Comments

Out-of-date comments are worse than no comments at all.

Keep your comments up-to-date.

#### Block comments
- apply to some (or all) code that follows them
- are indented to the same level as that code. 
- Each line of a block comment starts with a # and a single space



{:.input_area}
```python
# Badness
import random

def week_9():
# help try to destress students by picking one thing from the following list using random
    statements = ["You've totally got this!","You're so close!","You're going to do great!","Remember to take breaks!","Sleep, water, and food are really important!"]
    out = random.choice(statements)
    return out

week_9()
```





{:.output_data_text}
```
"You're so close!"
```





{:.input_area}
```python
# Goodness
def week_9():
    
    # Randomly pick from list of de-stressing statements
    # to help students as they finish the quarter.
    statements = ["You've totally got this!", 
                  "You're so close!", 
                  "You're going to do great!",
                  "Remember to take breaks!",
                  "Sleep, water, and food are really important!"]
    
    out = random.choice(statements)
    
    return out

week_9()
```





{:.output_data_text}
```
"You're going to do great!"
```



#### Inline comments
- to be used sparingly
- to be separated by at least two spaces from the statement
- start with a # and a single space



{:.input_area}
```python
# Badness
week_9()#words of encouragement
```





{:.output_data_text}
```
"You've totally got this!"
```





{:.input_area}
```python
# Goodness
week_9()  # words of encouragement
```





{:.output_data_text}
```
'Remember to take breaks!'
```



## Specific Guidelines - Documentation

- Write a descriptive docstring for all functions & classes

Note: If you're borrowing functions from an assignment, you should add documentation to these functions.

Comments within the functions you've borrowed noting that you've borrowed it as well as a general note in your project description will suffice for attribution.

If you've modified/edited the code from the assignment, state that you modified.

## Linters

<div class="alert alert-success">
A linter is a tool that analyzes code for both programmatic errors and stylistic issues. 
</div>

`pylint` is available from Anaconda to check this for you. (Not available on datahub.)

#### Clicker Question #8

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


- A) None
- B) 1 or 2 
- C) 3 or 4 
- D) 5 or 6
- E) 7 or more

# list here
- not readable for humans; not sure what it's supposed to do
- variable naming - improve
- function name - snake case
- spacing within list
- indentation - (red ind)
- line spacing
- general spacing overall



{:.input_area}
```python
# Let's fix this code
def my_function(input_num):
    
    my_list = [0, 1, 2, 3]
    if 1 in my_list: 
        ind = 1
    else:
        ind = 0
        
    qq = []
    for i in my_list[ind:]:
        qq.append(input_num/i)
    
    return qq
```




{:.input_area}
```python
# check using pylint
!pylint linter_example.py
```


{:.output_stream}
```
************* Module linter_example
linter_example.py:2:0: C0303: Trailing whitespace (trailing-whitespace)
linter_example.py:3:16: C0326: Exactly one space required after comma
    my_list = [0,1,2,3]
                ^ (bad-whitespace)
linter_example.py:3:18: C0326: Exactly one space required after comma
    my_list = [0,1,2,3]
                  ^ (bad-whitespace)
linter_example.py:3:20: C0326: Exactly one space required after comma
    my_list = [0,1,2,3]
                    ^ (bad-whitespace)
linter_example.py:6:0: W0311: Bad indentation. Found 6 spaces, expected 8 (bad-indentation)
linter_example.py:8:21: C0326: No space allowed before bracket
    for i in my_list [ind:]:
                     ^ (bad-whitespace)
linter_example.py:10:0: C0304: Final newline missing (missing-final-newline)
linter_example.py:1:0: C0111: Missing module docstring (missing-docstring)
linter_example.py:1:0: C0103: Function name "MyFunction" doesn't conform to snake_case naming style (invalid-name)
linter_example.py:1:0: C0111: Missing function docstring (missing-docstring)
linter_example.py:4:21: C0321: More than one statement on a single line (multiple-statements)
linter_example.py:7:4: C0103: Variable name "qq" doesn't conform to snake_case naming style (invalid-name)

------------------------------------
Your code has been rated at -3.33/10


```
