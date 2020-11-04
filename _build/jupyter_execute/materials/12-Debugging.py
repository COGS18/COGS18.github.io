**Course Announcements**

**Due Dates:**
- **A3** due tonight (11:59 PM) 
- [**Mid-course survey**](https://docs.google.com/forms/d/e/1FAIpQLSe0zyyiiQYT3yaizo34KQh9A5YHXOAC7XjyjWZHIV-hvPMfvQ/viewform?usp=sf_link) - complete by tonight for EC

**Notes**:
- **CL4** Grades Posted
- **CL5** is available
- **E1** Grades, Feedback & Answers Posted
    - Mean: 10.84/12.5 (86.7%)
    - rubric for partial credit in feedback & answer key
    - *regrades* (private to instructors on piazza): followed instructions but lost points; include explanation
    - Note: Q9 accepted multiple approaches due to ambiguity in the wording (whether or not to include courses taught in 2019)
- **A4** will be posted later today
    - Part 1 can be completed now
    - Parts 2 & 3 we start this week
    - Due Mon 11/16 (2 weeks from now) <- it is longer than other assignments
    - **Validate will give you a timed out error** (Use Kernel > Restart & Run all instead)

**A note on `assert` cells**

These are meant to *guide* you.

They are *not* meant to be what you use to completely guide your thinking.

When you get an error from an assert cell. Pause. Think about what you wanted your code to do. Think about the logic behind the code you've written. ***Edit your code with purpuse***.

Do ***not*** randomly change bits of your code until you get the assert to pass silently.

# Debugging

- Errors
    - Syntax
    - Exceptions
- `try`/`except`

<div class="alert alert-success">
Debugging is the process of finding and fixing errors in a computer program.
</div>

Now that we're writing functions, debugging will become _really_ critical.

### Clicker Question #1

Will I be able to define and execute this function?

def example_function(input_list):
    
    running_sum = 0
    for item in input_list:
        running_sum = running_sum + item
    
    special_value = input_list[3]
    
    return running_sum + special_value

example_function(input_list = [1, 2, 3])

- A) Yes 
- B) No
- C) Depends on the `input_list`
- D) There's no way to tell 
- E) I don't know

### executing the function
example_function(['a','b','c','d'])

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
my_list = [1, 2]
for value in my_list:
print(value)

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

my_list = [1, 2, 3]
my_list[5]

# Relatedly, 'KeyError' occurs if you ask for a dictionary key that doesn't exist
my_dictionary = {'name1' : 1, 'name2' : 2}
my_dictionary['name3']

### ValueError

ValueError occurs when you try to use an illegal value for something.

int('cat')

my_list = [1, 2, 3]
my_list.remove(0)

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


### Clicker Question #2

What type of error will the following code produce?

if num > 0
    print("Greater than 0")

- A) Syntax 
- B) Name
- C) Type
- D) Index
- E) Value

### Clicker Question #3

What type of error will the following code produce?

# without num will be a name error
num = 5

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
    # print(val)
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

int(6)

int('Shannon')

input('val')

try:
    int(input('Number'))
except:
    print("nahhh")

#### Try / Except within a While Loop

ask_for_num = True

while ask_for_num:
    try:
        my_num = int(input("Please enter a number: "))
        ask_for_num = False
    except ValueError or NameError:
        print("Oops!  That was no valid number. Try again!")
        
print('\nmy_num is: ', my_num)

### More Try / Except

# define a function divide
def divide(num1, num2):
    return num1 / num2

print(divide(2, 0))

# define a function safe_divide
def safe_divide(num1, num2):
    
    try:
        output = num1 / num2
    except ZeroDivisionError:
        output = None
    
    return output

print(safe_divide(2, 0))

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

### Clicker Question #4

Edit the code below (replacing `---` with either values or variable names) so that when executed, this cell returns `None`.

num1 = ---
num2 = ---

try:
    output = num1 / num2
except ZeroDivisionError:
    output = None
    
print(output)

- A) I did it!
- B) I _think_ I did it...
- C) I'm totally lost.