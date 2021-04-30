# COGS 18 - Exam 1

This is the first exam for Spring 2021. It covers topics through the Dictionaries Lecture.

This exam is out of 12.5 points, worth 12.5% of your grade.

**PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**

**PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE ASSIGNMENT.** (Note that you can add additional cells, if you want to test things out.

## Instructions

#### Timing
- The exam is designed to take you ~1h.
- There will be a 24 hour window during which you can complete this exam (due Sat 8AM).
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

## Part 1: Variables & Operators (3.75 points)

### Q1 - Variables (0.75 points)

In the cell below, create three variables: `var_a`, `var_b`, and `var_c`. 

- `var_a` should store four characters in an immutable variable type that is only able to store one piece of information
- `var_b` should be a single value that, when added to itself returns a whole number
- `var_c` should be an immutable variable storing three different values

The specific values you use to generate the variables are up to you, as long as they fulfull the criteria specified.

### BEGIN SOLUTION
# actual values stored will differ
var_a = 'abcd'
var_b = 6.0
var_c = (1,2,3)
### END SOLUTION

# check variable exists
assert var_a is not None
### BEGIN HIDDEN TESTS
assert isinstance(var_a, str)
assert len(var_a) == 4
### END HIDDEN TESTS

assert var_b is not None
### BEGIN HIDDEN TESTS
assert var_b % 1 == 0 
### END HIDDEN TESTS

assert var_c is not None
### BEGIN HIDDEN TESTS
assert isinstance(var_c, tuple)
assert len(var_c) == 3
### END HIDDEN TESTS

### Q2 - Math Operators (1 point)

Use the variables provided in the cell below (`var_low`, `var_mid` and `var_high`) to generate the variables: `var_even` and `var_odd` according to the following specifications:

- `var_even` | use the 3 variables provided once each and *at least two* of the math operators (`+`, `-`, `*`, `/`, `**`, `//`, `%`) to store the value 12 
- `var_odd` | use the 3 variables provided once each and *at least two* of the math operators (`+`, `-`, `*`, `/`, `**`, `//`, `%`) to store the value 13

# these variables provided for you
# this cell is read-only (cannot be changed)
var_low = 2
var_mid = 20
var_high = 30

### BEGIN SOLUTION
# actual operations will differ
var_even = (var_high + var_low) % var_mid
var_odd = (var_mid ** var_low) // var_high
### END SOLUTION

assert var_even is not None
### BEGIN HIDDEN TESTS
assert int(var_even % 2) == 0
assert var_even == 12
### END HIDDEN TESTS

assert var_odd is not None
### BEGIN HIDDEN TESTS
assert var_odd % 2 != 0
assert var_odd == 13
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- correct operators used (0.15)
- variables referenced; did not hard-code numbers (0.15)  

=== END MARK SCHEME ===


### Q3 - Comparison Operators (1 point)

First, define two variables below: `my_age` and `pres_age`. Store your age (as an integer) in `my_age` and store the current US President's age (as an integer) in `pres_age`. (Note: President Biden is 78 years old.)

Then, use (refer to) `my_age` and `pres_age` to define define two variables: `true_compar` and `false_compar`.

These variables must satisfy the following requirements:

1. Each variable must be defined using one comparison operator (`<`,`>`,`<=`,`>=`,`!=`,`==`).
2. Each variable must use and refer to `my_age` and `pres_age` (and no other values or variables)
4. `true_compar` should evaluate as the boolean `True`; `false_compar` should evaluate as the boolean `False`

### BEGIN SOLUTION
my_age = 31 # specific values will differ
pres_age = 78

true_compar = my_age < pres_age
false_compar = pres_age == my_age
### END SOLUTION

assert true_compar is not None
### BEGIN HIDDEN TESTS
assert true_compar
### END HIDDEN TESTS

assert false_compar is not None
### BEGIN HIDDEN TESTS
assert not false_compar
### END HIDDEN TESTS

assert my_age is not None
### BEGIN HIDDEN TESTS
assert isinstance(my_age, int)
assert my_age < 118
### END HIDDEN TESTS

assert pres_age is not None
### BEGIN HIDDEN TESTS
assert pres_age == 78
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- both variables reference `my_age` and `pres_age` (0.15)
- both variables reference use at least one comparison operator (0.15)

=== END MARK SCHEME ===

### Q4 - Membership Operators (0.5 points)

Two variables (`spring_holidays` and `current_holidays`) have been created for you below. Using **only these two variables and membership operators**, define the following two variables below (`yes_member` and `no_member`), such that they meet the following specifications:

- `yes_member` | stores the boolean `True`
- `no_member` | stores the boolean `False`

# these variables provided for you
# this cell is read-only (cannot be changed)
spring_holidays = ['César Chávez', 'Passover', 'Easter', 
                   'Ramadan', 'Shavout', 'Memorial Day']
current_holiday = 'Ramadan'

### BEGIN SOLUTION
yes_member = current_holiday in spring_holidays
no_member = current_holiday not in spring_holidays
### END SOLUTION

assert yes_member is not None
### BEGIN HIDDEN TESTS
assert yes_member
### END HIDDEN TESTS

assert no_member is not None
### BEGIN HIDDEN TESTS
assert not no_member
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- only references variables provided (+0.1)
- remove autograder credit of hard-coded (does not use membership operator)

=== END MARK SCHEME ===

### Q5 - String Concatenation (0.5 points)

Two strings (`feeling` and `vaccine`) below have been provided for you. *Referencing these variables and including additional strings as needed*, create (define) the variable `vaccination` such that it stores the string `"I'm so excited that students are now eligible for the vaccine!"`.

Notes: 
- Punctuation, captialization and spacing all matter here. Be sure your resulting string is equivalent to the string above. 
- Your answer should reference (meaning: use) the variables `feeling` and `vaccine`

# these variables provided for you
# this cell is read-only (cannot be changed)
feeling = 'excited'
vaccine = 'vaccine'

### BEGIN SOLUTION
vaccination = "I'm so " + feeling + " that students are now eligible for the " + vaccine + "!"
### END SOLUTION

assert vaccination is not None
### BEGIN HIDDEN TESTS
assert isinstance(vaccination, str)
### END HIDDEN TESTS

# hidden test checking for correct string
### BEGIN HIDDEN TESTS
assert vaccination == "I'm so excited that students are now eligible for the vaccine!"
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- if hard-coded (doesn't reference variables and use `+` operator/format string programmatically), remove autograder credit from cell above (-0.4)

=== END MARK SCHEME ===

## Part 2: Collections & Indexing  (3 points)

### Q6 - Lists & Indexing (1 point)

The list `trees` has been provided in the cell below for you.

***Use the `trees` variable and indexing*** to generate each of the four variables at left below, so that each stores the output at right below. For example, `trees_a` should refer to `trees` in its answer and use indexing to store the string 'Pine'.

- `trees_a` | `'Pine'`
- `trees_b` | `['Liquid Amber', 'Pepper', 'Podocarpus']`
- `trees_c` | `['Eucalyptus', 'Ficus', 'Tipuana', 'Pepper']`
- `trees_d` | `['Palms', 'Carrotwood', 'Tipuana', 'Podocarpus']`

# this variables provided for you
# this cell is read-only (cannot be changed)
trees = ['Palms', 'Jacaranda', 'Eucalyptus', 'Carrotwood', 
         'Ficus', 'Pine', 'Tipuana', 'Liquid Amber', 
         'Pepper', 'Podocarpus']

### BEGIN SOLUTION
# actual values will differ
trees_a = trees[5]
trees_b = trees[-3:]
trees_c = trees[2:9:2]
trees_d = trees[::3]
### END SOLUTION

assert trees_a
### BEGIN HIDDEN TESTS
assert trees_a == 'Pine'
### END HIDDEN TESTS

assert trees_b
### BEGIN HIDDEN TESTS
assert trees_b == ['Liquid Amber', 'Pepper', 'Podocarpus']
### END HIDDEN TESTS

assert trees_c
### BEGIN HIDDEN TESTS
assert trees_c == ['Eucalyptus', 'Ficus', 'Tipuana', 'Pepper']
### END HIDDEN TESTS

assert trees_d
### BEGIN HIDDEN TESTS
assert trees_d == ['Palms', 'Carrotwood', 'Tipuana', 'Podocarpus']
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- if hard-coded (doesn't use indexing & reference `trees`), remove autograder credit

=== END MARK SCHEME ===


### Q7 - Dictionaries & Tuples (2 points)

**Part 1** (1.5 points)

Generate a dictionary called `grading` that meets the following criteria:

- has 5 keys: 'A', 'B', 'C', 'D', 'F'
- stores a tuple containg the lower and upper bound for each letter grade for each key's value.

Use the following ranges for reference:

- A: 90-100
- B: 80-90
- C: 70-80
- D: 60-70
- F: 0-60

Note that the upper bound for one letter will be the same value as the lower bound for the higher grade. This is expected behavior.

### BEGIN SOLUTION
grading = {'A': (90, 100),
           'B': (80, 90),
           'C': (70, 80),
           'D': (60, 70),
           'F': (0, 60)}
### END SOLUTION

assert grading
### BEGIN HIDDEN TESTS
assert isinstance(grading, dict)
assert len(grading) == 5
### END HIDDEN TESTS

# hidden test to check types
### BEGIN HIDDEN TESTS
assert isinstance(list(grading.keys())[0], str)
assert isinstance(list(grading.values())[0], tuple)
### END HIDDEN TESTS

# hidden test to check the keys
### BEGIN HIDDEN TESTS
assert list(grading.keys()) == ['A', 'B', 'C', 'D', 'F']
### END HIDDEN TESTS

# hidden test to check the values
### BEGIN HIDDEN TESTS
assert list(grading.values()) == [(90, 100), (80, 90), (70, 80), 
                                  (60, 70), (0, 60)]
### END HIDDEN TESTS

**Part 2** (0.5 points)

Use the `grading` dictionary you just generated **and indexing** to generate two variables: `A_lower` and `A_upper`.

- `A_lower` will store the first (smaller) value in the tuple corresponding to the `'A'` key in `grading`.
- `A_upper` will store the second (larger) value in the tuple corresponding to the `'A'` key in `grading`

Note: Do not hard-code. For example, `A_lower = 90` is *not* the correct answer. Your code should reference `grading` and use indexing to store the value 90 in `A_lower`

### BEGIN SOLUTION
A_lower = grading['A'][0]
A_upper = grading['A'][1]
### END SOLUTION

assert A_lower
### BEGIN HIDDEN TESTS
assert A_lower == 90
### END HIDDEN TESTS

assert A_upper
### BEGIN HIDDEN TESTS
assert A_upper == 100
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- if hard-coded (doesn't use indexing & reference `grading`), remove autograder credit

=== END MARK SCHEME ===


## Part 3: Control Flow - Conditionals & Loops  (5.65 points)

### Q8 - Conditionals (2 points)

Store your desired score on this exam (out of 100 points) in the variable `desired_score`.

Then, write a conditional that will compare your `desired_score` to your values (from Q7) in `A_lower` and `A_upper`. 

If your desired_score is greater than or equal to `A_lower` and less than or equal to A_upper, store the string `'A desired'` in the variable `output`. Otherwise, store the string `'A not desired'` in the variable `output`.

Notes: 
1. Spelling/capitalization of the string stored in `output` matter. Be sure it matches the string specified in the instructions above.
2. (Ignore this if you completed Q7.) If you could not figure out Q7, define two variables here `A_lower` and `A_upper`, so that they store 90 and 100, respectively. This will allow you to complete this question. 

### BEGIN SOLUTION
desired_score = 100

# code will differ based on who is taking the exam
if desired_score >= A_lower and desired_score <= A_upper:
    output = 'A desired'
else:
    output = 'A not desired'
### END SOLUTION

assert output
# test to ensure no typos in string
assert output in ['A desired', 'A not desired']
### BEGIN HIDDEN TESTS
if desired_score >= A_lower and desired_score <= A_upper:
    test = 'A desired'
else:
    test = 'A not desired'

assert test == output
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===

- uses `if`/`else` OR `if`/`elif` syntax correctly (**0.5 points**)
- conditional correct 
    - references variables (`desired_score`, `A_lower`, `A_upper`) (**0.3 points**)
    - uses `>=` `and`/`&`, and `<=` (**0.3 points**)
- `output` assigned a string value (even if there are typos in string) (**0.15 points**)

=== END MARK SCHEME ===

### Q9 - `for` loop (2.5 points)

Background: While Professor Ellis cares most that students learn the material in COGS 18, students are often (understandably) curious about their final letter grade in her classes. Here, you're going to help students figure out their letter grade programmatically!

Define a grade between 0 and 100 in the variable `student_grade`.

Then, write code that uses the dictionary `grading` you created in Q7 to determine the student's `letter_grade` using the following logic:

For each key in `grading`, if the `student_grade` is 100, `letter_grade` will store the string 'A'. Otherwise, if the `student_grade` is *greater than or equal* to the lower value in the key's tuple value and *less than* the upper value in the key's tuple, the key will be stored in `letter_grade`.


Note: This should not be hard-coded. Your answer should use code constructs discussed in class. In other words, your code should produce the correct `letter_grade`, regardless of the specific value you choose for `student_grade`. In fact, a great way to test your code is to check to ensure it gives you the correct `letter_grade`, regardless of the value you input for `student_grade`. Specifically, it may be best to test that a `student_grade` of 89 should return `'B'` for `letter_grade`, while a `student_grade` of 90 would store `'A'` for `letter_grade`

### BEGIN SOLUTION
student_grade = 89

for grade in grading:
    if student_grade == 100:
        letter_grade = 'A'
    elif student_grade >= grading[grade][0] and student_grade < grading[grade][1]:
        letter_grade = grade
        
### END SOLUTION

assert letter_grade
### BEGIN HIDDEN TESTS
grading = {'A' : (90, 100), 
           'B' : (80, 90), 
           'C' : (70, 80), 
           'D' : (60, 70), 
           'F' : (0, 60)
          }


for grade in grading:
    if student_grade == 100:
        test = 'A'
    elif student_grade >= grading[grade][0] and student_grade < grading[grade][1]:
        test = grade
        
assert test == letter_grade
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===
- `student_grade` initialized with a value [0,100] (**0.25 points**)
- `for` loop thorugh `grading` (**0.25 points**)
- conditional for 100 correct (**0.25 points**)
- `elif` conditional correct: 
    - uses `>=`, `and`/`&`, `<`  (**0.25 points**)
    - indexes into `grading` correctly (**0.25 points**)
    - `letter_grade` stores key from `grade` (**0.25 points**)
    
=== END MARK SCHEME ===

### Q10 - Accomplishing a task (1.15 points)

Earlier (in Q5), you used string concatenation to store the string `"I'm so excited that students are now eligible for the vaccine!"`. Here we're going to accomplish the same task, but starting with the list below.

Using the list below and code constructs we discussed in class, convert the list provided (`vaccination_list`) into a single sentence: `"I'm so excited that students are now eligible for the vaccine!"`. Store this in the variable `sentence`.

vaccination_list = ["I'm ", "so ", "excited ", "that ", "students ", "are ", 
                    "now ", "eligible ", "for ", "the ", "vaccine!"]

### BEGIN SOLUTION
sentence = ''

for word in vaccination_list:
    sentence += word
### END SOLUTION

assert sentence is not None
### BEGIN HIDDEN TESTS
assert sentence == "I'm so excited that students are now eligible for the vaccine!"
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===
- `sentence` initialized as empty string (**0.25 points**)
- `for` loop set up correctly (**0.25 points**)
- string extended/concatenated correctly (**0.5 points**)  

=== END MARK SCHEME ===

### Submit on Datahub

Good work - you're done!

Check your work, and then when you're ready, **submit on datahub**.

We will not have your exam until you click submit and see this show up under 'submitted assignments'.