**Course Announcements**

Due Dates:
- Pre-course survey "due" tonight
- CL2 due Wednesday (11:59 PM)
- A1 due Monday (3/12, 11:59 PM)

**Q&A**

Q: What did `\` do inside of a string again?  
A: The backslash acts as an "escape" character. This means that whatever character follows after the backslash should be intererpeted as a "string literal." For example, if a quote is part of your string and you want to literally use a quotation mark (as a character, rather than to indicate the start or stop of a string), you could put `\"` within your string. This tells the computer to use the `"` as a character.

Q: You keep using underscores in your variable names...is that required?  
A: It's not required, but it is common in Python to use snake_case (all lower case, separate words with an `-`), so we'll use this throughout the course. You will be required to use this in your final exam/final project...but we'll discuss this explicitly when we talk about Code Style.

Q: Is there a back button?  
A: There is not a back button, but you can put your cursor within a cell and undo (ctrl/cmd + z)!

Q: How to handle data with integers and decimals?  
A: We'll get to this, but know for now that Python can work with both, but it will just convert everything to a float. If you want to specify the value to be an integer you would "typecast" (meaning specify the varaibles type) using `int(var_name)`, where `var_name` would be the variable you want to cast as an integer.

Q: What'st he difference between double quote and single quote in output?  
A: Nothing. They're equivalent.

Q: Can we put semicolons at the end of the line in python? Is that normal?  
A: While this is common and even required in some other programming languages, do your best to avoid doing it in Python. It's unecessary and makes your code less readable.

**A1: Clarification/Demo**

- variables created in `%%writefile` will be stored in file
- these variables will overwrite variables created in test cells

%%writefile new_file.py
# You can ignore the line above - it is used to help check your code

a = 3
b = 'new'
print(status)

status = False

%run -i new_file.py  
assert status == False

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

<div class="alert alert-success">
Python uses <code>=</code> for assignment.
</div>

my_var = 1

## Math Operators


- `+`, `-`, `*`, `/` for addition, subtraction, multiplication, & division
- `**` for exponentiation & `%` for modulus (remainder)
- `//` for floor division (integer division)

<div class="alert alert-success">
Python uses the <b>mathematical operators</b> <code>+</code>, <code>-</code>, <code>*</code>, <code>/</code> for 'sum', 'substract', 'multiply', and 'divide', repsectively.
</div>

print(2 + 3)

div_result = 4 / 2 
print(div_result)
type(div_result)

### Order of Operations

Mathematical operators follow the rules for order of operations.

- follow the rules for order of operations.
- parentheses specify which order you want to occur first

order_operations = 3 + 16 / 2
print(order_operations)

To specify that you want the addition to occur first, you would use parentheses.

specify_operations = (3 + 16) / 2
print(specify_operations)

#### Clicker Question #1

What would be the value stored in `my_value`? 

Note: Best to think about it before running the code to ensure you understand.

my_value = (3 + 2) + 16 / (4 / 2) 
my_value

- A) 7.0
- B) 10.5
- C) 13.0
- D) 20.0
- E) Produces an error

### More Math

<div class="alert alert-success">
Python also has <code>**</code> for exponentiation and <code>%</code> for remainder (called modulus). These also return numbers.
</div>

# 2 to the power 3
2 ** 3

# remainder of 17 divided by 7
17 % 7

#### Clicker Question #2

What would be the value stored in `remainder`?

remainder = 16 % 5
remainder

- A) 0
- B) 1
- C) 3
- D) 3.2
- E) Produces an error

#### Clicker Question #3

What would be the value stored in `modulo_time`?

modulo_time = 4 * 2 % 5
modulo_time

- A) 0
- B) 1
- C) 3
- D) 3.2
- E) Produces an error

## Remainder

How to get Python to tell you the integer and the remainder when dividing?

The way I first thought of involved a package and we haven't talked about those yet...

a = 17 // 7
b = 17 % 7

print(a, 'remainder', b)

`//` is an operator for floor division (integer division)

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

True and True

True or True

True and not False

not False

# two nots cancel one another out
not (not True)

### Capitalization matters

# this will give you an error
# 'TRUE' is not a boolean
# 'True' is
TRUE and TRUE

#### Clicker Question #4

How will the following boolean expression evaluate:

True and not False

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

a = 12
b = 13
a > b

True == True

True != False

'aa' == 'aa'

12 <= 13

#### Clicker Question #5

Assume you're writing a videogame that will only slay the dragon only if our magic lightsabre sword is charged to 90 or higher and we have 100 or more energy units in our protective shield. 


Start with the code in the following cell. Replace `---` with operators or values that will evaluate to `True` when the cell is run (and slay the dragon!).

- A) I did it!
- B) I tried but am stuck.
- C) I'm unsure where to start

## EDIT CODE HERE
sword_charge = 92
shield_energy = 100

(sword_charge >= 90) and (shield_energy >= 100)

## Understanding Boolean logic

When first learning booleans, we sometimes *think* we know what we're asking the computer to do, but our logic can be flawed.

Let's look at an example that could trip you up now.


1. Python considers empty strings as having boolean value of `False`. Non-empty string as having boolean value of `True`.


empty_string = ''
bool(empty_string)

nonempty_string = 'string has something in it'
bool(nonempty_string)

2.  For `and` operator if left value is `True`, then right value is checked and returned. If left value is `False`, then that left value is returned.


True and False

bool('a')

'a' and 'b'

'b' and 'a'

#### Clicker Question #6

What would the following code cell return?

'' and 'a'

- A) ''
- B) 'a'
- C) `True`
- D) `False`

# the left value in parentheses evaluates as True
'a' == ('b' and 'a')

# the left value in parentheses evaluates as True
'a' == ('a' and 'b')

# the left value in parentheses evaluates as False
'a' == ('' and 'a')

# what we actually wanted python to do
# to look at a in a and b
'a' == 'a' and 'a' == 'b' 

3. For `or` operator if left value is `True`, then it is returned, otherwise if left value is `False`, then right value is returned.

'a' or 'b'

# empty string evaluates as False
'' or 'b'

'a' == ('a' or 'b')

'b' == ('a' or 'b')

'b' == 'a' or 'b' == 'b'

#### Clicker Question #7

What would the following code cell return?

'a' == ('' or 'a')

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

a = 927
b = a
c = 927

print(a is b)
print(c is a)

 Two variables that are equal does **not** imply that they are identical.

If we wanted that second statement to evaluate as `True` we could use `is not`...

# make a True statement
print(c is not a)

# testing for value equality
a == b == c

#### Clicker Question #8


Using the variables provded below and identity operators replace `---` with code such that `true_variable` will return `True` and `false_variable` will return `False`. 


- A) I did it!
- B) I tried but am stuck.
- C) I'm unsure where to start

z = 5
x = '5'
c = 'Hello'
d = c
e = [1, 2, 3]
f = [1, 2, 3]

# EDIT CODE HERE
true_variable = c is d
false_variable = z is x

print(true_variable, false_variable)

### Delving Deeper: Identity Operators

A **new object** is created each time we have a variable that makes reference to it, but there are *few notable exceptions*:

- some simple strings
- Integers between -5 and 256 (inclusive)
- empty immutable containers (e.g. tuples) - we'll get to these later

While these may *seem* random, they exist for memory optimization in Python implementation. 

Shorter and less complex strings are "interned" (share the same space in memory).

The rules behind this are a bit fuzzy, so we'll just go through a few examples here. But, if you want to read more about string interning and how Python handles this, you can read more [here](http://guilload.com/python-string-interning/).

simple_string = 'string'
simple_string2 = 'string'

simple_string is simple_string2

print(id(simple_string), id(simple_string2))

longer_string = 'really long string that just keeps going'
longer_string2 = 'really long string that just keeps going'

longer_string is longer_string2

print(id(longer_string), id(longer_string2))

d = 5
e = 5

print(id(d), id(e))

print(d is e)

Python implementation front loads an array of integers between -5 to 256, so these objects *already exist*.

# Python doesn't create a new object here
j = 5
k = 5
l = 'Hello'
m = 'Hello'

true_variable_integer = j is k
true_variable_string = l is m

print(true_variable_integer, true_variable_string)

# Python DOES create a new object here
n = 975 #greater than 256
o = 975
p = 'Hello!' #that exclamation point makes it more complex
q = 'Hello!'

false_variable_integer = n is o
false_variable_string = p is q

print(false_variable_integer, false_variable_string)

#### Clicker Question #9

Using the variables provded below and identity operators replace `---` with code such that `true_variable` will return `True` and `false_variable` will return `False`. 

- A) I did it!
- B) I tried but am stuck.
- C) I'm unsure where to start

# equality (values are the same)
f == g

# identity (place in memory)
f is g

a = 5
b = 5
c = b
d = 'Hello!'
e = 'Hello!'
f = 567
g = 567

# EDIT CODE HERE
true_variable = a is c
false_variable = f is g

print(true_variable, false_variable)

## Membership Operators

<div class="alert alert-success">
Python uses <code>in</code> and <code>not in</code> to compare membership. These operators return booleans.
</div>

Membership operators are used to check whether a value or variable is found in a sequence.

Here, we'll just be checking for value membership in strings. But, we'll discuss lists, tuples, sets, and dictionaries soon.

- `in` : True if value is found in the sequence
- `not in` : True if value is not found in the sequence

x = 'I love COGS18!'
print('l' in x)

print('L' in x)

print('COGS' in x)

print('CSOG' in x)

print(' ' in x)

## String Concatenation

<div class="alert alert-success">
Operators sometimes do different things on different types of variables. For example, <code>+</code> on strings does concatenation.
</div>

a = 'COGS'
b = '18'

a + ' ' + b

'COGS' + ' 18'

'a' + 'b' + 'c'

## Chaining Operators

<div class="alert alert-success">
Operators and variables can also be chained together into arbitrarily complex expressions.
</div>

# Note that you can use parentheses to chunk sections
(13 % 7 >= 7) and ('COGS' + '18' == 'COGS18')

(13 % 7 >= 7)

('COGS' + '18' == 'COGS18')

#### Clicker Question #10

How will the following expression evaluate:

2**2 >= 4 and 13%3 > 1

2**2 >= 4

13%3

- a) True
- b) False
- c) None
- d) This code will fail