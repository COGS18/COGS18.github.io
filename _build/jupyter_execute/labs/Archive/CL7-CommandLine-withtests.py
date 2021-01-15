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
- Open the file (this may be from the Files tab on datahub)
- Write some Python code inside that file
    - For example: print('Hello World')
- Save the file (and return to the terminal
- Execute the Python file from the terminal

Describe your success/struggles/failures with the above steps here:


## Part II: Module Files

First, in notebook below, do the following:

- Write a new Class, and two derived classes that inherit from this base Class
    - This could be, for example, base class `Animal` and derived classes `Cat` and `Dog`
    - Make sure there is at least one method in the class that prints something out
- Write two new functions, that do something with instances of your new classes
    - For example, take a list of custom objects, and call a method on each one

# Class here

### BEGIN SOLUTION

### END SOLUTION

# new functions here

### BEGIN SOLUTION

### END SOLUTION

Next, we are going to move this code to an external file - a Python module file. 

- Open a new text file, from the Jupyter server page
- Copy your classes and functions into that file
- Save that file, with some name that you give it, and a '.py' extension
- Now, import the classes and functions from that file into the notebook, and check that you can use them. 

import ...

### BEGIN SOLUTION

### END SOLUTION

## Part III: Tests

Now write a test file that imports from your module file, and tests the functions/classes. (Refer back to testing lecture if you need to refresh your memory.)

To do so, start with the new text file. It should import your classes and functions from the file you made above. Then, write a test function (`test_...`) for each function and class. Remember these should contain `assert` statements and test the behavior of your functions. Save your file with a '.py' extension, and then use `pytest` to execute it from the terminal.

Explain your success/struggles/failures with the above here:

## Part IV: Python Scripts

Now write a small script that imports from your module file, and uses that code to do something.

To do so, start with the new text file. It should import your classes and functions from the file you made above. Then, use these functions and classes to do something (write some Python code that does something with these objects). Save your file with a '.py' extension, and then execute it from the terminal.

Explain your success/struggles/failures with the above here:

## The End!

This is the end of this Coding Lab!

Be sure you've made a concerted effort to complete all the tasks specified in this lab. Then, go ahead and submit on datahub!