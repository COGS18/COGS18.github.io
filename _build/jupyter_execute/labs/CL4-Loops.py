#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# figure out what to keep


# # CL4: Loops
# 
# Welcome to the fourth coding lab!
# 
# In this Coding Lab we will really focus in on understanding loops.

# **Note**: You may *not* be able to complete all of this in 50 minutes, particularly the challenge in Part 3.  This are meant to help you gain mastery and provide additional practices, not to stress you out a ton. Make a concerted effort. Do your best to complete it. But, if you don't figure it all out, that's why we post answers for these!

# ## Part 2: Debugging Questions

# ### Creating Errors
# For each of the follow Exceptions, write a small piece of code that will cause it to happen:
# - ZeroDivisionError
# - SyntaxError
# - IndentationError
# - TypeError
# - IndexError
# - ValueError
# - NameError

# In[8]:


# ZeroDividisionError

### BEGIN SOLUTION
# Zero Division Answer
1/0
### END SOLUTION


# In[9]:


# SyntaxError

### BEGIN SOLUTION
# Syntax Answer
for el in [1, 2]
    print(el)
### END SOLUTION


# In[10]:


# IndentationError

### BEGIN SOLUTION
# Indentation Error
for el in [1, 2]:
print(el)
### END SOLUTION


# In[11]:


# TypeError

### BEGIN SOLUTION
# Type error
(1, 2) + (2)
### END SOLUTION


# In[12]:


# IndexError

### BEGIN SOLUTION
# Index Error
lst = [1, 2]
lst[2]
### END SOLUTION


# In[13]:


# ValueError

### BEGIN SOLUTION
# Value Error
int('a')
### END SOLUTION


# In[14]:


# NameError

### BEGIN SOLUTION
# Name Error
a
### END SOLUTION


# ### Fixing Errors
# 
# For each of the following cells, try to debug the code to fix any errors, and get it running. 

# In[ ]:


if True
    print('It worked')
    
### BEGIN SOLUTION
# Answer: add a ':' to open the conditional code block
if True:
    print('It worked')
### END SOLUTION


# In[ ]:


age_string = "My favorite number is " + 27

### BEGIN SOLUTION
# Answer: typecase int to string
age_string = "My favorite number is " + "27"
# OR
age_string = "My favorite number is " + str(27)
### END SOLUTION


# In[ ]:


print('Three plus five equals' + str(3+5)

### BEGIN SOLUTION
# Answer: Missing closing parenthesis - add ')' at the end
print('Three plus five equals' + str(3+5))

### END SOLUTION


# ### Debugging Challenge
# 
# You're trying to write code that will count the number of vowels in your name, storing that value in `counter`. To get started, you store your name in the variable `my_name` and write the code you see below. However, the code below is not quite working...work to debug the code below to accomplish the task!
# 
# Note: This question uses a `for` loop. Next week's coding lab will get you lots of loops practice!

# In[2]:


my_name == 'Shannon'
vowels = ['A','E','I','O','U', 'a', 'e', 'i', 'o', 'u']
counter = 0

for char in my_name:
    if char == vowels:
        counter =  1

### BEGIN SOLUTION
# code will differ based on who is taking the exam
my_name = 'Shannon'
counter = 0

for char in my_name:
    if char in vowels:
        counter += 1
### END SOLUTION


# ## Part 3: Collection types
# 
# Collections are Python variable types than can store a 'collection' of items.

# ### Collection Questions
# 
# Create a list and a tuple. Fill them with with any values you want. 
# 
# Call them `my_list` and `my_tuple`.

# In[5]:


### BEGIN SOLUTION
# specific values will differ

my_list = [1, 2, 3]
my_tuple = ('a', 'b', 'c')
### END SOLUTION


# In[7]:


assert isinstance(my_list, list)
assert isinstance(my_tuple, tuple)


# Use the following cells to check the types of the variables you write are as expected

# In[19]:


type(my_list)


# In[20]:


type(my_tuple)


# #### Declaring Collections
# 
# Note that there can be more than one way to declare collections. 
# 
# As well as declaring them with '[]' and '()', we can use the list & tuple constructors, as shown below. 

# In[21]:


# Run me! - This creates another list & tuple, using the list & tuple constructors
some_list = list([1, 2, 3, 4, 5])
some_tuple = tuple(["peanut", "butter", "and", "jelly"])

print("'some_list' contains: \t", some_list)
print("'some_tuple' contains: \t", some_tuple)


# Compare the types of these variables to your equivalent variables to confirm.
# 
# In the cell below, write in the type of the objects that you expect them to be, and make sure the asserts pass. 

# In[ ]:


# Fill in `_WRITE_IN_TYPE_HERE` with the type you expect each variable to be
assert isinstance(some_list, _WRITE_IN_TYPE_HERE_)
assert isinstance(some_tuple, _WRITE_IN_TYPE_HERE_)

### BEGIN SOLUTION
assert isinstance(some_list, list)
assert isinstance(some_tuple, tuple)
### END SOLUTION


# ### Indexing
# 
# Given the following list, do the following operations:
# - Get the length of the list (assign this to a variable `lst_len`)
# - Get the 1st element of the list (call the selection `ind1`)
# - Get the last element of the list (call the selection `ind2`)
# - Get the second to the fourth element of the list (call the selection `ind3`)
# - Get from the fifth element, to the end of the list (call the selection `ind4`)
# - Get every second element of the list, starting at the first element (call the selection `ind5`)
# - Get every second element of the list, starting at the second element (call the selection `ind6`)

# In[23]:


my_lst = ['a', True, 12, 'tomato', False, None, 23, 'python', [], 5.5]


# In[24]:


### BEGIN SOLUTION
lst_len = len(my_lst)
ind1 = my_lst[0]
ind2 = my_lst[-1]
ind3 = my_lst[1:4]
ind4 = my_lst[4:]
ind5 = my_lst[0::2]
ind6 = my_lst[1::2]
### END SOLUTION


# In[ ]:





# ## Part 1: Loops Review
# 
# We will now explore two ways to iterate over data in Python - `for` and `while` loops. 
# 
# Each type of loop performs its respective code block until certain conditions are met. Here, we will explore what those conditions are. 
# 
# Note: "iterate" means to perform an action repeatedly 
# 
# Note: Sometimes, we accidentally make loops that never end. 
# - If that happens, "break" the cell by selecting it and then pressing "ctrl+c". Alternatively, press the "stop" button (square icon) in the Jupyter toolbar. 

# ### Loops 
# 
# First, declare a variable called `counter` that has type int and value zero.
# 
# Then write a `while` loop that runs 10 times and use `counter` to track how many times the loop runs. 

# In[6]:


### BEGIN SOLUTION
counter = 0
while counter < 10:
    counter = counter + 1
### END SOLUTION


# In[7]:


# Check that (after the loop runs) that there is a variable called `counter` that has value 10
assert counter == 10


# ### Infinite Loops
# 
# The while loop below will run indefinitely unless someone puts a stop to it! 
# 
# Add your own code that causes the loop to exit when the `counter` variable reaches 10. You can use `break` to do this. 
# 
# Note: Sometimes, we accidentally make loops that never end - try that by running the cell below before adding 
# 
# If that happens, interrupt the cell by selecting it and then pressing "ctrl+c". Alternatively, press the "stop" button (square icon) in the Jupyter toolbar. 
# 
# For refernece, the starter code provided is:
# ```python
# counter = 0
# 
# while True:
#     
#     print("the value of 'counter' = " + str(counter))
#     counter +=1
#     
# ```

# In[8]:


counter = 0

while True:
    
    print("the value of 'counter' = " + str(counter))
    counter +=1
    
### BEGIN SOLUTION
    if counter >= 10:
        break
### END SOLUTION


# Now, rather than using `break`, edit the loop from above so that the condition following `while` will eventually evaluate as `False` (and thus terminate the loop).

# In[9]:


### BEGIN SOLUTION
counter = 0

# edit condition
while counter < 10:
    
    print("the value of 'counter' = " + str(counter))
    counter +=1
### END SOLUTION


# ## Part 2: Loop Explorations
# 
# Now, explore using for and while loops and breaks. 
# 
# Here are some things to try, and questions to ask - each of which you should explore in code. 
# - What happens if you use 'break' all by itself?
# - What are some different ways to loop through a list? tuple?
# - Write these combinations: 
#     - a `for` loop with a `break`, a `for` loop with a `continue`
#     - a `while` loop with a `break`, a `while` loop with a `continue`
# - Write some loops that loop across lists:
#     - Write a loop that loops across, and prints out, all the elements of a list
#     - Write a loop that loops across, and prints out, every second element of a list
#     - Write a loop that loops across, and prints out, every element of a list in reverse order
#     - Write a loop that loops across, and prints out, the first half of a list
# - Write a loop with a conditional inside it.
# - Can you have loops inside loops? If you think so, try and write a nested loop. 
# 
# Reminder: you can add as many cells as you'd like to test these out! 

# In[5]:


### BEGIN SOLUTION
my_list = [1, 2]
my_tuple = ('a', 'b')

# You can loop through lists or tuples directly, or with indices
# Loop through list with for - same goes for tuple
for el in my_list:
    print(el)

print('')
    
# Loop through tuple using indexing - same goes for list
for ind in range(2):
    print(my_tuple[ind])

#- Write these combinations: 
#    - a `for` loop with a `break`, a `for` loop with a `continue`
#    - a `while` loop with a `break`, a `for` loop with a `continue`

letter_list = ['a', 'c', 'e']

for it in letter_list:
    if it == 'c':
        break

for it in letter_list:
    if it == 'a':
        continue

# While loops with break and continue
ind = 0

while ind < 5:
    if ind == 2:
        break
    ind = ind + 1

while ind < 5:
    ind = ind + 1
    if ind == 2:
        continue

# These are loops using indexing, to grab different elements of the list
another_list = [1, 2, 3, 4]

print('Print all elements list:')
for it in another_list:
    print(it)
print('')
    
print('Print every second element list:')
for it in another_list[1::2]:
    print(it)
print('')

print('Print reversed list:')
for it in another_list[::-1]:
    print(it)
print('')

print('Print first half:')
half_index = int(len(another_list)/2)
for it in another_list[0:half_index]:
    print(it)
print('')

# Loop with a conditional in it
for it in [True, False]:
    if it == True:
        print('Yay.')

# Yes, you can have a loop inside a loop
for a_val in [1, 2, 3]:
    for b_val in ['a', 'b', 'c']:
        print(a_val, b_val)


### END SOLUTION


# ### Specific looping task
# 
# `print`ing the output is great to learn about and explore loops, but typically we're looping to generate some output. 
# 
# Generate a list below that stores various integers and strings. 
# 
# Write a loop that will separate out the elements in your list by type, such that all the integers are stored in a list called `my_ints` and all of the strings are stored in a list called `my_strs`

# In[1]:


### BEGIN SOLUTION
# the specific list you create is up to you
my_list = [1, "apple", 15, "banana", 29, 30, "yay python!"]
my_ints = []
my_strs = []

for val in my_list:
    if type(val) == int:
        my_ints.append(val)
    elif type(val) == str:
        my_strs.append(val)
        
print(my_ints)
print(my_strs)
### END SOLUTION


# In[4]:


assert type(my_ints) == list
assert type(my_strs) == list

# check to make sure all values in each list are of expected type
assert all([isinstance(x, int) for x in my_ints])
assert all([isinstance(x, str) for x in my_strs])


# ## Part 3: Nested Loop Challenge
# 
# Using nested loops, you will print out a pattern that looks like this:
# 
# 1 <br>
# 1 2 <br>
# 1 2 3 <br>
# 1 2 3 4 <br>
# 1 2 3 4 5 <br>
# 1 2 3 4 5 6 <br>
# 1 2 3 4 5 6 7
# 
# Hints:
# - You can do this with two while loops, one inside the other.
# - You will have two indices counters, one for each loop. 
# - For the print statement, it will look something like `print(index_inner, end=" ")`

# In[3]:


print("a", end=" ")
print("b")


# In[6]:


### BEGIN SOLUTION
index_outer = 1
while index_outer < 8:
    
    index_inner = 1
    
    while index_inner <= index_outer:
        print(index_inner, end=" ")
        index_inner = index_inner + 1
        
    print("")
    index_outer = index_outer + 1
### END SOLUTION


# If you get the above pattern working, try manipulating the code to print out different patterns, and with different symbols. 

# In[ ]:




