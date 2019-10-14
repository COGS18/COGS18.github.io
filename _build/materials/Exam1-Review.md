---
interact_link: content/materials/Exam1-Review.ipynb
download_link: assets/downloads/Exam1-Review.ipynb.zip
pdf_link: assets/pdf/Exam1-Review.pdf
layout: materials
title: 'Exam1-Review'
prev_page:
  url: /materials/A2-Examples
  title: 'A2-Examples'
next_page:
  url: /materials/Exam1-Practice
  title: 'Exam1-Practice'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Exam 1 Review

<h1 align="center">Exam #1 is Monday 10/21</h1>

## Midterm Expectations

You will be expected to: 

1. Recognize, understand and _respond_ to Python syntax:
    - statements & comments, whitespace, code blocks & indentation levels
2. Recognize, understand and be able to _explain_ code constructions:
    - variables, operators, data types, conditionals, loops
3. Know and be able to explain (roughly define) concepts we have talked about:
    - encodings
4. Be able to apply what you've learned:
    - Given a task:
        - what kind of code constructions are needed to answer it?
        - what kind of concepts does it relate to?
5. With respect to everything above, be able to read and respond to short code snippets and write out code.

### Midterm Mechanics

- Primarily short answers
- Also: multiple choice, true/false, etc.

#### The test is on paper.
- You _will_ be both writing and interpreting code
- You will _NOT_ be writing or debugging _large_ code sections on paper

### Reminder:

There are two extra notebooks that you can use for review:

1. [A1-Syntax](https://cogs18.github.io/materials/A1-Syntax/)
2. [A2-Examples](https://cogs18.github.io/materials/A2-Examples/)

There are also a few Exam #1 Practice Problems [here](https://cogs18.github.io/materials/Exam1-Practice).

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




{:.input_area}
```python
# Operators Question #3
2**2 + 2
```




{:.input_area}
```python
# Operators Question #4
'cogs' + '18'
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

