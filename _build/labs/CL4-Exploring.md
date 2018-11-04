---
download_link: assets/downloads/labs/CL4-Exploring.ipynb.zip
layout: notebooks
title: 'CL4-Exploring'
prev_page:
  url: /labs/CL3B-Answers
  title: 'CL3B-Answers'
next_page:
  url: /labs/CL4B-Answers
  title: 'CL4B-Answers'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# CL4: Reading Code

Welcome to the fourth coding lab!

In this CodingLab we will be thinking and working on debugging & objects. 

We will also start thinking about exploring all of the Python resources and tools that are available, with an eye towards starting to think about the projects.

## Debugging Questions

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
# YOUR CODE HERE
```


### Fixing Errors

For each of the following cells, try to debug the code to fix any errors, and get it running. 



{:.input_area}
```python
if True
    print('It worked')
```




{:.input_area}
```python
age_string = "My favourite number is " + 27
```




{:.input_area}
```python
my_list = [1, a, 24]
```




{:.input_area}
```python
my_list2 = ['1st', '2nd', '3rd', '4th', '5th']
print('Printing the 3rd element of my list ' + my_list2(2))
```




{:.input_area}
```python
print('Three plus five equals' + str(3+5)
```


## Debugging Challenges

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




{:.input_area}
```python
my_function([0, 1], [0])
```




{:.input_area}
```python
my_function([0], [0, 1])
```




{:.input_area}
```python
my_function([1], [1])
```




{:.input_area}
```python
my_function([1], ['1'])
```


## Object Explorations



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


** Now see if you can turn your answer to part d into a function.**

This function should be general such that it can calculate the number of times any day of the week occurs in a given month and year. 

To do this your function should take `year`, `month` and `day_of_the_week` as arguments.



{:.input_area}
```python
# YOUR CODE HERE

```




{:.input_area}
```python
# Check if your function works
count_days(1854, 3, 4)
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


### DateTime Manipulation Questions

- a) What day of the week it will be 4675 days from now?
- b) Write a boolean if/else stement that checks whether `date_1` is earlier or later than `date_2`, and prints out 'earlier' or 'later' appropriately.



{:.input_area}
```python
# YOUR CODE HERE
```


### DateTime Manipulation Exploration

If you start from Jan 1st, 1757, and repeatedly add 8 days, until you hit 1800, how many times will it be a Monday?



{:.input_area}
```python
# YOUR CODE HERE

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

```




{:.input_area}
```python
# Check that the function returns the expected result for an example case
assert count_weekdays(datetime(1322, 6, 17), 3, 1324, 5) == 27
```


## Exploring Code

One of the great things about Python is how many tools, utilities and examples there are out there.

Let's start exploring what is available:

GitHub is a website that people use to save and present code. Below we have listed some some notebooks that are hosted on GitHub showing some particular projects, as well as a link to Github in general, and a curated list of interesting Jupyter notebooks. 

Take time to look at at least one of the notebooks mentioned below. See if you can get, to a first approximation, a sense of what the notebook is doing, and how the Python code does it. 

Also go and search through Github and/or the list of notebooks, to see if you can find some code projects that interest you. See if you can get any ideas for things that you could do in your project for this class. 

Don't worry if you don't understand all the code you see - this is just a start, to see what is out there, and you will understand more and more of it as we go along. 

- https://anaconda.org/jbednar/census/notebook - Demographic data plotted out on maps of the US, showing differences in racial segregation/integration in different cities.
- https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks#linguistics-and-text-mining - Mining text to learn trends in bodies of text.
- https://anaconda.org/jbednar/nyc_taxi/notebook - NYC taxi data plotted out on cities of NYC
- https://www.fullstackpython.com/ - for advanced python user, next level guideline

<div class="alert alert-info">
Go and explore [Github](https://github.com), and search for some Python projects. And/or check out this list of interesting [Jupyter notebooks](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks). 
</div>
