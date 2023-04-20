#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - A1 due Friday (11:59 PM)
# - CL3 answers posted
# - A2 now available (due *next* Friday)
#     - will have all information for A2 after this set of notes

# # Collections
# 
# - Lists, Tuples, Dictionaries
# - Indexing
# - Mutating
# - `chr` and `ord`

# ## Collections: Lists 

# <div class="alert alert-success">
# A <b>list</b> is a mutable collection of ordered items, that can be of mixed type. Lists are created using square brackets.
# </div>

# ### List examples

# In[ ]:


# Define a list
lst = [1, 'a', True]


# In[ ]:


# Print out the contents of a list
print(lst)


# In[ ]:


# Check the type of a list
type(lst)


# ### Indexing

# <div class="alert alert-success">
# <b>Indexing</b> refers to selecting an item from within a collection. Indexing is done with square brackets.
# </div>

# In[ ]:


# Define a list 
my_lst = ['Julian', 'Amal', 'Richard', 'Juan', 'Xuan']


# In[ ]:


# Indexing: Count forward, starting at 0, with positive numbers
print(my_lst[1])


# In[ ]:


# Indexing: Count backward, starting at -1, with negative numbers
print(my_lst[-1])


# In[ ]:


# Indexing: Grab a group of adjacent items using `start:stop`, called a slice
print(my_lst[2:4])


# In[ ]:


# indexing to end of list
print(my_lst[2:])


# In[ ]:


# Indexing from beginning of list
print(my_lst[:4])


# In[ ]:


# slicing by skipping a value [start:stop:step]
print(my_lst[0:4:2])


# ### Reminders

# - Python is zero-based (The first index is '0')
# - Negative indices index backwards through a collection
# - A sequence of indices (called a slice) can be accessed using `start:stop`
#     - In this contstruction, `start` is included then every element until `stop`, not including `stop` itself
#     - To skip values in a sequence use `start:stop:step`

# <div class="alert alert-success">
# Starting at zero is a convention (some) languages use that comes from how variables are stored in memory
# , and 'pointers' to those locations.
# </div>

# #### Class Question #1
# 
# What would be the appropriate line of code to return `['butter', '&', 'jelly']`?

# In[ ]:


q3_lst = ['peanut', 'butter', '&','jelly']


# - A) `q3_lst[2:4]`
# - B) `q3_lst[1:3]`
# - C) `q3_lst[:-2]`
# - D) `q3_lst[-3:]`
# - E) `q3_lst[1:4:2]`

# Note: The following has been added to the notes due to student questions in previous iterations. This and the following two cells are *not* someting you'll be tested on. Including as an FYI for those curious.
# 
# You *can* return ['jelly', '&', 'butter'] but it combines two different concepts.
# 
# 1. the `start:stop` now refers to indices in the reverse.
# 2. `-1` is used as the step to reverse the output.
# 
# More details about `step`:  
# `step`: the amount by which the index increases, defaults to 1. If it's negative, you're slicing over the iterable in reverse.

# In[ ]:


# slice in reverse
q3_lst[-1:-4:-1]


# In[ ]:


# you can use forward indexing
# makes this a little clearer
q3_lst[3:0:-1]


# ## Mutating a List

# <div class="alert alert-success">
# Lists are <i>mutable</i>, meaning after definition, you can update and change things about the list.
# </div>

# In[ ]:


# reminder what's in my_lst 
my_lst


# In[ ]:


# Redefine a particular element of the list
my_lst[2] = 'Rich'


# In[ ]:


# Check the contents of the list
print(my_lst)


# #### Class Question #2
# 
# What would the following code accommplish?

# In[ ]:


lst_update = [1, 2, 3, 0, 5]
lst_update[3] = 4 


# - A) replace 0 with 4 in `lst_update`
# - B) replace 4 with 0 in `lst_update`
# - C) no change to `lst_update`
# - D) produce an error
# - E) I'm not sure

# ## Collections: Tuples 

# <div class="alert alert-success">
# A <b>tuple</b> is an <i>immutable</i> collection of ordered items, that can be of mixed type. Tuples are created using parentheses. Tuples are used when you don't want to be able to update the items in your tuple.
# </div>

# ### Tuple Examples

# In[ ]:


# Define a tuple
tup = (2, 'b', False)


# In[ ]:


# Print out the contents of a tuple
print(tup)


# In[ ]:


# Check the type of a tuple
type(tup)


# In[ ]:


# Index into a tuple
tup[0]


# In[ ]:


# Get the length of a tuple
len(tup)


# ### Tuples are Immutable

# In[ ]:


# Tuples are immutable - meaning after they defined, you can't change them
# This code will produce an error.
tup[2] = 1


# #### Class Question #3
# 
# Which of the following specifies a tuple of 2 items?

# In[ ]:


item_A = ['100-11-2233', '200-22-3344']
item_B = ('100-11-2233', '200-22-3344')
item_C = ['100-11-2233', '200-22-3344', 1234, 0]
item_D = ('100-11-2233', '200-22-3344', 1234, 0)
item_E = (12)


# - A) item_A
# - B) item_B
# - C) item_C
# - D) item_D
# - E) item_E

# ## Dictionaries
# 

# <div class="alert alert-success">
# A dictionary is mutable collection of items, that can be of mixed-type, that are stored as key-value pairs.
# </div>

# ### Dictionaries as Key-Value Collections

# In[ ]:


# Create a dictionary
dictionary = {'key_1' : 'value_1', 'key_2' : 'value_2'}


# In[ ]:


# Check the contents of the dictionary
print(dictionary)


# In[ ]:


# Check the type of the dictionary
type(dictionary)


# In[ ]:


# Dictionaries also have a length
# length refers to how many pairs there are
len(dictionary)


# ### Dictionaries: Indexing

# In[ ]:


# Dictionaries are indexed using their keys
dictionary['key_1']


# ### Dictionaries are mutable
# 
# This means that dictionaries, once created, values *can* be updated.

# In[ ]:


completed_assignment = {
    'A1234' : True,
    'A5678' : False,
    'A9123' : True
}

completed_assignment


# In[ ]:


# change value of specified key
completed_assignment['A5678'] = True
completed_assignment


# Because dictionaries are mutable, key-value pairs can also be removed from the dictionary using `del`.

# In[ ]:


print(completed_assignment)
len(completed_assignment)


# In[ ]:


## remove key-value pair using del
del completed_assignment['A5678']

print(completed_assignment)
len(completed_assignment)


# ### Additional Dictionary Properties
# 
# - Only one value per key. No duplicate keys allowed. 
#     - If duplicate keys specified during assignment, the last assignment wins.

# In[ ]:


# Last duplicate key assigned wins
{'Student' : 97, 'Student': 88, 'Student' : 91}


# - **keys** must be of an immutable type (string, tuple, integer, float, etc)
# - Note: **values** can be of any type

# In[ ]:


# lists are not allowed as key types
# this code will produce an error
{['Student'] : 97}


# - Dictionary keys are case sensitive.
# 

# In[ ]:


{'Student' : 97, 'student': 88, 'STUDENT' : 91}


# #### Class Question #4
# 
# Fill in the '---' in the code below to return the value stored in the second key.

# In[ ]:


height_dict = {'height_1' : 60, 'height_2': 68, 'height_3' : 65, 'height_4' : 72}
height_dict[---]


# - A) I did it
# - B) I think I did it...
# - C) I tried and am stuck
# - D) No clue where to start...

# #### Class Question #5
# 
# Write the code that would create a dictionary `car` that stores values about your dream car's `make`, `model`, and `year`.
# 
# - A) I did it
# - B) I think I did it...
# - C) I tried and am stuck
# - D) No clue where to start...

# In[ ]:


# YOUR CODE HERE


# ## Revisiting membership: `in` operator

# <div class="alert alert-success">
# The <code>in</code> operator asks whether an element is present inside a collection, and returns a boolean answer. 
# </div>

# In[ ]:


# Define a new list and dictionary to work with
lst_again = [True, 13, None, 'apples']
dict_again = {'Shannon': 33, 'Josh': 41}


# In[ ]:


# Check if a particular element is present in the list
True in lst_again


# In[ ]:


# The `in` operator can also be combined with the `not` operator
'19' not in lst_again


# In[ ]:


# In a dictionary, checks if value is a key
'Shannon' in dict_again


# In[ ]:


# does not check for values in dictionary
33 in dict_again


# #### Class Question #6
# 
# After executing the following code, what will be the value of `output`?

# In[ ]:


ex2_lst = [0, False, 'ten', None]

bool_1 = False in ex2_lst
bool_2 = 10 not in ex2_lst

output = bool_1 and bool_2

print(output)


# - a) True
# - b) False
# - c) This code will fail
# - d) I don't know

# ## Unicode

# <div class="alert alert-success">
# Unicode is a system of systematically and consistently representing characters. 
# </div>

# Every character has a unicode `code point` - an integer that can be used to represent that character. 
# 
# If a computer is using unicode, it displays a requested character by following the unicode encodings of which `code point` refers to which character. 

# ### ORD & CHR

# <div class="alert alert-success">
# <code>ord</code> returns the unicode code point for a one-character string.
# </div>
# 
# <div class="alert alert-success"> 
# <code>chr</code> returns the character encoding of a code point. 
# </div>

# ### ord & chr examples

# In[ ]:


print(ord('a'))


# In[ ]:


print(chr(97))


# ### Inverses
# 
# `ord` and `chr` are inverses of one another. 

# In[ ]:


inp = 'b'
out = chr(ord(inp))

assert inp == out
print('Input: \t', inp, '\nOutput: ', out)


# ## Aside: Aliases
# 
# Note: This was introduced in the Variables lecture.

# In[ ]:


# Make a variable, and an alias
a = 1
b = a
print(b)


# Here, the value 1 is assigned to the variable `a`.  
# 
# We then make an **alias** of `a` and store that in the variable `b`. 
# 
# Now, the same value (1) is stored in both `a` (the original) and `b` (the alias).

# What if we change the value of the original variable (`a`) - what happens to `b`?

# #### Class Question #7
# 
# After executing the following code, what will the values stored in `a` and `b` be?

# In[ ]:


# Make a variable & an alias
# change value of original variable
a = 1
b = a
a = 2

print(a)
print(b)


# - A) `a` and `b` both store 1
# - B) `a` and `b` both store 2
# - C) `a` stores 2 `b` stores 1
# - D) `a` stores 1 `b` stores 2
# - E) No clue

# Reminder: integers are **immutable**.

# ### Alias: mutable types
# 
# What happens if we make an alias of a **mutable** variable, like a list?

# In[ ]:


first_list = [1, 2, 3, 4]
alias_list = first_list
alias_list


# In[ ]:


#change second value of first_list
first_list[1] = 29
first_list


# In[ ]:


# check alias_list
alias_list


# For *mutable* type variables, when you change one, both change.

# #### Class Question #8
# 
# After executing the following code, what will the second value stored in `second_tuple`?

# In[ ]:


# Make a variable & an alias
# change value of original variable
my_tuple = (1, 2, 3, 4)
second_tuple = my_tuple
my_tuple[1] = 29 


# - A) 1
# - B) 2
# - C) 29
# - D) This will Error
# - E) I'm lost.

# ### Why allow aliasing? 
# 
# Aliasing can get confusing and be difficult to track, so why does Python allow it?
# 
# Well, it's more efficient to point to an alias than to make an entirely new copy of a a very large variable storing a lot of data. 
# 
# Python allows for the confusion, in favor of being more efficient.
