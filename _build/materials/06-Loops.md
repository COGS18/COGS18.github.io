---
interact_link: content/materials/06-Loops.ipynb
download_link: assets/downloads/06-Loops.ipynb.zip
pdf_link: assets/pdf/06-Loops.pdf
layout: materials
title: '06-Loops'
prev_page:
  url: /materials/05-Collections
  title: '05-Collections'
next_page:
  url: /materials/07-Dictionaries
  title: '07-Dictionaries'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
## Course Announcements

- **A1** due tonight (11:59 PM)
- **CL2** due Wednesday (7/9; 11:59 PM)
- **A2** due Mon 7/13
    - builds up to an application (cipher)
- **Exam I** *next* Monday (7/13)
    - we'll discuss format/logistics on Thursday
    - there will be a practice exam so you get familiar

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



{:.input_area}
```python
lst = ['you@yahoo.com', 'them@bing.com']

email = lst[0]

email = lst[1]
```


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

### While Loop Example I



{:.input_area}
```python
connected = False

while not connected:
    
    # Try and establish connection (placeholder code)
    print('Establishing Connection...')
    
    # a keyword that breaks out of the loop when encountered
    break
```


{:.output_stream}
```
Establishing Connection...

```

### While Loop Example II



{:.input_area}
```python
has_user_input = False

while not has_user_input:
    
    # Ask for user input (placeholder code)
    print('Asking for user input...')
    
    break
```


{:.output_stream}
```
Asking for user input...

```

## While Loops



{:.input_area}
```python
number = -5

while number < 0:
    print(number)
    number = number + 1
```


{:.output_stream}
```
-5
-4
-3
-2
-1

```



{:.input_area}
```python
keep_looping = True
counter = 0

while keep_looping:
#     print(counter)
    counter = counter + 1
    
    if counter > 3:
        keep_looping = False

print(counter)
```


{:.output_stream}
```
4

```

#### Clicker Question #1

How many temperature values will be output from this `while` loop before "The tea is cool enough." is printed?



{:.input_area}
```python
temperature = 115
 
while temperature > 112: 
    print(temperature)
    temperature = temperature - 1
    
print('The tea is cool enough.')
```


{:.output_stream}
```
115
114
113
The tea is cool enough.

```

- A) 1
- B) 2
- C) 3
- D) 4
- E) Infinite


#### Clicker Question #2

What will be the value of `counter` after this loop is run:



{:.input_area}
```python
keep_looping = True
counter = 0

while keep_looping:

    counter = counter + 1
    
    if counter > 3:
        keep_looping = False

print(counter)
```


{:.output_stream}
```
4

```

<pre> A) 0 | B) 2 | C) 3 | D) 4 | E) Infinite </pre> 

### Stepping Through the Loop



{:.input_area}
```python
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
```


{:.output_stream}
```
START LOOP
	Start counter:  0
	Mid counter:  1
	End counter:  1
START LOOP
	Start counter:  1
	Mid counter:  2
	End counter:  2
START LOOP
	Start counter:  2
	Mid counter:  3
	End counter:  3
START LOOP
	Start counter:  3
	Mid counter:  4
	End counter:  4

Final counter:  4

```

## For Loops

<div class="alert alert-success">
A <b>for loop</b> is a procedure a to repeat code for every element in a sequence.
</div>

### For Loop Example I

Looping through a list



{:.input_area}
```python
# Define a list of items
list_of_items = ['A', True, 12]

# Loop across each element
for my_item in list_of_items:
     print(my_item)
    
print('\tLast value: ', my_item)
```


{:.output_stream}
```
A
True
12
	Last value:  12

```

### For Loop Example II

Looping through a string



{:.input_area}
```python
# Loop across items in a string
for char in 'python': 
    print(char)
```


{:.output_stream}
```
p
y
t
h
o
n

```

#### Clicker Question #3

What will the following loop print out:



{:.input_area}
```python
my_lst = [0, 1, 2, 3, 4]

for item in my_lst[0:-2]:
    print(item + 1)
```


{:.output_stream}
```
1
2
3

```

- A) 0, 1, 2
- B) 0, 1
- C) 1, 2
- D) 2, 3
- E) 1, 2, 3

#### Clicker Question #4

How many values will be output from this `for` loop before it *first* prints "The tea is too hot!"?



{:.input_area}
```python
temperatures = [114, 115, 116, 117, 118]

for temp in temperatures: 
    print(temp)
    
    if(temp > 115):
        print('The tea is too hot!')

```


{:.output_stream}
```
114
115
116
The tea is too hot!
117
The tea is too hot!
118
The tea is too hot!

```

- A) 1
- B) 2
- C) 3
- D) 4
- E) Infinite


![](img/study_abroad.png)

## Course Announcements

- **CL2** due Wednesday (7/9; 11:59 PM)
- **A2** due Mon 7/13
- **Exam I** Monday (7/13)

## `range`

<div class="alert alert-success">
<code>range</code> is an operator to create a range of numbers, that is often used with loops.
</div>

### `range` Examples



{:.input_area}
```python
for ind in [0, 1, 2, 3, 4]:
    print(ind)
```


{:.output_stream}
```
0
1
2
3
4

```



{:.input_area}
```python
range(0,5)
```





{:.output_data_text}
```
range(0, 5)
```





{:.input_area}
```python
# the asterisk here unpacks the range
# don't worry about this syntax now
print(*range(0, 5))
```


{:.output_stream}
```
0 1 2 3 4

```



{:.input_area}
```python
# Loop across a sequence of numbers, using range
for ind in range(0, 5):
    print(ind)
```


{:.output_stream}
```
0
1
2
3
4

```



{:.input_area}
```python
# Range, like indexing, is defined by 'start', 'stop', 'step'
for ind in range(2, 6, 2):
    print(ind)
```


{:.output_stream}
```
2
4

```



{:.input_area}
```python
# using range in example above
for temp in range(114, 119): 
    print(temp)
    
    if(temp > 115):
        print('The tea is too hot!')
```


{:.output_stream}
```
114
115
116
The tea is too hot!
117
The tea is too hot!
118
The tea is too hot!

```

#### Clicker Question #5

How many values would this loop print and what would be the last value printed? 



{:.input_area}
```python
for ind in range(1, 10, 3):
    print(ind)
```


{:.output_stream}
```
1
4
7

```

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



{:.input_area}
```python
lst = [0, 1, 2, 3]

for item in lst:
    
    if item == 2:
        continue
    
    print(item)
```


{:.output_stream}
```
0
1
3

```



{:.input_area}
```python
courses = ['cogs9', 'cogs18', 'cogs108']

for course in courses:

    if course == 'cogs18':
        continue
  
    print(course)
    print(course + '!')
```


{:.output_stream}
```
cogs9
cogs9!
cogs108
cogs108!

```



{:.input_area}
```python
string = "python"

for char in string: 
    
    if char == "p" or char == "y":
        continue
    
    print(char)
```


{:.output_stream}
```
t
h
o
n

```

#### Clicker Question #6

What will be the value of `counter` after this code has run:



{:.input_area}
```python
counter = 0
my_lst = [False, True, False, True]

for item in my_lst:
    if item in my_lst:
        continue
    else:
        counter = counter + 1
        
print(counter)
```


{:.output_stream}
```
0

```

- A) 0 
- B) 1
- C) 2 
- D) 3
- E) 4

## `break`

<div class="alert alert-success">
<code>break</code> is a special operator to break out of a loop.
</div>



{:.input_area}
```python
connected = False

while not connected:
    
    # Try and establish connection (placeholder code)
    print('Establishing Connection...')
    
    break
```


{:.output_stream}
```
Establishing Connection...

```

### `break` examples



{:.input_area}
```python
lst = [0, 1, 2, 3]

for item in lst:
    
    if item == 2:
        break
    
    print(item)
```


{:.output_stream}
```
0
1

```



{:.input_area}
```python
courses = ["cogs9", "cogs18", "cogs108"]

for course in courses:

    if course == "cogs18":
        break
  
    print(course)
```


{:.output_stream}
```
cogs9

```



{:.input_area}
```python
string = "love python"

for char in string: 
    if char == "p" or char == "y":
        break
        
    print(char)
```


{:.output_stream}
```
l
o
v
e
 

```



{:.input_area}
```python
# using range in example above
for temp in range(114, 119): 
    print(temp)
    
    if(temp > 115):
        print('The tea is too hot!')
        break
```


{:.output_stream}
```
114
115
116
The tea is too hot!

```

#### Clicker Question #7

What will the following code print out:



{:.input_area}
```python
number = 1

while True:
    if number % 3 == 0:
        break
   
    print(number)
    
    number = number + 1
```


{:.output_stream}
```
1
2

```

- A) 1 
- B) 1 2 
- C) 1 2 3
- D) Something else 
- E) This code prints forever

#### Clicker Question #8

For how many `temp` will output be printed from this for loop? 

(In other words, how many times in this `for` loop will something be printed out?)



{:.input_area}
```python
# using range in example above
for temp in range(114, 119): 
    
    if(temp < 116):
        continue
    elif(temp == 116):
        print('The tea is too hot!')
    else:
        break
```


{:.output_stream}
```
The tea is too hot!

```

- A) 0 
- B) 1
- C) 3
- D) 5
- E) 6

#### Clicker Question #9

What will be the value of `counter` after this code has run:



{:.input_area}
```python
counter = 0
my_lst = [False, True, False, True]


for item in my_lst:
    if item:
        continue
    else:
        counter = counter + 1
        
print(counter)
```


{:.output_stream}
```
2

```

- A) 0 
- B) 1
- C) 2 
- D) 3
- E) 4

### Loops Practice #1

Write a loop that adds all the *odd* numbers between 1 and 1000 together.



{:.input_area}
```python
# Answer here
# counter; initial variable
total = 0

# for loop
# check over range of numbers (range(1,1000,2))
for value in range(1,1000,2):
    
    # conditional if this is true
    # modulus - check for odd (number % 2 != 0)
    if value % 2 != 0:
        total = total + value

total
```





{:.output_data_text}
```
250000
```



- A) I did it!
- B) I think I did it.
- C) I started but am now stuck.
- D) I have no idea where to start.



{:.input_area}
```python
# create some variables to get yourself started
total = 0
current = 1
stop = 1000

# logic to tell while when to stop
while current <= stop:
    
    # check if odd
    if current % 2 != 0:
        total = total + current
    
    # increment counter by 1
    current = current + 1

total
```





{:.output_data_text}
```
250000
```





{:.input_area}
```python
# less ideal solution

# create some variables to get yourself started
total = 0
current = 1
stop = 1000

while current <= stop:
    
    # increase total
    total = total + current
    
    # if we increment counter by 2
    # will work, but only if current starts as odd number
    current = current + 2

total
```





{:.output_data_text}
```
250000
```





{:.input_area}
```python
# A for loop approach
total = 0

for val in range(1, 1000, 2):
    total = total + val
    
total
```





{:.output_data_text}
```
250000
```



### Loops Practice #2

Store your name as a string in a variable called `my_name`.

Write a loop that will loop through all the letters in `my_name` and count all the vowels in your name.



{:.input_area}
```python
# Answer here
my_name = 'ShannonAEI'
vowels = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')
counter = 0

# for loop - loop through my_name
for char in my_name:
    # need some conditional
    if char in vowels:
        # adjust counter (conditional on if it's a vowel)
        counter = counter + 1

# print at the end to check our work
counter
```





{:.output_data_text}
```
5
```



- A) I did it!
- B) I think I did it.
- C) I started but am now stuck.
- D) I have no idea where to start.



{:.input_area}
```python
my_name = 'Shannon'
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
counter = 0

for char in my_name:
    if char in vowels:
        counter = counter + 1

counter
```





{:.output_data_text}
```
2
```


