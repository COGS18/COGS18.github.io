#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - **E1** due Monday at 11:59 PM
#     - released this afternoon (I'll message via Campuswire)
#     - complete individually
#     - submit on datahub
#     - No lecture or office hours Monday
# - **A2** due *next Friday* 10/22 (11:59 PM)
#     - Recommended to complete before exam: Q1-2, 4-12
# - **CL4** will be released this afternoon; due Wed
#     - Loops practice; can complete all of it

# **Prof Ellis' Office Hours**
# 
# ![courtyar](../img/courtyard.png)

# **Q&A** 
# 
# Q: For loops, do we ever move through loops backwards?  
# A: You could, but we won't.
# 
# Q: what is `isinstance`?  
# A: This returns True if the variable specified right after the parentheses is of the type specified after hte comma. For example `isinstance(6, int)` would return True b/c 6 is an integer. `isinstance(6, str)` would return False b/c 6 is not a string.
# 
# Q: How can you use for loops to add all the numbers in a range together?  
# A: See discussions on campuswire. 
# 
# Q: Will the lectures always give examples that will help with the assignments? I’m stuck on Q7 on A2 and can’t seem to find an example similar.  
# A: You'll always have seen the basic concepts in lectures and coding labs needed to figure out the assignments. But, you won't always have a "similar example." The idea is if you really understand the concept, you can figure out the question's answer. If you're just trying to copy+paste and "make it work," you'll struggle on a handful of questions.
# 
# Q: I am wondering why I got such a bad grade on A1, I need to re-evaluate and try to do my best. It's important I dont make the same mistakes twice.  
# A: Check your feedback on datahub, and come to office hours if still unsure. We definitely want to be sure you're clear and good to go for future assignments!
# 
# Q: I am kind of iffy on the difference between continue and break when writing the loop.  
# A: `continue` means "skip to the next iteration of the loop"; `break` means break out of the loop. Do not go on. Do not go to the next iteration. Just stop.
# 
# Q: To have access to my coding work in the future, I need something called Anaconda right? How do I set that up?  
# A: See part 3 of the first coding lab. You can download Anaconda to your computer.
# 
# Q: Is there a great place to find coding help for specific issues or questions? google is not the most reliable  
# A: For this class, campuswire is the best place. 
# 
# Q: Does the "continue" apply only for the "for" or can it be used for other purposes? Can I apply "continue" to other situations other than for "for" and does it run completely from the top of the cell?  
# A: `continue` can be used in any loop; it runs from the top of the loop, not necessarily the top of the cell.
# 
# Q: Can we have more than one "and" or "or" operator for a if condition?  
# A: Yup.
# 
# Q: How do you define odd and even numbers in a range, and them add them together?  
# A: Think about the logic about how you can use range's `start`, `stop`, and `step` for the first part. Then, consider the logic you would need in the loop to add the values together.
# 
# Q: For the break function, does it matter if you put break after the for statement or after the print statement?  
# A: Yes, if you put it before the `print()` statement, it will break before printing. If you put it after, it will `print` first.

# # Exam 1 Review
# 
# **Exam 1 Topics** (updated Friday 10/15)
# - Q0: Honor Code (0.15 points)
# - Variables & Operators (3.65 points)
#     - Q1: Variables
#     - Q2: Math Operators
#     - Q3: Comparison Operators
#     - Q4: Membership Operators
#     - Q5: String Concatenation
# - Collections & Indexing (2.5 points)
#     - Q6: Lists & Indexing
#     - Q7: Tuples
#     - Q8: Collections & Indexing
# - Control Flow - Conditionals & Loops (6.2 points)
#     - Q9: Conditionals
#     - Q10: `for` loop
#     - Q11: Accomplishing a task

# ## Midterm Notes
# 
# - I'm not trying to trick you:
#     - variable is `var_str`...it's going to be a string
#     - question is called "Membership Operators"...it's about membership operators
# - Do not hard code.
# - `assert`s will guide you less than on exams
# - `append` helpful on one exam question

# In[ ]:





# #### Clicker Question #1
# 
# Which topic would you like to review on the practice midterm?
# 
# - A) Variables & Operators
# - B) Collections & Indexing
# - C) Loops
# - D) Conditionals
# - E) Accomplishing a task

# #### Clicker Question #2
# 
# Click in when you...
# 
# - A) have finished
# - B) think you have finished but aren't totally sure
# - C) are stuck.

# ## Midterm Expectations
# 
# You will be expected to: 
# 
# 1. Recognize, understand and _respond_ to Python syntax:
#     - statements & comments, whitespace, code blocks & indentation levels
# 2. Recognize, understand and be able to _explain_ code constructions:
#     - variables, operators, data types, conditionals, loops
# 3. Know and be able to explain (roughly define) concepts we have talked about:
#     - encodings
# 4. Be able to apply what you've learned:
#     - Given a task:
#         - what kind of code constructions are needed to answer it?
#         - what kind of concepts does it relate to?
# 5. With respect to everything above, be able to read and respond to short code snippets and write out code.

# ### Reminder: 
# 
# There are two extra notebooks that you can use for review:
# 
# 1. [A1-Syntax](https://cogs18.github.io/materials/A1-Syntax.html)
# 2. [A2-Examples](https://cogs18.github.io/materials/A2-Examples.html)
# 
# There are also a few Exam #1 Practice Problems [here](https://cogs18.github.io/materials/Exam-Prep/E1-Practice.html).
# 
# And, there is a practice Exam on datahub.

# ## Topics & Example Questions
# 
# - Variables & Data Types
# - Operators
# - Conditionals
# - Loops
# 
# Note: The questions below are _less_ involved than the questions on your midterm. These are meant to help guide your studying. If you're stuck on one of these, you know where to focus your studying.

# ### Variables & DataTypes
# 
# Types:
# - strings, integers, floats, Booleans, None
# - Collections
#     - Lists
#     - Tuples
#     - Dictionaries
# 
# Concepts:
# - Mutable vs. Immutable
# - Indexing

# #### Data Types Question #1
# 
# What is the difference between a tuple and a list?

# #### Data Types Question #2
# 
# Given the following list: 
# 
# ```python
# ice_cream = ['vanilla', 'chocolate', 'strawberry', 'cherry', 'salted caramel']
# 
# ```
# 
# Edit the code at right with how would you return the specified values on left:
# 
# ```python
# ['vanilla', 'chocolate', 'strawberry'] : ice_cream[      ]
# ```

# #### Data Types Question #3
# 
# Write a line of code that would change the third element of a list `my_list` to store the value `12`.

# ### Operators
# 
# - assignment : `=`
# - math: `+`, `-`, `/`, `*`, `**`, `//`
# - comparison : `==`, `!=`, `<`, `>`, `<=`, `>=`
# - logic: `and`, `or`, `not`
# - identity: `is`, `is not`
# - membership : `in`, `not in`

# #### Operators Question #1
# 
# What is the difference between `=` and `==`?

# #### Operators Question #2
# 
# Create a variable `oper_var` that uses both the not and or operators (each at least once) such that `oper_var` stores (returns) the value `True`.

# #### Operators Question #3
# 
# Using at least 4 different math operators, create a variable `math_var` that stores (returns) the value '18' (or 18.0)

# #### Operators Question #4
# 
# Create a variable `string_concat` that demonstrates how you can concatenate two different strings together with a space between the two different strings. 

# ### Conditionals
# 
# - `if`, `elif`, & `else`

# #### Conditionals Question #1
# 
# Circle necessary or optional, as applicable: In Python, a conditional has a necessary / optional `if` statement, one or more necessary / optional `elif` statement(s) and a necessary / optional `else` statement. 

# #### Conditionals Question #2
# 
# Given the following outline of a conditional:
# 
# ```python
#     if COND_A:
#         # Code Block A
# 	elif COND_B:
# 		# Code Block B
# 	else:
# 		# Code Block C
# ```
# 
# 1. If `COND_A` and `COND_B` are both `True`, which code block(s) evaluate?
# 2. If `COND_A` is False and `COND_B` is `True`, which code block(s) evaluate?

# #### Conditionals Question #2
# 
# You use have a list that stores 20 different integers. You use a comparison operator to compare the relationship between two of the elements in the list and store that output in a variable. What would the type of that output variable be?

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
