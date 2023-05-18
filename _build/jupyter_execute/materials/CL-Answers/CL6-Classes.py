#!/usr/bin/env python
# coding: utf-8

# # CL6: Classes
# 
# Welcome to the sixth coding lab!
# 
# In this CodingLab we will revisit functions & then focus on objects. 
# 
# We will also start thinking about exploring all of the Python resources and tools that are available, with an eye towards starting to think about the projects.

# ## Part I: (More) Functions 

# ### Reverse a string Function
# 
# Write a function `reverse_string` that will take a string as an input and `return` the reverse of that string as its output. (For example, if the input were 'apple' the function woudl return 'elppa'
# 
# Note that there are multiple ways in which to approach this. One possible approach would use the logic laid out in this pseudocode:
# 
# ```python
# # define function with input
#     
#     # generate empty string
#     # start counter at the length of the input string
#     
#     # while the counter is more than zero
#         # add the letter at index into the input string starting at end of input string to growing string
#         # decrease counter by 1
#     
#     # return string 
# ```

# In[1]:


### BEGIN SOLUTION
def reverse_string(input_string):
    
    rev = ''
    counter = len(input_string) 
    
    while counter > 0: 
        rev = rev + input_string[counter - 1]
        counter = counter - 1
    
    return rev
### END SOLUTION


# In[2]:


assert reverse_string('apple') == 'elppa'


# ### Palindrome Function
# 
# Write a function `check_palindrome` that takes a string as an input and within that function determines whether the input string is a palindrome or not (a word or phrase that is read the same forward as it is backward - i.e. kayak, dad, etc.). 
# 
# If it is a palindrome, `return` 'Hey! That's a palindrome!'
# 
# If it is not a palindrome, `return` 'Bummer. Not a palindrome.'
# 
# Remember that you created a function that can reverse a string above.

# In[3]:


### BEGIN SOLUTION
def check_palindrome(input_string):
    rev = reverse_string(input_string)

    if rev == input_string:
        out = "Hey! That's a palindrome!"
    else:
        out = "Bummer. Not a palindrome."
    
    return out
### END SOLUTION


# In[4]:


assert check_palindrome('kayak') == "Hey! That's a palindrome!"
assert check_palindrome('blargh') == 'Bummer. Not a palindrome.'


# ## Part II: Objects Questions

# ## Example Class

# In[5]:


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


# In[6]:


# Create an instance of our class
python = Language('python', 'computer', 'lots of')
python.print_goodness_level()


# In[7]:


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

# In[8]:


### BEGIN SOLUTION
class TritonCourse():
    
    university = "UC San Diego"
    
    def __init__(self, department, code, title):

        self.department = department
        self.code = code
        self.title = title
### END SOLUTION


# #### Instances
# 
# Once you've written the class defintion above, you should be able to run the following code to create an instance of this class. 
# 
# You can then print out the attributes and check that they hold the values that you expect. 

# In[9]:


# Define an instance of our class
cogs18 = TritonCourse("COGS", 18, "Introduction to Python")


# In[10]:


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

# In[11]:


### BEGIN SOLUTION
class1  = TritonCourse("ECE",15,"Engineering Programming")
class2 = TritonCourse("MUS", 8, "American Music: Jazz Culture")
### END SOLUTION


# #### Methods
# 
# Now, make a new version of `TritonCourse` that has a method. 
# 
# Specifically, this method, called `print_info` should print out the information about the course as:
# 
#     'department name code : title'
#     
# So, for example, once you add this method, using the method on our `cogs18` instance should `return`:
# 
#     `COGS 18 : Introduction to Python`

# In[1]:


### BEGIN SOLUTION
class TritonCourse():
    
    university = "UC San Diego"
    
    def __init__(self, department, code, title):
    
        self.department = department
        self.code = code
        self.title = title
    
    def print_info(self):
        return self.department + str(self.code) + ': ' + self.title 
### END SOLUTION


# In[2]:


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

# In[3]:


### BEGIN SOLUTION
# specifics will differ between students
print("\nTritonCourse Example:")
class TritonCourse():
    
    university = "UC San Diego"
    location = "La Jolla"
    
    def __init__(self, department, code, title, quarter, enrollment):
    
        self.department = department
        self.code = code
        self.title = title
        self.quarter = quarter
        self.enrollment = enrollment
    
    def print_info(self):
        return self.department + str(self.code) + ': ' + self.title
    
    def determine_large(self):
        if (self.enrollment) > 100:
            output = "large enrollment"
        else:
            output = "typical enrollment"
        return output

# test it out 
my_course = TritonCourse("Cognitive Science", "COGS 18", 
                        "Introduction to Python",
                        "Sp22", 330)
print(my_course.enrollment)
print(my_course.determine_large())

print("\nOffice Hours Example:")
# trying out another class
class OfficeHours():
    
    university = 'UC San Diego'
    
    def __init__(self):
        self.n_students = 0
        self.who_arrived = []
    
    def add_student(self, first_name):
        try:
            assert type(first_name) == str
            self.n_students += 1
            self.who_arrived.append(first_name)
        except:
            print("please provide a first name as a string to the method call")
   
    def busy_OH(self):
        if self.n_students > 10:
            output = 'busy OH'
        else:
            output = 'typical OH'
        return output


may6 = OfficeHours()
may6.add_student(4) # this one will trigger the exception
may6.add_student("Shannon")
may6.add_student("Josh")
print(may6.n_students)
print(may6.who_arrived)
print(may6.busy_OH())
### END SOLUTION


# ### Objects Challenge
# 
# Define a class `Cogs18Students` that has: 
# 
# - Instance Attibutes:
#     - `students` : list (initalize it as an empty list)
# - Methods:
#     - `add_student()`
#     - `calculate_points()`
#     
# #### Method: `add_student`
# 
# Input(s):
# - `pid` : string
# - `a1` : int or float
# - `a2` : int or float
# - `e1` : int or float
# 
# This method, when executed should take in the student's PID and their scores on A1, A2 and E1. These values should be stored in a single dictionary for each student with the keys 'PID', 'A1', 'A1', and 'E1', with the student's respective PID and scores as the values for each key. This dictionary should then be added to the `students` attribute for the class.
# 
# #### Method: `calculate_points`
# 
#  
# Input(s):
# - `student_pid` : string
# 
# This method should calculate the total number of points for all assignments for the student PID specified in `student_pid`. The sum of the students' points on A1, A2, and E1 should be returned from the method.

# In[4]:


### BEGIN SOLUTION
class Cogs18Students:
    
    def __init__(self):
        self.students = []

    def add_student(self, pid, a1, a2, e1):
        self.students.append({'PID': pid,
                              'A1': a1,
                              'A2': a2, 
                              'E1': e1})
        
    def calculate_points(self, student_pid):
        
        total_points = 0
        
        for element in self.students:
            if element['PID'] == student_pid:
                for key in element:
                    if key != 'PID':
                        total_points += element[key]
        
        return total_points

cogs18 = Cogs18Students()  # initialize object
cogs18.add_student('A1234', 8, 8, 12.5)  # add student
cogs18.add_student('A7777', 8, 6, 12.5)  # add another student
print(cogs18.students)  # see what's stored in attribute
cogs18.calculate_points('A7777')  # test out my method
### END SOLUTION


# In[16]:


# initialiaze a Cogs18Students object here
# test out your methods

