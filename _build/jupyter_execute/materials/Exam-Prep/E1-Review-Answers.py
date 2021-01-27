# Exam 1 Review (Answers)

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

1. [A1-Syntax](https://cogs18.github.io/materials/A1-Syntax.html)
2. [A2-Examples](https://cogs18.github.io/materials/A2-Examples.html)

There are also a few Exam #1 Practice Problems [here](https://cogs18.github.io/materials/Exam-Prep/E1-Review.html).

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

What is the difference between a tuple, a dictionary, and a list?

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

Tuples are created with () and are immutable; store single elements of mixed types.  
Lists are created with [] and are mutable; store single elements of mixed types.
Dictionaries are created with {} and are mutable; store elements as key-value pairs; can be of mixed types.

# Data Types Question #2
ice_cream = ['vanilla', 'chocolate', 'strawberry', 'cherry', 'salted caramel']
print(ice_cream[-5:-2])
print(ice_cream[:3])
ice_cream[0:3]

# Data Types Question #3
my_list[2] = 12 

# Data Types Question #3
my_list = [1, 2 , 3, 4, 5, 6]
my_list[2] = 12
my_list

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

Create a variable `oper_var` that uses both the `not` and `or` operators (each at least once) such that `oper_var` stores (returns) the value `True`.

#### Operators Question #3

Using at least 4 different math operators, create a variable `math_var` that stores (returns) the value '18' (or 18.0)

#### Operators Question #4

Create a variable `string_concat` that demonstrates how you can concatenate two different strings together with a space between the two different strings. 

#### Operators Answers

Operators Question #1

= is an assignment operator  
== checks for equality

# Operators Question #2

# one possible answer
# a = not False
# b = not True
# open_var = a or b

# OR
open_var = not False or not True
print(open_var)

# Operators Question #3
# one possible answer to get to 18
math_var =   36 // ((((2 + 3) * 2) / 2) - 3)
math_var 

# Operators Question #4
# possible answer

string_concat = 'COGS' + ' ' + '18'
print(string_concat)
# OR
a = 'COGS'
b = '18'
string_concat = a + ' ' + b
print(string_concat)

string_concat = 'COGS ' + '18'
print(string_concat)

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
2. If `COND_A` is `False` and `COND_B` is `True`, which code block(s) evaluate?

#### Conditionals Question #3

You use have a list that stores 20 different integers. You use a comparison operator to compare the relationship between two of the elements in the list and store that output in a variable. What would the type of that output variable be?

#### Conditionals Answers

Conditionals Question #1

necessary, optional, optional

Conditionals Question #2

1. Code Block A
2. Code Block B

###### how to check your thinking when you're studying
COND_A = True
COND_B = True

if COND_A:
    print('a')
elif COND_B:
    print('b')
else:
    print('c')

Conditionals Question #3

A Boolean

# Example code to demonstrate:
test_list = range(0,21)

# test 1
out = test_list[1] != test_list[2]
print(type(out))

# test 2
out = test_list[17] <= test_list[15]
print(type(out))

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


#### Loops Answers

Loops Question #1

for and while

# Loops Question #2
ind = 1

while ind <= 4:
    print(ind)
    ind += 1
    #or ind = ind + 1

# Loops Question #3

fav_pet = ['p', 'u', 'p', 'p', 'y']

reverse_pet = []
for letter in fav_pet[::-1]:
    reverse_pet.append(letter)

#OR
reverse_pet = []
for letter in [fav_pet[4], fav_pet[3], fav_pet[2], fav_pet[1], fav_pet[0]]:
    reverse_pet.append(letter)

#OR

reverse_pet = []
for letter in [fav_pet[-1], fav_pet[-2], fav_pet[-3], fav_pet[-4], fav_pet[-5]]:
    reverse_pet.append(letter)
    
print(reverse_pet)