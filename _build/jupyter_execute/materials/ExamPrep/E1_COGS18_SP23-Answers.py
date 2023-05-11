#!/usr/bin/env python
# coding: utf-8

# Answers/points to **in-class** exam: https://cogs18.github.io/assets/intro/exams/E1_Sp23_Answers.pdf

# # COGS 18 - Exam 1 (Take-Home)
# 
# This is the take-home portion of the first exam for Spring 2023. It covers the technical implementation of topics through the Debugging Lecture.
# 
# This take-home portion of the exam is out of 2.5 points, worth 2.5% of your grade.
# 
# **PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**
# 
# **PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE ASSIGNMENT.** (Note that you can add additional cells, if you want to test things out.

# #### Instructions
# 
# #### Timing
# - There will be a multi-day window during which you can complete this exam.
# - Exam deadline (submit button on Datahub) is 11:59pm Friday May 5th.
# 
# #### The Rules
# - You are to complete this exam on your own.
# - This is open-notes & open-Internet.
# - You may not talk to any humans about this exam. 
# - The following are all *prohibited*:
#     - text/phone/online chat communication
#     - posting questions to a message board where a human could respond (Discord, Chegg, any similar site)
#     - viewing exam questions from a message board (as described above)
#     - asking anyone via any form about a question on this test directly
# - Clarification questions will ***not*** be allowed and there will be no posting on Piazza about the exam at all. 
#     - Piazza posts about the exam will not be answered and will be deleted. 
#     - Students who post questions about the exam to Piazza are at risk of losing points on the exam.
#     - If you are confused about wording, add a note to your exam explaining your confusion and how you interpreted the question. 
#     - Note: This policy is b/c we are incapable of responding for the entirety of the exam. This is the only way to make it fair across the board for students.
#     - If you have a technical issue completing the exam, message (Piazza or email) Prof Ellis ASAP.
# 

#  <span style="color: red;">Note: </span> This portion of the midterm will be autograded, similar to an assingment. `assert` statements are there to guide your thinking but do not guarantee you've gotten the answer correct.

# ### Q0 - Honor Code (0.05 points)
# 
# In the cell below, include a variable `honor_code` that stores the boolean `True` if you agree to the following statement:
# 
# >I agree that this exam was completed individually with the knowlege in my brain, information the notes from this course, and/or with searching for help on the Internet *without searching for answers to the text from these questions directly*. I did not ask anyone about specific questions on this exam. I did not post these questions (in part or in whole) on the Internet. I did not copy answers to these questions from anywhere or anyone else. I understand all code I've written on this exam and could explain my answers to someone else if asked.
# 

# In[1]:


### BEGIN SOLUTION
honor_code = True
### END SOLUTION


# In[2]:


assert honor_code


# ### Background
# 
# On the in-person portion of the midterm you were told the following: You sat down to write code to make a very basic memory game. The idea here is that there will be three functions: 1) a function that displays a single character; 2) a function that displays a set of characters;  3) a function that determines if the single character is in the set of characters. Now, let's write the code for those functions!

# ### Q1 - Function execution (0.6 pts)
# 
# On the midterm you were provided the function provided beow and had the opportunity to describe how the function worked. 
# 
# Here, now that you have understanding, **execute the function** such that the provided `assert` statements for this question pass silently.

# In[3]:


def display_char(index):
    
    objects = ['x', 'ã', 'ƫ', '%', '§', '¶',
              'Ł', 'Œ', 'Ɓ', 'Ɍ', 'Ɏ', 'ḉ']
    
    char = objects[index]
    
    return char


# In[4]:


### BEGIN SOLUTION
out1 = display_char(5)
out2 = display_char(2)
out3 = display_char(-1)

print(out1, out2, out3)
### END SOLUTION


# In[5]:


# you can use this cell to test/execute/check your thinking (optional)


# In[6]:


assert out1 == '¶'


# In[7]:


assert out2 == 'ƫ'


# In[8]:


assert out3 == 'ḉ'


# ### Q2 - Debugging a function (0.4 pts)
# 
# The following function was provided on the midterm: 
# 
# ```python
# def display_objects(start, stop, skip):
#     
#     objects = ['x', 'ã', 'ƫ', '%', '§', '¶',
#               'Ł', 'Œ', 'Ɓ', 'Ɍ', 'Ɏ', 'ḉ']
#     
#     objects[start:stop:skip]
#     
#     return objects
# ```
# 
# ...with the following additional information: 
# 
# > You sit down to write a function (`display_objects`) that will return a slice of a specified list (`objects`). The idea is that, when executed, the function would use the values specified for the three parameters (`start`, `stop`, and `skip`)
# 
# **Debug this function so that it accomplishes what you had intended.**

# In[9]:


### BEGIN SOLUTION
def display_objects(start, stop, skip):
    
    objects = ['x', 'ã', 'ƫ', '%', '§', '¶',
              'Ł', 'Œ', 'Ɓ', 'Ɍ', 'Ɏ', 'ḉ']
    
    output = objects[start:stop:skip]
    
    return output # could also return the output directly
### END SOLUTION


# In[10]:


# you can use this cell to test/execute/check your thinking (optional)


# In[11]:


assert callable(display_objects)

# hidden tests that check the function works as specified
### BEGIN HIDDEN TESTS
assert display_objects(0,1,1) == ['x']
assert display_objects(1,6,2) == ['ã', '%', '¶']
### END HIDDEN TESTS


# ### Q3 - Defining a function (1.45 pts)
# 
# Define a function `determine_match`. 
# 
# This function should take in two parameters, `char` (the output from `display_char`) and `list_of_objects` (the output from `display_objects`).
# 
# If the output from `display_char` is in an element in the output from `display_objects`, this function should `return` `True`; otherwise, it should `return` `False`. 
# 
# For example:
# - `determine_match(display_char(5), display_objects(1,6,2))` should `return` `True`
# - `determine_match(display_char(0), display_objects(1,6,2))` should `return` `False`

# In[15]:


### BEGIN SOLUTION
def determine_match(char, list_of_objects):

    if char in list_of_objects:
        output = True
    else:
        output = False
    
    return output
### END SOLUTION


# In[13]:


# you can use this cell to test/execute/check your thinking (optional)


# In[13]:


assert callable(determine_match)

# hidden test that checks the output is of the expected type
### BEGIN HIDDEN TESTS
# note: this would still give credit, even if you had an error earlier
assert type(determine_match('a', ['a','b']))
### END HIDDEN TESTS


# In[14]:


# hidden tests that check the parameter names
### BEGIN HIDDEN TESTS
# note: this would still give credit, even if you had an error earlier
assert determine_match(char='a', list_of_objects=['a','b'])
assert not determine_match(char='c', list_of_objects=['a','b'])
### END HIDDEN TESTS


# In[15]:


# hidden tests that check the provided examples
### BEGIN HIDDEN TESTS
# note: this requires all three functions to work  to get credit
assert determine_match(display_char(5), display_objects(1,6,2))
assert not determine_match(display_char(0), display_objects(1,6,2))
### END HIDDEN TESTS


# In[16]:


# hidden tests that check overall functionality
### BEGIN HIDDEN TESTS
# note: this requires all three functions to work  to get credit
assert not determine_match(char=display_char(5), list_of_objects=display_objects(1,6,3))
assert determine_match(display_char(0), display_objects(0, 12, 4))
### END HIDDEN TESTS

