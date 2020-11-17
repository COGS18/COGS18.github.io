**Course Announcements**

**Due Dates:**
- **A4** due the Mon *after* next 11/16 (11:59 PM) 

**Notes**
- **CL5** grades posted and answers on website
- No class or Coding Lab next Wednesday (Veteran's Day)
    - **CL6** will be released later today but will not be due until Wed of week 7 (11/18)
- **E2** Friday of week 7 (11/20) 

**A brief functions review**

- defining vs. executing
- input parameters vs. variable assignment
- debugging & testing

# coding lab example
def reverse_string(input_string):
    
    rev = ''
    counter = len(input_string) 
    
    while counter > 1: 
        rev = rev + input_string[counter - 1]
        counter = counter - 1
    
    return rev

reverse_string('apple')

assert reverse_string('apple') == 'elppa'

# Classes

- `class`
    - attributes
    - methods
- instances
    - `__init__`
    - `super()`
- objects

## Objects Review

- Objects are a way to combine associated data (attributes) and procedures (methods) to do upon that data with a systematic organization

- So how do we define objects?
    - people have built & defined objects (i.e. dates and datetime)
    - defining your own

## Classes

<div class="alert alert-success">
<b>Classes</b> define objects. The <code>class</code> keyword opens a code block for instructions on how to create objects of a particular type.
</div>

Think of classes as the _blueprint_ for creating and defining objects and their properties (methods, attributes, etc.). They keep related things together and organized.

## Example Class: Dog

# Define a class with `class`. 
# By convention, class definitions use CapWords (Pascal)
class Dog():
    
    # Class attributes for objects of type Dog
    sound = 'Woof'
    
    # Class methods for objects of type Dog
    def speak(self, n_times=2):
        return self.sound * n_times

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


# Initialize a dog object
george = Dog()

# george, has 'sound' attribute(s) from Dog()
george.sound

# george, has 'Dog' method(s)
# remember we used `self`
george.speak(4)

#### Clicker Question #1

Which of the following statements is true about the example we've been using? 

class Dog():
    
    sound = 'Woof'
    
    def speak(self, n_times=2):
        return self.sound * n_times

- A) `Dog` is a Class, `sound` is an attribute, and `speak` is a method. 
- B) `Dog` is a function, `sound` is an attribute, and `speak` is a method. 
- C) `Dog` is a Class, `sound` is a method, and `speak` is an attribute. 
- D) `Dog` is a function, `sound` is an method, and `speak` is an attribute. 

### Using our Dog Objects

# Initialize a group of dogs
pack_of_dogs = [Dog(), Dog(), Dog(), Dog()]

# take a look at this
pack_of_dogs

# take a look at this
type(pack_of_dogs[0])

for dog in pack_of_dogs:
    print(dog.speak())

## Instances & self

<div class="alert alert-success">
An <b>instance</b> is particular instantiation of a class object. <code>self</code> refers to the current instance. 
</div>

# Initialize a dog object
george = Dog()

From our example above:

- Dog is the Class we created
- `george` was an _instance_ of that class
- self just refers to whatever the _current_ instance is

#### Clicker Question #2

How many instances of `Dog()` are created below and how many times does the `speak()` method execute?

pack_of_dogs = [Dog(), Dog(), Dog(), Dog()]

counter = 1

for doggie in pack_of_dogs:
    if counter <= 2:
        print(doggie.speak())
        counter += 1
    else:
        break

- A) 2 instances, 2 method executions
- B) 2 instances, 4 method executions
- C) 4 instances, 2 method executions
- D) 4 instances, 4 method executions
- E) ¯\\\_(ツ)\_/¯

## Instance Attributes

An instance attribute specific to the instance we're on. This allows different instances of the same class to be unique (have different values stored in attributes and use those in methods).

# Initialize a group of dogs
pack_of_dogs = [Dog(), Dog(), Dog(), Dog()]

This creates four different `Dog` type objects and stores them in a list. But, up until now...every `Dog` was pretty much the same.

<div class="alert alert-success">
Instance attributes are attributes that we can make be different for each instance of a class. <code>__init__</code> is a special method used to define instance attributes. 
</div>

## Example Class: Dog Revisited

- Two trailing underscores (a `dunder`, or double underscore) is used to indicate something Python recognizes and knows what to do every time it sees it.
- Here, we use `__init__` to execute the code within it every time you initialize an object.

class Dog():
    
    # Class attributes for Dogs
    sound = 'Woof'
    
    # Initializer, allows us to specify instance-specific attributes
    # leading and trailing double underscores indicates that this is special to Python
    def __init__(self, name):
        self.name = name
    
    def speak(self, n_times=2):
        return self.sound * n_times

# this code will give TypeError
Dog()

# Initialize a dog
# what goes in the parentheses is defined in the __init__
gary = Dog(name = 'Gary') 

# Check gary's attributes
print(gary.sound)    # This is an class attribute
print(gary.name)     # This is a instance attribute

# Check gary's methods
gary.speak()

**Course Announcements**

**Due Dates:**
- **A4** due Mon 11/16 (11:59 PM) 

**Notes**
- **A3** grades posted
- No class or Coding Lab Wednesday (Veteran's Day)
- **CL6** now available; due Wed of week 7 (11/18)
- **E2** Friday of week 7 (11/20) 

#### Clicker Question #3

Edit the code we've been using for the Class `Dog` to include information about the breed of the Class Dog in `NewDog`?

# EDIT CODE HERE
class NewDog():
    
    sound = 'Woof'
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def speak(self, n_times=2):
        return self.sound * n_times

## We'll execute here
lexi = NewDog('Lexi', 'Italian Greyhound')
lexi.name

- A) I did it!
- B) I think I did it!
- C) So lost. -_-

## Class example: Cat

# Define a class 'Cat'
class Cat():
    
    sound = "Meow"
    
    def __init__(self, name):
        self.name = name
    
    def speak(self, n_times=2):
        return self.sound * n_times

## Instances Examples

# Define some instances of our objects
pets = [Cat('Jaspurr'), Dog('Barkley'), 
        Cat('Picatso'), Dog('Ruffius')]

for pet in pets:
    print(pet.name, ' says:')
    print(pet.speak())

#### Clicker Question #4

What will the following code snippet print out?

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

student = MyClass('Rob', 'rob@python.com', 62)
student.check_score()

- A) True
- B) 'Rob'
- C) False 
- D) 'rob@python.com'
- E) None

from datetime import date
## see underlying code for date class
## we know what even more of this means now!
date??

## Class Inheritance

<div class="alert alert-success">
Objects can also be built from other objects, inheriting their properties and building off them.
</div>

If you have a hierarchical structure, this can be very helpful.

### Class Inheritance: `Animal()`

For our `Dog()` and `Cat()` example, you may on some more general `Animal()` class. 

You would want `Cat()` and `Dog()` to inherit all the 'stuff' from the `Animal` class. This would avoid the need to have the same code for the `speak` method in both `Cat()` and `Dog()`! Another way to cut down on copy + paste and code redundancy!

class Animal():
    
    sound = 'Generic Animal Sound'
    
    def __init__(self, name):
        self.name = name
    
    def speak(self, n_times=2):
        return self.sound * n_times

# specify class inheritance by passing
# parent class in parentheses
class Dog(Animal):
    sound = 'Woof'

class Cat(Animal):
    sound = "Meow"

Dog('Rufus').speak()

Cat('Purrnicia').speak(4)

**Terminology**:

- Parent Class: `Animal`
- Child classes: `Dog()` & `Cat()`

### Class Inheritance: `Tool()`

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


my_tool = Tool()
my_hammer = Hammer()
print(my_hammer.is_tool)
print(my_hammer.why)
print(my_hammer.tool_type)
my_hammer.use_tool()


**Terminology**:

- Note: the child's `__init__` function overrides the inheritance of a parent's `__init__` function
- `super()` function: inherit all methods and properties from parent

#### Clicker Question #5

Given the following set of classes, what will the cell below print out?

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
        
    

sheep = SheepBrain()
sheep.print_info()

- A) This brain is medium and folded.
- B) This brain is large and folded.
- C) This brain is medium and not folded.
- D) This brain is medium and False.
- E) ¯\\\_(ツ)\_/¯

#### Clicker Question #6

Given the following set of classes, what will the cell below print out?

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

sheep = SheepBrain()
human = HumanBrain()
human.folded and sheep.folded

- A) True
- B) False
- C) None
- D) AssertionError
- E) ¯\\\_(ツ)\_/¯

# has access to Brain() methods
sheep.print_info()

### Example: `ProfCourses()`

Let's put a lot of these concepts together in a more complicated example...

What if we wanted some object type that would allow us to keep track of Professor Ellis' Courses? Well...we'd want this to work for any Professor, so we'll call it `ProfCourses`.

We would likely want an object type and then helpful methods that allow us to add a class to the course inventory and to compare between courses.

class ProfCourses():
        
    # create three instance attributes
    def __init__(self, prof):
        self.n_classes = 0
        self.classes = []
        self.prof = prof

ellis_courses = ProfCourses('Ellis')
print(ellis_courses.n_classes)
print(ellis_courses.prof)

**`add_class()` method**

class ProfCourses():
    
    def __init__(self, prof):
        self.n_classes = 0
        self.classes = []
        self.prof = prof
    
    # add method that will add classes as a dictionary
    # to our attribute (classes)...which is a list
    def add_class(self, course_name, quarter, n_students):
        
        self.classes.append({'course_name': course_name,
                             'quarter' : quarter,
                             'n_students': n_students})
        # increase value store in n_classes
        # by 1 any time a class is added
        self.n_classes += 1

# create ellis_courses
ellis_courses = ProfCourses('Ellis')

# add a class
ellis_courses.add_class('COGS18', 'fa20', 363)

# see output
print(ellis_courses.n_classes)
ellis_courses.classes

**`compare()` method**

class ProfCourses():
    
    def __init__(self, prof):
        self.n_classes = 0
        self.classes = []
        self.prof = prof
    
    def add_class(self, course_name, quarter, n_students):
        
        self.classes.append({'course_name': course_name,
                             'quarter' : quarter,
                             'n_students': n_students})
        self.n_classes += 1
           
    # add method to compare values in classes
    def compare(self, attribute, direction='most'):
    
        fewest = self.classes[0]
        most = self.classes[0] 
        
        for my_class in self.classes:
            if my_class[attribute] <= fewest[attribute]:
                fewest = my_class
            elif my_class[attribute] >= most[attribute]:
                most = my_class
                
        if direction == 'most':
            output = most
        elif direction == 'fewest':
            output = fewest

        return output

# create ellis_courses
ellis_courses = ProfCourses('Ellis')

# add a bunch of classes
ellis_courses.add_class('COGS18', 'fa20', 363)
ellis_courses.add_class('COGS108', 'fa20', 447)
ellis_courses.add_class('COGS18', 'su20', 88)
ellis_courses.add_class('COGS108', 'sp20', 469)
ellis_courses.add_class('COGS108', 'sp19', 825)

# see the courses
print(ellis_courses.n_classes)
ellis_courses.classes

# make comparison among all courses
# returns the class with the most students
ellis_courses.compare('n_students')

# return the class with the fewest students
ellis_courses.compare('n_students', 'fewest')

**extending the functionality of the `compare()` method**

class ProfCourses():
    
    def __init__(self, prof):
        self.n_classes = 0
        self.classes = []
        self.prof = prof
    
    def add_class(self, course_name, quarter, 
                  n_students, n_exams, n_assignments):
        
        # add in additional key-value pairs
        self.classes.append({'course_name': course_name,
                             'quarter' : quarter,
                             'n_students': n_students,
                             'n_exams' : n_exams,
                             'n_assignments' : n_assignments})
        self.n_classes += 1
        
     
    def compare(self, attribute, direction='most'):
    
        fewest = self.classes[0]
        most = self.classes[0] 
        
        for my_class in self.classes:
            if my_class[attribute] <= fewest[attribute]:
                fewest = my_class
            elif my_class[attribute] >= most[attribute]:
                most = my_class
                
        if direction == 'most':
            output = most
        elif direction == 'fewest':
            output = fewest

        return output

# create ellis_courses
ellis_courses = ProfCourses('Ellis')

# add a bunch of classes
ellis_courses.add_class('COGS18', 'fa20', 363, 2, 5)
ellis_courses.add_class('COGS108', 'fa20', 447, 0, 6)
ellis_courses.add_class('COGS18', 'su20', 88, 3, 5)
ellis_courses.add_class('COGS108', 'sp20', 469, 0, 6)
ellis_courses.add_class('COGS108', 'sp19', 825, 0, 5)
ellis_courses.add_class('COGS18', 'fa19', 301, 2, 4)

# see the courses
print(ellis_courses.n_classes)

# return the class with the most exams
ellis_courses.compare('n_exams', 'most')

# return the class with the fewest assignments
ellis_courses.compare('n_assignments', 'fewest')

**Improving & updating this code**
- account for ties in `compare()`
- edit code in `compare()` to make the `for` loop and following conditional more intuitive
- add a method to put dictionary in time order
- etc.

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

- You can Inherit attributes and methods from other objects
    - pass the parent name into parentheses of child `class` definition
    - `super()` refers to the parent you're inheriting from (without having to specify parent class' name)

## Everything in Python is an Object!

### Data variables are objects

print(isinstance(True, object))
print(isinstance(1, object))
print(isinstance('word', object))
print(isinstance(None, object))

a = 3
print(isinstance(a, object))

### Functions are objects

print(isinstance(sum, object))
print(isinstance(max, object))

# Custom function are also objects
def my_function():
    print('yay Python!')
    
isinstance(my_function, object)

### Class definitions & instances are objects

class MyClass():
    def __init__(self):
        self.data = 13

my_instance = MyClass()

print(isinstance(MyClass, object))
print(isinstance(my_instance, object))

## Object-Oriented Programming

<div class="alert alert-success">
<b>Object-oriented programming (OOP)</b> is a programming paradigm in which code is organized around objects. Python is an OOP programming langauge. 
</div>