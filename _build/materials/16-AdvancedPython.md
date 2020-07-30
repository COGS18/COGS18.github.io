---
interact_link: content/materials/16-AdvancedPython.ipynb
download_link: assets/downloads/16-AdvancedPython.ipynb.zip
pdf_link: assets/pdf/16-AdvancedPython.pdf
layout: materials
title: '16-AdvancedPython'
prev_page:
  url: /materials/15-OpenSource-API
  title: '15-OpenSource-API'
next_page:
  url: /materials/A1-Syntax
  title: 'A1-Syntax'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Advanced Python

- string formatting (`format`)
- sets
- `collections`
- args & kwargs
- list comprehensions
- map
- overloading operators

...or: a day of shortcuts

Note: Shortcuts make *your* life easier, but your code *less* understandable to beginners.

It's hard to search for things you don't know exist.

Today's goal : let you know these things exist.

NOT today's goal : teach you all the details.



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





{:.output_data_text}
```
'Hello! My name is Shannon. My job is Assistant Teaching Professor, and I work on Python'
```



## Sets

Sets are a variable type that store **only unique entries**.



{:.input_area}
```python
my_set = set([1, 1, 2, 3, 4])
my_set
```





{:.output_data_text}
```
{1, 2, 3, 4}
```



Like lists, they are iterable & mutable.



{:.input_area}
```python
my_set.add(6)
my_set
```





{:.output_data_text}
```
{1, 2, 3, 4, 6}
```



#### Clicker Question #1

How many values would be in the following set?



{:.input_area}
```python
clicker_set = set([1, 1, 2, 2, 3, 4])
clicker_set.add(6)
clicker_set.add(1)
clicker_set
```





{:.output_data_text}
```
{1, 2, 3, 4, 6}
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
Counter({1: 3, 0: 1, 2: 1})
```





{:.input_area}
```python
import collections
```




{:.input_area}
```python
collections.Counter([1, 0, 1, 2, 1])
```





{:.output_data_text}
```
Counter({1: 3, 0: 1, 2: 1})
```





{:.input_area}
```python
# can count how many of each letter are in there
Counter("I wonder how many times I use the letter 'e'")
```





{:.output_data_text}
```
Counter({'I': 2,
         ' ': 9,
         'w': 2,
         'o': 2,
         'n': 2,
         'd': 1,
         'e': 7,
         'r': 2,
         'h': 2,
         'm': 2,
         'a': 1,
         'y': 1,
         't': 4,
         'i': 1,
         's': 2,
         'u': 1,
         'l': 1,
         "'": 2})
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





{:.output_data_text}
```
True
```





{:.input_area}
```python
all(my_bool_list)
```





{:.output_data_text}
```
False
```



#### Clicker Question #2

What would the following return?



{:.input_area}
```python
my_list = [True, True, False, True]
any(my_list)
```





{:.output_data_text}
```
True
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


## `args` & `kwargs`

- allow you to pass a variable number of arguments to a function
    - `*args` - allow any number of extra arguments (including zero)
    - `**kwargs` - allow any number of *keyword* arguments to be passed (as a dictionary)

### `*args`



{:.input_area}
```python
# use *arguments to demonstrate args
def tell_audience(*arguments):
    for arg in arguments:
        print(arg)
```




{:.input_area}
```python
tell_audience('asdf')
```


{:.output_stream}
```
asdf

```



{:.input_area}
```python
tell_audience("Hello!", 
              "My name is Shannon.", 
              "My job is Assistant Teaching Professor.")
```


{:.output_stream}
```
Hello!
My name is Shannon.
Hello!
My job is Assistant Teaching Professor.

```

### `**kwargs`



{:.input_area}
```python
def tell_audience_kwargs(**info):
    print("type: ", type(info), '\n')
    
    for key, value in info.items():
        print("key: ", key)
        print("value: ", value, "\n")
```




{:.input_area}
```python
tell_audience_kwargs(first='Shannon', 
                     last='Ellis', 
                     email='sellis@ucsd.edu')
```


{:.output_stream}
```
type:  <class 'dict'> 

key:  first
value:  Shannon 

key:  last
value:  Ellis 


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





{:.output_data_text}
```
[1, 2, 3]
```





{:.input_area}
```python
# This list comprehension is equivalent to the cell above
# note the square brackets on the outside
[ind + 1 for ind in [0, 1, 2]]
```





{:.output_data_text}
```
[1, 2, 3]
```





{:.input_area}
```python
# You can also include conditionals inside a list comprehension
my_list = [1, 2, 3, 4, 5]
my_list2 = [val for val in my_list if val % 2 == 0]
```




{:.input_area}
```python
print(my_list)
print(my_list2)
```


{:.output_stream}
```
[1, 2, 3, 4, 5]
[2, 4]

```

#### Clicker Question #3

What would the following return?



{:.input_area}
```python
list1 = [3, 4, 5]
multiplied = [item * 3 for item in list1] 
multiplied
```





{:.output_data_text}
```
[9, 12, 15]
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





{:.output_data_text}
```
['o', 'o', 'o', 'o']
```





{:.input_area}
```python
# but the patterns are where these shine
re.findall('\d\d', my_string)
```





{:.output_data_text}
```
['12', '14', '16']
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
out = []

for val in [1, False, 's', True]:
    out.append(is_bool(val))

out
```





{:.output_data_text}
```
[False, True, False, True]
```





{:.input_area}
```python
# apply function to every element of list
# function to apply is first input to filter
list(filter(is_bool, [1, False, 's', True]))
```





{:.output_data_text}
```
[False, True]
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





{:.output_data_text}
```
2
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





{:.output_data_text}
```
2
```



#### Clicker Question #4

What would the following return?



{:.input_area}
```python
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0), my_list))
new_list
```





{:.output_data_text}
```
[4, 6, 8, 12]
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





{:.output_data_text}
```
[2, 4, 6, 8]
```





{:.input_area}
```python
# Note - we can use lambda functions with map
list(map(lambda x: x *2, my_list))
```





{:.output_data_text}
```
[2, 4, 6, 8]
```



## Conditional Assignment

You can use a conditional within an assignment, to manipulate what gets assigned given some condition. 



{:.input_area}
```python
# variable assignment
condition = False
my_var = 1 if condition else 2
```




{:.input_area}
```python
print(my_var)
```


{:.output_stream}
```
2

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



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
TypeError                                 Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-34-e14a904b0af2> in <module>()
      1 # this will error
----> 2 my_func(my_list)

```

{:.output_traceback_line}
```
TypeError: my_func() missing 2 required positional arguments: 'yy' and 'zz'
```




{:.input_area}
```python
# unpack the list
my_func(*my_list)
```


{:.output_stream}
```
1 2 3

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


{:.output_stream}
```
1 2 3

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


{:.output_stream}
```
The programming language python

```



{:.input_area}
```python
python > perl
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
NameError                                 Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-1-980459611ff9> in <module>()
----> 1 python > perl

```

{:.output_traceback_line}
```
NameError: name 'python' is not defined
```

