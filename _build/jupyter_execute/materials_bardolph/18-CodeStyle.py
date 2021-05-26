**Course Announcements**

- **CL8** due Wednesday
- **A5** due next Monday (5/31)

**Q&A**

Q: When you say we need to have 3 unit tests in our final project code, is it in a notebook or in separate py files and terminals?  
A: This will be a separate `.py` file

Q: Kinda hard to understand if we should create test files first before writing functions/methods  
A: Ideally, you should create your tests first; up to you what you do though

Q: One question remains for me is the very last part of lecture. Can we test whether our code is correct or not  in Jypternotebook by using the '.py' we create?  
A: Yup - this was asked after class - see end of Friday's lecture for example! 

Q: How are we able to create a test function when we haven't even written the function yet?  
A: Because you know what the function *should* do when it works. You've designed the inputs and what the function should return, so you should be able to `assert` things that will be `True` prior to actually writing the function and can include those tests within a test function.

Q: What does isinstance do? 
A: Checks that the variable specified in the first argument is of the type specified in the second.

Q: Why do we write a test in a separate module?  
A: By storing it in a standalone file, as you develop your project you can "run" your tests (using `pytest`) each time you add an additional function/method/class. Storing them separately facilitates this and keeps your code organized.

Q: When would one use a pytest if they could just include a unit test below the code they are attempting to test if both do the same thing and use the same code?  
A: `pytest` just speeds up the process of running your entire "test suite" for you with a single command. (See above answer about organization as well.)

Q: Do we use pytest only in a terminal?  
A: Nope - it can also be used from a notebook. Remember that any time you want to call a terminal command from a notebook, however, it will start with `!`.

Q: Do professional coders who use python utilize pytest or is it mostly for beginners?  
A: Professional coders absolutely write unit tests. Many use `pytest`, but there are a few testing modules in python...so some use a different one.

Q: In the exam, will there be specific commands on what should we write in the unit test?  
A: No, you will have to write the tests yourself (but you'll know the function/method you're testing and what/how it should work.

Q: When is Final practice exam going to be available?  
A: By Wed of week 10.

Q: I do not have a terminal for windows, curious how I should run pytest for datahub files.  
A: When on datahub, you are working on UCSD's computers, so you have access to a terminal from datahub (Files Tab, New > terminal).  

Q: My question is whether or not we need code tests in our projects. Also, can we use the pytest on our code or do we need to make up our own tests?  
A: Yes - tests are required. See project documentation here https://cogs18.github.io/projects/overview.html (with a FAQ also available: https://cogs18.github.io/projects/faq.html)

Q: I'm curious on what we're gonna be learning in the last couple weeks of class.  
A: Code Style, Code Documentation, How to pull code together into a project, and some more advanced python we haven't yet discussed

Q: Are test functions all one line, straight forward code? Like there's no fancy structure added to them? For example, a test function would never house a for loop or something, right?  
A: They're often just single one line `assert`s. Sometimes, you'd add some code at the beginning to generate an object to use in testing (see coding lab this week), but typically the code is much simpler in the test than the function the test is testing.

Q: Is it still possible that wrong code passes even when tested?  
A: Yup - if the test written doesn't actually test the functionality of the code, the test could pass while the code is not functioning properly. 

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

import this

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

# Badness
def my_func():
    my_nums = '123'
    output = ''
    for num in my_nums:
        output += str(int(num) + 1)
    return output

my_func()

# Goodness
def my_func():
    
    my_nums = '123'    
    output = ''
    
    for num in my_nums:  
        output += str(int(num) + 1)
    
    return output

Note that documentation here is missing (as are comments). This is to highlight the spacing. You'll need documentation and comments.

I promise it's better to comment as you go along rather than coming along after you've written all the code and adding comments.

Similar to writing: write comments -> write code -> review code & comments

#### Clicker Question #1

Which of these is best - A, B, or C?

# Option A
def squared(input_number):
    val = input_number
    power = 2    
    output = val ** power
    return output

# Option B
def squared(input_number, power=2):
    
    output = input_number ** power
    
    return output

# Option C
def squared(input_number):
    
    val = input_number
    power = 2
    
    output = val ** power
    
    return output

### Indentation

Use spaces to indicate indentation levels, with each level defined as 4 spaces. 

# Badness
if True:
  print('Words.')

# Goodness
if True:    
    print('Words.')

### Spacing

- Put one (and only one) space between each element
- Index and assignment don't have a space between opening & closing '()' or '[]'

# Badnesses
my_var=1+2==3
my_list  =  [ 1,2,3,4 ]
el = my_list [1]

# Goodnesses
my_var = 1 + 2 == 3
my_list = [1, 2, 3, 4]
el = my_list[1]

#### Clicker Question #2

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

# Badness
for i in [1, 2, 3]: print(i**2 + i%2)

# Goodness
for i in [1, 2, 3]:
    print(i**2 + i%2)

### Multi-Line

my_long_list = [1, 2, 3, 4, 5,
                6, 7, 8, 9, 10]

# Note: you can explicitly indicate a new line with '\'
my_string = 'Python is ' + \
            'a pretty great language.'

### Imports

- Import one module per line
- Avoid `*` imports
- Use the import order: standard library; 3rd party packages; local / custom code

# Badness
from numpy import *

import os, sys

# Goodness
import os
import sys

import numpy as np

Note: If you don't know how to import a local/custom module, figure that out this week in Coding Lab or office hours.

## Specific Guidelines - Naming

### Valid Names

- Use descriptive names for all modules, variables, functions and classes, that are longer than 1 character

# Badness
a = 12
b = 24

# Goodness
n_filters = 12
n_freqs = 24

Find + Replace also works better when you have specific variable names 

### Naming Style

- CapWords (leading capitals, no separation) for Classes
- snake_case (all lowercase, underscore separator) for variables, functions, and modules

# Badness
def MyFunc():
    pass
    
class my_class():
    def __init__():
        pass

# Goodness
def my_func():
    pass


class MyClass():
    def __init__():
        pass

Note: snake_case is easier to read than CapWords, so we use snake_case for the things (variables, functions) that we name more frequently.

#### Clicker Question #3

If you were reading code and came cross the following, which of the following would you expect to be a class?

- A) `Phillies_Game`
- B) `PhilliesGame`
- C) `phillies_game`
- D) `philliesgame`
- E) `PhIlLiEsGaMe`

#### Clicker Question #4

If you were reading code and came cross the following, which of the following would you expect to be a function or variable name?

- A) `Phillies_Game`
- B) `PhilliesGame`
- C) `phillies_game`
- D) `philliesgame`
- E) `PhIlLiEsGaMe`

### Indicating Scope

- Leading underscores indicate a 'private' attribute or method of the class, meaning it is an internal value, not expected to be accessed by the user.

class MyClass():
    def __init__():
        self.public = None
        self._private = None

The leading underscore indicates to the user that this attribute shouldn't be changed/modified by the user.

`import *` will not import underscored attributes (private attributes).

## Specific Guidelines - String Quotes

In Python, single-quoted strings and double-quoted strings are the same. 

This PEP does not make a recommendation for this. **Pick a rule and stick to it.** 

When a string contains single or double quote characters: use the other one to avoid backslashes in the string. It improves readability.



# Badness
my_string = 'Prof\'s Project'

# Goodness
my_string = "Prof's Project"

#### Clicker Question #5

Which of the following would not cause an error in Python and would store the string *You're so close!*  ?

- A) `my_string = "You're so close!"`
- B) `my_string = "You"re so close!"`
- C) `my_string = 'You''re so close!'`
- D) `my_string = "You\\'re so close"`
- E) `my_string = 'You're so close!'`

# my_string = "You're so close!"
# my_string = "You"re so close!"
my_string = 'You''re so close!'
# my_string = "You\\'re so close!"
# my_string = 'You're so close!'
my_string

## Specific Guidelines - Comments

Out-of-date comments are worse than no comments at all.

Keep your comments up-to-date.

#### Block comments
- apply to some (or all) code that follows them
- are indented to the same level as that code. 
- Each line of a block comment starts with a # and a single space

# Badness
import random

def week_9():
# help try to destress students by picking one thing from the following list using random
    statements = ["You've totally got this!","You're so close!","You're going to do great!","Remember to take breaks!","Sleep, water, and food are really important!"]
    out = random.choice(statements)
    return out

week_9()

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

#### Inline comments
- to be used sparingly
- to be separated by at least two spaces from the statement
- start with a # and a single space

# Badness
week_9()#words of encouragement

# Goodness
week_9()  # words of encouragement

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

```python
# to install on datahub
!pip install --user pylint
```

#### Clicker Question #6

How many PEP8 violations can you find in this code?

def MyFunction(input_num):
    
    my_list = [0,1,2,3]
    if 1 in my_list: ind = 1
    else:
      ind = 0
    qq = []
    for i in my_list [ind:]:
        qq.append(input_num/i)
    return qq

- A) None
- B) 1 or 2 
- C) 3 or 4 
- D) 5 or 6
- E) 7 or more

- function name (not descriptive)
- spacing in the list
- spacing (line)
- no indent after the if statement; new line
- indentation issue (ind = 0)
- variable naming (`qq`)
- spaces in append
- spaces in indexing
- function name not snake_case

# Let's fix this code
def append_list(input_num):
    
    my_list = [0, 1, 2, 3]
    
    if 1 in my_list: 
        ind = 1
    else:
        ind = 0
   
    output_list = []
    for val in my_list[ind:]:
        output_list.append(input_num / val)

    return output_list

# check using pylint
!pylint linter_example.py