#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# - **CL5** due tomorrow (Wed)
# - **A3** due Friday (it typically takes students longer than A2)
# - [**Mid-course survey**](https://docs.google.com/forms/d/e/1FAIpQLSdOQLk7FvTYT-o79kEbc5Bo_DF8EvKzZm-ebcyXSSQRDH6P9g/viewform?usp=sf_link) now available ("due" Friday; link also on Canvas)

# **Exams**
# - **In-class** portion can be reviewed in coding lab tomorrow OR in Prof's OH Th 1-3 PM
#     - You CANNOT take the exam with you
#     - You CAN take pictures of your midterms
#     - Score on canvas = (Score on paper + 1)/3 
# - **Regrades**:
#     - Staple a piece of paper to your exam with explanation of regrade request and ask staff member to put aside for me to review
#     - Post on Piazza with explanation for where you think a mistake was made
# - **Take-home** portion grades will be released Wed (feedback will be available on datahub)

# # Methods
# 
# - string, list, & dictionary
# - in place vs not in place
# - relationship to functions

# #### Class Question #1
# 
# What will the following code snippet print?

# In[1]:


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

# In[3]:


# student question about appending a list to a list
my_list = [1, 2, 3]
my_list2 = [4, 5]
my_list.append(my_list2)


# In[4]:


my_list


# In[6]:


# + operator to concatenate two lists into a single list
my_list = [1, 2, 3]
my_list2 = [4, 5]
my_list + my_list2


# In[7]:


my_list.append[4]


# In[2]:


# The `append` method, defined on lists
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)


# The method `append()` is called directly on the list `my_list`

# In[8]:


# append is a method for lists
# this will error with a string
my_string = 'cogs18'
my_string.append('!')


# In[9]:


# The `is_integer()` method, defined on floats
my_float = 12.2
my_float.is_integer()


# In[10]:


# The `is_integer()` method, attempted on an integer
# this code will produce an error
my_int = 12
my_int.is_integer()


# ## String Methods
# 
# There are a whole bunch of string methods, all described [here](https://www.w3schools.com/python/python_ref_string.asp). We'll review a few of the most commonly used here.

# In[12]:


# Make a string all lower case
'aBcDEF'.lower()


# In[13]:


# Make a string all upper case
'aBc'.upper()


# In[14]:


# Capitalize a string
'python is great'.capitalize()


# In[15]:


# Find the index of where a string starts 
'Hello, my name is'.find('name')


# #### Class Question #2
# 
# What will the following code snippet print out?

# In[26]:


count = 0
count += 1 # works with strings too
count


# In[24]:


inputs = ['fIx', 'tYpiNg', 'lIkE', 'tHiS']
output = ''

for element in inputs:
#     print(element)
    output = output + element.lower() + ' '
#     print(output)

output.capitalize()


# - A) 'fix typing like this ' 
# - B) ['fix', 'typing', 'like', 'this'] 
# - C) 'Fix typing like this '  
# - D) 'Fix typing like this'  
# - E) 'Fixtypinglikethis'

# ## List Methods
# 
# There are also a bunch of list methods, all described [here](https://www.w3schools.com/python/python_ref_list.asp). You've seen some of these before, but we'll review a few of the most commonly used here.

# In[29]:


# sort sorts integers in numerical orders
ints = [16, 88, 33, 40]
ints.sort() # reverse parameter is False by default
ints


# In[30]:


ints.sort(reverse=True)
ints


# In[34]:


# append adds to the end of a list
ints.append(2)
ints


# In[32]:


# remove value from list
ints.remove(40)
ints


# In[33]:


get_ipython().run_line_magic('pinfo', 'list.remove')


# In[35]:


# reverse order of list
ints.reverse()
ints


# #### Class Question #3
# 
# What will the following code snippet print out?

# In[37]:


list_string = ['a', 'c', 'd', 'b']
list_string.sort()
print('after sort: ', list_string)
list_string.reverse()
print('after reverse: ', list_string)
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

# In[42]:


car = {
  "brand": "BMW",
  "model": "M5",
  "year": 2019
}

# keys() returns the keys of a dictionary
car.keys()


# In[43]:


# get returns the value of a specified key
mod = car.get('model')

# equivalent
mod2 = car['model']

print(mod)
print(mod2)


# In[ ]:


# previously done this by indexing
print(car['model'])


# In[44]:


# update adds a key-value pair
car.update({"color": "Black"})

print(car) 


# #### Class Question #4
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

# #### Class Question #5
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

# In[47]:


# Reverse a list
my_list = ['a', 'b', 'c']
my_list.reverse()

print(my_list)


# In[48]:


# Sort a list
my_numbers = [13, 3, -1]
my_numbers.sort()

print(my_numbers)


# #### Dictionary methods that are not in place

# In[49]:


car


# In[50]:


# Return the keys in the dictionary
out = car.keys() 


# In[51]:


# print keys
print(type(out))
print(out)


# In[52]:


# car has not changed
print(type(car))
print(car)


# In[53]:


# Return the values in the dicionary
car.values()


# ## Finding Methods

# Typing the object/variable name you want to find methods for followed by a '.' and then pressing tab will display all the methods available for that type of object.

# In[54]:


# Define a test string
my_string = 'Python'


# In[ ]:


# See all the available methods on an object with tab complete
my_string.


# Using the function `dir()` returns all methods available

# In[55]:


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


# ## More Functions & Methods
# 

# ### `sort_array`
# 
# A version of a **selection sort**:
# - loop through current list
# - find lowest item
# - put that at the front of your sorted list
# - remove lowest item from current list
# - wash, rinse, repeat

# In[56]:


def sort_array(array_to_sort):
    """A function to sort an array."""

    is_sorted = False    # Keeps track of when we are done sorting
    sorted_array = []    # A new list that we will use to store our sorted values
     
    while is_sorted == False:

        lowest = None
        for item in array_to_sort:
            if lowest == None:  # If not defined (first element) set the current element as lowest
                lowest = item
            if item < lowest:
                lowest = item
        
        # these next two lines uses some new (to us) list methods
        sorted_array.append(lowest)    # Add the lowest value to our sorted array output
        array_to_sort.remove(lowest)   # Drop the now sorted value from the original array

        if len(array_to_sort) == 0:    # When `array_to_sort` is empty, we are done sorting
#             break (option to break here)
            is_sorted = True
    
    return sorted_array


# ### Using `sort_array`

# In[57]:


# Sort an array of integers
unsorted_array = [12, 7, 19, 12, 25]
sorted_array = sort_array(unsorted_array)
print(sorted_array)


# In[58]:


# Sort an array of floats
unsorted_array = [21.3, 56.7, 2.3, 2.9, 99.9]
sorted_array = sort_array(unsorted_array)
print(sorted_array)


# ## SideNote: `sorted`

# In[ ]:


# Sort a list, with `sorted`
data = [7, 4, 6]
sorted(data)


# In[ ]:


# what about a list of strings?
sorted(['asdf','abcd'])


# In[ ]:


# Sort different data types
print(sorted(['a', 'c', 'b']))
print(sorted([True, False, True]))
print(sorted([[1, 4], [1, 2]]))

