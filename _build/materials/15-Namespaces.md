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
  url: /materials/16-CommandLine
  title: '16-CommandLine'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Namespaces

## Namespaces & Scope

<div class="alert alert-success">
A namespace is a 'place' with a set of names and their corresponding objects.
</div>

Names that are defined and available in a given namespace are in 'scope'.

That is, the 'scope' of an object is where it is available to / from. 

## Modules & Packages

<div class="alert alert-success">
A 'module' is a set of Python code with functions, classes, etc available in it. A Python package is a directory of modules.
</div>

Modules are stored in Python files. We can import these files into our namespace, to gain access to the module within Python.

## `import`

<div class="alert alert-success">
`import` is a keyword to import external code into the local namespace.
</div>

### `import` example: math module



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





{:.output_data_text}
```
module
```





{:.input_area}
```python
# By the way - modules are objects
isinstance(math, object)
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
# Using code from our math module
math.sqrt(4)
```





{:.output_data_text}
```
2.0
```



### import example: random module



{:.input_area}
```python
import random
```




{:.input_area}
```python
# Random is also a module
type(random)
```





{:.output_data_text}
```
module
```





{:.input_area}
```python
# Explore what is available in random
random.
#dir(random)
```




{:.input_area}
```python
# Random example
to_choose_from = ['1', '2', '3', '4', '5']
number_to_choose = 2

chosen = random.sample(to_choose_from, number_to_choose)

print(chosen)
```


{:.output_stream}
```
['1', '5']

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
# Import a module with a specific name in our namespace
import collections as cols
```




{:.input_area}
```python
# Import a specific thing and give it a specific name
from string import punctuation as punc
```


### Clicker Question #1

Which of the following is not a valid Python import statement?

- a) `import collections as col`
- b) `from statistics import mean as average`
- c) `from os import path`
- d) `from random import choice, choices`
- e) `import ascii_letters from string`

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





{:.output_data_text}
```
3
```



## Importing Custom Code II



{:.input_area}
```python
# Import a 
from remote import MyNumbers
```




{:.input_area}
```python
# Define an instance of our custom class
nums = MyNumbers(2, 3)
```




{:.input_area}
```python
# Check 
nums.
```




{:.input_area}
```python
## Name
nums.add()
```





{:.output_data_text}
```
5
```



## Name Conflicts



{:.input_area}
```python
choice?
```




{:.input_area}
```python
from remote import choice
```




{:.input_area}
```python
choice?
```




{:.input_area}
```python
choice([1, 2, 3])
```





{:.output_data_text}
```
3
```



## A note on '*'

If you see `from module import *` this means to import everything (read as 'from module import everything). 

This is generally considered not to the best 
