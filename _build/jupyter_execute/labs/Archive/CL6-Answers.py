#!/usr/bin/env python
# coding: utf-8

# # CL6: Classes
# 
# Welcome to the sixth coding lab!
# 
# In this CodingLab we will be thinking and working with objects.

# **Note**: Part I is _challenging_. Do your best there. Be sure you understand what attributes and methods are. Be sure you know how to write functions, but if you can't figure it all out, that is OK. Do your best throughout this coding lab. If you get stuck on Part I, go ahead and give Part II and Part II a try!

# ## Part I: Object Explorations

# In[1]:


# Import 
from datetime import date, time, datetime, timedelta


# ## Questions
# 
# - a) What day of the week was January 2nd, 1994
# - b) What is the latest date the datetime object can store? What is the earliest?
#     - Hint: explore using `dir` to see if you can find these values.
# - c) What type of error is raised if you try to create a datetime object that is the 32nd day of any month?
# - d) How many Mondays where there in February, 1916? 

# In[2]:


# YOUR CODE HERE


# In[3]:


# Answer for a
jan2nd = date(1994, 1, 2)
jan2nd.isoweekday()


# In[4]:


# Answer for b
print(date.max)
print(date.min)


# In[5]:


# Answer for c
date(2001, 4, 32)


# In[ ]:


# Answer for d
year = 1916
month = 2
day = 1

counting = True
n_mondays = 0

while counting:
    try:
        dt = date(year, month, day)
        if dt.isoweekday() == 1:
            n_mondays += 1
    except ValueError:
        counting = False
        print('Finished counting.')
    
    day += 1
        
print('The number of Mondays is', n_mondays)


# **Now see if you can turn your answer to part d into a function.**
# 
# This function should be general such that it can calculate the number of times any day of the week occurs in a given month and year. 
# 
# To do this your function should take `year`, `month` and `day_of_the_week` as arguments.

# In[ ]:


# YOUR CODE HERE
def count_days(year, month, day_of_the_week):

    counting = True
    n_days = 0
    day = 1

    while counting:
        try:
            my_date = date(year, month, day)
            if my_date.isoweekday() == day_of_the_week:
                n_days += 1
        except ValueError:
            counting = False

        day += 1
    
    return n_days


# In[ ]:


# Check if your function works
count_days(1854, 3, 4)


# ## Datetime Manipulations
# 
# Using `datetime` objects there are several operations and methods we can use that are useful, some of these are shown as examples below.

# In[6]:


# Get current times
now = datetime.now()


# In[17]:


# Create a time delta object, to represent a 
delta = timedelta(days=1, minutes=7, seconds=37)


# In[18]:


# Add a time
later = now + delta


# In[19]:


# Check out what time it will be after 
#   Note - format is 'YEAR-MONTH-DAY'T'HOUR:MINUTE:SECOND:MICROSECOND'
later.isoformat()


# ### DateTime Manipulation Questions

# - a) What day of the week it will be 4675 days from now?
# - b) Write a boolean if/else stement that checks whether `date_1` is earlier or later than `date_2`, and prints out 'earlier' or 'later' appropriately.

# In[149]:


# YOUR CODE HERE


# In[38]:


# Answer for a
(now+timedelta(days=4657)).isoweekday()


# In[ ]:


# Answer for b
if date_1 < date_2:
    print('Earlier')
else:
    print('Later')


# ### DateTime Manipulation Exploration
# 
# If you start from Jan 1st, 1757, and repeatedly add 8 days, until you hit 1800, how many times will it be a Monday?

# In[9]:


# YOUR CODE HERE
check_date = date(1757, 1, 1)

adding = True
mondays_count = 0
days_to_add = timedelta(days=8)

while adding:

    # Add days
    check_date = check_date + days_to_add
    
    # Check if the date was a monday
    if check_date.isoweekday() == 1:
        mondays_count += 1
    
    # Check if we've hit 
    if check_date.year >= 1800:
        adding = False
        
print('There were', str(mondays_count), 'mondays.')


# #### Make a function
# 
# Once you have answered this question, convert your code into a generalized function. 
# 
# This function, call it `count_weekdays` should take:
# - `start_date`: a start date (a datetime object)
# - `add_days`: a number of days to add (an int)
# - `stop_year`: a stop year (an int)
# - `weekday`: a day to count, represented in isoweekday format (an int)
# 
# It should return the number of `weekday`'s that occur from the start date, until stop year, when adding `add_days` days.

# In[7]:


# YOUR CODE HERE
def count_weekdays(start_date, add_days, stop_year, weekday):

    count = 0
    days_to_add = timedelta(days=add_days)
    check_date = start_date

    while True:

        check_date = check_date + days_to_add

        if check_date.isoweekday() == weekday:
            count += 1

        if check_date.year >= stop_year:
            break
    
    return count


# In[11]:


# Check that the function returns the expected result for an example case
assert count_weekdays(datetime(1322, 6, 17), 3, 1324, 5) == 27


# ## Part II: Objects Questions

# ## Example Class

# In[1]:


class Language():
    """A Python class to store and use information about languages."""
    
    # Class Attributes
    purpose = 'communication'
    
    def __init__(self, name, language_type, amount_of_goodness):
        
        # Instance Attributes
        self.name = name
        self.language_type = language_type
        self.amount_of_goodness = amount_of_goodness
        
    # Class Method
    def print_goodness_level(self):
        print('The language', self.name, 'has', self.amount_of_goodness, 'goodness.')


# In[2]:


# Create an instance of our class
python = Language('python', 'computer', 'lots of')
python.print_goodness_level()


# In[3]:


# Create another instance of our class
english = Language('english', 'human', 'some')
english.print_goodness_level()


# ### TritonCourse class
# 
# Let’s create a class to represent courses at UCSD! 

# #### Class Definition
# 
# Write a class to store information about UCSD courses, called `TritonCourse`. 
# 
# This course assumes all courses belong to a department, have a course code, and have a title.
# 
# That is, write a class called `TritonCourse` that has instance attributes `department` (string), `code` (int), and `title` (string). 

# In[4]:


class TritonCourse():
    
    university = "UC San Diego"
    
    def __init__(self, department, code, title):
        """
        department: string
        code: int
        title: string
        """
    
        self.department = department
        self.code = code
        self.title = title


# #### Instances
# 
# Once you've written the class defintion above, you should be able to run the following code to create an instance of this class. 
# 
# You can then print out the attributes and check that they hold the values that you expect. 

# In[5]:


# Define an instance of our class
cogs18 = TritonCourse("COGS", 18, "Introduction to Python")


# In[6]:


# Check the instance attributes
print(cogs18.department)
print(cogs18.code)
print(cogs18.title)


# Now, create some more instances of our class:
# 
# - ECE 15, "Engineering Programming" 
#     - Save the result to a variable called `class1`
# - MUS 8, "American Music: Jazz Culture"
#     - Save the result to a variable called `class2`

# In[7]:


class1  = TritonCourse("ECE",15,"Engineering Programming")
class2 = TritonCourse("MUS", 8, "American Music: Jazz Culture")


# #### Methods
# 
# Now, make a new version of `TritonCourse` that has a method. 
# 
# Specifically, this method, called `print_info` should print out the information about the course as:
# 
#     'department name code : title'
#     
# So, for example, once you add this method, using the method on our `cogs18` instance should print out:
# 
#     COGS 18 : Introduction to Python

# In[8]:


class TritonCourse():
    
    university = "UC San Diego"
    
    def __init__(self, department, code, title):
        """
        department: string
        code: int
        title: string
        """
    
        self.department = department
        self.code = code
        self.title = title
    
    def print_info(self):
        print(self.department + str(self.code) + ': ' + self.title)


# In[9]:


# Check the method works on our cogs18 instance
cogs18 = TritonCourse("COGS", 18, "Introduction to Python")
cogs18.print_info()


# ## Part III: Objects Explorations
# 
# - What kind of other attributes and methods might we want on our `TritonCourse` object?
#     - Make an extended version of `TritonCourse` with at least one extra class attribute, instance attribute and method. 
# - Create a brand new class, to do something new / different!
#     - Make sure it has at least one class attribute, instance attribute, and some methods
#     - Create at least one methods that takes in an argument (doesn't just use class & instance attributes)
#     - Create at least one method that has a conditional in it, one with a loop, and one with a try/except

# In[ ]:


## YOUR CODE HERE

