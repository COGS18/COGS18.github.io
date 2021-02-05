# COGS 18 - Exam 1

This is the first exam for Winter 2021. It covers topics through the Dictionaries Lecture.

This exam is out of 12.5 points, worth 12.5% of your grade.

**PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**

**PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE ASSIGNMENT.** (Note that you can add additional cells, if you want to test things out.

## Instructions

#### Timing
- The exam is designed to take you ~1h.
- There will be a 72hour ~24 hour~ window during which you can complete this exam (due Mon 8AM).
- If it takes you longer than 1h, you're free to use that time.

#### The Rules
- You are to complete this exam on your own.
- This is open-notes & open-Google
- You may not talk to any humans about this exam. 
- The following are all *prohibited*:
    - text/phone/online chat communication
    - posting questions to a message board where a human could respond
    - asking anyone via any form about a question on this test directly
- Clarification questions will ***not*** be allowed and there will be no posting on Campuswire about the exam at all. 
    - Campuswire posts about the exam will not be answered and will be deleted. 
    - Students who post questions about the exam to Campuswire are at risk of losing points on the exam.
    - If you are confused about wording, add a note to your exam explaining your confusion and how you interpreted the question. 
    - Note: This policy is b/c we are incapable of responding for 24h straight. This is the only way to make it fair across the board for students.

 <span style="color: red;">Note: </span> There _is_ a chance for partial credit on some questions, so _some_ code is better than _no_ code. Even if it throws an error, having some code that partially answers the question will benefit you/your grade.

### Q0 - Honor Code (0.1 points - bonus)

In the cell below, include a variable `honor_code` that stores the boolean `True` if you agree to the following statement:

>I agree that this exam was completed individually with the knowlege in my brain, information the notes from this course, and/or with searching for help on the Internet without searching for answers to these questions directly. I did not ask anyone about specific questions on this exam. I did not post these questions (in part or in whole) on the Internet.


### BEGIN SOLUTION
honor_code = True
### END SOLUTION

assert honor_code

## Part 1: Variables & Operators (3 points)

### Q1 - Variables (1 point)

In the cell below, create three variables: `var_int`, `var_float`, and `var_combined`. 

- `var_int` should store an integer
- `var_float` should store a float
- `var_combined` should use a math operator to add `var_int` and `var_float` together

The specific values you use to generate `var_int` and `var_float` are up to you, as long as they fulfull the criteria specified.

### BEGIN SOLUTION
# actual values stored will differ
var_int = 10
var_float = 1.0 
var_combined = var_int + var_float
### END SOLUTION

# check variable exists
assert var_int is not None
### BEGIN HIDDEN TESTS
assert isinstance(var_int, int)
### END HIDDEN TESTS

# check variable exists
assert var_float is not None
### BEGIN HIDDEN TESTS
assert isinstance(var_float, float)
### END HIDDEN TESTS

# check variable exists
assert var_combined is not None
### BEGIN HIDDEN TESTS
assert isinstance(var_combined, float)
assert var_combined == var_int + var_float
### END HIDDEN TESTS

### Q2 - Math Operators (1 point)

In the cell below, create three variables: `var_even`, `var_odd`, and `var_operator`.

Across these three variables:
- all seven math operators (`+`, `-`, `/`, `*`, `**`, `%`, `//`) must be used _at least once_ 
- `var_even` must store an even number
- `var_odd` must store an odd number
- `var_operator` can include other variables/numbers but must use (refer to) the variables `var_even` *and* `var_odd` during assignment and must store (have the value) 6 (or 6.0)

### BEGIN SOLUTION
# actual operations will differ
var_odd = (9 + 2 - 1) % 3
var_even = 25 / 5 * 2 // 1
var_operator = var_odd ** var_even + 5
### END SOLUTION

assert var_odd is not None
### BEGIN HIDDEN TESTS
assert var_odd % 2 != 0
### END HIDDEN TESTS

assert var_even is not None
### BEGIN HIDDEN TESTS
assert int(var_even % 2) == 0
### END HIDDEN TESTS

assert var_operator is not None
### BEGIN HIDDEN TESTS
assert isinstance(var_operator, float) or isinstance(var_operator, int)
assert var_operator == 6
### END HIDDEN TESTS

### Q3 - Comparison Operators (1 point)

Your answer will define two variables: `true_var` and `false_var`.

These variables must satisfy the following requirements:

1. Each variable must be defined using *at least one* comparison operator (`<`,`>`,`<=`,`>=`,`!=`,`==`).
2. Each variable must use and refer to at least one variables defined below (`var_low`, `var_mid`, `var_high`)
3. Additional values and/or operators may also be used, but `true_var` must use the `or` operator; `false_var` must use the `and` operator.
4. `true_var` should evaluate as the boolean `True`; `false_var` should evaluate as the boolean `False`

# these variables provided for you
# this cell is read-only (cannot be changed)
var_low = 35 % 11
var_mid = 5 ** 2
var_high = (14 + 2) * 6

### BEGIN SOLUTION
# actual variable creation will differ
true_var = (var_low < var_mid) or (var_high >= var_mid)
false_var = (var_mid != var_low) and (var_high < var_mid)
### END SOLUTION

assert isinstance(true_var, bool)
### BEGIN HIDDEN TESTS
assert true_var
### END HIDDEN TESTS

assert isinstance(false_var, bool)
### BEGIN HIDDEN TESTS
assert not false_var
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- both variables reference `var_low`, `var_mid`, or `var_high` at least once (0.2)
- both variables reference use at least one comparison operator (0.2)
- `true_var` uses `or`; `false_var` uses `and`  (0.1)

=== END MARK SCHEME ===


## Part 2: Collections & Indexing  (3 points)

### Q4 - Lists & Indexing (2.25 points)

#### Part 1 (0.75 points)

Generate a list called `midterm_list` that meets the following criteria:

- contains 6 elements/items 
- has 2 strings, 1 float, 1 boolean, 1 dictionary, and 1 tuple as its elements

The specific elements in the list `midterm_list` are up to you and can be stored in any order/position within the list, so long as they're in there and of the types specified above.

### BEGIN SOLUTION
# actual values will differ
midterm_list = ['a', 'b', 2.9, True, {'A':1, 'B':2}, (2, 3)]
### END SOLUTION

assert midterm_list
### BEGIN HIDDEN TESTS
assert isinstance(midterm_list, list)
### END HIDDEN TESTS

#hidden test to ensure conditions specified in instructions were followed
### BEGIN HIDDEN TESTS
assert len(midterm_list) == 6
### END HIDDEN TESTS

#hidden test to ensure conditions specified in instructions were followed
### BEGIN HIDDEN TESTS
float_count = 0
string_count = 0
bool_count = 0
dict_count = 0
tuple_count = 0

for n in midterm_list:
    if isinstance(n, float):
        float_count += 1
    if isinstance(n, str):
        string_count += 1
    if isinstance(n, bool):
        bool_count += 1
    if isinstance(n, dict):
        dict_count += 1
    if isinstance(n, tuple):
        tuple_count += 1

assert float_count == 1
assert string_count == 2
assert bool_count == 1
assert dict_count == 1
assert tuple_count == 1
### END HIDDEN TESTS

#### Part 2 (1.5 points)

Using the list you defined in Part 1 (`midterm_list`), ***use indexing*** to return the slice/element of the list specified below, storing it in the variable name provided:

- `slice_1` | stores the second, third, and fourth elements in `midterm_list`
- `slice_2` | stores the second, fourth, and sixth elements in `midterm_list`
- `slice_3` | uses ***negative indexing*** to return the single element stored in the third position from the end of `midterm_list`

Note on wording: the first _element_ in a given list is the same as the 0<sup>th</sup> _index_ of that list.


### BEGIN SOLUTION
slice_1 = midterm_list[1:4]
slice_2 = midterm_list[1::2]
slice_3 = midterm_list[-3]
### END SOLUTION

assert slice_1
### BEGIN HIDDEN TESTS
assert len(slice_1) == 3
assert slice_1 == midterm_list[1:4]
### END HIDDEN TESTS

assert slice_2
### BEGIN HIDDEN TESTS
assert len(slice_2) == 3
assert slice_2 == midterm_list[1::2]
### END HIDDEN TESTS

assert slice_3
### BEGIN HIDDEN TESTS
assert slice_3 == midterm_list[-3]
### END HIDDEN TESTS

### Q5 - Dictionaries (0.75 points)

Generate a dictionary called `midterm_dict` that meets the following criteria:

- has three keys: 'name', 'favorite_game', and 'height'
- stores _your_ `name` (string), `favorite_game` (string), and `height` (int) in inches as each key's value

(Note: I don't care if you use your real name, favorite_game, and height as the values in the dictionary, so long as they are of the specified type.)

### BEGIN SOLUTION
midterm_dict = {'name': 'Shannon',
               'favorite_game' : 'Coup',
               'height': 65}
### END SOLUTION

assert midterm_dict
### BEGIN HIDDEN TESTS
assert isinstance(midterm_dict, dict)
### END HIDDEN TESTS

#hidden test to ensure conditions specified in instructions were followed
### BEGIN HIDDEN TESTS
assert len(midterm_dict) == 3
### END HIDDEN TESTS

#hidden test to ensure conditions specified in instructions were followed
### BEGIN HIDDEN TESTS
assert isinstance(midterm_dict['name'], str)
assert isinstance(midterm_dict['favorite_game'], str)
assert isinstance(midterm_dict['height'], int)
### END HIDDEN TESTS

## Part 3: Control Flow - Conditionals & Loops  (6.5 points)

### Q6 - Conditionals (1.5 points)

Write a conditional that will determine if you are taller, the same height as, or shorter than Professor Ellis. 

To do this, you will access (meaning, refer to) the `midterm_dict` dictionary you created in Q6 and compare *your* height with the height specified in the `height` value in the `prof_dict` dictionary defined below. 

If you are:
-  taller than Prof. Ellis, store the string 'taller' in the variable `output`
- shorter than Prof. Ellis, store the string 'shorter' in the variable `output`
- the same height as Prof Ellis, store the string 'same height' in the variable `output`

Notes: 
1. Do not hard-code. This means your code should work (store the correct string in `output`) regardless of the specific value stored for `height` in `midterm_dict`. In other words, you must use the code constructs from class to determine your answer.
2. Spelling/capitalization of the string stored in `output` matter. Be sure it matches the string specified in the instructions above.

# prof_dict is provided for you
# do not change height value - it should be 65
prof_dict = {'height': 65}

### BEGIN SOLUTION
# output will differ based on who is taking the exam
if midterm_dict['height'] < prof_dict['height']:
    output = 'shorter'
elif midterm_dict['height'] > prof_dict['height']:
    output = 'taller'
elif midterm_dict['height'] == prof_dict['height']:
    output = 'same height'
else:
    output = 'not possible'
### END SOLUTION

assert output
# test to ensure no typos in string
assert output in ['shorter', 'taller', 'same height']
### BEGIN HIDDEN TESTS
if midterm_dict['height'] < prof_dict['height']:
    test = 'shorter'
elif midterm_dict['height'] > prof_dict['height']:
    test = 'taller'
elif midterm_dict['height'] == prof_dict['height']:
    test = 'same height'
else:
    test = 'not possible'

assert test == output
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===

- uses if, elif, else OR if, elif, elif syntax correctly (0.25)
- conditionals correct (0.5 points)
- `output` assigned a string value (even if there are typos in string) (0.25)

=== END MARK SCHEME ===

### Q7 - Accomplishing a task (5 points)

Background: Professor Ellis has made a mess of her to do list (`to_do_list`, provided below). She accidentally combined her to do list with her grocery list and the the her daily step count from last week. She needs your help to detangle this mess!

**Part I (2.5 points)**

Your job is to separate `to_do_list` out into three separate lists:
- `steps` - a list of all the steps from last week (you know which values these are becuase they are integer values)
- `to_do` - a list that contains the to do list items (you know which values these are because they contain 'cogs' in the string)
- `grocery` - a list of all of the grocery list items (you know which values these are because they do NOT contain 'cogs' in the string)

Each of the above lists should contain only the elements from `to_do_list` that match the specified description above. Specifically:
- `steps` should be a list of integers
- `to_do` should be a list of strings 
- `grocery` should be a list of strings

The values in `steps`, `to_do`, and `grocery` should appear in the same relative order as in the original list (`to_do_list`).

Note: This should not be hard-coded. Your answer should use code constructs discussed in class. In other words, your code should produce the correct lists, regardless of the specific values in `to_do_list`.

# run this to create list
to_do_list = ['mushrooms', 'peanut butter', 'release cogs18 exam', 10000, 8500, 
              'release cogs108 lab', 6000, 'tahini', 15000, 'post cogs18 lectures', 
              'post cogs108 lectures', 'release cogs18 practice exam', 12000, 'pineapple', 
              'udon noodles', 18000, 8000, 'romaine lettuce']

### BEGIN SOLUTION
# there is more than one correct approach here
steps = []
to_do = []
grocery = []

for value in to_do_list:
    if isinstance(value, int):
        steps.append(value)
    else:
        if 'cogs' in value:
            to_do.append(value)
        else: 
            grocery.append(value)
### END SOLUTION

assert grocery
### BEGIN HIDDEN TESTS
assert grocery == ['mushrooms', 'peanut butter',
                   'tahini', 'pineapple', 'udon noodles',
                   'romaine lettuce']
### END HIDDEN TESTS

assert steps
### BEGIN HIDDEN TESTS
assert steps == [10000, 8500, 6000, 15000, 12000, 18000, 8000]
### END HIDDEN TESTS

assert to_do
### BEGIN HIDDEN TESTS
assert to_do ==  ['release cogs18 exam', 'release cogs108 lab',
                  'post cogs18 lectures', 'post cogs108 lectures',
                  'release cogs18 practice exam']
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===
- empty lists initialized (0.25)
- for loop set up correctly (0.25)
- conditionals correct (0.25)
- list appended correctly (0.25)

=== END MARK SCHEME ===

**Part II (2.5 points)**

Now that you've got the `steps` extracted, Professor Ellis needs a dictionary of which steps she took on which day. 

Using the values in your list `steps`, create a dictionary `steps_dict` that stores each value as a different day's steps, starting with 'Monday'. For example, the first value in the `steps` list will be the value for the key 'Monday', the second for 'Tuesday', so on and so forth. 

Be sure to spell out the day of the week, using a capital letter for the first letter in the day. The list `days_of_week` has been provided, as it may be helpful in answering the question.

Note: This should not be hard-coded. Your answer should use code constructs discussed in class. In other words, your code should produce the correct `steps_dict` if the specific values in `steps` were to change/differ.

# provided if helpful
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

### BEGIN SOLUTION
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
steps_dict = {}

# there is more than one approach here
for i in range(0,7):
    key = days_of_week[i]
    val = steps[i]
    steps_dict[key] = val
    
steps_dict
### END SOLUTION

assert steps_dict 
### BEGIN HIDDEN TESTS
# check to be sure all keys are strings
assert all(isinstance(x, str) for x in list(steps_dict.keys()))
### END HIDDEN TESTS

assert isinstance(steps_dict, dict) 
### BEGIN HIDDEN TESTS
# check to be sure all values are integers
assert all(isinstance(x, int) for x in list(steps_dict.values()))
### END HIDDEN TESTS

# hidden test to check the keys in the dictionary
### BEGIN HIDDEN TESTS
assert set(list(steps_dict.keys())) ==  set(days_of_week)
### END HIDDEN TESTS

# hidden test to check the values in the dictionary
### BEGIN HIDDEN TESTS
assert sum(steps_dict.values()) ==  77500
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===
- dictionary initialized (0.25)
- loop set up correctly (0.25)
- key and val accessed correctly (0.25)
- new value assigned to steps_dict correctly (0.25)

=== END MARK SCHEME ===

### Submit on Datahub

Good work - you're done!

Check your work, and then when you're ready, **submit on datahub**.

We will not have your exam until you click submit and see this show up under 'submitted assignments'.