#!/usr/bin/env python
# coding: utf-8

# # CL5: Loops
# 
# Welcome to the fifth coding lab!
# 
# In this Coding Lab we will focus on understanding loops and incorporating them into functions.

# **Note**: You may *not* be able to complete all of this in 50 minutes.  This are meant to help you gain mastery and provide additional practices, not to stress you out a ton. Make a concerted effort. Do your best to complete it. But, if you don't figure it all out, that's why we post answers for coding labs!

# ## Part 1: Loops Review & Exploration
# 
# We will now explore two ways to iterate over data in Python - `for` and `while` loops. 
# 
# Each type of loop performs its respective code block until certain conditions are met. Here, we will explore what those conditions are. 
# 
# Notes: 
# - "iterate" means to perform an action repeatedly 
# - Sometimes, we accidentally make loops that never end (infinite loop). If that happens (and you see an asterisk to the left of your cell), "break" the cell by selecting it and then pressing "ctrl+c". Alternatively, press the "stop" button (square icon) in the Jupyter toolbar. 

# ### Loops 
# 
# First, declare a variable called `counter` that has type int and value zero.
# 
# Then write a `while` loop that runs 10 times and use `counter` to track how many times the loop runs. 

# In[ ]:


### BEGIN SOLUTION
counter = 0
while counter < 10:
    counter = counter + 1
### END SOLUTION


# In[ ]:


# Check that (after the loop runs) that there is a variable called `counter` that has value 10
assert counter == 10


# ### Infinite Loops
# 
# The while loop included here would run indefinitely unless someone puts a stop to it! 
# 
# Add your own code that causes the loop to exit when the `counter` variable reaches 10 by using `break`. 
# 
# Note: Sometimes, we accidentally make loops that never end - try that by running the cell below before adding 
# 
# If that happens, interrupt the cell by selecting it and then pressing "ctrl+c". Alternatively, press the "stop" button (square icon) in the Jupyter toolbar. 
# 
# Infinite loop to fix:
# ```python
# counter = 0
# 
# while True:
#     
#     print("the value of 'counter' = " + str(counter))
#     counter +=1
#     
# ```

# In[ ]:


### BEGIN SOLUTION
counter = 0

while counter < 10:

    print("the value of 'counter' = " + str(counter))
    counter +=1
    
    if counter >= 10:
        break
### END SOLUTION


# Now, rather than using `break`, edit the loop from above so that the condition following `while` will eventually evaluate as `False` (and thus terminate the loop).

# In[ ]:


### BEGIN SOLUTION
counter = 0

# edit condition
while counter < 10:
    
    print("the value of 'counter' = " + str(counter))
    counter +=1
### END SOLUTION


# ### Loop Explorations
# 
# Now, explore using for and while loops and breaks. 
# 
# Here are some things to try, and questions to ask - *try to write code for a few of these* (but know that you should ultimately be familiar with all of them):
# - What happens if you use 'break' all by itself?
# - What are some different ways to loop through a list? tuple?
# - Write these combinations: 
#     - a `for` loop with a `break`, a `for` loop with a `continue`
#     - a `while` loop with a `break`, a `while` loop with a `continue`
# - Write some loops that loop across lists:
#     - Write a loop that loops across, and prints out, all the elements of a list
#     - Write a loop that loops across, and prints out, every second element of a list
#     - Write a loop that loops across, and prints out, every element of a list in reverse order
#     - Write a loop that loops across, and prints out, the first half of a list
# - Write a loop with a conditional inside it.
# - Can you have loops inside loops? If you think so, try and write a nested loop. 
# 
# Reminder: you can add as many cells as you'd like to test these out! 

# In[ ]:


### BEGIN SOLUTION
my_list = [1, 2]
my_tuple = ('a', 'b')

# You can loop through lists or tuples directly, or with indices
# Loop through list with for - same goes for tuple
for el in my_list:
    print(el)

print('')
    
# Loop through tuple using indexing - same goes for list
for ind in range(2):
    print(my_tuple[ind])

#- Write these combinations: 
#    - a `for` loop with a `break`, a `for` loop with a `continue`
#    - a `while` loop with a `break`, a `for` loop with a `continue`

letter_list = ['a', 'c', 'e']

for it in letter_list:
    if it == 'c':
        break

for it in letter_list:
    if it == 'a':
        continue

# While loops with break and continue
ind = 0

while ind < 5:
    if ind == 2:
        break
    ind = ind + 1

while ind < 5:
    ind = ind + 1
    if ind == 2:
        continue

# These are loops using indexing, to grab different elements of the list
another_list = [1, 2, 3, 4]

print('Print all elements list:')
for it in another_list:
    print(it)
print('')
    
print('Print every second element list:')
for it in another_list[1::2]:
    print(it)
print('')

print('Print reversed list:')
for it in another_list[::-1]:
    print(it)
print('')

print('Print first half:')
half_index = int(len(another_list)/2)
for it in another_list[0:half_index]:
    print(it)
print('')

# Loop with a conditional in it
for it in [True, False]:
    if it == True:
        print('Yay.')

# Yes, you can have a loop inside a loop
for a_val in [1, 2, 3]:
    for b_val in ['a', 'b', 'c']:
        print(a_val, b_val)


### END SOLUTION


# ### Specific looping task
# 
# `print`ing the output is great to learn about and explore loops, but typically we're looping to generate some output. 
# 
# Generate a list below that stores various integers and strings. 
# 
# Write a loop that will separate out the elements in your list by type, such that all the integers are stored in a list called `my_ints` and all of the strings are stored in a list called `my_strs`

# In[ ]:


### BEGIN SOLUTION
# the specific list you create is up to you
my_list = [1, "apple", 15, "banana", 29, 30, "yay python!"]
my_ints = []
my_strs = []

for val in my_list:
    if type(val) == int:
        my_ints.append(val)
    elif type(val) == str:
        my_strs.append(val)
        
print(my_ints)
print(my_strs)
### END SOLUTION


# In[ ]:


assert type(my_ints) == list
assert type(my_strs) == list

# check to make sure all values in each list are of expected type
assert all([type(x) == int for x in my_ints])
assert all([type(x) == str for x in my_strs])


# ## Part 2:  Ciphers (revisited)
# 
# In A2, you created functions that would encode and decode a single character...but not an entire message. Here, we'll revist the concepts from Part 3 of A2...but you'll be able to encode and decode entire strings.
# 
# **Be sure to at least give `encoder()` and `decoder()` a concerted effort**. And, if you don't finish all of this section, check the answer key when posted!

# ### `encoder()`
# 
# In this question, you'll update the `encoder()` function from A2. The function's goal is the same as in A2...but we want this function to encode an entire string, not just a single character.
# 
# Write a function `encoder()` to encode a string into a secret message.
# 
# Your function will take two parameters:
# - `input_string` | The string to be encoded (str)
# - `key` | The key to be used during encoding (int; default: 200)
# 
# Within the function:
# 
# - initalize an empty string `output_string`
# - Then, loop through each `char` in `input_string` and:
#     - Get the unicode code point for each `char` (using `ord`)
#     - Add the value of `key` to that code point (which should be an int)
#     - Convert this new int back to a character (using `chr`).
#     - Add this new character to the string `output_string`
# 
# Be sure to `return` your encoded string from the function.

# In[ ]:


### BEGIN SOLUTION
def encoder(input_string, key=200):
    output_string = ''
    
    for char in input_string:
        output_string = output_string + chr(ord(char) + key)
    
    return output_string
### END SOLUTION


# In[ ]:


# you can use this cell to test/execute/check your thinking (optional)


# In[ ]:


assert callable(encoder)
assert type(encoder('hello')) == str
assert encoder(input_string='hello') == 'İĭĴĴķ'


# In[ ]:


assert encoder(input_string='hello', key=500) == 'ɜəɠɠɣ'
assert encoder(input_string='HELLO', key=100) == '¬©°°³'


# ### `decoder()`
# 
# In this question, you'll update the `decoder()` function from A2. The function's goal is the same as in A2...but we want this function to decode an entire string, not just a single character.
# 
# Write a function `decoder()` to decode a string back into its original message.
# 
# Your function will take two parameters:
# - `input_string` | The string to be decoded (str)
# - `key` | The key to be used during decoding (int; default: 200)
# 
# Within the function:
# 
# - initalize an empty string `output_string`
# - Then, loop through each `char` in `input_string` and:
#     - Get the unicode code point for each `char` (using `ord`)
#     - *Subtract* the value of `key` to that code point (which should be an int)
#     - Convert this new int back to a character (using `chr`).
#     - Add this new character to the string `output_string`
# 
# Be sure to `return` your encoded string from the function.

# In[ ]:


### BEGIN SOLUTION
def decoder(input_string, key=200):
    output_string = ''
    
    for char in input_string:
        output_string = output_string + chr(ord(char) - key)
    
    return output_string
### END SOLUTION


# In[ ]:


# you can use this cell to test/execute/check your thinking (optional)


# In[ ]:


assert callable(decoder)
assert type(decoder('İĭĴĴķ')) == str
assert decoder(input_string='İĭĴĴķ') == 'hello'


# In[ ]:


assert decoder(input_string='ɜəɠɠɣ', key=500) == 'hello'
assert decoder(input_string='¬©°°³', key=100) == 'HELLO'


# ### Using the encoder and decoder together
# 
# The following are a couple examples of using the encoder and decoder together. 

# In[ ]:


# Using the encoder & decoder
key = 500
message = 'This is a secret message'
encoded_message = encoder(message, key)
decoded_message = decoder(encoded_message, key)

print('\nOriginal Message: \t', message)
print('\nEncoded Message: \t', encoded_message)
print('\nDecoded Message: \t', decoded_message, '\n')

assert message == decoded_message


# In[ ]:


# Using the encoder & decoder
key = 1000
message = 'Python is pretty cool, right?'

encoded_message = encoder(message, key)
decoded_message = decoder(encoded_message, key)

print('\nOriginal Message: \t', message)
print('\nEncoded Message: \t', encoded_message)
print('\nDecoded Message: \t', decoded_message, '\n')

assert message == decoded_message


# ### Using Variable Keys
# 
# Part of the reason the unicode code point conversion can be easy to decode is that the same character always gets encoded to the same output. So, if you know a pattern of the language, for example that 'e' is usually the most common letter, you can use this to make an educated guess that the most common character in the encoded message is probable 'e', and from there figure out the encoding key. 
# 
# One way around this is to use a procedure to use different transforms for each character, or, basically, use a different key for each time you encode a character. This breaks the 1-to-1 mapping between original and encoded characters, and makes the encoding harder to crack. However, as long as the decoder knows a pattern of how the key updates, then it is still decodable by knowing the first key and the pattern to get to the next keys. 

# ### Encoder with variable keys
# 
# Here we will write a function `variable_encoder()` that will use variable keys within the function, such that a new/different key is used for each character to be encoded. 
# 
# This function will have the following input parameters:
# - `input_string` | the string to be encoded (str)
# - `start_key` | the first value to be used for key within the function (int)
# - `key_increment` | the value by which to increment the key each time a character is encoded (int)
# 
# This code will look very similar to the code for the `encoder()` question earlier in this assignment. Copy that code in to start and then update to:
# 
# 1. Have the correct function/parameter names as specified above
# 2. Before the loop, specify that the value of `key` should be `start_key`
# 3. The loop will contain the same code to encode each character, but you need to add a line within the loop, after the encoding, that updates the `key` variable by incremening the value in `key` by the value stored in `key_increment`
# 
# Be sure to `return` the encoded string (`output_string`) from the function

# In[ ]:


### BEGIN SOLUTION
def variable_encoder(input_string, start_key, key_increment):
    output_string = ''
    key = start_key
    
    for char in input_string:
        output_string = output_string + chr(ord(char) + key)
        key = key + key_increment
        
    return output_string
### END SOLUTION


# In[ ]:


# you can use this cell to test/execute/check your thinking (optional)


# In[ ]:


message = "By the way, what we're doing here basically the same as encryption"

# use our variable encoder
encoded = variable_encoder(input_string=message, start_key=150, key_increment=3)

assert type(encoded) == str
assert encoded == "ØĒ¼ēĊĊÈĢďĪà×ıĥġķæŀıöńĺøĿōŊŒŎĊŕŕťśęŞŠŵŮūŬźŽƍķƎƅƅŃƙƊƙƔŒƖƫśƣƯƧƹǃƽǄƼǅǇ"

print('\nOriginal Message: \t', message)
print('\nEncoded Message: \t', encoded, '\n')


# ### Breaking a Variable Encoder
# 
# #### Extra (optional) Information for the Curious - on Cryptography & Alan Turing
# 
# This kind of 'variable encoder' in which the encoding transform updates every time it is applied is much harder for an outside attacker to break (if they do not know the initial key and the way it changes every application). 
# 
# This is, broadly, the kind of encryption which was used by German forces in World War II to encode messages - the ENIGMA code. 
# 
# This approach is, however, still breakable - it just takes a lot of clever analysis and number crunching. During World War II, Alan Turing, having already at that point done fundamental work developing the very concept of a digital computer, developed machines and algorithms to try to break the German ENIGMA code, eventually managing to decode it with his team at Bletchley Park.
# 
# Cracking this code was a huge development in the war - it is estimated this code breaking work, which allowed the Allies to decode messages and anticipate German actions, may have shortened the war by up to 2 to 3 years, saving millions of lives in the process.
# 
# By the early 1950s, though his codebreaking work was still strictly confidential and he was largely unknown by the general public, Alan Turing had gone on to make other huge contributions to the fields of computation and artificial intelligence, amongst others, that would go on to have massive impacts on the modern world. 
# 
# The British government, who years before had employed him as a codebreaker, then prosecuted Alan Turing for homosexual activity and forced him to undergo chemical castration. Alan Turing died of suicide in 1954, at the age of 41. 
# 
# For more information on Alan Turing, check out the article linked below, and/or look into the movie `The Imitation Game`, a dramatization of his work on code breaking during the war. 
# 
# Short Article on Alan Turing: https://www.bbc.com/news/technology-18419691

# ### Variable Decoder
# 
# The code below is provided for you, and performs decoding of a variable encoder. 
# 
# To do so, it needs to know the `start_key` and `key_increment` that were used.

# In[ ]:


def variable_decoder(input_message, start_key, key_increment):
    # Knowing the start key and the length of the message, we can reconstruct the current key
    key = start_key + (len(encoded) * key_increment)

    decoded = ''

    # Note that this decodes the message backwards, stepping back along key values
    for char in encoded[::-1]:

        # Step the key back one step, and apply to current character
        key = key - key_increment
        decoded = decoded + chr(ord(char) - key)

    # Having decoded backwards, flip the message back around
    decoded = decoded[::-1]
    
    return decoded


# ### Decoding a provided message
# 
# The cell below has an encoded message (using variable encoding) and the `start_key` and `key_increment` needed to decode. 
# 
# Run the following cell to execute the decoding code from above, and decode the message. 

# In[ ]:


# Do decoding on message above
encoded = 'Ãâø¡ü¬èõ÷\xad¼±ÜµÿĈċĂ¿ĚĒĚÇĊĝĒÏĖġğĦĲĤīĦáķĭĬéķĮıòÝĞĽùŔŌŔāŋņŗřŐśďťŢĕũŞŜũūźģűŰŴŰĭƃŹżƈķżƄƍƇƆƕŅƚƝƠƓƕőŠŕƝƨƧƩƮƸƬƳƮũǀƽůǀǁŵǋǁǄǐſǘǌǑǓƉǍǒƏǒƓǛǠǧǜǩƟǱǵǴǱǮǮȁƯȀȃȉȀȈȉǋǈ'
decoded = variable_decoder(input_message=encoded, start_key=123, key_increment=2)

print(decoded)


# ## Part 3: Challenges
# 
# Give these a shot, but it's definitely ok if you don't figure these out all the way! Remember, if you don't figure out the answer, definitely check the answer key when posted!

# ### Debugging Challenge
# 
# You're trying to write a function that will count the number of vowels in your name, storing that value in `counter` and `return`ing that value from the function. To get started, you store your name in the variable `my_name` and write the code you see here:
# 
# ```python
# my_name == 'Shannon'
# vowels = ['A','E','I','O','U', 'a', 'e', 'i', 'o', 'u']
# counter = 0
# 
# for char in my_name:
#     if char == vowels:
#         counter =  1
# ```
# 
# ...However, 2)the code above is not quite working and 2) it's not a function!...work to debug the code to accomplish the task!
# 
# Note: This question uses a `for` loop. Next week's coding lab will get you even more loops practice!

# In[2]:


### BEGIN SOLUTION
def count_vowels(my_name):
    vowels = ['A','E','I','O','U', 'a', 'e', 'i', 'o', 'u']
    counter = 0

    for char in my_name:
        if char in vowels:
            counter += 1
    
    return counter
### END SOLUTION


# In[ ]:


# try it out down here...


# ### Nested Loop Challenge
# 
# Using nested loops, write code that will print out a pattern that looks like this:
# 
# 1 <br>
# 1 2 <br>
# 1 2 3 <br>
# 1 2 3 4 <br>
# 1 2 3 4 5 <br>
# 1 2 3 4 5 6 <br>
# 1 2 3 4 5 6 7
# 
# Hints:
# - You can do this with two while loops, one inside the other.
# - You will have two indices counters, one for each loop. 
# - For the print statement, it will look something like `print(index_inner, end=" ")`

# In[ ]:


### BEGIN SOLUTION
index_outer = 1
while index_outer < 8:
    
    index_inner = 1
    
    while index_inner <= index_outer:
        print(index_inner, end=" ")
        index_inner = index_inner + 1
        
    print("")
    index_outer = index_outer + 1
### END SOLUTION


# If you get the above pattern working, try manipulating the code to print out different patterns, and with different symbols. 

# In[ ]:





# ## The End!
# 
# This is the end of this Coding Lab!
# 
# Be sure you've made a concerted effort to complete all the tasks specified in this lab. Then, go ahead and submit on datahub!
