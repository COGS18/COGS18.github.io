# COGS 18 - Practice Final Exam

This is the practice final exam for Winter 2021. It covers topics through the end of the course.

This exam is out of 0 points, worth 0% of your grade. (The real final will be worth 19% of your grade)

**PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**

**PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE EXAM.** (Note that you can add additional cells, if you want to test things out.

## Instructions

#### Timing
- The exam is designed to take you ~2-3 hours.
- If it takes you longer than 2-3 hours, you're free to use that time.

#### The Rules
- You are to complete this exam on your own.
- This is open-notes & open-Google.
- You may not talk to any humans about this exam. 
- The following are all *prohibited*:
    - text/phone/online chat communication
    - posting questions to a message board where a human could respond
    - asking anyone via any form about a question on this test directly
- Clarification questions will ***not*** be allowed and there will be no posting on Campuswire about the exam at all. 
    - Campuswire posts about the exam will not be answered and will be deleted. 
    - Students who post questions about the exam to Campuswire are at risk of losing points on the exam.
    - If you are confused about wording, add a note to your exam explaining your confusion and how you interpreted the question. 
    - Note: This policy is b/c we are incapable of responding for 3d straight. This is the only way to make it fair across the board for students.

 <span style="color: red;">Note: </span> There _is_ a chance for partial credit on some questions, so _some_ code is better than _no_ code. Even if it throws an error, having some code that partially answers the question will benefit you/your grade.

## Part 1: Variables, Conditionals, & Loops (3.5 points)

### Q1 - Conditionals (2 points)

**Goal**: Given a character, return the capitalized character in the reverse position within the alphabet in the variable `output`. For example, if the input character is 'A' or 'a', `output` would store 'Z'. If the character is 'B' or 'b', the `output` would store 'Y'. (and vice versa: the input 'Z' or 'z' would store 'A' in `output`).

**Approach**:

Using the three variables provided below (`alpha`, `reverse_alpha`, and `char`), write code to acommplish the following:
- check if the in input variable (`char`) is a string of length 1:
     - if it is:
         - convert the input (`char`) to upper case
         - check to see if this upper case value is a value in `alpha`
             - if it is: use `reverse_alpha` (provided below) to store the reverse alphabetical position in `output`
     - otherwise (if the input is not a string of length 1):
         - `output` should store `None`          
         
Note: feel free to test your code with values of `char` other than `'m'`, but be sure that `char = 'm'` when you submit your exam.

# these three variables provided
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
reverse_alpha = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
char = 'm'

### BEGIN SOLUTION
if type(char) == str and len(char) == 1:
    char = char.upper()
    if char in alpha:
        position = alpha.find(char)
        output = reverse_alpha[position]
else: 
    output = None
### END SOLUTION

assert output is not None

### BEGIN HIDDEN TESTS
assert output == 'N'
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- if hard-coded, no partial credit
- correctly checks if str/length 1 (0.5)
- converts to upper case correctly (0.25)
- checks if in alpha correctly (0.25)
- finds position in reverse list correctly (0.5) 

=== END MARK SCHEME ===

### Q2 - Loops (1.5 points)

Let's build on that last question! 

Here, you will write code that will again find the reverse alphabetical position; however, in this code, you will need to be able to do this for an entire string, not just a single character. 

Your code should again use `alpha` and `reverse_alpha` (from Q1), but should return the character in the reverse alphabetical position for the entire string stored in `input_string`. Store the reverse alphabetical string (which should be in all CAPS in the variable `output_string`.

If the upper case of any character in your string is not in `alpha`, `output_string` should store `None`.

Notes:
1. Your code can assume `input_string` is a string and your code does not need to check this.
2. Feel free to test your code with values of `input_string` other than `'HELLO'`, but be sure that `input_string = 'HELLO'` when you submit your exam.


input_string = 'HELLO'

### BEGIN SOLUTION
output_string = ''

for char in input_string:
    char = char.upper()
    if char in alpha:
        position = alpha.find(char)
        output_string += reverse_alpha[position]
    else:
        output_string = None
        break
        
output_string
### END SOLUTION

assert output_string is not None

### BEGIN HIDDEN TESTS
assert output_string == 'SVOOL'
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- if hard-coded, no points
- loops through string correctly (0.25)
- extends string correctly (0.5)
- sets output_string to None correctly (0.25)

=== END MARK SCHEME ===

## Part 2: Functions & Testing (5 points)

### Q3 - `atbash_encrypt` (2.5 points)

Let's continue the process!

Write a function `atbash_encrypt()` that takes a string as its input and returns the reverse alphabetical string as its output (the same task as Q2...just turning it into a function).

Remember that functions have their own namespace, so you'll likely want to redefine `alpha` and `reverse_alpha` in your function directly. (I promise this will come in handy later in the exam...)

### BEGIN SOLUTION
def atbash_encrypt(input_string):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reverse_alpha = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

    output_string = ''

    for char in input_string:
        char = char.upper()
        if char in alpha:
            position = alpha.find(char)
            output_string += reverse_alpha[position]
        else:
            output_string = None
            break
        
    return output_string
### END SOLUTION

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)

assert atbash_encrypt is not None

### BEGIN HIDDEN TESTS
assert atbash_encrypt('cogs') == 'XLTH'
### END HIDDEN TESTS

assert callable(atbash_encrypt)

### BEGIN HIDDEN TESTS
assert atbash_encrypt('COGS') == 'XLTH'
### END HIDDEN TESTS

### Q4 - Test Function: `test_atbash_encrypt` (2.5 points)

Write a test function `test_atbash_encrypt()` that:

1. contains at least three asserts that test the functionality of `atbash_encrypt()`
2. passes silently when executed

### BEGIN SOLUTION
# specific tests will differ
def test_atbash_encrypt():
    assert callable(atbash_encrypt)
    assert isinstance(atbash_encrypt('HELLO'), str)
    assert atbash_encrypt('HELLO') == 'SVOOL'
    assert atbash_encrypt('hello') == 'SVOOL'
### END SOLUTION

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)

assert callable(test_atbash_encrypt)

### BEGIN HIDDEN TESTS
try:
    test_atbash_encrypt()
    out = 'good'
except:
    out = 'bad'
    
assert out == 'good'
### END HIDDEN TESTS

##### **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- test function defined correctly (0.25)
- contains at least three asserts (0.5)
- asserts are meaningful for function (0.75)

=== END MARK SCHEME ===

## Part 3: Style & Documentation (11 points)

### Q5 - Code Style (3 points)

In the file `atbash.py`, there is a function `atbash_decrypt()`. The code is functional and the function name is the name we want; however, within the function, the variable naming and code style need improvement. And, documentation and code comments are completely missing.

Edit the function in `atbash.py` to:
1. Improve the function's variable naming (but: do *not* change the function's name)
2. Improve the overall code style (using what we discussed in class about PEP8)
3. Add a `numpy` style docstring (at the level discussed in class)
4. Add code comments where needed

Be sure to save changes in `atbash.py` when completed. 

Note: You do not have to actually add any code to this notebook for this question. All changes occur in `atbash.py`. (Partial credit for this question is awarded at the end of the exam.)

### Q6 - `atbash.py` (1 point)

You now have two functions and two test functions, but they're not all yet organized! Let's do that now...

**`atbash.py`**
1. Add `atbash_encrypt()` (from Q3) to `atbash.py`
2. Add a `numpy`-style docstring & appropriate code comments to `atbash_encrypt()` (if you haven't already) in `atbash.py`.
3. Double check the naming/code style used in `atbash_encrypt()` - improve if needed

**`test_atbash.py`**
1. Add `test_atbash_encrypt` (from Q4) to `test_atbash.py`
2. Update `import` statement at top (if needed)

Once completed, `import` both of the functions from `atbash.py` below, such that the code `ab.atbash_encrypt('HELLO')` and `ab.atbash_decrypt('SVOOL')` both execute without issue.

Note: You may have to restart your kernel for the `import` to work without issue.

The assert cells below this question only test the import. The style/tests will be manually graded in Q7 (which is why that one is worth so many points).

### BEGIN SOLUTION
import atbash as ab
### END SOLUTION

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to check your work (optional)

assert callable(ab.atbash_encrypt)

# hidden test to ensure atbash_encrypt works on import
### BEGIN HIDDEN TESTS
assert ab.atbash_encrypt('HELLO') == 'SVOOL'
### END HIDDEN TESTS

assert callable(ab.atbash_decrypt)

# hidden test to ensure atbash_decrypt works on import
### BEGIN HIDDEN TESTS
assert ab.atbash_decrypt('SVOOL') == 'HELLO'
### END HIDDEN TESTS

### Q7 - `atbash_wrapper` (7.25 points)

Your module now has two functions (in `atbash.py`) and two accompanying test functions (in `test_atbash.py`). Let's add one final function and one final test function to complete the project.

Steps:
- Add a function `atbash_wrapper()` to `atbash.py` 
    - It should take two input parameters: `input_string` and `method`
    - Within the function:
        - if `method = 'encrypt'`, use `atbash_encrypt()` with `input_string` as the input to the function, returning, the output
        - if `method = 'decrypt'`, use `atbash_decrypt()` with `input_string` as the input to the function, returning the output
        - if `method` is anything other than these two specific strings, the function should `return` the string "Expecting method to be either 'encrypt' or 'decrypt'".  <- Just copy + paste the string to avoid typing issues :)
- Add a test function `test_atbash_wrapper()` to `test_atbash.py` to test the functionality of `atbash_wrapper()`
    - This test should contain at least three `asserts` and should pass silently
    - Update imports at the top of the file (if needed)

# After accomplishing tasks above, feel free to use this cell to check your work (optional)

# tests to ensure wrapper function works for decryption

### BEGIN HIDDEN TESTS
import atbash as ab
assert ab.atbash_wrapper('HELLO', 'decrypt') == 'SVOOL'
### END HIDDEN TESTS

# tests to ensure wrapper function works for encryption

### BEGIN HIDDEN TESTS
assert ab.atbash_wrapper('SVOOL', 'encrypt') == 'HELLO'
### END HIDDEN TESTS

# tests to ensure wrapper function works when method is anything other than encrypt or decrypt

### BEGIN HIDDEN TESTS
assert ab.atbash_wrapper('SVOOL', 'blargh') == "Expecting method to be either 'encrypt' or 'decrypt'"
### END HIDDEN TESTS

# tests to ensure test functions pass silently
# uses pytest

### BEGIN HIDDEN TESTS
out = !pytest test_atbash.py
assert out.grep("ERRORS") == []
assert out.grep("FAILED") == []
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading code style and documentation of `atbash_encrypt` in `atbash.py`.)


=== BEGIN MARK SCHEME ===

partial credit for `atbash_encrypt` in `atbash.py`:   
- has numpy-style docstring & comments (**0.75 points**)
- uses good naming/API + Code Style (**0.75 points**)

=== END MARK SCHEME ===

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading code style and documentation of `atbash_decrypt` in `atbash.py`, from Q5.)


=== BEGIN MARK SCHEME ===

`atbash_decrypt` in `atbash.py` (partial credit from Q5)
- has numpy style docstring (**0.75 points**)
- has at least one good code comment; does not comment every line (**0.75 points**)
- has good Code Style (**0.75 points**)
    - some line spacing
    - spacing around operators
- has better naming (**0.75 points**) 
    - `l` is no longer `l` 
    - `alpha`/`reverse_alpha` are lowercase
    - `letter_index` uses snakecase

=== END MARK SCHEME ===

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading tests and imports in `test_atbash.py`)


=== BEGIN MARK SCHEME ===

partial credit for `test_atbash.py`:
- contains `test_atbash_encrypt` & `test_wrapper` (**1 point**)
- all 3 functions inported at top correctly (**0.5 points**)
- agreement between import at top and how used in tests (**0.5 points**)

=== END MARK SCHEME ===

## Part 4: True/False (1.5 points)

### Q8 - True/False (1.5 points)

Following the instructions & example above, store the appropriate boolean in the variable provided for each of the following statements:

- `function_names` | `basketball_game` is a better function name than `BasketballGame`
- `pwd` | `pwd` is a shell command that prints your current working directory
- `cd` | `cd` is a shell command that lists the files in your current working directory
- `relative_paths` | relative paths specify location relative to the computer's root directory
- `script` | To execute a script `my_script.py` from a Jupyter Notebook in the same directory, the cell would contain `!python my_script.py`
- `module` | To import a module `my_module.py` from a Jupyter Notebook in the same directory, the cell would contain `import my_module.py`

### BEGIN SOLUTION
function_names = True
pwd = True
cd = False
relative_paths = False
script = True
module = False
### END SOLUTION

assert function_names is not None

### BEGIN HIDDEN TESTS
assert function_names
### END HIDDEN TESTS

assert pwd is not None

### BEGIN HIDDEN TESTS
assert pwd
### END HIDDEN TESTS

assert cd is not None

### BEGIN HIDDEN TESTS
assert not cd
### END HIDDEN TESTS

assert relative_paths is not None

### BEGIN HIDDEN TESTS
assert not relative_paths
### END HIDDEN TESTS

assert script is not None

### BEGIN HIDDEN TESTS
assert script
### END HIDDEN TESTS

assert module is not None

### BEGIN HIDDEN TESTS
assert not module
### END HIDDEN TESTS

### Practice Final Exam complete!

Good work - you're done with the final exam!

Check your work, and then when you're ready, **submit on datahub**.

We will not have your exam until you click submit and see this show up under 'submitted assignments'.

### contents of atbash.py

```python
def atbash_decrypt(crypto):     
    """Decrypt Message using atbash method, returning reverse alphabetical position. 
    
    Parameters
    ----------
    crypto : string
        The string to be decrypted.
    
    Returns
    -------
    message : string
        The atbash decrypted message. 
    """
    
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reverse_alpha = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
    message = ''
    crypto = crypto.upper()
   
    for char in crypto:
        # if char in crypto is found, 
        # return indexed letters from reverse alpha
        if char in reverse_alpha:
            letter_index = reverse_alpha.find(char)
            message = message + alpha[letter_index]
        else: message = message + char
        
    return message


def atbash_encrypt(input_string):
    """Reverse alphabetical position of letters within a string. 
    
    Parameters
    ----------
    input_string : string
        string to be encrypthed
        
    Returns
    -------
    answer : string
        The encrypted string, storing the reverse alphabetical position of input string. 
    """
   
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reverse_alpha = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
    output_string = ''
    
    for char in input_string:
        char = char.upper()  # covert to upper case
    
        if char.isalpha():
            index = alpha.index(char)  # get position
            output_string += reverse_alpha[index]
        else:
            output_string += char
        
    return output_string


        
def atbash_wrapper(input_string, method):
    """Reverse alphabetical position of letters within a string. 
    
    Parameters
    ----------
    input_string : string
        string to be encrypted or decrypted
    method: string
        The method to use ("encrypt" or "decrypt")
        
    Returns
    -------
    ouput : string
        The string, either encrypted or decrypted as indicated by method. 
    """
           
    if method == 'encrypt':
        output = atbash_encrypt(input_string)
    elif method == 'decrypt':
        output = atbash_decrypt(input_string)
    else:
        output = "Expecting method to be either 'encrypt' or 'decrypt'"
    
    return output
```

### contents of test_atbash.py

Note: Your specific tests could differ

```python
from atbash import atbash_decrypt, atbash_encrypt, atbash_wrapper

def test_atbash_decrypt():

    assert callable(atbash_decrypt)
    assert isinstance(atbash_decrypt("HMVZPB KBGSLM HMZPV"), str)
    assert atbash_decrypt("HMVZPB KBGSLM HMZPV") == "SNEAKY PYTHON SNAKE"

def test_atbash_encrypt():
    
    assert callable(atbash_encrypt)
    assert isinstance(atbash_encrypt("VCZN"), str)
    assert atbash_decrypt("VCZN") == "EXAM"
    
    
def test_atbash_wrapper():
    
    assert callable(atbash_wrapper)
    assert atbash_wrapper("HMVZPB KBGSLM HMZPV", "decrypt") == "SNEAKY PYTHON SNAKE"
    assert atbash_wrapper("SNEAKY PYTHON SNAKE", "encrypt") == "HMVZPB KBGSLM HMZPV"
    
```