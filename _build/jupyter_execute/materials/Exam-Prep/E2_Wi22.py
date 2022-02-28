#!/usr/bin/env python
# coding: utf-8

# # COGS 18 - Exam 2
# 
# This is the second exam for Winter 2022. It covers topics through the Classes Lecture.
# 
# This total exam is out of 12.5 points, worth 12.5% of your grade. 
# 
# **PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**
# 
# **PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE EXAM.** (Note that you can add additional cells, if you want to test things out.

# ## Instructions
# 
# #### Timing
# - The exam is designed to take you ~1-2h.
# - If it takes you longer than 1-2h, you're free to use that time, so long as you submit the exam before the deadline (Sunday 11:59 PM)
# 
# #### The Rules
# - You are to complete this exam on your own.
# - This is open-notes & open-Google
# - You may not talk to any humans about this exam. 
# - The following are all *prohibited*:
#     - text/phone/online chat communication
#     - posting questions to a message board where a human could respond (Campuswire, Discord, Chegg, any similar site)
#     - viewing exam questions from a message board (as described above)
#     - asking anyone via any form about a question on this test directly
# - Clarification questions will ***not*** be allowed and there will be no posting on Campuswire about the exam at all. 
#     - Campuswire posts about the exam will not be answered and will be deleted. 
#     - Students who post questions about the exam to Campuswire are at risk of losing points on the exam.
#     - If you are confused about wording, add a note to your exam explaining your confusion and how you interpreted the question. 
#     - Note: This policy is b/c we are incapable of responding for the entirety of hte exam. This is the only way to make it fair across the board for students.

#  <span style="color: red;">Note: </span> There _is_ a chance for partial credit on some questions, so _some_ code is better than _no_ code. Even if it throws an error, having some code that partially answers the question will benefit you/your grade.

# ### Q0 - Honor Code
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


# ## Part 1: Methods, Debugging, & Code Style (4.5 points)

# ### Q1 - Method I (0.75 points)
# 
# `title()` is a built-in string method that "converts the first character of each word to upper case". 
# 
# Store your favorite book's title using all lowercase characters in the variable `fav_book`.
# 
# Then, use the `.title()` string method to convert the string in `fav_book` to title case (meaning the first letter of each word is upper case), and storing this result in the variable `book_title`.

# In[3]:


### BEGIN SOLUTION
# specific strings will differ
fav_book = 'evicted'
book_title = fav_book.title()

print(fav_book, book_title)
### END SOLUTION


# In[4]:


assert fav_book is not None
### BEGIN HIDDEN TESTS
assert fav_book.islower()
### END HIDDEN TESTS


# In[5]:


assert book_title is not None
### BEGIN HIDDEN TESTS
assert book_title.istitle()
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# - uses `title()` syntax correctly (**0.35 pts**)
# - uses `fav_book` when calling `.title()` (**0.2 pts**) 
# 
# === END MARK SCHEME ===

# ### Q2 - Method II (1.25 points)
# 
# `.count()` is a built-in tuple method that "returns the number of times a specified value occurs in a tuple."
# 
# In the cell below, the variable `students_fruits` has been provided for you. Using *only* `students_fruits` and the `count()` method, generate the three variables specified at left in the bulleted list below, satisfying the following criteria:
# 
# - `apple_count` | the number of times `'apple'` shows up in `students_fruits`
# - `lychee_count` | the number of times `'lychee'` shows up in `students_fruits`
# - `pineapple_count` | the number of times `'pineapple'` shows up in `students_fruits`
# 
# Note you will have to execute the cell with the variable provided below before being able to reference it in your answer.

# In[29]:


# these variables provided for you
# you will not be able to edit this cell
students_fruits = ('apple', 'apple', 'apple', 'banana', 'pear', 'dragonfruit', 'starfruit', 'apple', 
                   'pear', 'pineapple', 'apple', 'grapefruit', 'lime', 'lychee', 'plum', 'plum', 'pineapple')


# In[53]:


# ignore this cell; it's being used in grading
# be sure to put your answer in the cell below this cell
### BEGIN HIDDEN TESTS
# editing tuple to avoid hard-coding issues 
students_fruits = ('apple', 'apple', 'banana', 'pear', 'dragonfruit', 'starfruit', 'lychee', 'apple', 
                   'pear', 'pineapple', 'apple', 'grapefruit', 'lime', 'lychee', 'plum', 'plum')
### END HIDDEN TESTS


# In[31]:


### BEGIN SOLUTION
apple_count = students_fruits.count('apple')
lychee_count = students_fruits.count('lychee')
pineapple_count = students_fruits.count('pineapple')

print(apple_count, lychee_count, pineapple_count)
### END SOLUTION


# In[32]:


assert apple_count is not None
### BEGIN HIDDEN TESTS
assert apple_count == 4
### END HIDDEN TESTS


# In[33]:


assert lychee_count is not None
### BEGIN HIDDEN TESTS
assert lychee_count == 2
### END HIDDEN TESTS


# In[34]:


assert pineapple_count is not None
### BEGIN HIDDEN TESTS
assert pineapple_count == 1
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# - `count()` syntax correct (called directly on object) (**0.5 pts**)
# 
# === END MARK SCHEME ===

# ### Q3 - Debugging & Code Style (2.5 points)
# 
# In the cell below, there is a function that is not operating as anticipated *and* that has poor code style.
# 
# `determine_letter_grade()` is *supposed* to take a student's points received (`student_points`) on an assignment as well as the possible points the student *could* have earned (`possible_points`) and `return` the letter grade the student earned...but it's not quite functioning as anticipated. 
# 
# More specifically, this function should:
# - calculate the *percentage* of the possible points the student earned on the assignment (Note: you're only expected to account for percentages between 0 and 100 inclusive...so you don't have to consider 101%, for example.)
# - use the dictionary (`letter_grades`) provided in the function below to determine what letter grade (the key in the dictionary) the student has earned. Note that the values in the dictionary are the range of possible percentages corresponding to the letter grade. The lower bound should be included in the range while the upper value for each element in the dictionary should *not* be included in the range for that letter value (i.e. 90% would be an 'A'; 80% would be a 'B', etc.)
# - `return` the letter grade earned from the function
# 
# For example:
# - `determine_letter_grade(student_points = 10, possible_points = 10)` would `return` `'A'`
# - `determine_letter_grade(student_points = 89, possible_points = 100)` would `return` `'B'`
# - `determine_letter_grade(student_points = 5, possible_points = 10)` would `return` `'F'`
# 
# **Debug, edit, and test the function provided below so that it accomplishes the intended goal.** 
# 
# ```python
# def determine_letter_grade(student_points,possible_points):
#     letter_grades={'A':(90,101),'B':(80,90),'C':(70,80),'D':(60,70),'F':(0,60)}
#     percentage=(student_points/possible_points)
#     for letter in letter_grades:
#         if percentage<=letter_grades[letter][0] and percentage>=letter_grades[letter][1]:
#             print(letter_grades[letter])
#         break
# ```
# 
# *Then*, be sure to **edit the function you generate so that it follows the code style guidelines** discussed in class.

# In[10]:


### BEGIN SOLUTION
def determine_letter_grade(student_points, possible_points):

    letter_grades = {'A' : (90, 101),
                     'B' : (80, 90), 
                     'C' : (70, 80), 
                     'D' : (60, 70), 
                     'F' : (0, 60)}

    percentage = (student_points/possible_points) * 100

    for letter in letter_grades:
        if percentage >= letter_grades[letter][0] and percentage < letter_grades[letter][1]:
            return letter
            break
### END SOLUTION


# In[11]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)


# In[12]:


assert determine_letter_grade
# hidden tests to check the specific cases given in the instructions
### BEGIN HIDDEN TESTS
assert determine_letter_grade(student_points = 10, possible_points = 10) == 'A' 
assert determine_letter_grade(student_points = 89, possible_points = 100) == 'B'
assert determine_letter_grade(student_points = 5, possible_points = 10) == 'F' 
### END HIDDEN TESTS


# In[13]:


assert callable(determine_letter_grade)
# hidden tests to check additional cases beyond what was specified in the instructions
### BEGIN HIDDEN TESTS
assert determine_letter_grade(student_points = 0, possible_points = 10) == 'F'
assert determine_letter_grade(student_points = 18, possible_points = 20) == 'A'
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading for debugging.)
# 
# === BEGIN MARK SCHEME ===
# 
# Check if points lost on autograder above: 
# - `percentage` calculates percentage (`*100` added) (**0.25 pts**)
# - conditional operator logic fixed `>=` and `<` (**0.25 pts**)
# - `break` moved inside the conditional (or removed/handled some other way) (**0.25 pts**)
# - `print` statement -> `return` statement (**0.25 pts**)
# - `return`s `letter` (key) not the value (**0.25 pts**)
# 
#                                                               
# === END MARK SCHEME ===

# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading for code style.)
# 
# === BEGIN MARK SCHEME ===
# 
# Code Style: 
# - Improved spacing in dictionary for readability (**0.25 pts**)
# - some logical line spacing included (**0.25 pts**)
# - reasonable spacing around operators (**0.25 pts**)
#                                                               
# === END MARK SCHEME ===

# ## Part 2: Loops & Functions (4 points)

# ### Q4 - Function I: `purchase_items()` (1.75 points)
# 
# In this question, you're going to define a function called `purchase_items()` that will take two parameters as input:
# 
# - `cost` | a dictionary of the items (the keys; strings) and how much each item costs (the values; ints or floats)
# - `cash` | how much cash the buyer gave the cashier (int or float)
# 
# Within the function, your code should:
# 
# - Determine if the `cash` provided is enough to pay for all the items in `items`.
# - If there is enough `cash`, the function should determine (and `return`) how much change the buyer should receive, given how much they paid `cash` and how much the items in `cost` cost in total.
# - If there is not enough `cash` to cover *all* the items in `items`, the function should `return` the string 'More cash needed'
# 
# For example:
# - `purchase_items(cost={'tool': 10, 'food': 5.5}, cash=16)` should `return` `0.5`
# - `purchase_items(cost={'tool': 10, 'food': 5}, cash=15)` should `return` `0`
# - `purchase_items(cost={'tool': 10, 'food': 5}, cash=14)` should `return` `'More cash needed'`

# In[35]:


### BEGIN SOLUTION
def purchase_items(cost, cash):

    sum_values = sum(cost.values())
    
    for item in cost:
        if cash >= 0:
            cash = cash - cost[item]
        
    if cash < 0: 
        cash = 'More cash needed'
    
    return cash
### END SOLUTION


# In[36]:


# BE SURE YOUR ANSWER IS IN THE CELL BELOW
# but you can use this cell to test/execute/check your thinking (optional)


# In[37]:


assert purchase_items
# hidden tests to check the specific cases given in the instructions
### BEGIN HIDDEN TESTS
assert purchase_items(cost={'tool': 10, 'food': 5.5}, cash=16) == 0.5
assert purchase_items(cost={'tool': 10, 'food': 5}, cash=15) == 0
assert purchase_items(cost={'tool': 10, 'food': 5}, cash=14) == 'More cash needed'
### END HIDDEN TESTS


# In[38]:


assert callable(purchase_items)
# hidden tests to check additional cases beyond what was specified in the instructions
### BEGIN HIDDEN TESTS
# ensuring works with different length dictionaries/other keys
assert purchase_items(cost={'tool': 2, 'food': 4, 'gas': 40}, cash=106) == 60
assert purchase_items(cost={'A': 2, 'B': 4, 'C': 40, 'D': 30}, cash=40) == 'More cash needed'
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# Only check if autograder credit lost above:
# - function defined correctly with two input parameters `cost` and `cash` (**0.15 pts**)
# - loops through `cost` dictionary (**0.25 pts**)
# - has conditionals to determine:
#     - when out of cash (**0.35 pts**)
#     - when string should be returned (**0.3 pts**)
# - has `return` statement (**0.1 pts**)
# 
# === END MARK SCHEME ===

# ### Q5 - Function II: `string_shortener()`  (2.25 points)
# 
# Define a function `string_shortener()` that takes two parameters as inputs `str_list` (a list of strings) and `int_list` (a list of integers).
# 
# Within the function, your code should extract the number of characters in each element of `str_list` as specified by the integer in the corresponding element in `int_list`, adding each shortened string to `output_list` (which should be `return`ed from the function.) For example, if the first element in `str_list` were `'hello'`, and the first element in `int_list` were `3`, the string `'hel'` (the first three letters of `'hello'`) should be added to `output_list`. 
# 
# One caveat, is that *if* the integer specified in `int_list` is *greater* than the number of characters in the corresponding element in `str_list`, then `None` should be added to `output_list` (instead of a shortened string).
# 
# For example:
# - `string_shortener(str_list=['hello', 'hey', 'everything'], int_list=[3, 2, 5])` should `return` `['hel', 'he', 'every']`
# - `string_shortener(str_list=['somanyletters', 'everything'], int_list=[40, 17])` should `return` `[None, None]`
# 
# Notes: 
# - you can assume that the length of both inputs is the same (your code does NOT have to check for/account for this)
# - you can assume that `str_list` contains a list of strings and `int_list` contains a list of integers (your code does NOT have to check for/account for this)
# - the `output_list` should always have the same number of elements as the input parameter lists
# - remember that `zip()`, introduced on A4, is available for use. This question *can* be completed without `zip()`...but it may be simpler if you use `zip()`

# In[39]:


### BEGIN SOLUTION
def string_shortener(str_list, int_list):
    
    output_list = []
    
    # can be accomplished without zip by specifying/using index
    for my_int, my_str in zip(int_list, str_list):
        if my_int <= len(my_str):
            output_list.append(my_str[0:my_int])
        else:
            output_list.append(None)
    
    return output_list
        
### END SOLUTION


# In[40]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)


# In[41]:


assert string_shortener
# hidden test to check that the output is of the expected type (a list)
### BEGIN HIDDEN TESTS
assert callable(string_shortener)
assert type(string_shortener(str_list=['hi', 'hello'], int_list=[5,6])) == list
### END HIDDEN TESTS


# In[42]:


# hidden test to check the first example provided in the instructions
### BEGIN HIDDEN TESTS
assert string_shortener(str_list = ['hello', 'hey', 'everything'], int_list=[3, 2, 5]) == ['hel', 'he', 'every']
### END HIDDEN TESTS


# In[43]:


# hidden test to check the second example provided in the instructions
### BEGIN HIDDEN TESTS
assert string_shortener(str_list = ['somanyletters', 'everything'], int_list=[40, 17]) == [None, None]
### END HIDDEN TESTS


# In[44]:


# hidden test to check example not provided in the instructions
### BEGIN HIDDEN TESTS
# checks that code works with combination of strings and None
assert string_shortener(str_list = ['hello', 'everything'], int_list=[5, 17]) == ['hello', None]
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# Check if points lost on autograder above: 
# 
# - `def` correct with 2 parameters `str_list` and `int_list` (**0.15 pts**)
# - `output_list` initialized as an empty list (**0.25 pts**)
# - code loops through `str_list` and `int_list` (does NOT have to be at the same time) (**0.25 pts**)
# - `.append()` used to add element to `output_list` (or equivalent) (**0.25 pts**)
# - has conditional to account for length of string (**0.25 pts**)
# - includes `return` statement (**0.1 pts**)
# 
# Notes:
# - if only issue is `return` statement is missing, return autograder credit lost and only deduct for `return` statement missing
# 
# === END MARK SCHEME ===

# ## Part 3: Classes (4 points)

# ### Q6 - Classes I: `ClassRoster()` (1.5 points)
# 
# 
# The following class has been provided for you:
# 
# ```python
# class ClassRoster():
#         
#     def __init__(self, course):
#         self.students = []
#         self.course = course
#         
#     def add_student(self, pid, name):
#         self.students.append({pid: name})
# ```
# 
# In the cell below, describe what a class is in general and what the `ClassRoster` class does. Be sure to be specific in your answer, and make sure to discuss each of its components (This will likely require you to talk about specific lines of code).
# 
# 
# Note: you do not need to write any python code for this question; we're looking for a written explanation in the cell provided below.
# 
# <span style="color:red">Be sure to include your text response in the cell below!</span>
# 

# Possible answer: 
# 
# In general, a class defines a a blueprint for creating a new object, allowing for attributes (variables/data) and functions (methods) to be organized and operate together. 
# 
# The `ClassRoster` class has two instance-specifc attributes: `course` (initialized with the value specified by the user for the `course` parameter on instantiation) and `students` (initialized as an empty list). The use of `self` here indicates that these values can/will differ between different instantiations of the class (i.e. for different courses).
# 
# The class also has a method, `add_student`, that takes two parameters (`pid` and a student's `name`). This method appends a key (`pid`) - value (`name`) pair to the instance attribute `students` list. Together, this allows an instructor to add all of their studentes to their `students` list.

# In[45]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# - describes what a class is; generally describes that a ClassRoster object would allow you to keep track of a list of students PIDs and names as a dictionary in the `students` list (**0.25 pts**)
# - has *some* reasonable explanation of what `self` is in explanation (**0.25 pts**)
# - describes the instance attributes:
#     - `students` is initialized as an empty list (**0.25 pts**)
#     - `course` takes input from the user (**0.25 pts**)
# - describes the `add_student` method:
#     - takes two parameters from the user (**0.1 pts**)
#     - correctly desctibes that the parameters are stored in a dictionary AND that that dictionary is appended to the `students` attribute (**0.4 pts**)
#     
# === END MARK SCHEME ===

# ### Q7 - Classes II: `Warehouse()` (2.5 points)
# 
# Define a class `Warehouse()` that meets the following specifications:
# 
# - has a class attribute: `purpose` which always has the value 'storing goods' (a string)
# 
# - has one instance attribute
#     - `department` | a string corresponding to the department; this is specified by the user on creation of a `Warehouse()` type object using the `department` parameter
# 
# - has two methods:
#     - `calculate_imports()` 
#         - calculates the sum of all the values in `imports` (the function's parameter; a *list* of all the imports for the department)
#         - This function should `return` the string `'Total imports for [department]: [sum of imports]'`, where `[department]` and `[sum of imports]` are replaced with the `department` attribute and sum total calculated within the function, respectively
#     - `calculate_exports()`
#         - calculates the sum of all the values in `exports` (the function's parameter; a *list* of all the exports for the department)
#         - This function should `return` the string `'Total exports for [department]: [sum of exports]'`, where `[department]` and `[sum of sum of exports]` are replaced with the `department` attribute and sum total calculated within the function, respectively
#         
# For example, if you were to create an instance of this object with the `'crafts'` and then called the `calculate_imports()` method on that object with the input `[4,5,6]`, you would expect this to `return` the string `'Total imports for crafts: 15'`

# In[46]:


### BEGIN SOLUTION
class Warehouse():
        
    purpose = 'storing goods'
    
    def __init__(self, department):
        self.department = department
        
    def calculate_imports(self, imports):
        sum_imports = sum(imports)     
        return "Total imports for " + self.department + ": " + str(sum_imports)
    
    def calculate_exports(self, exports):
        sum_exports = sum(exports)     
        return "Total exports for " + self.department + ": " + str(sum_exports)
    
    ### END SOLUTION


# In[47]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)


# In[48]:


assert callable(Warehouse)
my_warehouse = Warehouse(department='Clothing')


# In[49]:


# tests for class attribute
assert my_warehouse.purpose == 'storing goods'


# In[50]:


# tests for instance attribute
assert my_warehouse.department == 'Clothing'


# In[51]:


# tests for method calculate_imports
assert callable(Warehouse.calculate_imports)
assert my_warehouse.calculate_imports([4, 5, 6]) == 'Total imports for Clothing: 15'
# ensure executes with correct parameter name
assert my_warehouse.calculate_imports(imports=[4, 5, 6]) == 'Total imports for Clothing: 15'


# In[52]:


# tests for method calculate_exports
assert callable(Warehouse.calculate_exports)
assert my_warehouse.calculate_exports([1, 2, 3]) == 'Total exports for Clothing: 6'
# ensure executes with correct parameter name
assert my_warehouse.calculate_exports(exports=[1, 2, 3]) == 'Total exports for Clothing: 6'


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# Check if points lost on autograder above (Note none of the tests were hidden...so we should avoid many string errors): 
# - `class` defined correctly (**0.1 pts**)
# - class attribute correct (**0.2 pts**)
# - instance attribute
#     - `def __init__(self, department)` correct (**0.2 pts**)
#     - `self` used within definition (**0.2 pts**)
#     - `department` attribute initialized correctly (**0.2 pts**)
# - `calculate_import` and/or `calculate_export` methods (grade the one that's more corrrect):
#     - method definition correct with `self` and additional parameter (**0.2 pts**)
#     - calculates sum correctly (**0.1 pts**)
#     - uses self. to refer to attribute in string  (**0.2 pts**)
#     - `return`s a concatenated string (even if string incorrect) (**0.1 pts**)
# 
# Note: autograder credit can be returned for portions above if particular aspect (class attribute, instance attribute, or method) were correct, but test failed because overall `class` was defined incorrectly
# 
# === END MARK SCHEME ===

# ### Exam II complete!
# 
# Good work - you're done with the second exam!
# 
# Check your work, and then when you're ready, **submit on datahub**.
# 
# We will not have your exam until you click submit and see this show up under 'submitted assignments'.
