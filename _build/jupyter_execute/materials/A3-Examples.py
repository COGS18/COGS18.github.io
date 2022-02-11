#!/usr/bin/env python
# coding: utf-8

# # Python Examples

# The following is a set of quick examples of the code constructs that we work through in class. 
# 
# This notebook does not have any explanations - so do check the course Materials for those details. 

# ## Defining Variables

# ### Basic Types

# In[1]:


my_int = 1
my_float = 12.2
my_boolean = True


# ### Collection Types

# In[2]:


my_string = 'abc'
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_dictionary = {'name1' : True, 'name2' : 12}


# ## Operators

# ### Mathematical Operators

# In[3]:


print('Addition: \t', 12 + 3)
print('Subtraction: \t', 12 - 3)
print('Multiplication: ', 12 * 3)
print('Division: \t', 12 / 3)


# In[4]:


print('Exponentiation:\t', 2**2)
print('Remainder: \t', 7%2)


# ### Boolean Operators

# In[5]:


# Boolean `and`
True and True


# In[6]:


# Boolean `or`
True or False


# In[7]:


# Boolean `not`
not True


# ### Other Operators

# In[8]:


# String concatenation
print('a' + 'b' + 'c')


# ## Value Comparisons

# In[9]:


# Equality comparisons
print('Equal:  \t', 1 == 1)
print('Unequal:\t', 2 != 1)


# In[10]:


# Magnitude Comparisons
print('Less Than:     \t\t\t', 2 < 3)
print('Greater Than:  \t\t\t', 4 > 5)
print('Less Than Or Equal to:     \t', 2 <= 2)
print('Greater Than Or Equal to:  \t', 3 >= 5)


# ## Conditionals

# In[11]:


first_condition = False
other_condition = True

if first_condition:
    print('if condition')
elif other_condition:
    print('elif condition')
else:
    print('else condition')    


# ## Loops

# In[12]:


# While Loop
ind = 0
while ind < 3:
    print('Looping!')
    ind = ind + 1

# see value of ind after loop terminates
print(ind)


# In[13]:


# For Loop
list_of_items = [1, 2, 3]
for item in list_of_items:
    print(item)


# In[14]:


# For Loop using Range
for iteration in range(5):
    print(iteration)


# **Note:** This is where material on the first midterm ends.

# ## Functions

# In[15]:


# Defining a function
def function_name(function_input_1, function_input_2):

    output = function_input_1 + function_input_2
    
    return output


# In[16]:


# Calling a function
answer = function_name(1, 2)

print('Answer:\t', answer)


# In[17]:


# Define a function with default values
def multiply(num1, num2=2):
    return num1 * num2


# In[18]:


# Calling a function that has default values
print(multiply(2))
print(multiply(2, 3))


# ## Combining Functions with Control Flow

# In[19]:


# Defining a Function with a Conditional inside it
def conditional_function(input_boolean):
    
    if input_boolean == True:
        output = 'Yay!'
    else:
        output = 'Nay.'
    
    return output


# In[20]:


# Calling our function
returned = conditional_function(True)
print(returned)


# In[21]:


# Defining a Function with a Loop inside it
def loop_function(my_list):
    
    new_list = []
    for item in my_list:
        temp = item + 1
        new_list.append(temp)
        
    return new_list


# In[22]:


# Calling our function
out_list = loop_function([1, 2, 3])
print(out_list)


# In[23]:


# Function with everything
def busy_function(complex_list):
    """This function takes a complex list, and returns the numbers of booleans in the list."""
    
    boolean_counter = 0
    
    for item in complex_list:
        if item == True or item == False:
            boolean_counter = boolean_counter + 1
            
    return boolean_counter


# In[24]:


# Calling our function
busy_function([True, 7.2, 'and', 13, False, '', None, 'word', True])


# ## Errors

# In[25]:


# Raise an error
raise ValueError('The value you gave is no good.')


# In[26]:


# Try / Except
try:
    sum()
except TypeError:
    print('Hmm. It seems that did not work.')


# ## Classes

# In[27]:


class Animal():
    
    # Create a class attribute
    domain = 'eukaryota'

    # Use init to define instance attributes
    def __init__(self, sound):
        self.sound = sound

    # Define a class method
    def speak(self):
        print(self.sound)


# In[28]:


# Create an instance of our class
gary = Animal('woof')
gary.speak()

