---
interact_link: content/materials/04-Operators.ipynb
download_link: assets/downloads/04-Operators.ipynb.zip
pdf_link: assets/pdf/04-Operators.pdf
layout: materials
title: '04-Operators'
prev_page:
  url: /materials/03-Variables
  title: '03-Variables'
next_page:
  url: /labs/CL1-ProgrammingI
  title: 'Coding Labs'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Operators

- assignment
- math
- logic
- comparison
- identity
- membership

<div class="alert alert-success">
Operators are special symbols in Python that carry out arithmetic or logical computation.
</div>

## Assignment Operator

- `=` for assignment

There are additional assignment operators in Python, but this is the one you will use *all the time*, so we'll stick to this for now.

## Math Operators


- `+`, `-`, `*`, `/` for addition, subtraction, multiplication, & division
- `**` for exponentiation & `%` for modulus (remainder)
- `//` for floor division (integer division)

- follow the rules for order of operations.
- parentheses specify which order you want to occur first

## Remainder

How to get Python to tell you the integer and the remainder when dividing?

The way I first thought of involved a package and we haven't talked about those yet...



{:.input_area}
```python
a = 17 // 7
b = 17 % 7

print(a, 'remainder', b)
```


`//` is an operator for floor division (integer division)

### Clicker #1

What value is stored in `math_out` from the code below?



{:.input_area}
```python
math_out = 32 / (1 + 3) ** 2 
```


- A) 8
- B) 16
- C) 64
- D) This code will fail

## Logical (Boolean) operators
- use Boolean logic
- logical operators: `and`, `or`, and `not`

Booleans are named after the British mathematician - George Boole. He first formulated Boolean algebra, which are a set of rules for how to reason with and combine these values. This is the basis of all modern computer logic.

<div class="alert alert-success">
Python has `and`, `or` and `not` for boolean logic. These operators return booleans.
</div>

- `and` : True if both are true
- `or` : True if at least one is true
- `not` : True only if false



{:.input_area}
```python
True and True
```




{:.input_area}
```python
True or True
```




{:.input_area}
```python
True and not False
```




{:.input_area}
```python
not False
```




{:.input_area}
```python
# two nots cancel one another out
not (not True)
```


### Capitalization matters



{:.input_area}
```python
# this will give you an error
# 'TRUE' is not a boolean
# 'True' is
TRUE and TRUE
```


### Clicker #2

What will the following boolean expression evaluate as:



{:.input_area}
```python
True and False
```


- A) True
- B) False
- C) None
- D) This code will fail

### Short-circuit evaluation

The second argument is evaluated only if the first argument does not definitively determine the value of the expression.



{:.input_area}
```python
# python stops after False
# no need to check second expression
# since first is False
False and print("Hi")
```




{:.input_area}
```python
# Continues to evaluate the expression
True and print("Hi")
```


### Clicker #3

What will the following boolean expression evaluate as?



{:.input_area}
```python
True and not True or False
```


- A) True
- B) False
- C) None
- D) This code will fail

### Clicker #4

What will the following boolean expression evaluate as:



{:.input_area}
```python
True and not False
```


- A) True
- B) False
- C) None
- D) This code will fail

## Comparison Operators

<div class="alert alert-success">
Python has comparison operators `==`, `!=`, `<`, `>`, `<=`, and `>=` for value comparisons. These operators return booleans.
</div>

- `==` : values are equal
- `!=` : values are not equal
- `<` : value on left is less than value or right
- `>` : value on left is greater than value on right
- `<=` : value on left is less than *or equal to* value on right
- `>=` : value on left is greater than or equal to value on the right



{:.input_area}
```python
True == True
```




{:.input_area}
```python
True != False
```




{:.input_area}
```python
'aa' == 'aa'
```




{:.input_area}
```python
13 >= 12
```


### Clicker #5

Assume you're writing a videogame that will only slay the dragon only if our magic lightsabre sword is charged to 90% or higher and we have 100 or more energy units in our protective shield. 


Start with the code in the following cell. Replace `---` with values that will evaluate to `True` when the cell is run (and slay the dragon!).

- A) I did it!
- B) I tried but am stuck.
- C) I'm unsure where to start



{:.input_area}
```python
## EDIT CODE HERE
sword_charge = ---
shield_energy = ---

(sword_charge --- ---) and (shield_energy --- ---)
```


## Identity Operators

<div class="alert alert-success">
Python uses `is` and `is not` to compare identity. These operators return booleans.
</div>

 Identity operators are used to check if two values (or variables) are located on the same part of the memory.

- `is` : True if both refer to the same object
- `is not` : True if they do not refer to the same object



{:.input_area}
```python
a = 927
b = a
c = 927
```




{:.input_area}
```python
print(a is b)
print(c is a)
```


 Two variables that are equal does **not** imply that they are identical.

If we wanted that second statement to evaluate as `True` we could use `is not`...



{:.input_area}
```python
print(c is not a)
```




{:.input_area}
```python
a == b == c
```


### Clicker #6


Using the variables provded below and identity operators replace `---` with code such that `true_variable` will return `True` and `false_variable` will return `False`. 


- A) I did it!
- B) I tried but am stuck.
- C) I'm unsure where to start



{:.input_area}
```python
a = 5
b = 5
c = 'Hello'
d = c
e = [1,2,3]
f = [1,2,3]

# EDIT CODE HERE
true_variable = ---
false_variable = ---

print(true_variable, false_variable)
```


## Membership Operators

<div class="alert alert-success">
Python uses `in` and `not in` to compare membership. These operators return booleans.
</div>

Membership operators are used to check whether a value or variable is found in a sequence.

Here, we'll just be checking for value membership in strings. But, we'll discuss lists, tuples, sets, and dictionaries soon.

- `in` : True if value is found in the sequence
- `is not` : True if value is not found in the sequence



{:.input_area}
```python
x = 'I love COGS18!'
print('l' in x)
```




{:.input_area}
```python
print('L' in x)
```




{:.input_area}
```python
print('COGS' in x)
```




{:.input_area}
```python
print('CSOG' in x)
```


## String Concatenation

<div class="alert alert-success">
Operators sometimes do different things on different types of variables. For example, `+` on strings does concatenation.
</div>



{:.input_area}
```python
'a' + 'b' + 'c'
```


## Chaining Operators

<div class="alert alert-success">
Operators and variables can also be chained together into arbitrarily complex expressions.
</div>



{:.input_area}
```python
# Note that you can use parentheses to chunk sections
(13 % 7 >= 7) and ('COGS' + '18' == 'COGS18')
```




{:.input_area}
```python
(13 % 7 >= 7)
```




{:.input_area}
```python
('COGS' + '18' == 'COGS18')
```


### Clicker #7

What will the following expression evaluate as:



{:.input_area}
```python
2**2 >= 4 and 13%3 > 1
```


- a) True
- b) False
- c) None
- d) This code will fail

## Understanding Boolean logic

When first learning booleans, we sometimes *think* we know what we're asking the computer to do, but our logic can be flawed.

Let's look at an example that could trip you up now.




{:.input_area}
```python
'a' == ('a' or 'b')
```




{:.input_area}
```python
'b' == ('a' or 'b')
```


### Clicker #8


What would the code below return?



{:.input_area}
```python
'a' == ('a' and 'b')
```


- A) True
- B) False
- C) None 
- D) 'a'
- E) I'm really not sure



{:.input_area}
```python
'a' == ('b' and 'a')
```




{:.input_area}
```python
# what we actually wanted python to do
# to look at a in a or b
'a' == 'a' or 'a' == 'b' 
```




{:.input_area}
```python
# how we'd specify to python to see 
# if a was in a and b
'a' == 'a' and 'a' == 'b' 
```


# Conditionals

- `if`
- `elif`
- `else`

## Conditionals: if

<div class="alert alert-success">
Conditionals are statements that check for a condition, using the `if` statement, and then only execute a set of code if the condition evaluates as `True`.
</div>



{:.input_area}
```python
condition = True

if condition:
    print('This code executes if the condition evaluates as True.')
```


## Conditional: else

<div class="alert alert-success">
After an `if`, you can use an `else` that will run if the conditional(s) above have not run.
</div>



{:.input_area}
```python
condition = True

if condition:
    print('This code executes if the condition evaluates as True.')
else: 
    print('This code executes if the condition evaluates as False')
```


## Conditional: elif

<div class="alert alert-success">
After an `if` statement, you can have any number of `elif`'s (meaning 'else if') to check other conditions.
</div>



{:.input_area}
```python
condition_1 = False
condition_2 = False

if condition_1:
    print('This code executes if condition_1 evaluates as True.')
elif condition_2:
    print('This code executes if condition_1 did not evaluate as True, but condition_2 does.')
else: 
    print('This code executes if both condition_1 and condition_2 evaluate as False')
```


## Conditionals With Value Comparisons

<div class="alert alert-success">
Any expression that can be evaluated as a boolean, such as value comparisons, can be used with conditionals.
</div>



{:.input_area}
```python
language = "Python"

if language == "Python":
    print("Yay!")
elif language == "Perl":
    print("Oh no.")
else:
    print("Get yourself a programming language!")
```

