# Exam 1 Review

**Exam 1 Topics**
- Q0: Honor Code (0.1 points)
- Variables & Operators (3.75 points)
    - Q1: Variables
    - Q2: Math Operators
    - Q3: Comparison Operators
    - Q4: Membership Operators
    - Q5: String Concatenation
- Collections & Indexing (3 points)
    - Q6: Lists & Indexing
    - Q7: Dictionaries & Tuples
- Control Flow - Conditionals & Loops (5.65 points)
    - Q8: Conditionals
    - Q9: `for` loop
    - Q10: Accomplishing a task

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

### Reminder: 

There are two extra notebooks that you can use for review:

1. [A1-Syntax](https://cogs18.github.io/materials/A1-Syntax/)
2. [A2-Examples](https://cogs18.github.io/materials/A2-Examples/)

There are also a few Exam #1 Practice Problems [here](https://cogs18.github.io/exams/Exam1-Practice).

And, there is a practice Exam on datahub.

## Topics & Example Questions

- Variables & Data Types
- Operators
- Conditionals
- Loops

Note: The questions below are _less_ involved than the questions on your midterm. These are meant to help guide your studying. If you're stuck on one of these, you know where to focus your studying.

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

Create a variable `oper_var` that uses both the not and or operators (each at least once) such that `oper_var` stores (returns) the value `True`.

#### Operators Question #3

Using at least 4 different math operators, create a variable `math_var` that stores (returns) the value '18' (or 18.0)

#### Operators Question #4

Create a variable `string_concat` that demonstrates how you can concatenate two different strings together with a space between the two different strings. 

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

#### Conditionals Question #2

You use have a list that stores 20 different integers. You use a comparison operator to compare the relationship between two of the elements in the list and store that output in a variable. What would the type of that output variable be?

### Loops

- loops: `for` and `while`
    - `continue`, `break`, `pass`

#### Loops Question #1
What are the two kinds of loops? ____________ and ____________

#### Loops Question #2
Use the following:
`ind = 1` to write a loop (using real Python code) that would loop and print the value `ind` of ind each time through the loop _and_ update the value of ind by 1. Have this loop stop after 4 iterations. 

#### Loops Question #3

Create a list that stores each letter of your favorite animal as a different element in a list. Store that in the variable `fav_pet`. 

Initialize an additional variable called `reverse_pet` that will store an empty string to start.

Then, using indexing, loop through each letter in that list such that `reverse_pet` stores a list with your favorite pet spelled backward.

For example, if your favorite pet were "cat", the output stored in `reverse_pet` should be: `['t', 'a', 'c']`
