---
interact_link: content/materials/Exam-Prep/Exam2-Review-Answers.ipynb
download_link: assets/downloads/Exam2-Review-Answers.ipynb.zip
title: 'Exam2-Review-Answers'
prev_page:
  url: /materials/Exam-Prep/Exam2-Review
  title: 'Exam2-Review'
next_page:
  url: /materials/Exam-Prep/Exam2-Practice
  title: 'Exam2-Practice'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Exam 2 Review

- **CL4** due tonight
- **Exam #2 is tomorrow (Thurs)** 
    - released at 11AM ; 24h to complete and submit
    - must be submitted on datahub
    - E1 was a _tad_ too easy; E2 a *bit* more difficult
- **A4 is due Mon** (11:59 PM)
    - Have a solid understanding of the assigmnment through Q4 by Exam time
    - Bots (Part 3) beyond what will be tested on Exam #2
- Prof Ellis: Office Hours today 4-6 PM

## Exam II Plan (12.5 points)

Part I: **E1 Review** (2.25 points) 
- Q1: Variables & Indexing (0.75 points)
- Q2: Loops (0.5 points)*
- Q3: Code to accomplish a task (1 point)*

Part II: **Functions** (5.25 points)  
- Q4: Function execution (0.75 points)*
- Q5: Function I (2 points)*
- Q6: Function II (2.5 points)*

Part III: **Objects & Classes** (5 points)
- Q7: objects (0.5 points)*
- Q8: Classes I (2.5 points)*
- Q9: Classes II (2 points)*


\* : includes manual grading (partial credit)

### Reminder:

There are two extra notebooks that you can use for review:

1. [A1-Syntax](https://cogs18.github.io/materials/A1-Syntax/)
2. [A2-Examples](https://cogs18.github.io/materials/A2-Examples/)

There are also a few Exam #2 Practice Problems [here](https://cogs18.github.io/materials/Exam-Prep/Exam2-Practice) and a practice exam on datahub.

## Questions?

A reminder, as it will come up on the exam:



{:.input_area}
```python
# can have a dictionary as a key for an outside dictionary
my_dict = {'Shannon' : {'key': ['last_name', 'activity']}}
```




{:.input_area}
```python
my_dict['Shannon']
```





{:.output_data_text}
```
{'key': ['last_name', 'activity']}
```



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

<h3><center> We will focus on the Python ecosystem, "good code," and applications of Python. </center></h3>
