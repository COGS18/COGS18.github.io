# Coding Lab 3: Programming II

Welcome to the third coding lab!

CodingLab labs are meant to be interactive - so you should find another person to work together with on this notebook. For this lab, you can either work together on one notebook, or work together but each fill out your own notebook, if you prefer. 

CodingLabs are also meant to be exploratory. There are broad questions in the notebook that you should explore, and try to answer - but you are also very much encouraged to explore other related ideas as you go! 

If you have a question about how something works / what something does - try it out, and see what happens!

## Part 1: Collection types

Collections are Python variable types than can store a 'collection' of items.

### Collection Questions

Create a list and a tuple. Fill them with with any values you want. 

Call them `my_list` and `my_tuple`.

### BEGIN SOLUTION
# specific values will differ

my_list = [1, 2, 3]
my_tuple = ('a', 'b', 'c')
### END SOLUTION

Use the following cells to check the types of the variables you write are as expected

type(my_list)

type(my_tuple)

#### Declaring Collections

Note that there can be more than one way to declare collections. 

As well as declaring them with '[]' and '()', we can use the list & tuple constructors, as shown below. 

# Run me! - This creates another list & tuple, using the list & tuple constructors
some_list = list([1, 2, 3, 4, 5])
some_tuple = tuple(["peanut", "butter", "and", "jelly"])

print("'some_list' contains: \t", some_list)
print("'some_tuple' contains: \t", some_tuple)

Compare the types of these variables to your equivalent variables to confirm.

In the cell below, write in the type of the objects that you expect them to be, and make sure the asserts pass. 

# Fill in `_WRITE_IN_TYPE_HERE` with the type you expect each variable to be
assert isinstance(some_list, _WRITE_IN_TYPE_HERE_)
assert isinstance(some_tuple, _WRITE_IN_TYPE_HERE_)

### Indexing

Given the following list, do the following operations:
- Get the length of the list (assign this to a variable `lst_len`)
- Get the 1st element of the list (call the selection `ind1`)
- Get the last element of the list (call the selection `ind2`)
- Get the second to the fourth element of the list (call the selection `ind3`)
- Get from the fifth element, to the end of the list (call the selection `ind4`)
- Get every second element of the list, starting at the first element (call the selection `ind5`)
- Get every second element of the list, starting at the second element (call the selection `ind6`)

my_lst = ['a', True, 12, 'tomato', False, None, 23, 'python', [], 5.5]

### BEGIN SOLUTION
lst_len = len(my_lst)
ind1 = my_lst[0]
ind2 = my_lst[-1]
ind3 = my_lst[1:5]
ind4 = my_lst[4:]
ind5 = my_lst[0::2]
ind6 = my_lst[1::2]
### END SOLUTION

## Part 2: Conditionals

Conditionals a form of control flow for executing certain code if a specific condition is met. 

### Conditional Questions

In this part, we will re-visit some questions about conditionals, and start combining them together with collections. 

Make sure you can use if/elif/else statements to control which code blocks are run.

#### Controlling Output With Conditionals I

Using the code below, keep updating the variable value to make sure you can make the conditional return each of the possibilities. 

# ToDo: Update value to control what gets executed
value = 10

# This code provided
if isinstance(value, int):
    if value < 10:
        result = 'small value'
    if value >= 10:
        result = 'big value'
else:
    result = 'false value'

print(result)

#### Controlling Output With Conditionals II

In the cell below, first write something into each result assignment related to  for example, it could be "B1 is False & B2 is True"). 

Then make sure you can change values of b1 & b2 to make the program execute each option. 

# ToDo: Update b1 & b2 to control what gets executed
b1 = False
b2 = False

# Next, try this out
if b1 and not b2:
    result = ''
elif not b1 and b2:
    result = ''
elif b1 and b2:
    result = ''
else:
    result = ''

print(result)

### Conditional Challenges

The following are more challenging questions relating to conditional statements. If they seem too tricky for now, just skip ahead to the next section.

#### Conditional Challenge #1

Write a conditional that prints "Found it" if a given `val_2` is a multiple of 10, otherwise prints "Nope."

### BEGIN SOLUTION
# Set a test value for `val_2`
val_2 = 100

if val_2 % 10 == 0:
    print('Found it')
else:
    print('Nope')
### END SOLUTION

#### Conditional Challenge #2

Input: assumes a variable `val_1`, that can be either a string or an integer

Output: based on the conditions, this code block will assign a variable called `output` to be a boolean

Use conditions to check whether `val_1` is a string or an integer object:
- If it is a string, check whether it's length is greater then 8
    - If so, set the value `output` to True
- If it is an integer, compare whether it is less than 100
    - If so, set the value `output` to True
- Else, set output to False

### BEGIN SOLUTION
# Set a test value for `val_1`
val_1 = 'string'

if isinstance(val_1, str):
    output = True
elif isinstance(val_1, int):
    output = True
else:
    output = False

# Check the output
print(output)
### END SOLUTION

### Operator Explorations

For each of the following questions, start by writing out a guess of what you think it might do. 

Then, test out each one by writing out some code. 

Finally, once you have answered the question, using some code, add a comment in the markdown here with the answer. 

Questions:
- Can you include multiple conditions in an if statement?
    - If think so, write an if statement that tests multiple conditions.
- What happens if you put an if statement inside an if statement? When would such a statement run?
    - To explore this, write an if statement that has an embedded if statement in it. 


### BEGIN SOLUTION
v1 = True
v2 = False

# Option 1
# Yes, you can include multiple conditions in an if statement
if v1 == True and v2 == False:
    print('YES!')

# Option 2
# Yes, you can have an if statement within an if statement
#   The embedded if will end up running if both conditions of both if's are True   
if v1 == True:
    if v2 == False:
        print('Also YES!')
### END SOLUTION

## Part 3: Debugging Questions

### Creating Errors
For each of the follow Exceptions, write a small piece of code that will cause it to happen:
- ZeroDivisionError
- SyntaxError
- IndentationError
- TypeError
- IndexError
- ValueError
- NameError

# ZeroDividisionError

### BEGIN SOLUTION
# Zero Division Answer
1/0
### END SOLUTION

# SyntaxError

### BEGIN SOLUTION
# Syntax Answer
for el in [1, 2]
    print(el)
### END SOLUTION

# IndentationError

### BEGIN SOLUTION
# Indentation Error
for el in [1, 2]:
print(el)
### END SOLUTION

# TypeError

### BEGIN SOLUTION
# Type error
(1, 2) + (2)
### END SOLUTION

# IndexError

### BEGIN SOLUTION
# Index Error
lst = [1, 2]
lst[2]
### END SOLUTION

# ValueError

### BEGIN SOLUTION
# Value Error
int('a')
### END SOLUTION

# NameError

### BEGIN SOLUTION
# Name Error
a
### END SOLUTION

### Fixing Errors

For each of the following cells, try to debug the code to fix any errors, and get it running. 

if True
    print('It worked')
    
### BEGIN SOLUTION
# Answer: add a ':' to open the conditional code block
if True:
    print('It worked')
### END SOLUTION

age_string = "My favorite number is " + 27

### BEGIN SOLUTION
# Answer: typecase int to string
age_string = "My favorite number is " + "27"
# OR
age_string = "My favorite number is " + str(27)
### END SOLUTION


print('Three plus five equals' + str(3+5)

### BEGIN SOLUTION
# Answer: Missing closing parenthesis - add ')' at the end
print('Three plus five equals' + str(3+5))

### END SOLUTION


## The End!

This is the end of this Coding Lab!

Be sure you've made a concerted effort to complete all the tasks specified in this lab. Then, go ahead and submit on datahub!