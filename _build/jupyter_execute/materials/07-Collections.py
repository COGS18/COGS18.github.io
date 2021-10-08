#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - **A1** due Fri
#     - A staff member brought to my attention that some students thought A1 wasn't due until Monday (CL1 slide issue)
#     - As a result, you can turn in A1 until the late deadline (Mon; 11:59 PM) without late penalty
#     - The late deadline will *not* be extended.
# - **A2** is now available (due next Friday)
# - **Posts on Campsuwire with answers to an assignment question must be private to TAs/Instructors**

# **Common Confusions**
# - `=` vs `==` : introduced in operators lecture; discussed in depth Wed 10/6 (starting 22:58)
# - detecting whether a substring is contained in a string - introduced in operators discussing membership operators; also Holly (TA) made post on Campuswire
# - not sure what the `%run -i ./A1Code/q7_code.py`  does - see explanation at beginning of Fri 10/1 (starting 5:38)

# **Q&A**
# 
# Q: In the assignments, what are some examples of the hidden tests? How can we be more sure that we are passing those hidden tests?  
# A: Often, the hidden tests check for the correct value directly. For example, if we ask you to add 6 and 7 and store it in the variable `my_var`, the hidden assert would be `assert my_var == 13`. The way you can be sure is by reading and understanding the instructions and being sure your code does what is being asked. Using `print()` statements is a good way to check your work.
# 
# Q: Will out midterm timed or it allows us to finish with no time limit?  
# A: It won't be timed, but there will be a time window. For example, you will have ~24h to complete...and you could, theoretically, spend the entire time on it...although that will not be necessary and is not advised.
# 
# Q: Are the textbook question exam styled questions? if not, where can we access those?  
# A: Some of the textbook questions are from previous COGS 18 exams. I will also provide you with a practice exam. The questions on that come from previous exams.
# 
# 
# Q: Also, how do we access campuswire? I made an account but I cannot see the class.   
# A: https://campuswire.com/p/G3CF63BDA and use the access code on Canvas.
# 
# Q: When we have multiple errors in code that we need to fix, is it advised that we go back and clear/rerun the kernel?  
# A: Not necessarily. However, if you've created a bunch of variables and you're not sure which you need and which you don't and have deleted a bunch of code but can't remember exactly what you deleted, then go ahead and restart your kernel - will give you a clean slate.

# # Collections
# 
# - Lists
#     - Indexing
#     - Mutating
# - Tuples

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


# #### Clicker Question #1
# 
# Which of the following specifies a list of 4 items?

# In[ ]:


item_A = [0, 'string', 18]
item_B = (0, 'string', 18, 'name')
item_C = [0, 'string', 18, 'name']
item_D = (0, 'string', 18)
item_E = [1234]


# - A) item_A
# - B) item_B
# - C) item_C
# - D) item_D
# - E) item_E

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


# can determine type in list
type(my_lst[2])


# In[ ]:


my_lst[2:-1]


# In[ ]:


# indexing to end of list
print(my_lst[2:])


# In[ ]:


# Indexing from beginning of list
print(my_lst[:4])


# In[ ]:


# slicing by skipping a value [start:stop:step]
print(my_lst[0:4:2])


# ### Index Practices

# In[ ]:


# Define a list for the examples
example_lst = [1, 2, 3, 4, 5]


# In[ ]:


example_lst[2]


# In[ ]:


example_lst[-3]


# In[ ]:


example_lst[1:3]


# #### Clicker Question #2
# 
# What will be the output of the following piece of code:

# In[ ]:


q2_lst = ['a', 'b', 'c','d']
q2_lst[-3:-1]


# - A) ['a', 'b', 'c']
# - B) ['c', 'b', 'a']
# - C) ['c', 'b']
# - D) ['b', 'c', 'd']
# - E) ['b', 'c']

# Note: The following has been added to the notes due to student questions in previous iterations. This and the following two cells are *not* someting you'll be tested on. Including as an FYI for those curious.
# 
# You *can* return ['c','b'] but it combines two different concepts.
# 
# 1. the `start:stop` now refers to indices in the reverse.
# 2. `-1` is used as the step to reverse the output.
# 
# More details about `step`:  
# `step`: the amount by which the index increases, defaults to 1. If it's negative, you're slicing over the iterable in reverse.

# In[ ]:


# slice in reverse
q2_lst[-2:-4:-1]


# In[ ]:


# you can use forward indexing
# makes this a little clearer
q2_lst[2:0:-1]


# #### Clicker Question #3
# 
# What would be the appropriate line of code to return `['butter', '&', 'jelly']`?

# In[ ]:


q3_lst = ['peanut', 'butter', '&','jelly']


# - A) `q3_lst[2:4]`
# - B) `q3_lst[1:3]`
# - C) `q3_lst[:-2]`
# - D) `q3_lst[-3:]`
# - E) `q3_lst[1:4:2]`

# ### Reminders

# - Python is zero-based (The first index is '0')
# - Negative indices index backwards through a collection
# - A sequence of indices (called a slice) can be accessed using `start:stop`
#     - In this contstruction, `start` is included then every element until `stop`, not including `stop` itself
#     - To skip values in a sequence use `start:stop:step`

# ### SideNote: But why is it like this...

# <div class="alert alert-success">
# Starting at zero is a convention (some) languages use that comes from how variables are stored in memory
# , and 'pointers' to those locations.
# </div>

# ### Length of a collection

# In[ ]:


# Define a new list
another_lst = ['Peter', 'Hind', 'Jack', 'Pam', 'Barbara', 'Colin', 'Felix']

# Get the length of the list, and print it out
len(another_lst)


# ## The `in` Operator

# <div class="alert alert-success">
# The <code>in</code> operator asks whether an element is present inside a collection, and returns a boolean answer. 
# </div>

# In[ ]:


# Define a new list to work with
lst_again = [True, 13, None, 'apples']


# In[ ]:


# Check if a particular element is present in the list
True in lst_again


# In[ ]:


# The `in` operator can also be combined with the `not` operator
'19' not in lst_again


# ### Practice with `in`

# In[ ]:


# Define a list to practice with
practice_lst = [1, True, 'alpha', 13, 'cogs18']


# In[ ]:


13 in practice_lst


# In[ ]:


False in practice_lst


# In[ ]:


'True' in practice_lst


# In[ ]:


#searching partial strings
'cogs' in practice_lst


# In[ ]:


'cogs18' not in practice_lst


# #### Clicker #4
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

# ### Reminder

# - The `in` operator checks whether an element is present in a collection, and can be negated with `not`

# ## Mutating a List

# <div class="alert alert-success">
# Lists are <i>mutable</i>, meaning after definition, you can update and change things about the list.
# </div>

# In[ ]:


# Define a list
updates = [1, 2, 3]


# In[ ]:


# Check the contents of the list
print(updates)


# In[ ]:


# Redefine a particular element of the list
updates[1] = 0


# In[ ]:


# Check the contents of the list
print(updates)


# #### Clicker Question #5
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
# A <b>tuple</b> is an <i>immutable</i> collection of ordered items, that can be of mixed type. Tuples are created using parentheses.
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


# #### Clicker Question #6
# 
# Which of the following specifies a tuple of 4 items?

# In[ ]:


item_A = [0, 'string', 18]
item_B = (0, 'string', 18, 'name')
item_C = [0, 'string', 18, 'name']
item_D = (0, 'string', 18)
item_E = [1234]


# - A) item_A
# - B) item_B
# - C) item_C
# - D) item_D
# - E) item_E

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

# #### Clicker Question #7
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

# #### Clicker Question #8
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

# ## Strings as Collections

# <div class="alert alert-success">
# Strings act similarly to ordered collections of homogenous elements - specifically characters. But, they are <b>immutable</b>.
# </div>

# In[ ]:


# Define a string
my_str = 'TheFamousFive'


# In[ ]:


# Index into a string
my_str[2]


# In[ ]:


# Ask if an item is in a string
'Fam' in my_str


# In[ ]:


# Check the length of a string
len(my_str)


# In[ ]:


# Index into a string
# This code will produce an error
my_str[1:3] = 'HE'


# ### SideNote: using counters

# In[ ]:


# Initialize a counter variable
counter = 0 
print(counter)


# In[ ]:


counter = counter + 1
print(counter)


# In[ ]:


counter = counter + 1
print(counter)


# ## Pulling it Together: Collections, Membership & Conditionals

# #### Clicker Question #9
# 
# What will be the value of `counter` after this code is run?

# In[ ]:


things_that_are_good = ['python', 'data', 'science', 'tacos']

counter = 0

if 'python' in things_that_are_good:
    counter = counter + 1

if len(things_that_are_good) == 4:
    counter = counter + 1
    
if things_that_are_good[2] == 'data':
    counter = counter + 1 
    
print(counter)


# <pre> A) 0   B) 1   C) 2   D) 3   E) 4 </pre>

# #### Clicker Question #10
# 
# What will be printed out from running this code?

# In[ ]:


lst = ['a', 'b', 'c']
tup = ('b', 'c', 'd')

if lst[-1] == tup[-1]:
    print('EndMatch')
elif tup[1] in lst:
    print('Overlap')
elif len(lst) == tup:
    print('Length')
else:
    print('None')


# <pre> A) EndMatch   B) Overlap   C) Length   D) Overlap & Match   E) None </pre>
