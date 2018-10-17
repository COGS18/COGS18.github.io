---
download_link: assets/downloads/07-Loops.ipynb.zip
pdf_link: assets/pdf/07-Loops.pdf
title: '07-loops'
permalink: '/chapters/07-Loops'
previouschapter:
  url: /chapters/06-DataTypes
  title: '06-datatypes'
nextchapter:
  url: /chapters/08-Encodings
  title: '08-encodings'
redirect_from:
  - '/chapters/07-loops'
---

# Control Flow - Loops

## Loops

<div class="alert alert-success">
A **loop** is a procedure to repeat a piece of code.
</div>

## While Loops

<div class="alert alert-success">
A ** while loop** is a procedure to repeat a piece of code while some condition is still met. 
</div>

## While Loops

While loops always have the structure

```
while condition:
    # Loop contents
```

While condition is true, execute the code contents. 

Repeat until condition is no longer True. 

### While Loops



{:.input_area}
```python
number = 0
while number < 5:
    print(number)
    number = number + 1
```


{:.output_stream}
```
0
1
2
3
4

```

### While Loop Example I



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

## Clicker Question #1

What will be the value of `counter` after this loop is run:

```
keep_looping = True
counter = 0

while keep_looping:

    counter = counter + 1
    
    if counter > 3:
        keep_looping = False
```

A) 0 | B) 2 | C) 3 | D) 4 | E) Infinite

### Clicker Question Answer



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


## For Loops

<div class="alert alert-success">
A ** for loop** is a procedure a to repeat code for every element in a sequence.
</div>

### For Loop Example I



{:.input_area}
```python
# Define a list of items
list_of_items = ['A', True, 12]

# Loop across each element
for item in list_of_items:
    print(item)
```


{:.output_stream}
```
A
True
12

```

### For Loop Example II



{:.input_area}
```python
# Loop across items in a string
for char in "python":
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

## Clicker Question #2

What will the following loop print out:

```
my_lst = [0, 1, 2]

for item in my_lst[0:-1]:
    print(item + 1)
```

A) 0, 1, 2 | B) 0, 1 | C) 1, 2 | D) 2, 3 | E) 1, 2, 3

### Clicker Question Answer



{:.input_area}
```python
my_lst = [0, 1, 2]

for item in my_lst[0:-1]:
    print(item + 1)
```


## `range`

<div class="alert alert-success">
`range` is an operator to create a range of numbers, that is often used with loops.
</div>

### Range Examples



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

## `continue`

<div class="alert alert-success">
`continue` is a special operator to jump ahead to the next iteration of a loop.
</div>

### continue examples



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

## `break`

<div class="alert alert-success">
`break` is a special operator to break out of a loop.
</div>

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

## Clicker Question #3

What will the following code print out:

```
number = 1
while True:
    if number % 3 == 0:
        break
    print(number)
    
    number = number + 1
```

A) 1 | B) 1 2 | C) 1 2 3 | D) Something else | E) This code prints forever

### Clicker Question Answer



{:.input_area}
```python
number = 1
while True:
    if number % 3 == 0:
        break
    print(number)
    
    number = number + 1
```


## Clicker Question #4

What will be the value of counter after this code has run:

```
counter = 0
my_lst = [False, True, False, True]


for item in my_lst:
    if item:
        continue
    else:
        counter = counter + 1
```

ANSWERS
A) 0 | B) 1 | C) 2 | D) 3 | E) 4

### Clicker Question Answer



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

