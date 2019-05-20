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
  url: /materials/14-Classes
  title: '14-Classes'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

## Course Announcements

- Exam next Friday in class (5/10)
- A4 due Mon 5/13 (11:59 PM)

- Extra office hours this week and next (for assignment and/or extra midterm help):
    - **When**: Wed 5/1 (that's today!) and Wed 5/8 ; 11AM - 1PM
    - **Where**: 1st floor of CSE (Computer Science and Engineering Building)
    - **Who**: Edward and Miranda
    
    
    
- All other normal office hours still occurring:
    - Myles - Mon 5-6 PM (Sun God Lounge)
    - Charles - Wed 1-2 PM CSE Basement Benches - Far End)
    - Professor Ellis - Fri 3-5 PM (CSB 243)
    - Shreenivas - Fri 6-7 PM (CSB 114)


Check-In

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

my_number = 13.3; my_string = "word"

check_data(my_string, my_number)
```





{:.output_data_text}
```
'A2'
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


{:.output_stream}
```
['Mercury', 'Venus', 'Earth', 'Mars', 'Jupyter', 'Saturn', 'Uranus', 'Neptune']

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


{:.output_stream}
```
Third Rock From The Sun

```

- A) Third Rock From The Sun
- B) third rock from the sun
- C) Third rock from the sun
- D) thirdrockfromthesun 
- E) ¯\\\_(ツ)\_/¯

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



### Clicker Question #2

Given the code below:



{:.input_area}
```python
my_date = date(year=1050, month=12, day=12)
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


{:.output_stream}
```
2019-05-01 09:34:41.436294

```



{:.input_area}
```python
# Check some attributes of the object
print(now.year)
print(now.day)
```


{:.output_stream}
```
2019
1

```



{:.input_area}
```python
# Check a method of the object
print(now.weekday())
```


{:.output_stream}
```
2

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

## Classes

<div class="alert alert-success">
'Classes' define objects. The 'class' keyword opens a code block for instructions on how to create objects of a particular type.
</div>

Think of classes as the _blueprint_ for creating and defining objects and their properties (methods, attributes, etc.)

## Example Class: Dog



{:.input_area}
```python
# Define a class with `class`. 
# By convention, class definitions use CamelCase
class Dog():
    
    # Class attributes for objects of type Dog
    sound = 'Woof'
    
    # Class methods for objects of type Dog
    def speak(self):
        print(self.sound)
```




{:.input_area}
```python
# Initialize a dog object
george = Dog()
```




{:.input_area}
```python
# george, has 'Dog' attribute(s)
print(george.sound)
```


{:.output_stream}
```
Woof

```



{:.input_area}
```python
# george, has 'Dog' method(s)
# remember we used `self`
george.speak()
```


{:.output_stream}
```
Woof

```



{:.input_area}
```python
## see underlying code for date class
date??
```

