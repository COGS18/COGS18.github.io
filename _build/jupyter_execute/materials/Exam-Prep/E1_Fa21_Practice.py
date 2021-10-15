#!/usr/bin/env python
# coding: utf-8

# # COGS 18 - Practice Exam
# 
# This is the practice exam for Fall 2021. It covers topics through the Dictionaries Lecture.
# 
# This exam is out of 0 points, worth 0% of your grade, but the real thing will be out of 12.5 points.
# 
# **PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**
# 
# **PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE EXAM.** (Note that you can add additional cells, if you want to test things out.)

# ## Instructions
# 
# #### Timing
# - The exam is designed to take you ~1h.
# - There will be a 24 hour window during which you can complete this exam (due Sat 8AM).
# - If it takes you longer than 1h, you're free to use that time.
# 
# #### The Rules
# - You are to complete this exam on your own.
# - This is open-notes & open-Google
# - You may not talk to any humans about this exam. 
# - The following are all *prohibited*:
#     - text/phone/online chat communication
#     - posting questions to a message board where a human could respond
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


# ## Part 1: Variables & Operators (3.75 points)
# ^ The headers and point values correspond to the actual headers and point values you'll have for each section on your exam

# ### Example Q1 - Variables & Operators 
# 
# In the cell below, create three variables: `var_a`, `var_b`, and `var_c`.
# 
# These variables must satisfy the following requirements:
# 
# 1. `var_a` must store a float (you get to choose the specific float)
# 2. `var_b` must use *at least two* of the comparison operators (`<`,`>`,`<=`,`>=`,`!=`,`==`) and store (return) the value `True`. 
# 3. `var_c` must use *at least two* of the math operators (`+`, `-`, `/`, `*`, `**`, `%`, `//`) and store the value 36

# In[3]:


### BEGIN SOLUTION
# actual variable creation will differ
var_a = 7.3
var_b = 6 == 6 and 3 <= 4
var_c = (6 + 3) * 4
### END SOLUTION


# In[4]:


# check variable exists
assert var_a is not None

### BEGIN HIDDEN TESTS
assert isinstance(var_a, float)
### END HIDDEN TESTS


# In[5]:


assert isinstance(var_b, bool)

### BEGIN HIDDEN TESTS
assert var_b 
### END HIDDEN TESTS


# In[6]:


# check variable exists
assert var_c is not None

### BEGIN HIDDEN TESTS
assert var_c == 36
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

# ## Part 2: Collections & Indexing  (3 points)

# ### Example Q2 - Indexing
# 
# Given a the list `my_list` provided below, include code below *using indexing* to return the values specified below from `my_list`.
# 
# 
# 1. In `list_a`, index `my_list` such that it will store (return) `['c', 'd']`
# 2. In `list_b`, index `my_list` such that it will store (return) `['a', 'c', 'e']`

# In[7]:


# my_list is provided for you
my_list = ['a', 'b', 'c', 'd', 'e']

### BEGIN SOLUTION
# specific indexing approaches may differ
list_a = my_list[2:4]
list_b = my_list[0::2]
### END SOLUTION


# In[8]:


assert isinstance(list_a, list)

### BEGIN HIDDEN TESTS
assert list_a == ['c', 'd']
### END HIDDEN TESTS


# In[9]:


assert isinstance(list_b, list)

### BEGIN HIDDEN TESTS
assert list_b == ['a', 'c', 'e']
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

# ## Part 3: Control Flow - Conditionals & Loops  (5.65  points)
# 
# **Note**: This section is longer and has more questions than what will be on your exam; however, this is where students struggle the most, so I wanted to give you more practice questions.

# ### Example Q3 - `while` loop
# 
# Include code in your answer below that:
# 
# 1. Creates (initializes) a counter `counter` that starts at 0
# 2. Creates (initializes) an empty list `out`
# 3. Creates a loop that will run as long as the value of `counter` is less than or equal to 10
#     - Within the loop:
#         - first: if the value of `counter` is odd, `append` the value of `counter` to the list `out`
#         - then: increase the value of `counter` by 1 each time through the loop 

# In[10]:


### BEGIN SOLUTION
out = []
counter = 0 

while counter <= 10: 
    if counter % 2 != 0:
        out.append(counter)

    counter += 1
### END SOLUTION


# In[11]:


assert counter > 0 & counter < 100

### BEGIN HIDDEN TESTS
assert counter == 11
### END HIDDEN TESTS


# In[12]:


assert isinstance(out, list)

### BEGIN HIDDEN TESTS
assert out == [1, 3, 5, 7, 9]
### END HIDDEN TESTS


# ### Example Q4 - `for` loop
# 
# Store your first name as a string in the variable `my_name` and initialize a `counter` (use that variable name).
# 
# Then, write a `for` loop that loops through the letters of your first name, increasing the counter by one for each consonant (non-vowel) in your name. 
# 
# The value stored in the counter at the end of your loop’s execution should be the number of consonants in your first name. Be sure that 'B' and 'b' are counted as the same letter in your code.
# 

# In[13]:


### BEGIN SOLUTION
# code will differ based on who is taking the exam
my_name = 'Shannon'
counter = 0

for char in my_name:
    char = char.lower()
    if char not in ['a', 'e', 'i', 'o', 'u']:
        counter += 1
        
# OR
# note `vowels` could also be a string
vowels = ['A','E','I','O','U', 'a', 'e', 'i', 'o', 'u']
counter = 0

for char in my_name:
    if char not in vowels:
        counter += 1
### END SOLUTION


# In[14]:


assert isinstance(counter, int)
assert isinstance(my_name, str)

### BEGIN HIDDEN TESTS
count = 0

for char in my_name:
    char = char.lower()
    if char not in ['a', 'e', 'i', 'o', 'u']:
        count += 1
        
assert counter == count
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# 
# === BEGIN MARK SCHEME ===
# 
# - counter & my_name created (0.25 points)
# - for loop initialized correctly (0.25 points)
# - capitalization accounted for (0.5 points)
# - conditional correct (0.5 points)
# 
# === END MARK SCHEME ===

# ### Example Q5 - Conditionals
# 
# Store your desired score on this exam (out of 100 points) in the variable `desired_score`. 
# 
# Then, write a conditional that will compare your `desired_score` to the lower (90) and upper (100) bound for an A on the exam.
# 
# If your desired_score is greater than or equal to the lower bound and less than or equal to the upper bound, store the string `'A desired'` in the variable `output`. Otherwise, store the string `'A not desired'` in the variable `output`.
# 
# Notes: 
# 1. Spelling/capitalization of the string stored in `output` matter. Be sure it matches the string specified in the instructions above.

# In[15]:


### BEGIN SOLUTION
desired_score = 100

# code will differ based on who is taking the exam
if desired_score >= 90 and desired_score <= 100:
    output = 'A desired'
else:
    output = 'A not desired'
### END SOLUTION


# In[16]:


assert output
# test to ensure no typos in string
assert output in ['A desired', 'A not desired']
### BEGIN HIDDEN TESTS
if desired_score >= 90 and desired_score <= 100:
    test = 'A desired'
else:
    test = 'A not desired'

assert test == output
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# 
# === BEGIN MARK SCHEME ===
# 
# - uses `if`/`else` OR `if`/`elif` syntax correctly (**0.5 points**)
# - conditional correct 
#     - references variables (`desired_score`, `A_lower`, `A_upper`) (**0.3 points**)
#     - uses `>=` `and`/`&`, and `<=` (**0.3 points**)
# - `output` assigned a string value (even if there are typos in string) (**0.15 points**)
# 
# === END MARK SCHEME ===

# ### Example Q6 - `for` loop (2 points)
# 
# Background: Imagine that in a few weeks you find yourself wanting to talk to someone on the instructional staff who has actually completed the COGS 18 final project. When this happens, you suddenly remember you created a list of all the staff members in COGS 18 earlier in the quarter when you were practicing with lists. Perfect! You can use this to help you figure out who you should talk to, since you know that all of the IAs previously took COGS 18 and completed the project. They will be able to discuss their experience with you!
# 
# The list of staff members and their role is below and is called `staff`. Run the cell below to generate the `staff` list.
# 
# 
# Then, write code to loop through the provided list. Within the loop, write code that will store any entry in the list with '\_IA' in the entry into a new list. Store this (the entries in `staff` corresponding to IAs) in a new list called `to_contact`.

# In[17]:


# run this to create list
staff = ['Anu_IA', 'Bob_IA', 'Boning_IA', 'Bora_IA', 'David_TA', 'Emma_IA', 
         'Ellis_Prof', 'Frank_IA', 'Mani_IA', 'Harrison_IA', 'Shivani_TA']


# In[18]:


### BEGIN SOLUTION
# code will differ based on who is taking the exam
to_contact = []

for person in staff:
    if '_IA' in person:
        to_contact.append(person)

to_contact
### END SOLUTION


# In[19]:


assert to_contact

### BEGIN HIDDEN TESTS
assert to_contact == ['Anu_IA',
                     'Bob_IA',
                     'Boning_IA',
                     'Bora_IA',
                     'Emma_IA',
                     'Frank_IA',
                     'Mani_IA',
                     'Harrison_IA']
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# - empty list initialized (0.25)
# - for loop set up correctly (0.25)
# - conditional correct (0.5)
# - list extended correctly (0.5)
# 
# === END MARK SCHEME ===

# ### Q7 - Accomplishing a task (1.15 points)
# 
# The goal here is to store the string `"I'm so excited that students are now eligible for the vaccine!"` in a single string. However, right now, each word is separated out into separate elements in a list...
# 
# Using the list below and code constructs we discussed in class, convert the list provided (`vaccination_list`) into a single sentence: `"I'm so excited that students are now eligible for the vaccine!"`. Store this in the variable `sentence`.

# In[20]:


vaccination_list = ["I'm ", "so ", "excited ", "that ", "students ", "are ", 
                    "now ", "eligible ", "for ", "the ", "vaccine!"]


# In[21]:


### BEGIN SOLUTION
sentence = ''

for word in vaccination_list:
    sentence += word
### END SOLUTION


# In[22]:


assert sentence is not None
### BEGIN HIDDEN TESTS
assert sentence == "I'm so excited that students are now eligible for the vaccine!"
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# - `sentence` initialized as empty string (**0.25 points**)
# - `for` loop set up correctly (**0.25 points**)
# - string extended/concatenated correctly (**0.5 points**)  
# 
# === END MARK SCHEME ===

# ### Example Q8 - Accomplishing a task
# 
# Background: Professor Ellis has made a mess of her to do list (`to_do_list`, provided below). She accidentally combined her to do list with her grocery list and the the her daily step count from last week. She needs your help to detangle this mess!
# 
# Your job is to separate `to_do_list` out into three separate lists:
# - `steps` - a list of all the steps from last week (you know which values these are becuase they are integer values)
# - `to_do` - a list that contains the to do list items (you know which values these are because they contain 'cogs' in the string)
# - `grocery` - a list of all of the grocery list items (you know which values these are because they do NOT contain 'cogs' in the string)
# 
# Each of the above lists should contain only the elements from `to_do_list` that match the specified description above. Specifically:
# - `steps` should be a list of integers
# - `to_do` should be a list of strings 
# - `grocery` should be a list of strings
# 
# The values in `steps`, `to_do`, and `grocery` should appear in the same relative order as in the original list (`to_do_list`).
# 
# Note: This should not be hard-coded. Your answer should use code constructs discussed in class. In other words, your code should produce the correct lists, regardless of the specific values in `to_do_list`.

# In[23]:


# run this to create list
to_do_list = ['mushrooms', 'peanut butter', 'release cogs18 exam', 10000, 8500, 
              'release cogs108 lab', 6000, 'tahini', 15000, 'post cogs18 lectures', 
              'post cogs108 lectures', 'release cogs18 practice exam', 12000, 'pineapple', 
              'udon noodles', 18000, 8000, 'romaine lettuce']


# In[24]:


### BEGIN SOLUTION
steps = []
to_do = []
grocery = []

for value in to_do_list:
    if isinstance(value, int):
        steps.append(value)
    else:
        if 'cogs' in value:
            to_do.append(value)
        else: 
            grocery.append(value)
### END SOLUTION


# In[25]:


assert grocery
### BEGIN HIDDEN TESTS
assert grocery == ['mushrooms', 'peanut butter',
                   'tahini', 'pineapple', 'udon noodles',
                   'romaine lettuce']
### END HIDDEN TESTS


# In[26]:


assert steps
### BEGIN HIDDEN TESTS
assert steps == [10000, 8500, 6000, 15000, 12000, 18000, 8000]
### END HIDDEN TESTS


# In[27]:


assert to_do
### BEGIN HIDDEN TESTS
assert to_do ==  ['release cogs18 exam', 'release cogs108 lab',
                  'post cogs18 lectures', 'post cogs108 lectures',
                  'release cogs18 practice exam']
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# - empty lists initialized (0.25)
# - for loop set up correctly (0.25)
# - conditionals correct (0.25)
# - list appended correctly (0.25)
# 
# === END MARK SCHEME ===

# ### Submit on Datahub
# 
# Good work - you're done!
# 
# Check your work, and then when you're ready, **submit on datahub**.
# 
# We will not have your exam until you click submit and see this show up under 'submitted assignments'.
