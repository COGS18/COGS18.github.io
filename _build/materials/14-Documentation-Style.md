---
interact_link: content/materials/14-Documentation-Style.ipynb
download_link: assets/downloads/14-Documentation-Style.ipynb.zip
pdf_link: assets/pdf/14-Documentation-Style.pdf
layout: materials
title: '14-Documentation-Style'
prev_page:
  url: /materials/13-CommandLine
  title: '13-CommandLine'
next_page:
  url: /materials/15-OpenSource-API
  title: '15-OpenSource-API'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
## Course Announcements

**Due Dates**
- **CL5** due Wed (5/13)
- **A5** due *Friday* (not Thursday) (11:59 PM) 
- **Final Exam** Friday (due Sat 11 AM)

# Documentation & Style

- Documentation
    - readability
    - comments
    - documentation
- Style
    - PEP8
    - spacing
    - line length
    - comments

## Code Readability

"Code is more often read than written" - Guido van Rossum

So: code should be written to be readable by humans.

Note: one of those humans is future you.

### Writing Readable Code

So how do we write good code for humans?

- Use good structure
- Use good naming
- Use code comments and include documentation

### Good Structure

If you design your program using separate functions for each task, avoid copying + pasting (functions and loops instead), and consider structure beforehand, you'll be set up for success

### Good Naming

Clear names are for humans. The computer doesn't care, but you and others reading your code do.

### Code comments & Documentation

Helpful comments and documentation take your code to the next level. The final piece in the trifecta of readable code! 

Good code has good documentation - but code documentation should _not_ be used to try and fix unclear names, or bad structure. 

Rather, comments should add any additional context and information that helps explain what the code is, how it works, and why it works that way. 

#### Clicker Question #1

What does the following code do?



{:.input_area}
```python
def ff(jj):
    oo = list(); jj = list(jj) 
    for ii in jj: oo.append(str(ord(ii)))
    return '+'.join(oo)
ff('Hello World.')
```





{:.output_data_text}
```
'72+101+108+108+111+32+87+111+114+108+100+46'
```



- A) Returns unicode code points, as a list
- B) Encodes a string as a cypher, returning a string of alphabetical characters
- C) Returns unicode code points, as a string
- D) Encodes inputs alphabetical characters, returned as a list
- E) This code will fail

Improvement Considerations:
- Structural considerations: indentations & spacing
- Improved naming: functions & variables
- Add Comments within code



{:.input_area}
```python
str.join?
```




{:.input_area}
```python
# let's improve...
def return_unicode(input_list):
    string = list()
    input_list = list(input_list)
    
    # looping through to return unicode code point
    for character in input_list: 
        string.append(str(ord(character)))
        
    output_string = '+'.join(string)
    return output_string

return_unicode('Hello World.')
```





{:.output_data_text}
```
'72+101+108+108+111+32+87+111+114+108+100+46'
```



Improvement Considerations:
- Structural considerations: indentations & spacing
- Improved naming: functions & variables
- Add Comments within code
- **Proper Documentation!**



{:.input_area}
```python
# Let's fix this code!
def convert_to_unicode(input_string):
    """Converts an input string into a string containing the unicode code points.
    
    Parameters
    ----------
    input_string : string
        String to convert to code points
        
    Returns
    -------
    output_string : string
        String containing the code points for the input string.
    """ 
    
    output = list()
    # Converting a string to a list, to split up the characters of the string
    input_list = list(input_string)
    
    for character in input_list:   
        temp = ord(character)
        output.append(temp)

    output_string = '+'.join(output)
        
    return output_string
```


## Code Documentation

<div class="alert alert-success">
Code documentation is text that accompanies and/or is embedded within a software project, that explains what the code is and how to use it. 
</div>

Stuff written for humans in human language to help the humans.

## Code Comments vs. Documentation

#### Comments

Comments are string literals written directly in the code, typically directed at developers - people reading and potentially writing the code. 

#### Documentation

Documentation are descriptions and guides written for code users. 

## Inline Comments

Code comments should use `#`, and be written at the same indentation level of the code it describes. 

How to use comments:
- Generally:
    - focus on the *how* and *why*, over literal 'what is the code'
    - explain any context needed to understand the task at hand
    - give a broad overview of what approach you are taking to perform the task
    - if you're using any unusual approaches, explain what they are, and why you're using them
- Comments need to be maintained - make sure to keep them up to date

#### Bad Comments



{:.input_area}
```python
# This is a loop that iterates over elements in a list
for element in list_of_elements:
    pass
```


#### Good Comments



{:.input_area}
```python
# Because of X, we will use approach Y to do Z
for element in list_of_elements:
    # comment for code block
    pass
```


## Docstrings

<div class="alert alert-success">
<b>Docstrings</b> are in-code text that describe modules, classes and functions. They describe the operation of the code.
</div>

### Numpy style docs
[Numpy style docs](https://numpydoc.readthedocs.io/en/latest/format.html) are a particular specification for docstrings. 

### Example Docstring



{:.input_area}
```python
def add(num1, num2):
    """Add two numbers together. 
    
    Parameters
    ----------
    num1 : int or float
        The first number, to be added. 
    num2 : int or float
        The second number, to be added.
    
    Returns
    -------
    answer : float
        The result of the addition. 
    """
    
    answer = num1 + num2
    
    return answer
```


Docstrings

- multi-line string that describes what's going on
- starts and ends with triple quotes `"""`
- one sentence overview at the top - the task/goal of function
- **Parameters** : description of function arguments, keywords & respective types
- **Returns** : explanation of returned values and their types

**Docstrings** are available to you *outside* of the source code.

### Docstrings are available through the code



{:.input_area}
```python
add?
```




{:.input_area}
```python
# The `help` function prints out the `docstring` 
# of an object (module, function, class)
help(add)
```


{:.output_stream}
```
Help on function add in module __main__:

add(num1, num2)
    Add two numbers together. 
    
    Parameters
    ----------
    num1 : int or float
        The first number, to be added. 
    num2 : int or float
        The second number, to be added.
    
    Returns
    -------
    answer : float
        The result of the addition.


```

### `__doc__`



{:.input_area}
```python
# Docstrings get stored as the `__doc__` attribute
# can also be accessed from there
print(add.__doc__)
```


{:.output_stream}
```
Add two numbers together. 
    
    Parameters
    ----------
    num1 : int or float
        The first number, to be added. 
    num2 : int or float
        The second number, to be added.
    
    Returns
    -------
    answer : float
        The result of the addition. 
    

```



{:.input_area}
```python
# pull up source code for function
add??
```


#### Clicker Question #2

What should be included in a docstring?

1) Input arguments and their types  
2) A brief overview sentence about the code  
3) A copy of the `def` line  
4) Returned variables and their types  
5) A step by step description of the procedure used in the code  

- A) 1, 4 
- B) 2, 3, 5
- C) 3, 5 
- D) 1, 2, 4 
- E) 1, 2, 3, 4, 5

## Documentation for a Software Project

Documentation Files:
- A `README` is a file that provides an overview of the project to potential users and developers
- A `LICENSE` file specifies the license under which the code is available (the terms of use)
- An `API Reference` is a collection of the docstrings, listing public interfaces, parameters and return values
- Tutorials and/or Examples show examples and tutorials for using the codebase

## Documentation Sites

<div class="alert alert-success">
Documentation sites are a host of a package's documentation, for code users. 
</div>

### Example: Function Documentation
`numpy.array` :
https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html

### Example: Package Documentation
**scikit learn** (`sklearn`) : https://scikit-learn.org/stable/index.html

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





{:.output_data_text}
```
'234'
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


Note that documentation here is missing (as are comments). This is to highlight the spacing. You'll need documentation and comments on your final exam (will be specified in instructions).

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




{:.input_area}
```python
# Option D (added during lecture)
def squared(input_number, power=2):
    
    return input_number ** power
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




{:.input_area}
```python
my_function(input1=7, input2=8)
```




{:.input_area}
```python
def my_function(input1=6, input2=7):
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
my_string
```





{:.output_data_text}
```
'Python is a pretty great language.'
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
my_string = "You're so close!"
#my_string = "You"re so close!"
#my_string = 'You''re so close!'
# my_string = "You\\'re so close!"
#my_string = 'You're so close!'
my_string
```





{:.output_data_text}
```
"You're so close!"
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

def week_5():
# help try to destress students by picking one thing from the following list using random
    statements = ["You've totally got this!","You're so close!","You're going to do great!","Remember to take breaks!","Sleep, water, and food are really important!"]
    out = random.choice(statements)
    return out

week_5()
```





{:.output_data_text}
```
'Remember to take breaks!'
```





{:.input_area}
```python
# Goodness
def week_5():

    # Randomly pick from list of de-stressing statements
    # to help students as they finish the quarter.
    statements = ["You've totally got this!", 
                  "You're so close!", 
                  "You're going to do great!",
                  "Remember to take breaks!",
                  "Sleep, water, and food are really important!"]
    
    out = random.choice(statements)
    
    return out

week_5()
```





{:.output_data_text}
```
"You're so close!"
```



#### Inline comments
- to be used sparingly
- to be separated by at least two spaces from the statement
- start with a # and a single space



{:.input_area}
```python
# Badness
week_5()#words of encouragement
```





{:.output_data_text}
```
"You're so close!"
```





{:.input_area}
```python
# Goodness
week_5()  # words of encouragement
```





{:.output_data_text}
```
"You've totally got this!"
```



## Specific Guidelines - Documentation

- Write a descriptive docstring for all functions & classes

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

#### list here
- function naming (my_function); not be CapWords
- spacing in list
- line spacing between statements
- indentation (ind = 0)
- variable naming == poor (non-descrptive)
- conditional (if) all on a single line; should be separated
- spacing for indexing into `my_list`



{:.input_area}
```python
# Let's fix this code
# still missing documentation
def my_function(input_num):

    my_list = [0, 1, 2, 3]

    if 1 in my_list:
        ind = 1
    else:
        ind = 0

    out_list = []
    for i in my_list[ind:]:
        out_list.append(input_num/i)

    return out_list
```




{:.input_area}
```python
# check using pylint
!pylint linter_example.py
```


{:.output_stream}
```

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 8.89/10, +1.11)


```



{:.input_area}
```python
from linter_example import my_function
```




{:.input_area}
```python
my_function(2)
```





{:.output_data_text}
```
[2.0, 1.0, 0.6666666666666666]
```


