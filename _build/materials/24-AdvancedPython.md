---
interact_link: content/materials/24-AdvancedPython.ipynb
download_link: assets/downloads/24-AdvancedPython.ipynb.zip
pdf_link: assets/pdf/24-AdvancedPython.pdf
layout: materials
title: '24-AdvancedPython'
prev_page:
  url: /materials/23-CodeProjects
  title: '23-CodeProjects'
next_page:
  url: /materials/25-WrapUp
  title: '25-WrapUp'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Advanced Python



{:.input_area}
```python
import antigravity
```


## String Formatting

Use the `format` method to manipulate and format strings.



{:.input_area}
```python
name = "Tom"
job = "instructor"
topic = "Python"

"Hello! My name is {}, my job is {} and I work on {}".format(name, job, topic)
```





{:.output_data_text}
```
'Hello! My name is Tom, my job is instructor and I work on Python'
```



## Sets

Sets are a variable type that store only unique entries.



{:.input_area}
```python
my_set = set([1, 1, 2, 3, 4])
my_set
```





{:.output_data_text}
```
{1, 2, 3, 4}
```



## Collections

The `collections` module has a number of useful variable types, with special properties. 



{:.input_area}
```python
from collections import Counter
```




{:.input_area}
```python
Counter([1, 0, 1, 2, 1])
```





{:.output_data_text}
```
Counter({0: 1, 1: 3, 2: 1})
```





{:.input_area}
```python
Counter("I wonder how many times I use the letter 'e'")
```





{:.output_data_text}
```
Counter({' ': 9,
         "'": 2,
         'I': 2,
         'a': 1,
         'd': 1,
         'e': 7,
         'h': 2,
         'i': 1,
         'l': 1,
         'm': 2,
         'n': 2,
         'o': 2,
         'r': 2,
         's': 2,
         't': 4,
         'u': 1,
         'w': 2,
         'y': 1})
```



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



## getattr & setattr

`getattr` and `setattr` can be used to get and set attributes, respectively. 



{:.input_area}
```python
class MyClass():
    
    def __init__(self):
        
        self.var_a = 'string'
        self.var_b = 12
        
instance = MyClass()
```




{:.input_area}
```python
# Get a specified attribute
getattr(instance, 'var_a')
```





{:.output_data_text}
```
'string'
```





{:.input_area}
```python
# Set a specified attribute
setattr(instance, 'var_b', 13)
print(instance.var_b)
```


{:.output_stream}
```
13

```

## List Comprehensions

List comprehensions allow you to run loops and conditionals, inside lists



{:.input_area}
```python
input_list = [0, 1, 2]
output_list = []
for ind in input_list:
    output_list.append(ind + 1)
```




{:.input_area}
```python
# This list comprehension is equivalent to the cell above
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
[val for val in my_list if val % 2 == 0]
```





{:.output_data_text}
```
[2, 4]
```



Note: there are also tuple & dictionary comprehensions.

## Regular Expressions

Regular expressions allow you to work with specified patterns in strings.



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
re.findall('\d\d', my_string)
```





{:.output_data_text}
```
['12', '14', '16']
```



## filter

`filter` is a function that takes in another function, and a collection object, and filters the collection with the function. 



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
list(filter(is_bool, [1, False, 's', True]))
```





{:.output_data_text}
```
[False, True]
```



## Lambda Functions

Lambda functions are small, anonymous functions. 



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
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0), my_list))
new_list
```





{:.output_data_text}
```
[4, 6, 8, 12]
```



## map

`map` applies a given function to each element in a collection. 



{:.input_area}
```python
def double(val):
    return val * 2
```




{:.input_area}
```python
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
condition = True
my_var = 1 if condition else 2
```




{:.input_area}
```python
print(my_var)
```


{:.output_stream}
```
1

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
my_list = [1, 2, 3]
```




{:.input_area}
```python
my_func(*my_list)
```


{:.output_stream}
```
1 2 3

```



{:.input_area}
```python
my_dict = {'xx' : 1, 'yy' : 2, 'zz' : 3}
```




{:.input_area}
```python
my_func(**my_dict)
```


{:.output_stream}
```
1 2 3

```

## Overloading Operators

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




{:.input_area}
```python
python = Language('python')
java = Language('java')
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
python > java
```





{:.output_data_text}
```
True
```


