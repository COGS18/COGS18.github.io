---
interact_link: content/materials/Exam-Prep/COGS18_E1_Su20.ipynb
download_link: assets/downloads/COGS18_E1_Su20.ipynb.zip
title: 'E1_Su20_Answers'
prev_page:
  url: /materials/Exam-Prep/E1_Su20_Practice_Answers
  title: 'E1_Su20_Practice_Answers'
next_page:
  url: /materials/Exam-Prep/Exam2-Review
  title: 'Exam2-Review'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# COGS 18 - Exam 1

This is the first exam for Summer 2020. It covers topics through the Dictionaries Lecture.

This exam is out of 12.5 points, worth 12.5% of your grade.

**PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**

**PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE EXAM.** (Note that you can add additional cells, if you want to test things out.)

## Instructions

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

### Q1 - Variables (0.5 points)

In the cell below, write five lines of code that define five different variables named `var_float`, `var_str`, and `var_bool`, `var_tuple`, and `var_dict`, storing a float, a string, and a boolean, a tuple, and a dictionary, respectively. 

You get to choose the specific float, string, boolean, tuple, or dictionary each variable stores; however, they must satisify the following conditions:

- var_tuple must store numeric elements
- var_float must be less than the first element stored in `var_tuple`
- `var_dict` must have strings for its keys
- The first key in `var_dict` should be the string stored in `var_str`



{:.input_area}
```python
### BEGIN SOLUTION
# actual values stored will differ
var_float = 0.2
var_str = 'cogs18'
var_bool = False
var_tuple = (1, 2, 3)
var_dict = {var_str:1}
### END SOLUTION
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
assert var_str is not None

### BEGIN HIDDEN TESTS
assert isinstance(var_str, str)
### END HIDDEN TESTS
```




{:.input_area}
```python
assert var_bool is not None

### BEGIN HIDDEN TESTS
assert isinstance(var_bool, bool)
### END HIDDEN TESTS
```




{:.input_area}
```python
assert var_tuple is not None

### BEGIN HIDDEN TESTS
assert isinstance(var_tuple, tuple)
assert var_float < var_tuple[0]
### END HIDDEN TESTS
```




{:.input_area}
```python
assert var_dict is not None

### BEGIN HIDDEN TESTS
assert isinstance(var_dict, dict)
assert var_str == list(var_dict.keys())[0]
### END HIDDEN TESTS
```


### Q2 - Math Operators (1 point)

In the cell below, create three variables: `var_a`, `var_b`, and `var_c`.

These variables must satisfy the following requirements:
1. Each variable must be created using *at least two (2) different math operators* (but *can* use more than 2)
2. Each variable must store (return) the value 4 (or 4.0). 
3. Across the creation of these three variables, all seven of the math operators (`+`, `-`, `/`, `*`, `**`, `%`, `//`) discussed in class must be used *at least* once. 



{:.input_area}
```python
### BEGIN SOLUTION
# actual operations will differ
var_a = 3 ** 2 // 2 + 0
var_b = 4 + 3 - 3
var_c = (9 % 5) * 2 / 2 
### END SOLUTION
```




{:.input_area}
```python
assert var_a is not None

### BEGIN HIDDEN TESTS
assert var_a == 4
### END HIDDEN TESTS
```




{:.input_area}
```python
assert var_b is not None

### BEGIN HIDDEN TESTS
assert var_b == 4
### END HIDDEN TESTS
```




{:.input_area}
```python
assert var_c is not None

### BEGIN HIDDEN TESTS
assert var_c == 4
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- all seven operators are used (0.2)
- at least two operators used per variable (0.2)

=== END MARK SCHEME ===

### Q3 - Comparison Operators (1 point)

In the cell below, create three variables: `comp_a`, `comp_b`, and `comp_c`.

These variables must satisfy the following requirements:

1. Each variable must store (aka return) the Boolean `False`
2. Additional operators may also be used, but `comp_a` must use the `and` operator; `comp_b` must use the `or` operator, and `comp_c` must use the `not` operator. 
3. Each variable must be created using *at least two* of the comparison operators (`<`,`>`,`<=`,`>=`,`!=`,`==`).
4. All six comparison operators must show up in the cell below *at least once*.




{:.input_area}
```python
### BEGIN SOLUTION
# actual variable creation will differ
comp_a = 7 < 6 and 6 < 7
comp_b = 3 != 3 or 4 <= 3
comp_c = 3 == 3 and not 4 == 4
### END SOLUTION
```




{:.input_area}
```python
assert isinstance(comp_a, bool)

### BEGIN HIDDEN TESTS
assert not comp_a
### END HIDDEN TESTS
```




{:.input_area}
```python
assert isinstance(comp_b, bool)

### BEGIN HIDDEN TESTS
assert not comp_b
### END HIDDEN TESTS
```




{:.input_area}
```python
assert isinstance(comp_c, bool)

### BEGIN HIDDEN TESTS
assert not comp_c
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- all six operators are used (0.2)
- and, or, or not all used (0.2)

=== END MARK SCHEME ===


### Q4 - Membership Operators (0.5 points)

Using the following string and list provided, create two variables `memb_a` and `memb_b` that satisfy the following conditions:

1. `memb_a` must use the `not` operator to check membership in `my_string`. It should store (return) `False`.
2. `memb_b` must use the `in` operator to check membership in `my_list`. It should store (return) `True`. 
3. `memb_a` must refer to the `my_string` variable defined for you below. `memb_b` must refer to the `my_list` variable defined for you below.



{:.input_area}
```python
# these variables are defined for you - no need to change them
my_string = 'I love COGS 18!'
my_list = ['Assignments', 'Exams', 'CodingLabs']

### BEGIN SOLUTION
# actual operations will differ
memb_a = 'love' not in my_string
memb_b = 'Assignments' in my_list
### END SOLUTION
```




{:.input_area}
```python
assert isinstance(memb_a, bool)

### BEGIN HIDDEN TESTS
assert not memb_a
### END HIDDEN TESTS
```




{:.input_area}
```python
assert isinstance(memb_b, bool)

### BEGIN HIDDEN TESTS
assert memb_b
### END HIDDEN TESTS
```


### Q5 - Variables (1 point)

Consider each of the following scenarios and determine what type of collection (list, tuple, dictionary) would be best to use. For each scenario, store 'list', 'tuple' or 'dictionary' in the variable, depending upon which is best for the given scnenario. (Note: Capitalization and spelling matter.)


For example, for `scenario_A`, if you thought the correct answer were 'list' your answer in the answer cell would be:

```python
scenario_A = 'list'
```

Scenarios:

- `scenario_A` | You want to store the social security numbers (and only the social security numbers) for all the people who were injured at the Battle of Gettysburg.
- `scenario_B` | You want to create a record to keep track of the email addresses (and only the email addresses) of all the employees who work at Gettysburg National Park.
- `scenario_C` | You want to create registry to keep track of the names and email addresses of all the employees who work at the Gettysburg National Park. 
- `scenario_D` | You want to store information in such a way that you would be able to loop through all the people who work at Gettysburg National Park and call each person at their cell phone number to update them on a policy.



{:.input_area}
```python
### BEGIN SOLUTION
scenario_A = 'tuple'
scenario_B = 'list'
scenario_C = 'dictionary'
scenario_D = 'dictionary'
### END SOLUTION
```




{:.input_area}
```python
assert scenario_A in ['tuple', 'list', 'dictionary']

### BEGIN HIDDEN TESTS
assert scenario_A == 'tuple'
### END HIDDEN TESTS
```




{:.input_area}
```python
assert scenario_B in ['tuple', 'list', 'dictionary']

### BEGIN HIDDEN TESTS
assert scenario_B == 'list'
### END HIDDEN TESTS
```




{:.input_area}
```python
assert scenario_C in ['tuple', 'list', 'dictionary']

### BEGIN HIDDEN TESTS
assert scenario_C == 'dictionary'
### END HIDDEN TESTS
```




{:.input_area}
```python
assert scenario_D in ['tuple', 'list', 'dictionary']

### BEGIN HIDDEN TESTS
assert scenario_D == 'dictionary'
### END HIDDEN TESTS
```


## Part 2: Indexing  (1 point)

### Q6 - Indexing (0.5 points)

*Using the list `cogs18` provided below and indexing*, write the line of code you would use to index the list and return the specified output:

1. `['Geoff', 'Jose', 'Paul']`  (Store in `ind_a`)
2. `['Jose', 'Sylvia']` (Store in `ind_b`)
3. `['Prof', 'Sylvia', 'Taylor']` (Store in `ind_c`; ***use negative indexing***)



{:.input_area}
```python
# list below provided for you
cogs18 = ['Geoff', 'Jose', 'Paul', 'Prof', 'Sylvia', 'Taylor']

### BEGIN SOLUTION
ind_a = cogs18[:3]
ind_b = cogs18[1::3]
ind_c = cogs18[-3:]
### END SOLUTION
```




{:.input_area}
```python
assert isinstance(ind_a, list)

### BEGIN HIDDEN TESTS
assert ind_a == ['Geoff', 'Jose', 'Paul']
### END HIDDEN TESTS
```




{:.input_area}
```python
assert isinstance(ind_b, list)

### BEGIN HIDDEN TESTS
assert ind_b == ['Jose', 'Sylvia']
### END HIDDEN TESTS
```




{:.input_area}
```python
assert isinstance(ind_c, list)

### BEGIN HIDDEN TESTS
assert ind_c == ['Prof', 'Sylvia', 'Taylor']
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- does not hard code (0.25)
- negative indexing used when creating `ind_c` (0.1)

=== END MARK SCHEME ===

### Q7 - Dictionaries (0.5 points)

Create three variables ***using the dictionary `cogs18_dict` provided*** below and functions discussed in class that will store the variable specified:

1. `dict_a`: stores 'Prof'
2. `dict_b`: stores 'dict' (or, when printed: `<class 'dict'>`)
3. `dict_c`: stores `6`

Note: each variable's line of code must have `cogs18_dict` as part of your code. (1 point)



{:.input_area}
```python
cogs18_dict = {'Paul' : 'TA',  'Sylvia' : 'TA', 'Jose' : 'IA', 
               'Taylor': 'IA', 'Geoff': 'IA', 'Ellis' : 'Prof'}

### BEGIN SOLUTION
dict_a = cogs18_dict['Ellis']
dict_b = type(cogs18_dict)
dict_c = len(cogs18_dict)
### END SOLUTION
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
assert dict_c == 6
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===

- cogs18_dict referenced in all three variables (not hard-coded) (0.35)

=== END MARK SCHEME ===


## Part 3: Control Flow - Conditionals & Loops  (7.5 points)

### Q8 - `for` loop (2.5 points)

Store your first name as a string in the variable `my_name` and initialize a `counter` (use that variable name).

Then, write a `for` loop that loops through the letters of your first name, increasing the counter by one for each consonant (non-vowel) in your name. 

The value stored in the counter at the end of your loop’s execution should be the number of consonants in your first name. Be sure that 'B' and 'b' are counted as the same letter in your code.




{:.input_area}
```python
### BEGIN SOLUTION
# code will differ based on who is taking the exam
my_name = 'Shannon'
counter = 0

for char in my_name:
    char = char.lower()
    if char not in ['a', 'e', 'i', 'o', 'u']:
        counter += 1
### END SOLUTION
```




{:.input_area}
```python
assert isinstance(counter, int)
assert isinstance(my_name, str)

### BEGIN HIDDEN TESTS
count = 0

for char in my_name:
    char = char.lower()
    if char not in ['a', 'e', 'i', 'o', 'u']:
        count += 1
        
assert counter == count
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===

- counter & my_name created (0.25 points)
- for loop initialized correctly (0.25 points)
- capitalization accounted for (0.5 points)
- conditional correct (0.5 points)

=== END MARK SCHEME ===

### Q9 - `dictionary` (3.5 points)

Write code that will generate a dictionary `name_consonants` that stores each consonant letter in `my_name` (defined in previous question) as a key in the dictionary, and the number of times each consonant shows up in `my_name` as the letter's value. 

Noe that this code should run, regardless of what string is stored in `my_name`.

For example, `name_consonants` for 'Shannon' would return:

```
{'s': 1, 'h': 1, 'n': 3}
```

Note that if you have no consonants in your name, this code would still run, but would return an empty dictionary.



{:.input_area}
```python
### BEGIN SOLUTION
# output will differ based on who is taking the exam
name_consonants = {}

vowels = ['a', 'e', 'i', 'o', 'u']
            
for char in my_name:
    char = char.lower()
    if char not in vowels:
        if char not in name_consonants:
            name_consonants[char] = 1
        else:
            name_consonants[char] += 1            
### END SOLUTION
```




{:.input_area}
```python
assert isinstance(name_consonants, dict)

### BEGIN HIDDEN TESTS
check = {}
check_alt = {}

for char in my_name:
    if char not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        if char not in check:
            check[char] = 1
        else:
            check[char] += 1
print(check)

for char in my_name:
    char = char.lower()
    if char not in ['a','e', 'i', 'o', 'u']:
        if char not in check_alt:
            check_alt[char] = 1
        else:
            check_alt[char] += 1
print(check_alt)
            

assert name_consonants == check or name_consonants == check_alt
### END HIDDEN TESTS
```


{:.output_stream}
```
{'S': 1, 'h': 1, 'n': 3}
{'s': 1, 'h': 1, 'n': 3}

```

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===

- refers back to my_name variable (0.5 points)
- for loop initialized correctly (0.5 points)
- capitalization accounted for (0.5 points)
- conditional correct (0.5 points)
- dictionary incremented correctly (0.5 points)

=== END MARK SCHEME ===

### Q10 - Loops (1.5 points)

Write code that will loop through the `name_consonants` dictionary created in the previous question and store the sum of the values in the dictionary into `consonant_count`. (For the name Shannon, `consonant_count` would store 5).

Be sure your answer refers back to `name_consonants` defined in the previous question



{:.input_area}
```python
### BEGIN SOLUTION
# output will differ based on who is taking the exam
consonant_count = 0

for key in name_consonants:
    consonant_count += name_consonants[key]
### END SOLUTION
```




{:.input_area}
```python
assert consonant_count is not None

### BEGIN HIDDEN TESTS
check = 0

for key in name_consonants:
    check += name_consonants[key]
    
assert consonant_count == check
### END HIDDEN TESTS
```


##### **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===

- counter initialized (0.25)
- for loop correct (0.25)
- accessing dictionary/increase counter correct (0.5)

=== END MARK SCHEME ===

### Submit on Datahub

Good work - you're done!

Check your work, and then when you're ready, **submit on datahub**.

We will not have your exam until you click submit and see this show up under 'submitted assignments'.
