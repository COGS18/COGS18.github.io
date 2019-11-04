---
interact_link: content/labs/CL5B-Answers.ipynb
download_link: assets/downloads/CL5B-Answers.ipynb.zip
layout: notebooks
title: 'CL5B-Answers'
prev_page:
  url: /labs/CL5-Debugging
  title: 'CL5-Debugging'
next_page:
  url: /labs/CL6-Classes
  title: 'CL6-Classes'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# CL4: Reading Code

Welcome to the fourth coding lab!

In this CodingLab we will be thinking and working on debugging & objects. 

We will also start thinking about exploring all of the Python resources and tools that are available, with an eye towards starting to think about the projects.

ANSWERS: There may be many valid answers to the questions in this coding lab, so it's fine if your answers differ to those provided here, if they have the right output. 

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
<ipython-input-3-bb3d282f11da> in <module>()
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
  File "<ipython-input-4-625533441b23>", line 1
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
  File "<ipython-input-5-6369af162a3e>", line 2
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
<ipython-input-11-9343b3b5f280> in <module>()
      1 #
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
<ipython-input-6-30dc726de1d4> in <module>()
      1 lst = [1, 2]
----> 2 lst[2]

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
<ipython-input-8-295af53e266f> in <module>()
      1 my_dict = {'a': 1, 'b':2}
----> 2 my_dict['c']

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
<ipython-input-13-b67a141da135> in <module>()
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
<ipython-input-14-9c0d71849fd4> in <module>()
      1 #
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
  File "<ipython-input-122-109b4889dbec>", line 1
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
<ipython-input-121-4fb094c5d994> in <module>()
----> 1 age_string = "My favourite number is " + 27

```

{:.output_traceback_line}
```
TypeError: must be str, not int
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
<ipython-input-1-fe84cb26012f> in <module>
----> 1 my_list = [1, a, 24]

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
<ipython-input-3-b7acbbea7bc3> in <module>
      1 my_list2 = ['1st', '2nd', '3rd', '4th', '5th']
----> 2 print('Printing the 3rd element of my list ' + my_list2(2))

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
  File "<ipython-input-1-82866694322c>", line 1
    print('Three plus five equals' + str(3+5)
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
  File "<ipython-input-2-103c9b89a124>", line 4
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




{:.input_area}
```python
# Answer for b
print(date.max)
print(date.min)
```




{:.input_area}
```python
# Answer for c
date(2001, 4, 32)
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
# Create a time delta object, to represent a 
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
'2018-10-30T09:38:00.355841'
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
3
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


## Exploring Code

One of the great things about Python is how many tools, utilities and examples there are out there.

Let's start exploring what is available. GitHub is a website that people use to save and present code, below we have some notebooks that are hosted on GitHub showing the projects that they have made. Take time to look at one of the notebooks below that intrests you and read the explination as well as getting an understanding of what is being performed in each of the code cells. 

- https://anaconda.org/jbednar/census/notebook - Demographic data plotted out on maps of the US, showing differences in racial segregation/integration in different cities.
- https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks#linguistics-and-text-mining - Mining text to learn trends in bodies of text.
- https://anaconda.org/jbednar/nyc_taxi/notebook - NYC taxi data plotted out on cities of NYC
- https://www.fullstackpython.com/ - for advanced python user, next level guideline

<div class="alert alert-info">
Go and explore [Github](https://github.com), and search for some Python projects. And/or check out this list of interesting [Jupyter notebooks](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks). 
</div>
