**Course Announcements**

- CL7 due tonight (11:59 PM)
- A5 now available; due *next* Friday (we have just started material A5 focuses on)

# Modules & Scripts

- namespaces & scope
- modules
- `import`
    - `from`
    - `as`

## Namespaces & Scope

<div class="alert alert-success">
A <b>namespace</b> is a 'place' with a set of names and their corresponding objects.
</div>

Each Jupyter Notebook has its own Namespace.

If you have two notebooks open at the same time, they don't know about eachother or what variables have been created in the other.

Names that are defined and available in a given namespace are in **scope**.

That is, the *scope* of an object is where it is available to / from. 

# see what's stored in global namespace
a = 3
b = 15
%whos

## Modules & Packages

<div class="alert alert-success">
A <b>module</b> is a set of Python code with functions, classes, etc. available in it. A Python <b>package</b> is a directory of modules.
</div>

Modules are stored in Python files (.py). We can import these files into our namespace, to gain access to the module within Python.

In A3 you had to import the package: `nltk`: 

- **package** is a whole bunch of modules
- a **module** stores python (.py) files
- when imported, we have access to its functionality

## `import`

<div class="alert alert-success">
<code>import</code> is a keyword to import external code into the local namespace.
</div>

Why do it this way (importing modules)? 

1. Minimize startup costs
2. Functions in different packages could have the same name - break programs

### `import` example: math module

For something not yet in your Namespace...

# we haven't imported the module yet
# this code fails if you haven't yet imported math
type(math)

# Import the math module
import math

# Check the type of math
type(math)

# By the way - modules are objects
isinstance(math, object)

# Using code from our math module
# remember to tab complete or use dir(math)
math.sqrt(9)

### `import` example: random module

import random

# Random is also a module
type(random)

# Explore what is available in random
dir(random)

# working with random
random.

## access documentation
random.choice?

## access underlying code
random.choice??

### `random` Example

# random.sample() documentation
random.sample?

# Random example
to_choose_from = ['1', '2', '3', '4', '5']
number_to_choose = 2

chosen = random.sample(to_choose_from, number_to_choose)

print(chosen)

## Imports: `from` & `as`

<div class="alert alert-success">
<code>from</code> and <code>as</code> allows us to decide exactly what objects to import into our namespace, and what we call them (in our namespace).
</div>

# Import a specific object from a module
from random import choice

## do NOT have to type module name 
## using this approach
## to call this
choice(to_choose_from)

# Import a module with a specific name in our namespace
# used when module names are long
import collections as cols

## collections is not defined
## this code will fail
collections.

# this is how you would do it
cols.

# putting it all together
# Import a specific thing and give it a specific name
from string import punctuation as punc

#### Clicker Question #1

Which of the following is NOT a valid Python import statement?

- A) `import collections as col`
- B) `from statistics import mean as average`
- B) `from os import path`
- D) `from random import choice, choices`
- E) `import ascii_letters from string`

#### Clicker Question Answer

# Check our imports
# import collections as col
# from statistics import mean as average
# from os import path
# from random import choice, choices
import ascii_letters from string

## Importing Custom Code I

Why do this? 

Having a whole bunch of functions in a Jupyter Notebook will start to get clutered.

Also, they're not reusable later without copying them into your new notebook. 

Modules avoid this!

## module: `remote.py`

If you want to practice using import with the `remote` example in lecture, store the code in the next cell in a text file saved as `remote.py`. Be sure this is saved in the same directory (folder) as the notebook from which you're trying to call it.

def my_remote_function(input_1, input_2):
    """A function from far away.
    
    This function returns the sum of the two inputs.
    """
    
    return input_1 + input_2

def choice(list_to_choose_from):
    """Choose and return an item from a list. 
    
    Notes: I am a custom choice function: I am NOT from `random`.
    
    Hint: my favorite is the last list item.
    """
    
    return list_to_choose_from[-1]

class MyNumbers():
    
    kind_of_thing = 'numbers'
    
    def __init__(self, num1, num2):
        
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        
        return self.num1 + self.num2
    
    def subtract(self):
        
        return self.num2 - self.num1

# Import some custom code
from remote import my_remote_function

# Investigate our imported function
my_remote_function?

# Run our function
my_remote_function(2, 1)

## Importing Custom Code II

# Import a class class from an external module
from remote import MyNumbers

# Define an instance of our custom class
nums = MyNumbers(2, 3)
type(nums)

# Check 
nums.add()

# Check the definition of the code we imported
nums.add??

## Name Conflicts

from random import choice

# choice is currently from random module
choice?

choice([1, 2, 3, 4, 5])

from remote import choice

# now it's from my remote module
choice?

choice([1, 2, 3, 4, 5])

While you _can_ have functions with the same name in two different places...do your best to avoid this.

It's Python legal but bad for your nerves.

## A note on `*`

If you see `from module import *` this means to import everything (read as 'from module import everything'). 

This is generally considered not to be the best, as it is then unclear in your code exactly where the functionality came from.

# don't do it
# avoid doing * imports
from random import *
choice([2,3,4])

# a valid way to import
from random import choice
choice([2,3,4])

# a valid way to import
import random
random.choice([2,3,4,])

## script: `remote_script.py`


If you want to run your own script example in lecture, store the code in the next cell in a text file saved as `remote_script.py`. Be sure this is saved in the same directory (folder) as the notebook from which you're trying to call it.

from remote import MyNumbers
nums = MyNumbers(2, 3)
print("nums value: ", nums)
print("nums type: ", type(nums))

# run the script
!python remote_script.py

<h1 align="center">We have finished Python!</h1>



<h3 align="right">well, kind of.</h3>