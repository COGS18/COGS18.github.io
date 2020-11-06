**Course Announcements**

**Due Dates:**
- **CL5** due tonight (11:59 PM)
- **A4** due Mon 11/16 (11:59 PM) 

**Notes**
- Posted mid-course survey feedback
    - responded to student questions
    - Median time spent on assignments & exam:
        - A1: 2h
        - A2: 3.5
        - Studying for exam: 2h
        - Completing Exam: 2h
    - Big Theme: Harder/more involved examples in lecture, please!
    - Upcoming Extra Credit opportunities? 
        - CAPEs & post-course survey
        - Final Project: project & GitHub
        

# Objects

- `date` & `datetime`
- methods & attributes

#### Clicker Question #1

What would be the best way to store a date?

- A) A string
- B) A list of numbers
- C) It can't be done
- D) A dictionary
- E) Something else

### Storing Dates

# A date, stored as a string
date_string = '29/09/1988'
print(date_string)

# A date, stored as a list of number
date_list = ['29', '09', '1988']
date_list

# A date, stored as a series of numbers
day = 29
month = 9
year = 1988

print(day)

# A date, stored as a dictionary
date_dictionary = {'day': 29, 'month': 9, 'year': 1988}
date_dictionary

## Objects

<div class="alert alert-success">
Objects are an organization of data (called <b>attributes</b>), with associated code to operate on that data (functions defined on the objects, called <b>methods</b>).
</div>

Ways to organize data (variables) and functions together. 

### Example Object: Date

# Import a date object
from datetime import date

date?

date(1988, 9, 29).year

new_date.year

date(day = 29, month = 9, year = 1988)

# Set the data we want to store in our date object
day = 29
month = 9
year = 1988

# Create a date object
my_date = date(year, month, day)
print(my_date)

# Check what type of thing `my_date` is
type(my_date) 

## Accessing Attributes & Methods

<div class="alert alert-success">
Attributes and methods are accessed with a <code>.</code>, followed by the attribute/method name on the object. 
</div>

### Date - Attributes

Attributes look up & return information about the object.

**attributes** maintain the object's state, simply returning information about the object to you

# Get the day attribute
my_date.day

# Get the month attribute
my_date.month

# Get the year attribute
my_date.year

### Date - Methods

These are _functions_ that *belong* to and operate on the object directly.

**methods** modify the object's state

# Method to return what day of the week the date is
my_date.weekday()

# Reminder: check documentation with '?'
date.weekday?

# Get the ISO format representation of the date (as a string)
my_date.isoformat()

# operates on date object
# returns a string
type(my_date.isoformat())

It's also possible to carry out operations on multiple date objects.

# define a second date
my_date2 = date(1980, 7, 29)
print(my_date, my_date2)

# calculate the difference between times
time_diff = my_date - my_date2
print(time_diff.days,  "days") #in days
print(time_diff.days/365,"years") #in years

### Listing Attributes & Methods : `dir`

# tab complete to access
# methods and attributes
my_date.

# works to find attributes and methods
# for date type objects generally
date.

## dir ouputs all methods and attributes
## we'll talk about the double underscores next lecture
dir(my_date)

#### Clicker Question #2

Given the code below:

my_date = date(year = 1050, month = 12, day = 12)

Which is the best description:
- A) `my_date` is an object, with methods that store data, and attributes that store procedures
- B) `my_date` is variable, and can be used with functions
- C) `my_date` is an attribute, with methods attached to it
- D) `my_date` is a method, and also has attributes
- E) `my_date` is an object, with attributes that store data, and methods that store procedures

#### Clicker Question #3

For an object `lets` with a method `do_something`, how would you execute that method?

- A) `do_something(lets)`
- B) `lets.do_something`
- C) `lets.do_something()`
- D) `lets.do.something()`
- E) ¯\\\_(ツ)\_/¯

#### Clicker Question #4

For an object `lets` with an attribute `name`, how would you return the information stored in `name` for the object `lets`?

- A) `name(lets)`
- B) `lets.name`
- C) `lets.name()`
- D) lets.get.name()
- E) ¯\\\_(ツ)\_/¯

### Objects Example: DateTime

from datetime import datetime

# get documentation
datetime?

# Get the current date & time
now = datetime.today()

print(now) 

# Check some attributes of the object
print(now.year)
print(now.day)

# Check a method of the object
print(now.weekday())

### Objects Summary

- Objects allow for data (attributes) and functions (methods) to be organized together
    - methods operate on the object type (modify state)
    - attributes store and return information (data) about the object (maintain state)
- `dir()` returns methods & attributes for an object
- Syntax:
    - `obj.method()`
    - `obj.attribute`
- `date` and `datetime` are two types of objects in Python

### Using `date`/ `datetime` objects in user-defined functions

What if we wanted to determine how many days there was in February of a given year?

We could write a function to do that!

# YOUR CODE HERE
def count_feb_days(year):
    
    #initialize variables
    month = 2
    counting = True
    n_days = 0
    day = 1

    while counting:
        try:
            my_date = date(year, month, day)
            n_days += 1
        except ValueError:
            counting = False

        day += 1
    
    return n_days

# execute your function
count_feb_days(2020)