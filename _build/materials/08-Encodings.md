---
download_link: assets/downloads/materials/08-Encodings.ipynb.zip
pdf_link: assets/pdf/08-Encodings.pdf
layout: materials
title: '08-Encodings'
prev_page:
  url: /materials/07-Loops
  title: '07-Loops'
next_page:
  url: /materials/09-FunctionsI
  title: '09-FunctionsI'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Encodings

## Clicker Question #1

What is a symbol?

- A) A character that can be typed on a computer
- B) Something that can stand in the place of something else
- C) Something that looks like something else
- D) A character or sign used to represent something arbitrary
- E) I have no idea

## Symbols

<div class="alert alert-success">
Symbols are characters (or 'signs') of arbitrary shape, that can refer to (or represent) something. 
</div>

##  Representation

<div class="alert alert-success">
To represent means to stand in for something.
</div>

### Symbol Examples - 1

- The symbol `2` represents the concept of `two-ness`. 
    - This is arbitrary: there is nothing 'two-like' about `2`
    - We need not use this symbol. The symbol `II` also represent `two-ness`.
    - `2` and `II` are two different representations for the concept of two.
- The symbol `b`, in english represents the sound `buh` (sort of). 
    - There is nothing 'buh' like about the symbol `b`

### Symbol Examples - 2

Given the symbol `2`, or `b` we have systematic rules of things we can do with them. 
- We can take `2` and add `1` and get a new symbol which represents the concept of `the value one bigger than two`
- We can concatenate some, but not all, other letters (symbols) to `b` to start making rules
- These rules are agnostic to what `2` or `b` represent, they are simply manipulations we can do with these symbols

## Digital Computers

<div class="alert alert-success">
Computation is symbol manipulation - using formal rules to manipulate symbols. 
</div>

Whenever we have symbols, and rules to manipulate them, we can do computation. 

When we use these symbols that represent meaningful things, we can use computers to make meaningful inferenes.

##  Encoding & Decoding

<div class="alert alert-success">
Encoding can be throught of as the process of 'changing representation', and decoding as the process of changing it back. 
</div>

## Aside: Binary

Fundamentally, digital computers can represent two states. Because of this, we say computers are / use binary. 

From binary, we can build up to store other things, that reduce down to binary representations.

We can then encode any value we would like to represent on our computer.  

### Binary in Code



{:.input_area}
```python
# The `bin` operator returns the binary representation of an integer
print(bin(1))

print(bin(11))
```


{:.output_stream}
```
0b1
0b1011

```



{:.input_area}
```python
# We can also convert binary back to integers with 
int(0b1011)
```





{:.output_data_text}
```
11
```



## Character Encodings

Character encodings are a set of rules of how to represent a broad range of characters (symbols) in computers. 

We already have a way to represent numbers in binary.  

Using numbers, we can build a general procedure to encode characters as numbers.

We then have a way to represent characters, that we can reduce all the way to binary, that we can use that on computers.

## Example: Character Encoding

As a simple example, let's assign a number to a series of characters we want to be able to represent. 

Every time we see that number, we can evaluate it to replace it with the character it represents. 

### Character Encoding in Code



{:.input_area}
```python
# Set the value we
character_encoding = 0

# Use conditional to interpret the character as a particular symbol
if character_encoding == 0:
    print('ñ')
elif character_encoding == 1:
    print('é')
elif character_encoding == 2:
    print('¿')
```


{:.output_stream}
```
ñ

```

## Aside: Dictionaries


<div class="alert alert-success">
A dictionary is mutable collection of items, that can be of mixed-type, that are stored as key-value pairs. 
</div>

### Dictionaries as Key-Value Collections



{:.input_area}
```python
# Create a dictionary
dictionary = {'name_1' : 'value_1', 'name_2' : 'value_2'}
```




{:.input_area}
```python
# Check the contents of the dictionary
print(dictionary)
```


{:.output_stream}
```
{'name_1': 'value_1', 'name_2': 'value_2'}

```



{:.input_area}
```python
# Check the type of the dictionary
type(dictionary)
```





{:.output_data_text}
```
dict
```





{:.input_area}
```python
# Dictionaries also have a length
len(dictionary)
```





{:.output_data_text}
```
2
```



### Dictionaries: Indexing & Looping



{:.input_area}
```python
# Dictionaries are indexed using their keys
dictionary['name_1']
```





{:.output_data_text}
```
'value_1'
```





{:.input_area}
```python
# Loop over a dictionary loops across the keys
#   Inside the loop, you can use the key to access the associated value
for item in dictionary:
    print('Loop Iteration')
    print('\tKey:\t', item)
    print('\tValue:\t', dictionary[item])
```


{:.output_stream}
```
Loop Iteration
	Key:	 name_1
	Value:	 value_1
Loop Iteration
	Key:	 name_2
	Value:	 value_2

```

### Example Dictionaries



{:.input_area}
```python
student_emails = {
    'Betty Jennings' : 'bjennings@eniac.org',
    'Ada Lovelace': 'ada@analyticengine.com',
    'Alan Turing' : 'aturing@thebomb.gov',
    'Grace Hopper' : 'ghopper@navy.usa'
}
```




{:.input_area}
```python
completed_coding_lab = {
    'A1234' : True,
    'A5678' : False,
    'A9123' : True
}
```




{:.input_area}
```python
mixed_types = {
    True  : [1, 2, 3], 
    False : None
}
```


## Clicker Question #2

What will the value of result be after this code has run?

```
dictionary = {'alpha' : [8, 12], 'beta'  : [13, 30], 'theta' : [4, 8]}

check = 10
for item in dictionary:
    temp = dictionary[item]
    if temp[0] >= check <= temp[1]:
        result = item
```

A) alpha | B) [8, 12] | C) beta | D) theta | E) None

### Clicker Question Answer



{:.input_area}
```python
dictionary = {'alpha' : [8, 12], 'beta'  : [13, 30], 'theta' : [4, 8]}

check = 10
for item in dictionary:

    temp = dictionary[item]

    if temp[0] <= check <= temp[1]:
        result = item

print(result)
```


{:.output_stream}
```
alpha

```

## Character Encodings with Dictionaries



{:.input_area}
```python
# Define some character encodings
character_encodings = {
    0 : 'ñ',
    1 : 'é',
}
```




{:.input_area}
```python
# Use character encodings to use symbols we want - example 1
my_sentence = 'no hablo espa' + character_encodings[0] + 'ol'
print(my_sentence)
```


{:.output_stream}
```
no hablo español

```



{:.input_area}
```python
# Use character encodings to use symbols we want - example 1
my_sentence = 'yo hablo ingl' + character_encodings[1] + 's'
print(my_sentence)
```


{:.output_stream}
```
yo hablo inglés

```

## Unicode

<div class="alert alert-success">
Unicode is a system of systematically and consistently representing characters. 
</div>

Every character has a unicode `code point` - an integer that can be used to represent that number. 

If a computer is using unicode, it display a requested character by following the unicode encodings of which `code point` refers to which character. 

### ORD & CHR

<div class="alert alert-success">
`ord` returns the unicode code point for a one-character string. `chr` represent the character encoding of a code point. 
</div>

### ord & chr examples



{:.input_area}
```python
print(ord('a'))

print(chr(97))
```


{:.output_stream}
```
97
a

```

### Inverses

`ord` and `chr` are inverses of one another. 



{:.input_area}
```python
inp = 'b'
out = chr(ord(inp))

assert inp == out
print('Input: \t', inp, '\nOutput: ', out)
```


{:.output_stream}
```
Input: 	 b 
Output:  b

```
