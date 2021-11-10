#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# - CL7 due tonight (11:59 PM)
# - A4 due Friday (11:59 PM)
# 
# **Note**:
# - No class Wed before Thanksgiving (11/24)

# **Q&A** 
# 
# Q: Are the terminal commands universal? And if  " .. " is a command to go to a directory, then is " . " also a thing for going to a folder or subfolder?  
# A: The terminal commands are universal on Unix/Mac operating systems. Windows uses slightly different. "." indicates "this directory"
# 
# Q: For CL 7, are we going to be creating code in the terminal instead in the Python notebooks?  
# A: Yes in the terminal and in separate .py files.
# 
# Q: I just looked at CL7 and I have no idea what to do with the first question: do we need to write down all the codes we use on terminal?  
# A: You could but you don't have to. You could just summarize (as notes to yourself) what you were able to accomplish and what you were not, so you know what to review/work on/ask questions about going forward.
# 
# Q: Why is the command line more useful than manipulating the files in an explorer?  
# A: Speed!
# 
# Q: what is "!echo"?  
# A: It's equivalent to `print()` in python. It prints something out to screen.
# 
# Q: I just wanted to know what the difference between class and def is?  
# A: `class` creates a new class/object type. `def` (outside of `class`) defines a function. `def` (inside of `class`) defines a method.
# 
# Q: Why I created a file which has a name ended with ".py" but can not import the code in that file in a jupyter notebook?  
# A: Consider file paths - is your .py file in the same folder/directory as your notebook?
# 
# Q: how will this come into play in our project?  
# A: We'll discuss this Friday, but your project will have .py files as part of it.
# 
# Q: In what instances is it more beneficial to use a relative vs. an absolute path?  
# A: Absolute paths are specific to *your* computer, so they're used less often. Relative paths will work on someone else's computer, so long as their project/directory structure is the same.
# 
# Q: I think something that I was curious about during lecture was how you were able to access your own computer's files through the datahub/jupytr terminal and whether that is possible for students as well. Did you have to change computer permissions or authorize datahub access to your own personal files in order to do so?  
# A: This is through Anaconda - see Coding Lab 1 if you didn't download it yet.
# 
# Q: Is it possible to have functions and classes defined in a script file along with other script contents rather than import them as a module?  
# A: Yes. Although, ideally functions/classes would be defined in a module and imported into your script (better organization; allows re-usability)
# 
# Q: How do you know where the computer thinks you are?  
# A: `pwd` 

# # Modules & Scripts
# 
# - namespaces & scope
# - modules
# - `import`
#     - `from`
#     - `as`

# ## Namespaces & Scope

# <div class="alert alert-success">
# A <b>namespace</b> is a 'place' with a set of names and their corresponding objects.
# </div>

# Each Jupyter Notebook has its own Namespace.
# 
# If you have two notebooks open at the same time, they don't know about eachother or what variables have been created in the other.

# Names that are defined and available in a given namespace are in **scope**.

# That is, the *scope* of an object is where it is available to / from. 

# In[ ]:


# see what's stored in global namespace
a = 3
b = 15
get_ipython().run_line_magic('whos', '')


# ## Modules & Packages

# <div class="alert alert-success">
# A <b>module</b> is a set of Python code with functions, classes, etc. available in it. A Python <b>package</b> is a directory of modules.
# </div>

# Modules are stored in Python files (.py). We can import these files into our namespace, to gain access to the module within Python.

# In A3 you had to import the package: `nltk`: 
# 
# - **package** is a whole bunch of modules
# - a **module** stores python (.py) files
# - when imported, we have access to its functionality

# ## `import`

# <div class="alert alert-success">
# <code>import</code> is a keyword to import external code into the local namespace.
# </div>

# Why do it this way (importing modules)? 
# 
# 1. Minimize startup costs
# 2. Functions in different packages could have the same name - break programs

# ### `import` example: math module

# For something not yet in your Namespace...

# In[ ]:


# we haven't imported the module yet
# this code fails if you haven't yet imported math
type(math)


# In[ ]:


# Import the math module
import math


# In[ ]:


# Check the type of math
type(math)


# In[ ]:


# By the way - modules are objects
isinstance(math, object)


# In[ ]:


# Using code from our math module
# remember to tab complete or use dir(math)
math.sqrt(9)


# ### `import` example: random module

# In[ ]:


import random


# In[ ]:


# Random is also a module
type(random)


# In[ ]:


# Explore what is available in random
dir(random)


# In[ ]:


# working with random
random.


# In[ ]:


## access documentation
get_ipython().run_line_magic('pinfo', 'random.choice')


# In[ ]:


## access underlying code
get_ipython().run_line_magic('pinfo2', 'random.choice')


# ### `random` Example

# In[ ]:


# random.sample() documentation
get_ipython().run_line_magic('pinfo', 'random.sample')


# In[ ]:


# Random example
to_choose_from = ['1', '2', '3', '4', '5']
number_to_choose = 2

chosen = random.sample(to_choose_from, number_to_choose)

print(chosen)


# ## Imports: `from` & `as`

# <div class="alert alert-success">
# <code>from</code> and <code>as</code> allows us to decide exactly what objects to import into our namespace, and what we call them (in our namespace).
# </div>

# In[ ]:


# Import a specific object from a module
from random import choice


# In[ ]:


## do NOT have to type module name 
## using this approach
## to call this
choice(to_choose_from)


# In[ ]:


# Import a module with a specific name in our namespace
# used when module names are long
import collections as cols


# In[ ]:


## collections is not defined
## this code will fail
collections.


# In[ ]:


# this is how you would do it
cols.


# In[ ]:


# putting it all together
# Import a specific thing and give it a specific name
from string import punctuation as punc


# #### Clicker Question #1
# 
# Which of the following is NOT a valid Python import statement?
# 
# - A) `import collections as col`
# - B) `from statistics import mean as average`
# - B) `from os import path`
# - D) `from random import choice, choices`
# - E) `import ascii_letters from string`

# #### Clicker Question Answer

# In[ ]:


# Check our imports
# import collections as col
# from statistics import mean as average
# from os import path
# from random import choice, choices
# import ascii_letters from string


# ## Importing Custom Code I

# Why do this? 
# 
# Having a whole bunch of functions in a Jupyter Notebook will start to get clutered.
# 
# Also, they're not reusable later without copying them into your new notebook. 
# 
# Modules avoid this!

# ## module: `remote.py`
# 
# If you want to practice using import with the `remote` example in lecture, store the code in the next cell in a text file saved as `remote.py`. Be sure this is saved in the same directory (folder) as the notebook from which you're trying to call it.

# In[ ]:


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


# In[ ]:


# Import some custom code
from remote import my_remote_function


# In[ ]:


# Investigate our imported function
get_ipython().run_line_magic('pinfo', 'my_remote_function')


# In[ ]:


# Run our function
my_remote_function(2, 1)


# ## Importing Custom Code II

# In[ ]:


# Import a class class from an external module
from remote import MyNumbers


# In[ ]:


# Define an instance of our custom class
nums = MyNumbers(2, 3)
type(nums)


# In[ ]:


# Check 
nums.add()


# In[ ]:


# Check the definition of the code we imported
get_ipython().run_line_magic('pinfo2', 'nums.add')


# ## Name Conflicts

# In[ ]:


from random import choice


# In[ ]:


# choice is currently from random module
get_ipython().run_line_magic('pinfo', 'choice')


# In[ ]:


choice([1, 2, 3, 4, 5])


# In[ ]:


from remote import choice


# In[ ]:


# now it's from my remote module
get_ipython().run_line_magic('pinfo', 'choice')


# In[ ]:


choice([1, 2, 3, 4, 5])


# While you _can_ have functions with the same name in two different places...do your best to avoid this.
# 
# It's Python legal but bad for your nerves.

# ## A note on `*`
# 
# If you see `from module import *` this means to import everything (read as 'from module import everything'). 
# 
# This is generally considered not to be the best, as it is then unclear in your code exactly where the functionality came from.

# In[ ]:


# a valid way to import
from random import choice
choice([2,3,4])


# In[ ]:


# a valid way to import
import random
random.choice([2,3,4,])


# ## script: `remote_script.py`
# 
# 
# If you want to run your own script example in lecture, store the code in the next cell in a text file saved as `remote_script.py`. Be sure this is saved in the same directory (folder) as the notebook from which you're trying to call it.

# In[ ]:


from remote import MyNumbers
nums = MyNumbers(2, 3)
print("nums value: ", nums)
print("nums type: ", type(nums))


# In[ ]:


# run the script
get_ipython().system('python remote_script.py')


# <h1 align="center">We have finished Python!</h1>
# 
# 

# <h3 align="right">well, kind of.</h3>
