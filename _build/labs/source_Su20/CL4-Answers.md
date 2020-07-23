---
interact_link: content/labs/source_Su20/CL4-Answers.ipynb
download_link: assets/downloads/CL4-Answers.ipynb.zip
title: 'CL4-Answers'
prev_page:
  url: /labs/source_Su20/CL3-Answers
  title: 'CL3-Answers'
next_page:
  url: /
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# CL4: Debugging & Classes

Welcome to the fourth coding lab!

In this CodingLab we will be thinking and working with debugging, classes, and objects.

**Note**: Part III is _challenging_. Do your best there. Be sure you understand what attributes and methods are. Be sure you know how to write functions, but if you can't figure it all out, that is OK. Do your best throughout this coding lab. If you get stuck on Part III, go ahead and give Part IV and Part V a try!

## Part I: Debugging Questions

### Creating Errors
For each of the follow Exceptions, write a small piece of code that will cause it to happen:
- ZeroDivisionError
- SyntaxError
- IndentationError
- TypeError
- IndexError
- KeyError
- ValueError
- NameError



{:.input_area}
```python
# Zero Division Answer
1/0
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
ZeroDivisionError                         Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-16-f28cdaa31700> in <module>()
      1 # Zero Division Answer
----> 2 1/0

```

{:.output_traceback_line}
```
ZeroDivisionError: division by zero
```




{:.input_area}
```python
# Syntax Answer
for el in [1, 2]
    print(el)
```



{:.output_traceback_line}
```
  File "<ipython-input-17-a830bc61fe3a>", line 2
    for el in [1, 2]
                    ^
SyntaxError: invalid syntax

```




{:.input_area}
```python
# Indentation Error
for el in [1, 2]:
print(el)
```



{:.output_traceback_line}
```
  File "<ipython-input-18-2a1f9b3e7199>", line 3
    print(el)
        ^
IndentationError: expected an indented block

```




{:.input_area}
```python
# Type error
(1, 2) + (2)
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
TypeError                                 Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-19-595b6eb4dcfc> in <module>()
      1 # Type error
----> 2 (1, 2) + (2)

```

{:.output_traceback_line}
```
TypeError: can only concatenate tuple (not "int") to tuple
```




{:.input_area}
```python
# Index Error
lst = [1, 2]
lst[2]
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
IndexError                                Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-20-3f3b0d0c5ac4> in <module>()
      1 # Index Error
      2 lst = [1, 2]
----> 3 lst[2]

```

{:.output_traceback_line}
```
IndexError: list index out of range
```




{:.input_area}
```python
# Key Error
my_dict = {'a': 1, 'b':2}
my_dict['c']
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
KeyError                                  Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-21-680eee3d9fac> in <module>()
      1 # Key Error
      2 my_dict = {'a': 1, 'b':2}
----> 3 my_dict['c']

```

{:.output_traceback_line}
```
KeyError: 'c'
```




{:.input_area}
```python
# Value Error
int('a')
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
ValueError                                Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-22-b8f9f0574b88> in <module>()
      1 # Value Error
----> 2 int('a')

```

{:.output_traceback_line}
```
ValueError: invalid literal for int() with base 10: 'a'
```




{:.input_area}
```python
# Name Error
a
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
NameError                                 Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-23-3756bd7ebda8> in <module>()
      1 # Name Error
----> 2 a

```

{:.output_traceback_line}
```
NameError: name 'a' is not defined
```


### Fixing Errors

For each of the following cells, try to debug the code to fix any errors, and get it running. 



{:.input_area}
```python
if True
    print('It worked')
# Answer: add a ':' to open the conditional code block
```



{:.output_traceback_line}
```
  File "<ipython-input-24-95a7c5ac0335>", line 1
    if True
           ^
SyntaxError: invalid syntax

```




{:.input_area}
```python
age_string = "My favourite number is " + 27
# Answer: typecase int to string, `+ str(27)`
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
TypeError                                 Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-25-631e1cbf3b94> in <module>()
----> 1 age_string = "My favourite number is " + 27
      2 # Answer: typecase int to string, `+ str(27)`

```

{:.output_traceback_line}
```
TypeError: can only concatenate str (not "int") to str
```




{:.input_area}
```python
my_list = [1, a, 24]
# Answer: assuming `a` was supposed to be a string, update to 'a'
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
NameError                                 Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-26-d3f7afd4a3bc> in <module>()
----> 1 my_list = [1, a, 24]
      2 # Answer: assuming `a` was supposed to be a string, update to 'a'

```

{:.output_traceback_line}
```
NameError: name 'a' is not defined
```




{:.input_area}
```python
my_list2 = ['1st', '2nd', '3rd', '4th', '5th']
print('Printing the 3rd element of my list ' + my_list2(2))
# Answer: wrong syntax to index, replace with '[]'
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
TypeError                                 Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-27-7884fb47db55> in <module>()
      1 my_list2 = ['1st', '2nd', '3rd', '4th', '5th']
----> 2 print('Printing the 3rd element of my list ' + my_list2(2))
      3 # Answer: wrong syntax to index, replace with '[]'

```

{:.output_traceback_line}
```
TypeError: 'list' object is not callable
```




{:.input_area}
```python
print('Three plus five equals' + str(3+5)
# Answer: Missing closing parenthesis - add ')' at the end
```



{:.output_traceback_line}
```
  File "<ipython-input-28-475bf438490d>", line 2
    # Answer: Missing closing parenthesis - add ')' at the end
                                                              ^
SyntaxError: unexpected EOF while parsing

```


## Part II: Debugging Challenges

### Debugging A Function

The following function has a series of issues with it. 

Work through debugging this function, fixing it up to be able to run with all the inputs below. 



{:.input_area}
```python
def my_function(input_1, input_2):
    """A long function that might error."""
    
    if len(input_1) > 1
        if input_1[0] = 0:
        answer = 0
    
    elif len(input_2) == 2:
        answer = input_2[1] / input_1[0]
        
    elif len(input_1) == len(input_2):
        answer = input_1[0] + input_2[0]
        
    print(answer)
```



{:.output_traceback_line}
```
  File "<ipython-input-29-e8d365c645be>", line 4
    if len(input_1) > 1
                       ^
SyntaxError: invalid syntax

```




{:.input_area}
```python
# ANSWER: Fixed version
def my_function(input_1, input_2):
    """A long function that might error."""
    
    if len(input_1) > 1:
        if input_1[0] == 0:
            answer = 0
    
    elif len(input_2) == 2:
        try:
            answer = input_2[1] / input_1[0]
        except ZeroDivisionError:
            answer = None
        
    elif len(input_1) == len(input_2):
        try:
            answer = input_1[0] + input_2[0]
        except TypeError:
            answer = None
        
    print(answer)
```




{:.input_area}
```python
my_function([0, 1], [0])
```


{:.output_stream}
```
0

```



{:.input_area}
```python
my_function([0], [0, 1])
```


{:.output_stream}
```
None

```



{:.input_area}
```python
my_function([1], [1])
```


{:.output_stream}
```
2

```



{:.input_area}
```python
my_function([1], ['1'])
```


{:.output_stream}
```
None

```

## Exploring Code

One of the great things about Python is how many tools, utilities and examples there are out there.

Let's start exploring what is available. GitHub is a website that people use to save and present code, below we have some notebooks that are hosted on GitHub showing the projects that they have made. Take time to look at one of the notebooks below that intrests you and read the explination as well as getting an understanding of what is being performed in each of the code cells. 

- https://anaconda.org/jbednar/census/notebook - Demographic data plotted out on maps of the US, showing differences in racial segregation/integration in different cities.
- https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks#linguistics-and-text-mining - Mining text to learn trends in bodies of text.
- https://anaconda.org/jbednar/nyc_taxi/notebook - NYC taxi data plotted out on cities of NYC
- https://www.fullstackpython.com/ - for advanced python user, next level guideline

<div class="alert alert-info">
Go and explore <a href="https://github.com">GitHub</a>, and search for some Python projects. And/or check out this list of interesting <a href="https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks">Jupyter Notebooks</a>. 
</div>

## Part III: Object Explorations



{:.input_area}
```python
# Import 
from datetime import date, time, datetime, timedelta
```


## Questions

- a) What day of the week was January 2nd, 1994
- b) What is the latest date the datetime object can store? What is the earliest?
    - Hint: explore using `dir` to see if you can find these values.
- c) What type of error is raised if you try to create a datetime object that is the 32nd day of any month?
- d) How many Mondays where there in February, 1916? 



{:.input_area}
```python
# YOUR CODE HERE
```




{:.input_area}
```python
# Answer for a
jan2nd = date(1994, 1, 2)
jan2nd.isoweekday()
```





{:.output_data_text}
```
7
```





{:.input_area}
```python
# Answer for b
print(date.max)
print(date.min)
```


{:.output_stream}
```
9999-12-31
0001-01-01

```



{:.input_area}
```python
# Answer for c
date(2001, 4, 32)
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
ValueError                                Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-38-d5119f14f5ae> in <module>()
      1 # Answer for c
----> 2 date(2001, 4, 32)

```

{:.output_traceback_line}
```
ValueError: day is out of range for month
```




{:.input_area}
```python
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
```


{:.output_stream}
```
Finished counting.
The number of Mondays is 4

```

**Now see if you can turn your answer to part d into a function.**

This function should be general such that it can calculate the number of times any day of the week occurs in a given month and year. 

To do this your function should take `year`, `month` and `day_of_the_week` as arguments.



{:.input_area}
```python
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
```




{:.input_area}
```python
# Check if your function works
count_days(1854, 3, 4)
```





{:.output_data_text}
```
5
```



## Datetime Manipulations

Using `datetime` objects there are several operations and methods we can use that are useful, some of these are shown as examples below.



{:.input_area}
```python
# Get current times
now = datetime.now()
```




{:.input_area}
```python
# Create a time delta object
delta = timedelta(days=1, minutes=7, seconds=37)
```




{:.input_area}
```python
# Add a time
later = now + delta
```




{:.input_area}
```python
# Check out what time it will be after 
#   Note - format is 'YEAR-MONTH-DAY'T'HOUR:MINUTE:SECOND:MICROSECOND'
later.isoformat()
```





{:.output_data_text}
```
'2020-07-24T06:00:58.781302'
```



### DateTime Manipulation Questions

- a) What day of the week it will be 4675 days from now?
- b) Write a boolean if/else stement that checks whether `date_1` is earlier or later than `date_2`, and prints out 'earlier' or 'later' appropriately.



{:.input_area}
```python
# YOUR CODE HERE
```




{:.input_area}
```python
# Answer for a
(now+timedelta(days=4657)).isoweekday()
```





{:.output_data_text}
```
6
```





{:.input_area}
```python
# Answer for b
if date_1 < date_2:
    print('Earlier')
else:
    print('Later')
```


### DateTime Manipulation Exploration

If you start from Jan 1st, 1757, and repeatedly add 8 days, until you hit 1800, how many times will it be a Monday?



{:.input_area}
```python
# YOUR CODE HERE
check_date = date(1799, 1, 1)

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
```


{:.output_stream}
```
There were 6 mondays.

```

#### Make a function

Once you have answered this question, convert your code into a generalized function. 

This function, call it `count_weekdays` should take:
- `start_date`: a start date (a datetime object)
- `add_days`: a number of days to add (an int)
- `stop_year`: a stop year (an int)
- `weekday`: a day to count, represented in isoweekday format (an int)

It should return the number of `weekday`'s that occur from the start date, until stop year, when adding `add_days` days.



{:.input_area}
```python
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
```




{:.input_area}
```python
# Check that the function returns the expected result for an example case
assert count_weekdays(datetime(1322, 6, 17), 3, 1324, 5) == 27
```


## Part IV: Objects Questions

## Example Class



{:.input_area}
```python
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
```




{:.input_area}
```python
# Create an instance of our class
python = Language('python', 'computer', 'lots of')
python.print_goodness_level()
```


{:.output_stream}
```
The language python has lots of goodness.

```



{:.input_area}
```python
# Create another instance of our class
english = Language('english', 'human', 'some')
english.print_goodness_level()
```


{:.output_stream}
```
The language english has some goodness.

```

### TritonCourse class

Let’s create a class to represent courses at UCSD! 

#### Class Definition

Write a class to store information about UCSD courses, called `TritonCourse`. 

This course assumes all courses belong to a department, have a course code, and have a title.

That is, write a class called `TritonCourse` that has instance attributes `department` (string), `code` (int), and `title` (string). 



{:.input_area}
```python
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
```


#### Instances

Once you've written the class defintion above, you should be able to run the following code to create an instance of this class. 

You can then print out the attributes and check that they hold the values that you expect. 



{:.input_area}
```python
# Define an instance of our class
cogs18 = TritonCourse("COGS", 18, "Introduction to Python")
```




{:.input_area}
```python
# Check the instance attributes
print(cogs18.department)
print(cogs18.code)
print(cogs18.title)
```


{:.output_stream}
```
COGS
18
Introduction to Python

```

Now, create some more instances of our class:

- ECE 15, "Engineering Programming" 
    - Save the result to a variable called `class1`
- MUS 8, "American Music: Jazz Culture"
    - Save the result to a variable called `class2`



{:.input_area}
```python
class1  = TritonCourse("ECE",15,"Engineering Programming")
class2 = TritonCourse("MUS", 8, "American Music: Jazz Culture")
```


#### Methods

Now, make a new version of `TritonCourse` that has a method. 

Specifically, this method, called `print_info` should print out the information about the course as:

    'department name code : title'
    
So, for example, once you add this method, using the method on our `cogs18` instance should print out:

    COGS 18 : Introduction to Python



{:.input_area}
```python
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
```




{:.input_area}
```python
# Check the method works on our cogs18 instance
cogs18 = TritonCourse("COGS", 18, "Introduction to Python")
cogs18.print_info()
```


{:.output_stream}
```
COGS18: Introduction to Python

```

## Part V: Objects Explorations

- What kind of other attributes and methods might we want on our `TritonCourse` object?
    - Make an extended version of `TritonCourse` with at least one extra class attribute, instance attribute and method. 
- Create a brand new class, to do something new / different!
    - Make sure it has at least one class attribute, instance attribute, and some methods
    - Create at least one methods that takes in an argument (doesn't just use class & instance attributes)
    - Create at least one method that has a conditional in it, one with a loop, and one with a try/except



{:.input_area}
```python
# answers would vary here

```


## The End!

This is the end of this Coding Lab!

Be sure you've made a concerted effort to complete all the tasks specified in this lab. Then, go ahead and submit on datahub!
