---
interact_link: content/materials/13-Objects.ipynb
download_link: assets/downloads/13-Objects.ipynb.zip
pdf_link: assets/pdf/13-Objects.pdf
layout: materials
title: '13-Objects'
prev_page:
  url: /materials/12-Algorithms
  title: '12-Algorithms'
next_page:
  url: /materials/14-Classes
  title: '14-Classes'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
## Course Announcements

- A3 due tonight (11:59 PM)
- Coding Lab 6 due Wednesday
- Exams (& A4) will be released later today

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



{:.input_area}
```python
# A date, stored as a string
date_string = '29/09/1988'
print(date_string)
```


{:.output_stream}
```
29/09/1988

```



{:.input_area}
```python
# A date, stored as a list of number
date_list = ['29', '09', '1988']
date_list
```





{:.output_data_text}
```
['29', '09', '1988']
```





{:.input_area}
```python
# A date, stored as a series of numbers
day = 29
month = 9
year = 1988

print(day)
```


{:.output_stream}
```
29

```



{:.input_area}
```python
# A date, stored as a dictionary
date_dictionary = {'day': 29, 'month': 9, 'year': 1988}
date_dictionary
```





{:.output_data_text}
```
{'day': 29, 'month': 9, 'year': 1988}
```



## Objects

<div class="alert alert-success">
Objects are an organization of data (called <b>attributes</b>), with associated code to operate on that data (functions defined on the objects, called <b>methods</b>).
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


{:.output_stream}
```
1988-09-29

```



{:.input_area}
```python
# Check what type of thing `my_date` is
type(my_date) 
```





{:.output_data_text}
```
datetime.date
```



## Accessing Attributes & Methods

<div class="alert alert-success">
Attributes and methods are accessed with a <code>.</code>, followed by the attribute/method name on the object. 
</div>

### Date - Attributes

Attributes look up & return information about the object.

**attributes** maintain the object's state, simply returning information about the object to you



{:.input_area}
```python
# Get the day attribute
my_date.day
```





{:.output_data_text}
```
29
```





{:.input_area}
```python
# Get the month attribute
my_date.month
```





{:.output_data_text}
```
9
```





{:.input_area}
```python
# Get the year attribute
my_date.year
```





{:.output_data_text}
```
1988
```



### Date - Methods

These are _functions_ that *belong* to and operate on the object directly.

**methods** modify the object's state



{:.input_area}
```python
# Method to return what day of the week the date is
my_date.weekday()
```





{:.output_data_text}
```
3
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





{:.output_data_text}
```
'1988-09-29'
```





{:.input_area}
```python
# operates on date object
# returns a string
type(my_date.isoformat())
```





{:.output_data_text}
```
str
```



It's also possible to carry out operations on multiple date objects.



{:.input_area}
```python
# define a second date
my_date2 = date(1980, 7, 29)
print(my_date, my_date2)
```


{:.output_stream}
```
1988-09-29 1980-07-29

```



{:.input_area}
```python
# calculate the difference between times
time_diff = my_date - my_date2
print(time_diff.days,  "days") #in days
print(time_diff.days/365,"years") #in years
```


{:.output_stream}
```
2984 days
8.175342465753424 years

```

### Listing Attributes & Methods : `dir`



{:.input_area}
```python
# tab complete to access
# methods and attributes
my_date.

# works to find attributes and methods
# for date type objects generally
date.
```




{:.input_area}
```python
## dir ouputs all methods and attributes
## we'll talk about the double underscores next lecture
dir(my_date)
```





{:.output_data_text}
```
['__add__',
 '__class__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__ne__',
 '__new__',
 '__radd__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rsub__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__sub__',
 '__subclasshook__',
 'ctime',
 'day',
 'fromisoformat',
 'fromordinal',
 'fromtimestamp',
 'isocalendar',
 'isoformat',
 'isoweekday',
 'max',
 'min',
 'month',
 'replace',
 'resolution',
 'strftime',
 'timetuple',
 'today',
 'toordinal',
 'weekday',
 'year']
```



#### Clicker Question #2

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


{:.output_stream}
```
2020-05-04 08:28:31.305005

```



{:.input_area}
```python
# Check some attributes of the object
print(now.year)
print(now.day)
```


{:.output_stream}
```
2020
4

```



{:.input_area}
```python
# Check a method of the object
print(now.weekday())
```


{:.output_stream}
```
0

```

### Objects Summary

- Objects allow for data (attributes) and functions (methods) to be organized together
    - methods operate on the object type (modify state)
    - attributes store and return information (data) about the object (maintain state)
- `dir()` returns methods & attributes for an object
- Syntax:
    - `obj.method()`
    - `obj.attribute`
- `date` and `datetime` are two types of objects in Python