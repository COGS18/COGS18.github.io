#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# Due Dates:
# - [mid-course survey](https://docs.google.com/forms/d/e/1FAIpQLSdswcDdmqv_kogN7mGkhr_1DJ6jDMLPVblqlz_BZyxizZrOSw/viewform?usp=sf_link) "due" tonight (Mon 11:59 PM; optional for EC; link also on Canvas)
# - **CL6** due Wednesday (11:59 PM)
# - **A3** due Thursday 2/10 (11:59 PM)
# 
# Notes:
# - **CL5** grades posted
# - **E1** grades and answer key posted
#     - Regrade requests (all handled by Prof Ellis): 
#         - YES when you believe you lost points and should not have (human error; we missed something, etc.)
#         - NOT for when you don't like the rubric, misread the instructions, *meant* to do soemthing else, etc.

# **Q&A**
# 
# Q: In a range, do you include the last value, or is that value excluded?  
# A: The last value is excluded....just like in indexing/getting a slice of a collection
# 
# Q: where should I place my break for the output that I want  
# A: This completely depends upon the code you're writing and the logic of that code. Remember that wherever python encounters `break`, the loop will terminate immediately.
# 
# Q: What is the purpose of combining dictionaries with looping? (I'm assuming dictionaries do not always have to be repeated)  
# A: It allows you to access information associated with a key and use that within a function.
# 
# Q: Why do we use .append to add an item to a list but use += to add to a string?  
# A: This is because concatenation for a string is associated with the `+` operator, whereas the `+` operator only works to add two lists together (concatenate them into one list). When you want to add a new *value* to a list, we need the `append()` method.
# 
# Q: I am still confused on the importance of how a print statement in a loop. When will we need to use print statements in the loop and when do we use them outside of loops?  
# A: You never need to use a print statement. They do not affect the functionality of your code. They only `print()` to screen what you ask them to print...so we use them to better understand our code.
# 
# Q: when we write loops with a conditional but not include an else statement (sometimes it's not needed right?), would we be marked down for not including an else statement? are else statements always necessary?  
# A: From a grading perspective, if we don't specify an else condition you don't need to put one. From a logical perspective, it can be helpful to have them to make sure/convince yourself that all conditions have been considered.
# 
# Q: "Does it make a different if we were to declare a variable (ex: an empty list) OUTSIDE of a function? I tried to do it in my assignment but it gives me ""UnboundLocalError."""  
# A: Yes. It does make a difference. Remember that functions have their own namespace. They only have access to variables passed in as input OR defined within the function.
# 
# Q: when do you use a while loop versus a for loop?  
# A: `while` when you want code to repeat based on a condition (something that's true or false); `for` when you have a collection (i.e. list, tuple, dictionary, range, etc.) that you want to repeat code over.
# 
# Q: Is there someplace that we can see a list of algorithms commonly used in Python like sort_array?  
# A: https://docs.python.org/3/library/functions.html
# 
# Q: Is "item" the only word we can use to refer to each item in a list?  
# A: There are other words. "element" would be another commonly-used term.
# 
# Q: Can you also put multiple break statements in a conditional or only once?  
# A: You could put it in, but only one would be used by python (the first one it encounters)
# 
# Q: 1) strings = 'COGS18'; for char in strings: # here char is literally every character in COGS18 (like C, O, G, S, 1, 8) and not just the word COGS18? This is confusing me because strings here is not a collection, so for is not checking for an item, it is checking for single letters/characters?  
# A: Strings are a collection. So far we've learned about lists, tuples, dictionaries, range, and strings. It's less common to loop over strings/treat them as a collection, but it is possible!
# 
# Q: what does vowels mean?  
# A: https://en.wikipedia.org/wiki/Vowel
# 
# Q: couter+=1(why does it contain both "plus" and "equal" sign.  
# A: This is shorthand. It is equivaelnt to `counter = counter + 1`

# # Methods
# 
# - string, list, & dictionary
# - in place vs not in place
# - relationship to functions

# #### Clicker Question #1
# 
# What will the following code snippet print?

# In[ ]:


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


# - A) ['first', 'second', 'third'] 
# - B) {1, 2, 3}
# - C) ['first', 1, 'second', 2, 'third', 3] 
# - D) [1, 2, 3] 
# - E) None

# ## Methods

# <div class="alert alert-success">
# <b>Methods</b> are functions that are defined and called directly on an object. 
# </div>
# 
# <div class="alert alert-success">
# For our purposes, <b>objects</b> are any data variable. 
# </div>

# ### Method Examples
# 
# A method is a function applied directly to the object you call it on.

# General form of a method:
# 
# ```python
# object.method()
# ```

# In other words: methods "belong to" an object.

# In[ ]:


# The `append` method, defined on lists
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)


# The method `append()` is called directly on the list `my_list`

# In[ ]:


# append is a method for lists
# this will error with a string
my_string = 'cogs18'
my_string.append('!')


# In[ ]:


# The `is_integer()` method, defined on floats
my_float = 12.2
my_float.is_integer()


# In[ ]:


# The `is_integer()` method, attempted on an integer
# this code will produce an error
my_int = 12
my_int.is_integer()


# ## String Methods
# 
# There are a whole bunch of string methods, all described [here](https://www.w3schools.com/python/python_ref_string.asp). We'll review a few of the most commonly used here.

# In[ ]:


# Make a string all lower case
'aBc'.lower()


# In[ ]:


# Make a string all upper case
'aBc'.upper()


# In[ ]:


# Capitalize a string
'python is great'.capitalize()


# In[ ]:


# Find the index of where a string starts 
'Hello, my name is'.find('name')


# #### Clicker Question #3
# 
# What will the following code snippet print out?

# In[ ]:


inputs = ['fIx', 'tYpiNg', 'lIkE', 'tHiS']
output = ''

for element in inputs:
    output = output + element.lower() + ' '

output.capitalize()


# - A) 'fix typing like this ' 
# - B) ['fix', 'typing', 'like', 'this'] 
# - C) 'Fix typing like this '  
# - D) 'Fix typing like this'  
# - E) 'Fixtypinglikethis'

# ## List Methods
# 
# There are also a bunch of list methods, all described [here](https://www.w3schools.com/python/python_ref_list.asp). You've seen some of these before, but we'll review a few of the most commonly used here.

# In[ ]:


# sort sorts integers in numerical orders
ints = [16, 88, 33, 40]
ints.sort()
ints


# In[ ]:


ints.sort(reverse=True)
ints


# In[ ]:


# append adds to the end of a list
ints.append(2)
ints


# In[ ]:


# remove value from list
ints.remove(40)
ints


# In[ ]:


get_ipython().run_line_magic('pinfo', 'list.remove')


# In[ ]:


# reverse order of list
ints.reverse()
ints


# #### Clicker Question #4
# 
# What will the following code snippet print out?

# In[ ]:


list_string = ['a', 'c', 'd', 'b']
list_string.sort()
list_string.reverse()
list_string


# - A) ['a', 'c', 'd', 'b']
# - B) ['a', 'b', 'c', 'd']
# - C) ['d', 'c', 'b', 'a']  
# - D) ['d', 'b', 'a', 'c']  
# - E) ['d', 'a', 'b', 'c']

# ## Dictionary Methods
# 
# As with string and list methods, there are many described [here](https://www.w3schools.com/python/python_ref_dictionary.asp) that are helpful when working with dictionaries.
# 

# In[ ]:


car = {
  "brand": "BMW",
  "model": "M5",
  "year": 2019
}

# keys() returns the keys of a dictionary
car.keys()


# In[ ]:


# get returns the value of a specified key
mod = car.get('model')

# equivalent
mod2 = car['model']

print(mod)
print(mod2)


# In[ ]:


# previously done this by indexing
print(car['model'])


# In[ ]:


# update adds a key-value pair
car.update({"color": "Black"})

print(car) 


# #### Clicker Question #5
# 
# Assuming `dictionary` is a dictionary that exists, what would the following accomplish:
# 
# ```python
# 
# dictionary.get('letter')
# 
# ```
# 
# - A) Return the key for the value 'letter' from `dictionary`
# - B) Add the key 'letter' to `dictionary`
# - C) Add the value 'letter' to `dictionary`
# - D) Return the value for the key 'letter' from `dictionary`
# 

# #### Clicker Question #6
# 
# Which method would you use to add a new key-value pair to a dictionary?
# 
# - A) `.append()`
# - B) `.get()`
# - C) `.keys()` 
# - D) `.update()`
# 

# ### Methods: In Place vs Not In Place

# <div class="alert alert-success">
# Some methods update the object directly (in place), whereas others return an updated version of the input. 
# </div>

# #### List methods that are in place

# In[ ]:


# Reverse a list
my_list = ['a', 'b', 'c']
my_list.reverse()

print(my_list)


# In[ ]:


# Sort a list
my_numbers = [13, 3, -1]
my_numbers.sort()

print(my_numbers)


# #### Dictionary methods that are not in place

# In[ ]:


car


# In[ ]:


# Return the keys in the dictionary
out = car.keys() 


# In[ ]:


# print keys
print(type(out))
print(out)


# In[ ]:


# car has not changed
print(type(car))
print(car)


# In[ ]:


# Return the values in the dicionary
car.values()


# ## Finding Methods

# Typing the object/variable name you want to find methods for followed by a '.' and then pressing tab will display all the methods available for that type of object.

# In[ ]:


# Define a test string
my_string = 'Python'


# In[ ]:


# See all the available methods on an object with tab complete
my_string.


# Using the function `dir()` returns all methods available

# In[ ]:


# For our purposes now, you can ignore any leading underscores (these are special methods)
dir(my_string)


# ## Correspondance Between Functions & Methods

# All methods are functions. Methods are special functions *attached* to a variable type. All functions are NOT methods. 
# 
# Note that:
# 
# ```python
# my_variable.function_call()
# ```
# 
# acts like:
# 
# ```python
# function_call(my_variable)
# ```
# 
# A function that we can call directly on a variable (a method) acts like a shortcut for passing that variable into a function. 

# ### Functions: Reminders
# 
# Additional notes included here to remind you of points we've already discussed. Not presented in class, but feel free to review and gain additional clarificaiton.
# 
# 1. `def` defines a function
# 2. `function_name()` - parentheses are required to execute a function
# 3. `function_name(input1)` - input parameters are specified within the function parentheses 
# 4. `function_name(input1, input2)` - functions can take multiple parameters as inputs
#     - `input1` and `input2` can then be used within your function when it executes
# 5. To store the output from a function, you'll need a `return` statement

# #### For example....
# 
# If you write a function called `is_odd()` which takes an input `value`, 

# In[ ]:


def is_odd(value):
    if value % 2 != 0:
        answer = True
    else:
        answer = False
    
    return answer


# to use that function, you would execute `is_odd(value)` ....something like `is_odd(value = 6)`

# In[ ]:


out = is_odd(6)
out


# Later on, if you wanted to use that function _within another function_ you still have to pass an input to the function.

# In[ ]:


def new_function(my_list):
    output = []
    for val in my_list:
        if is_odd(val):
            output.append('yay!')
    return output
            


# In[ ]:


new_function([1,2,3,4])

