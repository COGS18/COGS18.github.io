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
  url: /materials/A1-Syntax
  title: 'A1-Syntax'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

### Course Announcements

- A3 now available - due Friday 11/1 (11:59 PM)
- We're grading exams Friday
- Mid-course survey now available
    - http://bit.ly/cogs18_midcourse
    - opportunity for extra credit (if completed by Sunday 10/27 at 11:59 PM)

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


### Clicker Warmup #1



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
print_numbers(5, 12.2)
```


- A) 5 , 11.5
- B) 2, 12.2 
- C) 2 , 11.5 
- D) 5 , 12.2
- E) None

### Clicker Warmup #2



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

- We'll update here


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




{:.input_area}
```python
# Sort an array of floats
unsorted_array = [21.3, 56.7, 2.3, 2.9, 99.9]
sorted_array = sort_array(unsorted_array)
print(sorted_array)
```


### Clicker Question #3

Using our `sort_array` function from above, what will the following code snippet print out:



{:.input_area}
```python
data = ['a', 'c', 'b'] 
sort_array(data)
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




{:.input_area}
```python
ord('a')
```




{:.input_area}
```python
ord('b')
```


### Clicker Question #4

Using our `sort_array` function from above, what will the following code snippet print out:



{:.input_area}
```python
data = [True, False, True]
sort_array(data)
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




{:.input_area}
```python
bin(True)
```




{:.input_area}
```python
bin(False)
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




{:.input_area}
```python
# Sort different data types
print(sorted(['a', 'c', 'b']))
print(sorted([True, False, True]))
print(sorted([[3, 4], [1, 2]]))
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
