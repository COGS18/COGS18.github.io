#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - E2 due this morning (8AM) - be sure you clicked submit 
# - CL7 due Wednesday (11:59 PM)
# - A4 due Friday (11:59 PM)
# - We'll start discussing the final project/exam on Friday

# **Q&A**
# 
# Q: Will the final also be take home like the other exams?  
# A: Yes
# 
# Q: I'm curious about what is python party on next Mon.  
# A: This will be when we discuss the final project/exam. Because we're a bit behind, this will be this coming Friday.
# 
# Q: Will there be any more extra credit options available later after E2?  
# A: Yes. Final course-survey. CAPEs. Extra credit on the final project. Continued extra credit on daily participation.
# 
# Q: I am curious about if you can put a class inside a class and if that would be useful or convoluted.  
# A: Yes, theoretically you could....however, there's actually a concept called inheritance. We don't discuss that in this course, but this would be what to look up if you're curious! 
# 
# Q: I'm still not sure when to use def  
# A: Any time you want to define a function or a method.
# 
# Q: will the exam or the class be curved?  
# A: Typically, no neither is.

# # Command Line
# 
# - command line & shell commands
# - file paths (absolute and relative)
# - scripts and modules

# Jupyter Notebooks are a helpful tool, but they're _bulky_.

# ## File Systems

# <div class="alert alert-success">
# Computers use a hierarchical file systems that organizes files & folders.
# </div>

# When you click through the folders (directories) on your computer, you're interacting with this hierarchical system.

# ## Command Line

# <div class="alert alert-success">
# A <b>command line interface</b> is a way to interact with a computer through written commands.
# </div>

# The command line allows us to:
# 
# - create files
# - edit files
# - run python scripts
# - etc.
# 
# ...without clicking on anything.

# ### The Terminal
# 
# The **terminal** is where you can type these commands into the command line.
# 
# Accessing the terminal...
# 
# - possible on your computer
# - and on datahub

# ### Shell Commands
# 
# ...can be run in the terminal _and_ Jupyter notebooks
# 
# Do this by starting with `!`

# #### Check current directory

# In[1]:


# print working directory
get_ipython().system('pwd')


# ## An important aside: File Paths

# <div class="alert alert-success">
# The specific location of a file or folder on your computer. </div>

# When using a Graphical User Interface (GUI), you click on directories to access subdirectories and finally find the file you're interested in.

# When using the command line, you specify a file's path explicitly with text. 

# ### Absolute vs. Relative Paths
# 
# The two ways to specify the path to your file of interest allow for flexibility in programming.

# #### Absolute Paths

# <div class="alert alert-success">
# <b>Absolute paths</b> specify the <b>full</b> path for a given file system (starting from the root directory). 
# </div>

# **root** specifies the 'highest' directory in the file structure (the start).
# 
# An absolute file path starts with a slash `/` specifying the root directory.
# 

# In[2]:


## absolute path
## this is specific to my computer
## look at the path output above for you computer
get_ipython().system('ls /Users/shannonellis/Desktop/Teaching/COGS18/Materials')


# #### Relative Paths

# <div class="alert alert-success">
# <b>Relative paths</b> specify the path to a file from your <b>current working directory</b> (where your computer is working right now). 
# </div>

# In[3]:


# remind us of our current working directory
get_ipython().system('pwd')


# In[4]:


# relative path
# this is specific to my computer
get_ipython().system('ls ../../COGS108/Lectures-Wi21')


# 
# - `..` specify you want to move one directory up in your hierarchy
# - `COGS108/Lectures-Fa20` specifies the path to the directory I want to list files in
# - each directory is separated with a slash (`/`)

# This **relative** path does _not_ start with a leading slash (b/c it's not an absolute path).

# #### Clicker Question #1
# 
# Given the following file structure: 
# 
# - `/`
#     - `scripts/`
#         - cool_thing.py
#         - super_cool_thing.py
#     - `images/`
#         - image1.png
#         - image2.png
#     - `notebooks/`
#         - 00_intro.ipynb
#         - 01_variables.ipynb
#     
# 
# If your current working directory is `notebooks`, what is the **absolute path** to `cool_thing.py`?
# 
# - A) `/scripts/cool_thing.py`
# - B) `scripts/cool_thing.py`
# - C) `cool_thing.py`
# - D) `../scripts/cool_thing.py`
# - E) ¯\\\_(ツ)\_/¯

# #### Clicker Question #2
# 
# Given the same file structure: 
# 
# - `/`
#     - `scripts/`
#         - cool_thing.py
#         - super_cool_thing.py
#     - `images/`
#         - image1.png
#         - image2.png
#     - `notebooks/`
#         - 00_intro.ipynb
#         - 01_variables.ipynb
#     
# 
# If your current working directory is `notebooks`, what is the **relative path** to `cool_thing.py`?
# 
# - A) `/notebooks/../scripts/cool_thing.py`
# - B) `scripts/cool_thing.py`
# - C) `/scripts/cool_thing.py`
# - D) `../scripts/cool_thing.py`
# - E) ¯\\\_(ツ)\_/¯

# ### Shell Commands
# 
# ...can be run in the terminal _and_ Jupyter notebooks

# #### Check current directory

# In[5]:


# print working directory
get_ipython().system('pwd')


# #### Change directory

# In[ ]:


# change directory 
get_ipython().system('cd ~/ ')


# Here, we saw `~/`. 
# 
# - `~` specifies the user's home directory of your computer
# - each directory is separated with a slash (`/`)

# #### List files in a directory

# In[6]:


# list files (list segments)
get_ipython().system('ls')


# ### More Shell Commands

# #### Make a new directory

# In[7]:


# make directory 
get_ipython().system('mkdir dir_name')


# #### Create a file

# In[8]:


# create an empty file
get_ipython().system('touch new_file.py ')


# #### Move a file

# In[9]:


# move file
# notice the relative file path
get_ipython().system('mv new_file.py dir_name/')


# ### And Some More

# #### Print out a message

# In[10]:


get_ipython().system('echo Hello World!')


# #### Print the contents of a file

# In[11]:


get_ipython().system('cat dir_name/new_file.py')


# #### Open to see and edit contents of a file

# In[ ]:


# will not work on datahub
get_ipython().system('open dir_name/new_file.py')


# #### Clicker Question #3
# 
# Which is the best description of the following command:
#     
# `ls -l`
# 
# - A) `ls -l` is most analogous to a class in Python
# - B) The whole `ls -l` is like a function call
# - C) `-l` is analogous to a function call, and `ls` is like a parameter
# - D) `ls` is analogous to a function, and `-l` is like a parameter
# - E) There is no clear analogy here to Python

# In[12]:


## test out here
get_ipython().system('ls -l')


# #### Clicker Question #4
# 
# Which creates a file?     
#    
# - A) `mkdir`
# - B) `pwd`
# - C) `cd`
# - D) `touch`
# - E) `cat`

# ## Windows Command Prompt
# 
# Some commands are slightly different if you are using windows command prompt:
# 
# - `dir` : lists files in current directory
# - `move` : moves a file
# - `copy` : copies a file
# - `rename` : renames a file
# - `type` : can be used to print out a file
#     
# Note that `pwd`, `cd`, `mkdir`, `echo` are all the same in Windows command prompt.
# 
# If you want to make a new empty file, you can do:
# 
# `'' > my_file.py`
# 
# ^This construction puts an empty string into a file. If the filename is not found, it will create a new (empty) file.

# ## Python Files

# <div class="alert alert-success">
# Python files are plain-text files, with Python code in them, that can be executed and/or imported from.
# </div>

# ### Script vs. Module File

# ### Scripts

# <div class="alert alert-success">
# A <b>script</b> is a Python file that can be run to execute a particular task. 
# </div>

# ### Module Files

# <div class="alert alert-success">
# A <b>module</b> file is a file with Python code (typically functions & classes) that we can import and use.
# </div>

# Remember: if you're writing code, you cannot just click through to the file you want. You need to specify _using code_ where the file you want is. 
# 
# This is where understanding file paths is critically important.

# ## Text Editors

# <div class="alert alert-success">
# Text-editors are programs made for editing text. Many text-editors are designed for writing code specifically. 
# </div>

# ### Terminal Based Text Editors
# 
# There are text editors designed to be used within a terminal, such as `vim`, `emacs`, or `nano`. 

# #### vim
# 
# `vim` is a terminal based text-editor. Type `vim filename` in command line to open a file in vim. 
# 
# `vim` has different modes:
# 
# - click `escape` + `i` to enter edit mode (insert mode). 
#     - This will let you write text / code into the file
# - To escape vim, press `escape` then type `:wq` and enter to save and quit vim
#     - If you want to exit without saving, you can do `:!q` to force quit without saving

# ### Non-Terminal Text Editors
# 
# For writing code (outside of notebooks and the terminal), you probably want a code focused stand-alone text editor, like `Sublime`.

# ## Executing Python Files

# From the command line, you can execute a Python script using the `python` command:
# 
# `python dir_name/new_file.py`

# #### Clicker Question #5
# 
# To create a file and see its contents, which command line commands would you use (and in which order)?    
#    
# - A) `mkdir` > `cd`
# - B) `pwd` > `ls`
# - C) `cd` > `pwd`
# - D) `touch` > `cat`
# - E) `cat` > `touch`

# #### Clicker Question #6
# 
# Given the file structure from earlier: 
# 
# - `/`
#     - `scripts/`
#         - cool_thing.py
#         - super_cool_thing.py
#     - `images/`
#         - image1.png
#         - image2.png
#     - `notebooks/`
#         - 00_intro.ipynb
#         - 01_variables.ipynb
# 
# Your currently working within `notebooks` and you want to execute the code in 'cool_thing.py' from the command line. How would you do that?
# 
# 
# - A) `python cool_thing.py` 
# - B) `python ../notebooks/cool_thing.py` 
# - C) `python ../scripts/cool_thing.py` 
# - D) `python ../cool_thing.py` 
# - E) ¯\\\_(ツ)\_/¯ 
