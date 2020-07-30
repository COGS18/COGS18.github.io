---
interact_link: content/labs/source_Su20/CL5-Answers.ipynb
download_link: assets/downloads/CL5-Answers.ipynb.zip
title: 'CL5-Answers'
prev_page:
  url: /labs/source_Su20/CL4-Answers
  title: 'CL4-Answers'
next_page:
  url: /
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# CL5: Command Line

Welcome to the fifth coding lab!

In this CodingLab we will be working with the command line, and with python files (module files and scripts). 

While this _may_ feel like busy work, understanding and completing this coding lab will be essential when it comes time for your final exam and future coding projects. Do your very best to complete all parts of this CodingLab!

## Part I: Command Line

Open a terminal from the Jupyter notebook server (either on your local computer or datahub), and do the following:

- Navigate to your desktop (or home directory on datahub)
- Make a new directory
- Move inside that directory
- Create a new Python file
- Open the file you just created
- Write some Python code inside that file
    - For example: print('Hello World')
- Save and exit from the text editor
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



{:.input_area}
```python
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
```




{:.input_area}
```python
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
```


Dustin then stored two files in the same folder as their notebook:
- `cravings.py` : stored `Noodles`, `Ramen`, `eating`, and `soup`
- This whole module is imported and used below
- The cells below will not run if you don't create the module with the same name

Next, we are going to move this code to an external file - a Python module file. 

- Open a new text file, from the Jupyter server page
- Copy your classes and functions into that file
- Save that file, with some name that you give it, and a '.py' extension
- Now, import the classes and functions from that file into the notebook, and check that you can use them. 



{:.input_area}
```python
import cravings as crave

tonkotsu = crave.Ramen()
print(crave.eating(tonkotsu))
print(crave.soup(tonkotsu))
```


{:.output_stream}
```
Slurp slurp slurp, delicious!

Should I drink the soup?
	I really shouldn't... There's too much sodium.

```

## Part III: Tests

Now write a test file that imports from your module file, and tests the functions/classes. (Refer back to testing lecture if you need to refresh your memory.)

To do so, start with the new text file. It should import your classes and functions from the file you made above. Then, write a test function (`test_...`) for each function and class. Remember these should contain `assert` statements and test the behavior of your functions. Save your file with a '.py' extension, and then use `pytest` to execute it from the terminal.

The code below has been stored in a file called `test_cravings.py`:



{:.input_area}
```python
import cravings as crave

def test_Noodles():
    # test default values
    tonkotsu = crave.Noodles()
    assert tonkotsu.available == None
    assert tonkotsu.size == None   
    assert tonkotsu.order_to_go() == "I'm sorry, but we aren't taking to-go orders right now."
    
def test_Ramen():
    # test default values
    tonkotsu = crave.Ramen()
    assert tonkotsu.available == "Yes"
    assert tonkotsu.size == "large"    
    assert tonkotsu.order_to_go() == "I'll have your order ready in 20 minutes"
    
    # test other values
    ramen_small = crave.Ramen(size='small', available=None)
    assert ramen_small.size == 'small'
    assert ramen_small.available == None
    assert ramen_small.order_to_go() == "I'm sorry, but we aren't taking to-go orders right now."

def test_eating():
    tonkotsu = crave.Ramen()
    ramen_small = crave.Ramen(size='small', available=None)

    assert crave.eating(tonkotsu) == 'Slurp slurp slurp, delicious!'
    assert crave.eating(ramen_small) == 'Quarantine can be rough. It be like that sometimes.'
    
def test_soup():
    tonkotsu = crave.Ramen()
    ramen_small = crave.Ramen(size='small', available=None)

    assert crave.soup(tonkotsu) == "\n" + 'Should I drink the soup?' + "\n\t" + "I really shouldn't... There's too much sodium."
    assert crave.soup(ramen_small) == "\n" + 'Should I drink the soup?' + "\n\t" + "You only live once! Slurp slurp slurp!"
    
```




{:.input_area}
```python
!pytest test_cravings.py
```


{:.output_stream}
```
[1m============================= test session starts ==============================[0m
platform darwin -- Python 3.7.0, pytest-3.8.0, py-1.6.0, pluggy-0.7.1
hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/Users/shannonellis/Desktop/Teaching/COGS18/CodingLabs/source_Su20/.hypothesis/examples')
rootdir: /Users/shannonellis/Desktop/Teaching/COGS18/CodingLabs/source_Su20, inifile:
plugins: remotedata-0.3.0, openfiles-0.3.0, doctestplus-0.1.3, astropy-header-0.1.1, arraydiff-0.2, hypothesis-4.36.2
collected 4 items                                                              [0m[1m

test_cravings.py ....[36m                                                    [100%][0m

[32m[1m=========================== 4 passed in 0.05 seconds ===========================[0m

```

Explain your success/struggles/failures with the above here:

## Part IV: Python Scripts

Now write a small script that imports from your module file, and uses that code to do something.

To do so, start with the new text file. It should import your classes and functions from the file you made above. Then, use these functions and classes to do something (write some Python code that does something with these objects). Save your file with a '.py' extension, and then execute it from the terminal.

I've stored the following few lines of code in a file called `cravings_script.py`:



{:.input_area}
```python
import cravings as crave

tonkotsu = crave.Ramen()
print(crave.eating(tonkotsu))
print(crave.soup(tonkotsu))
```




{:.input_area}
```python
# execute script
!python cravings_script.py
```


{:.output_stream}
```
Itadakimasu
Slurp slurp slurp, delicious!

Should I drink the soup?
	I really shouldn't... There's too much sodium.

```

Explain your success/struggles/failures with the above here:

## The End!

This is the end of this Coding Lab!

Be sure you've made a concerted effort to complete all the tasks specified in this lab. Then, go ahead and submit on datahub!
