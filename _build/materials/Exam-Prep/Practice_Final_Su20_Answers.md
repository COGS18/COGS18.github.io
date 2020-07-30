---
interact_link: content/materials/Exam-Prep/Practice_Final_Su20_Answers.ipynb
download_link: assets/downloads/Practice_Final_Su20_Answers.ipynb.zip
title: 'Final_Practice_Su20_Answers'
prev_page:
  url: /materials/Exam-Prep/Final-Review
  title: 'Final-Review'
next_page:
  url: /labs/source_Su20/CL1-Tooling
  title: 'Coding Labs'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# COGS 18 - Practice Final Exam

This is the practice final exam for Summer 2020. It covers topics through the Open-Source/API Lecture.

This exam is out of 0 points, worth 0% of your grade. 

**PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**

**PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE EXAM.** (Note that you can add additional cells, if you want to test things out.

## Instructions

#### Timing
- The exam is designed to take you ~2 hours.
- There will be a 24 hour window during which you can complete this exam.
- If it takes you longer than 2 hours, you're free to use that time.

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

## Part 1: Variables, Conditionals, & Loops (2.5 points)

Review E1 for material in this section

### Q1 - Conditionals (1.5 points)

### Q2 - Loops (1 point)

## Part 2: Functions & Testing (3 points)

### Q3 - `years_to_days` (1.5 points)

Write a function `years_to_days()` that takes the number of years as its input and then convers that to days (You should assume there are 365 days in a year for this question.) Return the number of days from the function as an integer.

Note:
- You can assume the input val is numeric
- This function is admittedly _less_ involved than the function on your exam, so that we can focus on the new material



{:.input_area}
```python
### BEGIN SOLUTION
def years_to_days(val):
    
    return int(val*365)
### END SOLUTION
```




{:.input_area}
```python
assert years_to_days is not None

### BEGIN HIDDEN TESTS
assert years_to_days(1) == 365
assert years_to_days(1.5) == 547
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

RUBRIC USED IN GRADING
                                                                        
=== END MARK SCHEME ===

### Q4 - Test Function: `test_years_to_days` (1.5 points)

Write a test function `test_years_to_days()` that:

1. contains at least three asserts that test the functionality of `years_to_days()`
2. passes silently when executed



{:.input_area}
```python
### BEGIN SOLUTION
# specific tests will differ
def test_years_to_days():
    assert callable(years_to_days)
    assert isinstance(years_to_days(1), int)
    assert years_to_days(1) == 365
    assert years_to_days(1.5) == 547
### END SOLUTION
```




{:.input_area}
```python
assert callable(test_years_to_days)

### BEGIN HIDDEN TESTS
try:
    test_years_to_days()
    out = 'good'
except:
    out = 'bad'
    
assert out == 'good'
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

RUBRIC USED IN GRADING

=== END MARK SCHEME ===

## Part 3: Style & Documentation (8.25 points)

### Q5 - Code Style (2 points)

In the file `years.py`, there is a function `days_to_years()`. The code is functional; however, the API/naming and code style need improvement. And, documentation and code comments are completely missing.

Edit the function in `years.py` to:
1. Improve the function's API/naming (but: do *not* change the function's name)
2. Improve the overall code style (using what we discussed in class about PEP8)
3. Add a `numpy` style docstring (at the level discussed in class)
4. Add code comments where needed

Be sure to save changes in `years.py` when completed. 

Note: You do not have to actually add any code to this notebook for this question.

see function below for "improved" API/documentation

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

RUBRIC USED IN GRADING

=== END MARK SCHEME ===

### Q6 - `years.py` (2 points)

You now have two functions and two test functions, but they're not all yet organized! Let's do that now...

**`years.py`**
1. Add `years_to_days()` (from Q3) to `years.py`
2. Add a `numpy`-style docstring & appropriate code comments to `years_to_days()` (if you haven't already).
3. Double check the naming/code style used in `days_to_years()` - improve if needed

**`test_years.py`**
1. Add `test_years_to_days` (from Q4) to `test_years.py`
2. Update `import` statement at top (if needed)

Once completed, `import` both of the functions from `years.py` below, such that the code `yr.years_to_days(1)` and `yr.days_to_years(365)` both execute without issue.

Note: You may have to restart your kernel for the `import` to work without issue.

What should be in `years.py`:



{:.input_area}
```python
def days_to_years(input_days):
    """convert input value into years
    
    Parameters
    ----------
    input_days: int or float
        input number of days to be converted
    
    Returns
    -------
    output_years: float
        converted value in years
    
    """
    
    # convert to years, round to two decimal place
    output_years = input_days/365
    output_years = round(output_years, 2)
   
    return output_years

def years_to_days(input_years):
    """convert input value into days
    
    Parameters
    ----------
    input_years: int or float
        input number of years to be converted
    
    Returns
    -------
    output_days: float
        converted value in years
    
    """
    
    output_days = int(input_years * 365)
    
    return output_days

```


What should be in `test_years.py`:



{:.input_area}
```python
from years import days_to_years, years_to_days

def test_days_to_years():
    assert callable(days_to_years)
    assert isinstance(days_to_years(365), float)
    assert days_to_years(365) == 1
    assert days_to_years(547) == 1.5


def test_years_to_days():
    assert callable(years_to_days)
    assert isinstance(years_to_days(1), int)
    assert years_to_days(1) == 365
    assert years_to_days(1.5) == 547
```




{:.input_area}
```python
### BEGIN SOLUTION
import years as yr
### END SOLUTION
```




{:.input_area}
```python
# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to check your work (optional)
```


Note: I updated these asserts to not have a typo:



{:.input_area}
```python
assert callable(yr.years_to_days)

### BEGIN HIDDEN TESTS
assert yr.years_to_days(1) == 365
### END HIDDEN TESTS
```




{:.input_area}
```python
assert callable(yr.days_to_years)

### BEGIN HIDDEN TESTS
# use default parameter
assert yr.days_to_years(365) == 1
### END HIDDEN TESTS
```




{:.input_area}
```python
# to run pytest
!pytest test_years.py
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===

RUBRIC USED FOR GRADING

=== END MARK SCHEME ===

### Q7 -  (4.25 points)

Another function + code style + documentation + import question will be included here

## Part 4: True/False (1.25 points)

### Q8 - True/False (1.25 points)

Following the instructions & example above, store the appropriate boolean in the variable provided for each of the following statements:

- `objects` | In Python, everything is an object



{:.input_area}
```python
### BEGIN SOLUTION
objects = True
### END SOLUTION
```




{:.input_area}
```python
assert objects is not None

### BEGIN HIDDEN TESTS
assert objects
### END HIDDEN TESTS
```


### Final Exam complete!

Good work - you're done with the final exam!

Check your work, and then when you're ready, **submit on datahub**.

We will not have your exam until you click submit and see this show up under 'submitted assignments'.
