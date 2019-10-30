---
interact_link: content/materials/13-Objects.ipynb
download_link: assets/downloads/13-Objects.ipynb.zip
pdf_link: assets/pdf/13-Objects.pdf
layout: materials
title: '13-Objects'
prev_page:
  url: /materials/12-Debugging
  title: '12-Debugging'
next_page:
  url: /materials/A1-Syntax
  title: 'A1-Syntax'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

## Course Announcements

- A3 due Friday (11:59 PM)
- Exam will be available in CodingLab today
    - You *can* take pictures of it
    - You *cannot* take the original with you

### Review Question #1

What will the following code snippet print out:



{:.input_area}
```python
def check_data(word, number):

    if not word.islower():
        answer = 'A1'
    elif number.is_integer() or word.isalpha():
        answer = 'A2'
    else:
        answer = 'A3'
        
    return answer

my_number = 13.3
my_string = "word"

check_data(my_string, my_number)
```


- A) 'A1'
- B) 'A2' 
- C) 'A3' 
- D) 'A1, A2' 
- E) None



{:.input_area}
```python
# a reminder to find out information about 
# methods you're less familiar with
str.isalpha?
```


### Review Question #2

What would the following code return?



{:.input_area}
```python
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupyter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
planets.remove('Pluto') 
print(planets)
```


- A) the original list - we didn't store the output of `planets.remove()`
- B) the original list, but without 'Pluto'
- C) both the original list and the list without 'Pluto'
- D)  ¯\\\_(ツ)\_/¯

### Review Question #3

What would the following code return?



{:.input_area}
```python
home = 'Third Rock From The Sun'
home.lower() 
print(home)
```


- A) Third Rock From The Sun
- B) third rock from the sun
- C) Third rock from the sun
- D) thirdrockfromthesun 
- E) ¯\\\_(ツ)\_/¯

## Exam Review

- [Blank Exam #1](https://cogs18.github.io/assets/intro/exams/E1_Fa19.pdf)
- [Exam #1 Answers](https://cogs18.github.io/assets/intro/exams/E1_Fa19_answer.pdf)
- [Exam #1 Code](https://cogs18.github.io/materials/E1-Answers)

# Objects

- `date` & `datetime`
- methods & attributes

### Clicker Question #1

What would be the best way to store a date?

- A) A string
- B) A list of numbers
- C) It can't be done
- D) A dictionary
- E) Something else

### Storing Dates



{:.input_area}
```python
# A date, stored as a string
date_string = '29/09/1988'
print(date_string)
```




{:.input_area}
```python
# A date, stored as a list of number
date_list = ['29', '09', '1988']
date_list
```




{:.input_area}
```python
# A date, stored as a series of numbers
day = 29
month = 9
year = 1988

print(day)
```




{:.input_area}
```python
# A date, stored as a dictionary
date_dictionary = {'day': 29, 'month': 9, 'year': 1988}
date_dictionary
```


## Objects

<div class="alert alert-success">
Objects are an organization of data (called attributes), with associated code to operate on that data (functions defined on the objects, called methods).
</div>

Ways to organize data (variables) and functions together. 

### Example Object: Date



{:.input_area}
```python
# Import a date object
from datetime import date
```




{:.input_area}
```python
date?
```




{:.input_area}
```python
# Set the data we want to store in our date object
day = 29
month = 9
year = 1988

# Create a date object
my_date = date(year, month, day)
print(my_date)
```




{:.input_area}
```python
# Check what type of thing `my_date` is
type(my_date)
```


## Accessing Attributes & Methods

<div class="alert alert-success">
Attributes and methods are accessed with a '.', followed by the attribute/method name on the object. 
</div>

### Date - Attributes

Attributes look up & return information about the object.

**attributes** maintain the object's state, simply returning information about the object to you



{:.input_area}
```python
# Get the day attribute
my_date.day
```




{:.input_area}
```python
# Get the month attribute
my_date.month
```




{:.input_area}
```python
# Get the year attribute
my_date.year
```


### Date - Methods

These are _functions_ that *belong* to and operate on the object directly.

**methods** modify the object's state



{:.input_area}
```python
# Method to return what day of the week the date is
my_date.weekday()
```




{:.input_area}
```python
# Reminder: check documentation with '?'
date.weekday?
```




{:.input_area}
```python
# Get the ISO format representation of the date (as a string)
my_date.isoformat()
```




{:.input_area}
```python
# operates on date object
# returns a string
type(my_date.isoformat())
```


It's also possible to carry out operations on multiple date objects.



{:.input_area}
```python
# define a second date
my_date2 = date(1980, 7, 29)
print(my_date, my_date2)
```




{:.input_area}
```python
# calculate the difference between times
time_diff = my_date - my_date2
print(time_diff.days,  "days") #in days
print(time_diff.days/365,"years") #in years
```


### Listing Attributes & Methods : `dir`



{:.input_area}
```python
# tab complete to access
# methods and attributes
my_date.
```




{:.input_area}
```python
## dir ouputs all methods and attributes
## we'll talk about the double underscores next lecture
dir(my_date)
```


### Clicker Question #2

Given the code below:



{:.input_area}
```python
my_date = date(year = 1050, month = 12, day = 12)
```


Which is the best description:
- A) `my_date` is an object, with methods that store data, and attributes that store procedures
- B) `my_date` is variable, and can be used with functions
- C) `my_date` is an attribute, with methods attached to it
- D) `my_date` is a method, and also has attributes
- E) `my_date` is an object, with attributes that store data, and methods that store procedures

### Clicker Question #3

For an object `lets` with a method `do_something`, how would you execute that method?

- A) `do_something(lets)`
- B) `lets.do_something`
- C) `lets.do_something()`
- D) lets.do.something()
- E) ¯\\\_(ツ)\_/¯

### Clicker Question #4

For an object `lets` with an attribute `name`, how would you return the information stored in `name` for the object `lets`?

- A) `name(lets)`
- B) `lets.name`
- C) `lets.name()`
- D) lets.get.name()
- E) ¯\\\_(ツ)\_/¯

### Objects Example: DateTime



{:.input_area}
```python
from datetime import datetime
```




{:.input_area}
```python
# get documentation
datetime?
```




{:.input_area}
```python
# Get the current date & time
now = datetime.today()

print(now) 
```




{:.input_area}
```python
# Check some attributes of the object
print(now.year)
print(now.day)
```




{:.input_area}
```python
# Check a method of the object
print(now.weekday())
```


### Objects Summary

- Objects allow for data (attributes) and functions (methods) to be organized together
    - methods operate on the object type (modify state)
    - attributes store and return information (data) about the object (maintain state)
- `dir()` returns methods & attrbutes for an object
- Syntax:
    - `obj.method()`
    - `obj.attribute`
- `date` and `datetime` are two types of objects in Python
