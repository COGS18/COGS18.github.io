---
interact_link: content/materials/23-AdvancedPython.ipynb
download_link: assets/downloads/23-AdvancedPython.ipynb.zip
pdf_link: assets/pdf/23-AdvancedPython.pdf
layout: materials
title: '23-AdvancedPython'
prev_page:
  url: /materials/22-CodeProjects
  title: '22-CodeProjects'
next_page:
  url: /materials/A1-Syntax
  title: 'A1-Syntax'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Advanced Python

- string formatting (`format`)
- sets
- `collections`
- list comprehensions
- map
- overloading operators

...or: a day of shortcuts

Note: Shortcuts make *your* life easier, but your code *less* understandable to beginners.

It's hard to search for things you don't know exist.

Today's goal : let you know these things exist.

NOT today's goal : teach you all the details.

You do *not* need to incorporate these into your project, but if they'll help you, go for it!



{:.input_area}
```python
import antigravity
```


## String Formatting

Use the `format` method to manipulate and format strings.



{:.input_area}
```python
name = "Shannon"
job = "Assistant Teaching Professor"
topic = "Python"

"Hello! My name is {}. My job is {}, and I work on {}".format(name, job, topic)
```


## Sets

Sets are a variable type that store **only unique entries**.



{:.input_area}
```python
my_set = set([1, 1, 2, 3, 4])
my_set
```


Like lists, they are iterable & mutable.



{:.input_area}
```python
my_set.add(6)
my_set
```


### Clicker Question #1

How many values would be in the following set?



{:.input_area}
```python
clicker_set = set([1, 1, 2, 2, 3, 4])
clicker_set.add(6)
clicker_set.add(1)
clicker_set
```


- A) 0
- B) 4
- C) 5
- D) 6
- E) ¯\\\_(ツ)\_/¯

Reminder that if you add a value that is already in the set...the set will not change

## Collections

The `collections` module has a number of useful variable types, with special properties. 

"Special editions" of collections we've discussed before (lists, tuples, and dictionaries).



{:.input_area}
```python
from collections import Counter
```




{:.input_area}
```python
# count how many elements there are in collection
# return values in a dictionary
Counter([1, 0, 1, 2, 1])
```





{:.output_data_text}
```
Counter({0: 1, 1: 3, 2: 1})
```





{:.input_area}
```python
# can count how many of each letter are in there
Counter("I wonder how many times I use the letter 'e'")
```


Think back to our encryption scheme! 

The most common letter in the English language is 'e'.

If you just move each letter over by 1 position, you can just use a Counter to crack the code.

Why we moved to a variable encoder!

## `any` & `all`

`any` and `all` evaluate collections for whether elements evaluate as True. 



{:.input_area}
```python
my_bool_list = [True, False, True]
```




{:.input_area}
```python
any(my_bool_list)
```




{:.input_area}
```python
all(my_bool_list)
```


### Clicker Question #2

What would the following return?



{:.input_area}
```python
my_list = [True, True, False, True]
any(my_list)
```


- A) `True`
- B) `False`
- C) `[True, True, True]`
- D) `[False]`
- E) ¯\\\_(ツ)\_/¯

## `getattr` & `setattr`

`getattr` and `setattr` can be used to get and set attributes, respectively. 

Flexibly return and define instance attributes.



{:.input_area}
```python
class MyClass():
    
    def __init__(self):
        
        self.var_a = 'string'
        self.var_b = 12

# create instance 
instance = MyClass()
```




{:.input_area}
```python
instance.var_a
```




{:.input_area}
```python
# Get a specified attribute
# define var_a as an input
getattr(instance, 'var_a')
```




{:.input_area}
```python
# Set a specified attribute
setattr(instance, 'var_b', 13)
print(instance.var_b)
```


## List Comprehensions

List comprehensions allow you to run loops and conditionals, *inside lists*.

The general format is :

`[ expression for item in list if conditional ]`




{:.input_area}
```python
# NOT a list comprehension
# how we've been doing it
input_list = [0, 1, 2]
output_list = []

for ind in input_list:
    output_list.append(ind + 1)
    
# look at output
output_list
```




{:.input_area}
```python
# This list comprehension is equivalent to the cell above
# note the square brackets on the outside
[ind + 1 for ind in [0, 1, 2]]
```




{:.input_area}
```python
# You can also include conditionals inside a list comprehension
my_list = [1, 2, 3, 4, 5]
[val for val in my_list if val % 2 == 0]
```


### Clicker Question #3

What would the following return?



{:.input_area}
```python
list1 = [3, 4, 5]
multiplied = [item * 3 for item in list1] 
multiplied
```


- A) `True`
- B) `False`
- C) `[9, 12, 15]`
- D) `15`
- E) ¯\\\_(ツ)\_/¯

Note: there are also tuple & dictionary comprehensions.

## Regular Expressions

Regular expressions allow you to work with **specified patterns in strings**.



{:.input_area}
```python
import re
```




{:.input_area}
```python
my_string = "If 12 Python programmers try to complete 14 tasks in 16 minutes, why?"
```




{:.input_area}
```python
# can just search for a letter
re.findall('o', my_string)
```




{:.input_area}
```python
# but the patterns are where these shine
re.findall('\d\d', my_string)
```


## filter

`filter` is a function that takes in another function, and a collection object, and **filters the collection with the function**. 



{:.input_area}
```python
def is_bool(val):
    if isinstance(val, bool):
        return True
    else:
        return False
```




{:.input_area}
```python
#filter?
```




{:.input_area}
```python
# apply function to every element of list
# function to apply is first input to filter
list(filter(is_bool, [1, False, 's', True]))
```


## Lambda Functions

Lambda functions are small, anonymous functions. 

Can define them in line.



{:.input_area}
```python
increment = lambda a : a + 1
```




{:.input_area}
```python
increment(1)
```




{:.input_area}
```python
# not a lambda function
def lambda_equivalent(a):
    
    output = a + 1
    
    return output
```




{:.input_area}
```python
lambda_equivalent(1)
```


### Clicker Question #4

What would the following return?



{:.input_area}
```python
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0), my_list))
new_list
```


- A) `[1, 5, 11, 3]`
- B) `[1, 3, 5, 11]`
- C) `[4, 6, 8, 12]`
- D) `[1, 5, 4, 6, 8, 11, 3, 12]`
- E) ¯\\\_(ツ)\_/¯

## map

`map` applies a given function to each element in a collection. 



{:.input_area}
```python
# create a function
def double(val):
    return val * 2
```




{:.input_area}
```python
# map function to each element of list
my_list = [1, 2, 3, 4]
list(map(double, my_list))
```




{:.input_area}
```python
# Note - we can use lambda functions with map
list(map(lambda x: x *2, my_list))
```


## Conditional Assignment

You can use a conditional within an assignment, to manipulate what gets assigned given some condition. 



{:.input_area}
```python
# variable assignment
condition = True
my_var = 1 if condition else 2
```




{:.input_area}
```python
print(my_var)
```


## Unpacking

You can unpack collection objects with `*`, and key, value pairs with `**`. 



{:.input_area}
```python
def my_func(xx, yy, zz):
    print(xx, yy, zz)
```




{:.input_area}
```python
# create list
my_list = [1, 2, 3]
```




{:.input_area}
```python
# this will error
my_func(my_list)
```




{:.input_area}
```python
# unpack the list
my_func(*my_list)
```




{:.input_area}
```python
# create dictionary
my_dict = {'xx' : 1, 'yy' : 2, 'zz' : 3}
```




{:.input_area}
```python
# unpack the dictionary
my_func(**my_dict)
```


## Overloading Operators

In other words: Nothing in Python is sacred.

Operators and special operations for objects are defined by double underscore methods, which we can overload to change how the object acts. 



{:.input_area}
```python
class Language():
    
    def __init__(self, name):
        self.name = name.lower()
    
    # Overload what the printed representation of the object as a string
    def __repr__(self):
        return "The programming language " + self.name
    
    # Overload the greater than symbol
    def __gt__(self, other):
        return True if self.name == 'python' else False
```


Note: "dunder" is how we refer to those double underscore methods



{:.input_area}
```python
python = Language('python')
perl = Language('perl')
```




{:.input_area}
```python
print(python)
```




{:.input_area}
```python
python > perl
```


## Where We've Been:

- Python & Jupyter
- Variables
- Operators
- Conditionals
- Lists, Tuples & Dictionaries
- Loops
- Functions
- Objects & Classes
- Namespaces
- Command Line
- APIs, Scientific Computing, & Open Source
- Documentation, Code Style, Code Testing

## Clicker Question #1

After COGS 18, I feel \_\_\_\_\_\_\_\_\_\_\_\_ my Python programming abilities

- A) very confident in
- B) somewhat confident in
- C) middle-of-the-raod about
- D) somewhat unsure about
- E) very unsure about


## Clicker Question #2

After COGS 18, I feel the following about my future Python programming:

- A) will use again for sure
- B) may use again
- C) unsure if will use again
- D) probably won't use again
- E) definitely won't use again


## How to Continue with Coding

- Write Code
- Read Code
- Learn and follow standard procedures
- Do code reviews
- Interact with the community
- Build a code portfolio

## Powered by Python

This course used:
- Python Programming Language
- Jupyter Notebooks
- RISE Jupyter Slides
- nbgrader
- Jupyter Book
- scipy stack & many other 3rd party modules

## Where do you go from here

- if want_more_data_science:
    - go to COGS 9
- if you want_more_data_science *and* Python
    - got take COGS 108
- if interested_in_research:
    - look for labs, tell them you can code
- if want_something_else:
    - go do it!

## Acknowledgements

Thank you to Tom Donoghue for his original design of this course.

Thank you to the TAs & IAs for their tireless work on this class.

Thank you students for you time, effort and patience with this (kinda new) course. 

<center><h1> The End 
