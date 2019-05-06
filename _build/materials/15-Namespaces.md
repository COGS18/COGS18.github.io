---
interact_link: content/materials/15-Namespaces.ipynb
download_link: assets/downloads/15-Namespaces.ipynb.zip
pdf_link: assets/pdf/15-Namespaces.pdf
layout: materials
title: '15-Namespaces'
prev_page:
  url: /materials/14-Classes
  title: '14-Classes'
next_page:
  url: /materials/A1-Syntax
  title: 'A1-Syntax'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

### Course Announcements

- Exam Friday (We'll review Wednesday)
- A4 due Monday (11:59 PM)


*Reminder*: Code shared on Piazza containing code for assignment questions must be posted ***to Instructors only***.  
*Note*: I have a 10AM meeting and have to leave right after class today.

## Midterm Expectations

You will be expected to: 

1. Recognize, understand and _respond_ to Python syntax:
    - statements & comments, whitespace, code blocks & indentation levels
2. Recognize, understand and be able to _explain_ code constructions:
    - variables, operators, data types, conditionals, loops, functions, errors, & classes 
    - keywords (`def`, `class`, `return`, etc.)
3. Know and be able to explain (roughly define) concepts we have talked about
    - encodings & algorithms are related concepts (encryption, computability)
4. Be able to apply what you've learned:
    - Given a task:
        - what kind of code constructions are needed to answer it?
        - what kind of concepts does it relate to?
5. With respect to everything above, be able to read and respond to short code snippets and write out code 

### A4: Artificial Agents

Creating multiple bots that move: 

- randomly
- with a purpose
- teleport

### Clicker Question

How much work have you done on A4?

- A) Haven't looked at it at all
- B) Had a look, haven't started
- C) A little
- D) A Fair amount
- E) Most or all of it

### A4 Point of Clarification: Q2

- question asks you to set the default parameter `reverse` to the function as `False`. 
- Be sure to do that.




{:.input_area}
```python
# setting a default input for a parameter
def my_function(my_input, reverse=False):
    pass
```


- question also asks you to use the `sorted()` function
- so do that also.



{:.input_area}
```python
sorted?
```




{:.input_area}
```python
# A4 Q2
my_list = [1, 16, 15]
print(sorted(my_list))
```




{:.input_area}
```python
print(sorted(my_list, reverse=True))
```




{:.input_area}
```python
print(sorted(my_list, reverse=False))
```


#### Putting it all together



{:.input_area}
```python
def my_function(my_input, reverse=False):
    
    output = sorted(my_input, reverse=reverse)

    return output
```




{:.input_area}
```python
my_function(my_list)
```




{:.input_area}
```python
my_function(my_list, reverse=True)
```


### Review Question #1

After executing the following code, which of the following statements is NOT true?



{:.input_area}
```python
from datetime import date

my_date = date(year = 1988, month = 9, day = 29)
my_year = my_date.year
my_weekday = my_date.weekday()
```


- A) `my_date`, `my_year`, and `my_weekday` are all objects
- B) `my_weekday` is a date type object
- C) `year` is an attribute stored in date type objects
- D) `weekday` is a method available for date type objects
- E) `type(my_date)` would return 'datetime.date'

### Review Question #2

After executing the code below, which of the following options would output `True`?




{:.input_area}
```python
def exponentiate(number, exponent = 2):    
    return number**exponent

a = exponentiate(exponent = 3, number = 2)
b = exponentiate(3)
```


- A) `a == b`
- B) `a < b`
- C) `a > b`
- D) This would produce an error.




{:.input_area}
```python
print( a == b)
print( a < b )
print(a > b)
```


### Classes Review

- `class` creates a new class type
    - names tend to use CamelCase
    - can have attributes, instance attributes, and methods
        - `obj.attribute` accesses data stored in attribute
        - `obj.method()` carries out code defined within method 
        - instance attributes defined with `__init__`
    - `self` refers to current instance
- to create an object of a specified class type (`ClassType`):
    - `object_name = ClassType(input1, input2)`
    - `self` is not given an input when creating an object of a specified class

### Review Question #3

Given the following set of classes and code executed below, what will print out?



{:.input_area}
```python
class Brain(): 
    
    def __init__(self, size=None, folded=None):
        self.size = size
        self.folded = folded
        
    def print_info(self):
        folded_string = ''
        if not self.folded:
            folded_string = 'not'
        print('This brain is ' + self.size + ' and is ' + folded_string + ' folded.')
        
class SheepBrain(Brain):
    
    def __init__(self, size='medium', folded=False):
        super().__init__(size, folded)
        
class HumanBrain(Brain):
    def __init__(self, size='large', folded=True):
        super().__init__(size, folded)
```




{:.input_area}
```python
sheep = SheepBrain()
human = HumanBrain()
human.folded and sheep.folded
```


- A) True
- B) False
- C) None
- D) AssertionError
- E) ¯\\\_(ツ)\_/¯



{:.input_area}
```python
# has access to Brain() methods
sheep.print_info()
```


# Namespaces

- namespaces & scope
- modules
- `import`
    - `from`
    - `as`

General note: Today's details are not on the exam _but_ we have spoken about Namespaces previously. That material _IS_ fair game for the exam.

## Namespaces & Scope

<div class="alert alert-success">
A namespace is a 'place' with a set of names and their corresponding objects.
</div>

Each Jupyter Notebook has its own Namespace.

If you have two notebooks open at the same time, they don't know about eachother or what variables have been created in the other.

Names that are defined and available in a given namespace are in 'scope'.

That is, the 'scope' of an object is where it is available to / from. 



{:.input_area}
```python
# see what's stored in namespace
%whos
```


## Modules & Packages

<div class="alert alert-success">
A 'module' is a set of Python code with functions, classes, etc. available in it. A Python package is a directory of modules.
</div>

Modules are stored in Python files. We can import these files into our namespace, to gain access to the module within Python.

In A3 you had to import `nltk`: 

- **package** is a whole bunch of modules
- a **module** stores python files 
- when imported, we have access to its functionality

## `import`

<div class="alert alert-success">
`import` is a keyword to import external code into the local namespace.
</div>

Why do it this way (importing modules)? 

1. Minimize startup costs
2. Functions in different packages could have the same name - break programs

### `import` example: math module

For something not yet in your Namespace...



{:.input_area}
```python
# we haven't imported the module yet
# this code fails if you haven't yet imported math
type(math)
```




{:.input_area}
```python
# Import the math module
import math
```




{:.input_area}
```python
# Check the type of math
type(math)
```




{:.input_area}
```python
# By the way - modules are objects
isinstance(math, object)
```




{:.input_area}
```python
# Using code from our math module
# remember to tab complete or use dir(math)
math.
```


### `import` example: random module



{:.input_area}
```python
import random
```




{:.input_area}
```python
# Random is also a module
type(random)
```




{:.input_area}
```python
# Explore what is available in random
dir(random)
```




{:.input_area}
```python
# working with random
random.
```




{:.input_area}
```python
## access documentation
random.choice?
```




{:.input_area}
```python
## access underlying code
random.choice??
```


### `random` Example



{:.input_area}
```python
# random.sample() documentation
random.sample?
```




{:.input_area}
```python
# Random example
to_choose_from = ['1', '2', '3', '4', '5']
number_to_choose = 2

chosen = random.sample(to_choose_from, number_to_choose)

print(chosen)
```


## Imports: `from` & `as`

<div class="alert alert-success">
`from` and `as` allows us to decide exactly what objects to import into our namespace, and what we call them (in our namespace).
</div>



{:.input_area}
```python
# Import a specific object from a module
from random import choice
```




{:.input_area}
```python
## do NOT have to type module name 
## using this approach
## to call this
choice(to_choose_from)
```




{:.input_area}
```python
# Import a module with a specific name in our namespace
# used when module names are long
import collections as cols
```




{:.input_area}
```python
## collections is not defined
## this code will fail
collections.
```




{:.input_area}
```python
# this is how you would do it
cols.
```




{:.input_area}
```python
# putting it all together
# Import a specific thing and give it a specific name
from string import punctuation as punc
```


### Clicker Question #1

Which of the following is NOT a valid Python import statement?

- A) `import collections as col`
- B) `from statistics import mean as average`
- B) `from os import path`
- D) `from random import choice, choices`
- E) `import ascii_letters from string`

#### Clicker Question Answer



{:.input_area}
```python
# Check our imports
#import collections as col
#from statistics import mean as average
#from os import path
#from random import choice, choices
#import ascii_letters from string
```


## Importing Custom Code I

Why do this? 

Having a whole bunch of functions in a Jupyter Notebook will start to get clutered.

Also, they're not reusable later without copying them into your new notebook. 

Modules avoid this!



{:.input_area}
```python
# Import some custom code
from remote import my_remote_function
```




{:.input_area}
```python
# Investigate our imported function
my_remote_function?
```




{:.input_area}
```python
# Run our function
my_remote_function(2, 1)
```


## Importing Custom Code II



{:.input_area}
```python
# Import a class class from an external module
from remote import MyNumbers
```




{:.input_area}
```python
# Define an instance of our custom class
nums = MyNumbers(2, 3)
type(nums)
```




{:.input_area}
```python
# Check 
nums.subtract()
```




{:.input_area}
```python
# Check the definition of the code we imported
nums.subtract??
```


## Name Conflicts



{:.input_area}
```python
# choice is currently from random module
choice?
```




{:.input_area}
```python
choice([1, 2, 3])
```




{:.input_area}
```python
from remote import choice
```




{:.input_area}
```python
# now it's from my remote module
choice?
```




{:.input_area}
```python
choice([1, 2, 3])
```


While you _can_ have functions with the same name in two different places...do your best to avoid this.

It's Python legal but bad for your nerves.

## A note on '*'

If you see `from module import *` this means to import everything (read as 'from module import everything). 

This is generally considered not to be the best.

<h1 align="center">We have finished Python!</h1>



<h3 align="right">well, kind of.</h3>
