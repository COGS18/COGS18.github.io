**Course Announcements**

**Due Dates**
- A2 due Monday (4/19), may be submitted by Thursday (4/22) without penalty - no submissions after Thursday  
- CL4 due next Wednesday
- E1 is next Friday 

**Notes**
- CL2 Scores have been posted
- CL3 Answer key on website (All CL answer keys can be found on [the course website](https://cogs18.github.io/intro.html))

**Common Question**

Q: When you say "first element" or "first item" in the list...what do you mean?  
A: I mean the first thing in the list, which is in the zeroth index. What I mean will be made *very* clear on the wording on any exams.

# 'first item' is the first item/element here
# 'second element' is the 2nd item/element here
my_list['first item', 'second element']

Q: How do we know when to use a `for` loop and when to use a `while` loop?  
A: A `for` loop runs for a set number of times (iterations). A `while` loop would be used if you aren't sure how long it will take for your condition to be met or you want to run while/until your condition becomes true.

Q: Are `for` loops and `while` loops the only types of loops we will cover?  
A: Yes.  

Q: Help! I'm confused about stepping through the loop!  
A: You're not alone - this is the most difficult concept we've discussed so far. We'll do more examples in class. And, CL3 should help! If that doesn't, two suggestions: 1) ask to step through a loop together in anyone's office hours and 2) "talk" to yourself (like, out loud) and explain what happens each time through the loop

Q: What's the difference between `range` and indexing? Are they the same?  
A: They are different. `range` is used to create a series of values that can be used in a loop (an index variable). Indexing usually refers to using brackets to access elements of a collection (like a list, tuple, or string).

Q: What values can go in `range`? Can we use floats?  
A: Integers only! Floats will give you a TypeError (i.e. `range(0.3, 5.6)`).


# Encodings & Dictionaries

- symbols & representations
- Encodings
- Dictionaries
- `ord` & `chr`

What is a human representaion? human encoding? 

How do computers encode information?

## Symbols

<div class="alert alert-success">
Symbols are characters (or 'signs') of arbitrary shape, that can refer to (or represent) something. 
</div>

##  Representation

<div class="alert alert-success">
To represent means to stand in for something.
</div>

- **iconic representation** : the object looks like the thing it represents (i.e. a picture)
- **symbolic representation** : the symbol does *not* look like the thing it represents (i.e. letters, numbers) 


### Symbol Examples : concepts

- The symbol `2` represents the concept of `two-ness`. 
    - This is arbitrary: there is nothing 'two-like' about `2`
    - We need not use this symbol. The symbol `II` also represent `two-ness`.
    - `2` and `II` are two different representations for the concept of two.
- The symbol `b`, in english represents the sound `buh` (sort of). 
    - There is nothing 'buh' like about the symbol `b`

### Symbol Examples : rules

Given the symbol `2`, or `b` we have systematic rules of things we can do with them. 
- We can take `2` and add `1` and get a new symbol which represents the concept of `the value one bigger than two`
- We can concatenate some, but not all, other letters (symbols) to `b` to start making rules
- These rules are agnostic to what `2` or `b` represent, they are simply manipulations we can do with these symbols

## Digital Computers

Computers don't care about what the symbols look like. They don't care what symbols you use.

But, once a rule is established for a certain symbol, the computer will always follow that rule. 

<div class="alert alert-success">
Computation is symbol manipulation - using formal rules to manipulate symbols. 
</div>

Whenever we have symbols, and rules to manipulate them, we can do computation. 

When we use these symbols that represent meaningful things, we can use computers to make meaningful inferences.

Everything you think of as a computer (laptop, cell phone, etc.) works as a digital computer.

##  Encoding & Decoding

<div class="alert alert-success">
Encoding can be thought of as the process of 'changing representation', and decoding as the process of changing it back. 
</div>

Changing back and forth between using the symbol '2' and 'II' to represent the concept of two is an example of "changing representation."

## Aside: Binary

Fundamentally, digital computers can represent two states. Because of this, we say computers are / use binary. 

From binary, we can build up to store other things, that reduce down to binary representations.

We can then encode any value we would like to represent on our computer.  

### Binary in Code

## The `bin` operator returns the binary representation of an integer
# encoding an integer
print(bin(1))

print(bin(78))

#possible to encode Booleans in binary
#encoding a boolean
bin(False)

print(bool(0b0))

# We can also convert binary back to integers with 
# decoding from binary
int(0b1011)

## Character Encodings

Character encodings are a set of rules of how to represent a broad range of characters (symbols) in computers. 

We already have a way to represent numbers in binary.  

Using numbers, we can build a general procedure to encode characters as numbers.

We then have a way to represent characters, that we can reduce all the way to binary, that we can use that on computers.

## Example: Character Encoding

As a simple example, let's assign a number to a series of characters we want to be able to represent. 

Every time we see that number, we can evaluate it to replace it with the character it represents. 

### Character Encoding in Code

# Set the value we want to encode
character_encoding = 0

# Use conditional to interpret the character as a particular symbol
if character_encoding == 0:
    print('ñ')
elif character_encoding == 1:
    print('é')
elif character_encoding == 2:
    print('¿')

## Dictionaries


<div class="alert alert-success">
A dictionary is mutable collection of items, that can be of mixed-type, that are stored as key-value pairs.
</div>

### Dictionaries as Key-Value Collections

# Create a dictionary
dictionary = {'key_1' : 'value_1', 'key_2' : 'value_2'}

# Check the contents of the dictionary
print(dictionary)

# Check the type of the dictionary
type(dictionary)

# Dictionaries also have a length
# length refers to how many pairs there are
len(dictionary)

### Dictionaries: Indexing & Looping

# Dictionaries are indexed using their keys
dictionary['key_1']

# Loop over a dictionary loops across the keys
#   Inside the loop, you can use the key to access the associated value
for item in dictionary:
    print('Loop Iteration')
    print('\tKey:\t', item)
    print('\tValue:\t', dictionary[item])

# another approach that you will find if you Google
for key, val in dictionary.items():
    print('Loop Iteration')
    print('\tKey:\t', key)
    print('\tValue:\t', val)

#### Poll Question #1

Which of the following would create a dictionary of length 3?

- A) `{'Student_1' : 97, 'Student_2'}`
- B) `{'Student_1', 'Student_2', 'Student_3'}`
- C) `['Student_1' : 97, 'Student_2': 88, 'Student_3' : 91]`
- D) `{'Student_1' : 97, 'Student_2': 88, 'Student_3' : 91}`
- E) `('Student_1' : 97, 'Student_2': 88, 'Student_3' : 91)`


#### Poll Question #2

Fill in the '---' in the code below to return the value stored in the second key.

height_dict = {'height_1' : 60, 'height_2': 68, 'height_3' : 65, 'height_4' : 72}
height_dict[---]

- A) I did it
- B) I think I did it...
- C) I tried and am stuck
- D) No clue where to start...

### Example Dictionaries

student_emails = {
    'Betty Jennings' : 'bjennings@eniac.org',
    'Ada Lovelace' : 'ada@analyticengine.com',
    'Alan Turing' : 'aturing@thebomb.gov',
    'Grace Hopper' : 'ghopper@navy.usa'
}

student_emails

completed_coding_lab = {
    'A1234' : True,
    'A5678' : False,
    'A9123' : True
}

completed_coding_lab

mixed_types = {
    True  : [1, 2, 3],  
    False : None
}

mixed_types

#### Poll Question #3

Write the code that would create a dictionary `car` that stores values about your dream car's `make`, `model`, and `year`.

- A) I did it
- B) I think I did it...
- C) I tried and am stuck
- D) No clue where to start...

# YOUR CODE HERE

### Dictionaries are mutable

This means that dictionaries, once created, values *can* be updated.

# remember what dictionary we created above
completed_coding_lab

# change value of specified key
completed_coding_lab['A5678'] = True
completed_coding_lab

Because dictionaries are mutable, key-value pairs can also be removed from the dictionary using `del`.

print(completed_coding_lab)
len(completed_coding_lab)

## remove key-value pair using del
del completed_coding_lab['A5678']

print(completed_coding_lab)
len(completed_coding_lab)

### Dictionaries and operators

The operators we've discussed previously can be used when working with dictionaries.

To determine if a specified key is present in a dictionary we can use the `in` operator:

if 'A1234' in completed_coding_lab:
    print('Yes, that student is in this class')

### Additional Dictionary Properties

- Only one value per key. No duplicate keys allowed. 
    - If duplicate keys specified during assignment, the last assignment wins.

# Last duplicate key assigned wins
{'Student' : 97, 'Student': 88, 'Student' : 91}

- **keys** must be of an immutable type (string, tuple, integer, float, etc)
- Note: **values** can be of any type

# lists are not allowed as key types
# this code will produce an error
{['Student'] : 97}

- Dictionary keys are case sensitive.


{'Student' : 97, 'student': 88, 'STUDENT' : 91}

#### Poll Question #4

Why does the following code produce an error?

student_emails = {
    'Betty Jennings' : 'bjennings@eniac.org',
    'Ada Lovelace' : ['ada@analyticengine.com'],
    'Ada Lovelace' : 'aturing@thebomb.gov',
    ['Grace Hopper'] : 'ghopper@navy.usa'
}

- A) duplicate keys
- B) mutable key specified
- C) keys are case sensitive 
- D) mutable value specified 
- E) ¯\\\_(ツ)\_/¯

## Character Encodings with Dictionaries

# Define some character encodings
character_encodings = {
    0 : 'ñ',
    1 : 'é',
}

# Use character encodings to use symbols we want - example 1
my_sentence = 'no hablo espa' + character_encodings[0] + 'ol'
print(my_sentence)

# Use character encodings to use symbols we want - example 2
my_sentence = 'yo hablo ingl' + character_encodings[1] + 's'
print(my_sentence)

## Unicode

<div class="alert alert-success">
Unicode is a system of systematically and consistently representing characters. 
</div>

Every character has a unicode `code point` - an integer that can be used to represent that character. 

If a computer is using unicode, it displays a requested character by following the unicode encodings of which `code point` refers to which character. 

### ORD & CHR

<div class="alert alert-success">
<code>ord</code> returns the unicode code point for a one-character string.
</div>

<div class="alert alert-success"> 
<code>chr</code> returns the character encoding of a code point. 
</div>

### ord & chr examples

print(ord('a'))

print(chr(97))

### Inverses

`ord` and `chr` are inverses of one another. 

inp = 'b'
out = chr(ord(inp))

assert inp == out
print('Input: \t', inp, '\nOutput: ', out)