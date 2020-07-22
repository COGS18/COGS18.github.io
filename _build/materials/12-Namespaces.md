---
interact_link: content/materials/12-Namespaces.ipynb
download_link: assets/downloads/12-Namespaces.ipynb.zip
pdf_link: assets/pdf/12-Namespaces.pdf
layout: materials
title: '12-Namespaces'
prev_page:
  url: /materials/11-Classes
  title: '11-Classes'
next_page:
  url: /materials/A1-Syntax
  title: 'A1-Syntax'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
### Course Announcements

- CL4 tomorrow (7/22; 11:59 PM)
- Exam 2 *Thurs* (due Fri 7/24; 11 AM)
- A4 due Mon (11:59 PM)


**Updates**:
- Prof Ellis OH: Wed 4-6 PM (this week only)
- A2 posted
- E1 regrades were handled this morning

# Namespaces

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



{:.input_area}
```python
# see what's stored in global namespace
a = 3
b = 15
%whos
```


{:.output_stream}
```
Variable   Type    Data/Info
----------------------------
a          int     3
b          int     15

```

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



{:.input_area}
```python
# we haven't imported the module yet
# this code fails if you haven't yet imported math
type(math)
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
<ipython-input-2-0a474bb83797> in <module>()
      1 # we haven't imported the module yet
      2 # this code fails if you haven't yet imported math
----> 3 type(math)

```

{:.output_traceback_line}
```
NameError: name 'math' is not defined
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
# remember to tab complete or use dir(math)
math.sqrt(9)
```





{:.output_data_text}
```
3.0
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





{:.output_data_text}
```
module
```





{:.input_area}
```python
# Explore what is available in random
dir(random)
```





{:.output_data_text}
```
['BPF',
 'LOG4',
 'NV_MAGICCONST',
 'RECIP_BPF',
 'Random',
 'SG_MAGICCONST',
 'SystemRandom',
 'TWOPI',
 '_BuiltinMethodType',
 '_MethodType',
 '_Sequence',
 '_Set',
 '__all__',
 '__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 '_acos',
 '_bisect',
 '_ceil',
 '_cos',
 '_e',
 '_exp',
 '_inst',
 '_itertools',
 '_log',
 '_os',
 '_pi',
 '_random',
 '_sha512',
 '_sin',
 '_sqrt',
 '_test',
 '_test_generator',
 '_urandom',
 '_warn',
 'betavariate',
 'choice',
 'choices',
 'expovariate',
 'gammavariate',
 'gauss',
 'getrandbits',
 'getstate',
 'lognormvariate',
 'normalvariate',
 'paretovariate',
 'randint',
 'random',
 'randrange',
 'sample',
 'seed',
 'setstate',
 'shuffle',
 'triangular',
 'uniform',
 'vonmisesvariate',
 'weibullvariate']
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
random.choice(to_choose_from)
```





{:.output_data_text}
```
'2'
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
['4', '1']

```

## Imports: `from` & `as`

<div class="alert alert-success">
<code>from</code> and <code>as</code> allows us to decide exactly what objects to import into our namespace, and what we call them (in our namespace).
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





{:.output_data_text}
```
'4'
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
type(collections)
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
<ipython-input-20-45554599f3a7> in <module>()
      1 ## collections is not defined
      2 ## this code will fail
----> 3 type(collections)

```

{:.output_traceback_line}
```
NameError: name 'collections' is not defined
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




{:.input_area}
```python
punc
```





{:.output_data_text}
```
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
```



#### Clicker Question #1

Which of the following is NOT a valid Python import statement?

- A) `import collections as col`
- B) `from statistics import mean as average`
- C) `from os import path`
- D) `from random import choice, choices`
- E) `import ascii_letters from string`

#### Clicker Question Answer



{:.input_area}
```python
# Check our imports
# import collections as col
# from statistics import mean as average
# from os import path
# from random import choice, choices
import ascii_letters from string
```



{:.output_traceback_line}
```
  File "<ipython-input-31-037fa158f972>", line 6
    import ascii_letters from string
                            ^
SyntaxError: invalid syntax

```


## Importing Custom Code I

Why do this? 

Having a whole bunch of functions in a Jupyter Notebook will start to get clutered.

Also, they're not reusable later without copying them into your new notebook. 

Modules avoid this!

## Using `remote.py`

If you want to practice using import with the `remote` example in lecture, store the code in the next cell in a text file saved as `remote.py`. Be sure this is saved in the same directory (folder) as the notebook from which you're trying to call it.



{:.input_area}
```python
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
```


#### Clicker Question #2

Have you created remote.py?

- A) Yup!
- B) I wanted to...but I'm confused/stuck.
- C) I'm going to do it later on.



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
# Import a class class from an external module
from remote import MyNumbers
```




{:.input_area}
```python
# Define an instance of our custom class
nums = MyNumbers(2, 3)
type(nums)
```





{:.output_data_text}
```
remote.MyNumbers
```





{:.input_area}
```python
# Check 
nums.add()
```





{:.output_data_text}
```
5
```





{:.input_area}
```python
# Check the definition of the code we imported
nums.add??
```


## Name Conflicts



{:.input_area}
```python
from random import choice
```




{:.input_area}
```python
# choice is currently from random module
choice?
```




{:.input_area}
```python
choice([1, 2, 3, 4, 5])
```





{:.output_data_text}
```
4
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
choice([1, 2, 3, 4, 5])
```





{:.output_data_text}
```
5
```



While you _can_ have functions with the same name in two different places...do your best to avoid this.

It's Python legal but bad for your nerves.

## A note on `*`

If you see `from module import *` this means to import everything (read as 'from module import everything'). 

This is generally considered not to be the best.



{:.input_area}
```python
# a valid way to import
from random import choice
choice([2,3,4])
```





{:.output_data_text}
```
2
```





{:.input_area}
```python
# a valid way to import
import random
random.choice([2,3,4,])
```





{:.output_data_text}
```
3
```



<h1 align="center">We have finished Python!</h1>



<h3 align="right">well, kind of.</h3>
