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
  url: /materials/05-Conditionals
  title: '05-Conditionals'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Course Announcements

- A1 is due Friday (10/11)
    - We have not yet covered all content on assignment
    - Just an FYI: A2 is more difficult than A1
- Coding Labs
    - must attend 6/9 weeks
    - "answers" posted the following week to website
    - check your work
- I'll post updated iclicker and coding lab attendance weekly
- survey follow-up

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

### Order of Operations

Mathematical operators follow the rules for order of operations.

- follow the rules for order of operations.
- parentheses specify which order you want to occur first



{:.input_area}
```python
order_operations = 3 + 16 / 2
print(order_operations)
```


{:.output_stream}
```
11.0

```

To specify that you want the addition to occur first, you would use parentheses.



{:.input_area}
```python
specify_operations = (3 + 16) / 2
print(specify_operations)
```


### Clicker #1

What would be the value stored in `my_value`?



{:.input_area}
```python
my_value = (3 + 2) + 2 / (16/2)
my_value
```


- A) 0.218
- B) 0.875
- C) 5.25
- D) 40
- E) Produces an error

### More Math

<div class="alert alert-success">
Python also has <code>**</code> for exponentiation and <code>%</code> for remainder (called modulus). These also return numbers.
</div>



{:.input_area}
```python
# 2 to the power 3
2 ** 3
```




{:.input_area}
```python
# remainder of 17 divided by 7
17 % 7
```


### Clicker #2

What would be the value stored in `remainder`?



{:.input_area}
```python
remainder = 16 % 5
remainder
```


- A) 0
- B) 1
- C) 3
- D) 3.2
- E) Produces an error

### Clicker #3

What would be the value stored in `modulo_time`?



{:.input_area}
```python
modulo_time = 4 * 2 % 5
modulo_time
```


- A) 0
- B) 1
- C) 3
- D) 3.2
- E) Produces an error

## Remainder

How to get Python to tell you the integer and the remainder when dividing?

The way I first thought of involved a package and we haven't talked about those yet...



{:.input_area}
```python
a = 17 // 7
b = 17 % 7

print(a, 'remainder', b)
```


{:.output_stream}
```
2 remainder 3

```

`//` is an operator for floor division (integer division)

### Clicker #4

What value is stored in `math_out` from the code below?



{:.input_area}
```python
math_out = 32 / (1 + 3) ** 2 
math_out
```





{:.output_data_text}
```
2.0
```



- A) 2
- B) 16
- C) 64
- D) This code will fail

## Logical (Boolean) operators
- use Boolean logic
- logical operators: `and`, `or`, and `not`

Booleans are named after the British mathematician - George Boole. He first formulated Boolean algebra, which are a set of rules for how to reason with and combine these values. This is the basis of all modern computer logic.

<div class="alert alert-success">
Python has <code>and</code>, <code>or</code> and <code>not</code> for boolean logic. These operators return booleans.
</div>

- `and` : True if both are true
- `or` : True if at least one is true
- `not` : True only if false



{:.input_area}
```python
True and True
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
True or True
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
True and not False
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
not False
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
# two nots cancel one another out
not (not True)
```





{:.output_data_text}
```
True
```



### Capitalization matters



{:.input_area}
```python
# this will give you an error
# 'TRUE' is not a boolean
# 'True' is
TRUE and TRUE
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
NameError                                 Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-9-9b3f2ee967bc> in <module>()
      2 # 'TRUE' is not a boolean
      3 # 'True' is
----> 4 TRUE and TRUE

```

{:.output_traceback_line}
```
NameError: name 'TRUE' is not defined
```


### Clicker #5

What will the following boolean expression evaluate as:



{:.input_area}
```python
True and False
```





{:.output_data_text}
```
False
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





{:.output_data_text}
```
False
```





{:.input_area}
```python
# Continues to evaluate the expression
True and print("Hi")
```


{:.output_stream}
```
Hi

```



{:.input_area}
```python
# evaluates print statement before and
print("Hi") and False
```


{:.output_stream}
```
Hi

```

### Clicker #6

What will the following boolean expression evaluate as?



{:.input_area}
```python
True and not True or False
```





{:.output_data_text}
```
False
```



- A) True
- B) False
- C) None
- D) This code will fail

### Clicker #7

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
Python has comparison operators <code>==</code>, <code>!=</code>, <code><</code>, <code>></code>, <code><=</code>, and <code>>=</code> for value comparisons. These operators return booleans.
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





{:.output_data_text}
```
True
```





{:.input_area}
```python
True != False
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
'aa' == 'aa'
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
12 <= 13
```





{:.output_data_text}
```
True
```



### Clicker #8

Assume you're writing a videogame that will only slay the dragon only if our magic lightsabre sword is charged to 90 or higher and we have 100 or more energy units in our protective shield. 


Start with the code in the following cell. Replace `---` with values that will evaluate to `True` when the cell is run (and slay the dragon!).

- A) I did it!
- B) I tried but am stuck.
- C) I'm unsure where to start



{:.input_area}
```python
## EDIT CODE HERE
sword_charge = 95
shield_energy = 100

(sword_charge >= 90) and (shield_energy >= 100)
```





{:.output_data_text}
```
True
```



## Understanding Boolean logic

When first learning booleans, we sometimes *think* we know what we're asking the computer to do, but our logic can be flawed.

Let's look at an example that could trip you up now.


1. Python considers empty strings as having boolean value of `False`. Non-empty string as having boolean value of `True`.




{:.input_area}
```python
empty_string = ''
bool(empty_string)
```





{:.output_data_text}
```
False
```





{:.input_area}
```python
nonempty_string = 'string has something in it'
bool(nonempty_string)
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
bool(None)
```


2.  For `and` operator if left value is `True`, then right value is checked and returned. If left value is `False`, then that left value is returned.




{:.input_area}
```python
True and False
```





{:.output_data_text}
```
False
```





{:.input_area}
```python
bool('a')
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
'a' and 'b'
```





{:.output_data_text}
```
'b'
```





{:.input_area}
```python
'b' and 'a'
```





{:.output_data_text}
```
'a'
```



### Clicker Question #9

What would the following code cell return?



{:.input_area}
```python
'' and 'a'
```





{:.output_data_text}
```
''
```



- A) ''
- B) 'a'
- C) `True`
- D) `False`



{:.input_area}
```python
# the left value in parentheses is True
'a' == ('b' and 'a')
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
'b' and 'a'
```





{:.output_data_text}
```
'a'
```





{:.input_area}
```python
'a' and 'b'
```





{:.output_data_text}
```
'b'
```





{:.input_area}
```python
# the left value in parentheses is True
'a' == ('a' and 'b')
```





{:.output_data_text}
```
False
```





{:.input_area}
```python
# the left value in parentheses is False
'a' == ('' and 'a')
```





{:.output_data_text}
```
False
```





{:.input_area}
```python
# what we actually wanted python to do
# to look at a in a and b
'a' == 'a' and 'a' == 'b' 
```





{:.output_data_text}
```
False
```



3. For `or` operator if left value is `True`, then it is returned, otherwise if left value is `False`, then right value is returned.



{:.input_area}
```python
'a' or 'b'
```





{:.output_data_text}
```
'a'
```





{:.input_area}
```python
# empty string evaluates as False
'' or 'b'
```





{:.output_data_text}
```
'b'
```





{:.input_area}
```python
'' or 'b'
```





{:.output_data_text}
```
'b'
```





{:.input_area}
```python
'' or ''
```





{:.output_data_text}
```
''
```





{:.input_area}
```python
'b' or ''
```





{:.output_data_text}
```
'b'
```





{:.input_area}
```python
'a' == ('a' or 'b')
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
'b' == ('a' or 'b')
```





{:.output_data_text}
```
False
```



### Clicker Question #10

What would the following code cell return?



{:.input_area}
```python
'a' == ('' or 'a')
```





{:.output_data_text}
```
True
```



- A) ''
- B) 'a'
- C) `True`
- D) `False`

## Identity Operators

 Identity operators are used to check if two values (or variables) are located on the same part of the memory.

<div class="alert alert-success">
Python uses <code>is</code> and <code>is not</code> to compare identity. These operators return booleans.
</div>

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


{:.output_stream}
```
True
False

```

 Two variables that are equal does **not** imply that they are identical.

If we wanted that second statement to evaluate as `True` we could use `is not`...



{:.input_area}
```python
# make a True statement
print(c is not a)
```


{:.output_stream}
```
True

```



{:.input_area}
```python
# testing for value equality
a == b == c
```





{:.output_data_text}
```
True
```



### Clicker #11


Using the variables provded below and identity operators replace `---` with code such that `true_variable` will return `True` and `false_variable` will return `False`. 


- A) I did it!
- B) I tried but am stuck.
- C) I'm unsure where to start



{:.input_area}
```python
z = 5
x = '5'
c = 'Hello'
d = c
e = [1, 2, 3]
f = [1, 2, 3]

# EDIT CODE HERE
true_variable = c is d 
false_variable = c is not d

print(true_variable, false_variable)
```


{:.output_stream}
```
True False

```

### Delving Deeper: Identity Operators

A **new object** is created each time we have a variable that makes reference to it, but there are *few notable exceptions*:

- some simple strings
- Integers between -5 and 256 (inclusive)
- empty immutable containers (e.g. tuples) - we'll get to these later

While these may *seem* random, they exist for memory optimization in Python implementation. 

Shorter and less complex strings are "interned" (share the same space in memory).

The rules behind this are a bit fuzzy, so we'll just go through a few examples here. But, if you want to read more about string interning and how Python handles this, you can read more [here](http://guilload.com/python-string-interning/).



{:.input_area}
```python
simple_string = 'string'
simple_string2 = 'string'
```




{:.input_area}
```python
simple_string is simple_string2
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
print(id(simple_string), id(simple_string2))
```


{:.output_stream}
```
4535947872 4535947872

```



{:.input_area}
```python
longer_string = 'really long string that just keeps going'
longer_string2 = 'really long string that just keeps going'
```




{:.input_area}
```python
longer_string is longer_string2
```





{:.output_data_text}
```
False
```





{:.input_area}
```python
print(id(longer_string), id(longer_string2))
```


{:.output_stream}
```
4572797424 4572798480

```



{:.input_area}
```python
d = 5
e = 5
```




{:.input_area}
```python
print(id(d), id(e))
```


{:.output_stream}
```
4533003824 4533003824

```



{:.input_area}
```python
print(d is e)
```


{:.output_stream}
```
True

```

Python implementation front loads an array of integers between -5 to 256, so these objects *already exist*.



{:.input_area}
```python
# Python doesn't create a new object here
j = 5
k = 5
l = 'Hello'
m = 'Hello'

true_variable_integer = j is k
true_variable_string = l is m

print(true_variable_integer, true_variable_string)
```


{:.output_stream}
```
True True

```



{:.input_area}
```python
# Python DOES create a new object here
n = 975 #greater than 256
o = 975
p = 'Hello!' #that exclamation point makes it more complex
q = 'Hello!'

false_variable_integer = n is o
false_variable_string = p is q

print(false_variable_integer, false_variable_string)
```


{:.output_stream}
```
False False

```

### Clicker #12


Using the variables provded below and identity operators replace `---` with code such that `true_variable` will return `True` and `false_variable` will return `False`. 

- A) I did it!
- B) I tried but am stuck.
- C) I'm unsure where to start



{:.input_area}
```python
a = 5
b = 5
c = b
d = 'Hello!'
e = 'Hello!'
f = 567
g = 567

# EDIT CODE HERE
true_variable = a is c
false_variable = d is e

print(true_variable, false_variable)
```


{:.output_stream}
```
True False

```

## Membership Operators

<div class="alert alert-success">
Python uses <code>in</code> and <code>not in</code> to compare membership. These operators return booleans.
</div>

Membership operators are used to check whether a value or variable is found in a sequence.

Here, we'll just be checking for value membership in strings. But, we'll discuss lists, tuples, sets, and dictionaries soon.

- `in` : True if value is found in the sequence
- `not in` : True if value is not found in the sequence



{:.input_area}
```python
x = 'I love COGS18!'
print('l' in x)
```


{:.output_stream}
```
True

```



{:.input_area}
```python
print('L' in x)
```


{:.output_stream}
```
False

```



{:.input_area}
```python
print('COGS' in x)
```


{:.output_stream}
```
True

```



{:.input_area}
```python
print('CSOG' in x)
```


{:.output_stream}
```
False

```



{:.input_area}
```python
print(' ' in x)
```


{:.output_stream}
```
True

```

## String Concatenation

<div class="alert alert-success">
Operators sometimes do different things on different types of variables. For example, <code>+</code> on strings does concatenation.
</div>



{:.input_area}
```python
'a' + 'b' + 'c'
```





{:.output_data_text}
```
'abc'
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





{:.output_data_text}
```
False
```





{:.input_area}
```python
(13 % 7 >= 7)
```





{:.output_data_text}
```
False
```





{:.input_area}
```python
('COGS' + '18' == 'COGS18')
```





{:.output_data_text}
```
True
```



### Clicker #13

What will the following expression evaluate as:



{:.input_area}
```python
2**2 >= 4 and 13%3 > 1
```





{:.output_data_text}
```
False
```



- a) True
- b) False
- c) None
- d) This code will fail
