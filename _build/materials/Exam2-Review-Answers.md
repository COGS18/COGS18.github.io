---
interact_link: content/materials/Exam2-Review-Answers.ipynb
download_link: assets/downloads/Exam2-Review-Answers.ipynb.zip
pdf_link: assets/pdf/Exam2-Review-Answers.pdf
layout: materials
title: 'Exam2-Review-Answers'
prev_page:
  url: /materials/Exam2-Review
  title: 'Exam2-Review'
next_page:
  url: /materials/Exam2-Practice
  title: 'Exam2-Practice'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Exam 2 Review

- **Exam #2 is Friday** 
    - released at 8AM ; 24h to complete and submit
    - must be submitted on datahub
- **CL7** due tonight (11:59 PM)
- **A4 is due Mon 5/18** (11:59 PM)
    - Have a solid understanding of the assigmnment through the `OfficeHours` example by Exam time
    - Car Inventory & Bots w/ Inheritance beyond what will be tested on Exam #2
- No office hours on Friday for any Instructional Staff
    - Prof Ellis will hold extra office hours Thurs 10-11 AM & 12-1 PM

## Exam II Plan (20 points)

Part I: **E1 Review** (5 points) 
- Q1: Variables & Operators (1 point)
- Q2: Variables & Indexing (1 point)
- Q3: Loops (1 point)
- Q4: Code to accomplish a task (2 points)

Part II: **Functions** (9 points)  
- Q5: Function execution (2 points)*
- Q6: Function I (3 points)*
- Q7: Function II (4 points)*

Part III: **Objects & Classes** (5 points)
- Q8: objects (1 point)*
- Q9: classes (4 points)*

Part IV: **True/False** (1 point)  

\* : includes manual grading (partial credit)

Note: There will be **two notebooks** to complete for the second exam.

This will enable the calculation of your "E1 on E2 score" - allowing for potential increase in E1 scores (No E1 scores will be decreased.)

### E1 vs E2

Similarities between E1 and E2:
- format and timeline
- limited assert statements
- less guided than assignments

Differences between E1 and E2:
- No `%%writefile` cells
- No 'hypothetical' objects
- No written responses
- More partial credit
- True/False section
- Two notebooks to complete
- Fewer questions on E2

### Reminder:

There are two extra notebooks that you can use for review:

1. [A1-Syntax](https://cogs18.github.io/materials/A1-Syntax/)
2. [A2-Examples](https://cogs18.github.io/materials/A2-Examples/)

There are also a few Exam #2 Practice Problems [here](https://cogs18.github.io/materials/Exam2-Practice) and a practice exam on datahub.

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


#### Functions Answers



{:.input_area}
```python
## Functions Quesiton #1

def remainder(num1, num2):  # set default values within parenthesis
    out = num1 % num2
    return out
```




{:.input_area}
```python
## Functions Question #2

my_remainder = remainder(10, 4)
my_remainder
```





{:.output_data_text}
```
2
```





{:.input_area}
```python
## Functions Question #3
sum_list([1, 2, 3])
```





{:.output_data_text}
```
6
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


The exam question will be more involved than this example. It's meant to combine all the pieces we've learned this quarter (classes w/ methods, conditionals, etc).

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


#### Objects & Classes Answers

Question #1A: 



{:.input_area}
```python
class Rocket():
    
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def move_up(self):
        self.y += 1
```


Question #1B:



{:.input_area}
```python
my_rocket = Rocket()
```


Question #1C:



{:.input_area}
```python
my_rocket.move_up()
my_rocket.move_up()
my_rocket.y
```





{:.output_data_text}
```
2
```



Question #2: 
- method
- object

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

#### Extras Answers



{:.input_area}
```python
# Extras Question #1
print(chr(ord('A')))
```


{:.output_stream}
```
A

```

Extras Question #2

returning information about what objects are stored in your namespace (i.e. variables, functions, classes, etc.)



{:.input_area}
```python
%whos
```


{:.output_stream}
```
Variable       Type        Data/Info
------------------------------------
Rocket         type        <class '__main__.Rocket'>
my_remainder   int         2
my_rocket      Rocket      <__main__.Rocket object at 0x10ff9def0>
remainder      function    <function remainder at 0x10ff5ee18>
sum_list       function    <function sum_list at 0x10ff6da60>

```

Extras Question #3

For each of the following, indicate if the statement is True or False about Python and programming:

- **True**/False Whitespace matters in Python
- True/**False** Comments in Python start with '%' 					
- True/**False** You have to specify a data type when you define a variable
- True/**False** Every Python variable is available from every namespace		
- True/**False** `ls` is a shell command that creates a new file 		
- True/**False** `cd` returns your current working directory		
- **True**/False Everything in Python is an object
- **True**/False `print_name()` follows best practices for function naming

<h2><center>After the second exam:</center></h2>

<h3><center> We will focus on the Python ecosystem, and applications of Python. </center></h3>

<h3><center> We also become a project based course. </center></h3>
