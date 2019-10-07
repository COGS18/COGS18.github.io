---
interact_link: content/labs/CL1-Tooling.ipynb
download_link: assets/downloads/CL1-Tooling.ipynb.zip
layout: notebooks
title: 'Coding Labs'
prev_page:
  url: /materials/04-Operators
  title: '04-Operators'
next_page:
  url: /labs/CL1-Tooling
  title: 'CL1-Tooling'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Coding Lab 1: Tech Setup & Tooling

Welcome to the first coding lab!

CodingLab labs are meant to be interactive - so most weeks, feel free to find another person to work together with on your CodingLab notebooks. 

For this lab, however, it's really important that you're comfortable with all of the tools we introduce here, as we'll be using them throughout the quarter. So, while you should feel free to consult with your classmates, you'll want to be sure you carry out each part on your own. 

If you have a question about how something works / what something does - try it out, and see what happens! If you get stuck, consult your classmates. If you're still stuck, your instructional staff are there to help!

## Part 1: Jupyter

This is a Jupyter Notebook! They are a very helpful learning tool because they allow plain text (like this!) and code (coming up!) to be combined in a single document.

The notes presented in lecture are Jupyter Notebooks. Your CodingLabs will be in Jupyter Notebooks. And, your assignments will be completed in Jupyter Notebooks. So, you'll want to get very comfortable with working within a notebook.

## Cells

The operational unit of the notebook is the cell.

Cells are primarily either text (Markdown) or code. 

If you click on this cell, you should see in the menu above that it says "Markdown"



### YOUR TURN: Add a new cell

Single click on this cell. 

Then, click the '+' icon on the toolbar at the top to add a new cell below this one.

The cell you just added above is a code cell by default. You can tell by the `In [ ]:` to the left of the cell and the fact that the drop-down box above says "Code"

Use that drop-down menu to change the type of that cell you just created to be a text cell. Type the following in that cell "Learning to program in Python makes me ..." and finish the sentence with how you feel about learning to program in python.

### YOUR TURN: Editing Text Cells

To edit the text in this cell, double-click on it.

Add information below about yourself to get practice with editing text cells.

Name:   
PID:  
College:  
Major:  


### Markdown

As discussed in lecture, these cells are formatted using [Markdown syntax](https://www.markdownguide.org/basic-syntax/). 

Edit the text in the cell below so that it has the formatting specified by the text. 

For example, if the text said:

This sentence is bold.

You would edit the text so that it was bold:

**This sentence is bold.**

Note that to see the formatting changes, you'll have to run the cell using the Run icon above (or more simply use 'Shift + Enter' on your keyboard.

### YOUR TURN: Edit this text

This is a heading level 4 (H4)

This sentence is italicized.

Below is a bulleted list:
bullet item 1 
bullet item 2
bullet item 3

Below is a numbered list:
list item 1
list item 2
list item 3

This sentence is bold AND italic.

### Code Cells

Below this cell, you see a code cell. 

Code is added to cells, but they have to be Run (executed) for the code to be processed.

Type `x = 3` in the code cell below. Then, click "Run" from the menu above of press 'Shift + Enter' on your keybood to execute that code.



{:.input_area}
```python
## YOUR CODE HERE


```


After running the code cell above, there will be a number between the brackets to the left of the cell. Each time you run a code cell, this number will increase by 1. Run the code cell below to see what we mean.



{:.input_area}
```python
y = 29
```


One thing that sometimes trips users up is the fact that cells do NOT have to be run in order from top to bottom. Python remembers whatever was executed most recently. To see what we mean, run the cell below and see what it returns:



{:.input_area}
```python
x
```


Now, return to the cell above where you defined `x = 3` and change it to `x = 9`. Be sure to re-run this cell. When you do so, note that the number to the left of the cell updates to be the most recent number. `x` is now defined as 9, as that is the most recent cell that executed. 

The **order** in which the cells are run matters **NOT** the order in which they appear in the notebook.

## Part 2: Datahub

Assignments will be retrieved and submitted on [datahub](https://datahub.ucsd.edu).

**Datahub** is a server-based service hosted by UCSD. It provides each of you with a space to complete your work. This is space on a UCSD server. You have your own account where you can save your own files and do your own computing. This is what you'll use to complete your assignments.



### Step 1: Log Into Datahub

**Log in (using your UCSD credentials/gmail account) to [datahub](https://datahub.ucsd.edu) now.**

Note that *if* you are officially on the class roster, there will be an environment for this class there for you. For example, for the Fall 2019, you should see COGS18_FA19_A00. Click on this and then click 'Launch Environment'.

Your server space will launch.

Notice the tabs along the top. One of these should say "Assignments." This is where you will fetch, complete, and submit assignments. Let's practice this process now.


### Step 2: Fetch Assignment

Under the 'Assignments' tab, you will see an assignment called "Practice." 

1. **Click Fetch** to get your copy of this practice assignment. 

        After clicking Fetch, this assignment will be listed under your "Downloaded Assignments". 
        You *could* click on this assignment there, but let's take a look at where this assignment lives on your space in the server. 

2. **Click on the Files tab** along the top. There should now be a directory (folder) in there called "Practice"

3. **Click on the "Practice" directory** to display its contents.

4. Within this directory, you'll see a Jupyter Notebook. **Click on this notebook** to open it up. 

Now, once you open up this file, you're ready to complete the practice assignment!


<div class="alert alert-danger">
Whatever you do, please <b> DO NOT RENAME ASSIGNMENT NOTEBOOK FILES! </b>
</div>

When completing your assignments, you will write and execute your code directly within this document, but you **should not** rename it. Our autograding system is expecting a file of the same name. 

### Step 3: Complete & Submit

Complete the assignment within the notebook you've just opened up. 

Be sure to read all of the text within the notebook as this information applies to all of your assignment submissions this quarter.

Once you complete the assignment, submit it on Datahub. You'll see this assignment show up within the "Submitted Assignments" section within the "Assignments" tab.

We're not going to grade this one, but we wanted to be sure you all got practice before doing the real thing for class.

## Part 3: Anaconda

As noted above, assignments will be completed on Datahub. However, the second part of the course involves completing a project. This *can* be completed on datahub, but you'll likely want to complete this on your local computer. To do so, you'll need Python downloaded on your computer. 

Additionally, after this course, if you want to have the tools we use here, you'll want to have them installed on your own computer.

To ensure that this is possible, we ask that you **download the [Anaconda Distribution](https://www.anaconda.com/distribution/) now**. This is available for mac, windows,and linux operating systems. However, note that if you have a linux-based machine, you may run into a few hurdles upon installation.

The Anaconda distribution is:

> a package manager, an environment manager, a Python/R data science distribution, and a collection of over 1,500+ open source packages. Anaconda is free and easy to install, and it offers free community support."

This provides you with a local copy of Jupyter and access to commonly-used python packages.

