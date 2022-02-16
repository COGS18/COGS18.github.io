#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# Due Dates:
# - **CL6** due (again) tonight (11:59 PM) - *NO* new CL this week
# - **E2** due Sunday (2/20; 11:59 PM); released Thursday 2/17 3PM
# - **A4** due Mon 2/28
# 
# Notes:
# - No lecture this Friday (exam) OR Monday (holiday)
# - **A3** scores posted
# - Exam Review answer keys have been posted

# **Q&A**
# 
# Q: Will functions and classes only use for loops if loops are included at all? While loops aren't used for these cases?  
# A: `while` loops can be used within functions, although we will use `for` loops more frequently.
# 
# Q: For the compare method examples why / how did it also return the number of courses printed? Like the first one I know is 5 and the second is 6 but how did it do it and do we need to have it?  
# A: This was because I had a line of code asking to print the `n_classes` *attribute* from the object. It was not from the method.
# 
# Q: I am also confused about the use of "self" and when to use "self".   
# A: `self` allows us to refer to the *current instance* of a given object. Tips for when to use self: 1) before the name of the attribute when defining instsance attributes; 2) as the first parameter to every method; 3) within methods anytime you want to reference an attribute (whether it's a class attribute OR an instance attribute, `self.` will be needed) 
# 
# Q: Will our lectures in the future keep building to produce even longer segments of code?   
# A: No. (I believe) Classes is the longest code we'll go through/build toward in this course.
# 
# Q: How much points does each participation survey worth?  
# A: Not totally sure, but if you complete every single one, it's 3.5% to your final project/final exam.
# 
# Q: I'm confused about the compare method example. Why do we specifically define the 0th index for the fewest and most variables, (fewest = self.course [0]) in the function?   
# A: This was to give us something to compare to the first time through the loop.
# 
# Q: The only part that I don't get is why can we set both most and fewest to the index [0]. Wouldn't it contradict each other?  
# A: Similar to the above question (read that first), we start with both being the same...but notice in the conditional, `most` and `fewest` change differently, depending upon the stated condition....so they won't end up the same.
# 
# Q: will we be using isinstance tool more in this class or not really?  
# A: Nope. Don't worry about it; just know that everything in python is an object/python is an object-oriented programming language.
# 
# Q: If python is an object program, what other program types are there and what would those do?   
# A: Lots explained [here](https://en.wikipedia.org/wiki/Programming_paradigm).
# 
# Q: for the instance in class, can you create a compare method that gives you both the most and fewest value?  
# A: Yup! I encourage you to edit the code provided to return both! Let's discuss in office hours or on campuswire if you struggle to determine how to do that.
# 
# Q: when we used the command dir(my_date) we get a list of methods and attributes, can we use this on any object, or how can we know what methods we can use in which objects. I got confused because professor said that we use append for lists but can we use for any other type of object?  
# A: For that example, those methods/attributes can *only* be used with *date* type objects. So, you must first know the type of the object and *then* can determine what methods are available.
# 
# Q: How do we extract an attribute if it's a string? I am getting a TypeError: string indices must be integers.
# A: I'd have to see your specific example, but remember if you're trying to index into a string, what goes between the brackets must be an integer (`i.e. my_string[0]`) So, this error suggests you're trying to index using something other than an integer. 
# 
# Q: In ProfCourses, Why does the last self.n_courses+1 in add_course add 1 every time a new course is added? I'm still a little confused about this because it doesn't look like a loop.  
# A: You're right that it's NOT a loop. Each time the method is called the previous value in `n_courses` is increased by 1...so it does NOT loop, but rather would increase by one each time the method is called/executed on an object.

# # Exam 2 Review

# ## Exam II Plan (12.5 points)
# 
# 
# Part I: **Methods, Debugging, & Code Style** (4.5 points) 
# - Q1: Method I (0.75 points)*
# - Q2: Method II (1.25 points)*
# - Q3: Debugging & Code Style (2.5 points)*
# 
# Part II: **Loops & Functions** (4 points)  
# - Q4: Function I (1.75 points)*
# - Q5: Function II (2.25 points)*
# 
# Part III: **Classes** (4 points)
# - Q6: Classes I (1.5 points)*
# - Q7: Classes II (2.5 points)*
# 
# \* : includes manual grading (partial credit)

# ### Reminder: 
# 
# There are three extra notebooks that you can use for review (in addition to your notes, labs, and assignments):
# 
# 1. [A1-CodeSytle](https://cogs18.github.io/materials/A1-CodeStyle.html)
# 1. [A2-Syntax](https://cogs18.github.io/materials/A2-Syntax.html)
# 2. [A3-Examples](https://cogs18.github.io/materials/A3-Examples.html)
# 
# There is also a practice exam on datahub and additional practice problems [here](https://shanellis.github.io/pythonbook/content/intro.html). Note that answers are included for all practice problems in the "Answers" chapter.

# ### Questions?

# ### Loops
# 
# - loops: `for` and `while`
#     - `continue`, `break`, `pass`

# #### Loops Question #1
# What are the two kinds of loops? ____________ and ____________

# #### Loops Question #2
# Use the following:
# `ind = 1` to write a loop (using real Python code) that would loop and print the value `ind` of ind each time through the loop _and_ update the value of ind by 1. Have this loop stop after 4 iterations. 

# #### Loops Question #3
# 
# Create a list that stores each letter of your favorite animal as a different element in a list. Store that in the variable `fav_pet`. 
# 
# Initialize an additional variable called `reverse_pet` that will store an empty string to start.
# 
# Then, using indexing, loop through each letter in that list such that `reverse_pet` stores a list with your favorite pet spelled backward.
# 
# For example, if your favorite pet were "cat", the output stored in `reverse_pet` should be: `['t', 'a', 'c']`
# 

# #### Loops Question #4
# Assuming the following function has been defined, what would `sum_list([1, 2, 3])` return?

# In[10]:


def sum_list(my_list):
    total = 0
    
    for item in my_list:
        total += item
        
    return total


# In[4]:


## CODE TO TEST HERE


# ## Objects & Classes
# 
# - objects & `class`
#     - attributes
#     - methods
#     - instances
# 

# #### Objects & Classes Question #1
# 
# **Part A**
# 
# We want to simulate a rocket ship for a game.
# 
# Write code that will create a class `Rocket`. 
# 
# This class should have two instance attributes: `x` and `y`. These will specify the x,y position of the rocket. Each attribute should be initialized with hte value 0. 
# 
# Your `Rocket` should also have the method `move_up()`. This method should increment the y-position of the rocket by 1. 

# In[8]:


## YOUR CODE HERE


# The exam question will be more involved than this example. It's meant to combine all the pieces we've learned this quarter (classes w/ methods, conditionals, etc).

# **Part B**
# 
# Create an instance `my_rocket` of your Rocket object.

# In[9]:


## YOUR CODE HERE


# **Part C**
# 
# Update `my_rocket` so that `my_rocket` has the `y` position 3.

# In[10]:


## YOUR CODE HERE


# #### Objects & Classes Question #2
# 
# Fill in the blanks:
# 
# 	What is the name of a function defined within a class: ______________
# 
# 	In Python, everything is a(n) ______________. 
# 

# ## Python & Jupyter Extras
# - encodings (`chr` & `ord`)
# - whitespace
# - namespace
# - kernel
# - code comments
# - magic functions

# #### Extras Question #1
# What will the following piece of code print out?
# 
# ```print(chr(ord('A')))``` 
#     
#      _____________

# #### Extras Question #2 
# 
# What is the magic function `%whos` used for?

# #### Extras Question #3
# 
# For each of the following, indicate if the statement is True or False about Python and programming:
# 
# - True/False Whitespace matters in Python
# - True/False Comments in Python start with '%' 					
# - True/False You have to specify a data type when you define a variable
# - True/False Every Python variable is available from every namespace				
# - True/False `print_name()` folles best practices for function naming

# <h2><center>After the second exam:</center></h2>

# <h3><center> We will focus on the Python ecosystem, and applications of Python. </center></h3>

# <h3><center> We also become a project based course. </center></h3>
