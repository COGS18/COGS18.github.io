---
interact_link: content/assignments/A2B-Answers.ipynb
download_link: assets/downloads/A2B-Answers.ipynb.zip
layout: notebooks
title: 'A2B-Answers'
prev_page:
  url: /assignments/A2-Ciphers
  title: 'A2-Ciphers'
next_page:
  url: /assignments/A3-Chatbots
  title: 'A3-Chatbots'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# A2-Ciphers

## Overview

This assignment covers Collections, Loops & Encodings, and builds up to the application of Ciphers. 

This assignment is out of 8 points, worth 8% of your grade.

Make sure your completed assignment passes all the asserts. This assignment also has hidden tests - which means that passing all the asserts you see does not guarantee that you have the correct answer! Make sure to double check and re-run your code to make sure it does what you expect, and that the variables you define end up with values you'd expect. 

Also note that some questions use a `%%writefile` line to help grade them. You don't have to do anything with these lines (you can basically ignore them), but just make sure you do not delete them! You must leave them in for your assignment to grade properly. 

## Part 1: Collection Types

This part covers collection types: lists, tuples and dictionaries. 

### Q1 - Lists (0.25 points)

Below are the results of a hypothetical experiment of measuring the height of a class in a land far away:

- Mario is 5.6 feet tall
- Sarai is 5.4 feet tall
- Demi is 6.2 feet tall
- Ian is 5.8 feet tall
- Dawn is 5.7 feet tall

Create a list, called `class_names` and fill it with the names of each person in the class. 

Create another list, called `class_heights` and fill it with the heights of each person in the class. 

Remember that the order of lists matters, and so make sure to keep the order of items the same as listed above!



{:.input_area}
```python
### BEGIN SOLUTION
class_names = ['Mario', 'Sarai', 'Demi', 'Ian', 'Dawn' ]
class_heights = [5.6, 5.4, 6.2, 5.8, 5.7]
### END SOLUTION
```




{:.input_area}
```python
# Tests for Q1

# Check both lists are defined
assert isinstance(class_names, list)
assert isinstance(class_heights, list)

# Check both lists have the same length, and are of length 5
assert len(class_names) == len(class_heights) == 5

### BEGIN HIDDEN TESTS
assert class_names == ['Mario', 'Sarai', 'Demi', 'Ian', 'Dawn' ]
assert class_heights == [5.6, 5.4, 6.2, 5.8, 5.7]
### END HIDDEN TESTS
```


Now that we have the data stored in lists, we will explore other collection types. 

### Q2 - Tuples (0.25 points)

Create a tuple, that contains just the names of the people in the experiment. Call this tuple 'names_tuple'. 



{:.input_area}
```python
### BEGIN SOLUTION
names_tuple = ('Mario', 'Sarai', 'Demi', 'Ian', 'Dawn' )
### END SOLUTION
```




{:.input_area}
```python
assert isinstance(names_tuple, tuple)

### BEGIN HIDDEN TESTS
assert names_tuple == ('Mario', 'Sarai', 'Demi', 'Ian', 'Dawn')
### END HIDDEN TESTS
```


### Q3 - Dictionaries (0.25 points)

Next, store the data into a dictionary, where each student's name is the key and their height is the value.

Call this dictionary `results_dictionary`. 



{:.input_area}
```python
### BEGIN SOLUTION
results_dictionary = {'Mario': 5.6, 'Sarai': 5.4, 'Demi': 6.2, 'Ian': 5.8, 'Dawn': 5.7 }
### END SOLUTION
```




{:.input_area}
```python
assert isinstance(results_dictionary, dict)

### BEGIN HIDDEN TESTS
assert results_dictionary == {'Mario': 5.6, 'Sarai': 5.4, 'Demi': 6.2, 'Ian': 5.8, 'Dawn': 5.7 }
### END HIDDEN TESTS
```


### Q4 - Lists of Lists (0.25 points)

You can also make lists, that are filled with lists! List-ception. 

First, create three different lists:
- A list called `string_list` that contains three strings (can be any strings)
- A list called `number_list` that contains three numbers (can be any numbers - int or float)
- A list called `boolean_list` that contains three boolean (can be any booleans)

Then, create a new list, called `nested_list` which contains the three lists you created above. 



{:.input_area}
```python
### BEGIN SOLUTION
string_list = ['a', 'b', 'c']
number_list = [12.4, 16.4, 11.2]
boolean_list = [True, False, True]
nested_list = [string_list, number_list, boolean_list]
### END SOLUTION
```




{:.input_area}
```python
assert isinstance(string_list, list)
assert len(string_list) == 3
assert isinstance(string_list[0], str)

assert isinstance(number_list, list)
assert len(number_list) == 3
assert isinstance(number_list[0], int) or isinstance(number_list[0], float)

assert isinstance(boolean_list, list)
assert len(boolean_list) == 3
assert isinstance(boolean_list[0], bool)
```




{:.input_area}
```python
assert isinstance(nested_list, list)
assert len(nested_list) == 3
assert isinstance(nested_list[0], list)
```


## Part 2: Working With Collections

This part covers working with collections and indexing.



{:.input_area}
```python
# For Q5 & Q6, the following lists are provided for you
list_1 = [10, 20, 40, 50]
list_2 = [13, 15, 17, 19, 22, 25]
list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
list_4 = [21, 9, 98, 289, 938]
```


### Q5 - Indexing (0.5 points)

Do the following using indexing:
- Store the first value in `list_1` to `index_1`
- Store the last value in `list_2` to `index_2`
- Store the first four values of `list_2` to `index_3`
- Store the last four values of `list_3` to `index_4` 



{:.input_area}
```python
### BEGIN SOLUTION
index_1 = list_1[0]
index_2 = list_2[-1]
index_3 = list_2[0:4]
index_4 = list_3[-4:]
### END SOLUTION
```




{:.input_area}
```python
assert isinstance(index_1, int)

### BEGIN HIDDEN TESTS
assert index_1 == 10
### END HIDDEN TESTS
```




{:.input_area}
```python
assert isinstance(index_2, int)

### BEGIN HIDDEN TESTS
assert index_2 == 25
### END HIDDEN TESTS
```




{:.input_area}
```python
assert isinstance(index_3, list)
assert len(index_3) == 4

### BEGIN HIDDEN TESTS
assert index_3 == [13, 15, 17, 19]
### END HIDDEN TESTS
```




{:.input_area}
```python
assert isinstance(index_4, list)
assert len(index_4) == 4

### BEGIN HIDDEN TESTS
assert index_4 == [8, 9, 10, 11]
### END HIDDEN TESTS
```


### Q6 - Comparisons using Indexing (0.5 points)

Do the following comparisons using indexing:
- Check if the first value of `list_1` is one of the last three values in `list_3` (Hint: remember operator 'in')
    - Store the result in `comp_result_1`
    
    
- Check if the third value of `list_4` is greater than the fourth value in `list_4`
    - Store the result in `comp_result_2`
    
    
- Check if the last value of `list_4` is less than the second value in `list_4`
    - Store the result in `comp_result_3`
    
    
- Check if the second value of `list_2` multiplied by the seventh value of `list_3` is greater than the second to last value in `list_4`
    - Store the result in `comp_result_4`
    
Keep in mind that you are storing the result of a comparison to a variable, so resulting variables should all be booleans. 



{:.input_area}
```python
### BEGIN SOLUTION
comp_result_1 = list_1[0] in list_3[-3:]
comp_result_2 = list_4[2] > list_4[3]
comp_result_3 = list_4[-1] < list_4[1]
comp_result_4 = (list_2[1]*list_3[6]) > list_4[-2]
### END SOLUTION
```




{:.input_area}
```python
assert isinstance(comp_result_1, bool)

### BEGIN HIDDEN TESTS
assert comp_result_1 == True
### END HIDDEN TESTS
```




{:.input_area}
```python
assert isinstance(comp_result_2, bool)

### BEGIN HIDDEN TESTS
assert comp_result_2 == False
### END HIDDEN TESTS
```




{:.input_area}
```python
assert isinstance(comp_result_3, bool)

### BEGIN HIDDEN TESTS
assert comp_result_3 == False
### END HIDDEN TESTS
```




{:.input_area}
```python
assert isinstance(comp_result_4, bool)

### BEGIN HIDDEN TESTS
assert comp_result_4 == False
### END HIDDEN TESTS
```


## Part 3: Loops

This part covers using loops. 

### Q7 - Loop Questions (0.5 points)

For each of the scenarios below, indicate whether it is a procedure best done with a for loop, a while loop, or if the task is not something best done with a loop. 

For each question, answer by setting a string to requested variable name, that stores one of 'for', 'while' or 'not_a_loop' to indicate your answer.

- a) You want to apply a transform to every piece of data in a list. 
    - Answer in a variable called `loop_q_a`
- b) You want to continuously update the position of a character displayed on a screen, as long as the status of the character is 'alive'.
    - Answer in a variable called `loop_q_b`
- c) You want to check three different value comparisons are all true together, each checking a different variable.
    - Answer in a variable called `loop_q_c`
- d) You want your computer to connect to an external network. As long as your connection status is False, you want to try and re-connect. 
    - Answer in a variable called `loop_q_d`



{:.input_area}
```python
### BEGIN SOLUTION
loop_q_a = 'for'
loop_q_b = 'while'
loop_q_c = 'not_a_loop'
loop_q_d = 'while'
### END SOLUTION
```




{:.input_area}
```python
assert loop_q_a in ['for', 'while', 'not_a_loop']

### BEGIN HIDDEN TESTS
assert loop_q_a == 'for'
### END HIDDEN TESTS
```




{:.input_area}
```python
assert loop_q_b in ['for', 'while', 'not_a_loop']

### BEGIN HIDDEN TESTS
assert loop_q_b == 'while'
### END HIDDEN TESTS
```




{:.input_area}
```python
assert loop_q_c in ['for', 'while', 'not_a_loop']

### BEGIN HIDDEN TESTS
assert loop_q_c == 'not_a_loop'
### END HIDDEN TESTS
```




{:.input_area}
```python
assert loop_q_d in ['for', 'while', 'not_a_loop']

### BEGIN HIDDEN TESTS
assert loop_q_d == 'while'
### END HIDDEN TESTS
```


### Q8 - For Loop (0.5 points)

What is the sum of all even numbers between 19 and 35?

Answer this question using a for loop, and using `range`. 

Save the result out to a variable called `sum_result`. 



{:.input_area}
```python
### BEGIN SOLUTION
sum_result = 0
for number in range(20, 35, 2):
    sum_result = sum_result + number
### END SOLUTION
```




{:.input_area}
```python
assert isinstance(sum_result, int)

### BEGIN HIDDEN TESTS
assert sum_result == 216
### END HIDDEN TESTS
```


### Q9 - While Loop (0.5 points)

Write a while loop that adds the first 100 numbers (from 1 to 100) together.

To do so, use a while loop that continues while the condition of `cur_num` being less than or equal to `stop_num` is `True`. 

Inside the loop, it should add `cur_num` to the running `total` variable, and also add 1 to `cur_num`. 

Make sure to check at the end that the value of `total` reflects the total summation. 



{:.input_area}
```python
# These variables provided for you - use them in your solution
total = 0
cur_num = 1
stop_num = 100

### BEGIN SOLUTION
while cur_num <= stop_num:
    total = total + cur_num
    cur_num = cur_num + 1
### END SOLUTION
```




{:.input_area}
```python
assert isinstance(cur_num, int)
assert isinstance(total, int)

# This will check that the `cur_num` increment variable ended at the right value
assert cur_num == 101

### BEGIN HIDDEN TESTS
assert total == 5050
### END HIDDEN TESTS
```


### Example: Append

In the following examples we will need to use an operation to add something to a list. Some examples for doing so are provided. 

Given a list, `my_list` to add an item `my_item` to the end of the list, you can do `my_list.append(my_item)`. 



{:.input_area}
```python
# Example of appending to a list
my_list = ['a', 12, None]

print('Before Append: ', my_list)

my_list.append(True)

print('After  Append: ', my_list)
```


{:.output_stream}
```
Before Append:  ['a', 12, None]
After  Append:  ['a', 12, None, True]

```



{:.input_area}
```python
# Example of using append with loops
list_of_values = [0, 1, 2, 3]

# Initialize an empty list that will be used to store outputs
outputs = []

# Loop through all items in `list_of_items`
for item in list_of_values:
    
    # Add incremented item to the list of outputs
    outputs.append(item + 1)

# Check what outputs ends up as
print(outputs)
```


{:.output_stream}
```
[1, 2, 3, 4]

```

### Q10 - Loops: Multiplication (0.5 points)

Using the provided variable `num_list`, write a for loop to loop across each value, multiplying it by -1. 

Store the result for each value, in a list called `eval_1`, by defining `eval_1` before the loop, and using `append` inside the loop. 



{:.input_area}
```python
# This creates a list of all numbers from 1-12, inclusive
num_list = list(range(1, 13))
```




{:.input_area}
```python
### BEGIN SOLUTION
eval_1 = []
for item in num_list:
    eval_1.append(item * -1)
### END SOLUTION
```




{:.input_area}
```python
assert isinstance(eval_1, list)
assert isinstance(eval_1[0], int)

### BEGIN HIDDEN TESTS
assert eval_1 == list(reversed(range(-12, -0)))
### END HIDDEN TESTS
```


## Part 4: Combining Loops & Conditionals

This part covers integrating collections and loops with conditional and operators. 



{:.input_area}
```python
# This list provided to use for the following questions
data_list = [-1, 20, -100, -40, 33, 97, -101, 45, -79, 96]
```


### Q11 - Loops: Division (0.5 points)

Write some code that uses a loop to find all the values from `data_list` that are perfectly divisible by 3. 

Use a for loop with a conditional to do this, and save any values from `data_list` that meet this condition into a new list called `div_3`. 



{:.input_area}
```python
### BEGIN SOLUTION
div_3 = []
for number in data_list:
    if number % 3 == 0:
        div_3.append(number)
### END SOLUTION
```




{:.input_area}
```python
assert isinstance(div_3, list)
assert(len(div_3) == 3)

### BEGIN HIDDEN TESTS
assert div_3 == [33, 45, 96]
### END HIDDEN TESTS
```


### Q12 - Loops: Odd or Even (0.5 points)

Write a for loop that is going to check whether the values in `data_list` are even or odd. 

Use a for loop with a conditional to do this. 

For each value, it should add `True` to a new list `is_even` if the value is even, and `False` to `is_even` if the value is odd. 



{:.input_area}
```python
### BEGIN SOLUTION
is_even = []
for item in data_list:
    if item%2 == 0:
        is_even.append(True)
    else:
        is_even.append(False)
### END SOLUTION
```




{:.input_area}
```python
assert isinstance(is_even, list)
assert(len(is_even) == len(data_list))

### BEGIN HIDDEN TESTS
assert sum(is_even) == 4
### END HIDDEN TESTS
```


### Q13 - Loops: Multiple Conditions (0.5 points)

Write a for loop that will check each value in `data_list` to see if they are even or odd and whether they are positive or negative.
- If they are both positive and even, encode this as the number 1
- If they are both negative and odd, encode this as the number -1
- Otherwise, encode this as the number 0

- Store the result for each value into a list called `num_type`



{:.input_area}
```python
### BEGIN SOLUTION
num_type = []
for item in data_list:
    if item%2 == 0 and item > 0:
        num_type.append(1)
    elif item%2 != 0 and item < 0:
        num_type.append(-1)
    else:
        num_type.append(0)
### END SOLUTION
```




{:.input_area}
```python
assert isinstance(num_type, list)
assert(len(num_type) == len(data_list))

### BEGIN HIDDEN TESTS
assert sum([1 for it in num_type if it == 1 ]) == 2
assert sum([1 for it in num_type if it == -1 ]) == 3
assert sum([1 for it in num_type if it == 0 ]) == 5
### END HIDDEN TESTS
```


### Example: Looping through Dictionaries



{:.input_area}
```python
# This example of looping through dictionaries provided
dictionary = {
    'key1' : 'value1', 
    'key2' : 'value2'
}

for item in dictionary:
    
    # When you loop through a dictionary like this, `item` is the key 
    key = item
    
    # Using the key, you can access the associated value of the dictionary from within the loop
    value = dictionary[item]
    
    # Print out data for each loop iteration
    print('New Loop Iteration')
    print('\tKey is:\t', item)
    print('\tVal is:\t', value)
```


{:.output_stream}
```
New Loop Iteration
	Key is:	 key1
	Val is:	 value1
New Loop Iteration
	Key is:	 key2
	Val is:	 value2

```

### Q14 - Loops: Dictionaries (0.5 points)

Using the `subjects` dictionary, write a for loop that loops across the dictionary and collects all subject numbers (ex. 'S2') where the dictionary value is False. 

Imagine, for example, the dictionary indicates whether processing is complete, and we wanted to get a list of the subjects that need more analyses. 

To answer this question, use a for loop across the `subjects` dictionary. You then need to get the associated value in each iteration, and check if it is `True`. If it is `True`, you can use `continue` to skip ahead to the next iteration. Otherwise, append the subject number (ex 'S2') to a list called `not_finished`. 



{:.input_area}
```python
# This dictionary provided for you
subjects = {
    'S1' : True,
    'S2' : False,
    'S3' : True,
    'S4' : False,
}
```




{:.input_area}
```python
### BEGIN SOLUTION
not_finished = []
for subject in subjects:
    
    if subjects[subject] == True:
        continue
    else:
        not_finished.append(subject)
### END SOLUTION
```




{:.input_area}
```python
assert isinstance(not_finished, list)
assert len(not_finished) == 2

### BEGIN HIDDEN TESTS
assert not_finished == ['S2', 'S4'] or not_finished == ['S4', 'S2']
### END HIDDEN TESTS
```


## Part 5:  Ciphers

This part is an application of all the tools we have covered so far, to the problem of creating and using ciphers. 

A cipher is procedure for encoding and decoding secret messages (or encrypted data). 

To work on this application, we are going to need to use loops and collections. 

It also uses concepts and ideas from encoding and decoding - and in particular the operators `ord` and `chr`. 



{:.input_area}
```python
# Setup - run this cell before doing the next part of the assignment
import os
if not os.path.exists('A2Code'):
    os.mkdir('A2Code')
```




{:.input_area}
```python
# Example / outline of writing a cipher
#   The following shows a layout of writing a cipher.
#   You will be writing code to actually do the encoding / decoding.

# Create a message
original_message = 'Hello from Tom.'
print('Original Message:\t', original_message)

# First, Apply Encoding Code, to convert to an encoded message
encoded = 'ĐĭĴĴķèĮĺķĵèĜķĵö'
print('Encoded Message:\t', encoded)

# Then, Apply Decoding Code, to decode into an interpretable message
decoded = 'Hello from Tom.'
print('Decoded Message:\t', decoded)
```


{:.output_stream}
```
Original Message:	 Hello from Tom.
Encoded Message:	 ĐĭĴĴķèĮĺķĵèĜķĵö
Decoded Message:	 Hello from Tom.

```

### Q15 - Creating an Encoder (0.5 points)

Write a code block to encode strings into a secret message.

Your code will presume a number, stored in `key`, and a message to encode, as a string variable called `message`. Don't define these variables in your code - they will be defined when you run the tests.

To do so:
- Initialize a variable called `encoded` as an empty string
- Use a for loop to loop across all characters of a string variable `message`
    - Inside the loop, convert the character to another character:
        - Get the unicode code point for the character (using `ord`)
        - Add the value of `key` to that code point (which should be an int)
        - Convert this new int back to a character (using `chr`).
    - Also inside the loop, add this converted char to the string `encoded`



{:.input_area}
```python
%%writefile A2Code/encoder.py

### BEGIN SOLUTION
encoded = ''
for char in message:
    encoded = encoded +  chr(ord(char) + key)
### END SOLUTION
```


{:.output_stream}
```
Overwriting A2Code/encoder.py

```



{:.input_area}
```python
key = 200
message = 'hello'

%run -i ./A2Code/encoder.py  

assert isinstance(encoded, str)
assert encoded == 'İĭĴĴķ'

print('Original Message: \t', message)
print('Encoded Message: \t', encoded)
```


{:.output_stream}
```
Original Message: 	 hello
Encoded Message: 	 İĭĴĴķ

```

### Q16 - Decoder (0.5 points)

Write a code block to decode strings from secret encodings back to readable messages.

To do so:
- Initialize a variable called `decoded` as an empty string
- Use a for loop to loop across all characters of a presumed string variable called `encoded`
    - Inside the loop, convert the character to another character:
        - Get the unicode code point for the character (using `ord`)
        - Subtract the value of `key` to that code point (which should be an int)
            - This undoes the secret encoding of the character, getting back to the original value
        - Convert this new int back to a character (using `chr`).
    - Also inside the loop, add this converted char to the string `decoded`
    
Note that the code to answer this question should look very similar to how you answered the encoding question. 

In fact, you can even copy over the encoding code, and make some small changes to make it function as a decoder. 



{:.input_area}
```python
%%writefile A2Code/decoder.py

### BEGIN SOLUTION
decoded = ''
for char in encoded:
    decoded = decoded + chr(ord(char) - key)
### END SOLUTION
```


{:.output_stream}
```
Overwriting A2Code/decoder.py

```



{:.input_area}
```python
key = 200
encoded = 'İĭĴĴķ'

%run -i ./A2Code/decoder.py  

assert isinstance(decoded, str)
assert decoded == 'hello'

print('Encoded Message: \t', encoded)
print('Decoded Message: \t', decoded)
```


{:.output_stream}
```
Encoded Message: 	 İĭĴĴķ
Decoded Message: 	 hello

```

### Using the encoder and decoder together

The following are a couple examples of using the encoder and decoder together. 



{:.input_area}
```python
# Using the encoder
key = 500
message = 'This is a secret message'

%run -i ./A2Code/encoder.py  
%run -i ./A2Code/decoder.py

print('\nOriginal Message: \t', message)
print('\nEncoded Message: \t', encoded)
print('\nDecoded Message: \t', decoded, '\n')

assert message == decoded
```


{:.output_stream}
```

Original Message: 	 This is a secret message

Encoded Message: 	 ɈɜɝɧȔɝɧȔɕȔɧəɗɦəɨȔɡəɧɧɕɛə

Decoded Message: 	 This is a secret message 


```



{:.input_area}
```python
# Using the encoder
key = 1000
message = 'Python is pretty cool, eh?'

%run -i ./A2Code/encoder.py  
%run -i ./A2Code/decoder.py

print('\nOriginal Message: \t', message)
print('\nEncoded Message: \t', encoded)
print('\nDecoded Message: \t', decoded, '\n')

assert message == decoded
```


{:.output_stream}
```

Original Message: 	 Python is pretty cool, eh?

Encoded Message: 	 иѡќѐїіЈёћЈјњэќќѡЈыїїєДЈэѐЧ

Decoded Message: 	 Python is pretty cool, eh? 


```

### Using a Custom Encoder

The encoder & decoding we created above is built on conversions based on manipulating unicode code points.

If a potential attacker wanted to decode our messages, and happened to know we were using this approach, there are some relatively simple ways that they could try to figure out our encoding key, and then, if successful decode our messages. 

Thought experiment: can you think of ways to decode messages that use this encoding?

To thwart this potential attacker, let's now explore using a custom encoding. Instead of manipulating code points, we are going to use a custom mapping to switch out characters to encode our messages. 



{:.input_area}
```python
# Custom encoding dictionary provided - make sure you run this cell
#   In this encoding, each key will get switched out for the associated value
#     So, for example, whenever we see an 'a', we want to switch it out for an 'r'. 
custom_encodings = {
    'a' : 'r', 
    'e' : 'p', 
    'i' : 'm',
    'o' : 'n',
    'u' : 's'
}
```


### Q17 - Custom Encoder (0.5 points)

Write a code block to encode strings from original messages, using our custom encoding.

To do so:
- Initialize a variable called `custom_encoded` as an empty string
- Use a for loop to loop across all characters of a presumed string variable called `custom_message`
    - Inside the loop, check if the current character is in the `custom_encodings` dictionary
        - If it is, use the current char to get the value from `custom_encodings`, and concatenate it to `custom_encoded`
            - The line inside the if should look something like `out = out + dictionary[char]`
            
        - Otherwise, concatenate the current character to `custom_encoded`



{:.input_area}
```python
%%writefile A2Code/custom_encoder.py

### BEGIN SOLUTION
custom_encoded = ''
for char in custom_message:
    
    if char in custom_encodings:
        custom_encoded = custom_encoded + custom_encodings[char]
    else:
        custom_encoded = custom_encoded + char
### END SOLUTION
```


{:.output_stream}
```
Overwriting A2Code/custom_encoder.py

```



{:.input_area}
```python
custom_message = 'vowels aint great'

%run -i ./A2Code/custom_encoder.py

assert isinstance(custom_encoded, str)
assert custom_encoded == 'vnwpls rmnt grprt'

print('\nOriginal Message: \t', custom_message)
print('\nEncoded Message: \t', custom_encoded, '\n')
```


{:.output_stream}
```

Original Message: 	 vowels aint great

Encoded Message: 	 vnwpls rmnt grprt 


```

### Using Variable Keys

Part of the reason the unicode code point conversation can be easy to decode is that character always get encoded to the same output. So, if you know a pattern of the language, for example that 'e' is usually the most common letter, you can use this to make an educated guess that the most common character in the encoded message is probable 'e', and from there figure out the encoding key. 

One way around this is to use a procedure to use different transforms for each character, or, basically, use a different key for each time you encode a character. This breaks the 1-to-1 mapping between original and encoded characters, and makes the encoding harder to crack. As long as the decoder knows a pattern of how update keys, then it is still decodable, by knowing the first key, and the pattern to get to the next keys. 

### Q18 - Encodings with variable keys (0.5 points)

Here we will write an encoder that using a variable keys, whereby each time a key is applied, the key itself is also updated, by adding a number. 

This code will presume two numbers, `start_key` and `key_increment`. 

This code will look very similar to the code for the encoder in Q15. Copy that code in and you are going to `key = start_key` before the loop. The loop will contain the same code to encode each character, and you need to add a line within the loop, after the encoding, that update the `key` variable to increment it by the value stored in `key_increment`. 



{:.input_area}
```python
%%writefile A2Code/variable_encoder.py

### BEGIN SOLUTION
key = start_key
encoded = ''
for char in message:
    encoded = encoded + chr(ord(char) + key)
    key = key + key_increment
### END SOLUTION
```


{:.output_stream}
```
Overwriting A2Code/variable_encoder.py

```



{:.input_area}
```python
message = "By the way, what we're doing here basically the same as encryption"

start_key = 150
key_increment = 3

%run -i ./A2Code/variable_encoder.py

assert isinstance(encoded, str)
assert encoded == "ØĒ¼ēĊĊÈĢďĪà×ıĥġķæŀıöńĺøĿōŊŒŎĊŕŕťśęŞŠŵŮūŬźŽƍķƎƅƅŃƙƊƙƔŒƖƫśƣƯƧƹǃƽǄƼǅǇ"

print('\nOriginal Message: \t', message)
print('\nEncoded Message: \t', encoded, '\n')
```


{:.output_stream}
```

Original Message: 	 By the way, what we're doing here basically the same as encryption

Encoded Message: 	 ØĒ¼ēĊĊÈĢďĪà×ıĥġķæŀıöńĺøĿōŊŒŎĊŕŕťśęŞŠŵŮūŬźŽƍķƎƅƅŃƙƊƙƔŒƖƫśƣƯƧƹǃƽǄƼǅǇ 


```

### Breaking a Variable Encoder

#### Extra (optional) Information for the Curious - on Cryptography & Alan Turing

This kind of 'variable encoder' in which the encoding transform updates every time it is applied is much harder for an outside attacker to break (if they do not know the initial key, and the way it changes every application). 

This is, broadly, the kind of encryption which was used by German forces in World War II to encode messages - the ENIGMA code. 

This approach is, however, still breakable - it just takes a lot of clever analysis and number crunching. During World War II, Alan Turing, having already at that point done fundamental work developing the very concept of a digital computer, developed machines and algorithms to try to break the German Enigma code, eventually managing to decode it with his team at Bletchley Park.

Cracking this code was a huge development in the war - it is estimated this code breaking work, which allowed the Allies to decode messages and anticipate German actions, may have shortened the war by up 2 to 3 years, saving millions of lives in the process.

By the early 1950s, though his codebreaking work was still strictly confidential and he was largely unknown by the general public, Alan Turing had gone on to make other huge contributions to the fields of computation and artificial intelligence, amongst others, that would go on to have massive impact on the modern world. 

The British government, who years before had employed him as a codebreaker, then prosecuted Alan Turing for homosexual activity, and forced him to undergo chemical castration. Alan Turing died of suicide in 1954, at the age of 41. 

For more information on Alan Turing, check out the article linked below, and/or look into the movie `The Imitation Game`, a dramatization of his work on code breaking during the war. 

Short Article on Alan Turing: https://www.bbc.com/news/technology-18419691

### Variable Decoder

The code below is provided for you, that performs decoding of a variable decoder. 

To do so, it needs to know the `start_key` and `key_increment` that were used.



{:.input_area}
```python
%%writefile A2Code/variable_decoder.py

# Knowing the start key, and the length of the message, we can reconstruct the current key
key = start_key + (len(encoded) * key_increment)

decoded = ''

# Note that this decodes the message backwards, stepping back along key values
for char in encoded[::-1]:
    
    # Step the key back one step, and apply to current character
    key = key - key_increment
    decoded = decoded + chr(ord(char) - key)
    
# Having decoded backwards, flip the message back around
decoded = decoded[::-1]
```


{:.output_stream}
```
Overwriting A2Code/variable_decoder.py

```

### Decoding a provided message

The cell below has an encoded message, using variable encoding, and the `start_key` and `key_increment` needed to decode. 

Run the following cell to execute the decoding code from above, and decode the message. 



{:.input_area}
```python
# Do decoding on message above
encoded = """Ãâø¡ü¬èõ÷­¼±ÜµÿĈċĂ¿ĚĒĚÇĊĝĒÏĖġğĦĲĤīĦáķĭĬéĬŀłĺĺŃńľŉőĀëíĪŐŝœŒšđŪŖŰęŴŬŴġŤŷŬĩůżŽŶĳƃƆƐŇĽƒƐŃƈƖ\
ƗƒƟƐƥƦŕƦƧśƱƧƢƷŦőœƍǆůǅƻƺŷǐƼǖƋƁǌǋƇǢǚǢƏǙǔǥǧǞǩƝǳǰƣǷǬǪǷǹȈƱǿǾȂǾƻȑȇȊȖǅȊȒțȕȔȣǓȨȫȮȡȣǟǮǣȫȶȵȷȼɆȺɁȼǷɎɋǽɎɏȃəɏɒ\
ɞȍɢɥɨɛɝșɲɦɫɭȣɧɬȩɬȭɿʃʂɿɼɼʏȽʎʑʗʎʖʗəȷȹɷʥʤʤɥɛʑʮʮ"""

start_key = 123
key_increment = 2

%run -i ./A2Code/variable_decoder.py

print(decoded)
```


{:.output_stream}
```
Hey y'all - I hope you are enjoying the assignment!

Either way you are done now, so congrats on that!

By the way, if you happen to really like this cipher stuff - following up on this stuff will be a project option.

From, Tom

```

## The End!

This is the end of the assignment!
Have a look back over your answers, and also make sure to Restart & Run All from the kernel menu to double check that everything is working properly. 

When you are ready to submit your assignment, upload it to TritonED under Assignment-2.
