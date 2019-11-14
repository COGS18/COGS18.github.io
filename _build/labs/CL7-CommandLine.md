---
interact_link: content/labs/CL7-CommandLine.ipynb
download_link: assets/downloads/CL7-CommandLine.ipynb.zip
layout: notebooks
title: 'CL7-CommandLine'
prev_page:
  url: /labs/CL6B-Answers
  title: 'CL6B-Answers'
next_page:
  url: /projects/ProjectIdeas
  title: 'Projects'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# CL7: Command Line

Welcome to the seventh coding lab!

In this CodingLab we will be working with the command line, and with python files (module files and scripts). 

While this _may_ feel like busy work, understanding and completing this coding lab will be essential when it comes time for your project. Do your very best to complete all parts of this CodingLab!

## Part I: Command Line

Open a terminal from the Jupyter notebook server (either on your local computer or datahub), and do the following:

- Navigate to your desktop (or home directory on datahub)
- Make a new directory
- Move inside that directory
- Create a new Python file
- Inside your terminal, use a text editor to open the file
- Write some Python code inside that file
    - For example: print('Hello World')
- Save and exit from the terminal text editor
- Execute the Python file from the terminal

## Part II: Module Files

First, in notebook below, do the following:

- Write a new Class, and two derived classes that inherit from this base Class
    - This could be, for example, base class `Animal` and derived classes `Cat` and `Dog`
    - Make sure there is at least one method in the class that prints something out
- Write two new functions, that do something with instances of your new classes
    - For example, take a list of custom objects, and call a method on each one



{:.input_area}
```python
# YOUR CODE HERE
```


Next, we are going to move this code to an external file - a Python module file. 

- Open a new text file, from the Jupyter server page
- Copy your classes and functions into that file
- Save that file, with some name that you give it, and a '.py' extension
- Now, import the classes and functions from that file into the notebook, and check that you can use them. 



{:.input_area}
```python
# YOUR CODE HERE
import ...
```


## Part III: Python Scripts

Now write a small script that imports from your module file, and uses that code to do something.

To do so, start with the new text file. It should import your classes and functions from the file you made above. Then, use these functions and classes to do something (write some Python code that does something with these objects). Save your file with a '.py' extension, and then execute it from the terminal.
