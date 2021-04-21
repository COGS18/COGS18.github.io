# COGS 18 - Practice Exam

This is the practice exam for Spring 2021. It covers topics through the Dictionaries Lecture.

This exam is out of 0 points, worth 0% of your grade, but the real thing will be out of 12.5 points.

**PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**

**PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE EXAM.** (Note that you can add additional cells, if you want to test things out.)

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
    - posting questions to a message board where a human could respond
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
^ The headers and point values correspond to the actual headers and point values you'll have for each section on your exam

### Example Q1 - Variables & Operators 

In the cell below, create three variables: `var_a`, `var_b`, and `var_c`.

These variables must satisfy the following requirements:

1. `var_a` must store a float (you get to choose the specific float)
2. `var_b` must use *at least two* of the comparison operators (`<`,`>`,`<=`,`>=`,`!=`,`==`) and store (return) the value `True`. 
3. `var_c` must use *at least two* of the math operators (`+`, `-`, `/`, `*`, `**`, `%`, `//`) and store the value 36

### BEGIN SOLUTION
# actual variable creation will differ
var_a = 7.3
var_b = 6 == 6 and 3 <= 4
var_c = (6 + 3) * 4
### END SOLUTION

# check variable exists
assert var_a is not None

### BEGIN HIDDEN TESTS
assert isinstance(var_a, float)
### END HIDDEN TESTS

assert isinstance(var_b, bool)

### BEGIN HIDDEN TESTS
assert var_b 
### END HIDDEN TESTS

# check variable exists
assert var_c is not None

### BEGIN HIDDEN TESTS
assert var_c == 36
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

## Part 2: Collections & Indexing  (3 points)

### Example Q2 - Indexing

Given a the list `my_list` provided below, include code below *using indexing* to return the values specified below from `my_list`.


1. In `list_a`, index `my_list` such that it will store (return) `['c', 'd']`
2. In `list_b`, index `my_list` such that it will store (return) `['a', 'c', 'e']`

# my_list is provided for you
my_list = ['a', 'b', 'c', 'd', 'e']

### BEGIN SOLUTION
# specific indexing approaches may differ
list_a = my_list[2:4]
list_b = my_list[0::2]
### END SOLUTION

assert isinstance(list_a, list)

### BEGIN HIDDEN TESTS
assert list_a == ['c', 'd']
### END HIDDEN TESTS

assert isinstance(list_b, list)

### BEGIN HIDDEN TESTS
assert list_b == ['a', 'c', 'e']
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

## Part 3: Control Flow - Conditionals & Loops  (5.65  points)

**Note**: This section is longer and has more questions than what will be on your exam; however, this is where students struggle the most, so I wanted to give you more practice questions.

### Example Q3 - `while` loop

Include code in your answer below that:

1. Creates (initializes) a counter `counter` that starts at 0
2. Creates (initializes) an empty list `out`
3. Creates a loop that will run as long as the value of `counter` is less than or equal to 10
    - Within the loop:
        - first: if the value of `counter` is odd, `append` the value of `counter` to the list `out`
        - then: increase the value of `counter` by 1 each time through the loop 

### BEGIN SOLUTION
out = []
counter = 0 

while counter <= 10: 
    if counter % 2 != 0:
        out.append(counter)

    counter += 1
### END SOLUTION

assert counter > 0 & counter < 100

### BEGIN HIDDEN TESTS
assert counter == 11
### END HIDDEN TESTS

assert isinstance(out, list)

### BEGIN HIDDEN TESTS
assert out == [1, 3, 5, 7, 9]
### END HIDDEN TESTS

### Example Q4 - `for` loop

Store your first name as a string in the variable `my_name` and initialize a `counter` (use that variable name).

Then, write a `for` loop that loops through the letters of your first name, increasing the counter by one for each consonant (non-vowel) in your name. 

The value stored in the counter at the end of your loop’s execution should be the number of consonants in your first name. Be sure that 'B' and 'b' are counted as the same letter in your code.


### BEGIN SOLUTION
# code will differ based on who is taking the exam
my_name = 'Shannon'
counter = 0

for char in my_name:
    char = char.lower()
    if char not in ['a', 'e', 'i', 'o', 'u']:
        counter += 1
        
# OR
# note `vowels` could also be a string
vowels = ['A','E','I','O','U', 'a', 'e', 'i', 'o', 'u']
counter = 0

for char in my_name:
    if char not in vowels:
        counter += 1
### END SOLUTION

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

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===

- counter & my_name created (0.25 points)
- for loop initialized correctly (0.25 points)
- capitalization accounted for (0.5 points)
- conditional correct (0.5 points)

=== END MARK SCHEME ===

### Example Q5  - `dictionary`

Write code that will generate a dictionary `name_consonants` that stores each consonant letter in `my_name` (defined in previous question) as a key in the dictionary, and the number of times each consonant shows up in `my_name` as the letter's value. 

Noe that this code should run, regardless of what string is stored in `my_name`.

For example, `name_consonants` for 'Shannon' would return:

```
{'s': 1, 'h': 1, 'n': 3}
```

Note that if you have no consonants in your name, this code would still run, but would return an empty dictionary.

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

# OR (different version b/c wording was not super clear)
# and we haven't yet discussed .lower()

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

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===

- refers back to my_name variable (0.5 points)
- for loop initialized correctly (0.5 points)
- capitalization accounted for (0.5 points)
- conditional correct (0.5 points)
- dictionary incremented correctly (0.5 points)

=== END MARK SCHEME ===

### Example Q6  - Loops

Write code that will loop through the `name_consonants` dictionary created in the previous question and store the sum of the values in the dictionary into `consonant_count`. (For the name Shannon, `consonant_count` would store 5).

Be sure your answer refers back to `name_consonants` defined in the previous question

### BEGIN SOLUTION
# output will differ based on who is taking the exam
consonant_count = 0

for key in name_consonants:
    consonant_count += name_consonants[key]
### END SOLUTION

assert consonant_count is not None

### BEGIN HIDDEN TESTS
check = 0

for key in name_consonants:
    check += name_consonants[key]
    
assert consonant_count == check
### END HIDDEN TESTS

##### **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===

- counter initialized (0.25)
- for loop correct (0.25)
- accessing dictionary/increase counter correct (0.5)

=== END MARK SCHEME ===

### Example Q7 - `for` loop (2 points)

Background: Imagine that in a few weeks you find yourself wanting to talk to someone on the instructional staff who has actually completed the COGS 18 final project. When this happens, you suddenly remember you created a list of all the staff members in COGS 18 earlier in the quarter when you were practicing with lists. Perfect! You can use this to help you figure out who you should talk to, since you know that all of the IAs previously took COGS 18 and completed the project. They will be able to discuss their experience with you!

The list of staff members and their role is below and is called `staff`. Run the cell below to generate the `staff` list.


Then, write code to loop through the provided list. Within the loop, write code that will store any entry in the list with '\_IA' in the entry into a new list. Store this (the entries in `staff` corresponding to IAs) in a new list called `to_contact`.

# run this to create list
staff = ['Anu_IA', 'Bob_IA', 'Boning_IA', 'Bora_IA', 'David_TA', 'Emma_IA', 
         'Ellis_Prof', 'Frank_IA', 'Mani_IA', 'Harrison_IA', 'Shivani_TA']

### BEGIN SOLUTION
# code will differ based on who is taking the exam
to_contact = []

for person in staff:
    if '_IA' in person:
        to_contact.append(person)

to_contact
### END SOLUTION

assert to_contact

### BEGIN HIDDEN TESTS
assert to_contact == ['Anu_IA',
                     'Bob_IA',
                     'Boning_IA',
                     'Bora_IA',
                     'Emma_IA',
                     'Frank_IA',
                     'Mani_IA',
                     'Harrison_IA']
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===
- empty list initialized (0.25)
- for loop set up correctly (0.25)
- conditional correct (0.5)
- list extended correctly (0.5)

=== END MARK SCHEME ===

### Example Q8 - Completing  a task (2 points)

Imagine you want to determine the total number of students Professor Ellis has taught in COGS 18 since arriving at UCSD.

To do so, first run the cell below to create the dictionary `ellis_courses`. This dictionary stores course names and quarters as keys and the number of students enrolled as values.

Then, using the information in the `ellis_courses` dictionary, determine what code constructs you would need to sum the values for the students who have taken cogs18 with Professor Ellis during this time. Store this value in the variable `cogs18_students`. 

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

### BEGIN SOLUTION
cogs18_students = 0

for key in ellis_courses:
    if 'cogs18' in key:
        cogs18_students = cogs18_students + ellis_courses[key]

cogs18_students
### END SOLUTION

assert cogs18_students 

### BEGIN HIDDEN TESTS
assert cogs18_students == 1298
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===
- counter initialized correctly (0.25)
- loop set up correctly (0.25)
- conditional used/checks membership correctly (0.5)
- value accessed from dictionary correctly (0.25)
- counter increased correctly (0.25)

=== END MARK SCHEME ===

### Example Q9 - Accomplishing a task

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
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
                'Friday', 'Saturday', 'Sunday']

### BEGIN SOLUTION
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
steps_dict = {}

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