---
interact_link: content/labs/CL5-ProjectPlans.ipynb
download_link: assets/downloads/CL5-ProjectPlans.ipynb.zip
layout: notebooks
title: 'CL5-ProjectPlans'
prev_page:
  url: /labs/CL4B-Answers
  title: 'CL4B-Answers'
next_page:
  url: /labs/CL6-CommandLine
  title: 'CL6-CommandLine'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# CL5: Project Plans

Welcome to the fifth coding lab!

In this CodingLab we will be thinking and working with objects.

First, however, we will start thinking and talking about projects!

## Project Preparation

First, make sure you have read through the Project Description outline that is posted on the website. 

Now, try and spend some time to explore what ideas you would like to work on. 

Talk to some other students to share ideas, and ask questions of the TAs & IAs. 

Try to figure out a first idea of what you would like to work on. 

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




{:.input_area}
```python
# Create another instance of our class
english = Language('english', 'human', 'some')
english.print_goodness_level()
```


## Objects Questions

### TritonCourse class

Let’s create a class to represent courses at UCSD! 

#### Class Definition

Write a class to store information about UCSD courses, called `TritonCourse`. 

This course assumes all courses belong to a department, have a course code, and have a title.

That is, write a class called `TritonCourse` that has instance attributes `department` (string), `code` (int), and `title` (string). 



{:.input_area}
```python
## YOUR CODE HERE

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


Now, create some more instances of our class:

- ECE 15, "Engineering Programming" 
    - Save the result to a variable called `class1`
- MUS 8, "American Music: Jazz Culture"
    - Save the result to a variable called `class2`



{:.input_area}
```python
## YOUR CODE HERE

```


#### Methods

Now, make a new version of `TritonCourse` that has a method. 

Specifically, this method, called `print_info` should print out the information about the course as:

    'department name code : title'
    
So, for example, once you add this method, using the method on our `cogs18` instance should print out:

    `COGS 18 : Introduction to Python`



{:.input_area}
```python
## YOUR CODE HERE

```




{:.input_area}
```python
# Check the method works on our cogs18 instance
cogs18 = TritonCourse("COGS", 18, "Introduction to Python")
cogs18.print_info()
```


## Objects Explorations

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

