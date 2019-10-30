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
  url: /materials/12-Debugging
  title: '12-Debugging'
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
my_very_long_variable_name
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


{:.output_stream}
```
[1, 2, 3]

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





{:.output_data_text}
```
4
```





{:.input_area}
```python
# Call the function, over-riding default value with something else
# python assumes values are in order of parameters specified in definition
exponentiate(2, 3)
```





{:.output_data_text}
```
8
```





{:.input_area}
```python
# you can always state this explicitly
exponentiate(number = 2, exponent = 3)
```





{:.output_data_text}
```
8
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





{:.output_data_text}
```
8
```





{:.input_area}
```python
# Keyword arguments are explicitly named as to which argument each value relates to
exponentiate(number = 2, exponent = 3)
```





{:.output_data_text}
```
8
```





{:.input_area}
```python
exponentiate(exponent = 3, number = 2)
```





{:.output_data_text}
```
8
```





{:.input_area}
```python
# Note: once you have a keyword argument, you can't have other positional arguments afterwards
# this cell will produce an error
exponentiate(number = 2, 3)
```



{:.output_traceback_line}
```
  File "<ipython-input-24-82d192fd1eb1>", line 3
    exponentiate(number = 2, 3)
                            ^
SyntaxError: positional argument follows keyword argument

```


Reminder, setting a default value for parameters is allowed during function *definition*.

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


{:.output_stream}
```
[1, 2, 3, 4]

```

The method `append()` is called directly on the list `my_list`



{:.input_area}
```python
# append is a method for lists
# this will error with a string
my_string = 'cogs18'
my_string.append('!')
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
AttributeError                            Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-26-b99e95dcd8d7> in <module>()
      2 # this will error with a string
      3 my_string = 'cogs18'
----> 4 my_string.append('!')

```

{:.output_traceback_line}
```
AttributeError: 'str' object has no attribute 'append'
```




{:.input_area}
```python
# The `is_integer()` method, defined on floats
my_float = 12.2
my_float.is_integer()
```





{:.output_data_text}
```
False
```





{:.input_area}
```python
# The `is_integer()` method, attempted on an integer
# this code will produce an error
my_int = 12
my_int.is_integer()
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
AttributeError                            Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-30-ba89eed6f102> in <module>()
      2 # this code will produce an error
      3 my_int = 12
----> 4 my_int.is_integer()

```

{:.output_traceback_line}
```
AttributeError: 'int' object has no attribute 'is_integer'
```


## String Methods

There are a whole bunch of string methods, all described [here](https://www.w3schools.com/python/python_ref_string.asp). We'll review a few of the most commonly used here.



{:.input_area}
```python
# Make a string all lower case
'aBc'.lower()
```





{:.output_data_text}
```
'abc'
```





{:.input_area}
```python
# Make a string all upper case
'aBc'.upper()
```





{:.output_data_text}
```
'ABC'
```





{:.input_area}
```python
# Capitalize a string
'python is great'.capitalize()
```





{:.output_data_text}
```
'Python is great'
```





{:.input_area}
```python
# Find the index of where a string starts 
'Hello, my name is'.find('name')
```





{:.output_data_text}
```
10
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





{:.output_data_text}
```
'Fix typing like this '
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





{:.output_data_text}
```
[16, 33, 40, 88]
```





{:.input_area}
```python
# append adds to the end of a list
ints.append(2)
ints
```





{:.output_data_text}
```
[16, 33, 40, 88, 2]
```





{:.input_area}
```python
# remove value from list
ints.remove(40)
ints
```





{:.output_data_text}
```
[16, 33, 88, 2]
```





{:.input_area}
```python
list.remove?
```




{:.input_area}
```python
# reverse order of list
ints.reverse()
ints
```





{:.output_data_text}
```
[2, 88, 33, 16]
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





{:.output_data_text}
```
['d', 'c', 'b', 'a']
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





{:.output_data_text}
```
dict_keys(['brand', 'model', 'year'])
```





{:.input_area}
```python
# get returns the value of a specified key
mod = car.get('model')

print(mod)
```


{:.output_stream}
```
M5

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


{:.output_stream}
```
{'brand': 'BMW', 'model': 'M5', 'year': 2019, 'color': 'Black'}

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


{:.output_stream}
```
['c', 'b', 'a']

```



{:.input_area}
```python
# Sort a list
my_numbers = [13, 3, -1]
my_numbers.sort()

print(my_numbers)
```


{:.output_stream}
```
[-1, 3, 13]

```

#### Dictionary methods that are not in place



{:.input_area}
```python
car
```





{:.output_data_text}
```
{'brand': 'BMW', 'model': 'M5', 'year': 2019}
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


{:.output_stream}
```
<class 'dict_keys'>
dict_keys(['brand', 'model', 'year'])

```



{:.input_area}
```python
# car has not changed
print(type(car))
print(car)
```


{:.output_stream}
```
<class 'dict'>
{'brand': 'BMW', 'model': 'M5', 'year': 2019}

```



{:.input_area}
```python
# Return the values in the dicionary
car.values()
```





{:.output_data_text}
```
dict_values(['BMW', 'M5', 2019])
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





{:.output_data_text}
```
['__add__',
 '__class__',
 '__contains__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__getnewargs__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mod__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rmod__',
 '__rmul__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'capitalize',
 'casefold',
 'center',
 'count',
 'encode',
 'endswith',
 'expandtabs',
 'find',
 'format',
 'format_map',
 'index',
 'isalnum',
 'isalpha',
 'isdecimal',
 'isdigit',
 'isidentifier',
 'islower',
 'isnumeric',
 'isprintable',
 'isspace',
 'istitle',
 'isupper',
 'join',
 'ljust',
 'lower',
 'lstrip',
 'maketrans',
 'partition',
 'replace',
 'rfind',
 'rindex',
 'rjust',
 'rpartition',
 'rsplit',
 'rstrip',
 'split',
 'splitlines',
 'startswith',
 'strip',
 'swapcase',
 'title',
 'translate',
 'upper',
 'zfill']
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


{:.output_stream}
```
True
True

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


{:.output_stream}
```
11.0

```




{:.output_data_text}
```
True
```



**A3 Q10**: The instructions use the word append. They don't tell you to use the method `append()`. Remember:

- `append()` is a list method (_not_ a string method)
- append (the word) just means add to the end 
- concatenation is how to add to the end of a string

### Functions: Points of Clarification

Additional notes included here to clarify points we've already discussed. Not presented in class, but feel free to review and gain additional clarificaiton.

1. `def` defines a function
2. `function_name()` - parentheses are required to execute a function
3. `function_name(input1)` - input parameters are specified within the function parentheses 
4. `function_name(input1, input2)` - functions can take multiple parameters as inputs
    - `input1` and `input2` can then be used within your function when it executes
5. To store the output from a function, you'll need a `return` statement

#### For example....

If you write a function called `is_odd()` which takes an input `value`, 



{:.input_area}
```python
def is_odd(value):
    if value % 2 != 0:
        answer = True
    else:
        answer = False
    
    return answer
```


to use that function, you would execute `is_odd(value)` ....something like `is_odd(value = 6)`



{:.input_area}
```python
out = is_odd(6)
out
```





{:.output_data_text}
```
False
```



Later on, if you wanted to use that function _within another function_ you still have to pass an input to the function.



{:.input_area}
```python
def new_function(my_list):
    output = []
    for val in my_list:
        if is_odd(val):
            output.append('yay!')
    return output
            
```




{:.input_area}
```python
new_function([1,2,3,4])
```





{:.output_data_text}
```
['yay!', 'yay!']
```


