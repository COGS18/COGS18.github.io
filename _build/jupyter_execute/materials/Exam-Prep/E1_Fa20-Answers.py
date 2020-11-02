# COGS 18 - Exam 1

This is the first exam for Fall 2020. It covers topics through the Dictionaries Lecture.

This exam is out of 12.5 points, worth 12.5% of your grade.

**PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**

**PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE ASSIGNMENT.** (Note that you can add additional cells, if you want to test things out.

## Instructions

#### Timing
- The exam is designed to take you ~1h.
- There will be a 24 hour window during which you can complete this exam.
- If it takes you longer than 1h, you're free to use that time.

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

### Q1 - Variables (1 point)

In the cell below, create two variables: `var_cat` and `var_sum`. 

- `var_cat` should store a string created (assigned) by concatenating two strings together 
- `var_sum` should store a numeric variable (float or int) created (assigned) by adding two numeric values together

The specific values you use to generate `var_cat` and `var_sum` are up to you, as long as they fulfull the criteria specified.

# actual values stored will differ
var_cat = 'cogs' + '18'
var_sum = 9 + 29

# check variable exists
assert var_cat is not None
assert isinstance(var_cat, str)

# check variable exists
assert var_sum is not None
assert isinstance(var_sum, float) or isinstance(var_sum, int)

### Q2 - Math Operators (1 point)

In the cell below, create three variables: `var_low`, `var_mid`, and `var_high`.

Across these three variables:
- all seven math operators (`+`, `-`, `/`, `*`, `**`, `%`, `//`) must be used _at least once_ 
- each variable must store a number (float or int)
- the values stored in each variable must satisfy the condition that `var_low` stores the smallest number and `var_high` the highest

# actual operations will differ
var_low = (9 + 2 - 1) % 3
var_mid = 25 / 5 * 2 // 1
var_high = 13 ** 2  

assert var_low is not None
assert isinstance(var_low, float) or isinstance(var_low, int)

assert var_mid is not None
assert isinstance(var_mid, float) or isinstance(var_mid, int)

assert var_high is not None
assert isinstance(var_high, float) or isinstance(var_high, int)

#hidden test to ensure conditions specified in instructions were followed
assert var_low < var_mid < var_high

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- all seven operators are used (0.2)

=== END MARK SCHEME ===

### Q3 - Comparison Operators (1 point)

In the cell below, create two variables: `true_var` and `false_var`.

These variables must satisfy the following requirements:

1. Each variable must be defined using *at least one* comparison operator (`<`,`>`,`<=`,`>=`,`!=`,`==`).
2. Each variable must use and refer to at least one variable created in Q2 (`var_low`, `var_mid`, `var_high`)
3. Additional values and/or operators may also be used, but `true_var` must use the `and` operator; `false_var` must use the `or` operator.
4. `true_var` should evaluate as the boolean `True`; `false_var` should evaluate as the boolean `False`

# actual variable creation will differ
true_var = (var_low < var_mid) and (var_high >= var_mid)
false_var = (var_mid == var_low) or (var_high < var_mid)

assert isinstance(true_var, bool)
assert true_var

assert isinstance(false_var, bool)
assert not false_var

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- both variables reference `var_low`, `var_mid`, or `var_high` at least once (0.2)
- both variables reference use at least one comparison operator (0.2)
- `true_var` uses `and`; `false_var` uses `or`  (0.1)

=== END MARK SCHEME ===


### Q4 - Variables (1 point)

Consider each of the following scenarios and determine what type of collection (list, tuple, dictionary) would be best to use. For each scenario, store 'list', 'tuple' or 'dictionary' in the variable specified, depending upon which is best for the given scnenario. (Note: Capitalization and spelling matter.)


For example, for `scenario_A`, if you thought the correct answer were 'list' your answer in the answer cell would be:

```python
scenario_A = 'list'
```

Scenarios:

- `scenario_A` | You want to store all of the names of the films that won an Academy Award last year.
- `scenario_B` | You want to keep a record of all the email addresses (and only the email addresses) of all of Directors working in Hollywood, so that you can email them your brilliant ideas whenever you have them. 
- `scenario_C` | You want to store the names *and* email addresses of all of the Directors working in Hollywood, so that you can email them your brilliant ideas whenever you have them *and* address the email to the right name. 
- `scenario_D` | You want to keep a record of all of the films that have ever won an Academy award and the year in which that award was won.

scenario_A = 'tuple'
scenario_B = 'list'
scenario_C = 'dictionary'
scenario_D = 'dictionary'

assert scenario_A in ['tuple', 'list', 'dictionary']
assert scenario_A == 'tuple'

assert scenario_B in ['tuple', 'list', 'dictionary']
assert scenario_B == 'list'

assert scenario_C in ['tuple', 'list', 'dictionary']
assert scenario_C == 'dictionary'

assert scenario_D in ['tuple', 'list', 'dictionary']
assert scenario_D == 'dictionary'

## Part 2: Collections & Indexing  (3 points)

### Q5 - Lists & Indexing (2.25 points)

#### Part 1 (0.75 points)

Generate a list called `midterm_list` that meets the following criteria:

- contains 7 elements/items 
- has 2 strings, 2 floats, 1 boolean, 1 list, and 1 tuple as its elements

The specific elements in the list `midterm_list` are up to you and can be stored in any order/position within the list, so long as they're in there and of the types specified above.

# actual values will differ
midterm_list = ['a', 'b', 2.2, 2.9, True, ['internal', 'list'], (2,3)]

assert midterm_list
assert isinstance(midterm_list, list)

#hidden test to ensure conditions specified in instructions were followed
assert len(midterm_list) == 7

#hidden test to ensure conditions specified in instructions were followed
float_count = 0
string_count = 0
bool_count = 0
list_count = 0
tuple_count = 0

for n in midterm_list:
    if isinstance(n, float):
        float_count += 1
    if isinstance(n, str):
        string_count += 1
    if isinstance(n, bool):
        bool_count += 1
    if isinstance(n, list):
        list_count += 1
    if isinstance(n, tuple):
        tuple_count += 1

assert float_count == 2
assert string_count == 2
assert bool_count == 1
assert list_count == 1
assert tuple_count == 1

#### Part 2 (1.5 points)

Using the list you defined in Part 1 (`midterm_list`), ***use indexing*** to return the slice/element of the list specified below, storing it in the variable name provided:

- `slice_1` | stores the third, fourth, and fifth elements in `midterm_list`
- `slice_2` | stores the first, third, and fifth elements in `midterm_list`
- `slice_3` | uses ***negative indexing*** to return the single element stored in the second position from the end of `midterm_list`

Note on wording: the first _element_ in a given list is the same as the 0<sup>th</sup> _index_ of that list.


### BEGIN SOLUTION
slice_1 = midterm_list[2:5]
slice_2 = midterm_list[0:6:2]
slice_3 = midterm_list[-2]
### END SOLUTION

assert slice_1
assert len(slice_1) == 3
assert slice_1 == midterm_list[2:5]

assert slice_2
assert len(slice_2) == 3
assert slice_2 == midterm_list[0:6:2]

assert slice_3
assert slice_3 == midterm_list[-2]

### Q6 - Dictionaries (0.75 points)

Generate a dictionary called `midterm_dict` that meets the following criteria:

- has three keys: 'name', 'age', and 'major'
- stores _your_ `name` (string), `age` (int), and `major` (string) as each key's value

(Note: I don't care if you use your real name, age, and major as the values in the dictionary, so long as they are of the specified type.)

midterm_dict = {'name': 'Shannon',
               'age' : 32,
               'major': 'biology'}

assert midterm_dict
assert isinstance(midterm_dict, dict)

#hidden test to ensure conditions specified in instructions were followed
assert len(midterm_dict) == 3

#hidden test to ensure conditions specified in instructions were followed
assert isinstance(midterm_dict['age'], int)
assert isinstance(midterm_dict['name'], str)
assert isinstance(midterm_dict['major'], str)

## Part 3: Control Flow - Conditionals & Loops  (5.5 points)

### Q7 - Conditionals (1.5 points)

Store your first name as a string in the variable `my_name`.

Write a conditional that will determine if there are more letters in your name (`my_name`) relative to the number of letters in the `comparison_name` (provided below, and storing the string 'Shannon').

If your name is:
- shorter than the `comparison_name`, store the string 'shorter' in the variable `output`
- longer than the `comparison_name`, store the string 'longer' in the variable `output`
- the same length as `comparison_name`, store the string 'same length' in the variable `output`

Note: Do not hard-code. This means your code should work (store the correct string in `output`) regardless of the specific strings stored in `comparison_name` or `my_name`. 

# comparison_name is provided for you
# do not change its value
comparison_name = 'Shannon'

# code will differ based on who is taking the exam
my_name = 'Shannon'

if len(my_name) < len(comparison_name):
    output = 'shorter'
elif len(my_name) > len(comparison_name):
    output = 'longer'
elif len(my_name) == len(comparison_name):
    output = 'same length'
else:
    print('something has gone awry')


assert my_name
assert output
# test to ensure no typos in string
assert output in ['shorter', 'longer', 'same length']

comparison_name = 'Shannon'

if len(my_name) < len(comparison_name):
    output_check = 'shorter'
elif len(my_name) > len(comparison_name):
    output_check = 'longer'
elif len(my_name) == len(comparison_name):
    output_check = 'same length'

assert output_check == output

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===

- uses if, elif, else OR if, elif, elif syntax correctly (0.25)
- conditionals correct (0.5 points)
- `output` assigned a string value (even if there are typos in string) (0.25)

=== END MARK SCHEME ===

### Q8 - `for` loop (2 points)

Background: Imagine that in a few weeks you find yourself wanting to talk to someone on the instructional staff who has actually completed the COGS 18 final project. When this happens, you suddenly remember you created a list of all the staff members in COGS 18 earlier in the quarter when you were practicing with lists. Perfect! You can use this to help you figure out who you should talk to, since you know that all of the IAs previously took COGS 18 and completed the project. They will be able to discuss their experience with you!

The list of staff members and their role is below and is called `staff`. Run the cell below to generate the `staff` list.


Then, write code to loop through the provided list. Within the loop, write code that will store any entry in the list with '\_IA' in the entry into a new list. Store this (the entries in `staff` corresponding to IAs) in a new list called `to_contact`.

# run this to create list
staff = ['Anu_IA', 'Bob_IA', 'Boning_IA', 'Bora_IA', 'David_TA', 'Emma_IA', 
         'Ellis_Prof', 'Frank_IA', 'Mani_IA', 'Harrison_IA', 'Shivani_TA']

# code will differ based on who is taking the exam
to_contact = []

for person in staff:
    if '_IA' in person:
        to_contact.append(person)

to_contact

assert to_contact

assert to_contact == ['Anu_IA',
                     'Bob_IA',
                     'Boning_IA',
                     'Bora_IA',
                     'Emma_IA',
                     'Frank_IA',
                     'Mani_IA',
                     'Harrison_IA']

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===
- empty list initialized (0.25)
- for loop set up correctly (0.25)
- conditional correct (0.5)
- list extended correctly (0.5)

=== END MARK SCHEME ===

### Q9 - Completing  a task (2 points)

Imagine you want to determine the total number of students Professor Ellis has taught in COGS 18 since arriving at UCSD.

To do so, first run the cell below to create the dictionary `ellis_courses`. This dictionary stores course names and quarters as keys and the number of students enrolled as values.

Then, using the information in the `ellis_courses` dictionary, determine what code constructs you would need to sum the values for the students who have taken cogs18 with Professor Ellis since Winter 2019. Store this value in the variable `cogs18_students`. 

Note: Do not hard-code. Your answer should use the code constructs taught so far in the course. For example, if the values in the dictionary were to be updated, your code should still produce the correct result.


# run this to create ellis_courses dictionary
ellis_courses = {'cogs9_wi19': 326,
                 'cogs108_sp19': 825,
                 'cogs18_sp19' : 272,
                 'cogs9_fa19' : 292,
                 'cogs18_fa19' : 301,
                 'cogs108_wi20' : 442,
                 'cogs18_sp20' : 307,
                 'cogs108_sp20' : 469,
                 'cogs18_su20' : 88,
                 'cogs18_fa20' : 330,
                 'cogs108_fa20' : 498
}

# Note: we accepted answers that summed all COGS18 classes or all COGS 18 classes other than those in 2019
cogs18_students = 0

for key in ellis_courses:
    if 'cogs18' in key:
        cogs18_students = cogs18_students + ellis_courses[key]

cogs18_students

assert cogs18_students 

assert cogs18_students == 1298 or cogs18_students == 725

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===
- counter initialized correctly (0.25)
- loop set up correctly (0.25)
- conditional used/checks membership correctly (0.5)
- value accessed from dictionary correctly (0.25)
- counter increased correctly (0.25)

=== END MARK SCHEME ===

### Submit on Datahub

Good work - you're done!

Check your work, and then when you're ready, **submit on datahub**.

We will not have your exam until you click submit and see this show up under 'submitted assignments'.