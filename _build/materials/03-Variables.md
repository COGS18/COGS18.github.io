---
interact_link: content/materials/03-Variables.ipynb
download_link: assets/downloads/03-Variables.ipynb.zip
pdf_link: assets/pdf/03-Variables.pdf
layout: materials
title: '03-Variables'
prev_page:
  url: /materials/02-JupyterNotebooks
  title: '02-JupyterNotebooks'
next_page:
  url: /
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<div class="alert alert-danger">
  <strong>Reminder:</strong> All lectures for COGS 18 are being recorded.
</div>

# Course Announcements

- Coding Labs are due Wednesdays
    - For Week 1 only: if you didn't submit, submit by tonight (Fri at 11:59 PM)
- A1 is due Mon of Week 3 (4/13)
    - We have not yet covered all content on assignment
- Course survey "due" tonight at 11:59 PM

### Course Materials

- [Website](https://cogs18.github.io/) + [Syllabus](https://cogs18.github.io/assets/intro/syllabus.pdf)
- [Canvas](https://canvas.ucsd.edu/courses/12653)

## Working with Variables



{:.input_area}
```python
a = 6
```




{:.input_area}
```python
a = 'string'
```




{:.input_area}
```python
print(a)
```


#### Clicker Question #1

**What is the value of `a`?**

- A) 6
- B) 'string'
- C) '6'
- D) 6 + 'string' 



{:.input_area}
```python
a = 6 
```




{:.input_area}
```python
print(a)
```


#### Clicker Question #2

**What is the value of `a`?**

- A) 6
- B) 'string'
- C) '6'
- D) 6 + 'string' 

## Programming With Python

Programming: a way to ask computer to store values (variables), and do things with them (operations).`



{:.input_area}
```python
# This is a comment. You can write a comment by using a `#`
my_variable = 12 

my_other_variable = 13 # Comments can be 'inline', like this one
```


### Defining Variables

<div class="alert alert-success">
In programming, variables are things that store values. Variables are defined with `name = value`.
</div>



{:.input_area}
```python
my_var = 1  # `my_var` is a variable

# This defines another variable
other_var = 'variables are cool'

```




{:.input_area}
```python
# once you create a variable it's stored in your namespace
my_variable

```


## Code Variables != Math Variables

In mathematics: `=` refers to equality (as a statement of truth).

In coding: `=` refers to assignment. 

Math: What is x?

y = 10x + 2

Code: What is x?

`x = x + 1`

#### Clicker Question #3

After executing the following code, what will be the value of `my_var`?



{:.input_area}
```python
my_var = 2 

my_var = my_var + 1

print(my_var)
```


- A) 2
- B) 3
- C) "my_var + 1"
- D) This code will fail

#### Clicker Question #4

After executing the following code, what will be the value of `diff_var`?



{:.input_area}
```python
diff_var = my_variable - my_var

print(diff_var)
```


- A) 4
- B) 9
- C) "my_variable - my_var"
- D) This code will fail

### Assignment Notes

- In programming `=` means assignment
- There can be more than one assignment in a single line
- Anything to the right of the `=` is evaluated before assignment
    - This process proceeds from right to left

## Declaring Variables Cheat Sheet

- Names are always on the left of the `=`, values are always on the right
- Names are case sensitive
- Variables must start with letters (or underscores)
    - After that, they can include numbers
    - They cannot include special characters (like &, *, #, etc)
- Python doesn't care what you name your variables
    - Humans do care. Pick names that describe the data / value that they store

## Reserved Words

There are 33 words that are not allowed to be used for variable assignment in Python 3.6.

<table type="text/css">
  <tr>
      <td><code>False</code></td>
      <td><code>None</code></td>
      <td><code>True</code></td>
      <td><code>and</code></td>
      <td><code>as</code></td>
      <td><code>assert</code></td>
      <td><code>break</code></td>
  </tr>
  <tr>
      <td><code>class</code></td>
      <td><code>continue</code></td>
      <td><code>def</code></td>
      <td><code>del</code></td>
      <td><code>elif</code></td>
      <td><code>else</code></td>
      <td><code>except</code></td>
  </tr>
  <tr>
      <td><code>finally</code></td>
      <td><code>for</code></td>
      <td><code>from</code></td>
      <td><code>global</code></td>
      <td><code>if</code></td>
      <td><code>import</code></td>
      <td><code>in</code></td>
  </tr>
  <tr>
      <td><code>is</code></td>
      <td><code>lambda</code></td>
      <td><code>nonlocal</code></td>
      <td><code>not</code></td>
      <td><code>or</code></td>
      <td><code>pass</code></td>
      <td><code>raise</code></td>
  </tr>    
  <tr>
      <td><code>return</code></td>
      <td><code>try</code></td>
      <td><code>while</code></td>
      <td><code>with</code></td>
      <td><code>yield</code></td>
  </tr>    
</table>



{:.input_area}
```python
# you will get an error if you try to assign a variable to one of these words
try = 6
```


## Kernels

<div class="alert alert-success">
The <b>kernel</b> is the thing that executes your code. It is what connects the notebook (as you see it) with the part of your computer that runs code. 
</div>

Your kernel also stores your **namespace** - all the variables and code that you have declared (executed). 

It can be useful to clear and re-launch the kernel. You can do this from the 'kernel' drop down menu, at the top, optionally also clearing all ouputs. Note that this will erase any variables that are stored in memory. 

## Namespace

<div class="alert alert-success">
The <b>namespace</b> is the 'place' where all your currently defined code is declared - all the things you have stored in active memory. 
</div>



{:.input_area}
```python
whos?
```




{:.input_area}
```python
# You can list everything declared in the namespace with '%whos'
%whos
```


## Variable Types

<div class="alert alert-success">
Every variable has a <b>type</b>, which refers to the kind of variable that it is, and how the computer stores that data.
</div>



{:.input_area}
```python
# Declare a variable
variable_name = 1

# You can always ask Python 'what type is this variable' using:
type(variable_name)
```


### Int

<div class="alert alert-success">
<b>Integers</b> store whole numbers.
</div>



{:.input_area}
```python
my_integer = 1
another_integer = 321
```




{:.input_area}
```python
# integers can be signed
yet_another_integer = -4
type(yet_another_integer)
```


### Float

<div class="alert alert-success">
<b>Floats</b> store signed, decimal-point numbers.
</div>



{:.input_area}
```python
my_float = 1.0
another_float = -231.45
```




{:.input_area}
```python
type(another_float)
```


### String

<div class="alert alert-success">
<b>Strings</b> store characters, as text. 
</div>



{:.input_area}
```python
my_string = 'words, words, words'
another_string = 'more words'

# Note that strings can be defined with either '' or ""
and_another = "and some more"
```




{:.input_area}
```python
print(and_another)
type(and_another)
```


#### Quotation Marks

About those quotation marks...



{:.input_area}
```python
my_string = 'This is a single-quoted string.'
my_string
```




{:.input_area}
```python
my_string = "This is a double-quoted string."
my_string
```


Note that Python will put single quotes around it, even if you specify double quotes. 

A general principle is to pick something and be consistent. In this course, I'll do my best to only use single quotes.

#### Aside: What if you want to print a quotation mark?
- use double quotes outside with apostraphe inside quotes
- use an escape `\` (backslash) before charater



{:.input_area}
```python
# double quotes on outside; single quote inside
my_string = "i wan't to see a quote."
my_string
```




{:.input_area}
```python
# backslash to "escape" quotation mark
string_quote = "And she said, \"Please teach me Python!\""
string_quote
```


## Boolean

<div class="alert alert-success">
<b>Booleans</b> store `True` or `False`. 
</div>



{:.input_area}
```python
my_bool = True
another_bool = False
```




{:.input_area}
```python
type(another_bool)
```


## None

<div class="alert alert-success">
`None` is a special type that stores `None`, used to denote a null or empty value.
</div>



{:.input_area}
```python
the_concept_of_nothing = None
```




{:.input_area}
```python
type(the_concept_of_nothing)
```


#### Clicker Question #5

After executing the following code, what will the type of `var_a` be?



{:.input_area}
```python
var_a = -17.5
```


- A) String
- B) Int
- C) Float
- D) Boolean
- E) None

#### Clicker Question #6

After executing the following code, what will the type of `var_b` be?



{:.input_area}
```python
var_b = '-17.5'
```


- A) String
- B) Int
- C) Float
- D) Boolean
- E) None

#### Clicker Question #7

After executing the following code, what will the type of the variable `m` be?



{:.input_area}
```python
n = 1
a = 'm'
m = n
type(m)
```


- A) String
- B) Int
- C) Float
- D) Boolean
- E) None

## Aliases

<div class="alert alert-success">
Variables are names assigned to a value. Values can have more than one name. 
</div>



{:.input_area}
```python
# Make a variable, and an alias
a = 1
b = a
print(b)
```


Here, the value 1 is assigned to the variable `a`.  

We then make an **alias** of `a` and store that in the variable `b`. 

Now, the same value (1) is stored in both `a` (the original) and `b` (the alias).

### Reminders

- Multiple variables can relate to the same value(s)

### Mutable vs Immutable

The variable types we've talked about today are all **immutable**. This means they cannot be altered after they're created. 



{:.input_area}
```python
immutable_string = 'COGS18 is the best!'
immutable_string[4]
```




{:.input_area}
```python
# cannot change part of the string after creation
immutable_string[4] = '0'
```


Python does have **mutable** types. We'll talk about these later in the course, and these are where aliasing shines!

## Indentation

Just a *brief* word on indentation.

Python *does* care about whitespace. 

You will get an error if it Python runs into unanticipated whitespace.



{:.input_area}
```python
a = 1
    b = a
    
    print(b) 
```


There *are* times when indentation will be required and expected. We'll discuss these in future lectures.
