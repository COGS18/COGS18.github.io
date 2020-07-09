---
interact_link: content/materials/Exam-Prep/E1_Su20_Practice_Answers.ipynb
download_link: assets/downloads/E1_Su20_Practice_Answers.ipynb.zip
title: 'E1_Su20_Practice_Answers'
prev_page:
  url: /materials/Exam-Prep/Exam1-Practice
  title: 'Exam1-Practice'
next_page:
  url: /labs/source_Su20/CL1-Tooling
  title: 'Coding Labs'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# COGS 18 - Practice Exam

This is the practice Exam I for Summer 2020. It covers topics through the Dictionaries Lecture.

This exam is out of 0 points, worth 0% of your grade, but the real thing will be out of 12.5 points.

**PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**

**PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE EXAM.** (Note that you can add additional cells, if you want to test things out.)

## Instructions
^ these are the instructions you will see on your real exam

#### Timing
- The exam is designed to take you ~1 hour.
- There will be a 24 hour window during which you can complete this exam.
- If it takes you longer than 1 hour, you're free to use that time.

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

 <span style="color: red;">Note: </span> There _is_ a chance for partial credit on some questions, so _some_ code is better than _no_ code. Even if it throws an error, having some code that partially answers the question will benefit you/your grade.

## Part 1: Variables & Operators (4 points)
^ The headers and point values correspond to the actual headers and point values you'll have for each section on your exam

### Example Q1 - Variables & Operators

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
assert var_b is not None

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


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


## Part 2: Indexing  (1 point)

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

## Part 3: Control Flow - Conditionals & Loops  (7.5 points)

### Example Q3 - `while` loop

Include code in your answer below that uses a `while` loop to loop through all the values between 0 and 20. Within the loop, store all of the odd values in the list  `out`.



{:.input_area}
```python
out = []
counter = 0 

while counter <= 20: 
    if counter % 2 != 0:
        out.append(counter)

    counter += 1

```




{:.input_area}
```python
assert isinstance(out, list)

### BEGIN HIDDEN TESTS
assert out == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
### END HIDDEN TESTS
```


### Submit on Datahub

Good work - you're done!

Check your work, and then when you're ready, **submit on datahub**.

We will not have your exam until you click submit and see this show up under 'submitted assignments'.
