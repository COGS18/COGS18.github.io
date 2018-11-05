---
download_link: assets/downloads/materials/13-Objects.ipynb.zip
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

# Objects

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
date_string = '21/07/1997'
```




{:.input_area}
```python
# A date, stored as a list of number
date_list = ['21', '07', '1997']
```




{:.input_area}
```python
# A date, stored as a series of numbers
day = 21
month = 7
year = 1997
```




{:.input_area}
```python
# A date, stored as a string
date_dictionary = {'day': 21, 'month': 7, 'year': 1997}
```


## Objects

<div class="alert alert-success">
Objects are an organization of data (called attributes), with associated code to operate on that data (functions defined on the objects, called methods).
</div>

### Example Object: Date



{:.input_area}
```python
# Import a date object
from datetime import date
```




{:.input_area}
```python
# Set the data we want to store in our date object
day = 21
month = 7
year = 1997

# Create a date object
my_date = date(year, month, day)
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



{:.input_area}
```python
# Get the day attribute
my_date.day
```





{:.output_data_text}
```
21
```





{:.input_area}
```python
# Get the month attribute
my_date.month
```





{:.output_data_text}
```
7
```





{:.input_area}
```python
# Get the year attribute
my_date.year
```





{:.output_data_text}
```
1997
```



### Date - Methods



{:.input_area}
```python
my_date.weekday?
```




{:.input_area}
```python
# Method to return what day of the week the date is
my_date.weekday()
```





{:.output_data_text}
```
0
```





{:.input_area}
```python
# Reminder: check documentation with '?'
my_date.weekday?
```




{:.input_area}
```python
# Get the ISO format representation of the date (as a sting)
my_date.isoformat( )
```





{:.output_data_text}
```
'1997-07-21'
```



### Listing Attributes & Methods With `dir`



{:.input_area}
```python
dir(my_date)
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

### Objects Example: DateTime



{:.input_area}
```python
from datetime import datetime
```




{:.input_area}
```python
# Get the current date & time
now = datetime.today()

print(now) 
```


{:.output_stream}
```
2018-10-29 10:31:18.212411

```



{:.input_area}
```python
# Attributes
print(now.year)
print(now.day)
```


{:.output_stream}
```
2018
29

```



{:.input_area}
```python
# Methods
print(now.weekday())
```


{:.output_stream}
```
0

```
