---
interact_link: content/materials/11-FunctionsII.ipynb
download_link: assets/downloads/11-FunctionsII.ipynb.zip
pdf_link: assets/pdf/11-FunctionsII.pdf
layout: materials
title: '11-FunctionsII'
prev_page:
  url: /materials/10-Algorithms
  title: '10-Algorithms'
next_page:
  url: /materials/A1-Syntax
  title: 'A1-Syntax'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

## Course Announcements

- A3 due *next* Friday 11/1 (11:59 PM)
- Mid-course survey available
    - http://bit.ly/cogs18_midcourse
    - opportunity for extra credit (if completed by Sunday 10/27 at 11:59 PM)
- I added notes to the end of 10-Algorithms to answer student question about type checking in functions
 

**Reminder**: tab completion is a thing!



{:.input_area}
```python
my_very_long_variable_name = 6
```




{:.input_area}
```python
## demonstrate tab completion here
```


# Functions II

- more on user-defined functions
    - docstrings
    - default values
- methods
    - string, list, & dictionary
    - in place vs not in place
    - relationship to functions

### Clicker Question #1

What will the following code snippet print?



{:.input_area}
```python
def my_func(my_dictionary):
    
    output = []

    for item in my_dictionary:
        value = my_dictionary[item]
        output.append(value) #append method adds an item to end of a list
    
    return output

# create dictionary and execute function
dictionary = {'first' : 1, 'second' : 2, 'third' : 3}
out = my_func(dictionary)

print(out)
```


- A) ['first', 'second', 'third'] 
- B) {1, 2, 3}
- C) ['first', 1, 'second', 2, 'third', 3] 
- D) [1, 2, 3] 
- E) None

## Docstrings

When writing functions, it's often helpful to include information about what the function does.

These are specified by text within triple quotes in the first line after your function is defined.



{:.input_area}
```python
def my_func(my_dictionary):
    """return list of dictionary values"""
    
    ## comment that is not very helpful
    output = []

    for item in my_dictionary:
        value = my_dictionary[item]
        output.append(value)
    
    return output
```




{:.input_area}
```python
my_func?
```


## Default Values

<div class="alert alert-success">
Function parameters can also take default values. This makes some parameters optional, as they take a default value if not otherwise specified.
</div>

#### Default Value Functions

Specify a default value in a function by doing an assignment within the function definition.



{:.input_area}
```python
# Create a function, that has a default values for a parameter
def exponentiate(number, exponent = 2):    
    return number ** exponent
```




{:.input_area}
```python
# Use the function, using default value
exponentiate(2)
```




{:.input_area}
```python
# Call the function, over-riding default value with something else
# python assumes values are in order of parameters specified in definition
exponentiate(2, 3)
```




{:.input_area}
```python
# you can always state this explicitly
exponentiate(number = 2, exponent = 3)
```


## Positional vs. Keyword Arguments

<div class="alert alert-success">
Arguments to a function can be indicated by either position or keyword.
</div>



{:.input_area}
```python
# Positional arguments use the position to infer which argument each value relates to
exponentiate(2, 3)
```




{:.input_area}
```python
# Keyword arguments are explicitly named as to which argument each value relates to
exponentiate(number = 2, exponent = 3)
```




{:.input_area}
```python
exponentiate(exponent = 3, number = 2)
```




{:.input_area}
```python
# Note: once you have a keyword argument, you can't have other positional arguments afterwards
# this cell will produce an error
exponentiate(number = 2, 3)
```


Reminder, setting a default value for one parameter is allowed during function *definition*.

(This may look like what we did above, but here we are including a default value for one parameter during function definition. During function *execution*, you can't mix and match using positional vs. keywords)



{:.input_area}
```python
def exponentiate(number, exponent = 2):    
    return number ** exponent
```


### Clicker Question #2

What will the following code snippet print?



{:.input_area}
```python
def exponentiate(number, exponent = 2):    
    return number ** exponent

exponentiate(exponent = 3, number = 2)
```


- A) 8
- B) 9
- C) SyntaxError
- D) None


Note: when using Keyword arguments position/order no longer matters

## Methods

<div class="alert alert-success">
<b>Methods</b> are functions that are defined and called directly on an object. 
</div>

<div class="alert alert-success">
For our purposes, <b>objects</b> are any data variable. 
</div>

### Method Examples

A method is a function applied directly to the object you call it on.

General form of a method:

```python
object.method()
```

In other words: methods "belong to" an object.



{:.input_area}
```python
# The `append` method, defined on lists
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
```


The method `append()` is called directly on the list `my_list`



{:.input_area}
```python
# append is a method for lists
# this will error with a string
my_string = 'cogs18'
my_string.append('!')
```




{:.input_area}
```python
# The `is_integer()` method, defined on floats
my_float = 12.2
my_float.is_integer()
```




{:.input_area}
```python
# The `is_integer()` method, attempted on an integer
# this code will produce an error
my_int = 12
my_int.is_integer()
```


## String Methods

There are a whole bunch of string methods, all described [here](https://www.w3schools.com/python/python_ref_string.asp). We'll review a few of the most commonly used here.



{:.input_area}
```python
# Make a string all lower case
'aBc'.lower()
```




{:.input_area}
```python
# Make a string all upper case
'aBc'.upper()
```




{:.input_area}
```python
# Capitalize a string
'python is great'.capitalize()
```




{:.input_area}
```python
# Find the index of where a string starts 
'Hello, my name is'.find('name')
```


### Clicker Question #3

What will the following code snippet print out?



{:.input_area}
```python
inputs = ['fIx', 'tYpiNg', 'lIkE', 'tHiS']
output = ''

for element in inputs:
    output = output + element.lower() + ' '

output.capitalize()
```


- A) 'fix typing like this ' 
- B) ['fix', 'typing', 'like', 'this'] 
- C) 'Fix typing like this '  
- D) 'Fix typing like this'  
- E) 'Fixtypinglikethis'

## List Methods

There are also a bunch of list methods, all described [here](https://www.w3schools.com/python/python_ref_list.asp). You've seen some of these before, but we'll review a few of the most commonly used here.



{:.input_area}
```python
# sort sorts integers in numerical orders
ints = [16, 88, 33, 40]
ints.sort()
ints
```




{:.input_area}
```python
# append adds to the end of a list
ints.append(2)
ints
```




{:.input_area}
```python
# remove value from list
ints.remove(40)
ints
```




{:.input_area}
```python
# reverse order of list
ints.reverse()
ints
```


### Clicker Question #4

What will the following code snippet print out?



{:.input_area}
```python
list_string = ['a', 'c', 'd', 'b']
list_string.sort()
list_string.reverse()
list_string
```


- A) ['a', 'c', 'd', 'b']
- B) ['a', 'b', 'c', 'd']
- C) ['d', 'c', 'b', 'a']  
- D) ['d', 'b', 'a', 'c']  
- E) ['d', 'a', 'b', 'c']

## Dictionary Methods

As with string and list methods, there are many described [here](https://www.w3schools.com/python/python_ref_dictionary.asp) that are helpful when working with dictionaries.




{:.input_area}
```python
car = {
  "brand": "BMW",
  "model": "M5",
  "year": 2019
}

# keys() returns the keys of a dictionary
car.keys()
```




{:.input_area}
```python
# get returns the value of a specified key
mod = car.get('model')

print(mod)
```




{:.input_area}
```python
# previously done this by indexing
print(car['model'])
```




{:.input_area}
```python
# update adds a key-value pair
car.update({"color": "Black"})

print(car)
```


### Clicker Question #5

Assuming `dictionary` is a dictionary that exists, what would the following accomplish:

```python

dictionary.get('letter')

```

- A) Return the key for the value 'letter' from `dictionary`
- B) Add the key 'letter' to `dictionary`
- C) Add the value 'letter' to `dictionary`
- D) Return the value for the key 'letter' from `dictionary`


### Clicker Question #6

Which method would you use to add a new key-value pair to a dictionary?

- A) `.append()`
- B) `.get()`
- C) `.keys()` 
- D) `.update()`


### Methods: In Place vs Not In Place

<div class="alert alert-success">
Some methods update the object directly (in place), whereas others return an updated version of the input. 
</div>

#### List methods that are in place



{:.input_area}
```python
# Reverse a list
my_list = ['a', 'b', 'c']
my_list.reverse()

print(my_list)
```




{:.input_area}
```python
# Sort a list
my_numbers = [13, 3, -1]
my_numbers.sort()

print(my_numbers)
```


#### Dictionary methods that are not in place



{:.input_area}
```python
car
```




{:.input_area}
```python
# Return the keys in the dictionary
out = car.keys() 
```




{:.input_area}
```python
# print keys
print(type(out))
print(out)
```




{:.input_area}
```python
# car has not changed
print(type(car))
print(car)
```




{:.input_area}
```python
# Return the values in the dicionary
car.values()
```


## Finding Methods

Typing the object/variable name you want to find methods for followed by a '.' and then pressing tab will display all the methods available for that type of object.



{:.input_area}
```python
# Define a test string
my_string = 'Python'
```




{:.input_area}
```python
# See all the available methods on an object with tab complete
my_string. 
```


Using the function `dir()` returns all methods available



{:.input_area}
```python
# For our purposes now, you can ignore any leading underscores (these are special methods)
dir(my_string)
```


## Correspondance Between Functions & Methods

Note that:

```python
my_variable.function_call()
```

acts like:

```python
function_call(my_variable)
```

A function that we can call directly on a variable (a method) acts like a shortcut for passing that variable into a function. 

### Method / Function Comparison Example



{:.input_area}
```python
my_float = 11.0

# Method call
print(my_float.is_integer())

# Function call
#   Note: `is_integer` is part of the float variable type, which is why we access it from there 
print(float.is_integer(my_float))
```




{:.input_area}
```python
# method documentation
float.is_integer?
```




{:.input_area}
```python
# function documentation
type?
```


#### `is_integer`

You _could_ write a function to check whether a float was an integer and use it as a function (rather than the method `.is_integer()`) ...and we know how to do that!



{:.input_area}
```python
def is_integer(my_float):
    
    if my_float % 1 == 0:
        is_int = True
    else:
        is_int = False
        
    return is_int
```




{:.input_area}
```python
print(my_float)
is_integer(my_float)
```

