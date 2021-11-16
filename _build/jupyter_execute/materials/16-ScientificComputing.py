#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# **Due Dates**
# - **CL8** now available; due Wednesday - this is your final CL to submit
# - **A5** now available; due Friday of week 10 (12/3) - canvas/syllabus have been updated
# - **Final exam/project** due Mon of Finals week (12/6; 11:59 PM)
# 
# **Notes**
# - CL7 scores posted 
# - E2 scores to be finalized posted (hopefully) later today; tomorrow at latest; will discuss in class Wed.
# - No class, office hours, or coding lab next Wed-Fri
# - Final Exam will be released Friday afternoon of week 10

# **Q&A**
# 
# Q: Will the final exam be analogous to an assignment in which were instructed how to make chat bots etc.  
# A: The final exam wil be similar to an assignment; however, there will be additional files involved (module, test file, etc.) to focus on what we're discussing these final weeks in the course.
# 
# Q: Are we allowed to use certain dictionaries defined online? For example, if we want a dictionary of all the nba players, would it be ok to just copy and paste one online?  
# A: Yes, but you must cite where it came from (i.e. provide the URL to the original data)
# 
# Q: Could I make a short questionnaire of questions for my final project?  
# A: Yes
# 
# Q: If I’m only semi-confident with my project but also semi-confident in the exam, what questions should I ask myself to see which one I should go for if I have the same level of confidence for each?  
# A: Give the project a go now and see if you can do it! 
# 
# Q: Will we be able to schedule one-on-one meetings with Professor Ellis or the TAs for help with the final project?  
# A: Office hours and coding lab week 10 will be the best place for questions. Prof Ellis will likely hold some appt. only 10min meetings right before the deadline for last minute questions. Staff are not required to hold additional office hours, but some may choose to do so.
# 
# Q: What is the average score for the people who choose to do the project? I'm not very confident in my coding abilities, and I don't know if its worth me stressing over not how to do the project. I just want to choose the option that will set me up for success.  
# A: The project average tends to be quite high (~90); the exam tends to be slightly lower than that (~85), but remember that many of the students who are more comfortable with the material choose the project.
# 
# Q: I want to make sure that the project like the assignments we will get 100% as long as we complete all of the parameters. I know the projects presented today were advanced but I am wondering if i do the 3/3 methods etc.. (i forget the rubric but whatever it says there) will i get full points?  
# A: Yup - even if it's simple, you can get full credit.
# 
# Q: What is the main purpose of importing modules?  
# A: To give you access to additional functionality without having to write all the code yourself.
# 
# Q: Are the TA's/IA's and professor able to help with coding issues for the project? As in helping the student figure out how to fix a particular issue with their code?   
# A: Yup.
# 
# Q: is a folder on datahub the same as creating a new directory?  
# A: Yes.
# 
# Q: For the final Project, do we have to get the project running or can we try our best to create this 'project'?  
# A: A non-functioning project will get some but not all credit.
# 
# Q: I can’t find artificial agents lecture   
# A: There was no artificial agents lecture. Classes are what A5 focuses on.
# 
# Q: Can we do the exam and the project?  
# A: Yes, but you can only submit one. If you submit both, I will post the lower score as your final grade (we have a LOT of grading to do, thus this policy).
# 
# Q: Will there be a rubric for the project? Is there a set amount of tasks our code needs to run?  
# A: See overview/project documentation provided.
# 
# Q: I am unsure about to the extent students can work together on the project. If a friend and I have totally different projects, but I have a question about a part of my code, am I allowed to discuss with my friend?   
# A: Yup!
# 
# Q: Just wanted to confirm, as written in the overview file, we need to comment that if our codes are from the Internet and student cooperation. So do we have to write comments for the codes from our homework?  
# A: Yes if from the internet; no if from the homework.
# 
# Q: If these homework codes were once written by ourselves, would they be graded?  
# A: Not if we told you what to write. These original functions must be designed and written by you.
# 
# Q: I intend to choose the Encryption project, and we are required to integrate the email function by Python. Currently, I have implemented it and modified some basic codes by constructing a class. However, most codes are nearly the same in this kind of email function, and we haven't learned it; we have to learn it by ourselves and then imitate the codes. So assume we modified and understood the codes, do we still have to annotate that these codes are cited, and will they be graded?  
# A: I'm not sure I understand - let's discuss in office hours?
# 
# Q: You mentioned that students will loose access to the class material after the course is over. Is there a way that students can import all of the class materials into Anaconda so we can use them for future reference?  
# A: Yes! I will post a how to video on campuswire at the end of the course to get everything off of datahub.

# # Scientific Computing

# <div class="alert alert-success">
# <b>Scientific Computing</b> is the application of computer programming to scientific applications: data analysis, simulation & modelling, plotting, etc. 
# </div>

# ## Scientific Python: Scipy Stack
# 
# Scipy = Scientific Python
# 
# - `scipy`
# - `numpy`
# - `pandas`
# - Data Analysis in Python

# <div class="alert alert-success">
# <b><code>Scipy</code></b> is an <i>ecosystem</i>, including a collection of open-source packages for scientific computing in Python.
# </div>

# A 'family' of packages that all work well together to do scientific computing.
# 
# Not made by the same people who manage the standard library.

# ## Homogenous Data
# 
# - for example: store data of the same type (i.e. all numerics)
# - recordings of values from experimental participants
# - heights or quantitative information from survey data

# Lists are a start, and lists of lists are possible.
# 
# But, they can get nightmareish.
# 
# So we use arrays.

# ### `numpy`
# 
# **`numpy`** - stands for numerical python

# **arrays** - work with arrays (matrices)
# 
# Allow you to efficiently operate on arrays (linear algebra, matrix operations, etc.)

# In[5]:


import numpy as np


# In[2]:


# Create some arrays of data
arr0 = np.array([1, 2, 3])
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])


# In[5]:


arr2


# In[6]:


# lists of lists don't store dimensionality well
[[1, 2], [3, 4]] 


# #### Arrays: attributes, methods, & indexing

# In[7]:


# Check out an array of data
arr1


# `numpy` arrays are an object type...so they have associated attributes (below) and methods (we'll get to these in a second)!

# In[8]:


# Check the shape of the array
arr1.shape


# In[9]:


# Index into a numpy array
arr1[0, 0]


# Working with N-dimensional (multidimensional) arrays is easy within `numpy`.

# #### Notes on Arrays

# In[10]:


# arrays are most helpful when they
# have the same length in each list
np.array([[1, 2, 3, 4], [2, 3, 4]])


# In[11]:


# arrays are meant to store homogeneous data
np.array([[1, 2, 'cogs18'], [2, 3, 4]])


# #### Working with Arrays
# 
# (Things you can't do with lists)

# In[12]:


# Add arrays together
arr1 + arr2


# In[13]:


# Matrix mutliplication
arr1 * arr2


# #### A brief aside: `zip()`

# `zip()` takes two iterables (things you can loop over) and loop over them together.

# In[14]:


for a, b in zip([1,2], ['a','b']):
    print(a, b)


# #### Clicker Question #1
# 
# Given the following code, what will it print out?

# In[15]:


data = np.array([[1, 2, 3, 4], 
                 [5, 6, 7, 8]])
 
output = []
for d1, d2 in zip(data[0, :], data[1, :]):
    output.append(d1 + d2)

print(output)


# - A) [1, 2, 3, 4]
# - B) [1, 2, 3, 4, 5, 6, 7, 8]
# - C) [6, 8, 10, 12]
# - D) [10, 26]
# - E) [36]

# Note that if you find yourself looping over arrays...there is probably a better way.

# In[16]:


# sum method
# by default sums all values in array
data.sum()


# In[17]:


# sum method
# has an axis parameter
# axis=0 sums across columns
data.sum(axis=0)


# In[18]:


# typecasting to a different variable type
out_list = data.sum(axis=0).tolist()
print(out_list)
type(out_list)


# What if you wanted to find the max value in an array...there's a method for that!

# In[19]:


# find max value in array
max_val = data.max()
max_val


# But what if you wanted to know not what the max value was...but where in your original array that value was found. 
# 
# There are also *functions* in `numpy` that operate on arrays. 

# In[20]:


# see documentation for np.where()
get_ipython().run_line_magic('pinfo', 'np.where')


# In[21]:


# find position in array with max value
out = np.where(data == max_val)
out


# In[23]:


data


# In[22]:


# check to be sure
data[1,3]


# ## Heterogenous Data
# 
# - have continuous (numeric) and categorical (discrete) data
# - different data types need to be stored
# - uses a DataFrame object (think: spreadsheet)
# - allows for column and row labels

# ### pandas

# Pandas is Python library for managing heterogenous data.
# 
# At it's core, Pandas is built around the **DataFrame** object, which is:
# - a data structure for labeled rows and columns of data
# - associated methods and utilities for working with data.
# - each column contains a `pandas` **Series**

# In[6]:


import pandas as pd


# In[25]:


# Create some example heterogenous data
d1 = {'Subj_ID': '001', 'score': 16, 'group' : 2, 'condition': 'cognition'}
d2 = {'Subj_ID': '002', 'score': 22, 'group' : 1, 'condition': 'perception'}
d3 = {'Subj_ID': '003', 'score': 18, 'group' : 1, 'condition': 'perception'}


# In[26]:


# Create a dataframe 
df = pd.DataFrame([d1, d2, d3], [0, 1, 2])


# In[27]:


# Check out the dataframe
df


# In[28]:


# You can index in pandas
# columns store information in series
df['condition']


# In[29]:


# You can index in pandas
# loc specifies row, column position
df.loc[0,:]


# In[30]:


# attribute of df object
# row, columns
df.shape


# #### Working with DataFrames
# 
# There are *a lot* of functions and methods within `pandas`. The general syntax is `df.method()` where the `method()` operates directly on the dataframe `df`.

# In[31]:


# calculate summary statistics
df.describe()


# In[34]:


# Take the average of all numeric columns
df.mean()


# In[35]:


# breakdown of how many of each category there are
val_counts = df['condition'].value_counts()
val_counts


# In[36]:


# which unique values are there in condition? 
df['condition'].unique()


# In[37]:


# how many unique values are there
len(df['condition'].unique())
# equivalent to
df['condition'].nunique()


# In[38]:


# how many rows there are in a series/df
len(df)


# In[39]:


# what's the category that shows up the most 
val_counts.idxmax()


# In[40]:


# what's the count of the value that shows up the most
val_counts.max()


# #### Clicker Question #2
# 
# Comparing them to standard library Python types, which is the best mapping for these new data types?
# 
# - A) DataFrames are like lists, arrays are like tuples
# - B) DataFrames and arrays are like lists
# - C) DataFrames are like tuples, arrays are like lists
# - D) DataFrames and arrays are like dictionaries
# - E) Dataframes are like dictionaries, arrays are like lists

# ## Plotting

# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt


# In[42]:


# Create some data
dat = np.array([1, 2, 4, 8, 16, 32])


# In[45]:


# Plot the data
plt.plot(dat);


# - can change plot type
# - _lots_ of customizations possible

# ## Analysis
# 
# - `scipy` - statistical analysis
# - `sklearn` - machine learning

# In[47]:


get_ipython().system('pip install --user scipy')


# In[1]:


import scipy as sp
from scipy import stats


# In[2]:


# Simulate some data
d1 = stats.norm.rvs(loc=0, size=1000)
d2 = stats.norm.rvs(loc=0.5, size=1000)


# ### Analysis - Plotting the Data

# In[7]:


# Plot the data
plt.hist(d1, 25, alpha=0.6);
plt.hist(d2, 25, alpha=0.6);


# ### Analysis - Statistical Comparisons

# In[8]:


# Statistically compare the two distributions
stats.ttest_ind(d1, d2)


# ## COGS 108: Data Science in Practice

# <div class="alert alert-info">
# If you are interested in data science and scientific computing in Python, consider taking <b>COGS 108</b> : <a>https://github.com/COGS108/</a>.
# </div>
