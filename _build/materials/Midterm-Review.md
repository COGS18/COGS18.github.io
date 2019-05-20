---
interact_link: content/materials/Midterm-Review.ipynb
download_link: assets/downloads/Midterm-Review.ipynb.zip
pdf_link: assets/pdf/Midterm-Review.pdf
layout: materials
title: 'Midterm-Review'
prev_page:
  url: /materials/A2-Examples
  title: 'A2-Examples'
next_page:
  url: /materials/MidtermPractice
  title: 'MidtermPractice'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Midterm Review

- A4 due Monday (11:59 PM)

<h1 align="center">Midterm is Friday 5/10</h1>

## Midterm Expectations

You will be expected to: 

1. Recognize, understand and _respond_ to Python syntax:
    - statements & comments, whitespace, code blocks & indentation levels
2. Recognize, understand and be able to _explain_ code constructions:
    - variables, operators, data types, conditionals, loops, functions, errors, classes & imports
    - keywords (def, class, return, etc.)
3. Know and be able to explain (roughly define) concepts we have talked about
    - encodings & algorithms are related concepts (encryption, computability)
4. Be able to apply what you've learned:
    - Given a task:
        - what kind of code constructions are needed to answer it?
        - what kind of concepts does it relate to?
5. With respect to everything above, be able to read and respond to short code snippets and write out code 

### Midterm Mechanics

- Primarily short answers
- Also: multiple choice, true/false, etc.

#### The test is on paper.
- You _will_ be both writing and interpreting code
- You will _NOT_ be writing or debugging _large_ code sections on paper

### Midterm Focus

- Heavier on the stuff you've been using and gotten lots of practice with (variables, operators, conditionals, loops, functions, etc.)
- Lighter on more recent material (Objects, Classes, instances, etc.) - it's on there, but it's more basic concepts, not tough applications

### Reminder:

There are two extra notebooks that you can use for review:

1. [A1-Syntax](https://cogs18.github.io/materials/A1-Syntax/)
2. [A2-Examples](https://cogs18.github.io/materials/A2-Examples/)

There are also a few Midterm Practice Problems [here](https://cogs18.github.io/materials/MidtermPractice).

## Topics & Example Questions

- Variables & Data Types
- Operators, Conditionals, & Loops
- Functions, Objects & Classes
- Python & Jupyter Extras

### Variables & DataTypes

Types:
- strings, integers, floats, Booleans, None
- Collections
    - Lists
    - Tuples
    - Dictionaries

Concepts:
- Mutable vs. Immutable
- Indexing

#### Data Types Question #1

What is the difference between a tuple and a list?

#### Data Types Question #2

Given the following list: 

```python
ice_cream = ['vanilla', 'chocolate', 'strawberry', 'cherry', 'salted caramel']

```

Edit the code at right with how would you return the specified values on left:

```python
['vanilla', 'chocolate', 'strawberry'] : ice_cream[      ]
```

#### Data Types Question #3

Write a line of code that would change the third element of a list `my_list` to store the value `12`.

#### Data Types Answers

Data Types Question #1

Tuples are created with () and are immutable.  
Lists are created with [] and are mutable.



{:.input_area}
```python
# Data Types Question #2
ice_cream = ['vanilla', 'chocolate', 'strawberry', 'cherry', 'salted caramel']
ice_cream[-5:-2]
ice_cream[:3]
ice_cream[0:3]
```





{:.output_data_text}
```
['vanilla', 'chocolate', 'strawberry']
```





{:.input_area}
```python
# Data Types Question #3
my_list[2] = 12
```




{:.input_area}
```python
# Data Types Question #3
my_list = [1,2,3,4,5,6]
my_list[2] = 12
my_list
```





{:.output_data_text}
```
[1, 2, 12, 4, 5, 6]
```



### Operators

- assignment : `=`
- math: `+`, `-`, `/`, `*`, `**`, `//`
- comparison : `==`, `!=`, `<`, `>`, `<=`, `>=`
- logic: `and`, `or`, `not`
- identity: `is`, `is not`
- membership : `in`, `not in`

#### Operators Question #1

What is the difference between `=` and `==`?

#### Operators Question #2

Write out what the following expression will evaluate as:

```python
not False or not True
```

#### Operators Question #3

Write out what the following expression will evaluate as:

```python
2**2 + 2
```

#### Operators Question #4

Write out what the following expression will evaluate as:

```python
'cogs' + '18'
```

#### Operators Answers

Operators Question #1

= is an assignment operator  
== checks for equality



{:.input_area}
```python
# Operators Question #2
not False or not True
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
# Operators Question #3
2**2 + 2
```





{:.output_data_text}
```
6
```





{:.input_area}
```python
# Operators Question #4
'cogs' + '18'
```





{:.output_data_text}
```
'cogs18'
```



### Conditionals

- `if`, `elif`, & `else`

#### Conditionals Question #1

Circle necessary or optional, as applicable: In Python, a conditional has a necessary / optional `if` statement, one or more necessary / optional `elif` statement(s) and a necessary / optional `else` statement. 

#### Conditionals Question #2

Given the following outline of a conditional:

```python
    if COND_A:
        # Code Block A
	elif COND_B:
		# Code Block B
	else:
		# Code Block C
```

1. If `COND_A` and `COND_B` are both `True`, which code block(s) evaluate?
2. If `COND_A` is False and `COND_B` is `True`, which code block(s) evaluate?

#### Conditionals Answers

Conditionals Question #1

necessary, optional, optional

Conditionals Question #2

1. Code Block A
2. Code Block B



{:.input_area}
```python
# how to check your thinking when you're studying
COND_A = True
COND_B = True

if COND_A:
    print('a')
elif COND_B:
    print('b')
else:
    print('c')
```


{:.output_stream}
```
a

```

### Loops

- loops: `for` and `while`
    - `continue`, `break`, `pass`

#### Loops Question #1
What are the two kinds of loops? ____________ and ____________

#### Loops Question #2
Use the following:
`ind = 1` to write a loop (using real Python code) that would loop and print the value `ind` of ind each time through the loop _and_ update the value of ind by 1. Have this loop stop after 4 iterations. 

#### Loops Answers

Loops Question #1

for and while



{:.input_area}
```python
# Loops Question #2
ind = 1

while ind <= 4:
    print(ind)
    ind += 1
    #or ind = ind + 1
```


{:.output_stream}
```
1
2
3
4

```

## Clicker Question

How are you feeling about the midterm?

- A) Very Prepared
- B) Somewhat prepared
- C) OK
- D) Somewhat nervous
- E) Very nervous

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
Write, in real code, a function called `add` that takes two inputs, assumed to be numbers, sums them together and returns the result.



{:.input_area}
```python
## YOUR CODE HERE
```


#### Functions Question #2
Using the function `add` you wrote above, write the python code you would use to add the value 16 and 18 together. Store the output in the variable `my_sum`.



{:.input_area}
```python
## YOUR CODE HERE
```


#### Functions Answers



{:.input_area}
```python
## Functions Quesiton #1

def add(num1, num2):  # set default vlues within parenthesis
    out = num1 + num2
    return out
```




{:.input_area}
```python
## Functions Question #2

my_sum = add(16,18)
# OR
my_sum = add(18,16)

my_sum
```





{:.output_data_text}
```
34
```



### Objects & Classes

- objects & `class`
    - attributes
    - methods
    - instances


#### Objects & Classes Question #1

Given an instance object 'koala' of the class 'Animals', write a line to:

	call the method 'speak' on 'koala': 	_________________________________

	access the attribute 'sound' of 'koala': 	_________________________________


#### Objects & Classes Question #2

Fill in the blanks:

	What is the name of a function defined within a class: ______________

	In Python, everything is a(n) ______________. 


#### Objects & Classes Answers

Question #1: 
- `koala.speak()`
- `koala.sound`

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

For each of the following, indicate if the statement is True or False about Python

- True/False Whitespace matters in Python
- True/False Comments in Python start with '%' 					
- True/False You have to specify a data type when you define a variable
- True/False Every Python variable is available from every namespace		


#### Extras Answers



{:.input_area}
```python
# Extras Question #1
print(chr(ord('A')))
```


Extras Question #2

returning information about what objects are stored in your namespace (i.e. variables, functions, classes, etc.)



{:.input_area}
```python
%whos
```


Extras Question #3

- True - Whitespace matters in Python
- False - Comments in Python start with '%' 					
- False - You have to specify a data type when you define a variable
- False - Every Python variable is available from every namespace	

<h2><center>After the midterm:</center></h2>

<h3><center> We will focus on the Python ecosystem, and applications of Python. </center></h3>

<h3><center> We also become a project based course. </center></h3>
