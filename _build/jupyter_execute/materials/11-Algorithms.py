#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# **Due Dates**
# - CL5 due Wednesday (11:59 PM)
# - A3 due Monday 11/1 (11:59 PM)
# 
# **Notes**
# - CL4 grades have been posted
# - E1 grades will be posted later today (there will be an accompanying Campuswire post)

# **Q&A**
# 
# Q: Are there any meaning behind using ( ), [ ], or { } for different commands? Or is it just to make it easy to differentiate between types.  
# A: When creating/defining variables, these indicate types. When indexing, it will always be `[]`. When calling a function it will always be `()`.
# 
# Q: Is it required to make a new variable inside of a function and then return that function as opposed to just returning the values directly?  
# A: Nope. You can return it directly.
# 
# Q: Why is it that for clicker question #3 we used assignment (`=`) rather than a colon (`:`)?  
# A: This is because we were updating values within the dictionary. When updating a value in a mutable variable, we do that by assignment (`=`).
# 
# Q: This is from clicker question #3. What exactly is the '+=' operator, and what is it used for?   
# A: `var += 6` is shorthand for `var = var + 6`. It says to add to the end *and* store it in the variable specified.
# 
# Q: Can we write more than two parameters when we define a function?  
# A: Yup! 
# 
# Q: For clicker question #3, do I have to define counter as literally "counter'? Is it okay if I use other variables like n for the counter? I think I've done that on the exam 1.  
# A: You can definitely use different variable names!
# 
# Q: What does * mean? It often shows up on the python while doing the coding lab.   
# A: This indicates that your code is still running. Typically, this shows up when you have an infinite loop in your code that is running forever. You'll want to stop (square icon at the top) the cell, edit your code to remove the infinite loop, and then rerun the cell before running any other code.
# 
# Q: When do we use return vs. print  
# A: We'll use `return` at the end of every function to return our output. `print()` statemetns are for checking your work/understanding.
# 
# Q: When do we use loops? When do we use functions?  
# A: Functions are most helpful when you want to execute code on an input, where that input can change each time you execute the function. Loops are helpful when you want to execute the same lines of code across a specific collection (`for` loop) or while a condition is true (`while` loop).
# 

# # Algorithms
# 
# What are the sorts of things that we should do with computers? What are things that are easy to compute? Hard to compute? Impossible to compute?

# ## Algorithms

# <div class="alert alert-success">
# An <b>algorithm</b> is a formal description of how to complete a procedure, typically taking inputs and returns some output.
# </div>

# If you can write the steps down, you can write an algorithm.
# 
# Algorithms are computable.

# Computers cannot read between the lines. They are very literal.

# ## Algorithm Example: Making a Sandwich

# #### Clicker Question #1
# 
# Can you write an algorithm to make a ham and cheese sandwich. 
# 
# - A) Yes 
# - B) No
# - C) I don't know

# ## Algorithm for making a ham & cheese sandwich
# 
# 

# Humans are pretty good at making sandwiches. Computers may struggle a bit.

# ## Algorithm Example: Sorting
# 
# Given a list of numbers, how can we sort it into the correct order?

# In[ ]:


# Define a list of numbers
list_of_numbers = [2, 1, 3]  


# #### Clicker Question #2

# **array**: a collection of items, where each item can be accessed by its index.

# Can you write an algorithm to sort an array?
# 
# - A) Yes 
# - B) No
# - C) I don't know

# Y'all Google is *really* good at sorting.
# 
# - ranking: rate a site as how related
# - sort: given a list of good sites, determine order to present to user
# 
# ...and do this on all the things

# ## `sort_array`
# 
# A version of a **selection sort**:
# - loop through current list
# - find lowest item
# - put that at the front of your sorted list
# - remove lowest item from current list
# - wash, rinse, repeat

# In[ ]:


def sort_array(array_to_sort):
    """A function to sort an array."""

    is_sorted = False    # Keeps track of when we are done sorting
    sorted_array = []    # A new list that we will use to 
     
    while not is_sorted:

        lowest = None
        for item in array_to_sort:
            if lowest == None:         # If not defined (first element) set the current element as lowest
                lowest = item
            if item < lowest:
                lowest = item
        
        # these next two lines use new methods
        sorted_array.append(lowest)    # Add the lowest value to our sorted array output
        array_to_sort.remove(lowest)   # Drop the now sorted value from the original array

        if len(array_to_sort) == 0:    # When `array_to_sort` is empty, we are done sorting
            is_sorted = True
    
    return sorted_array


# ## Using `sort_array`

# In[ ]:


# Sort an array of integers
unsorted_array = [12, 7, 19, 12, 25]
sorted_array = sort_array(unsorted_array)
print(sorted_array)


# In[ ]:


# Sort an array of floats
unsorted_array = [21.3, 56.7, 2.3, 2.9, 99.9]
sorted_array = sort_array(unsorted_array)
print(sorted_array)


# #### Clicker Question #3
# 
# Using our `sort_array` function from above, what will the following code snippet print out:

# In[ ]:


data = ['a', 'c', 'b'] 
sort_array(data)


# - A) ['a', 'c', 'b']
# - B) ['a', 'b', 'c']
# - C) [97, 98, 99]
# - D) None
# - E) This code will fail

# ### How Python evaluates strings

# In[ ]:


'a' < 'b'


# In[ ]:


ord('a')


# In[ ]:


ord('b')


# #### Clicker Question #4
# 
# Using our `sort_array` function from above, what will the following code snippet print out:

# In[ ]:


data = [True, False, True]
sort_array(data)


# - A) [False, True, True] 
# - B) [True, False, True] 
# - C) [0, 1, 1]
# - D) [True, True, False] 
# - E) This code will fail

# ### How Python evaluates Booleans

# In[ ]:


True < False


# In[ ]:


bin(True)


# In[ ]:


bin(False)


# #### Clicker Question #5
# 
# Using our `sort_array` function from above, what will the following code snippet print out:

# In[ ]:


data = [[1, 4], [1, 2]]
sort_array(data)


# - A) [[1, 4], [1, 2]]  
# - B) [1, 1, 2, 4] 
# - C) [[1, 2], [1, 4]]
# - D) None 
# - E) This code will fail

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


# ## Algorithmic Complexity

# <div class="alert alert-success">
# The complexity of an algorithm characterizes the relationship between the input size and the number of steps of an algorithm.
# </div>

# ## Algorithmic Complexity 
# 
# Things we might care about:
# - The number of steps it takes to complete our algorithm
#     - Usually defined in relation of the size of the input
# - The amount of memory it will take to run our algorithm

# ## Properties of our sorting algorithm
# 
# - It will require $n^2$ steps, where $n$ is the length of the list
# - It will require ~double the memory of the original list

# ## Computability

# Things that computers can do are things that we can write down an algorithm to do.
# 
# Things that we can write an algorithm to do are things that we can define a specific set of steps to complete.

# ## Variable Type Checking
# 
# **Note**: The rest of the noteook includes notes to answer a student's in class question. You will not be tested on this, but it will be helpful to understand and may be necessary for your final project.
# 

# To check on an input variable's type, you can use either of the following approaches:
# 
# ```python
# type(object) == type
# ```
# OR 
# 
# ```python
# isinstance(object, classinfo) 
# ```
# 
# `isinstance()` takes two parameters:
# - `object` : variable/object to be checked
# - `classinfo` : class, type, or tuple of classes and types

# For example, using the `string_manipulator` function from earlier, note that I've added the following two lines: 
# 
# ```python
# if not isinstance(string, str):
#     print("Warning: please provide a string as input")
# ```
# 
# This checks to see if the input is anything other than a string. If it is, the function prints a warning.

# In[ ]:


def string_manipulator(string):
    
    if type(string) != str:
        print("Warning: please provide a string as input")
    else:
        output = ''
        for char in string:
            if char == 'a' or char == 'e':
                char = 'z' 
            output = output + char
    
        return output


# In[ ]:


# use function with a string
string_manipulator('hello!')


# In[ ]:


# print warning if not a string
string_manipulator(5)


# However, sometimes, you want it to raise an error rather than just print something. Here we use `raise` instead of print. In this case, an error will be returned (with our specified message) to the user if the wrong variable type is provided:

# In[ ]:


def string_manipulator(string):
    
    if type(string) != str:
        raise ValueError("Please provide a string as input")
    else:
        output = ''
        for char in string:
            if char == 'a' or char == 'e':
                char = 'z' 
            output = output + char
    
        return output


# In[ ]:


# raise error instead of print message
string_manipulator(5)

