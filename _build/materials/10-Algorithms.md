---
interact_link: content/materials/10-Algorithms.ipynb
download_link: assets/downloads/10-Algorithms.ipynb.zip
pdf_link: assets/pdf/10-Algorithms.pdf
layout: materials
title: '10-Algorithms'
prev_page:
  url: /materials/09-FunctionsI
  title: '09-FunctionsI'
next_page:
  url: /materials/11-FunctionsII
  title: '11-FunctionsII'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

Course Check-In

### Course Announcements

- **A3 due Monday (11:59 PM)**
    - you must click "submit" on datahub to submit your assignment
- Python Syntax & Examples have been added to course website

### A note on the midterm

1. It's Friday of Week 6 (You have time)
2. We'll have a whole review day the Wednesday before.
3. It will cover content through the Friday of Week 5.
4. Types of questions:
    - matching
    - short answer
        - recall a definition
        - explain the difference between two terms
        - interpret code ; answer you write is output from code
        - write code (on paper) given a task
    - True/False
    - Circle correct term in context
    - multiple choice
    - etc.
5. A word on exam writing: Bloom's Taxonomy


- Preparing for the exam:
    - talk through code examples in class out loud
    - change variables, values, functions in code & anticipate change before running
    - write code from assignments
    - understand the applications in assignments

# Review Time

## Review Clicker #1

What will be the output of this code?



{:.input_area}
```python
lst = [0, 1, 2, 3]

my_val = 0

for item in lst:
    
    if item == 2:
        print(item)
        break
    elif item == 4:
        my_val = my_val + 1
    else:
        continue
```


{:.output_stream}
```
2

```

- A) 0, 1, 2
- B) 0, 1, 2, 3
- C) 2
- D) False, False, True
- E) False, False, True, True

## Review Clicker #2

What is the length of `my_dict`? 



{:.input_area}
```python
my_dict = {'member_1' : 'Jane', 'member_2' : 'Allie', 'member_3' : 'Antonio'}
len(my_dict)
```





{:.output_data_text}
```
3
```



- A) 1
- B) 2
- C) 3
- D) 6

## Review Clicker #3

When executed, what would be the output of the following code?



{:.input_area}
```python
lots_of_items =(1,2,4,5,6,7,9,11)
lots_of_items[5] = 'string'
print(lots_of_items[5])
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
TypeError                                 Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-5-2712cf662cb8> in <module>()
      1 lots_of_items =(1,2,4,5,6,7,9,11)
----> 2 lots_of_items[5] = 'string'
      3 print(lots_of_items[5])

```

{:.output_traceback_line}
```
TypeError: 'tuple' object does not support item assignment
```


- A) 5
- B) 6
- C) 7
- D) string
- E) TypeError

### Brief function review



{:.input_area}
```python
# define a function: return_value
# num is a parameter for the function
def return_value(num):
    
    # do some operation
    out = num
    
    # return variable
    return out
```


## Review Clicker #4



{:.input_area}
```python
an_int = 2
a_float = 11.5

def print_numbers(an_int, a_float):
    print(an_int, ',', a_float)
```


Assuming the cell above has been executed, what will the code below print out?



{:.input_area}
```python
print(an_int)
print_numbers(5, 12.2)
```


{:.output_stream}
```
2
5 , 12.2

```

- A) 5 , 11.5
- B) 2, 12.2 
- C) 2 , 11.5 
- D) 5 , 12.2
- E) None

## Clicker Question #5



{:.input_area}
```python
def string_manipulator(string):
    
    output = ''
    for char in string:
        if char == 'a' or char == 'e':
            char = 'z' 
        output = output + char
    
    return output
```


Given the function above, what will the following code print?



{:.input_area}
```python
variable = 'abcde'
manipulated_string = string_manipulator(variable)
print(manipulated_string)
```


- A) 'abcde' 
- B) 'zbcdz'
- C) 'zzzzz'
- D) 'azbcdez'
- E) ''

# Algorithms

What are the sorts of things that we should do with computers? What are things that are easy to compute? Hard to compute? Impossible to compute?

## Algorithms

<div class="alert alert-success">
An <b>algorithm</b> is a formal description of how to complete a procedure, typically taking inputs and returns some output.
</div>

If you can write the steps down, you can write an algorithm.

Algorithms are computable.

Computers cannot read between the lines. They are very literate.

## Algorithm Example: Making a Sandwich

### Clicker Question #1

Can you write an algorithm to make a ham and cheese sandwich. 

- A) Yes 
- B) No
- C) I don't know

## Algorithm for making a ham & cheese sandwich

- Step 0: Get bread, ham, and cheese
- Step 1: Place slice of bread on table
- Step 2: Place a slice of ham on top of the bread 
- Step 3: Place a slice of cheese on top of the ham
- ...


Humans are pretty good at making sandwiches. Computers may struggle a bit.

## Algorithm Example: Sorting

Given a list of numbers, how can we sort it into the correct order?

Y'all Google is *really* good at sorting.

- ranking: rate a site as how related
- sort: given a list of good sites, determine order to present to user

...and do this on all the things



{:.input_area}
```python
# Define a list of numbers
list_of_numbers = [2, 1, 3]
```


### Clicker Question #2

**array**: a collection of items, where each item can be accessed by its index.

Can you write an algorithm to sort an array?

- A) Yes 
- B) No
- C) I don't know

## `sort_array`

A version of a **selection sort**:
- loop through current list
- find lowest item
- put that at the front of your list
- wash, rinse, repeat



{:.input_area}
```python
def sort_array(array_to_sort):
    """A function to sort an array."""

    is_sorted = False    # Keeps track of when we are done sorting
    sorted_array = []    # A new list that we will use to 
     
    while not is_sorted:

        lowest = None
        for item in array_to_sort:
            if lowest == None:         # If not defined (first element) set the current element as lowest
                lowest = item
            if item < lowest:
                lowest = item
        
        # these next two lines use new methods
        sorted_array.append(lowest)    # Add the lowest value to our sorted array output
        array_to_sort.remove(lowest)   # Drop the now sorted value from the original array

        if len(array_to_sort) == 0:    # When `array_to_sort` is empty, we are done sorting
            is_sorted = True
    
    return sorted_array
```


## Using `sort_array`



{:.input_area}
```python
# Sort an array of integers
unsorted_array = [12, 7, 19, 12, 25]
sorted_array = sort_array(unsorted_array)
print(sorted_array)
```


{:.output_stream}
```
[7, 12, 12, 19, 25]

```



{:.input_area}
```python
# Sort an array of floats
unsorted_array = [21.3, 56.7, 2.3, 2.9, 99.9]
sorted_array = sort_array(unsorted_array)
print(sorted_array)
```


{:.output_stream}
```
[2.3, 2.9, 21.3, 56.7, 99.9]

```

### Clicker Question #3

Using our `sort_array` function from above, what will the following code snippet print out:



{:.input_area}
```python
data = ['a', 'c', 'b'] 
sort_array(data)
```





{:.output_data_text}
```
['a', 'b', 'c']
```



- A) ['a', 'c', 'b']
- B) ['a', 'b', 'c']
- C) [97, 98, 99]
- D) None
- E) This code will fail

### How Python evaluates strings



{:.input_area}
```python
'a' < 'b'
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
ord('a')
```





{:.output_data_text}
```
97
```





{:.input_area}
```python
ord('b')
```





{:.output_data_text}
```
98
```



### Clicker Question #4

Using our `sort_array` function from above, what will the following code snippet print out:



{:.input_area}
```python
data = [True, False, True]
sort_array(data)
```





{:.output_data_text}
```
[False, True, True]
```



- A) [False, True, True] 
- B) [True, False, True] 
- C) [0, 1, 1]]
- D) [True, True, False] 
- E) This code will fail

### How Python evaluates Booleans



{:.input_area}
```python
True < False
```





{:.output_data_text}
```
False
```





{:.input_area}
```python
bin(True)
```





{:.output_data_text}
```
'0b1'
```





{:.input_area}
```python
bin(False)
```





{:.output_data_text}
```
'0b0'
```



### Clicker Question #5

Using our `sort_array` function from above, what will the following code snippet print out:



{:.input_area}
```python
data = [[3, 4], [1, 2]]
sort_array(data)
```


- A) [[3, 4], [1, 2]]  
- B) [1, 2, 3, 4] 
- C) [[1, 2], [3, 4]]
- D) None 
- E) This code will fail

## SideNote: `sorted`



{:.input_area}
```python
# Sort a list, with `sorted`
data = [7, 4, 6]
sorted(data)
```





{:.output_data_text}
```
[4, 6, 7]
```





{:.input_area}
```python
# Sort different data types
print(sorted(['a', 'c', 'b']))
print(sorted([True, False, True]))
print(sorted([[3, 4], [1, 2]]))
```


{:.output_stream}
```
['a', 'b', 'c']
[False, True, True]
[[1, 2], [3, 4]]

```

## Algorithmic Complexity

<div class="alert alert-success">
The complexity of an algorithm characterizes the relationship between the input size and the number of steps of an algorithm.
</div>

## Algorithmic Complexity

Things we might care about:
- The number of steps it takes to complete our algorithm
    - Usually defined in relation of the size of the input
- The amount of memory it will take to run our algorithm

## Properties of our sorting algorithm

- It will require $n^2$ steps, where $n$ is the length of the list
- It will require ~double the memory of the original list

## Computability

Things that computers can do are things that we can write down an algorithm to do.

Things that we can write an algorithm to do are things that we can define a specific set of steps to complete.
