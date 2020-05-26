---
interact_link: content/materials/E2_Sp20-PartI_Answers.ipynb
download_link: assets/downloads/E2_Sp20-PartI_Answers.ipynb.zip
pdf_link: assets/pdf/E2_Sp20_PartI_Answers.pdf
layout: materials
title: 'E2_Sp20_PartI_Answers'
prev_page:
  url: /materials/E2_Practice_Sp20-PartII-Answers
  title: 'E2_Practice_Sp20-PartII-Answers'
next_page:
  url: /materials/E2_Sp20-PartII_Answers
  title: 'E1_Sp20_PartII_Answers'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# COGS 18 - Exam 2 (Part I)

This is the second exam for Spring 2020. It covers topics through the Command Line Lecture.

This total exam is out of 20 points, worth 20% of your grade. 

Part I is worth 5 points.

**PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**

**PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE EXAM.** (Note that you can add additional cells, if you want to test things out.

## Instructions

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

## Part 1: E1 Review (5 points)

### Q1 - Variables & Operators (1 point)

In the cell below, create three variables: `var_math`, `var_comp`, and `var_memb`.

Additional variables can be created and additional operators used, but the following three variables must be created and satisfy the following requirements:
1. `var_math` must use *at least three* of the seven of the math operators (`+`, `-`, `/`, `*`, `**`, `%`, `//`) and should store (return) the value 12 (or 12.0)
2. `var_comp` must be created using *at least three* of the comparison operators (`<`,`>`,`<=`,`>=`,`!=`,`==`) and store (return) the value `False`
3. `var_memb` must use a membership operator (`in`, `not in`) to check whether a string is in a list and return the value `True`. (You get to specify the specific string and the specific list used in your answer.)



{:.input_area}
```python
### BEGIN SOLUTION
# actual operations will differ
var_math = 12 * 2 + 2 - 14
var_comp = 7 < 6 and (6==6 or 7!=6)
var_memb = 'string' in [1,2,'string']
### END SOLUTION
```




{:.input_area}
```python
assert var_math is not None

### BEGIN HIDDEN TESTS
assert var_math == 12
### END HIDDEN TESTS
```




{:.input_area}
```python
assert var_comp is not None

### BEGIN HIDDEN TESTS
assert not var_comp
### END HIDDEN TESTS
```




{:.input_area}
```python
assert var_memb is not None

### BEGIN HIDDEN TESTS
assert var_memb
### END HIDDEN TESTS
```


### Q2 - Variables & Indexing (1 point)

Define a list `my_list` that stores 9 items: 3 integers, 3 strings, 2 booleans, and 1 float (in any order).

Then, write code that stores the following elements of that list.

1. Store the second element of `my_list` list through to the end of the list in the variable `list_a`
2. Store the last element of `my_list` in the variable `list_b`

Note: "element" refers to the position in the list - so the element at index 0 is the *first* element in any list.



{:.input_area}
```python
### BEGIN SOLUTION
my_list = [1, 2, 3, 'a', 'b', 'c', True, False, 1.0]
list_a = my_list[1:]
list_b = my_list[-1]
### END SOLUTION
```




{:.input_area}
```python
assert my_list is not None

### BEGIN HIDDEN TESTS
assert len(my_list) == 9

# check for specific type satistfied
num_int = 0
num_str = 0
num_bool = 0
num_float = 0

for el in my_list: 
    if type(el) == int: 
        num_int += 1
    if type(el) == str:
        num_str += 1
    if type(el) == bool:
        num_bool += 1
    if type(el) == float:
        num_float += 1
               
assert num_int == 3
assert num_str == 3
assert num_bool == 2
assert num_float == 1
### END HIDDEN TESTS
```




{:.input_area}
```python
assert list_a is not None

### BEGIN HIDDEN TESTS
assert list_a == my_list[1:]
### END HIDDEN TESTS
```




{:.input_area}
```python
assert list_b is not None

### BEGIN HIDDEN TESTS
assert list_b == my_list[-1]
### END HIDDEN TESTS
```


### Q3 - Loops (1 point)

Write code that will extract the strings from the `my_list` you created in the previous question, storing these values in to a new list called `list_str`.



{:.input_area}
```python
### BEGIN SOLUTION
# output will differ based on who is taking the exam
list_str = []
for el in my_list:
    if type(el) == str:
        list_str.append(el)
### END SOLUTION
```




{:.input_area}
```python
assert list_str is not None

### BEGIN HIDDEN TESTS
assert isinstance(list_str, list)
assert isinstance(list_str[0], str)
### END HIDDEN TESTS
```


### Q4 - Writing code to accomplish a task (2 points)

`grades` provided below stores the names of (fictional) students and their final project scores. Use this dictionary  to complete this task. (In other words, run that cell and use `grades` in your answer.)

**The task**: Write code that will programmatically determine which students got passing grades (defined as grades of 65 or higher) _and_ whose score was *odd*. 

The names of the students who match _both_ of these criteria should be stored in a list called `student_out`

Your response should use code constructs discussed in class (i.e conditionals, loops, operators, etc.) to carry out the process specified. You should *not* "hard-code" the answer.



{:.input_area}
```python
# The following dictionary provided for you
grades = {'Amir': 91,
         'Quynh': 80,
         'George': 67,
         'Camilla': 92,
         'Rachel': 98,
         'Sebi': 83,
         'Alma': 95,
         'Paul': 63,
         'Jessica': 65}
```




{:.input_area}
```python
### BEGIN SOLUTION
student_out = [] 

for val in grades:
    if grades[val] % 2 != 0 and grades[val] >= 65:
        student_out.append(val)
student_out
### END SOLUTION
```





{:.output_data_text}
```
['Amir', 'George', 'Sebi', 'Alma', 'Jessica']
```





{:.input_area}
```python
assert student_out is not None

### BEGIN HIDDEN TESTS
assert 'Rachel' not in student_out
### END HIDDEN TESTS
```




{:.input_area}
```python
assert isinstance(student_out, list)

### BEGIN HIDDEN TESTS
assert 'Jessica' in student_out
### END HIDDEN TESTS
```


### Part I complete!

Good work - you're done with the first part of the exam!

Check your work and then move onto complete Part II of the exam.
