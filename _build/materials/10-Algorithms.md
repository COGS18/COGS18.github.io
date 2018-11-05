---
download_link: assets/downloads/materials/10-Algorithms.ipynb.zip
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

# Algorithms

## Algorithms

<div class="alert alert-success">
An algorithm is a formal description of how to complete a procedure, typically taking inputs and returning some output.
</div>

## Algorithm Example: Making a Sandwich

### Clicker Question #1

Can you write an algorithm to make a ham and cheese sandwich. 

A) Yes | B) No | C) I don't know

## Algorithm Example: Sorting

Given a list of numbers, how can we sort it into the correct order?



{:.input_area}
```python
# Define a list of numbers
list_of_numbers = [2, 1, 3]
```


### Clicker Question #2

Can you write an algorithm to sort an array?

A) Yes | B) No | C) I don't know

## `sort_array`



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

Using our sort_array function from above, what will the following code snippet print out:



{:.input_area}
```python
data = ['a', 'c', 'b'] 
sort_array(data)
```





{:.output_data_text}
```
['a', 'b', 'c']
```



A) ['a', 'c', 'b'] | B) ['a', 'b', 'c'] | C) [97, 98, 99]| D) None | E) This code will fail

### Clicker Question #4

Using our sort_array function from above, what will the following code snippet print out:



{:.input_area}
```python
data = [True, False, True]
sort_array(data)
```





{:.output_data_text}
```
[False, True, True]
```



A) [False, True, True] | B) [True, False, True] | C) [0, 1, 1]]| D) [True, True, False] | E) This code will fail

### Clicker Question #5

Using our sort_array function from above, what will the following code snippet print out:



{:.input_area}
```python
data = [[3, 4], [1, 2]]
sort_array(data)
```





{:.output_data_text}
```
[[1, 2], [3, 4]]
```



A) [[3, 4], [1, 2]]  | B) [1, 2, 3, 4] | C) [[1, 2], [3, 4]]| D) None | E) This code will fail

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

- It will require n^2 steps, where n is the length of the list
- It will require ~double the memory of the original list

## Computability

Things that computers can do are things that we can write down an algorithm to do.

Things that we can write an algorithm to do are things that we can define a specific set of steps to complete.
