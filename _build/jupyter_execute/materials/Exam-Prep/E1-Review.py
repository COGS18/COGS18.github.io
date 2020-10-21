**Course Announcements**

- **Coding Lab** due tonight (11:59 PM)
- **A2** *really* due Thursday (11:59 PM)
- **Exam I** Friday
    - Fetch, complete and submit on Datahub
    - *No lecture or office hours this Friday*
- **A3** not due until Mon 11/2

Notes:
- CL2 scores posted on Canvas
- A1 feedback (w/ score) now available on datahub (Canvas scores coming shortly; Avg: 7.57/8)
- Zoom Link for Thursday 4PM internship chat w/ Weilun is on Canvas Homepage (at bottom of table)

# Exam 1 Review

**Exam 1 Topics**

- Variables & Operators (4 points)
    - Q1: Variables
    - Q2: Math Operators
    - Q3: Comparison Operators
    - Q4: Variables
- Collections & Indexing (3 points)
    - Q5: Lists & Indexing
    - Q6: Dictionaries
- Control Flow - Conditionals & Loops (5.5 points)
    - Q7: Conditionals
    - Q8: `for` loop
    - Q9: Completing a task

## Suggested Study Steps

1. Use/skim A1-Syntax, A2-Examples, Exam1-Review and Exam1-Practice to gain additional practice and identify points of confusion
2. Use notes, coding labs, and assignments to review topics of confusion. Re-do questions that previously tripped you up.
3. Return to Exam1-Review and Exam1-Practice to ensure you understand what you did not previously understand.
4. Complete practice exam on datahub

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

# review of slices (related concept: indexing)

my_list = ['a', 'b', 'c', 'd', 'e']
print(len(my_list))

# indexing
print(my_list[1])

# slicing - portion of the larger collection [start:stop:step]
print(my_list[1:4])
print(my_list[1:4:2])

# every other value starting at 1; stop & not include 20
range(1,20,2)

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
