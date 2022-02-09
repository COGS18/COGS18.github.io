#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# Due Dates:
# - **CL6** due tonight (11:59 PM)
# - **A3** due tomorrow (Thurs 2/10; 11:59 PM)
# 
# Notes:
# - mid-course EC posted
# - reminder about interactions with staff
# - Code Style guide has been posted
# - **E1**
#     - regrades submitted so far have been addressed
#     - **E1 Q10**: if the only thing wrong was a typo in your string, you should have had autograder credit returned and been deducted only 0.05 points for typo; submit a regrade request if not the case
# - **E2** plan
#     - Review: next Wed in class (2/16)
#     - Exam released: next Thursday (2/17; 3 PM)
#     - No lecture next Friday
#     - Exam due: Sunday 2/20 (11:59 PM)

# **Mid-course Survey Summary** 
# - N=283
# - Approximate hours spent:
#     - A1: 2
#     - A2: 3
#     - E1 Studying: 3
#     - E1 Completing: 2.5
# - A2/E1 more difficult than A1
# - Coding labs maybe a bit too long
# - if you asked a question, should have gotten a response via Campuswire DM/email

# **Q&A**
# 
# Q: In class we saw that using car['model'] and car.get('model') produced the same result for a dictionary. If they are effectively the same, what would be the reason to use the get method over simply using square braces?  
# A: While python *tries* to prioritize having *one* way to do things, it sometimes falls short. This is one case where there are two equivalent ways. As fair as I'm concerned, pick one and stick to it for consistency...whichever is more readable for you.
# 
# Q: I am still not sure about where the return statement should be in a loop. Can you go over that again?  
# A: The return statement should be placed where/when you want the output to return. If you want it to return the first time through your loop (typically you don't want this), the `return` statement would be indented within the loop. If you want it to `return` once the loop terminates, it would be after the loop and at the same level of indentation as the loop. This is a great question for office hours if still confused.
# 
# Q: I tried the same example and I defined the list of vowels inside the function yet it still said there was an error with the list of vowels being defined before assignment, but when I just rewrote my code it was fine, so does python get overwhelmed or need to restart sometimes?  
# A: No, you likely hadn't re-executed the cell after moving the list inside the function? 
# 
# Q: Will the codes changed in class by instructor be updated in our lecture notes? It seems like it doesn't, but I'd like to have it.   
# A: The updated notes from the previous class are posted to the course website before the next day's class.
# 
# Q: Can I append 2 lists together somehow? Do we need to know algorithms for the upcoming exam?  
# A: Yes - if you want to take two lists and turn them into one list, you can use the `+` operator. And, the algorithms notes do not introduce any new topics, but help solidify understanding of functions + loops, so it may be good to review, but there is nothing new topic-wise in that lecture.

# # Classes
# 
# - objects
# - `class`
#     - attributes
#     - methods
# - instances
#     - `__init__`

# ## Objects
# 
# <div class="alert alert-success">
# Objects are an organization of data (called <b>attributes</b>), with associated code to operate on that data (functions defined on the objects, called <b>methods</b>).
# </div>

# #### Clicker Question #1
# 
# Given what we've discussed in this course so far, if you wanted to store information about a date, how would you do so?
# 
# - A) string
# - B) dictionary
# - C) list
# - D) integers stored in separate variables

# ### Storing Dates (Motivation)

# In[ ]:


# A date, stored as a string
date_string = '29/09/1988'
print(date_string)


# In[ ]:


# A date, stored as a list of number
date_list = ['29', '09', '1988']
date_list


# In[ ]:


# A date, stored as a series of numbers
day = 29
month = 9
year = 1988

print(day)


# In[ ]:


# A date, stored as a dictionary
date_dictionary = {'day': 29, 'month': 9, 'year': 1988}
date_dictionary


# Ways to organize data (variables) and functions together. 

# ### Example Object: Date

# In[ ]:


# Import a date object
from datetime import date


# In[ ]:


get_ipython().run_line_magic('pinfo', 'date')


# In[ ]:


# Set the data we want to store in our date object
day = 29
month = 9
year = 1988

# Create a date object
my_date = date(year, month, day)
print(my_date)


# In[ ]:


# Check what type of thing `my_date` is
type(my_date) 


# ## Accessing Attributes & Methods

# <div class="alert alert-success">
# Attributes and methods are accessed with a <code>.</code>, followed by the attribute/method name on the object. 
# </div>

# ### Date - Attributes
# 
# Attributes look up & return information about the object.

# **attributes** maintain the object's state, simply returning information about the object to you

# In[ ]:


# Get the day attribute
my_date.day


# In[ ]:


# Get the month attribute
my_date.month


# In[ ]:


# Get the year attribute
my_date.year


# ### Date - Methods
# 
# These are _functions_ that *belong* to and operate on the object directly.

# **methods** modify the object's state

# In[ ]:


# Method to return what day of the week the date is
my_date.weekday()


# In[ ]:


# Reminder: check documentation with '?'
get_ipython().run_line_magic('pinfo', 'date.weekday')


# It's also possible to carry out operations on multiple date objects.

# In[ ]:


# define a second date
my_date2 = date(1980, 7, 29)
print(my_date, my_date2)


# In[ ]:


# calculate the difference between times
time_diff = my_date - my_date2
print(time_diff.days,  "days") #in days
print(time_diff.days/365,"years") #in years


# ### Listing Attributes & Methods : `dir`

# In[ ]:


# tab complete to access
# methods and attributes
my_date.

# works to find attributes and methods
# for date type objects generally
date.


# In[ ]:


## dir ouputs all methods and attributes
## we'll talk about the double underscores next lecture
dir(my_date)


# #### Clicker Question #2
# 
# Given the code below:

# In[ ]:


my_date = date(year = 1050, month = 12, day = 12)


# Which is the best description:
# - A) `my_date` is an object, with methods that store data, and attributes that store procedures
# - B) `my_date` is variable, and can be used with functions
# - C) `my_date` is an attribute, with methods attached to it
# - D) `my_date` is a method, and also has attributes
# - E) `my_date` is an object, with attributes that store data, and methods that store procedures

# #### Clicker Question #3
# 
# For an object `lets` with a method `do_something`, how would you execute that method?
# 
# - A) `do_something(lets)`
# - B) `lets.do_something`
# - C) `lets.do_something()`
# - D) `lets.do.something()`
# - E) ¯\\\_(ツ)\_/¯

# #### Clicker Question #4
# 
# For an object `lets` with an attribute `name`, how would you return the information stored in `name` for the object `lets`?
# 
# - A) `name(lets)`
# - B) `lets.name`
# - C) `lets.name()`
# - D) lets.get.name()
# - E) ¯\\\_(ツ)\_/¯

# ### Objects Summary
# 
# - Objects allow for data (attributes) and functions (methods) to be organized together
#     - methods operate on the object type (modify state)
#     - attributes store and return information (data) about the object (maintain state)
# - `dir()` returns methods & attributes for an object
# - Syntax:
#     - `obj.method()`
#     - `obj.attribute`
# - `date` and `datetime` are two types of objects in Python

# ## Classes

# <div class="alert alert-success">
# <b>Classes</b> define objects. The <code>class</code> keyword opens a code block for instructions on how to create objects of a particular type.
# </div>

# Think of classes as the _blueprint_ for creating and defining objects and their properties (methods, attributes, etc.). They keep related things together and organized.

# ## Example Class: Dog

# In[ ]:


# Define a class with `class`. 
# By convention, class definitions use CapWords (Pascal)
class Dog():
    
    # Class attributes for objects of type Dog
    sound = 'Woof'
    
    # Class methods for objects of type Dog
    def speak(self, n_times=2):
        return self.sound * n_times


# A reminder:
# - **attributes** maintain the object's state; they lookup information about an object
# - **methods** alter the object's state; they run a function on an object

# **`class`** notes:
# 
# - classes tend to use **CapWords** convention (Pascal Case)
#     - instead of snake_case (functions and variable names)
# - `()` after `Dog` indicate that this is callable
#     - like functions, Classes must be executed before they take effect
# - can define **attributes** & **methods** within `class`
# - `self` is a special parameter for use by an object
#     - refers to the thing (object) itself
# - like functions, a new namespace is created within a Class
# 

# In[ ]:


# Initialize a dog object
george = Dog()


# In[ ]:


# george, has 'sound' attribute(s) from Dog()
george.sound


# In[ ]:


# george, has 'Dog' method(s)
# remember we used `self`
george.speak()


# #### Clicker Question #5
# 
# Which of the following statements is true about the example we've been using? 

# In[ ]:


class Dog():
    
    sound = 'Woof'
    
    def speak(self, n_times=2):
        return self.sound * n_times


# - A) `Dog` is a Class, `sound` is an attribute, and `speak` is a method. 
# - B) `Dog` is a function, `sound` is an attribute, and `speak` is a method. 
# - C) `Dog` is a Class, `sound` is a method, and `speak` is an attribute. 
# - D) `Dog` is a function, `sound` is an method, and `speak` is an attribute. 

# ### Using our Dog Objects

# In[ ]:


# Initialize a group of dogs
pack_of_dogs = [Dog(), Dog(), Dog(), Dog()]


# In[ ]:


# take a look at this
pack_of_dogs


# In[ ]:


# take a look at this
type(pack_of_dogs[0])


# In[ ]:


for dog in pack_of_dogs:
    print(dog.speak())


# ## Instances & self

# <div class="alert alert-success">
# An <b>instance</b> is particular instantiation of a class object. <code>self</code> refers to the current instance. 
# </div>

# In[ ]:


# Initialize a dog object
george = Dog()


# From our example above:
# 
# - Dog is the Class we created
# - `george` was an _instance_ of that class
# - self just refers to whatever the _current_ instance is

# #### Clicker Question #6
# 
# How many instances of `Dog()` are created below and how many times does the `speak()` method execute?

# In[ ]:


pack_of_dogs = [Dog(), Dog(), Dog(), Dog()]

counter = 1

for doggie in pack_of_dogs:
    if counter <= 2:
        print(doggie.speak())
        counter += 1
    else:
        break


# - A) 2 instances, 2 method executions
# - B) 2 instances, 4 method executions
# - C) 4 instances, 2 method executions
# - D) 4 instances, 4 method executions
# - E) ¯\\\_(ツ)\_/¯

# ## Instance Attributes
# 
# An instance attribute specific to the instance we're on. This allows different instances of the same class to be unique (have different values stored in attributes and use those in methods).

# In[ ]:


# Initialize a group of dogs
pack_of_dogs = [Dog(), Dog(), Dog(), Dog()]


# This creates four different `Dog` type objects and stores them in a list. But, up until now...every `Dog` was pretty much the same.

# <div class="alert alert-success">
# Instance attributes are attributes that we can make be different for each instance of a class. <code>__init__</code> is a special method used to define instance attributes. 
# </div>

# ## Example Class: Dog Revisited
# 
# - Two trailing underscores (a `dunder`, or double underscore) is used to indicate something Python recognizes and knows what to do every time it sees it.
# - Here, we use `__init__` to execute the code within it every time you initialize an object.

# In[ ]:


class Dog():
    
    # Class attributes for Dogs
    sound = 'Woof'
    
    # Initializer, allows us to specify instance-specific attributes
    # leading and trailing double underscores indicates that this is special to Python
    def __init__(self, name):
        self.name = name
    
    def speak(self, n_times=2):
        return self.sound * n_times


# In[ ]:


# Initialize a dog
# what goes in the parentheses is defined in the __init__
gary = Dog(name = 'Gary') 


# In[ ]:


# Check gary's attributes
print(gary.sound)    # This is an class attribute
print(gary.name)     # This is a instance attribute


# In[ ]:


# Check gary's methods
gary.speak()


# #### Clicker Question #7
# 
# Edit the code we've been using for the Class `Dog` to include information about the breed of the Class Dog in `NewDog`?

# In[ ]:


# EDIT CODE HERE
class NewDog():
    
    sound = 'Woof'
    
    def __init__(self, name):
        self.name = name
    
    def speak(self, n_times=2):
        return self.sound * n_times


# In[ ]:


## We'll execute here


# - A) I did it!
# - B) I think I did it!
# - C) So lost. -_-

# ## Class example: Cat

# In[ ]:


# Define a class 'Cat'
class Cat():
    
    sound = "Meow"
    
    def __init__(self, name):
        self.name = name
    
    def speak(self, n_times=2):
        return self.sound * n_times


# ## Instances Examples

# In[ ]:


# Define some instances of our objects
pets = [Cat('Jaspurr'), Dog('Barkley'), 
        Cat('Picatso'), Dog('Ruffius')]


# In[ ]:


for pet in pets:
    print(pet.name, ' says:')
    print(pet.speak())


# #### Clicker Question #8
# 
# What will the following code snippet print out?

# In[ ]:


class MyClass():
    
    def __init__(self, name, email, score):
        self.name = name
        self.email = email
        self.score = score
    
    def check_score(self):        
        if self.score <= 65:
            return self.email
        else:
            return None


# In[ ]:


student = MyClass('Rob', 'rob@python.com', 62)
student.check_score()


# - A) True
# - B) 'Rob'
# - C) False 
# - D) 'rob@python.com'
# - E) None

# ## Code Style: Classes
# 
# - CapWords for class names
# - one blank line between methods/functions

# **Good Code Style**

# In[1]:


class MyClass():
    
    def __init__(self, name, email, score):
        self.name = name
        self.email = email
        self.score = score
    
    def check_score(self):        
        if self.score <= 65:
            return self.email
        else:
            return None


# **Code Style to Avoid**

# In[ ]:


class my_class(): # uses snake case for name
    def __init__(self, name, email, score):
        self.name = name
        self.email = email
        self.score = score   # no blank lines between methods  
    def check_score(self):        
        if self.score <= 65:
            return self.email
        else:
            return None


# ### Example: `ProfCourses()`
# 
# Let's put a lot of these concepts together in a more complicated example...
# 
# What if we wanted some object type that would allow us to keep track of Professor Ellis' Courses? Well...we'd want this to work for any Professor, so we'll call it `ProfCourses`.
# 
# We would likely want an object type and then helpful methods that allow us to add a class to the course inventory and to compare between courses.

# In[ ]:


class ProfCourses():
    
    # create three instance attributes
    def __init__(self, prof):
        self.n_courses = 0
        self.courses = []
        self.prof = prof


# In[ ]:


ellis_courses = ProfCourses('Ellis')
print(ellis_courses.n_classes)
print(ellis_courses.prof)


# **`add_class()` method**

# In[ ]:


class ProfCourses():
    
    def __init__(self, prof):
        self.n_courses = 0
        self.courses = []
        self.prof = prof
    
    # add method that will add classes as a dictionary
    # to our attribute (classes)...which is a list
    def add_course(self, course_name, quarter, n_students):
        
        self.courses.append({'course_name': course_name,
                             'quarter' : quarter,
                             'n_students': n_students})
        # increase value store in n_classes
        # by 1 any time a class is added
        self.n_classes += 1


# In[ ]:


# create ellis_courses
ellis_courses = ProfCourses('Ellis')

# add a class
ellis_courses.add_course('COGS18', 'fa20', 363)

# see output
print(ellis_courses.courses)
ellis_courses.courses


# **`compare()` method**

# In[ ]:


class ProfCourses():
    
    def __init__(self, prof):
        self.n_courses = 0
        self.courses = []
        self.prof = prof
    
    def add_course(self, course_name, quarter, n_students):
        
        self.courses.append({'course_name': course_name,
                             'quarter' : quarter,
                             'n_students': n_students})
        self.n_courses += 1
        
     
    # add method to compare values in classes
    def compare(self, attribute, direction='most'):
    
        fewest = self.courses[0]
        most = self.courses[0] 
        
        for my_course in self.courses:
            if my_course[attribute] <= fewest[attribute]:
                fewest = my_course
            elif my_course[attribute] >= most[attribute]:
                most = my_course
                
        if direction == 'most':
            output = most
        elif direction == 'fewest':
            output = fewest

        return output


# In[ ]:


# create ellis_courses
ellis_courses = ProfCourses('Ellis')

# add a bunch of classes
ellis_courses.add_course('COGS18', 'fa20', 363)
ellis_courses.add_course('COGS108', 'fa20', 447)
ellis_courses.add_course('COGS18', 'su20', 88)
ellis_courses.add_course('COGS108', 'sp20', 469)
ellis_courses.add_course('COGS108', 'sp19', 825)

# see the courses
print(ellis_courses.n_courses)
ellis_courses.courses


# In[ ]:


# make comparison among all courses
# returns the class with the most students
ellis_courses.compare('n_students')


# In[ ]:


# return the class with the fewest students
ellis_courses.compare('n_students', 'fewest')


# **extending the functionality of the `compare()` method**

# In[ ]:


class ProfCourses():
    
    def __init__(self, prof):
        self.n_courses = 0
        self.courses = []
        self.prof = prof
    
    def add_course(self, course_name, quarter, 
                   n_students, n_exams, n_assignments):
        
        # add in additional key-value pairs
        self.courses.append({'course_name': course_name,
                             'quarter' : quarter,
                             'n_students': n_students,
                             'n_exams' : n_exams,
                             'n_assignments' : n_assignments})
        self.n_courses += 1
        
     
    def compare(self, attribute, direction='most'):
    
        fewest = self.courses[0]
        most = self.courses[0] 
        
        for my_class in self.courses:
            if my_course[attribute] <= fewest[attribute]:
                fewest = my_course
            elif my_course[attribute] >= most[attribute]:
                most = my_course
                
        if direction == 'most':
            output = most
        elif direction == 'fewest':
            output = fewest

        return output


# In[ ]:


# create ellis_courses
ellis_courses = ProfCourses('Ellis')

# add a bunch of classes
ellis_courses.add_course('COGS18', 'fa20', 363, 2, 5)
ellis_courses.add_course('COGS108', 'fa20', 447, 0, 6)
ellis_courses.add_course('COGS18', 'su20', 88, 3, 5)
ellis_courses.add_course('COGS108', 'sp20', 469, 0, 6)
ellis_courses.add_course('COGS108', 'sp19', 825, 0, 5)
ellis_courses.add_course('COGS18', 'fa19', 301, 2, 4)

# see the courses
print(ellis_courses.n_courses)


# In[ ]:


# return the class with the most exams
ellis_courses.compare('n_exams', 'most')


# In[ ]:


# return the class with the fewest assignments
ellis_courses.compare('n_assignments', 'fewest')


# **Improving & updating this code**
# - account for ties in `compare()`
# - edit code in `compare()` to make the `for` loop and following conditional more intuitive
# - add a method to put dictionary in time order
# - etc.

# ### Classes Review
# 
# - `class` creates a new class type
#     - names tend to use CapWords case
#     - can have attributes (including instance attributes) and methods
#         - `obj.attribute` accesses data stored in attribute
#         - `obj.method()` carries out code defined within method 
# 

# - instance attributes defined with `__init__`
#     - `__init__` is a reserved method in Python
#     - This "binds the attributes with the given arguments"
#     - `self` refers to current instance

# - to create an object (instance) of a specified class type (`ClassType`):
#     - `object_name = ClassType(input1, input2)`
#     - `self` is not given an input when creating an object of a specified class

# ## Everything in Python is an Object!

# ### Data variables are objects

# In[ ]:


print(isinstance(True, object))
print(isinstance(1, object))
print(isinstance('word', object))
print(isinstance(None, object))

a = 3
print(isinstance(a, object))


# ### Functions are objects

# In[ ]:


print(isinstance(sum, object))
print(isinstance(max, object))


# In[ ]:


# Custom function are also objects
def my_function():
    print('yay Python!')
    
isinstance(my_function, object)


# ### Class definitions & instances are objects

# In[ ]:


class MyClass():
    def __init__(self):
        self.data = 13

my_instance = MyClass()

print(isinstance(MyClass, object))
print(isinstance(my_instance, object))


# ## Object-Oriented Programming

# <div class="alert alert-success">
# <b>Object-oriented programming (OOP)</b> is a programming paradigm in which code is organized around objects. Python is an OOP programming langauge. 
# </div>
