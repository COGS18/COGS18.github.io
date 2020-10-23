# COGS 18 - Practice Exam

This is the practice exam for Fall 2020. It covers topics through the Dictionaries Lecture.

This exam is out of 0 points, worth 0% of your grade, but the real thing will be out of 12.5 points.

**PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**

**PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE EXAM.** (Note that you can add additional cells, if you want to test things out.

## Instructions
^ these are the instructions you will see on your real exam

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
^ The headers and point values correspond to the actual headers and point values you'll have for each section on your exam

### Example Q1 - Variables & Operators 

In the cell below, create three variables: `var_a`, `var_b`, and `var_c`.

These variables must satisfy the following requirements:

1. `var_a` must store a float (you get to choose the specific float)
2. `var_b` must use *at least two* of the comparison operators (`<`,`>`,`<=`,`>=`,`!=`,`==`) and store (return) the value `True`. 
3. `var_c` must use *at least two* of the math operators (`+`, `-`, `/`, `*`, `**`, `%`, `//`) and store the value 36

# actual variable creation will differ
var_a = 7.3
var_b = 6 == 6 and 3 <= 4
var_c = (6 + 3) * 4

# check my work (optional)
print(var_a, var_b, var_c)

# check variable exists
assert var_a is not None


assert isinstance(var_b, bool)


# check variable exists
assert var_c is not None


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

## Part 2: Collections & Indexing  (3 points)

### Example Q2 - Indexing

Given a the list `my_list` provided below, include code below *using indexing* to return the values specified below from `my_list`.


1. In `list_a`, index `my_list` such that it will store (return) `['c', 'd']`
2. In `list_b`, index `my_list` such that it will store (return) `['a', 'c', 'e']`

# my_list is provided for you
my_list = ['a', 'b', 'c', 'd', 'e']

# specific indexing approaches may differ
list_a = my_list[2:4]
list_b = my_list[0::2]

# check my work (optional)
print(list_a, list_b)

assert isinstance(list_a, list)


assert isinstance(list_b, list)


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

## Part 3: Control Flow - Conditionals & Loops  (5.5  points)

**Note**: This section is longer and has more questions than what will be on your exam; however, this is where students struggle the most, so I wanted to give you more practice questions.

### Example Q3 - `while` loop

Include code in your answer below that:

1. Creates (initializes) a counter `counter` that starts at 0
2. Creates (initializes) an empty list `out`
3. Creates a loop that will run as long as the value of `counter` is less than or equal to 10
    - Within the loop:
        - first: if the value of `counter` is odd, `append` the value of `counter` to the list `out`
        - then: increase the value of `counter` by 1 each time through the loop 

# the question we did together in lecture
counter = 0
out = []

# loop until counter <= 10
while counter <= 10:
    # check if counter odd:
    if counter % 2 != 0:
        out.append(counter)
    counter = counter + 1
       # append counter to out
       # increase counter by 1
out

assert counter > 0 & counter < 100


assert isinstance(out, list)


### Example Q4 - `for` loop

Store your first name as a string in the variable `my_name` and initialize a `counter` (use that variable name).

Then, write a `for` loop that loops through the letters of your first name, increasing the counter by one for each consonant (non-vowel) in your name. 

The value stored in the counter at the end of your loop’s execution should be the number of consonants in your first name. Be sure that 'B' and 'b' are counted as the same letter in your code.


# code/output will differ based on who is taking the exam
my_name = 'Shannon'
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
counter = 0

for char in my_name:
    if char not in vowels:
        counter += 1

# check my work (optional)
print(counter)

assert isinstance(counter, int)
assert isinstance(my_name, str)


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)



### Example Q5  - `dictionary`

Write code that will generate a dictionary `name_consonants` that stores each consonant letter in `my_name` (defined in previous question) as a key in the dictionary, and the number of times each consonant shows up in `my_name` as the letter's value. 

Noe that this code should run, regardless of what string is stored in `my_name`.

For example, `name_consonants` for 'Shannon' would return:

```
{'s': 1, 'h': 1, 'n': 3}
```

Note that if you have no consonants in your name, this code would still run, but would return an empty dictionary.

# code/output will differ based on who is taking the exam
# note that we didn't take off points if the first letter was or was not capitalized when grading
name_consonants = {}
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
            
for char in my_name:
    if char not in vowels:
        if char not in name_consonants:
            name_consonants[char] = 1
        else:
            name_consonants[char] += 1

# check my work (optional)
name_consonants

assert isinstance(name_consonants, dict)


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)



### Example Q6  - Loops

Write code that will loop through the `name_consonants` dictionary created in the previous question and store the sum of the values in the dictionary into `consonant_count`. (For the name Shannon, `consonant_count` would store 5).

Be sure your answer refers back to `name_consonants` defined in the previous question

# output will differ based on who is taking the exam
consonant_count = 0

for key in name_consonants:
    consonant_count += name_consonants[key]

# check my work (optional)          
print(consonant_count)

assert consonant_count is not None


##### **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)



### Submit on Datahub

Good work - you're done!

Check your work, and then when you're ready, **submit on datahub**.

We will not have your exam until you click submit and see this show up under 'submitted assignments'.