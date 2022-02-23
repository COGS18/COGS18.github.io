#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - **A4** due Mon 2/28 (11:59 PM)
# - **CL7** due *next* Wednesday (3/2) - Coding Labs *are* happening today; will use same CL7 for two weeks
# 
# 
# **Notes**
# - Prof Ellis' OH:
#     - today: **in-person; new location** due to weather: **CSB 243** (9:30-10:30)
#     - extra **zoom office hours this Friday 9-10 AM** (will use normal zoom link on canvas; make-up for Monday)
# - **CL6** scores posted (Reminder to check CL6 answer key)
# 

# **Q&A**
# 
# Q: I was confused on why we don't include return statements sometimes when we have functions. I did not really understand why we don't include it, especially when we did the Todo example in class. I'm guessing that if the instructions don't say to include a return statement then we don't include it. I'm just confused on why that is.   
# A: In Clases, if you're updating the value for an attribute of that class, then you don't have to `return` it. When you want to return a variable from a function/method directly, you'll always need a `return`.
# 
# Q: I was looking at the grade book and was confused about what the GitHub Extra Credit is. Have we not learned about that yet, or am I missing something?  
# A: You have not learned about this yet; will be discussed Friday when we discuss the final project/exam.
# 
# Q: Can there be classes inside classes?  
# A: Theoretically, yes. In practice, no, that's not good practice. Rather, you would use what's known as "Class Inheritance" to *inherit* the properties from another class. We will not get to this concept this quarter.
# 
# Q: Since we were on the topic of exams, I wanted to know when we would be disclosed information regarding the final project for the class?   
# A: This Friday we'll discuss in detail!
# 
# Q: Do we put self for every method in class?  
# A: As the first parameter? Yes. 
# 
# Q: what does it mean when you run a class cell and it prints something like this : <__main__. object at 0x7f27d1802fd0>  
# A: That you've printed out the object...but haven't asked for any attributes from it/executed any methods on that object.
# 
# Q: how do you loop through a list and do replacing in checking if something is in the list wantted to be remove?  
# A: There is a `remove()` list method.
# 
# Q: I am still a little confused about coding style for classes. Is the only difference when defining the class. For example, the name of the class needing to be like this 'ClassName'.   
# A: That is the main one...the other is extra line spaces between attributes and methods.
# 
# Q: For the comparison example, why is it fewest = self.courses[0] since we aren't looking for the full dictionary instead we are looking for a specific value? Why is fewest not equal to the my_course[attribute] directly?  
# A: Because in this one, I ultimately decided I wanted to return the whole dictionary, determined by the value for a specific attribute. If you only wanted to return the value, you could do what you're suggesting.
# 
# Q: how many coding labs are left this quarter?  
# A: There will be two to complete: CL7 and CL8. Everyone will receive full credit on CL9; there will be nothing to turn in.
# 
# 
# Q: When we define a class that has more than 1 method, can we put a return statement for each method or does it have to be 1 return statement at the end of the class?  
# A: Each method could have its own `return` statement.

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

# In[ ]:


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

# In[1]:


## absolute path
## this is specific to my computer
## look at the path output above for you computer
get_ipython().system('ls /Users/shannonellis/Desktop/Teaching/COGS18/LectureNotes-COGS18')


# #### Relative Paths

# <div class="alert alert-success">
# <b>Relative paths</b> specify the path to a file from your <b>current working directory</b> (where your computer is working right now). 
# </div>

# In[ ]:


# remind us of our current working directory
get_ipython().system('pwd')


# In[3]:


# relative path
# this is specific to my computer
get_ipython().system('ls ../../COGS108')


# 
# - `..` specify you want to move one directory up in your hierarchy
# - `COGS108/` specifies the path to the directory I want to list files in
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

# In[ ]:


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

# In[ ]:


# list files (list segments)
get_ipython().system('ls')


# ### More Shell Commands

# #### Make a new directory

# In[ ]:


# make directory 
get_ipython().system('mkdir dir_name')


# #### Create a file

# In[ ]:


# create an empty file
get_ipython().system('touch new_file.py ')


# #### Move a file

# In[ ]:


# move file
# notice the relative file path
get_ipython().system('mv new_file.py dir_name/')


# ### And Some More

# #### Print out a message

# In[ ]:


get_ipython().system('echo Hello World!')


# #### Print the contents of a file

# In[ ]:


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

# In[ ]:


## test out here


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
