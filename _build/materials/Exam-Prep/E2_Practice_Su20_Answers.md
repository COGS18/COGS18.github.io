---
interact_link: content/materials/Exam-Prep/E2_Practice_Su20_Answers.ipynb
download_link: assets/downloads/E2_Practice_Su20_Answers.ipynb.zip
title: 'E2_Practice_Su20_Answers'
prev_page:
  url: /materials/Exam-Prep/Exam2-Practice
  title: 'Exam2-Practice'
next_page:
  url: /labs/source_Su20/CL1-Tooling
  title: 'Coding Labs'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# COGS 18 - Exam 2

This is the second exam for Summer 2020. It covers topics through the Namespace Lecture.

This is worth 0 points and worth 0% of your grade, but the real total exam is out of 12.5 points, worth 12.5% of your grade. 

**PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**

**PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE ASSIGNMENT.** (Note that you can add additional cells, if you want to test things out.

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

## Part 1: E1 Review (2.25 points)

There will be 3 questions on Part I, as specified below, with these point values.

To review for this part of the exam, review Exam 1 and Practice Exam 1

### Q1 - Variables & Indexing (0.75 points)


### Q2 - Loops (0.5 points)


### Q3 - Writing code to accomplish a task (1 point)


## Part 2: Functions (5.25 points)

### Q4 - Function execution (0.75 points)

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
assert  square_default == [4, 9, 16]
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
assert out_4  == [4, 4, 4, 4]
### END HIDDEN TESTS
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
NameError                                 Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-1-1861846acf6c> in <module>()
----> 1 assert out_4 is not None
      2 
      3 ### BEGIN HIDDEN TESTS
      4 assert out_4  == [4, 4, 4, 4]
      5 ### END HIDDEN TESTS

```

{:.output_traceback_line}
```
NameError: name 'out_4' is not defined
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

function executed appropriately for variable creation (aka not hard coded) (**1 point** ; 0.33 per function call)

=== END MARK SCHEME ===

### Q5 - `count_int` (2 points)

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
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

Rubric used in grading specified here

=== END MARK SCHEME ===

### Q6 - `provide_info` (2.5 points)

Write a function `provide_info` that takes three parameters: `name`, `year`, and `school` .

Set the default value for `school` to be 'UCSD'.

This function should `return` the string "Hi! I'm `name`. I am a `year` at `school`." (where the variable names are replaced by the values input to the function upon execution).

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
assert provide_info(name = 'Taylor', year = 'junior', school = 'UCLA') == "Hi! I'm Taylor. I am a junior at UCLA." or provide_info(name='Taylor', year='junior', school = 'UCLA') == "Hi. I'm Taylor. I am a junior at UCLA."
### END HIDDEN TESTS
```




{:.input_area}
```python
# hidden tests for function above
### BEGIN HIDDEN TESTS
# assure defaul parameter is correct
assert provide_info(name = 'Taylor', year = 'junior') == "Hi! I'm Taylor. I am a junior at UCSD." or provide_info(name='Taylor', year='junior') == "Hi. I'm Taylor. I am a junior at UCSD."
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===

Rubric used in grading specified here

=== END MARK SCHEME ===

## Part 3: Objects & Classes (5 points)

### Q7 - objects (0.5 points)

The real exam will include an objects question here.

### Q8 - Classes (2.5 points)

Generate a class called `BasketballGame`.

This class should have four instance attributes: `home_team`, `away_team`, `home_points`, and `away_points`

It should also have one method, `play_game()`. 

Within the `play_game` method, add code that would determine who the winner of the game is (determined by the team with the most points), returning Winner: ' and the winning team's name.

For ties, return: 'Winner: tie'



{:.input_area}
```python
### BEGIN SOLUTION
class BasketballGame():
    def __init__(self, home_team, away_team, home_points, away_points):
        self.home_team = home_team
        self.away_team = away_team
        self.home_points = home_points
        self.away_points = away_points
    
    def play_game(self):
        if self.home_points > self.away_points:
            out = 'Winner: ' + self.home_team
        elif self.away_points > self.home_points:
            out = 'Winner: ' + self.away_team
        else:
            out = 'Winner: tie'
        
        return out
        
    
### END SOLUTION
```




{:.input_area}
```python
# use this cell to test/execute/check your class (optional)
```




{:.input_area}
```python
assert callable(BasketballGame)

### BEGIN HIDDEN TESTS
game = BasketballGame(home_team='Warriors', away_team='Sixers', 
                      home_points=100, away_points=105)

# test attributes
assert game.home_team == 'Warriors'
assert game.away_team == 'Sixers'
assert game.home_points == 100
assert game.away_points == 105
### END HIDDEN TESTS
```




{:.input_area}
```python
assert callable(BasketballGame.play_game)

### BEGIN HIDDEN TESTS
# test method
assert game.play_game() == 'Winner: Sixers'
### END HIDDEN TESTS
```


This "blank" cell included intentionally. Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

Rubric used in grading specified here

=== END MARK SCHEME ===

### Q9 - `another_class` (2 points)

The real exam will include another class question here.

### Exam II complete!

Good work - you're done with the second exam!

Check your work, and then when you're ready, **submit on datahub**.

We will not have your exam until you click submit and see this show up under 'submitted assignments'.
