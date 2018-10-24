---
download_link: assets/downloads/11-FunctionsII.ipynb.zip
pdf_link: assets/pdf/11-FunctionsII.pdf
title: '11-functionsii'
permalink: '/chapters/11-FunctionsII'
previouschapter:
  url: /chapters/10-Algorithms
  title: '10-algorithms'
nextchapter:
  url: /chapters/A1-Syntax
  title: 'A1-syntax'
redirect_from:
  - '/chapters/11-functionsii'
---

# Functions II

### Clicker Question #1

What will the following code snippet print out?



{:.input_area}
```python
def my_func(my_dict):
    
    output = []

    for item in my_dict:
        value = my_dict[item]
        output.append(value)
    
    return output
        
dictionary = {'first' : 1, 'second' : 2, 'third' : 3}

out = my_func(dictionary)

print(out)
```


A) ['first', 'second', 'third'] | B) {1, 2, 3} | C) ['first', 1, 'second', 2, 'third', 3] | D) [1, 2, 3] | E) None

## Methods

<div class="alert alert-success">
Methods are functions that are called directly on an object. 
</div>

### Method Examples



{:.input_area}
```python
# The `append` method, defined on strings
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
```


{:.output_stream}
```
[1, 2, 3, 4]

```



{:.input_area}
```python
# The `is_integer` method, defined on floats
my_float = 12.2
my_float.is_integer()
```





{:.output_data_text}
```
False
```



## String Methods



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
'python'.capitalize()
```





{:.output_data_text}
```
'Python'
```





{:.input_area}
```python
# Find the index of where a string 
'Hello, my name is'.find('name')
```





{:.output_data_text}
```
10
```



### Clicker Question #2

What will the following code snippet print out?



{:.input_area}
```python
inputs = ['fIx', 'tYpiNg', 'lIkE', 'tHiS']
output = ''

for element in inputs:
    element.lower()
    output = output + element + ' '

output.capitalize()
```


A) 'fix typing like this '  | B) ['fix', 'typing', 'like', 'this'] | C) 'Fix typing like this '  | D) ['Fix', 'Typing', 'Like', 'This'] | E) 'Fixtypinglikethis'

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
my_list = [13, 3, -1]
my_list.sort()

print(my_list)
```


{:.output_stream}
```
[-1, 3, 13]

```

#### Dictionary methods that are not in place



{:.input_area}
```python
my_dict = {'n1' : True, 'n2' : False}
```




{:.input_area}
```python
# Return the keys in the dictionary
my_dict.keys()
```





{:.output_data_text}
```
dict_keys(['n1', 'n2'])
```





{:.input_area}
```python
# Return the values in the dicionary
my_dict.values()
```





{:.output_data_text}
```
dict_values([True, False])
```



## Finding Methods



{:.input_area}
```python
# Define a test string
my_string = 'Pyton'
```




{:.input_area}
```python
# See all the avaible methods on an object with tab complete
my_string.
```




{:.input_area}
```python
# You can also use `dir` on an object to see everything is has available
#   For our purposes now, you can ignore any leading underscores (these are special methods)
dir(my_string)
```


## Correspondance Between Functions & Methods

Note that:

```
my_variable.function_call()
```

acts like:

```
function_call(my_variable)
```

A function that we can call directly on a variable (a method) acts like a shortcut for passing that variable into a function. 

### Method / Function Comparison Example



{:.input_area}
```python
my_float = 11.0

# Method call
my_float.is_integer()

# Function call
#   Note: `is_integer` is part of the float variable type, which is why we access it from there 
float.is_integer(my_float)
```





{:.output_data_text}
```
True
```



#### `is_integer`



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
is_integer(my_float)
```





{:.output_data_text}
```
True
```


