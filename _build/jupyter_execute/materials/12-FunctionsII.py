#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - CL5 due tonight (11:59 PM)
# - A3 due Monday 11/1 (11:59 PM)
# - mid-course survey now [available](https://docs.google.com/forms/d/e/1FAIpQLSfZVIyKtegSiD3oRiKT6BwnQbTMFELxXwfhCuyKa1CmMsCk0A/viewform?usp=sf_link) (*optional*; link also on Canvas; due Mon 11/1 for extra credit)
# - E1 regrades open until Thursday night

# **Q&A**
# 
# Q: For the sort_array algorithm, is lowest = None the only way to put the first item into comparison? This part is a little confusing.  
# A: Nope! There are other approaches. For example, you could index into the first value in the list and store that in `lowest` and then do the comparison from there!
# 
# Q: I am confident at understanding the code for sorting, but I am not confident at writing a code like that. Will there be questions like that in homework? Is there any tip for writing a complex code like that?  
# A: No homework or exam question will require *that* much code; however, the tricks for writing that code is to first *plan*. Plan *what* your approach would be (without actually writing code...just getting the ideas down on paper) prior to writing the code. Then, write one piece at a time. Write the for loop. Make sure that works as intended. Then the conditional..make sure that works, testing out your function as you go. Until you get it completely done! Part I of CL5 helps you start this "plan it first" idea.
# 
# Q: Can I use sort_array function for tuple?  
# A: Try it out! (But yes, it will work like a list)
# 
# Q: What is the difference between an algorithm and a function?   
# A: We define functions to carry out the steps of an algorithm. 
# 
# Q: Will we be given all of the functions that we will need such as the sort function that we learned in order to complete exams and assignments?  
# A: Nope. You will be writing lots of your own functions from here on out! (For those functions like `sorted` that already exist, you will be reminded that they exist and encouraged to use them.)
# 
# Q: How do you use an apostrophe in a string (for example I want to write it's) without the string being interrupted by the apostrophe?   
# A: Use double quotes to start and end your string and the apostrophe inside your string.
# 
# Q: How would we know if we made a mistake (in python) when it comes to sorting? How would we fix it?  
# A: The first way is to execute your function and see if the output is what you expect. The other is to write unit tests. We'll talk about those soon! And, you would fix the mistake by figuring out where your code was incorrect inside the function definition.
# 
# Q: To what extent are we going to have to know how to utilize dictionaries on future exams?   
# A: There will be dictionary questions on future exams. You will need to know how to do all the things - define them, loop through them, index into them, etc.
# 
# Q: do we have to use sort_array(array_to_sort = [array name]) or can we just put sort_array([array_name]) with the array name by itself?  
# A: You can do either. Today's lecture will explain more/why!

# # Functions II
# 
# - quick review
# - more on user-defined functions
#     - function arguments: postional v.s. keywords
#     - default values in function arguments
#     - nested functions
# - methods
#     - difference/similarity between functions/ methods
#     - string, list, & dictionary methods
#     - in place vs not in place methods

# ### Quick review: Functions
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


out1 = is_odd(6)
out2 = is_odd(7)
out1,out2


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

# ## Positional vs. Keyword Arguments

# <div class="alert alert-success">
# Arguments to a function can be indicated by either position or keyword.
# </div>

# In[ ]:


def exponentiate(number, exponent):    
    return number ** exponent


# In[ ]:


# Positional arguments use the position of the input value to infer which argument each value relates to
exponentiate(2, 3)


# In[ ]:


# Keyword arguments are explicitly named as to which argument each value relates to
exponentiate(number = 2, exponent = 3)


# Note: when using Keyword arguments position/order no longer matters, but try to keep them in the same order as they're defined in the function to avoid confusion.

# In[ ]:


exponentiate(exponent = 3, number = 2)


# In[ ]:


# Note: once you have a keyword argument, you can't have other positional arguments afterwards
# this cell will produce an error
exponentiate(number = 2, 3)


# ## Default Values

# <div class="alert alert-success">
# Function parameters can also take <b>default values</b>. This makes some parameters optional, as they take a default value if not otherwise specified.
# </div>

# #### Default Value Functions
# 
# Specify a default value in a function by doing an assignment within the function definition.
# Soo... What's the purpose of default values? 
# 1. Sometimes, you know something will have a particular value most often, so it's more convenient to set up a default value
# 2. Or, you might have many arguments in one function, by specifying a default, you don't have to manually input all values

# In[ ]:


# Create a function, that has a default values for a parameter
# Save time when we know exponengt often takes the value of 2
def exponentiate(number, exponent = 2):  
    return number ** exponent


# In[ ]:


# Use the function, using default value
exponentiate(3)


# In[ ]:


# Call the function, over-riding default value with something else
a = exponentiate(2, 3)
b = exponentiate(number = 2, exponent = 3)
print(a,b)


# #### Clicker Question #2
# 
# What will the following code snippet print?

# In[ ]:


def exponentiate(number, exponent = 2):    
    return number ** exponent

exponentiate(exponent = 3, number = 2)


# - A) 8
# - B) 9
# - C) SyntaxError
# - D) None
# 

# ### Nested functions (functions within functions)
# - a function which is defined within another function

# In[ ]:


def is_odd(value):
    if value % 2 != 0:
        answer = True
    else:
        answer = False
    
    return answer


# In[ ]:


def new_function(my_list):
    output = []
    for val in my_list:
        print('the value of val is: ', val)
        print('the function is_odd(val) will evaluate to: ', is_odd(val), '\n')
        if is_odd(val):
            output.append('yay!')
            print('the output list is: ', output, '\n')
    return output 


# In[ ]:


new_function([1,2,3,4])


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


# ## Finding Methods

# Typing the object/variable name you want to find methods for followed by a '.' and then pressing tab will display all the methods available for that type of object.

# In[ ]:


# Define a test string
my_string = 'Python'


# In[ ]:


# See all the available methods on an object with tab complete
# Make sure that the cursor is right next to the period when you press TAB !!!!!!
my_string.


# Using the function `dir()` returns all methods available

# In[ ]:


# For our purposes now, you can ignore any leading underscores (these are special methods)
dir(my_string)


# ## Correspondance Between Functions & Methods

# Note that:
# 
# ```python
# my_variable.method_call()
# ```
# 
# acts like:
# 
# ```python
# function_call(my_variable)
# ```
# 
# We call methods directly on the variable to demonstrate that it is attached to that variable type.
# 
# **Don't forget the parentheses!! The parentheses ( ) indicates executing code**

# In[ ]:


#example of using a method 
my_list = [1,2,3]
my_list.append(12345)

my_list


# In[ ]:


#example of using a function

def is_odd(value):
    if value % 2 != 0:
        answer = True
    else:
        answer = False
    
    return answer

my_int = 12345

#function call
result = is_odd(my_int)
result


# ### Method / Function documentation

# In[ ]:


# method documentation
get_ipython().run_line_magic('pinfo', 'float.is_integer')


# In[ ]:


# function documentation
get_ipython().run_line_magic('pinfo', 'type')


# Also, you don't have to memorize all the methods that we will mention, but you need to know how to use them.

# ## String Methods
# 
# There are a whole bunch of string methods, all described [here](https://www.w3schools.com/python/python_ref_string.asp). We'll review a few of the most commonly used here.

# In[ ]:


# Make a string all lower case
'aBc123'.lower()


# In[ ]:


# Make a string all upper case
'aBc123'.upper()


# In[ ]:


# Capitalize a string
'python is great. yeey. '.capitalize()


# In[ ]:


# Captilize every element in a string
'i love python python loves me'.title()


# In[ ]:


# Find the index of where a string starts 
print('Hello, my name is'.find('name'))


# In[ ]:


print('Hello, my name is'[10])


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


ints.sort(reverse=True) # helpful for third assignment :) 
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
# Some methods update the object directly (in place) without assignment, whereas others return an updated version of the input and needs to be assigned to a variable. 
# </div>

# #### List methods that are in place

# In[ ]:


# Reverse a list, direct update without assignment 
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
car.keys() 


# In[ ]:


car


# In[ ]:


out = car.keys() 
out


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


# ## Lecture review
# - **functions** 
#     - def function_name(arguments)
#     - two types of function arguments: positional v.s. keywords
#     - function arguments can have default values
#     - nested function: function within function
# - **methods**
#     - similar to function, but they operates on a specific type of variable (objects)
#     - different syntax
#         - function: func(arguments)
#         - method: object.method(arguments)
#     - commonly used methods
#     - two types of methods
#         - inplace: directly alters the object (e.g. `list.append()`)
#         - not inplace: doesn't change the object, but returns a output (e.g.`dictionary.get()`)

# #### Clicker Question #7
# 
# What will the following code snippet print?

# In[ ]:


def find_even(my_list):
    output = []
    for item in my_list:
        if item %2 == 0:
            output.append(item)
        else:
            continue
    return output

def exponentiate_even_number(my_list,power = 2):
    output = []
    even_list = find_even(my_list)
    for i in even_list:
        output.append(i**power)
    return output


# In[ ]:


list_input = [1,3,5,7,9,2,4,6,8,10]
exponentiate_even_number(list_input,3)


# - A) [2,4,6,8,10]
# - B) [8, 64, 216, 512, 1000]
# - C) [1,3,5,7,9]  
# - D) [4, 16, 36, 64, 100]  
# - E) Nothing, calling this function will produce an error
