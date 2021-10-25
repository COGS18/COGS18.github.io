#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# **Due Dates**:
# - **A2** due tonight (10/22; 11:59 PM)
# 
# **Notes**:
# - Please fill out [daily participation survey] today(https://docs.google.com/forms/d/e/1FAIpQLScR65_Xk-ZDWFLQkGvzlKpBHm3Rxi8ZVep5vKGlcOdHjvmLEg/viewform?usp=sf_link) (optional) <- really helpful, especially when you're newer to teaching!
# - **CL3** grades have been posted

# **Q&A**
# 
# Q: what does the \t\t: thing mean?  
# A: '\t' is a special character that adds a tab into your code (to space things out more)
# 
# Q: Do we have to name the ord/char variables ourselves?  
# A: Nope - `ord()` and `chr()` are functions that exist in Python.
# 
# Q: Can I set systematic rules for encoding?  
# A: No because there are *many* different schemes for encoding, but the general idea is that you can "encode" the same message using different characters. The *meaning* doesn't changes, but the *representation* does. A bit more on encryption specifically [here](https://blog.storagecraft.com/5-common-encryption-algorithms/), if you're curious!
# 
# Q: Why does symbol represent something "arbitrary"? What does that mean?  
# A: Think about the letter "F". It's an arbitrary symbol that *we* as a society represents the sound "fah". We *could* have picked a different character...but we didn't. That's why it's "arbitrary."
# 
# Q: I am curious about encoding/decoding and would love to learn more about it.  
# A: This is an option for your final project! You could "extend" what we do in A2 and learn more about it for your final project! We'll discuss more about this later!
# 
# Q: Since we cannot have mutable thing as keys for dictionaries, can we have tuples as keys since it is immutable?  
# A: Yup! It's less common, but it is python-legal.
# 
# Q: Is unicode like ascii?  
# A: They're similar concepts, but not synonymous. More explanation [here](https://medium.com/@vanvlymenpaws/ascii-vs-unicode-4174def5c09d).
# 
# Q: In the last part we did with +500, why did it create a weird answer when we did shift and return? It had no numbers involved.  
# A: The weird answer was b/c of the characters associated with the unicode integers. To try it out, see that `chr(550)` gives you a weird character. Play around with the integer used to see the different characters. You can look up the characters associated with each integer [here](https://en.wikipedia.org/wiki/List_of_Unicode_characters).
# 
# Q: I have a question about Jupyter notebook, what does it mean when we try to validate an assignment and it says: "the source of the following cell has changed, but it should not have!" Will this cause problems with the grading? Sorry if I accidentally changed something :/  
# A: It typically means that you accidentally copy+pasted a cell that included instructions or changed a cell from code to markdown or vice versa. This is something we can fix in grading.
# 
# Q: I was looking at my notes on collections and I'm not sure if I missed that part of class or didn't catch it but are we supposed to know how to add new items into a list? I tried to look around in the "collections" notes to see if there was anything on adding in new items into a list but it doesn't seem like there's anything on that so far other than updating a list.  
# A: `append()` was introduced in A2 and discussed during the exam review. This is the simplest way to add things to the end of a list. However, the values in an existing list can be changed/assigned using indexing and assignment. So, that's another approach.
# 
# Q: I wonder what is the purpose of unicode? Why is there always a number associated with a character?  
# A: Allows for consistent communication across different platforms.
# 
# Q: When would using dictionaries be useful?  
# A: Whenever you have two pieces of information that you want to be associated together. For example someone's name and their age...best to store that in a dictionary.
# 
# Q: In the character encodings with dictionaries, I am still confused on the cells regarding the Spanish letters. When we used "character_encodings[0]," is that 0 in reference to the first position or the key being 0?   
# A: When indexing into a dictionary, the thing between the square brackets always refers to the key.

# # Functions I
# 
# - defining a function
#     - `def`
#     - `return`
# - executing a function
#     - parameters
#     - separate namespace

# # Vocab
# 
# - Define/create/make a function: To set up and write the instructions for a function.
# - Execute/call/use a function: To actually use the pre-defined function.
# 
# - Input/parameter/argument: A variable defined by the user that is put/passed in between the parantheses `()` that comes after the function name.  
# - Output: The variable that is `return`ed to the user after the function is executed.

# ## Functions
# 
# <div class="alert alert-success">
# A function is a re-usable piece of code that performs operations on a specified set of variables, and returns the result.
# </div>

# ![cheeseburger](img/cheeseburger.png)

# ## Modular Programming
# 
# <div class="alert alert-success">
# Modular programming is an approach to programming that focuses on building programs from indendent modules ('pieces'). 
# </div>

# Copy + Pasting the same/similar bit of code is to be avoided.
# 
# **Loops** were one way to avoid this.
# 
# **Functions** are another!

# ## Functions for Modular Programming

# - Functions allow us to flexibly re-use pieces of code
# - Each function is independent of every other function, and other pieces of code
# - Functions are the building blocks of programs, and can be flexibly combined and executed in specified orders
#     - This allows us to build up arbitrarily complex, well-organized programs

# In[ ]:


# you've seen functions before
# here we use the type() function
my_var = [3, 4, 5]
type(my_var)


# In[ ]:


# the function len() doesn't depend on type()
# but they can both be used on the same variable
len(my_var)


# ## Function Example I
# 
# When you use `def`, **you are defining a function**.
# You are metaphorically writing the instructions for how to make the cheeseburger.

# In[ ]:


# define a function: double_value
# Notice that the parameter `num` is not explicitly defined with an = 
# This is because it will be defined later by the user when they execute the function.
def double_value(num):

    # do some operation
    doubled = num + num
    
    # return output from function
    return doubled    


# In[ ]:


# excecute a function by calling the function's name
# and defining the parameter within the parentheses
double_value(num = 2) 


# In[ ]:


# equivalent function call
# Here the parameter `num` is defined without 
# explicitly specifying the name of the parameter
double_value(2) 


# ## Function Example II
# 
# Here we are defining a function with multiple parameters

# In[ ]:


def add_two_numbers(num1, num2):
    
    # Do some operations with the parameters
    answer = num1 + num2
    
    # Return the variable answer
    return answer


# In[ ]:


add_two_numbers(5, 14)


# In[ ]:


# Execute our function again on some other inputs to double check 
# that our function is working how we think it should
output = add_two_numbers(-1, 4)
print(output)


# ## Function Example III
# 
# Let's define a more interesting function. Here we are using conditionals within our function.

# In[ ]:


# Determine if a value is even or odd
def even_odd(value): 
    if (value % 2 == 0): 
        out = "even"
    else: 
        out = "odd"
        
    return out


# In[ ]:


# Execute our function to check that
# it is working according to our expectations
even_odd(-1)


# ## Function Properties

# - Functions are defined using `def` followed by the name of the function, parentheses `()`, parameters within the parentheses, and then `:` after the parentheses, which opens a code-block that comprises the function
#     - Running code with a `def` block *defines* the function (but does not *execute* it)

# - Functions are *executed* with the name of the function and parentheses - `()` without `def` and `:`
#     - This is when the code inside a function is actually run

# ## Function Properties continued

# - Inside a function, there is code that performs operations on the available variables

# - Functions use the special operator `return` to exit the function, passing out any specified variables

# - When you use a function, you can assign the output (whatever is `return`ed) to a variable

# #### Clicker Question #1
# Given the function defined below, what will the second code cell below print out?
# 
# A) 0   &emsp;B) 2    &emsp;C) 4    &emsp;D) '2r.2 + 1'    &emsp;E) ¯\\\_(ツ)\_/¯

# In[ ]:


def remainder(number, divider):
    
    r = number % divider
    
    return r


# In[ ]:


ans_1 = remainder(12, 5)
ans_2 = remainder(2, 2)

print(ans_1 + ans_2)


# #### Clicker Question #2
# 
# Write a function `greet` that takes the parameter `name`. Inside the function, concatenate 'Hello', the person's name, and 'Good morning!". Assign this to `output` and return `output`.
# 
# A) I did it! &emsp;B) I think I did it. &emsp;C) I tried but I am stuck. &emsp;D) Super duper lost

# In[ ]:


## YOUR CODE HERE  
def greet(name):
    
    output = 'Hello ' + name + ', Good morning!'
    
    return output


# In[ ]:


# TEST YOUR FUNCTION HERE
greet('students')


# #### Clicker Question #3 
# 
# Write a function `create_dictionary` that takes two input lists `lst_1` and `lst_2`. Inside the function, join the two lists to form a dictionary `joined_dictionary` where the first element in `lst_1` is the first key in `joined_dictionary` and the the first element in `lst_2` is the first value in `joined_dictionary` and so on and so forth. Then return `joined_dictionary` as the output. 
# 
# A) I did it! &emsp;B) I think I did it. &emsp;C) I tried but I am stuck. &emsp;D) Super duper lost

# In[ ]:


# YOUR CODE HERE
def create_dictionary(lst_1, lst_2):
    
    joined_dictionary = {}
    counter = 0

    for key in lst_1:
        joined_dictionary[key] = lst_2[counter]
        counter += 1

    return joined_dictionary


# In[ ]:


# TEST YOUR FUNCTION HERE
# Note that the two input lists are the 
# same length for the function to work properly
random_lst_1 = ['a', 'b', 'c', 'd']
random_lst_2 = [1, 2, 3, 4]

create_dictionary(random_lst_1, random_lst_2)


# ## Function Namespace 

# - Each function has its own namespace
#     - They only have access to variables explicitly passed into them

# In[ ]:


# You can check variables defined in the global namespace with `%whos`
get_ipython().run_line_magic('whos', '')


# ### Variables defined inside a function only exist within that function.

# In[ ]:


# Names used inside a function are independent of those used outside
# variables defined outside of functions are global variables
# global variables are always available
my_var = 'I am a variable'

print(my_var)

def concat_self(my_var):
    
    my_var = my_var + ' ' + my_var
    
    return my_var

print(concat_self(my_var))

print(my_var)

my_var = concat_self(my_var)
print(my_var)


# ### another namespace example

# In[ ]:


def change_var(my_var):
    my_var = 'I am something else'
    print('Inside function: \t\t', my_var)


# In[ ]:


# my_var in the global namespace
my_var = 18
my_var


# In[ ]:


# my_var within the function
change_var(my_var)


# In[ ]:


# my_var in the global namespace remains unchanged
my_var 


# In[ ]:


print('Outside, before function: \t', my_var)
change_var(my_var)
print('Outside, after function: \t', my_var)


# ## Summary
# - how to define a function
# - how to execute a function
# - global namespace vs. local namespace
