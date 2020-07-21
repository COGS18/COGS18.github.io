---
interact_link: content/materials/11-Classes.ipynb
download_link: assets/downloads/11-Classes.ipynb.zip
pdf_link: assets/pdf/11-Classes.pdf
layout: materials
title: '11-Classes'
prev_page:
  url: /materials/10-Testing-Debugging
  title: '10-Testing-Debugging'
next_page:
  url: /materials/12-Namespaces
  title: '12-Namespaces'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
## Course Announcements

**Due Dates**:
- A3 due tonight
- CL4 due Wednesday
- E2 on Thursday

**Updates**:
- E1 Scores on Canvas & Feedback on datahub
- A2 & CL3 scores will be on Canvas later today (E1 & CL3 Answers on course website)
- Prof Ellis OH: Wed 4-6 PM (this week only)

# Objects & Classes

- `date` & `datetime`
- methods & attributes
- `class`
    - attributes
    - methods
- instances
    - `__init__`
- objects

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
2020-07-20 11:37:58.461295

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
20

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

## Classes

<div class="alert alert-success">
<b>Classes</b> define objects. The <code>class</code> keyword opens a code block for instructions on how to create objects of a particular type.
</div>

Think of classes as the _blueprint_ for creating and defining objects and their properties (methods, attributes, etc.). They keep related things together and organized.

## Example Class: Dog



{:.input_area}
```python
# Define a class with `class`. 
# By convention, class definitions use CapWords (Pascal)
class Dog():
    
    # Class attributes for objects of type Dog
    sound = 'Woof'
    
    # Class methods for objects of type Dog
    def speak(self):
        print(self.sound)
```


A reminder:
- **attributes** maintain the object's state; they lookup information about an object
- **methods** alter the object's state; they run a function on an object

**`class`** notes:

- classes tend to use **CapWords** convention (Pascal Case)
    - instead of snake_case (functions and variable names)
- `()` after `Dog` indicate that this is callable
    - like functions, Classes must be executed before they take effect
- can define **attributes** & **methods** within `class`
- `self` is a special parameter for use by an object
    - refers to the thing (object) itself
- like functions, a new namespace is created within a Class




{:.input_area}
```python
# Initialize a dog object
george = Dog()
```




{:.input_area}
```python
# george, has 'sound' attribute(s) from Dog()
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

#### Clicker Question #1

Which of the following statements is true about the example we've been using? 



{:.input_area}
```python
class Dog():
    
    sound = 'Woof'
    
    def speak(self):
        print(self.sound)
```


- A) `Dog` is a Class, `sound` is an attribute, and `speak` is a method. 
- B) `Dog` is a function, `sound` is an attribute, and `speak` is a method. 
- C) `Dog` is a Class, `sound` is a method, and `speak` is an attribute. 
- D) `Dog` is a function, `sound` is an method, and `speak` is an attribute. 

### Using our Dog Objects



{:.input_area}
```python
# Initialize a group of dogs
pack_of_dogs = [Dog(), Dog(), Dog(), Dog()]
```




{:.input_area}
```python
# take a look at this
pack_of_dogs
```





{:.output_data_text}
```
[<__main__.Dog at 0x107c4b9e8>,
 <__main__.Dog at 0x107c4bdd8>,
 <__main__.Dog at 0x107c4bd30>,
 <__main__.Dog at 0x107c4b358>]
```





{:.input_area}
```python
# take a look at this
type(pack_of_dogs[0])
```





{:.output_data_text}
```
__main__.Dog
```





{:.input_area}
```python
for dog in pack_of_dogs:
    dog.speak()
```


{:.output_stream}
```
Woof
Woof
Woof
Woof

```

## Instances & self

<div class="alert alert-success">
An <b>instance</b> is particular instantiation of a class object. <code>self</code> refers to the current instance. 
</div>



{:.input_area}
```python
# Initialize a dog object
george = Dog()
```


From our example above:

- Dog is the Class we created
- `george` was an _instance_ of that class
- self just refers to whatever the _current_ instance is

#### Clicker Question #6

How many instances of `Dog()` are created below and how many times does the `speak()` method execute?



{:.input_area}
```python
pack_of_dogs = [Dog(), Dog(), Dog(), Dog()]

counter = 1

for doggie in pack_of_dogs:
    if counter <= 2:
        doggie.speak()
        counter += 1
    else:
        break
```


{:.output_stream}
```
Woof
Woof

```

- A) 2 instances, 2 method executions
- B) 2 instances, 4 method executions
- C) 4 instances, 2 method executions
- D) 4 instances, 4 method executions
- E) ¯\\\_(ツ)\_/¯

## Instance Attributes

An instance attribute specific to the instance we're on.

<div class="alert alert-success">
Instance attributes are attributes that we can make be different for each instance of a class. <code>__init__</code> is a special method used to define instance attributes. 
</div>

## Example Class: Dog Revisited

- Two trailing underscores is used to indicate something Python recognizes and knows what to do every time it sees it.
- Here, we use `__init__` to execute the code within it every time you initialize an object.



{:.input_area}
```python
class Dog():
    
    # Class attributes for Dogs
    sound = 'Woof'
    
    # Initializer, allows us to specify instance-specific attributes
    # leading and trailing double underscores indicates that this is special to Python
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.sound)
```




{:.input_area}
```python
# Initialize a dog
# what goes in the parentheses is defined in the __init__
gary = Dog(name = 'Gary') 
```




{:.input_area}
```python
# Check gary's attributes
print(gary.sound)    # This is an class attribute
print(gary.name)     # This is a instance attribute
```


{:.output_stream}
```
Woof
Gary

```



{:.input_area}
```python
# Check gary's methods
gary.speak()
```


{:.output_stream}
```
Woof

```

#### Clicker Question #7

Edit the code we've been using for the Class `Dog` to include information about the breed of the Class Dog?



{:.input_area}
```python
# EDIT CODE HERE
class Dog():
    
    # Class attributes for Dogs
    sound = 'Woof'
    
    # Initializer, allows us to specify instance specific attributes
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def speak(self):
        print(self.sound)
```




{:.input_area}
```python
## Test it out here
lexi = Dog(name='Lexi', breed='Italian Greyhound')
lexi.breed
```





{:.output_data_text}
```
'Italian Greyhound'
```



- A) I did it!
- B) I think I did it!
- C) So lost. -_-

## Class example: Cat



{:.input_area}
```python
# Define a class 'Cat'
class Cat():
    
    sound = "Meow"
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def speak(self):
        print(self.sound)
```


## Instances Examples



{:.input_area}
```python
# Define some instances of our objects
pets = [Cat('Jaspurr', 'Balinese'), Dog('Barkley', 'Corgi'), 
        Cat('Picatso', 'Birman'), Dog('Ruffius', 'Italian Greyhound')]
```




{:.input_area}
```python
for pet in pets:
    print(pet.name, '(', pet.breed , ') says:')
    pet.speak()
```


{:.output_stream}
```
Jaspurr ( Balinese ) says:
Barkley ( Corgi ) says:
Woof
Picatso ( Birman ) says:
Ruffius ( Italian Greyhound ) says:
Woof

```

#### Clicker Question #8

What will the following code snippet print out?



{:.input_area}
```python
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
```




{:.input_area}
```python
student = MyClass('Rob', 'rob@python.com', 62)
student.check_score()
```


- A) True
- B) 'Rob'
- C) False 
- D) 'rob@python.com'
- E) None

## Class Inheritance

<div class="alert alert-success">
Objects can also be built from other objects, inheriting their properties and building off them.
</div>

If you have a hierarchical structure, this can be very helpful.

For our `Dog()` and `Cat()` example, you may on some more general `Animal()` class. 

You would want `Animal()` to inherit all the 'stuff' from the other classes.



{:.input_area}
```python
class Tool():
    
    def __init__(self):       
        self.is_tool = True
        self.tool_type = None
    
    def use_tool(self):
        print('Using tool.')

class Hammer(Tool): #inherit Tool class
    
    def __init__(self):        
        super().__init__() # inherit initialization from Tool()
        self.tool_type = 'Hammer'
        self.why = 'To hammer things.'
```




{:.input_area}
```python
my_tool = Tool()
my_hammer = Hammer()
print(my_hammer.is_tool)
print(my_hammer.why)
my_hammer.use_tool()
```


#### Clicker Question #9

Given the following set of classes:



{:.input_area}
```python
class Brain(): 
    
    def __init__(self, size = None, folded = None):
        self.size = size
        self.folded = folded
        
    def print_info(self):
        folded_string = ''
        if not self.folded:
            folded_string = 'not'
        print('This brain is ' + self.size + ' and is ' + folded_string + ' folded.')
         
class SheepBrain(Brain):
    
    def __init__(self, size = 'medium', folded = False):
        super().__init__(size, folded)
```


What will the following print out?



{:.input_area}
```python
sheep = SheepBrain()
sheep.print_info()
```


- A) This brain is medium and folded.
- B) This brain is large and folded.
- C) This brain is medium and not folded.
- D) This brain is medium and False.
- E) ¯\\\_(ツ)\_/¯

#### Clicker Question #10

Given the following set of classes:



{:.input_area}
```python
class Brain(): 
        
    def __init__(self, size=None, folded=None):
        self.size = size
        self.folded = folded
        
    def print_info(self):
        folded_string = ''
        if not self.folded:
            folded_string = 'not'
        print('This brain is ' + self.size + ' and is ' + folded_string + ' folded.')
        
class SheepBrain(Brain):
    
    def __init__(self, size = 'medium', folded = False):
        super().__init__(size, folded)
        
class HumanBrain(Brain):
    def __init__(self, size = 'large', folded = True):
        super().__init__(size, folded)
```


What will the following print out?



{:.input_area}
```python
sheep = SheepBrain()
human = HumanBrain()
human.folded and sheep.folded
```


- A) True
- B) False
- C) None
- D) AssertionError
- E) ¯\\\_(ツ)\_/¯



{:.input_area}
```python
# has access to Brain() methods
sheep.print_info()
```


### Classes Review

- `class` creates a new class type
    - names tend to use CapWords case
    - can have attributes (including instance attributes) and methods
        - `obj.attribute` accesses data stored in attribute
        - `obj.method()` carries out code defined within method 


- instance attributes defined with `__init__`
    - `__init__` is a reserved method in Python
    - This "binds the attributes with the given arguments"
    - `self` refers to current instance

- to create an object (instance) of a specified class type (`ClassType`):
    - `object_name = ClassType(input1, input2)`
    - `self` is not given an input when creating an object of a specified class

## Everything in Python is an Object!

### Data variables are objects



{:.input_area}
```python
print(isinstance(True, object))
print(isinstance(1, object))
print(isinstance('word', object))
print(isinstance(None, object))

a = 3
print(isinstance(a, object))
```


### Functions are objects



{:.input_area}
```python
print(isinstance(sum, object))
print(isinstance(max, object))
```




{:.input_area}
```python
# Custom function are also objects
def my_function():
    print('yay Python!')
    
isinstance(my_function, object)
```


### Class definitions & instances are objects



{:.input_area}
```python
class MyClass():
    def __init__(self):
        self.data = 13

my_instance = MyClass()

print(isinstance(MyClass, object))
print(isinstance(my_instance, object))
```


## Object-Oriented Programming

<div class="alert alert-success">
<b>Object-oriented programming (OOP)</b> is a programming paradigm in which code is organized around objects. Python is an OOP programming langauge. 
</div>
