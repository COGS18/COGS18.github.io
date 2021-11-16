#!/usr/bin/env python
# coding: utf-8

# # COGS 18 - Exam 2
# 
# This is the second exam for Fall 2021. It covers topics through the Classes Lecture.
# 
# This total exam is out of 12.5 points, worth 12.5% of your grade. 
# 
# **PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**
# 
# **PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE EXAM.** (Note that you can add additional cells, if you want to test things out.

# ## Instructions
# 
# #### Timing
# - The exam is designed to take you ~1h.
# - There will be a >24 hour window during which you can complete this exam (due **Mon 8AM**).
# - If it takes you longer than 1h, you're free to use that time.
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
#     - Note: This policy is b/c we are incapable of responding for 24h straight. This is the only way to make it fair across the board for students.

#  <span style="color: red;">Note: </span> There _is_ a chance for partial credit on some questions, so _some_ code is better than _no_ code. Even if it throws an error, having some code that partially answers the question will benefit you/your grade.

# ### Q0 - Honor Code (0.1 points)
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


# ## Part 1: Methods & Debugging (3.5 points)

# ### Q1 - Method I (0.75 points)
# 
# `istitle()` is a string method that determines if the string follows the rules of a title (meaning the first letter of each distinct word is upper case while all other letters are lower case).
# 
# Use the `istitle()` method on two strings (of your choosing) below to create two variables:
# - `true_var` | should store the value `True`
# - `false_var` | should store the value `False`

# In[3]:


### BEGIN SOLUTION
true_var = 'My Title'.istitle()
false_var = 'MY TITLE'.istitle()
### END SOLUTION


# In[4]:


assert true_var is not None
### BEGIN HIDDEN TESTS
assert true_var
### END HIDDEN TESTS


# In[5]:


assert false_var is not None
### BEGIN HIDDEN TESTS
assert not false_var
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# - uses `istitle()` syntax correctly (**0.35 pts**)
# 
# === END MARK SCHEME ===

# ### Q2 - Method II (1.25 points)
# 
# 
# Using the `count()` method, code constructs discussed in class, and referencing the `prof_day` variable provided below, generate a dictionary `prof_events`, whose keys are each of the unique elements in `prof_day` and whose corresponding values are the number of times each value shows up in `prof_day`.
# 
# 
# Notes:
# - `prof_day` has been defined for you below
# - `count()` is a list method that counts the number of appearances of a specified element in a list.
# - Do not hard-code. You should use code contructs to determine `prof_events`.

# In[6]:


# this variable provided for you
# you will not be able to edit this cell
prof_day = ['write one exam', 'write one exam', 'grade exam', 'answer email', 'office hours', 'staff meeting']


# In[7]:


# hidden code being used in grading
### BEGIN HIDDEN TESTS
# change one value in list to ensure code still executes (aka is not hard-coded)
prof_day = ['write one exam', 'write one exam', 'answer email', 'answer email', 'office hours', 'staff meeting']
### END HIDDEN TESTS


# In[8]:


### BEGIN SOLUTION
prof_events = {}

for ele in prof_day:
    prof_events[ele] = prof_day.count(ele)

prof_events
### END SOLUTION


# In[9]:


assert prof_events is not None
### BEGIN HIDDEN TESTS
# check that keys are all what they should be
assert all(elem in list(prof_events.keys())  for elem in ['write one exam', 'answer email', 'office hours', 'staff meeting'])
### END HIDDEN TESTS


# In[10]:


# hidden tests for task above
### BEGIN HIDDEN TESTS
# check that values are what they should be
assert sum(prof_events.values()) == 6
assert all(elem in list(prof_events.values()) for elem in [2,1])
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# Check if points lost on autograder above: 
# - initialized or created `prof_events` as a dictionary (**0.25 pts**)
# - Used count() method correctly (**0.25 pts**)
# - updated `prof_events` dictionary correctly (**0.25 pts**)
# 
# === END MARK SCHEME ===

# ### Q3 - Debugging (1.5 points)
# 
# The following not-totally-functioning `give_ticket()` function has been provided for you. The *goal* of this function, is given two population inputs (`speed` and `zone`), the function should `return` the boolean True if the person should receive a ticket and the boolean False otherwise.
# 
# The rules for giving a ticket depend upon the driver's speed and the zone in which they were driving. They would get a ticket if: 1) they're in a 'private' `zone` and their speed is above 5, 2) they're in a 'local' `zone` and their speed is above 25, or 3) they're in a 'highway' `zone` and their speed is above 65. 
# 
# For example, if the driver's `speed` was 25 and their zone was 'local', the function would `return` `False`. However, if in the same zone, and their speed were 26, the function would `return` `True`. 
# 
# Consider the function provided here and debug in the cell below to accomplish the task described above:
# 
# ```python
# def give_ticket(self, zone, speed):
#     if zone = 'private' or speed > 5:
#         print(True)
#     elif zone = 'local' or speed > 25:
#         print(True)
#     elif zone = 'highway' or speed > 65:
#         print(True)
#     else:
#         print(False)
# ```
# 
# You can start by copy + pasting the code from here into the cell below and then start the process of debugging. 
# 
# Note: Do not change the name of the function (`give_ticket`), and the parameter names provided in the instructions (`speed`, `zone`) must be used.

# In[11]:


### BEGIN SOLUTION
def give_ticket(zone, speed):

    if zone == 'private' and speed > 5:
        ticket = True
    elif zone == 'local' and speed > 25:
        ticket = True
    elif zone == 'highway' and speed > 65:
        ticket = True
    else:
        ticket = False

    return ticket
### END SOLUTION


# In[12]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)


# In[13]:


assert give_ticket
### BEGIN HIDDEN TESTS
assert give_ticket(speed=6, zone='private') 
assert give_ticket(speed=26, zone='local') 
assert give_ticket(speed=66, zone='highway') 
### END HIDDEN TESTS


# In[14]:


assert callable(give_ticket)
### BEGIN HIDDEN TESTS
assert not give_ticket(speed=5, zone='private') 
assert not give_ticket(speed=10, zone='local') 
assert not give_ticket(speed=45, zone='highway') 
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# Check if points lost on autograder above: 
# - `self` removed as a parameter (**0.1 pts**)
# - fixed conditional operator `=` to `==` (**0.25 pts**)
# - `or` changed to `and` in conditional (**0.25 pts**)
# - `print()` statements changed to store variable (**0.25 pts**)
# - `reuturn` statement added (**0.15 pts**)
#                                                               
# === END MARK SCHEME ===

# ## Part 2: Functions (4.4 points)

# ### Q4 - Function Execution (1 point)
# 
# The function `modify_string()` has been provided for you below. 
# 
# **Part 1** (0.75 points)
# 
# First, in the cell provided below containing `YOUR ANSWER HERE`, describe what the `modify_string()` function accomplishes. This should include both 1) the overall task accomplished and 2) how the specific code used accomplishes this task.

# In[15]:


# function provided
# cell cannot be edited
def modify_string(input_string):
    new_language = {'a': 'ӓ',
                    'e' : 'ɚ',
                    'i' : '¡',
                    'o' : 'ð',
                    'u' : 'û',
                    'A' : 'Ӓ',
                    'E' : 'ɛ', 
                    'O' : 'Ó', 
                    'U' : 'Ü'} 
    modified_name = ''
    
    for letter in input_string:
        if letter in new_language:
            modified_name = modified_name + new_language[letter]
        else:
            modified_name = modified_name + letter

    return modified_name


# In[16]:


# BE SURE YOUR ANSWER IS IN THE CELL BELOW
# but you can use this cell to test/execute/check your thinking (optional)


# Describe the `modify_string()` function here.
# 
# 
# === BEGIN MARK SCHEME ===
# 
# - explains task generally accurately (**0.25 pts**)
# - explains what loop accomplishes accurately; links `input_string` parameter to how it is referenced in the code (**0.25 pts**)
# - explains how `modified_name` is updated/extended correctly w/ reference to `new_language` dictionary (**0.25 pts**)
# 
# === END MARK SCHEME ===

# **Part 2** (0.25 points)
# 
# Execute the `modify_string()` function such that it:
# - `return`s `'CÓGS18 ɛxӓm Dӓy'`; assign this output to the variable `out_string`.

# In[17]:


### BEGIN SOLUTION
out_string = modify_string('COGS18 Exam Day')
out_string
### END SOLUTION


# In[18]:


assert out_string
### BEGIN HIDDEN TESTS
assert out_string == 'CÓGS18 ɛxӓm Dӓy'
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# - remove autograder credit above if function not executed
# 
# === END MARK SCHEME ===

# ### Q5 - Function I: `wear_mask()`  (1.65 points)
# 
# While the rules have and will continue to change, we want a function that will help us determine if a mask should be worn.
# 
# This function `wear_mask()` will have three parameters:
# - `group_size`, which will have no default value
# - `location`, which should take the default value 'indoors' (a string)
# - `vaccinated`, which should take the default value `True` (a boolean)
# 
# This function will `return` the string specified below using the following logic:
# - if `vaccinated` is `False` (regardless of other parameter values),: `return`s 'Masking required'
# - if `vaccinated` is True:
#     - ...and if `location` is 'outdoors', and `group_size` is any value: `return`s 'Masking encouraged'
#     - ...and if `location` is 'indoors' and `group_size` is > 1: `return`s 'Masking required'
#     - ...and any other condition: `return`s 'Mask requirement uncertain'
# 
# Note that the string `return`ed must match exactly to string provided above. Likely best to copy + paste to avoid typos.
# 
# For example:
# - `wear_mask(group_size=10, location = 'indoors')` would `return` 'Masking required'
# - `wear_mask(group_size=10, location='outdoors')` would `return` 'Masking encouraged'
# - `wear_mask(group_size=10, location='outdoors', vaccinated=False)` would `return` 'Masking required'
# - `wear_mask(group_size=1, location='indoors')` would `return` 'Mask requirement uncertain'

# In[19]:


### BEGIN SOLUTION
def wear_mask(group_size, location='indoors', vaccinated=True):
    if not vaccinated:
        output = 'Masking required'
    else:
        if location == 'outdoors':
            output = 'Masking encouraged'

        elif location == 'indoors' and group_size > 1:
            output = 'Masking required'
        else:
            output = 'Mask requirement uncertain'
    
    return output
### END SOLUTION


# In[20]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)


# In[21]:


assert wear_mask
### BEGIN HIDDEN TESTS
assert wear_mask(group_size=10, location='outdoors', vaccinated=False) == 'Masking required'
### END HIDDEN TESTS


# In[22]:


# hidden test to check functionality
### BEGIN HIDDEN TESTS
# check indoors
assert wear_mask(group_size=10, location='indoors') == 'Masking required'
### END HIDDEN TESTS


# In[23]:


# hidden test to check functionality
### BEGIN HIDDEN TESTS
# check outdoors
assert wear_mask(group_size=1, location='outdoors') == 'Masking encouraged'
### END HIDDEN TESTS


# In[24]:


# hidden test to check functionality
### BEGIN HIDDEN TESTS
# check default values
assert wear_mask(1) == 'Mask requirement uncertain'
### END HIDDEN TESTS


# In[25]:


# hidden test to check functionality
### BEGIN HIDDEN TESTS
# check outdoors, but state vaccinated explicitly
assert wear_mask(group_size=1, location='outdoors', vaccinated=True) == 'Masking encouraged'
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# Check if points lost on autograder above: 
# - `def` correct with 3 parameters (**0.1 pts**)
# - `location` and `vaccinated` take default values correctly (**0.1 pts**)
# - condition for `not vaccinated` correct (**0.2 pts**)
# - condition for `location` correct (**0.2 pts**)
# - `else` condition for 'Mask requirement uncertain.' included (**0.2 pts**)
# - includes `return` statement (**0.1 pts**)
# 
# Note: if only issue is `return` statement is missing, return autograder credit lost and only deduct for `return` 
# statement missing
# 
# === END MARK SCHEME ===

# ### Q6 - Function II: `write_tickets()` (1.75 points)
# 
# Here you will write a function `write_tickets()` that will take a dictionary as input (using the parameter `input_dict`) and determine who in that dictionary will receive a ticket. The key in the `input_dict` will be the person's name, and the value will be a list of two values. The first value will be the person's zone ('private', 'local', or 'highway') and the second will be the speed at which the person was traveling. This function will `return` an output dictionary. Inside the output dictionary, the name of every person in the original dictionary will be the keys for the output dictionary. The value for each individual's key will be either the boolean `True` (if that person should receive a ticket) or `False` (if they should not), using the same logic as was described in Q3. 
# 
# For example: `write_tickets({'Shannon' : ['local', 20], 'Josh' : ['highway', 80]})` should `return` the dictionary `{'Shannon' : False, 'Josh' : True}`
# 
# Note: You can assume that each key in the input dictionary only shows up one time. You do not need to worry about how to handle the same name showing up more than once.

# In[26]:


### BEGIN SOLUTION
def write_tickets(input_dict):
    output_dict = {}
    
    for key in input_dict:
        zone = input_dict[key][0]
        speed = input_dict[key][1]
        
        if zone == 'private' and speed > 5:
            output_dict[key] = True
        elif zone == 'local' and speed > 25:
            output_dict[key] = True
        elif zone == 'highway' and speed > 65:
            output_dict[key] = True
        else:
            output_dict[key] = False

    return output_dict
### END SOLUTION


# In[27]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)


# In[28]:


assert write_tickets
### BEGIN HIDDEN TESTS
# check provided example
assert write_tickets({'Shannon' : ['local', 20], 'Josh' : ['highway', 80]}) == {'Shannon': False, 'Josh': True}
### END HIDDEN TESTS


# In[29]:


# hidden test to check function accomplishes task
### BEGIN HIDDEN TESTS
# check for parameter name
assert write_tickets(input_dict = {'Shannon' : ['private', 20], 'Josh' : ['highway', 80]}) == {'Shannon': True, 'Josh': True}
### END HIDDEN TESTS


# In[30]:


# hidden test to check function accomplishes task
### BEGIN HIDDEN TESTS
# check for a more than two values
assert write_tickets({'Shannon' : ['local', 20], 
                      'Kenny' : ['private', 20], 
                      'Josh' : ['highway', 80]}) == {'Shannon': False, 'Kenny': True, 'Josh': True}
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# Check if points lost on autograder above: 
# - function defined correctly with `input_dict` parameter (**0.1 pts**)
# - some output dictionary initialized (**0.2 pts**)
# - indexing into input_dict done correctly (**0.25 pts**)
# - loops through input_list correctly (or equivalent) (**0.15 pts**) 
# - conditionals included (even if not quite correct) (**0.2 pts**)
# - output dictionary updated correctly (**0.25 pts**)
# - includes `return` statement (**0.1 pts**) 
# 
# === END MARK SCHEME ===

# ## Part 3: Classes (4.5 points)

# ### Q7 - Classes I: `Warehouse()` (2.25 points)
# 
# Define a class `Warehouse()` that meets the following specifications:
# 
# - has a class attribute: `purpose` which always has the value 'storing goods'
# 
# - has two instance attributes:
#     - `location`, which is a specified by the user on creation of a `Warehouse()` type object using the `location` parameter
#     - `industry`, which is a specified by the user on creation of a `Warehouse()` type object using the `industry` parameter
# - a single method `return_info()`, which will `return` information about the warehouse object as a string. Specifically, this string will be: `'This warehouse is located at [location]. Its purpose is for [purpose] from the [industry] industry.`, where the values in brackets are replaced by the object's attributes. 
# 
# Note: there should not be brackets in your `return`ed string. The brackets above indicate that the value in between the brackets is what you should replace with the object's attributes.

# In[31]:


### BEGIN SOLUTION
class Warehouse():
        
    purpose = 'storing goods'
    
    def __init__(self, location, industry):
        self.location = location
        self.industry = industry
        
    def return_info(self):
        return 'This warehouse is located at ' + self.location + '. Its purpose is for ' + self.purpose + ' from the ' + self.industry + ' industry.'
### END SOLUTION


# In[32]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)


# In[33]:


assert callable(Warehouse)
### BEGIN HIDDEN TESTS
my_warehouse = Warehouse('California', 'automotive')
### END HIDDEN TESTS


# In[34]:


# tests for class attribute
### BEGIN HIDDEN TESTS
assert my_warehouse.purpose == 'storing goods'
### END HIDDEN TESTS


# In[35]:


# tests for instance attributes
### BEGIN HIDDEN TESTS
assert my_warehouse.location == 'California'
assert my_warehouse.industry == 'automotive'
### END HIDDEN TESTS


# In[36]:


# tests for method
assert callable(Warehouse.return_info)
### BEGIN HIDDEN TESTS
assert my_warehouse.return_info() == 'This warehouse is located at California. Its purpose is for storing goods from the automotive industry.'
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# Check if points lost on autograder above: 
# - `class` defined correctly (**0.1 pts**)
# - class attribute correct (**0.2 pts**)
# - instance attributes
#     - `def __init__(self)` correct (**0.2 pts**)
#     - `self` used within definition (**0.2 pts**)
#     - `location` and `industry` attribute initialized correctly (parameters) (**0.2 pts**)
# - `return_info` method:
#     - method definition correct with `self` (**0.2 pts**)
#     - string concatenation used (**0.1 pts**)
#     - uses self. to refer to attributes  (**0.2 pts**)
#     - `return` statement included (**0.1 pts**)
# 
# Note: autograder credit can be returned for portions above if particular aspect (class attribute, instance attribute, or method) were correct, but test failed because overall `class` was defined incorrectly
# 
# === END MARK SCHEME ===

# ### Q8 - Classes II: `TaskCalculator()` (2.25 points)
# 
# Define a class `TaskCalculator()` to keep track of how much time day's tasks will likely take.
# 
# This should have a single instance attribute: `daily_tasks`, which is initialized as an empty list.
# 
# It will then have two methods: `add_task` and `calculate_time`.
# 
# `add_task()`:
# - will have one parameter `task`
# - this method will add the string specified in `task` to the end of the list stored in the instance attribute `daily_tasks`
# 
# `calculate_time()`:
# - will have two lists defined within it: 
#     ```python
#     long_tasks = ['write one exam', 'grade exam', 'prep lecture', 'office hours']
#     short_tasks = ['review lecture', 'grade assignment', 'staff meeting', 'answer email']
#     ```
# - the code will then determine, given the values in the instance attribute `daily_tasks`, how long the `daily_tasks` are estimated to take, using the following logic:
#     - each value in `long_tasks` is estimated to take 2 hours
#     - each value in `short_tasks` is estimated to take 1 hour
# - the number of hours estimated should be `return`ed from this method as an integer (if `daily_tasks` is an empty list or does not have any tasks in either `long_tasks` or `short_tasks`, the method should `return` 0 (zero))

# In[37]:


### BEGIN SOLUTION
class TaskCalculator():
    
    def __init__(self):
        self.daily_tasks = []
        
    def add_task(self, task):
        self.daily_tasks.append(task)
        
    def calculate_time(self):
        long_tasks = ['write one exam', 'grade exam', 'prep lecture', 'office hours']
        short_tasks = ['review lecture', 'grade assignment', 'staff meeting', 'answer email']
        
        time_sum = 0
        
        for val in self.daily_tasks:
            if val in long_tasks:
                time_sum += 2
            elif val in short_tasks:
                time_sum +=1
                
        return time_sum
### END SOLUTION


# In[38]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)


# In[39]:


assert callable(TaskCalculator)
# hidden tests to check object can be created and empty list is initialized
### BEGIN HIDDEN TESTS
my_tasks = TaskCalculator()
assert my_tasks.daily_tasks == []
### END HIDDEN TESTS


# In[40]:


# check calculate_time method before adding tasks
### BEGIN HIDDEN TESTS
assert my_tasks.calculate_time() == 0
### END HIDDEN TESTS


# In[41]:


# check add_task method by adding tasks
### BEGIN HIDDEN TESTS
my_tasks.add_task('write one exam')
my_tasks.add_task('review lecture')
assert my_tasks.daily_tasks == ['write one exam', 'review lecture']
### END HIDDEN TESTS


# In[42]:


# check calculate_time method after adding tasks
### BEGIN HIDDEN TESTS
assert my_tasks.calculate_time() == 3
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# Check if points lost on autograder above: 
# - `class` defined correctly (**0.1 pts**)
# - instance attribute
#     - `def __init__(self)` correct (**0.1 pts**)
#     - `daily_tasks` attribute initialized correctly (empty list) (**0.1 pts**)
# 
# - `add_task` method:
#     - method definition correct with `self`, `task` (**0.1 pts**)
#     - `self` referenced within method  (**0.1 pts**)
#     - extends list correctly; `append` (**0.1 pts**)
# 
# - `calculate_item` method:
#     - method definition correct with `self` (**0.15 pts**)
#     - `long_tasks` and `short_tasks` defined wtihin method (**0.05 pts**)
#     - some variable initialized with 0; this variable `return`ed from function (**0.15 pts**)
#     - loops correctly through list attribute  (**0.15 pts**)
#     - variable tracking hours updated correctly  (**0.15 pts**)
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
