---
interact_link: content/materials/E1_Sp20_Answers.ipynb
download_link: assets/downloads/E1_Sp20_Answers.ipynb.zip
pdf_link: assets/pdf/E1-Answers.pdf
layout: materials
title: 'E1-Answers'
prev_page:
  url: /materials/E1_Sp20_Practice_Answers
  title: 'E1_Sp20_Practice_Answers'
next_page:
  url: /labs/CL2-Answers
  title: 'Coding Labs'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
### Regrades:

- Explanation of grading
- Prof Ellis will handle all regrades

Regrades are for: 
- Places where you followed instructions and lost points anyway

Regrades are *NOT* for:
- Partial credit on questions that did not have partial credit
- Places where you forgot to answer a question
- Places where you don't like how points were distributed

### E2

- will be cumulative, but will be focused on new material (Functions & Classes)
- The average between your score on the "E1" material on E2 and your first exam can be used to replace your E1 score
- I care that you know the stuff. You care about knowing the stuff and your grades. So, this is win-
- This will happen automatically. This will only be used to help students. No students will lose points as a result.

# COGS 18 - Exam 1 (Answers)

This is the first exam for Spring 2020. It covers topics through the Encodings Lecture.

This exam is out of 20 points, worth 20% of your grade.

**PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**

**PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE ASSIGNMENT.** (Note that you can add additional cells, if you want to test things out.

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

 <span style="color: red;">Note: </span> There _is_ a chance for partial credit on some questions, so _some_ code is better than _no_ code. Even if it throws an error, having some code that partially answers the question will benefit you/your grade.

## Part 1: Variables & Operators (6 points)

### Q1 - Variables

In the cell below, write five lines of code that define five different variables named `var_float`, `var_str`, and `var_bool`, `var_tuple`, and `var_dict`, storing a float, a string, and a boolean, a tuple, and a dictionary, respectively. (You get to choose the specific float, string, boolean, tuple, or dictionary each variable stores.) (1 pt):



{:.input_area}
```python
# actual values stored will differ
var_float = 9.29
var_str = 'cogs18'
var_bool = False
var_tuple = (1, 2, 3)
var_dict = {'a':1}

```




{:.input_area}
```python
# check variable exists
assert var_float is not None

### BEGIN HIDDEN TESTS
assert isinstance(var_float, float)
### END HIDDEN TESTS
```




{:.input_area}
```python
# check variable exists
assert var_str is not None

### BEGIN HIDDEN TESTS
assert isinstance(var_str, str)
### END HIDDEN TESTS
```




{:.input_area}
```python
# check variable exists
assert var_bool is not None

### BEGIN HIDDEN TESTS
assert isinstance(var_bool, bool)
### END HIDDEN TESTS
```




{:.input_area}
```python
# check variable exists
assert var_tuple is not None

### BEGIN HIDDEN TESTS
assert isinstance(var_tuple, tuple)
### END HIDDEN TESTS
```




{:.input_area}
```python
assert var_dict is not None

### BEGIN HIDDEN TESTS
assert isinstance(var_dict, dict)
### END HIDDEN TESTS
```


### Q2 - Operators

In the cell below, explain the difference between the equality operator and the assignment operator, being sure to state what character(s) is/are used for which in Python. Feel free to explain using examples of when each would be used (0.5 points).

=== BEGIN MARK SCHEME ===

- correct operators chosen for each (0.2)
- explanations make sense (0.3)

=== END MARK SCHEME ===

Answer: Equality operator (`==`) checks whether the two sides are equal, while the asignment operator (`=`) assigns the value on the right to the variable on the left. 

### Q3 - Math Operators

#### Part 1 (1.5 points)

In the cell below, create three variables: `var_a`, `var_b`, and `var_c`.

These variables must satisfy the following requirements:
1. Each variable must be created using *at least two (2) different math operators* (but *can* use more than 2)
2. Each variable must store (return) the value 6 (or 6.0). 
3. Across the creation of these three variables, all seven of the math operators (`+`, `-`, `/`, `*`, `**`, `%`, `//`) discussed in class must be used *at least* once. 



{:.input_area}
```python
# actual operations will differ
var_a = 3 ** 2 // 2 + 2
var_b = 6 + 3 - 3
var_c = (20 % 7) * 2 // 2 
```




{:.input_area}
```python
assert var_a

### BEGIN HIDDEN TESTS
assert var_a == 6
### END HIDDEN TESTS
```




{:.input_area}
```python
assert var_b

### BEGIN HIDDEN TESTS
assert var_b == 6
### END HIDDEN TESTS
```




{:.input_area}
```python
assert var_c

### BEGIN HIDDEN TESTS
assert var_c == 6
### END HIDDEN TESTS
```


#### Part 2 (0.5 points)

In the cell below explain, for a variable you created in Part I of this question that uses the `%` operator, explain in words/math terms below the mathematical operations you carried out to create that variable, being sure to explain what each math operator you used accomplishes. 

=== BEGIN MARK SCHEME ===

- correctly explains what the % operator does (0.3)
- all seven operators are used (0.1)
- at least two perators used per variable (0.1)

=== END MARK SCHEME ===

Answer: In creating `var_c` (`var_c = (20 % 7) * 2 // 2`), I first divided 20 by 7 using hte modulo, which keeps the remainder from this equation (6). This value was then multipled (`*`) by 2, storing 12. Finally floor division (`//`) was carried out dividing that value by 2, storing the integer of 12 divided by 2.

### Q4 - Comparison Operators

#### Part 1 (0.6 points)

In the cell below, create three variables: `comp_a`, `comp_b`, and `comp_c`.

These variables must satisfy the following requirements:

1. Each variable must store (aka return) the Boolean `True`
2. Additional operators may also be used, but `comp_a` must use the `and` operator; `comp_b` must use the `or` operator, and `comp_c` must use the `not` operator. 
3. Each variable must be created using *at least two* of the comparison operators (`<`,`>`,`<=`,`>=`,`!=`,`==`).
4. All six comparison operators must show up in the cell below *at least once*.




{:.input_area}
```python
# actual variable creation will differ
comp_a = 7 > 6 and 6 < 7
comp_b = 3 <= 3 or 4 <= 3
comp_c = 3 == 3 and not 3 != 3
```




{:.input_area}
```python
assert isinstance(comp_a, bool)

### BEGIN HIDDEN TESTS
assert comp_a
### END HIDDEN TESTS
```




{:.input_area}
```python
assert isinstance(comp_b, bool)

### BEGIN HIDDEN TESTS
assert comp_b
### END HIDDEN TESTS
```




{:.input_area}
```python
assert isinstance(comp_c, bool)

### BEGIN HIDDEN TESTS
assert comp_c
### END HIDDEN TESTS
```


#### Part 2 (0.4 points)

In the cell below explain, for a variable you created in Part I that uses the `not` operator, explain in words what your code is doing and the logic behind it. 

=== BEGIN MARK SCHEME ===

- logic of not operator explained correctly (0.2)
- all six operators are used (0.1)
- and, or, or not all used (0.1)

=== END MARK SCHEME ===


Answer: In creating `comp_c` (`comp_c = 3 == 3 and not 3 != 3`) the left hand sice checks whether 3 is equal to 3 (which it is - `True`) and the right hand sice checks that 3 is *not* equal to 3 (which is `False`) but the `not` negates that, so this side stores (`True`). Because there is an `and`, `True and True`, returns `True`.

### Q5 - Membership Operators (0.5 points)

Using the following string and list provided, create two variables `memb_a` and `memb_b` that satisfy the following conditions:

1. `memb_a` must use the `in` operator to check membership in `my_string`. It should store (return) `True`.
2. `memb_b` must use the `not in` operator to check membership in `my_list`. It should store (return) `False`. 
3. `memb_a` must refer to the `my_string` variable defined for you below. `memb_b` must refer to the `my_list` variable defined for you below.



{:.input_area}
```python
# these variables are defined for you - no need to change them
my_string = 'I love COGS 18!'
my_list = ['Assignments', 'Exams', 'CodingLabs']

# actual operations will differ
memb_a = 'love' in my_string
memb_b = 'Assignments' not in my_list
```




{:.input_area}
```python
assert isinstance(memb_a, bool)

### BEGIN HIDDEN TESTS
assert memb_a
### END HIDDEN TESTS
```




{:.input_area}
```python
assert isinstance(memb_b, bool)

### BEGIN HIDDEN TESTS
assert not memb_b
### END HIDDEN TESTS
```


### Q6 - Variables

In your own words, describe the difference between a list, a tuple, and a dictionary. Explain a situation/use an real-world example to describe where you would use each type of variable. (1 point)

=== BEGIN MARK SCHEME ===

- explanation of tuples, lists, and dictionaries correct (0.6)
- examples make sense (0.4)

=== END MARK SCHEME ===

Answer:

- Lists are ordered, mutable objects, created using square brackets, to store elements in sequence. (Example: You want to store True for students who have completed an assignment and False for students who haven't. You want to be able to update this when a student turns something in, so you use a list.
- Types are ordered, immutable objects, created using parentheses, to store elements in sequence. (Example: if you wanted to store Social security numbers - you know these will never change for an individual, so you use a tuple to ensure they are not changed later in your code.)
- Dictionaries are mutable objects, created using curly braces, to store key-value pairs. (Example: If you wanted to look up a friend's phone number using their name - their name would be the key, and the phone number would be the value. The dictionary would store all your friends.)

## Part 2: Indexing  (3 points)

### Q7 - Indexing

#### Part 1 (0.6 points)

*Using the list `cogs18` provided below and indexing*, write the line of code you would use to index the list and return the specified output:

1. `['Annie', 'Mudit', 'Melody']`  (Store in `ind_a`)
2. `['Ashlesha', 'Mudit','Fidella', 'Geoff']` (Store in `ind_b`)
3. `['AP', 'Griffin', 'Geoff']` (Store in `ind_c`; ***use negative indexing***)



{:.input_area}
```python
# list below provided for you
cogs18 = ['Ashlesha', 'Paul', 'Annie', 'Mudit', 'Melody', 'Jitarth',
          'Fidella', 'AP', 'Griffin', 'Geoff']

### BEGIN SOLUTION
ind_a = cogs18[2:5]
ind_b = cogs18[::3]
ind_c = cogs18[-3:]
### END SOLUTION
```




{:.input_area}
```python
assert isinstance(ind_a, list)

### BEGIN HIDDEN TESTS
assert ind_a == ['Annie', 'Mudit', 'Melody']
### END HIDDEN TESTS
```




{:.input_area}
```python
assert isinstance(ind_b, list)

### BEGIN HIDDEN TESTS
assert ind_b == ['Ashlesha', 'Mudit', 'Fidella', 'Geoff']
### END HIDDEN TESTS
```




{:.input_area}
```python
assert isinstance(ind_c, list)

### BEGIN HIDDEN TESTS
assert ind_c == ['AP', 'Griffin', 'Geoff']
### END HIDDEN TESTS
```


#### Part 2 (0.4 points)

In the cell below, explain in your own words what your code for creating `ind_c` accomplishes.

=== BEGIN MARK SCHEME ===

- explanation of `ind_c` correct (0.2)
- negative indexing used when creating `ind_c` (0.2)

=== END MARK SCHEME ===

Answer: When I create `ind_c` (`ind_c = cogs18[-3:]`), I'm specifying that I want to go to the third position from the end of the `cogs18` list and return every element until the end of the list.


### Q8 - Indexing

Given a theoretical list `my_list`, include code below using indexing to satisfy each of the following conditions


1. Store the fifth element of `my_list` list in the variable `list_a`
2. Store the second element ***from the end*** of `my_list` in the variable `list_b`
3. Store the fourth element of `my_list` through to the last element of the list in `list_c`

Note: "element" refers to the position in the list - so the element at index 0 is the *first* element in any list.

Note, your code should work for any list. It does not matter what the contents of `my_list` are. So, you should not create a list `my_list` in your answer. The test cells will create this list. You only need to write the three lines of code storing the three variables `list_a`, `list_b`, and `list_c`. (1 point)



{:.input_area}
```python
%%writefile q8_code.py
# You can ignore the line above - it is used to help check your code

list_a = my_list[4]
list_b = my_list[-2]
list_c = my_list[3:]

```


{:.output_stream}
```
Writing q8_code.py

```



{:.input_area}
```python
# this cell included for you to write tests of your own if you'd like. (optional)
# reminder: `%run -i ./q8_code.py` will run the code you stored above
```




{:.input_area}
```python
# hidden tests for `list_a`
### BEGIN HIDDEN TESTS
my_list = list(range(0,15))
%run -i ./q8_code.py 
assert list_a == 4
### END HIDDEN TESTS
```




{:.input_area}
```python
# hidden tests for `list_b`
### BEGIN HIDDEN TESTS
assert list_b == 13
### END HIDDEN TESTS
```




{:.input_area}
```python
# hidden tests for `list_c`
### BEGIN HIDDEN TESTS
assert list_c == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
### END HIDDEN TESTS
```


### Q9 - Dictionaries

Create three variables ***using the dictionary `cogs18_dict` provided*** below and functions discussed in class that will store the variable specified:

1. `dict_a`: stores 'Prof'
2. `dict_b`: stores 'dict' (or, when printed: `<class 'dict'>`)
3. `dict_c`: stores `5`

Note: each variable's line of code must have `cogs18_dict` as part of your code. (1 point)



{:.input_area}
```python
cogs18_dict = {'Annie' : 'TA',  'Ashlesha' : 'TA', 'Paul' : 'TA', 'Mudit': 'TA', 'Ellis' : 'Prof'}

dict_a = cogs18_dict['Ellis']
dict_b = type(cogs18_dict)
dict_c = len(cogs18_dict)
```




{:.input_area}
```python
assert dict_a

### BEGIN HIDDEN TESTS
assert dict_a == 'Prof'
### END HIDDEN TESTS
```




{:.input_area}
```python
assert dict_b

### BEGIN HIDDEN TESTS
assert dict_b == dict
### END HIDDEN TESTS
```




{:.input_area}
```python
assert dict_c

### BEGIN HIDDEN TESTS
assert dict_c == 5
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===

- cogs18_dict referenced in all three variables (not hard-coded)

=== END MARK SCHEME ===


## Part 3: Control Flow - Conditionals & Loops  (11 points)

### Q10 - `while` loop

Include code in your answer below that:

1. Creates (initializes) a counter `val` that starts at 0
2. Creates (initializes) an empty list `output`
3. Creates a loop that will run as long as the value of `val` is less than or equal to 100
    - Within the loop:
        - first: if the value of `val` is divisible by 10, `append` the value of `val` to the list `output`
        - then: increase the value of `val` by 1 each time through the loop
    
(2 points)
    




{:.input_area}
```python
output = []
val = 0 

while val <= 100: 
    if val % 10 == 0:
        output.append(val)
    
    val += 1
```




{:.input_area}
```python
assert val > 0 & val < 200

### BEGIN HIDDEN TESTS
assert val == 101
### END HIDDEN TESTS
```




{:.input_area}
```python
assert isinstance(output, list)

### BEGIN HIDDEN TESTS
assert output == [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100] or output == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
### END HIDDEN TESTS
```


### Q11 - `for` loop

Store your first name as a string in the variable `my_name` and initialize a `counter` (use that variable name) 

Then, write a `for` loop that loops through the letters of your first name, increasing the counter by one for each letter in your name. The value stored in the counter at the end of your loop’s execution should be the number of letters in your first name.

(2 points)



{:.input_area}
```python
# code will differ based on who is taking the exam
my_name = 'Shannon'
counter = 0

for char in my_name:
    counter += 1
```




{:.input_area}
```python
assert isinstance(counter, int)
assert isinstance(my_name, str)

### BEGIN HIDDEN TESTS
assert len(my_name) == counter
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===

- partial credit for answer above
- counter & my_name created (0.5 points)
- for loop initialized correctly (0.5 points)

=== END MARK SCHEME ===

### Q12 - `dictionary`

Programmatically (meaning: write python code), generate a dictionary `name_dict` that stores each unique letter in your name as a different key, and the number of times each letter shows up in your name as the letter's value. 

For example, `name_dict` for 'Shannon' would return:

```
{'S':1, 'h':1, 'a': 1, 'n': 3, 'o': 1}
```

To refer to your name, use the `my_name` variable created in your previous response. (3 points)



{:.input_area}
```python
# code will differ based on who is taking the exam
name_dict = {}

for char in my_name:
    if char not in name_dict:
        name_dict[char] = 1
    else:
        name_dict[char] += 1        
```




{:.input_area}
```python
assert isinstance(name_dict, dict)

### BEGIN HIDDEN TESTS
assert len(name_dict) == len(list(set(my_name.lower()))) or len(name_dict) == len(list(set(my_name)))
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===

- code references `my_name` (1 pt)
- code calculates integers programmatically / not hard-coded (1 pt)

=== END MARK SCHEME ===


### Q13 - `for` loop

Write a `for` loop that would loop through a hypothetical list `best_list`, storing any integers in the list in a list called `best_out_list`. Variables of any other type are not to be included in the output. (2 points)



{:.input_area}
```python
%%writefile q13_code.py
# You can ignore the line above - it is used to help check your code

best_out_list = []

for val in best_list:
    #if type(val) == int:
    if isinstance(val, int):
        best_out_list.append(val)
```


{:.output_stream}
```
Overwriting q13_code.py

```



{:.input_area}
```python
# this cell included for you to write tests of your own if you'd like. (optional)
# reminder: `%run -i ./q13_code.py` will run the code you stored above
```




{:.input_area}
```python
# hidden tests for Q13
### BEGIN HIDDEN TESTS
best_list = ['17', 5, 6, 7, 'help', 13.3]

%run -i ./q13_code.py 
assert best_out_list == [5, 6, 7]
### END HIDDEN TESTS
```


### Q14 - variable encoder

In your second assignment, you generated a number of different types of encoders and decoders. In this assignment, you wrote code to create an encoder with variable keys that would have included code like the following:

```python
key = start_key
encoded = ''
for char in message:
    encoded = encoded + chr(ord(char) + key)
    key = key + key_increment
```

In your own words below, explain what this code accomplished. (2 points)

=== BEGIN MARK SCHEME ===

- variable encoder explanation correct (0.5)
- ord() and chr() explanation correct (0.5)
- key explained correctly (0.5)
- extending a string explained (0.5)

=== END MARK SCHEME ===

Answer: 

- This code creates a variable `key` which stores the value in `start_key`
- It creates an empty string `encoded`
- It loops through every `char` (character) in a `message`
    - For each `char` it takes the unicode value of `char` (which is a number) and adds the value specified in `key` to that number. Then, `chr` converst that new number back to a character. This is added to the growing string `encoded`.
    - `key` is then increased by the value specified in `key_increment`. This value is used the next time through the loop, allowing for a different `key` value to be used for each character in our `message`

### Submit on Datahub

Good work - you're done!

Check your work, and then when you're ready, **submit on datahub**.

We will not have your exam until you click submit and see this show up under 'submitted assignments'.
