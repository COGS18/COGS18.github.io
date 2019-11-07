---
interact_link: content/materials/Exam2-Review.ipynb
download_link: assets/downloads/Exam2-Review.ipynb.zip
pdf_link: assets/pdf/Exam2-Review.pdf
layout: materials
title: 'Exam2-Review'
prev_page:
  url: /materials/E1-Answers
  title: 'E1-Answers'
next_page:
  url: /materials/Exam2-Review-Answers
  title: 'Exam2-Review-Answers'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Exam 2 Review

- **Exam #2 is Wed 11/13** (in class)
    - similar format to Exam #1
    - more places where you'll be asked to write code
- **A4 is due Fri 11/15** (11:59 PM)
    - Have a solid understanding of the `OfficeHours` example by Exam time
    - Car Inventory & Bots w/ Inheritance beyond what will be tested on Exam #2

### Exam #2 Mechanics

- Primarily short answers
- Also: multiple choice, true/false, etc.

#### The test is on paper.
- You _will_ be both writing and interpreting code
- You will _NOT_ be writing or debugging _large_ code sections (>15 lines) on paper

## Exam #2 Expectations

You will be expected to: 

1. Recognize, understand and _respond_ to Python syntax:
    - statements & comments, whitespace, code blocks & indentation levels
    - keywords (def, class, return, etc.)

2. Recognize, understand and be able to _explain_ code constructions:
    - variables, operators, data types, conditionals, loops
    - functions, classes
    - know and understand basic shell commands 

3. Know and be able to explain (roughly define) concepts we have talked about:
    - encodings, algorithms, computability are related concepts 
    - understand what you did on A2 and A3 
    - Namespaces & Debugging

4. Be able to apply what you've learned:
    - Given a task:
        - what kind of code constructions are needed to answer it?
        - what kind of concepts does it relate to?

5. With respect to everything above, be able to read and respond to short code snippets and write out code.

## Exam Plan (60 points)

Part I: Variables & Operators (6 points)  
Part II: Indexing (4 points)  
Part III: Control Flow - Conditionals & Loops (4 points)  
Part IV: **Functions** (27 points)  
Part V: **Objects & Classes** (12 points)  
Part VI: True/False (7 points)  


### Reminder:

There are two extra notebooks that you can use for review:

1. [A1-Syntax](https://cogs18.github.io/materials/A1-Syntax/)
2. [A2-Examples](https://cogs18.github.io/materials/A2-Examples/)

There are also a few Exam #2 Practice Problems [here](https://cogs18.github.io/materials/Exam2-Practice).

## Questions?

### Functions

- `def`
    - `return`
- executing a function
    - parameters
        - keyword vs. positional
        - default values
    - have a separate namespace
- methods 
    - in place vs. not in place

#### Functions Question #1
Write, in real code, a function called `remainder` that takes two inputs, divides the first input by the second and returns the remainder.



{:.input_area}
```python
## YOUR CODE HERE
```


#### Functions Question #2
Using the function `remainder` you wrote above, write the python code you would use to return the remainder of 10 divided by 4. Store the output in the variable `my_remainder`.



{:.input_area}
```python
## YOUR CODE HERE
```


#### Functions Question #3
Assuming the following function has been defined, what would `sum_list([1, 2, 3])` return?



{:.input_area}
```python
def sum_list(my_list):
    total = 0
    
    for item in my_list:
        total += item
        
    return total
```




{:.input_area}
```python
## CODE TO TEST HERE
```


### Objects & Classes

- objects & `class`
    - attributes
    - methods
    - instances


#### Objects & Classes Question #1

**Part A**

We want to simulate a rocket ship for a game.

Write code that will create a class `Rocket`. 

This class should have two instance attributes: `x` and `y`. These will specify the x,y position of the rocket. Each attribute should be initialized with hte value 0. 

Your `Rocket` should also have the method `move_up()`. This method should increment the y-position of the rocket by 1. 



{:.input_area}
```python
## YOUR CODE HERE
```


The exam question will be slightly more involved than this example. It's meant to combine all the pieces we've learned this quarter (classes w/ methods, conditionals, etc.

**Part B**

Create an instance `my_rocket` of your Rocket object.



{:.input_area}
```python
## YOUR CODE HERE
```


**Part C**

Update `my_rocket` so that `my_rocket` has the `y` position 3.



{:.input_area}
```python
## YOUR CODE HERE
```


#### Objects & Classes Question #2

Fill in the blanks:

	What is the name of a function defined within a class: ______________

	In Python, everything is a(n) ______________. 


### Python & Jupyter Extras
- encodings (`chr` & `ord`)
- whitespace
- namespace
- kernel
- code comments
- magic functions

#### Extras Question #1
What will the following piece of code print out?

```print(chr(ord('A')))``` 
    
     _____________

#### Extras Question #2

What is the magic function `%whos` used for?

#### Extras Question #3

For each of the following, indicate if the statement is True or False about Python and programming:

- True/False Whitespace matters in Python
- True/False Comments in Python start with '%' 					
- True/False You have to specify a data type when you define a variable
- True/False Every Python variable is available from every namespace		
- True/False `ls` is a shell command that creates a new file 		
- True/False `cd` returns your current working directory		
- True/False Everything in Python is an object
- True/False `print_name()` folles best practices for function naming

<h2><center>After the second exam:</center></h2>

<h3><center> We will focus on the Python ecosystem, and applications of Python. </center></h3>

<h3><center> We also become a project based course. </center></h3>
