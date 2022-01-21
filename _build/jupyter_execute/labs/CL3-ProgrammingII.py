#!/usr/bin/env python
# coding: utf-8

# # Coding Lab 3: Programming II
# 
# Welcome to the third coding lab!
# 
# CodingLab labs are meant to be interactive - so find another person to work together with on this notebook if you're able.
# 
# CodingLabs are also meant to be exploratory. There are broad questions in the notebook that you should explore, and try to answer - but you are also very much encouraged to explore other related ideas as you go! 
# 
# If you have a question about how something works / what something does - try it out, and see what happens!

# ## Part I: PseudoCode
# 
# First, let's briefly consider the idea of pseudocode. 
# 
# Pseudocode is an informal, 'high-level' sketch or description of a program or algorithm. 
# 
# It will typically resemble the structure of a program, but the details to make it actually run have not been fleshed out. 

# ### Pseudocode Human Language
# 
# Some pseudocode is written in human level language, in a way that sketches out the tasks and general control flow. 
# 
# This highly abstract pseudocode is often not specific to any particular programming language. 

# ```
# # PseudoCode for checking if a student got full credit on assignment
# 
# function that takes a list of student ids with student grades
# 
#     create an output object to collect full credit
# 
#     for student in list of grades
# 
#         if grade of student is equal to max grade
#             add to list of full credits
# 
#     return list of students who got full credit
# ```

# ### Pseudocode in Python format
# 
# You can also write pseudocode, that is much closer to Python (including Python syntax) but maintains more of a template / outline. 
# 
# Pseudocode like this is sometimes just a work-in-progress that is just not yet finished. 
# 
# Note the use of the `pass` keyword - `pass` is just a placeholder keyword that does nothing.

# In[1]:


# PseudoCode for a function to email a list of emails, and return a log of what was sent
def sent_emails(list_of_emails):

    emails_sent = {}  # Define an output variable for the logging

    for email in list_of_emails: # loop through all of the emails in a list of emails

        # Send email to current student
        pass

        # Add logging information that email was sent
        email_sent[email] = True

    return emails_sent


# ## Part II: Computation &  Algorithms
# 
# Both computers and humans are good at some things, and bad at others. However, it tends to be different things that computers and humans are good at. 
# 
# Here is a list of possible tasks that a human and/or computer could try and do:
# 
# - Given a list of 100K values, find the average and range of the list
# - Sort an array of randomly generated numbers from smallest to largest
# - Recognize the saddest part of a movie
# - Recall specific facts, like answering 'which day of the week was the 1st of June, 1997?'
# - Identify the likely country of origin of a person from their accent
# - Create a meme
# - Sort a list of 10,000 names alphabetically
# - Rank memes in order of how funny they are
# - Given two locations, figure out the best route to drive to get from one to another
# - Recognize the emotional state of a person
# - Flexibly change strategies based on cues in the environment
# - Write and perform a winning rap battle 
# - Learn and be able to understand a human language
# - Learn and be able to understand a programming language
# - Play tic-tac-toe
# - Write a review of a movie
# - Play chess
# - Play PACMAN

# ### Instructions
# 
# For each task above, we want to try and decide whether it is a task that computers would be better at, that humans would be better at, or if it would be a tie.
# 
# In small groups (2 or 3 people, or on your own if groups are not possible/you're not doing this in coding lab directly), pick 3 or 4 examples from the list of tasks above, have a quick discussion about the task at hand and try to answer the question of who (computers and/or humans) this task would be easier for. 
# 
# For each task, try to imagine how you might try and do this in Python. You don't need to know how to write the actual code yet; you can use comments to describe the step.
# 
# Use pseudocode to sketch out an outline of the procedure for a 'computer better' task. 
# - If you think it is something computers can do well, your pseudocode should roughly cover the whole process.
# 
# Note: as a rule of thumb, computers can perform (and are good at) anything we can write down a specified list of steps (aka an algorithm). 
# 
# So one way to approach this section is to think through if and how you would write an algorithm to complete each task.
# 
# Below is an example, with an answer for the first listed task. You will be asked to sketch out your own example under that.

# #### Example: Given a list of 100K values, find the average and range of the list
# 
# This is a task that is easier for computers because we can write down a clear set of steps to complete this task (we can write an algorithm). 
# 
# Humans would not be good at completing this task, as there are a lot of steps to complete, and it would be slow, and we might not have the memory to do it.  

# In[2]:


# Pseudocode for list of value statistics
def list_statistics():
    
    # Find the mean of the list of values. 
    pass
    # To do so:
        # Find the total sum of the list
        # Find the number of elements in the list
        # Divide the sum by the number of elements
        
    # Find the range of the list of values. 
    pass
    # To do so:
        # Find the maximum value of the list
        # Find the minimum value of the list
        # Calculate range by subtracting the max from the min for the array
    
    # Return the mean and range of the array
    return None


# ### Include sketch of (at least) one task
# 
# After brainstorming, include a sketch of your pseudocode for at least one of the tasks you brainstormed about earlier:

# In[3]:


## Make some notes & write some pseudocode for you chosen task(s) here


# ## Part 2: Functions
# 
# Functions are a way to organize code into a procedure that we can repeat and use whenever we want. 

# ### Function Questions

# #### Write a function that takes one input, multiplies it by two and returns the result
# 
# This function has been started for you, with the name `mult_two`.
# 
# Add some more code to finish this function. 

# In[4]:


def mult_two(input_number):
    

### BEGIN SOLUTION
    answer = input_number * 2
    return answer
### END SOLUTION


# In[5]:


# Check that you can use the function
mult_two(2)


# In[6]:


# Check this function returns the correct outputs
assert mult_two(2) == 4
assert mult_two(3) == 6


# #### Write a function that takes two inputs, adds them together, and returns the result
# 
# Call this function `add_two`.

# In[10]:


def add_two(_FILL_IN_INPUTS_):
    
### BEGIN SOLUTION
def add_two(num1, num2):

    answer = num1 + num2
    return answer
### END SOLUTION


# In[11]:


# Check that you can use the function
add_two(2, 2)


# In[12]:


# Check this function returns the correct number
assert add_two(2, 2) == 4
assert add_two(3, 2) == 5


# #### Write a function with a conditional inside it
# 
# You can decide what this function does. 
# 
# It could, for example, take in a boolean and print out a status if the given boolean is True. 

# In[13]:


### BEGIN SOLUTION
def check_bool(input_bool):
    
    if input_bool == True:
        out = 'Status is True'
    else:
        out = 'Status is not True'
    
    return out
### END SOLUTION


# In[ ]:


# you can test out your function down here...


# ## Part 3: Conditionals
# 
# Conditionals a form of control flow for executing certain code if a specific condition is met. 

# ### Conditional Questions
# 
# In this part, we will re-visit some questions about conditionals, and start combining them together with collections. 
# 
# Make sure you can use if/elif/else statements to control which code blocks are run.

# #### Controlling Output With Conditionals I
# 
# Using the code below, keep updating the variable value to make sure you can make the conditional return each of the possibilities. 

# In[1]:


# ToDo: Update value to control what gets executed
value = 10

# This code provided
if type(value) == int:
    if value < 10:
        result = 'small value'
    if value >= 10:
        result = 'big value'
else:
    result = 'false value'


# In[2]:


print(result)


# #### Controlling Output With Conditionals II
# 
# In the cell below, first write something into each `result` assignment string below. For example, it could be something like: "B1 is False & B2 is True"). 
# 
# Then make sure you can change values of `b1` & `b2` to make the program execute each option. 

# In[3]:


# ToDo: Update b1 & b2 to control what gets executed
b1 = False
b2 = False

# Next, try this out
if b1 and not b2:
    result = ''
elif not b1 and b2:
    result = ''
elif b1 and b2:
    result = ''
else:
    result = ''
    
### BEGIN SOLUTION
# specific strings could vary
if b1 and not b2:
    result = 'b1 true; b2 false'
elif not b1 and b2:
    result = 'b1 false; b2 true'
elif b1 and b2:
    result = 'both true'
else:
    result = 'both false'

### END SOLUTION


# In[4]:


print(result)


# ### Conditional Challenges
# 
# The following are more challenging questions relating to conditional statements. If they seem too tricky for now, just skip ahead to the next section.

# #### Conditional Challenge #1
# 
# Write a conditional that prints "Found it" if a given `val_2` is a multiple of 10, otherwise prints "Nope."

# In[5]:


### BEGIN SOLUTION
# Set a test value for `val_2`
val_2 = 100

if val_2 % 10 == 0:
    print('Found it')
else:
    print('Nope')
### END SOLUTION


# #### Conditional Challenge #2
# 
# Input: assumes a variable `val_1`, that can be either a string or an integer
# 
# Output: based on the conditions, this code block will assign a variable called `output` to be a boolean
# 
# Use conditions to check whether `val_1` is a string or an integer object:
# - If it is a string, check whether it's length is greater then 8
#     - If so, set the value `output` to True
# - If it is an integer, compare whether it is less than 100
#     - If so, set the value `output` to True
# - Else, set `output` to False

# In[2]:


### BEGIN SOLUTION
# Set a test value for `val_1`
val_1 = 'string'

if type(val_1) == str and len(val_1) > 8:
    output = True
elif type(val_1) == int and val_1 < 100:
    output = True
else:
    output = False

# Check the output
print(output)
### END SOLUTION


# In[3]:


assert type(output) == bool


# ### Operator Explorations
# 
# For each of the following questions, start by writing out a guess of what you think it might do. 
# 
# Then, test out each one by writing out some code. 
# 
# Finally, once you have answered the question, using some code, add a comment in the markdown here with the answer. 
# 
# Questions:
# - Can you include multiple conditions in an if statement?
#     - If think so, write an if statement that tests multiple conditions.
# - What happens if you put an if statement inside an if statement? When would such a statement run?
#     - To explore this, write an if statement that has an embedded if statement in it. 
# 

# In[7]:


### BEGIN SOLUTION
v1 = True
v2 = False

# Option 1
# Yes, you can include multiple conditions in an if statement
if v1 == True and v2 == False:
    print('YES!')

# Option 2
# Yes, you can have an if statement within an if statement
#   The embedded if will end up running if both conditions of both if's are True   
if v1 == True:
    if v2 == False:
        print('Also YES!')
### END SOLUTION


# ## The End!
# 
# This is the end of this Coding Lab!
# 
# Be sure you've made a concerted effort to complete all the tasks specified in this lab. Then, go ahead and submit on datahub!
