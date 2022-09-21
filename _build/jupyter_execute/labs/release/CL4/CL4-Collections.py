#!/usr/bin/env python
# coding: utf-8

# # CL4: Collections
# 
# Welcome to the fourth coding lab!
# 
# In this Coding Lab we will focus on working with collections and get additional practice with conditionals and functions.

# ## Part I: Collections
# 
# Collections are Python variable types than can store a 'collection' of items.
# 
# Here we'll practice defining collections and indexing.

# ### Collection Questions
# 
# Create a list, a tuple, and a dictionary. Fill them with with any values you want. 
# 
# Call them `my_list`, `my_tuple`, and `my_dictionary`.

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# Use the following cells to check the types of the variables you write are as expected

# In[ ]:


type(my_list)


# In[ ]:


type(my_tuple)


# In[ ]:


type(my_dictionary)


# On an assignment, you'd likely see the same concept tested with the following `assert` statements

# In[ ]:


assert type(my_list) == list
assert type(my_tuple) == tuple
assert type(my_dictionary) == dict


# #### Declaring Collections
# 
# Note that there can be more than one way to declare collections. 
# 
# As well as declaring them with '[]' and '()', we can use the list & tuple constructors, as shown below. 

# In[ ]:


# Run me! - This creates another list & tuple, using the list & tuple constructors
some_list = list([1, 2, 3, 4, 5])
some_tuple = tuple(["peanut", "butter", "and", "jelly"])
some_dict = dict([('First', 'Shannon'), ('Last', 'Ellis')])

print("'some_list' contains: \t", some_list)
print("'some_tuple' contains: \t", some_tuple)
print("'some_dict' contains: \t", some_dict)


# Compare the types of these variables to your equivalent variables to confirm.
# 
# In the cell below, write in the type of the objects that you expect them to be, and make sure the asserts pass. 

# In[ ]:


# Fill in `_WRITE_IN_TYPE_HERE` with the type you expect each variable to be
assert type(some_list) == _WRITE_IN_TYPE_HERE_
assert type(some_tuple) == _WRITE_IN_TYPE_HERE_
assert type(some_dict) == _WRITE_IN_TYPE_HERE_

# YOUR CODE HERE
raise NotImplementedError()


# ### Indexing
# 
# Given the following list (`my_lst`, defined below), do the following operations:
# - Get the length of the list (assign this to a variable `lst_len`)
# - Get the 1st element of the list (call the selection `ind1`)
# - Get the last element of the list (call the selection `ind2`)
# - Get the second to the fourth element of the list (call the selection `ind3`)
# - Get from the fifth element, to the end of the list (call the selection `ind4`)
# - Get every second element of the list, starting at the first element (call the selection `ind5`)
# - Get every second element of the list, starting at the second element (call the selection `ind6`)

# In[ ]:


my_lst = ['a', True, 12, 'tomato', False, None, 23, 'python', [], 5.5]


# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# ## Part II: Collections + Conditionals
# 
# Collections can work with all of the things we've discussed up to this point - variables, conditionals, functions, etc. Here, we'll get extra practice combining collections with conditionals.

# ### Collections + Conditionals Question
# 
# Imagine you've asked a group of young children to make a pile of at least 5 toys. 
# 
# You then want to write code to determine if the kid accomplished the task. Specifically, if the pile has at least 5 toys, you want `output` to store the string `'success'`. Otherwise, you want `output` to store the string `'try again'`
# 
# The toys placed in one of these kids' piles is defined below in the list `kid_a`. Using this list, and conditionals, write code to accomplish the task above! 

# In[ ]:


kid_a = ['truck', 'barbie', 'coloring book', 'dinosaur']


# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


assert output in ['success', 'try again']


# ## Part III: Collections + Conditionals + Functions
# 
# Let's put all of these conepts together...!

# ### Collections + Conditionals + Functions Question 
# 
# The code you generated in Part II will only work on a single list `kid_a`. Functions, on the other hand, are ways to define a set of instructions that can operate on various input, returning the correct output.
# 
# Here, write a function `toy_pile()` that accomplishes the same task as above, but takes a list of toys as input and `returns` either `'success'` or `'try again'`, depending upon how many toys are in the list of toys.
# 

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# test out your function here 


# In[ ]:


assert toy_pile(kid_a) == 'try again'


# In[ ]:


assert toy_pile(['lego', 'princess dress', 'tinker toy', 'doll', 'stroller']) == 'success'


# ### Putting it all together
# 
# Now that you've seen an example, think up another situation where you could write a function that incorporates the following:
# 
# - takes a dictionary as input
# - utilizes a conditional within the function
# - carries out some operation and `return`s some output
# 
# First, explain what your function does in plain English in the cell below. Then, write the python code for the function in the following cell and test it out in the last cell.

# Explain your function here (in words, not code)

# In[ ]:


# define your function here
# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# test out/execute your function here


# ## The End!
# 
# This is the end of this Coding Lab!
# 
# Be sure you've made a concerted effort to complete all the tasks specified in this lab. Then, go ahead and submit on datahub!
