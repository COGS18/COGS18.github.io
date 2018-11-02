---
download_link: assets/downloads/14-Classes.ipynb.zip
pdf_link: assets/pdf/14-Classes.pdf
title: '14-classes'
permalink: '/chapters/14-Classes'
previouschapter:
  url: /chapters/13-Objects
  title: '13-objects'
nextchapter:
  url: /chapters/15-Namespaces
  title: '15-namespaces'
redirect_from:
  - '/chapters/14-classes'
---

# Classes

### Clicker Question #1

What will the following code snippet print out:



{:.input_area}
```python
my_number = 13.3; my_string = "word"

def check_data(word, number):

    if not my_string.islower():
        answer = 'A1'
    elif number.is_integer() or word.isalpha():
        answer = 'A2'
    else:
        answer = 'A3'
        
    return answer

check_data(my_string, my_number)
```


A) 'A1' | B) 'A2' | C) 'A3' | D) 'A1,A2' | E) None

## Objects

- Objects are a way to combine associated data and procedures to do upon that data with a systematic organization

- So how do we define objects?

## Classes

<div class="alert alert-success">
'Classes' define objects. The 'class' keyword opens a code block for instructions on how to create objects of a particular type.
</div>

## Example Class: Dog



{:.input_area}
```python
# Define a class with `class`. By convention, class definitions use CamelCase
class Dog():
    
    # Class attributes for objects of type Dog
    sound = "Woof"
    
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
george.speak()
```


{:.output_stream}
```
Woof

```

### Using our Dog Objects



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

## Instances & Self

<div class="alert alert-success">
An 'instance' is particular instantiation of a class object. `self` refers to the current instance. 
</div>

## Instance Attributes

<div class="alert alert-success">
Instance attributes are attributes that we can make be different for each instance of a class. `__init__` is a special method used to define instance attributes. 
</div>

## Example Class: Dog Revisited



{:.input_area}
```python
class Dog():
    
    # Class attributes for Dogs
    sound = "Woof"
    
    # Initializer, which allows us to specificy instance specific attributes
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.sound)
```




{:.input_area}
```python
# Initialize a dog, that
gary = Dog('Gary')
```




{:.input_area}
```python
# Check gary's attributes
print(gary.sound)    # This is an instance attribute
print(gary.name)     # This is a class attribute
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

### Clicker Question #2

What will the following code snippet print out:



{:.input_area}
```python
class MyClass():
    
    def __init__(self, name, email, score):
        self.name = name
        self.email = email
        self.score = score
    
    def check_score(self):
        
        if self.score <= 75:
            return self.email
        else:
            return False
```




{:.input_area}
```python
student = MyClass('Rob', 'rob@python.com' , 62)
student.check_score()
```


A) True | B) 'Rob' | C) False | D) 'rob@python.com' | E) None

### Clicker Question #3

Which is the best description:
- A) objects are described by instances, with particular instantiations of them called classes. 
- B) instances are described by classes, with particular instantiations of them called objects. 
- C) classes are described by objects, with particular instantiations of them called instances. 
- D) objects are described by classes, with particular instantiations of them called instances. 
- E) None of this makes any sense. 

## Everything in Python is an Object!

### Data variables are objects



{:.input_area}
```python
print(isinstance(True, object))
print(isinstance(1, object))
print(isinstance('word', object))
print(isinstance(None, object))
```


{:.output_stream}
```
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

instance = MyClass()

print(isinstance(MyClass, object))
print(isinstance(instance, object))
```


{:.output_stream}
```
True
True

```

## Object Oriented Programming

<div class="alert alert-success">
Object-oriented programming (OOP) is a programming paradigm in which code is organized around objects. Python is an OOP programming langauge. 
</div>
