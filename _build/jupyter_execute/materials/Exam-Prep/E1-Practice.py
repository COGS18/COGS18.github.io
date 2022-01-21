#!/usr/bin/env python
# coding: utf-8

# # Exam #1 Practice Questions
# 
# To practice for the first exam, read through each of these questions and try and answer the question _before_ you run the code.
# 
# Since this is a notebook, you can also then run this code to check what it does. 
# 
# Make sure you understand why each thing does what it does!

# ## Variables & Operators
# 
# For each of the following cells, after executing the code, what will the value of `var_a` be?

# In[ ]:


# Variables-1
var_b = 2
var_a = var_b = 2%3


# In[ ]:


# Variables-2
var_b = False 
var_c = True
var_d = True
var_a = var_b or var_c or var_d


# In[ ]:


# Variables-3
var_b = 2**3
var_c = 2
var_a = float(var_b/var_c)


# In[ ]:


# Variables-4
var_a = 5**2 <= 30 or 25%4 > 1


# ## Indexing

# Given the following list:

# In[ ]:


my_lst = ['Python', True, 12, 'Java', False, None, 23, 'C++']


# What will each of the following code cells print out?

# In[ ]:


len(my_lst)


# In[ ]:


my_lst[1:4]


# In[ ]:


my_lst[-3:]


# In[ ]:


my_lst[1::2]


# In[ ]:


my_lst[1:6:2]


# ## Conditionals 

# ### Conditionals 1
# 
# What will the following code print out?

# In[ ]:


if True and not False:
    print('Yay')
elif False or not False:
    print('Also yay')


# ### Conditionals 2
# 
# What will the following code print out?
# 
# a) 1  b) 2  c) broken d) 3 e) This code won't execute

# In[ ]:


if 10%2 == 5:
    print('1')
elif True and False or False:
    print('2')
elif 5/0:
    print('broken')
else:
    print('3')


# ## Functions & Algorithms

# ### Functions 1
# 
# What will the following piece of code print out?

# In[ ]:


def manipulate_three(num1, num2, num3):

    answer = num1**num2%num3

    return answer

manipulate_three(3, 2, 5)


# ### Functions 2
# 
# What will the following code print: 
# 
# A) 'a'	B) 'A'	C) `dictionary`	D) ' ' (string with space)	E) '' (empty string)

# In[ ]:


def char_manipulator(char):
    
    dictionary = {
        'a' : 'A',
        'e' : 'E',
        'i' : 'I',
        'o' : 'O',
        'u' : 'U'
     }
    
    if char in dictionary:
        output = dictionary[char]
    else:
        output = char
    
    return output

variable = 'a'
manipulated_char = char_manipulator(variable)
print(manipulated_char)

