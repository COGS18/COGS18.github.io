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

### Student Example: Dustin Doan 

(slightly modified by Prof Ellis)

# Classes here
class Noodles():
    def __init__(self, size = None, available = None):
        self.size = size
        self.available = available
        
    def order_to_go(self):
        if self.available == None:
            out = "I'm sorry, but we aren't taking to-go orders right now."
        if self.available == 'Yes':
             out = "I'll have your order ready in 20 minutes"
        return out
    
class Ramen(Noodles):
    def __init__(self, size = 'large', available = 'Yes'):
        super().__init__(size, available)

# new functions here
def eating(Ramen):
    if Ramen.available == 'Yes':
        print('Itadakimasu') # means "I will receive"; something you say before eating
        out = 'Slurp slurp slurp, delicious!'
    else:
        out = 'Quarantine can be rough. It be like that sometimes.'
    return out

def soup(Ramen):
    if Ramen.size == 'large':
        out = "\n" + 'Should I drink the soup?' + "\n\t" + "I really shouldn't... There's too much sodium."
    if Ramen.size != 'large':
        out = "\n" + 'Should I drink the soup?' + "\n\t" + "You only live once! Slurp slurp slurp!"
    return out

Dustin then stored two files in the same folder as their notebook:
- `cravings.py` : stored `Noodles`, `Ramen`, `eating`, and `soup`
- This whole module is imported and used below
- The cells below will not run if you don't create the module with the same name

Next, we are going to move this code to an external file - a Python module file. 

- Open a new text file, from the Jupyter server page
- Copy your classes and functions into that file
- Save that file, with some name that you give it, and a '.py' extension
- Now, import the classes and functions from that file into the notebook, and check that you can use them. 

import cravings as crave

tonkotsu = crave.Ramen()
print(crave.eating(tonkotsu))
print(crave.soup(tonkotsu))

## Part III: Python Scripts

Now write a small script that imports from your module file, and uses that code to do something.

To do so, start with the new text file. It should import your classes and functions from the file you made above. Then, use these functions and classes to do something (write some Python code that does something with these objects). Save your file with a '.py' extension, and then execute it from the terminal.

I've stored the following few lines of code in a file called `cravings_script.py`:

import cravings as crave

tonkotsu = crave.Ramen()
print(crave.eating(tonkotsu))
print(crave.soup(tonkotsu))

# execute script
!python cravings_script.py

Explain your success/struggles/failures with the above here: