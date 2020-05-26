---
interact_link: content/materials/E2_Sp20-PartII_Answers.ipynb
download_link: assets/downloads/E2_Sp20-PartII_Answers.ipynb.zip
pdf_link: assets/pdf/E1_Sp20_PartII_Answers.pdf
layout: materials
title: 'E1_Sp20_PartII_Answers'
prev_page:
  url: /materials/E2_Sp20-PartI_Answers
  title: 'E2_Sp20_PartI_Answers'
next_page:
  url: /labs/CL2-Answers
  title: 'Coding Labs'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# COGS 18 - Exam 2 (Part II)

This is the second exam for Spring 2020. It covers topics through the Command Line Lecture.

This total exam is out of 20 points, worth 20% of your grade. 

Part II is worth 15 points.

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

 <span style="color: red;">Note: </span> There _is_ a chance for partial credit on some questions, so _some_ code is better than _no_ code. Even if it throws an error, having some code that partially answers the question will benefit you/your grade.

## Part 2: Functions (9 points)

### Q5 - Function execution (2 points)

The cell below includes a function that has been provided for you. After running the cell below (to define this function), execute (use) this function to create the following variables under the specified conditions:

1. `square_default` | execute the `square_all` function using the default parameter such that the output will carry out the function on a list of input values containing the integers 2, 3, and 4. 
2. `power_three` | Use the same input values as above, but this time, use the `square_all` function provided to raise all input values to the power 3
3. `out_4` | Execute the `square_all` function such that `out_4` will store a list with 4 values, each of which is the integer 4.



{:.input_area}
```python
def square_all(collection, power=2):
    
    square_list = []
    for val in collection:
        square_list.append(val**power)
    
    return square_list
```




{:.input_area}
```python
# BE SURE YOUR ANSWER IS IN THE CELL BELOW
# but you can use this cell to test/execute/check your thinking (optional)
```




{:.input_area}
```python
### BEGIN SOLUTION
square_default = square_all([2,3,4])
power_three = square_all([2,3,4], 3)
out_4 = square_all([2,2,2,2]) # this execution could differ
### END SOLUTION
```




{:.input_area}
```python
assert square_default is not None

### BEGIN HIDDEN TESTS
assert  square_default == [4,9,16]
### END HIDDEN TESTS
```




{:.input_area}
```python
assert power_three is not None

### BEGIN HIDDEN TESTS
assert power_three  == [8, 27, 64]
### END HIDDEN TESTS
```




{:.input_area}
```python
assert out_4 is not None

### BEGIN HIDDEN TESTS
assert out_4  == [4,4,4,4]
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

function executed appropriately for variable creation (aka not hard coded) (**1 point** ; 0.33 per function call)

=== END MARK SCHEME ===

### Q6 - `provide_info` (3 points)

Write a function `provide_info` that takes three parameters: `name`, `year`, and `school` .

Set the default value for `school` to be 'UCSD'.

This function should `return` the string "Hi. I'm `name`. I am a `year` at `school`." (where the variable names are replaced by the values input to the function upon execution).

For example, one possible execution of this function could return "Hi! I'm Shannon. I am a sophomore at UCSD."

Note: Be sure punctuation and spacing match that specified in the instructions.



{:.input_area}
```python
### BEGIN SOLUTION
def provide_info(name, year, school='UCSD'):
    output = "Hi. I'm " + name + '. I am a ' + year + ' at ' + school + '.'
    return output
### END SOLUTION
```




{:.input_area}
```python
# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)
```




{:.input_area}
```python
assert callable(provide_info)

### BEGIN HIDDEN TESTS
# Hi! and Hi. both accepted
assert provide_info(name = 'Taylor', year = 'junior', school = 'UCLA') == "Hi! I'm Taylor. I am a junior at UCLA." or provide_info(name='Taylor', year='junior', school = 'UCLA') == "Hi. I'm Taylor. I am a junior at UCLA."
### END HIDDEN TESTS
```




{:.input_area}
```python
# hidden tests for function above
### BEGIN HIDDEN TESTS
# Hi! and Hi. both accepted
# assure defaul parameter is correct
assert provide_info(name = 'Taylor', year = 'junior') == "Hi! I'm Taylor. I am a junior at UCSD." or provide_info(name='Taylor', year='junior') == "Hi. I'm Taylor. I am a junior at UCSD."
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===

partial credit for answer above:

- function defined correctly (**0.5 points**)
- 3 parameters specified (**0.5 points**)
- default parameter specified correctly (**0.5 points**)
- string concatenation attempted correctly (even if typos in string) (**1 point**)
- `return` statement included (**0.3 points**)

=== END MARK SCHEME ===

### Q7 - `count_int` (4 points)

Write a function `count_int` that will take a tuple or list as the input and count the number (count) of integer values in that tuple/list, returning this value from the function. 

For example, if 3 of the values in the input list were integers, the function would return 3.

Note: You can assume the input to this function will be a tuple or list and do *not* need to write code to check whether or not this is true.



{:.input_area}
```python
### BEGIN SOLUTION
def count_int(col):
    count = 0
    
    for val in col:
        if type(val) == int:
            count += 1
    
    return count
### END SOLUTION
```




{:.input_area}
```python
# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)
```




{:.input_area}
```python
assert callable(count_int)

### BEGIN HIDDEN TESTS
assert count_int((1,2,3,4,5,'string',4.4)) == 5
assert count_int([1,2,3,4,5,'string',4.4]) == 5
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

partial credit for answer above:

- function defined correctly (**0.5 points**)
- input parameter specified  (**0.5 points**)
- counter initialized (**0.5 points**)
- for loop (or equivalent) correct (**0.2 points**)
- conditional (or equivalent) correct (**0.3 points**)
- counter incremented correctly (**0.5 points**) 
- `return` statement included (**0.5 points**)

=== END MARK SCHEME ===

## Part 3: Objects & Classes (5 points)

### Q8 - objects (1 point)

In the cell below, import the `random` module so that you can use the `choice` function from the module. (Note: the `choice` function from the `random` module returns a single value from a collection at random.)

Use the `choice` function from the `random` module to randomly choose a value from `range(0,10)`.

Store the output from this operation in the variable `rand_int`



{:.input_area}
```python
### BEGIN SOLUTION
from random import choice
rand_int = choice(range(0,10))

# also valid:
# import random
# rand_int = random.choice(range(0,10))
### END SOLUTION
```




{:.input_area}
```python
assert rand_int is not None

### BEGIN HIDDEN TESTS
assert isinstance(rand_int, int)
assert rand_int in range(0,10)
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

**0.5 points** awarded if _either_ of the following are true:
- import statement correct 
- choice syntax correct

=== END MARK SCHEME ===

### Q9 - Classes (4 points)

Generate a class called `StudentInfo`.

This class should have four *instance attributes*: `name`, `year`, `school`, and `proj_grade`. 

This class must also have a single method: `follow_up`. This method should determine if `proj_grade` is 65 or below. If `proj_grade` is 65 or below, the method should return the name of the student as the key and their proj_grade as the value in a dictionary. (If the student has a grade above 65, this method should return an empty dictionary.)



{:.input_area}
```python
### BEGIN SOLUTION
class StudentInfo():
    
    def __init__(self, name, year, school, proj_grade):
        self.name = name
        self.year = year
        self.school = school
        self.proj_grade = proj_grade
        
    def follow_up(self):
        out = {}
        if self.proj_grade <= 65:
            out[self.name] = self.proj_grade
        return out
    
### END SOLUTION
```




{:.input_area}
```python
# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your class (optional)
```




{:.input_area}
```python
assert callable(StudentInfo)

### BEGIN HIDDEN TESTS
student1 = StudentInfo(name='Shannon', year='sophomore', school='UCSD', proj_grade=63)
student2 = StudentInfo(name='Josh', year='senior', school='UCSD', proj_grade=88)

# test attributes
assert student1.name == 'Shannon'
assert student1.school == 'UCSD'
assert student2.year == 'senior'
assert student2.proj_grade == 88
### END HIDDEN TESTS
```




{:.input_area}
```python
assert callable(StudentInfo.follow_up)

### BEGIN HIDDEN TESTS
# test method
assert student1.follow_up() == {'Shannon': 63}
assert student2.follow_up() == {}
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

partial credit for answer above:

- class defined correctly (**0.5 points**)
- instance attribute def correct  (**0.5 points**)
- `self` used correctly in instance attribute (**0.5 points**)
- method defined correctly (**0.5 points**)
- dictionary + conditional correct (**0.5 points**) 
- `return` statement included (**0.5 points**)

=== END MARK SCHEME ===

## Part 4: True & False (1 point)

For the statements below: depending upon whether the statement provided is True or False, store the appropriate boolean in the variable specified. 

For example, if the statement were:

`jupyter` | Jupyter Notebooks allow for text and code to be stored and executed in the same document.

your answer would be:

```python
jupyter = True
```

since, the statement above is `True` and the variable `jupyter` is what was specified at the start of the statement.

### Q10 - True/False (1 point)

Following the instructions & example above, store the appropriate boolean in the variable provided for each of the following statements:

- `class_names` | `BasketballGame` is a better class name than `basketball_game`
- `touch` | `touch` is a shell command that creates a new file
- `pwd` | `pwd` is a shell command that changes your current working directory
- `relative_paths` | relative paths specify location relative to the computer's root directory
- `objects` | In Python, everything is an object



{:.input_area}
```python
### BEGIN SOLUTION
class_names = True
touch = True
pwd = False
relative_paths = False
objects = True
### END SOLUTION
```




{:.input_area}
```python
assert class_names is not None

### BEGIN HIDDEN TESTS
assert class_names
### END HIDDEN TESTS
```




{:.input_area}
```python
assert touch is not None

### BEGIN HIDDEN TESTS
assert touch
### END HIDDEN TESTS
```




{:.input_area}
```python
assert pwd is not None

### BEGIN HIDDEN TESTS
assert not pwd
### END HIDDEN TESTS
```




{:.input_area}
```python
assert relative_paths is not None

### BEGIN HIDDEN TESTS
assert not relative_paths
### END HIDDEN TESTS
```




{:.input_area}
```python
assert objects is not None

### BEGIN HIDDEN TESTS
assert objects
### END HIDDEN TESTS
```


### Part II complete!

Good work - you're done with the second exam!

Check your work, and then when you're ready, **submit on datahub**.

We will not have your exam until you click submit and see this show up under 'submitted assignments'.
