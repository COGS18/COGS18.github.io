**Course Announcements**

Due Dates:
- A5 due Monday (5/31)
- Final Project/Exam (Fri 6/11 at 11:59 PM)
    - Exam: will have >= 48h to complete
    
Notes:
- Please fill out your CAPEs (+1% if >=85% response rate)
- No lecture/OH on Monday (Memorial Day)
- No OH for staff during Finals Week (Prof Ellis will have some; details TBD)

**Q&A**

Q: what does a `list(input_string)` do?  
A: This "typecasts" `input_string` (a string) to be a list. Typecasting specifies the type the variable should be. Here it's converting/typecasting a string to a list. To see an example of what this means, try `list('hello')`. 

Q: What's the difference between documentation and pseudocode?  
A: Psuedocode is for you as you're trying to plan/think through your code. It isn't meant for or to be read by others. Docstrings are for users of your code to know how to use your code. Comments in your code are for people who may be reading your code and want to understand your thinking. Sometimes pseudocode comments can be helpful comments, but other times, it's best to delete your pseudocode if it doesn't guide a reader's understanding.

Q: What resources can we use to make sure we follow good documentation and code style?  
A: [PEP8](https://www.python.org/dev/peps/pep-0008/) for code style; [numpy docstrings documentation](https://numpydoc.readthedocs.io/en/latest/format.html) for docstrings

Q: Are numpy docstring the only type of docstrings? if not, why would we choose numpy docstring style over the others?  
A: Nope - there are others. We choose this style b/c 1) it's popular and used by many and 2) it integrates well with a lot of documentation tools. Feel free to google sphinx to see what I mean! 

Q: Do we need to write an explanation for each line of code that we write?  
A: No. You should avoid this. This would make your code *less* readable.

Q: Why is documentation an important thing to incorporate in your code?  
A: It's the best way to communicate to others how to use your code. If, during CL8 or A5 you've googled how to use a function/method from `pandas`/`numpy`, you've benefitted from someone writing documentation!

Q: "When I ran `!pip show lisc` in my datahub, it said that ""WARNING: Package(s) not found: lisc""
Why is this happened? (this is the last line of code in today's notebook)"  
A: You would have to install this first:  `pip install --user lisc` first.

Q: When are major updates needed? Why isn't it always minor?  
A: B/c sometimes you re-think your approach and update/change your code base. A major change is then needed. Feel free to look up differences between Python 2 and Python 3 - so many changes...for the better!

Q: If there are multiple docstrings in a notebook, how are they specified and accessed through the '__doc__'  attribute?  
A: The attribute is attached to the object, so what comes before `__doc__` will specify which docstring you want to pull up.

Q: How to read the documentation of some packages, they still can be really confusing at times and I usually prefer looking at examples/tutorials rather than reading the documentation.  
A: That's OK! Examples/tutorials are a great place to start. I'd suggest doing the example/tutorial first and then look back at the documentation. Reading documentation is a skill, but a handy/helpful one, so I encourage you to look at the documentation after the example, once you have a sense of what it's doing to practice/hone this skill.

Q: Are docstrings automatically stored in `__doc__` through the double quotation marks?  
A: Yup!

Q: Where to put docstrings. I have a class with methods for my final project. I know I'd put a docstring under the class but do I have to put one for each of my methods as well?  
A: Yup - ideally each method would have one. Now, if your methods only included `print()` statements, you could omit the docstrings there, but if they're carrying out operations, best to document. We'll be looking to see you have at least 3 docstrings in your project.

# Code Projects

- modular design
- minimal viable product
- test-driven development
- rapid prototyping
- project organization
- refactoring
- code review

## Project Check-In


### Modular Design

<div class="alert alert-success">
Modular design, like modular programming, is the approach of designing and building things as independent modules. 
</div>

### Minimal Viable Product

<div class="alert alert-success">
A 'minimal viable product' is a product that contains the minimum amount of implemented features to use the code product - no more, no less.</div>

### Test-Driven Development

<div class="alert alert-success">
Writing the tests as soon as you have a plan & before you've written the code.
</div>

### Rapid Prototyping

<div class="alert alert-success">
Rapid prototyping is an approach for developing things in which you work on minimal prototypes and iterate on them quickly. 
</div>

#### Some examples

- Chatbot: start and end a chat
- Data Analysis: read a dataset in, make a basic plot
- Car Inventory: object with method that adds a car to the Inventory
- Artificial Agents: simple bot moves around randomly

## Project Organization

- **Notebooks**: good for interactive development
    - For when seeing the inputs and outputs of code running needs to be seen start to finish
    - file ends in `.ipynb`
- **Modules**: for storing mature Python code, that you can import
    - you don't *use* the functions in there, just define them
    - file ends in `.py`
- **Scripts**: a Python file for executing a particular task
    - this takes an input and does something start to finish
    - file ends in `.py`

### Project Workflow

Typical project workflow:

- Develop plan and write tests
- Develop code interactively in a Jupyter notebook/text editor
- As functions & classes become mature, move them to Python files that you then `import`
    - As you do so, go back through them to check for code style, add documentation, and run your code tests
- At the end of a project, (maybe) write a standalone script that runs the project

#### Project Notes

1. Design and write tests
2. Write some code
2. Test to make sure it works
3. Check code style (naming, spacing, etc.)
4. Add documentation
5. Move to module (if necessary)
6. Run all tests

### Project Design

- Idea: atbash encryption: return the capitalized, reverse alphabetical letter for each character in the input string

- Design:
    - `atbash_encrypt()` : take input string and return atbash encrypted string
        - inputs: `input_string` 
        - returns: `atbash_string`
    - `atbash_decrypt()` : take encrypted string and decrypt using atbash
        - inputs: `atbash_string`
        - returns: `decrypted_string`
    - `atbash_wrapper()` : does either of the above, as specified with input parameter
        - inputs: `input_string`, `method` (either 'encrypt' or 'decrypt', default: 'encrypt')
        - returns `output_string`

### Adding Unit Tests

def test_atbash_encrypt():
    assert callable(atbash_encrypt)
    assert isinstance(atbash_encrypt('hello'), str)
    assert atbash_encrypt('HELLO') == 'SVOOL'
    assert atbash_encrypt('hello') == 'SVOOL'
    
def test_atbash_decrypt():
    assert callable(atbash_decrypt)
    assert isinstance(atbash_decrypt('hello'), str)
    assert atbash_decrypt('SVOOL') == 'HELLO'
    assert atbash_decrypt('svool') == 'HELLO'

def test_atbash_wrapper():
    assert callable(atbash_wrapper)
    assert isinstance(atbash_wrapper('hello', method='encrypt'), str)
    assert atbash_wrapper('hello', method='encrypt') == 'SVOOL'
    assert atbash_wrapper('HELLO', method='encrypt') == 'SVOOL'
    assert atbash_wrapper('SVOOL', method='decrypt') == 'HELLO'
    assert atbash_wrapper('svool', method='decrypt') == 'HELLO'
    assert atbash_wrapper('svool', method='blargh') == "method should be either 'decrypt' or 'encrypt'"

...move to test file

...will uncomment as I write the code/functions

### Writing Code

#### `atbash_encrypt`

'hello'.find('e')

def atbash_encrypt(input_string):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reverse_alpha = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

    atbash_string = ''

    for char in input_string:
        char = char.upper()
        if char in alpha:
            position = alpha.find(char)
            atbash_string += reverse_alpha[position]
        else:
            atbash_string = None
            break
        
    return atbash_string

# smoke test
atbash_encrypt('!!!')

### Moving to a module...

- consider imports at the top

Note on `imports`: If you want to be able to use modules (imports) within a module/script, be sure to import it at the top. This applies to test files as well.

import atbash as ab

ab.atbash_encrypt('hello')

!pytest test_atbash.py

#### `atbash_decrypt`

# reminder: consider code style! 
def atbash_decrypt(atbash_string):    
    ALPHA='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    REVERSEALPHA='ZYXWVUTSRQPONMLKJIHGFEDCBA'
    atbash_string=atbash_string.upper()
    decrypted_string=''
    for l in atbash_string:
        if l in REVERSEALPHA:
            letterindex=REVERSEALPHA.find(l)
            decrypted_string=decrypted_string+ALPHA [letterindex]
        else: decrypted_string=decrypted_string+l
    return decrypted_string

# smoke test
atbash_decrypt('SVOOL')

!pytest test_atbash.py

#### `atbash_wrapper`

def atbash_wrapper(input_string, method='encrypt'):
    
    if method == 'encrypt':
        output_string = atbash_encrypt(input_string)
    elif method == 'decrypt':
        output_string = atbash_decrypt(input_string)
    else:
        output_string = "method should be either 'decrypt' or 'encrypt'"
    
    return output_string

# smoke test
atbash_wrapper('svool', method='aslfsdklj')

!pylint atbash.py

!pytest test_atbash.py

### Documentation

- Code in final project/exam requires:
    - numpy-style docstrings
    - code comments

### Putting it all together

from atbash import atbash_wrapper

# carry out atbash encryption by default
atbash_wrapper('hello')

# carry out atbash decryption
atbash_wrapper('svool', method='decrypt')

# gives appropriate response if incorrect method provided
atbash_wrapper('hello', method='blargh')

**atbash improvements**

import atbash as ab

ab.atbash_encrypt('hello')

ab.atbash_decrypt('hello')

### Refactoring

<div class="alert alert-success">
Refactoring is the process of restructuring existing computer code, without changing its external behaviour. 
</div>

Think of this as restructuring and final edits on your essay. 

**Nesting Functions** - If you have a whole bunch of functions, if statements, and for/while loops together within a single function, you probably want (need?) to refactor.

Clean functions accomplish a **single task**!

**DRY**: Don't Repeat Yourself

#### Refactoring Example: Chatbot

import random 

def have_a_chat():
    """Main function to run our chatbot."""
    
    chat = True

    while chat:

        # Get a message from the user
        msg = input('INPUT :\t')
        out_msg = None
        
        # Check if the input is a question
        input_string = msg
        if '?' in input_string:
            question = True
        else:
            question = False

        # Check for an end msg 
        if 'quit' in input_string:
            out_msg = 'Bye!'
            chat = False
            
        # If we don't have an output yet, but the input was a question, 
        # return msg related to it being a question
        if not out_msg and question:
            out_msg = "I'm too shy to answer questions. What do you want to talk about?"

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(['Good.', 'Okay', 'Huh?', 'Yeah!', 'Thanks!'])

        print('OUTPUT:', out_msg)

have_a_chat()

#### Refactored Example: Chatbot

What this function does:

1. takes an input
2. checks if input is a question
3. checks if input is supposed to end the chat
4. return appropriate response if question, end chat, or other

That's four different things! Functions should do a single thing...

def get_input():
    """ask user for an input message"""
    
    msg = input('INPUT :\t')
    out_msg = None
    
    return msg, out_msg

def is_question(input_string):
    """determine if input from user is a question"""
    
    if '?' in input_string:
        output = True
    else:
        output = False
    
    return output

def end_chat(input_list):
    """identify if user says 'quit' in input and end chat"""
    
    if 'quit' in input_list:
        output = 'Bye'
        chat = False
    else:
        output = None
        chat = True
        
    return output, chat

def return_message(out_msg, question):
    """generic responses for the chatbot to return"""
        
    # If we don't have an output yet, but the input was a question, 
    # return msg related to it being a question
    if not out_msg and question:
        out_msg = "I'm too shy to answer questions. What do you want to talk about?"

    # Catch-all to say something if msg not caught & processed so far
    if not out_msg:
        out_msg = random.choice(['Good.', 'Okay', 'Huh?', 'Yeah!', 'Thanks!'])
        
    return out_msg

def have_a_chat():
    """Main function to run our chatbot."""
    
    chat = True

    while chat:

        # Get input message from the user
        msg, out_msg = get_input()
        
        # Check if the input is a question
        question = is_question(msg)
         
        # Check for an end msg 
        out_msg, chat = end_chat(msg)
       
        # specify what to return
        out_msg = return_message(out_msg = out_msg, question = question)
        
        print('OUTPUT:', out_msg)

have_a_chat()  

## Code Review

<div class="alert alert-success">
Code reviews is a process for systematically reviewing someone else's code. 
</div>

This is what you'll have the chance to do in coding lab next week!