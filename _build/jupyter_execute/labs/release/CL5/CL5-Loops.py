#!/usr/bin/env python
# coding: utf-8

# # CL5: Loops
# 
# Welcome to the fifth coding lab!
# 
# In this Coding Lab we will focus on debugging and understanding loops.

# **Note**: You may *not* be able to complete all of this in 50 minutes, particularly the challenges in Part 3.  This are meant to help you gain mastery and provide additional practices, not to stress you out a ton. Make a concerted effort. Do your best to complete it. But, if you don't figure it all out, that's why we post answers for coding labs!

# ## Part 1: Debugging

# ### Creating Errors
# For each of the follow Exceptions, write a small piece of code that will cause it to happen:
# - ZeroDivisionError
# - SyntaxError
# - IndentationError
# - TypeError
# - IndexError
# - ValueError
# - NameError

# In[ ]:


# ZeroDividisionError

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# SyntaxError

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# IndentationError

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# TypeError

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# IndexError

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# ValueError

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# NameError

# YOUR CODE HERE
raise NotImplementedError()


# ### Fixing Errors
# 
# For each of the following cells, try to debug the code to fix any errors, and get it running. 

# In[ ]:


if True
    print('It worked')
    
# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


age_string = "My favorite number is " + 27

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


print('Three plus five equals' + str(3+5)

# YOUR CODE HERE
raise NotImplementedError()


# ## Part 2: Loops Review & Exploration
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

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


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

# In[ ]:


counter = 0

while True:
    
    print("the value of 'counter' = " + str(counter))
    counter +=1
    
# YOUR CODE HERE
raise NotImplementedError()


# Now, rather than using `break`, edit the loop from above so that the condition following `while` will eventually evaluate as `False` (and thus terminate the loop).

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# ### Loop Explorations
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

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# ### Specific looping task
# 
# `print`ing the output is great to learn about and explore loops, but typically we're looping to generate some output. 
# 
# Generate a list below that stores various integers and strings. 
# 
# Write a loop that will separate out the elements in your list by type, such that all the integers are stored in a list called `my_ints` and all of the strings are stored in a list called `my_strs`

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


assert type(my_ints) == list
assert type(my_strs) == list

# check to make sure all values in each list are of expected type
assert all([type(x) == int for x in my_ints])
assert all([type(x) == str for x in my_strs])


# ## Part 3: Challenges
# 
# Give tese a shot, but it's definitely ok if you don't figure these out all the way! Remember, if you don't figure out the answer, definitely check the answer key when posted!

# ### Debugging Challenge
# 
# You're trying to write code that will count the number of vowels in your name, storing that value in `counter`. To get started, you store your name in the variable `my_name` and write the code you see below. However, the code below is not quite working...work to debug the code below to accomplish the task!
# 
# Note: This question uses a `for` loop. Next week's coding lab will get you lots of loops practice!

# In[ ]:


my_name == 'Shannon'
vowels = ['A','E','I','O','U', 'a', 'e', 'i', 'o', 'u']
counter = 0

for char in my_name:
    if char == vowels:
        counter =  1

# YOUR CODE HERE
raise NotImplementedError()


# ### Nested Loop Challenge
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

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# If you get the above pattern working, try manipulating the code to print out different patterns, and with different symbols. 

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# ## The End!
# 
# This is the end of this Coding Lab!
# 
# Be sure you've made a concerted effort to complete all the tasks specified in this lab. Then, go ahead and submit on datahub!
