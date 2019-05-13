---
interact_link: content/labs/CL5B-Answers.ipynb
download_link: assets/downloads/CL5B-Answers.ipynb.zip
layout: notebooks
title: 'CL5B-Answers'
prev_page:
  url: /labs/CL5-Classes
  title: 'CL5-Classes'
next_page:
  url: /labs/CL6-ProjectBrainstorm
  title: 'CL6-ProjectBrainstorm'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# CL5: Classes

Welcome to the fifth coding lab!

In this CodingLab we will be thinking and working with objects.

## Part I: Objects Questions

## Example Class



{:.input_area}
```python
class Language():
    """A Python class to store and use information about languages."""
    
    # Class Attributes
    purpose = 'communication'
    
    def __init__(self, name, language_type, amount_of_goodness):
        
        # Instance Attributes
        self.name = name
        self.language_type = language_type
        self.amount_of_goodness = amount_of_goodness
        
    # Class Method
    def print_goodness_level(self):
        print('The language', self.name, 'has', self.amount_of_goodness, 'goodness.')
```




{:.input_area}
```python
# Create an instance of our class
python = Language('python', 'computer', 'lots of')
python.print_goodness_level()
```


{:.output_stream}
```
The language python has lots of goodness.

```



{:.input_area}
```python
# Create another instance of our class
english = Language('english', 'human', 'some')
english.print_goodness_level()
```


{:.output_stream}
```
The language english has some goodness.

```

### TritonCourse class

Let’s create a class to represent courses at UCSD! 

#### Class Definition

Write a class to store information about UCSD courses, called `TritonCourse`. 

This course assumes all courses belong to a department, have a course code, and have a title.

That is, write a class called `TritonCourse` that has instance attributes `department` (string), `code` (int), and `title` (string). 



{:.input_area}
```python
class TritonCourse:
    
    university = "UC San Diego"
    
    def __init__(self, department, code, title):
        """
        department: string
        code: int
        title: string
        """
    
        self.department = department
        self.code = code
        self.title = title
```


#### Instances

Once you've written the class defintion above, you should be able to run the following code to create an instance of this class. 

You can then print out the attributes and check that they hold the values that you expect. 



{:.input_area}
```python
# Define an instance of our class
cogs18 = TritonCourse("COGS", 18, "Introduction to Python")
```




{:.input_area}
```python
# Check the instance attributes
print(cogs18.department)
print(cogs18.code)
print(cogs18.title)
```


{:.output_stream}
```
COGS
18
Introduction to Python

```

Now, create some more instances of our class:

- ECE 15, "Engineering Programming" 
    - Save the result to a variable called `class1`
- MUS 8, "American Music: Jazz Culture"
    - Save the result to a variable called `class2`



{:.input_area}
```python
class1  = TritonCourse("ECE",15,"Engineering Programming")
class2 = TritonCourse("MUS", 8, "American Music: Jazz Culture")
```


#### Methods

Now, make a new version of `TritonCourse` that has a method. 

Specifically, this method, called `print_info` should print out the information about the course as:

    'department name code : title'
    
So, for example, once you add this method, using the method on our `cogs18` instance should print out:

    COGS 18 : Introduction to Python



{:.input_area}
```python
class TritonCourse:
    
    university = "UC San Diego"
    
    def __init__(self, department, code, title):
        """
        department: string
        code: int
        title: string
        """
    
        self.department = department
        self.code = code
        self.title = title
    
    def print_info(self):
        print(self.department + str(self.code) + ': ' + self.title)
```




{:.input_area}
```python
# Check the method works on our cogs18 instance
cogs18 = TritonCourse("COGS", 18, "Introduction to Python")
cogs18.print_info()
```


{:.output_stream}
```
COGS18: Introduction to Python

```

## Part II: Objects Explorations

- What kind of other attributes and methods might we want on our `TritonCourse` object?
    - Make an extended version of `TritonCourse` with at least one extra class attribute, instance attribute and method. 
- Create a brand new class, to do something new / different!
    - Make sure it has at least one class attribute, instance attribute, and some methods
    - Create at least one methods that takes in an argument (doesn't just use class & instance attributes)
    - Create at least one method that has a conditional in it, one with a loop, and one with a try/except



{:.input_area}
```python
## YOUR CODE HERE


```
