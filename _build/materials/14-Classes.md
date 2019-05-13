---
interact_link: content/materials/14-Classes.ipynb
download_link: assets/downloads/14-Classes.ipynb.zip
pdf_link: assets/pdf/14-Classes.pdf
layout: materials
title: '14-Classes'
prev_page:
  url: /materials/13-Objects
  title: '13-Objects'
next_page:
  url: /materials/15-Namespaces
  title: '15-Namespaces'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

## Course Announcements

- Exam next Friday 5/10
- A4 due Mon 5/13

# Classes

- `class`
    - attributes
    - methods
- instances
    - `__init__`
- objects

## Objects Review

- Objects are a way to combine associated data (attributes) and procedures (methods) to do upon that data with a systematic organization

- So how do we define objects?
    - people have built & defined objects (i.e. dates and datetime)
    - defining your own

## Classes

<div class="alert alert-success">
'Classes' define objects. The `class` keyword opens a code block for instructions on how to create objects of a particular type.
</div>

Think of classes as the _blueprint_ for creating and defining objects and their properties (methods, attributes, etc.). They keep related things together and organized.

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


A reminder:
- **attributes** maintain the object's state; they lookup information about an object
- **methods** alter the object's state; they run a function on an object

**Class** notes:

- classes tend to use **CamelCase**
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

### Clicker Question #1

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
[<__main__.Dog at 0x111c3a4e0>,
 <__main__.Dog at 0x111c3a518>,
 <__main__.Dog at 0x111c3a550>,
 <__main__.Dog at 0x111c3a588>]
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
An 'instance' is particular instantiation of a class object. `self` refers to the current instance. 
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

### Clicker Question #2

How many instances of `Dog()` are created below and how many times does the `speak()` method execute?



{:.input_area}
```python
pack_of_dogs = [Dog(), Dog(), Dog(), Dog()]

counter = 1

for doggie in pack_of_dogs:
    if(counter <= 2):
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



{:.input_area}
```python
# Initialize a group of dogs
pack_of_dogs = [Dog(), Dog(), Dog(), Dog()]
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

### Clicker Question #3

Considering the output above, how many instances of dog are there?

- A) 0
- B) 1
- C) 2
- D) 3
- E) 4

<div class="alert alert-success">
Instance attributes are attributes that we can make be different for each instance of a class. `__init__` is a special method used to define instance attributes. 
</div>

## Example Class: Dog Revisited

- Two trailing underscores is used to indicate something Python recognizes and knows what to do every time it sees it.
- Here, we use `__init__` to execute the code within it every time you initialize an object.



{:.input_area}
```python
class Dog():
    
    # Class attributes for Dogs
    sound = 'Woof'
    
    # Initializer, allows us to specificy instance-specific attributes
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
gary = Dog('Gary') 
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

### Clicker Question #4

Edit the code we've been using for the Class `Dog` to include information about the breed of the Class Dog?



{:.input_area}
```python
class Dog():
    
    # Class attributes for Dogs
    sound = 'Woof'
    
    # Initializer, allows us to specificy instance specific attributes
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def speak(self):
        print(self.sound)
```




{:.input_area}
```python
## We'll execute here
lexi = Dog('Lexi','Italian Greyhound')
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
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.sound)
```


## Instances Examples



{:.input_area}
```python
# Define some instances of our objects
pets = [Cat('Jaspurr'), Dog('Barkley'), Cat('Picatso'), Dog('Ruffius')]
```




{:.input_area}
```python
for pet in pets:
    print(pet.name, ' says:')
    pet.speak()
```


{:.output_stream}
```
Jaspurr  says:
Meow
Barkley  says:
Woof
Picatso  says:
Meow
Ruffius  says:
Woof

```

### Clicker Question #4

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
student = MyClass('Rob', 'rob@python.com' , 62)
student.check_score()
```





{:.output_data_text}
```
'rob@python.com'
```



- A) True
- B) 'Rob'
- C) False 
- D) 'rob@python.com'
- E) None

### Clicker Question #5

Which is the best description:
- A) objects are described by instances, with particular instantiations of them called classes. 
- B) instances are described by classes, with particular instantiations of them called objects. 
- C) classes are described by objects, with particular instantiations of them called instances. 
- D) objects are described by classes, with particular instantiations of them called instances. 
- E) None of this makes any sense. 



{:.input_area}
```python
from datetime import date
## see underlying code for date class
## we know what even more of this means now!
date??
```


## Class Inheritance

<div class="alert alert-success">
Objects can also be built from other objects, inheriting their properties and building of them.
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


{:.output_stream}
```
True
To hammer things.
Using tool.

```

### Clicker Question #6

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
    
    def __init__(self, size='medium', folded=False):
        super().__init__(size, folded)
```


What will the following print out?



{:.input_area}
```python
sheep = SheepBrain()
sheep.print_info()
```


{:.output_stream}
```
This brain is medium and is not folded.

```

- A) This brain is medium and folded.
- B) This brain is large and folded.
- C) This brain is medium and not folded.
- D) This brain is medium and False.
- E) ¯\\\_(ツ)\_/¯

### Clicker Question #7

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
    
    def __init__(self, size='medium', folded=False):
        super().__init__(size, folded)
        
class HumanBrain(Brain):
    def __init__(self, size='large', folded=True):
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

## Everything in Python is an Object!

### Data variables are objects



{:.input_area}
```python
print(isinstance(True, object))
print(isinstance(1, object))
print(isinstance('word', object))
print(isinstance(None, object))

a=3
print(isinstance(a, object))
```


{:.output_stream}
```
True
True
True
True
True

```

### Functions are objects



{:.input_area}
```python
print(isinstance(sum, object))
print(isinstance(max, object))
```


{:.output_stream}
```
True
True

```



{:.input_area}
```python
# Custom function are also objects
def my_function():
    print('yay Python!')
    
isinstance(my_function, object)
```





{:.output_data_text}
```
True
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


{:.output_stream}
```
True
True

```

<img src="img/object.jpg" width="600" align="middle">


## Object Oriented Programming

<div class="alert alert-success">
Object-oriented programming (OOP) is a programming paradigm in which code is organized around objects. Python is an OOP programming langauge. 
</div>

## Midterm Expectations

You will be expected to: 

1. Recognize, understand and _respond_ to Python syntax:
    - statements & comments, whitespace, code blocks & indentation levels
2. Recognize, understand and be able to _explain_ code constructions:
    - variables, operators, data types, conditionals, loops, functions, errors, & classes 
    - keywords (def, class, return, etc.)
3. Know and be able to explain (roughly define) concepts we have talked about
    - encodings & algorithms are related concepts (encryption, computability)
4. Be able to apply what you've learned:
    - Given a task:
        - what kind of code constructions are needed to answer it?
        - what kind of concepts does it relate to?
5. With respect to everything above, be able to read and respond to short code snippets and write out code 