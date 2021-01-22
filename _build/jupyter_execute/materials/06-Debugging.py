**Course Announcements**
- A1 due next Friday
- CL2 answers posted on website
- No Class Monday (MLK, Jr Day)

# Debugging

- Errors
    - Syntax
    - Exceptions
- `try`/`except`

<div class="alert alert-success">
Debugging is the process of finding and fixing errors in a computer program.
</div>

## Errors

<div class="alert alert-success">
Errors are problems with code definition or execution that interrupt running Python code.
</div>

### Syntax Errors

- Syntax Errors
- Indentation Errors

<div class="alert alert-success">
Syntax & Indentation Errors reflect code that doesn't follow Python structure, and will necessarily fail. 
</div>

### Syntax Error Examples

# will produce a syntax error
if True
    print('Yep.')

Python does its best to tell you:
- what type of error it is
- and where it _thinks_ it occurred (`^`)

# will produce a syntax error
# and specifically an indentation error
if 3 < 4:
print('value')

Python gives you a readout about what it was expecting and where you appear to have gone wrong.

## Exceptions

<div class="alert alert-success">
Exceptions are errors that occur when a code is executed.
</div>

For these, there's nothing wrong with the _syntax_ or _structure_ of the code, but in your specific case and how you're trying to use it, Python says 'no'.

### ZeroDivisionError

ZeroDivisionError occurs when you try to divide by zero. 

# produces ZeroDivisionError
1 / 0

Python specifies:
- the Exception and specific type / error
- points you to where the error occurred

### NameError

NameError occurs when you try to access a name that Python does not know.

# Define a variable
variable = 12

# If you typo a name, you will get a NameError
varaible

While it's annoying, it's helpful that Python doesn't just _guess_ that you _meant_ 'variable'....because sometimes Python would guess wrong. It's better for Python to just give us the error.

# You also get a name error if you try to use the wrong operator for assignment
new_variable == 1

### IndexError

IndexError occurs when you try to access an index that doesn't exist.

my_string = 'COGS18'
my_string[6]

# Relatedly, 'KeyError' occurs if you ask for a dictionary key that doesn't exist
my_dictionary = {'name1' : 1, 'name2' : 2}
my_dictionary['name3']

### ValueError

ValueError occurs when you try to use an illegal value for something.

int('cat')

### TypeError

'a_string' + 12

## Error Recap

- Syntax Errors
    - `SyntaxError`
    - `IndentationError`
- Exceptions
    - `ZeroDivisionError` 
    - `NameError`
    - Index Errors
        - `IndexError`
        - `KeyError`
    - `ValueError`
    - `TypeError`


#### Clicker Question #1

What type of error will the following code produce?

if num > 0
    print("Greater than 0")

- A) Syntax 
- B) Name
- C) Type
- D) Index
- E) Value

#### Clicker Question #2

What type of error will the following code produce?

if num > 0:
    print("Greater than 0")

- A) Syntax 
- B) Name
- C) Type
- D) Index
- E) Value

## Stack Trace

The trace (log) of what Python did as it went through your code. Gets printed out if Python runs into an error.

running_sum = 0
my_list = [1, 2, 3, 4, 5]

for val in my_list:
    
    if val % 2 == 0:
        temp = val / (val - 4)
        #+= allows you to add the value on the right to the variable on the left 
        # and assign it to the variable on the left
        running_sum += temp 
        # equivalent to:
        # running_sum = running_sum + temp

Sometimes these get really complex. We're here to get better at interpreting these traces.

Note that if external functions are being used, these will get longer.

## Try / Except

<div class="alert alert-success">
Exceptions do not necessarily have to lead to breaking the program - they can be programmatically dealt with, using 'try' and 'except'. 
</div>

### Try / Except Block

# Try / Except Block
try:
    # Tries to do this code
    pass # pass just says is not an operation; carry on
except:
    # If there is an error (an exception), keep going and do this instead
    pass

### Try / Except Example 

# Example: we want to get an input number from the user

my_num = input("Please type a number: ")

print('\nmy_num is: ', my_num)

### Example with Try / Except

int('asdlkfjasdflj')

try:
    int(input('Number'))
except:
    print('nahhh')

#### Try / Except within a While Loop

# getting an input from a user
input("text")

try:
    my_num = int(input("Please enter a number: "))
except ValueError: # can specify what type of error 
    print("Oops!  That was no valid number. Try again!")
        
print('\nmy_num is: ', my_num)

## Raising Errors

<div class="alert alert-success">
You can also write code to raise an Exception if something unexpected happens.
</div>

### Raise Exception Examples

`raise` is a keyword that tells Python you want to create your own error.

my_int = input('An integer please: ')

if not my_int.isnumeric():
    raise ValueError('I wanted a number! :(')
    
print('My integer is: ', my_int) 

#### Clicker Question #3

Edit the code below (replacing `---` with either values or variable names) so that when executed, this cell returns `None`.

output = 6/0

num1 = 6
num2 = 0

try:
    output = num1 / num2
except ZeroDivisionError:
    output = None
    
print(output)

- A) I did it!
- B) I _think_ I did it...
- C) I'm totally lost.

## Helping yourself when debugging

- You aren't sure how to approach a problem: add 'in python'
- You don't understand an error message: 
    - Use `print()` statements
    - Google the error message...but then you need to understand what you're reading

### Unsure how to approach a problem

"Write code that will check whether the value stored in `my_val` is both positive and even. If it is, store the integer `1` in the variable `output`"

...How do I check whether a variable stores an even value?

Google: "How to check whether a variable stores an even value _in python_"

my_val = 6

# check if positive and even (conditional)
if my_val > 0 and (my_val % 2) == 0:    
    # if true, store 1 in output
    output == 1

### Don't understand the error message

So you try to accomplish the task...below is your first attempt

# this code has errors
# we're going to debug together in class
my_val = 5

if my_val > 0 and my_val % 2 == 0:
    output = 1
else:
    output = None
    
print(output)