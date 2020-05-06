---
interact_link: content/materials/E1_Sp20_Practice_Answers.ipynb
download_link: assets/downloads/E1_Sp20_Practice_Answers.ipynb.zip
pdf_link: assets/pdf/E1_Sp20_Practice_Answers.pdf
layout: materials
title: 'E1_Sp20_Practice_Answers'
prev_page:
  url: /materials/Exam1-Practice
  title: 'Exam1-Practice'
next_page:
  url: /materials/E1_Sp20_Answers
  title: 'E1-Answers'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# COGS 108 - Practice Exam

This is the practice exam for Spring 2020. It covers topics through the Encodings Lecture.

This exam is out of 0 points, worth 0% of your grade, but the real thing will be out of 20 points.

**PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**

**PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE ASSIGNMENT.** (Note that you can add additional cells, if you want to test things out.

## Instructions
^ these are the instructions you will see on your real exam

#### Timing
- The exam is designed to take you 50 minutes.
- There will be a 24 hour window during which you can complete this exam.
- If it takes you longer than 50 minutes, you're free to use that time.

#### The Rules
- You are to complete this exam on your own.
- This is open-notes & open-Google
- You may not talk to any humans about this exam. 
- The following are all *prohibited*:
    - text/phone/online chat communication
    - posting questions to a message board where a human could respond
    - asking anyone via any form about a question on this test directly
- Clarification questions will ***not*** be allowed and there will be no posting on Piazza about the exam at all. 
    - Piazza posts about the exam will not be answered and will be deleted. 
    - Students who post questions about the exam to Piazza are at risk of losing points on the exam.
    - If you are confused about wording, add a note to your exam explaining your confusion and how you interpreted the question. 
    - Note: This policy is b/c we are incapable of responding for 24h straight. This is the only way to make it fair across the board for students.

## Part 1: Variables & Operators (6 points)
^ The headers and point values correspond to the actual headers and point values you'll have for each section on your exam

### Example Q1 - Variables & Operators

#### Part 1 (0.6 points)

In the cell below, create three variables: `var_a`, `var_b`, and `var_c`.

These variables must satisfy the following requirements:

1. `var_a` must store a float (you get to choose the specific float)
2. `var_b` must use *at least two* of the comparison operators (`<`,`>`,`<=`,`>=`,`!=`,`==`) and store (return) the value `True`. 
3. `var_c` must use *at least two* of the math operators (`+`, `-`, `/`, `*`, `**`, `%`, `//`) and store the value 36



{:.input_area}
```python
# actual variable creation will differ
var_a = 7.3
var_b = 6 == 6 and 3 <= 4
var_c = (6 + 3) * 4
```




{:.input_area}
```python
# check variable exists
assert var_a is not None

### BEGIN HIDDEN TESTS
assert isinstance(var_a, float)
### END HIDDEN TESTS
```




{:.input_area}
```python
assert isinstance(var_b, bool)

### BEGIN HIDDEN TESTS
assert var_b 
### END HIDDEN TESTS
```




{:.input_area}
```python
# check variable exists
assert var_c is not None

### BEGIN HIDDEN TESTS
assert var_c == 36
### END HIDDEN TESTS
```


#### Part 2 (0.4 points)

In the cell below explain, for the `var_b` you created in Part I, explain in words what your code is doing and the logic behind it. 

=== BEGIN MARK SCHEME ===

- logic of operators used explained correctly (0.2)
- two comparison operators used (0.2)

=== END MARK SCHEME ===


Answer: In my creation of `var_b` (`var_b = 6 == 6 and 3 <= 4`) I tested whether the value 6 is equal to 6 (which it is, so the left side of the `and` will be `True`. On the right hand side, I test whether 3 is less than or equal to 4, which is also True, this `True and True` will be True.


## Part 2: Indexing  (3 points)

### Example Q2 - Indexing

Given a the list `my_list` provided below, include code below *using indexing* to return the values specified below from `my_list`.


1. In `list_a`, index `my_list` such that it will store (return) `['c', 'd']`
2. In `list_b`, index `my_list` such that it will store (return) `['a', 'c', 'e']`



{:.input_area}
```python
# my_list is provided for you
my_list = ['a', 'b', 'c', 'd', 'e']

# specific indexing approaches may differ
list_a = my_list[2:4]
list_b = my_list[0::2]
```




{:.input_area}
```python
assert isinstance(list_a, list)

### BEGIN HIDDEN TESTS
assert list_a == ['c', 'd']
### END HIDDEN TESTS
```




{:.input_area}
```python
assert isinstance(list_b, list)

### BEGIN HIDDEN TESTS
assert list_b == ['a', 'c', 'e']
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===

- list_a indexed and not hard coded

=== END MARK SCHEME ===


## Part 3: Control Flow - Conditionals & Loops  (11 points)

### Example Q3 - `while` loop

Include code in your answer below that:

1. Creates (initializes) a counter `counter` that starts at 0
2. Creates (initializes) an empty list `out`
3. Creates a loop that will run as long as the value of `counter` is less than or equal to 10
    - Within the loop:
        - first: if the value of `counter` is odd, `append` the value of `counter` to the list `out`
        - then: increase the value of `counter` by 1 each time through the loop 



{:.input_area}
```python
out = []
counter = 0 

while counter <= 10: 
    if counter % 2 != 0:
        out.append(counter)

    counter += 1

```




{:.input_area}
```python
assert counter > 0 & counter < 100

### BEGIN HIDDEN TESTS
assert counter == 11
### END HIDDEN TESTS
```




{:.input_area}
```python
assert isinstance(out, list)

### BEGIN HIDDEN TESTS
assert out == [1, 3, 5, 7, 9]
### END HIDDEN TESTS
```


### Submit on Datahub

Good work - you're done!

Check your work, and then when you're ready, **submit on datahub**.

We will not have your exam until you click submit and see this show up under 'submitted assignments'.
