# COGS 18 - Exam 2

This is the second exam for Spring 2021. It covers topics through the Classes Lecture.

This total exam is out of 12.5 points, worth 12.5% of your grade. 

**PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**

**PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE EXAM.** (Note that you can add additional cells, if you want to test things out.

## Instructions

#### Timing
- The exam is designed to take you ~1h.
- There will be a 24 hour window during which you can complete this exam (due Tues 8AM).
- If it takes you longer than 1h, you're free to use that time.

#### The Rules
- You are to complete this exam on your own.
- This is open-notes & open-Google
- You may not talk to any humans about this exam. 
- The following are all *prohibited*:
    - text/phone/online chat communication
    - posting questions to a message board where a human could respond (Campuswire, Discord, Chegg, any similar site)
    - viewing exam questions from a message board (as described above)
    - asking anyone via any form about a question on this test directly
- Clarification questions will ***not*** be allowed and there will be no posting on Campuswire about the exam at all. 
    - Campuswire posts about the exam will not be answered and will be deleted. 
    - Students who post questions about the exam to Campuswire are at risk of losing points on the exam.
    - If you are confused about wording, add a note to your exam explaining your confusion and how you interpreted the question. 
    - Note: This policy is b/c we are incapable of responding for 24h straight. This is the only way to make it fair across the board for students.

 <span style="color: red;">Note: </span> There _is_ a chance for partial credit on some questions, so _some_ code is better than _no_ code. Even if it throws an error, having some code that partially answers the question will benefit you/your grade.

### Q0 - Honor Code (0.1 points)

In the cell below, include a variable `honor_code` that stores the boolean `True` if you agree to the following statement:

>I agree that this exam was completed individually with the knowlege in my brain, information the notes from this course, and/or with searching for help on the Internet *without searching for answers to the text from these questions directly*. I did not ask anyone about specific questions on this exam. I did not post these questions (in part or in whole) on the Internet. I did not copy answers to these questions from anywhere or anyone else. I understand all code I've written on this exam and could explain my answers to someone else if asked.


### BEGIN SOLUTION
honor_code = True
### END SOLUTION

assert honor_code

## Part 1: Methods & Debugging (3.5 points)

### Q1 - Method I (0.75 points)

`isalnum()` is a string method that determines if all the characters in a string are alphanumeric (meaning letters or numbers: A-Z, a-z, 0-9).

Use the `isalnum()` method on two strings (of your choosing) below to create two variables:
- `true_var` | should store the value `True`
- `false_var` | should store the value `False`

### BEGIN SOLUTION
true_var = 'asdf123'.isalnum()
false_var = '!!!!'.isalnum()
### END SOLUTION

assert true_var is not None
### BEGIN HIDDEN TESTS
assert true_var
### END HIDDEN TESTS

assert false_var is not None
### BEGIN HIDDEN TESTS
assert not false_var
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- uses `isalnum()` syntax correctly (**0.35 pts**)

=== END MARK SCHEME ===

### Q2 - Method II (1.25 points)

Here, `site_days` and `days_of_week` have been provided for you. 
- `site_days`: is a (totally made up) list of days on which people received their vaccinations
- `days_of_week`: a tuple containing the days of the week

Note: `count()` is a list method that counts the number of appearances of a specified element in a list.

Using the `count()` method, code constructs discussed in class, and referencing the two variables provided, generate a dictionary:
 - `days_summary`  | whose keys are each of the days of the week in `days_of_week` and whose corresponding values are the number of times each day shows up in `site_days`.

Note: Do not hard-code. You should use code contructs to determine `days_summary`.

site_days = ['M', 'W', 'Th', 'F', 'Tu', 'Sa', 'Su', 'W', 'Su', 'Su',
             'M', 'Th', 'Th', 'Sa', 'M', 'W', 'Sa', 'Tu', 'Sa', 'Su',
             'Su', 'Tu', 'F', 'Sa', 'F', 'W', 'M', 'M', 'Su', 'F',
             'Sa', 'W', 'F', 'W', 'F', 'Sa', 'Tu', 'W', 'Sa', 'Th',
             'W', 'Sa', 'Tu', 'W', 'Tu', 'Sa', 'Th', 'W', 'F', 'W',
             'F', 'Su', 'Th', 'Tu', 'Tu', 'Sa', 'F', 'M', 'Th', 'Tu',
             'M', 'M', 'M', 'Th', 'Sa', 'Sa', 'F', 'Th', 'Tu', 'M',
             'M', 'Tu', 'W', 'Tu', 'Su', 'Sa', 'Su', 'F', 'F', 'Su',
             'Sa', 'Th', 'F', 'W', 'W', 'Sa', 'Su', 'W', 'Sa', 'Su',            
            ]
days_of_week = ('M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su')

# hidden test being used in grading
### BEGIN HIDDEN TESTS
site_days = ['M', 'M', 'M', 'M']
days_of_week = ('M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su')
### END HIDDEN TESTS

### BEGIN SOLUTION
days_summary = {}

for day in days_of_week:
    days_summary[day] = site_days.count(day)
### END SOLUTION

assert days_summary is not None
### BEGIN HIDDEN TESTS
assert list(days_summary.keys()) == ['M', 'Tu', 'W', 'Th',
                                     'F', 'Sa', 'Su']
### END HIDDEN TESTS

# hidden tests for task above
### BEGIN HIDDEN TESTS
assert list(days_summary.values()) == [4, 0, 0, 0, 0, 0, 0]
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

Check if points lost on autograder above: 
- initialized or created `days_summary` as a dictionary (**0.25 pts**)
- Used count() method correctly (**0.25 pts**)
- updated `days_summary` dictionary correctly (**0.25 pts**)

=== END MARK SCHEME ===

### Q3 - Debugging (1.5 points)

The following not-totally-functioning `growth_rate()` function has been provided for you. The *goal* of this function, is given two population inputs: `last_year`, `this_year`, the function should return the population growth rate for that country.

For example, in 2020, China's population was `1439323776`. This year, its population is `1444216107`.

Population growth rate is calculated by taking the difference between this year's population minus last year's population, dividng that difference by last year's population, and multiplying the entire quantity by 100.

Given China's numbers above and this calculation, we know that this function should return `0.34`...but it's not at this point.

Consider the function currently and then debug (you can edit the code provided directly or copy and paste below so you still have the original if needed) to accomplish the task specified above. 

Note: Do not change the name of the function (`growth_rate`), and the parameter names provided in the instructions (`last_year`, `this_year`) must be used.

def growth_rate(self, this_year, last_year):
    self.this_year - self.last_year/self.last_year * 100

### BEGIN SOLUTION
def growth_rate(this_year, last_year):
    return ((this_year - last_year)/last_year) * 100
### END SOLUTION

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)

assert growth_rate
### BEGIN HIDDEN TESTS
from numpy import isclose
assert isclose(growth_rate(last_year=331002651, 
                           this_year=332915073), 0.58, 0.01)
### END HIDDEN TESTS


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

Check if points lost on autograder above: 
- `self` removed as a parameter (**0.25 pts**)
- `self` removed from within function (**0.25 pts**)
- parentheses added/Order of operations accounted for (**0.25 pts**)
- `reuturn` statement added (**0.25 pts**)
                                                              
=== END MARK SCHEME ===

## Part 2: Functions (4.4 points)

### Q4 - Function Execution (1 point)

The function `count_sentences()` has been provided for you below. Note that `split()` is a string method that splits a string at the character specified within the parentheses of the method call.

**Part 1** (0.75 points)

First, in the cell provided below containing `YOUR ANSWER HERE`, describe what the `count_sentences()` function accomplishes. This should include both 1) the overall task accomplished and 2) how the specific code used accomplishes this task.

def count_sentences(text):
    sentences = text.split('.')
    
    if sentences[-1]=='':
        num_sentences = len(sentences) - 1
    else:
        num_sentences = len(sentences)
        
    return num_sentences

# BE SURE YOUR ANSWER IS IN THE CELL BELOW
# but you can use this cell to test/execute/check your thinking (optional)

Describe the `count_sentences()` function here.


=== BEGIN MARK SCHEME ===

- explains task generally accurately (**0.25 pts**)
- explains what `.split()` does in context accurately (**0.25 pts**)
- explains what conditional does/why it's needed (**0.25 pts**)

=== END MARK SCHEME ===

**Part 2** (0.25 points)

Execute the `count_sentences()` function such that it:
- returns `2`; assign this output to the variable `out_2`.

### BEGIN SOLUTION
out_2 = count_sentences('A sentence with words. A second sentence with words.')
### END SOLUTION

assert out_2
### BEGIN HIDDEN TESTS
assert out_2 == 2
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- remove autograder credit above if function not executed

=== END MARK SCHEME ===

### Q5 - Function I: Username check (1.65 points)

Recently the company you work at ('cogs co.') realized that too many employees have problematic usernames. You're going to write a function (`change_username()`) that takes a single parameter `username` as input. 

This function will check if the `username` meets the following specifications:
- contains more than four characters
- includes only letters (A-Z; a-z) and/or numbers (0-9); in other words: is alphanumeric
- does NOT include the string 'cogs'

If the `username` meets the above specifications, the function will `return` `False` (indicating the username does *not* have to be changed. If any one of the above specifications is not met, the function will `return` `True` (indicating that the `username` does *not* meet at least one of the above specifications).

For example, `change_username(username='cogs')` would `return` `True` because it does not contain more than four letters *and* because it includes the string `'cogs'` in its name, while `change_username(username='Shannon')` would return `False`, as this meets all three specifications above. 

### BEGIN SOLUTION
def change_username(username):
    
    if not username.isalnum(): # determine if any letters are not in letters_numbers
        output = True
    elif len(username) <= 4:  # check length
        output = True
    elif 'cogs' in username:   #s check for string
        output = True
    else:
        output = False
    
    return output

# OR

def change_username(username):
    if len(username) > 4 and username.isalnum() and 'cogs' not in username:
        return False
    else:
        return True
### END SOLUTION

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)

assert change_username
### BEGIN HIDDEN TESTS
assert callable(change_username)
assert change_username('aaaaa') == False
### END HIDDEN TESTS

# hidden test to check functionality
### BEGIN HIDDEN TESTS
# check four letters
assert change_username('aaaa') == True
### END HIDDEN TESTS

# hidden test to check functionality
### BEGIN HIDDEN TESTS
# check capitalization
assert change_username('AAAAA') == False
### END HIDDEN TESTS

# hidden test to check functionality
### BEGIN HIDDEN TESTS
# check numbers
assert change_username('12345') == False
### END HIDDEN TESTS

# hidden test to check functionality
### BEGIN HIDDEN TESTS
# check cogs string
assert change_username('cogs123') == True
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

Check if points lost on autograder above: 
- `def` corect with `username` password (**0.2 pts**)
- condition for length correct (**0.2 pts**)
- condition for 'cogs' string correct (**0.2 pts**)
- condition for letters and numbers correct (**0.2 pts**)
- includes `return` statement (**0.1 pts**)

Note: if only issue is `return` statement is missing, return autograder credit lost and only deduct for `return` statement missing
=== END MARK SCHEME ===

### Q6 - Function II: Tax Rate (1.75 points)

Here you will write a function that, given a salary as input, will `return` how much of that person's salary is going toward taxes.

To accomplish this, write a function `to_taxes()` that takes two parameters as input: `salary` and `tax_brackets`. The default value for the `tax_brackets` parameter should be the `default_brackets` dictionary provided below. Then, use code constructs discussed in class to accomplish the above goal.

Note that the dictionary `default_brackets` provided will have to be used to accomplish this goal. The keys in `default_brackets` are the proportion of an individual's salary that will go toward taxes if their salary is within the range in a given key's value (tuple). For example, an individual who makes \$10,000 would contribute 12\% of their salary in taxes, given the information in `tax_brackets` (specifically becasue 10000 falls between 9876 and 40125).

Accordingly, `to_taxes(salary=10000)` should `return` 1200.0 (which corresponds to 12\% of the input $10,000 salary).

default_brackets = {0.10 : (0, 9875),
                    0.12 : (9876, 40125),
                    0.22 : (40126, 85525),
                    0.24 : (85526, 163300),
                    0.32 : (163301, 207350),
                    0.35 : (207351, 518400)
                   }

### BEGIN SOLUTION
def to_taxes(salary, tax_brackets=default_brackets):
    for key in tax_brackets:
        if tax_brackets[key][0] <= salary <= tax_brackets[key][1]:
            output = key * salary
    
    return output
### END SOLUTION

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)

assert to_taxes
### BEGIN HIDDEN TESTS
assert callable(to_taxes)
assert to_taxes(10000) == 1200.0
assert to_taxes(207355) == 72574.25
### END HIDDEN TESTS

# hidden test to check function accomplishes task
### BEGIN HIDDEN TESTS
# check for 22% bracket
# check that values on edges included
assert to_taxes(40126) == 8827.72
assert to_taxes(85525) == 18815.5
### END HIDDEN TESTS

# hidden test to check default parameter correct
### BEGIN HIDDEN TESTS
# check for a different tax_brackets
assert to_taxes(100, tax_brackets={0.5: (0,1000)}) == 50.0
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

Check if points lost on autograder above: 
- function defined correctly with `salary` parameter and default value for `tax_brackets` parameter (**0.25 pts**)
- loops through dictionary (or equivalent) correctly (**0.2 pts**)
- conditional accesses values in tuple correctly (**0.2 pts**)
- conditional checks lower and upper bound of range (**0.2 pts**)
- calculation correct (i.e. key * salary) (**0.2 pts**)
- includes `return` statement (**0.2 pts**) 

=== END MARK SCHEME ===

## Part 3: Classes (4.5 points)

### Q7 - Classes I (2.25 points)

Define a class `ClassRoster()` that meets the following specifications:

- has two instance attributes:
    - `students`; initialized as an empty list
    - `course`; which the user specifies when creating a `ClassRoster()` object
- a single method `add_student()`, which will have `pid` and `name` as arguments, and will add these two inputs as a dictionary with `pid` as the key and the student's `name` as the value to the `students` list each time the method is called

### BEGIN SOLUTION
class ClassRoster():
        
    def __init__(self, course):
        self.students = []
        self.course = course
        
    def add_student(self, pid, name):
        self.students.append({pid: name})
### END SOLUTION

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)

assert callable(ClassRoster)
my_course = ClassRoster('COGS 18')
### BEGIN HIDDEN TESTS
assert my_course.course == 'COGS 18'
### END HIDDEN TESTS

# tests for instance attribute
assert my_course.students is not None
### BEGIN HIDDEN TESTS
assert my_course.students == []
### END HIDDEN TESTS

# tests for method
assert callable(my_course.add_student)
### BEGIN HIDDEN TESTS
my_course.add_student(pid='A12345', name='Shannon')
my_course.add_student(pid='A56789', name='Josh')

assert my_course.students == [{'A12345':'Shannon'}, {'A56789': 'Josh'}]
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

Check if points lost on autograder above: 
- `class` defined correctly (**0.1 pts**)
- instance attributes
    - `def __init__(self)` correct (**0.2 pts**)
    - `self` used within definition (**0.2 pts**)
    - `students` attribute initialized correctly (empty list) (**0.2 pts**)
    - `course` intialized correctly  (**0.2 pts**)
- `add_student` method:
    - method definition correct with `self`, `pid`, and `name` (**0.2 pts**)
    - dictionary syntax correct  (**0.2 pts**)
    - added to list correct (`append`) (**0.2 pts**)

Note: autograder credit can be returned for portions above if particular aspect (class attribute, instance attribute, or method) were correct, but test failed because overall `class` was defined incorrectly

=== END MARK SCHEME ===

### Q8 - Classes II (2.25 points)

Define a class `ToDo()` to keep track of your to do list.

This should have a single instance attribute: `to_do`, which is initialized as an empty list.

It will then have two methods: `add_item` and `remove_item`.

`add_item()`:
- will have two parameters `item`, and `top` (`top` takes the default value `True`)
- if `top` is `True`:
    the string in `item` will be added to the top of `to_do`:
- if `top` is not true:
    the string it `item` will be added to the end of `to_do`

`remove_item()`:
- will have a single parameter `item`
- will remove the item specified from `to_do`

Note: there is a list method `insert()`, which operates in place to add a value to a list at the index specified with the general syntax `my_list.insert(index, item_to_add)`.

### BEGIN SOLUTION
class ToDo():
    
    def __init__(self):
        self.to_do = []
        
    def add_item(self, item, top=True):
        if top:
            self.to_do.insert(0, item)
        else: 
            self.to_do.append(item)
        
    def remove_item(self, item):
        self.to_do.remove(item)

### END SOLUTION

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)

assert callable(ToDo)
my_todo_list = ToDo()
### BEGIN HIDDEN TESTS
assert my_todo_list.to_do == []
### END HIDDEN TESTS

# check add_item method
### BEGIN HIDDEN TESTS
my_todo_list.add_item('A')
my_todo_list.add_item('B')
assert my_todo_list.to_do == ['B','A']
### END HIDDEN TESTS

# check add_item with non-default value
### BEGIN HIDDEN TESTS
my_todo_list.add_item('C', top=False)
assert my_todo_list.to_do == ['B','A', 'C']
### END HIDDEN TESTS

# check remove_item
### BEGIN HIDDEN TESTS
my_todo_list.remove_item('A')
assert my_todo_list.to_do == ['B', 'C']
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

Check if points lost on autograder above: 
- `class` defined correctly (**0.1 pts**)
- instance attribute
    - `def __init__(self)` correct (**0.2 pts**)
    - `to_do` attribute initialized correctly (empty list) (**0.2 pts**)

- `add_item` method:
    - method definition correct with `self`, `item`, and `top` (**0.15 pts**)
    - `top` default value set to `True`
    - conditional correct  (**0.15 pts**)
    - extends list correctly (**0.15 pts**)

- `remove_item` method:
    - method definition correct with `self` and `item` (**0.15 pts**)
    - item removed correctly  (**0.15 pts**)

Note: autograder credit can be returned for portions above if particular aspect (class attribute, instance attribute, or method) were correct, but test failed because overall `class` was defined incorrectly

=== END MARK SCHEME ===

### Exam II complete!

Good work - you're done with the second exam!

Check your work, and then when you're ready, **submit on datahub**.

We will not have your exam until you click submit and see this show up under 'submitted assignments'.