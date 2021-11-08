#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - **E2** released ~5PM tonight; **due Mon at 8AM**
#     - Answer keys have been posted (website & Exam-Prep folder on datahub)
# - **A4** due next Fri 11/12
#     - Before the exam, I'd recommend completing Q1-Q4

# **Q&A**
# 
# Q: what does "self" exactly mean or do?  
# A: `self` allows you to explicitly refer to the current instance of the object type. Since each object an differ in the values stored in its attributes, any time you want to refer to a specifc instance of an object, we use `self`.
# 
# Q: Why was 'most' the default when using the compare method?  
# A: Becuase I decided that would be what people would want to use most often. We could have chosen a different value.
# 
# Q: What are examples of projects for the final- what can I NOT do?  
# A: We'll discuss details next Friday in class. Examples are [here](https://github.com/COGS18/Projects). You cannot do a project on topics for which there are tons of tutorials already online. This will be better defined next week.
# 
# Q: for the ProfCourses example, what could be an example of a class attribute for this class  
# A: If everyone using `ProfCourses` were a UCSD professor, a class attribute could be `university = 'UCSD'`...as that would be true for every `ProfCourses` object.
# 
# Q: A question that still remains is the difference between class attributes and instance attributes. I think that instance attributes are more specific, but I'm not sure about the difference in the purpose for them. I'm unsure when I would determine something as a class attribute or instance attribute.  
# A: First, a class attribute is something that would be true for ALL instances of that object type (think about the `Dog` example. All dogs say "Woof"...class attribute. An instance attribute is something you'd want to be able to change depending on the specific instance (for `Dog`, this was `name` and `breed`, as each dog does not have the same). On the exam, we'll specify whether something should be an instance or class attribute.
# 
# Q: When I do assignment I could achieve the goal following the step by step instruction, but I think I can't code to achieve some functions if I don't have those detailed instruction. Is this normal?   
# A: This is normal. However, you should always think through the code after you "get it right" to make sure you understand what the steps are doing. Also, this is why we have the project at the end. We've given you lots of guidance throughout the quarter. The project is the time for you to figure more out on your own!
# 
# Q: Would there ever be a reason for having multiple _init_ in a class? Would I only use _init_ within a class or are there other reasons that I would use _init_?  
# A: Only one `__init__` per class!
# 
# Q: At the beginning, you showed a link for additional practice problems for harder and more examples and I clicked on it. However, the page says This book is currently under development. Full home page coming soon."
# I was wondering when it would come?  
# A: While it's still under development, there's a lot there already. The table of contents at the left of the page will have more practice there for you.
# 
# Q: When to use self and when to not.  
# A: We always use self as the first parameter in instance attribute `__init__` and the first parameter for methods. Then, any time you want to refer back to an attribute for the object, you'll need `self` before it.
# 
# Q: how does python know what you meant by 'fewest' and 'most' when comparing courses in the ProfCourses example from class?   
# A: It was the value taken in as a parameter for the method.
# 
# Q: Can’t find the online office hours sign up sheet  
# A: It's on the main canvas home page for the course.

# # Exam 2 Review

# ## Exam II Plan (12.5 points)
# 
# Honor Code (0.1 points)
# 
# Part I: **Methods & Debugging** (3.5 points) 
# - Q1: Method I (0.75 points)*
# - Q2: Method II (1.25 point)*
# - Q3: Deubbing (1.5 points)*
# 
# Part II: **Functions** (4.4 points)  
# - Q4: Function Execution (1 point)
# - Q5: Function I (1.65 points)*
# - Q6: Function II (1.75 points)*
# 
# Part III: **Objects & Classes** (4.5 points)
# - Q7: Classes I (2.25 points)*
# - Q8: Classes II (2.25 points)*
# 
# \* : includes manual grading (partial credit)

# ### Questions?

# #### Clicker Question #1
# 
# Which topic would you like to review on the practice midterm?
# 
# - A) Methods
# - B) Debugging
# - C) Functions
# - D) Classes

# #### Clicker Question #2
# 
# Click in when you...
# 
# - A) have finished
# - B) think you have finished but aren't totally sure
# - C) are stuck.

# ### Reminder: 
# 
# There are two extra notebooks that you can use for review:
# 
# 1. [A1-Syntax](https://cogs18.github.io/materials/A1-Syntax.html)
# 2. [A2-Examples](https://cogs18.github.io/materials/A2-Examples.html)
# 
# There are also a few Exam #2 Practice Problems [here](https://cogs18.github.io/materials/Exam-Prep/E2-Practice.html) and a practice exam on datahub.

# ### Questions?

# ## Functions
# 
# - `def`
#     - `return`
# - executing a function
#     - parameters
#         - keyword vs. positional
#         - default values
#     - have a separate namespace
# - methods 
#     - in place vs. not in place

# #### Functions Question #1
# Write, in real code, a function called `remainder` that takes two inputs, divides the first input by the second and returns the remainder.

# In[ ]:


## YOUR CODE HERE


# #### Functions Question #2
# Using the function `remainder` you wrote above, write the python code you would use to return the remainder of 10 divided by 4. Store the output in the variable `my_remainder`.

# In[ ]:


## YOUR CODE HERE


# #### Functions Question #3
# Assuming the following function has been defined, what would `sum_list([1, 2, 3])` return?

# In[ ]:


def sum_list(my_list):
    total = 0
    
    for item in my_list:
        total += item
        
    return total


# In[ ]:


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

# In[ ]:


## YOUR CODE HERE


# The exam question will be more involved than this example. It's meant to combine all the pieces we've learned this quarter (classes w/ methods, conditionals, etc).

# **Part B**
# 
# Create an instance `my_rocket` of your Rocket object.

# In[ ]:


## YOUR CODE HERE


# **Part C**
# 
# Update `my_rocket` so that `my_rocket` has the `y` position 3.

# In[ ]:


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
# - True/False `ls` is a shell command that creates a new file 		
# - True/False `cd` returns your current working directory		
# - True/False `print_name()` folles best practices for function naming

# <h2><center>After the second exam:</center></h2>

# <h3><center> We will focus on the Python ecosystem, and applications of Python. </center></h3>

# <h3><center> We also become a project based course. </center></h3>
