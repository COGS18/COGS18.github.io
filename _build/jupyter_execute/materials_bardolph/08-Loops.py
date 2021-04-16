**Course Announcements**

- CL3 due tonight (11:59 PM)
- A2 due Monday (4/19), may be submitted by Thursday (4/22) without penalty - no submissions after Thursday

**Notes**

- A1 will be (re)graded on Friday, A1 feedback will be released on Friday
- Midterm 1 is next Friday (4/23)

**Q&A**

Q: Are most types of errors when programming syntax errors? Are there other types of errors when programming?  
A: As a new programmer, you may encounter many syntax errors. Python reports syntax errors before exception errors, so you will likely see syntax errors most commonly. As you get more comfortable with correct syntax, you may encounter fewer syntax errors and more exception errors. There are many different exception errors (we only covered a few).  

Q: Will the error message always tell us what the error is?  
A: Python will always *try* to tell you what & where the error is, but the messages won't always be helpful. Successful debugging can take a lot of practice. It can get more complicated as your code gets more complex.  

Q: Why do we have two collections types, tuples and lists? Why is one immutable and the other is not? What are they used for that they have to be different?
A: Whenever you do not want to allow users of your code to change values in a collection, you can use a tuple - it will avoid accidental/inadertent changes. When you *do* want to be able to change values in a collection, you can use a list.

Q: Why does the code `print(my_lst[0:4:2])` not include 'Juan' in the output?  
A: See the Notes cells below for an explanation

# Students found this example in L07 confusing.
# Define a list 
my_lst = ['Julian', 'Amal', 'Richard', 'Juan', 'Xuan']

# slicing by skipping a value [start:stop:step]
print(my_lst[0:4:2])

In the code above, `[0:4:2]` represents start:stop:step values. We start at index 0 ('Julian'), then skip ahead 2 values ('Richard'), and continue extracting every 2nd element until we reach the stop value. Skipping ahead 2 more values would extract 'Xuan' next, skipping over 'Juan', but we stop *before* we reach index 4 ('Xuan'), so only 2 elements of the list are extracted.

# Control Flow - Loops

- `while`
- `for`
    - `range`
    - `continue`
    - `break`

## Loops

<div class="alert alert-success">
A <b>loop</b> is a procedure to repeat a piece of code.
</div>

### Avoid copy + pasting

For repetitive actions, if you find yourself copying + pasting, rethink your strategy.

Loops are one way to avoid this.

lst = ['you@yahoo.com', 'them@bing.com']

email = lst[0]

email = lst[1]

## While Loops

<div class="alert alert-success">
A <b>while loop</b> is a procedure to repeat a piece of code while some condition is still met. 
</div>

`while` loops always have the structure:

```python
while condition:
    # Loop contents
```

While condition is true, execute the code contents. 

Repeat until condition is no longer True. 

## While Loops

number = -5

while number < 0:
    print(number)
    number = number + 1

### While Loop Example I

connected = False

while not connected:
    
    # Try and establish connection (placeholder code)
    print('Establishing Connection...')
    
    break

### While Loop Example II

has_user_input = False

while not has_user_input:
    
    # Ask for user input (placeholder code)
    print('Asking for user input...')
    
    break

#### Poll Question #1

How many temperature values will be output from this `while` loop before "The tea is cool enough." is printed?

temperature = 115
 
while temperature > 112: 
    print(temperature)
    temperature = temperature - 1
    
print('The tea is cool enough.')

- A) 1
- B) 2
- C) 3
- D) 4
- E) Infinite


#### Poll Question #2

What will be the value of `counter` after this loop is run?

keep_looping = True
counter = 0

while keep_looping:

    counter = counter + 1
    
    if counter > 3:
        keep_looping = False

print(counter)

<pre> A) 0 | B) 2 | C) 3 | D) 4 | E) Infinite </pre> 

### Stepping Through the Loop

(Note: We skip this in class.) This is the same code as above with `print()` statements to explain what's going on at each step. If you're confused by the class example, walk through it here with the `print()` statements to guide you.

keep_looping = True
counter = 0

while keep_looping:
    print('START LOOP')
    print('\tStart counter: ', counter)

    counter = counter + 1
    
    print('\tMid counter: ', counter)
    
    if counter > 3:
        keep_looping = False
        
    print('\tEnd counter: ', counter)

print('\nFinal counter: ', counter)

## For Loops

<div class="alert alert-success">
A <b>for loop</b> is a procedure a to repeat code for every element in a sequence.
</div>

### For Loop Example I

Looping through a list

# Define a list of items
list_of_items = ['A', True, 12]

# Loop across each element
for my_item in list_of_items:
     print(my_item)
    
print('\tLast value: ', my_item)

### For Loop Example II

Looping through a string

# Loop across items in a string
for char in 'python': 
    print(char)

#### Poll Question #3

What will the following loop print out:

my_lst = [0, 1, 2, 3, 4]

for item in my_lst[0:-2]:
    print(item + 1)

- A) 0, 1, 2
- B) 0, 1
- C) 1, 2
- D) 2, 3
- E) 1, 2, 3

#### Poll Question #4

How many values will be output from this `for` loop before it *first* prints "The tea is too hot!"?

temperatures = [114, 115, 116, 117, 118]

for temp in temperatures: 
    print(temp)
    
    if(temp > 115):
        print('The tea is too hot!')


- A) 1
- B) 2
- C) 3
- D) 4
- E) Infinite


## `range`

<div class="alert alert-success">
<code>range</code> is an operator to create a range of numbers, that is often used with loops.
</div>

### `range` Examples

for ind in [0, 1, 2, 3, 4]:
    print(ind)

# the asterisk here unpacks the range
# don't worry about this syntax now
print(*range(0, 5))

# Loop across a sequence of numbers, using range
for ind in range(0, 5):
    print(ind)

# Range, like indexing, is defined by 'start', 'stop', 'step'
for ind in range(2, 6, 2):
    print(ind)

# using range in example above
for temp in range(114, 119): 
    print(temp)
    
    if(temp > 115):
        print('The tea is too hot!')

#### Poll Question #5

How many values would this loop print and what would be the last value printed? 

for ind in range(1, 10, 3):
    print(ind)

- A) values printed: 3; last value: 7
- B) values printed: 3; last value: 9
- C) values printed: 4; last value: 9
- D) values printed: 7; last value: 7
- E) values printed: 7; last value: 9


## `continue`

<div class="alert alert-success">
<code>continue</code> is a special operator to jump ahead to the next iteration of a loop.
</div>

### `continue` examples

lst = [0, 1, 2, 3]

for item in lst:
    
    if item == 2:
        continue
    
    print(item)

courses = ['cogs9', 'cogs18', 'cogs108']

for course in courses:

    if course == 'cogs18':
        continue
  
    print(course)
    print(course + '!')

string = "python"

for char in string: 
    
    if char == "p" or char == "y":
        continue
        
    print(char)

#### Poll Question #6

What will be the value of `counter` after this code has run:

counter = 0
my_lst = [False, True, False, True]

for item in my_lst:
    if item in my_lst:
        continue
    else:
        counter = counter + 1
        
print(counter)

- A) 0 
- B) 1
- C) 2 
- D) 3
- E) 4

## `break`

<div class="alert alert-success">
<code>break</code> is a special operator to break out of a loop.
</div>

connected = False

while not connected:
    
    # Try and establish connection (placeholder code)
    print('Establishing Connection...')
    
    break

### `break` examples

lst = [0, 1, 2, 3]

for item in lst:
    
    if item == 2:
        break
    
    print(item)

courses = ["cogs9", "cogs18", "cogs108"]

for course in courses:

    if course == "cogs18":
        break
  
    print(course)

string = "love python"

for char in string: 
    if char == "p" or char == "y":
        break
        
    print(char)

# using range in example above
for temp in range(114, 119): 
    print(temp)
    
    if(temp > 115):
        print('The tea is too hot!')
        break

#### Poll Question #7

What will the following code print out:

number = 1

while True:
    if number % 3 == 0:
        break
   
    print(number)
    
    number = number + 1

- A) 1 
- B) 1 2 
- C) 1 2 3
- D) Something else 
- E) This code prints forever

#### Poll Question #8

For how many `temp` will output be printed from this for loop? 

(In other words, how many times in this `for` loop will something be printed out?)

# using range in example above
for temp in range(114, 119): 
    
    if(temp < 116):
        continue
    elif(temp == 116):
        print('The tea is too hot!')
    else:
        break

- A) 0 
- B) 1
- C) 3
- D) 5
- E) 6

#### Poll Question #9

What will be the value of `counter` after this code has run?

counter = 0
my_lst = [False, True, False, True]


for item in my_lst:
    if item:
        continue
    else:
        counter = counter + 1
        
print(counter)

- A) 0 
- B) 1
- C) 2 
- D) 3
- E) 4

## Loops Practice

### Loops Practice #1

Write a loop that adds all the *odd* numbers between 1 and 1000 together.

# YOUR CODE HERE

- A) I did it!
- B) I think I did it.
- C) I started but am now stuck.
- D) I have no idea where to start.

### Loops Practice #2

Store your name as a string in a variable called `my_name`.

Write a loop that will loop through all the letters in `my_name` and count all the vowels in your name.

# YOUR CODE HERE

- A) I did it!
- B) I think I did it.
- C) I started but am now stuck.
- D) I have no idea where to start.