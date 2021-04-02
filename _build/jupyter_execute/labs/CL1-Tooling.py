# Coding Lab 1: Tech Setup & Tooling

Welcome to the first coding lab!

CodingLab labs are meant to be interactive - so, feel free to find another person to work together with on your CodingLab notebooks. 

For this lab, it's really important that you're comfortable with all of the tools we introduce here, as we'll be using them throughout the quarter. So, while you should feel free to consult with your classmates, you'll want to be sure you carry out each part on your own. 

If you have a question about how something works / what something does - try it out, and see what happens! If you get stuck, consult your classmates. If you're still stuck, your instructional staff are there to help!

## Reminders: 

- **PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**
- **PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE ASSIGNMENT.** (Adding new cells is allowed!)

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

In it you will see 

```python
# YOUR CODE HERE
raise NotImplementedError()
```

Any time you see this in a coding lab, assignment, or exam, you'll replace it with your answer.

Code is added to cells, but they have to be Run (executed) for the code to be processed.

Type `x = 3` in the code cell below. Then, click "Run" from the menu above of press 'Shift + Enter' on your keybood to execute that code.

### BEGIN SOLUTION
x = 3
### END SOLUTION

# this should not give any output if you did the above
# this checks to make sure x exists 
# but it does NOT check that it has the right value
assert x

After running the code cell above, there will be a number between the brackets to the left of the cell. Each time you run a code cell, this number will increase by 1. Run the code cell below to see what we mean.

y = 29

One thing that sometimes trips users up is the fact that cells do NOT have to be run in order from top to bottom. Python remembers whatever was executed most recently. To see what we mean, run the cell below and see what it returns:

x

Now, return to the cell above where you defined `x = 3` and change it to `x = 9`. Be sure to re-run this cell. When you do so, note that the number to the left of the cell updates to be the most recent number. `x` is now defined as 9, as that is the most recent cell that executed. 

The **order** in which the cells are run matters **NOT** the order in which they appear in the notebook.

## Part 2: CodingLab & Assignment Submission

Assignments will be retrieved and submitted on [datahub](https://datahub.ucsd.edu).

**Datahub** is a server-based service hosted by UCSD. It provides each of you with a space to complete your work. This is space on a UCSD server. You have your own account where you can save your own files and do your own computing. This is what you'll use to complete your assignments.



### Step 1: Log Into datahub

To get this CodingLab, your Instructional Staff guided you through logging onto datahub. Be sure that you're familiar with this process. The steps are explained below.

**Log in (using your UCSD credentials/gmail account) to [datahub](https://datahub.ucsd.edu).**

Note that *if* you are officially on the class roster (this includes those on the waitlist!), there will be an environment for this class there for you. For example., you should see an environment than starts with "COGS 18". Click on this and then click 'Launch Environment'.

Your server space will launch.

Notice the tabs along the top. One of these should say "Assignments." This is where you will fetch, complete, and submit coding labs and assignments. Let's practice this process now.

### Step 2: Fetch Assignment

Under the 'Assignments' tab, you will see an assignment called 'Practice_COGS18_SP21'. 

1. **Click Fetch** to get your copy of this practice assignment. 

        After clicking Fetch, this assignment will be listed under your "Downloaded Assignments". 
        You *could* click on this assignment there, but let's take a look at where this assignment lives on your space in the server. 

2. **Click on the Files tab** along the top. There should now be a directory (folder) in there called "Practice"

3. **Click on the "Practice_COGS18_SP21" directory** to display its contents.

4. Within this directory, you'll see a Jupyter Notebook. **Click on this notebook** to open it up. 

Now, once you open up this file, you're ready to complete the practice assignment!


<div class="alert alert-danger">
Whatever you do, please <b> DO NOT RENAME CODINGLAB OR ASSIGNMENT NOTEBOOK FILES! </b>
</div>

When completing your assignments, you will write and execute your code directly within this document, but you **should not** rename it. Our autograding system is expecting a file of the same name. 

### Step 3: Complete & Submit

Complete the assignment within the notebook you've just opened up. 

Be sure to read all of the text within the notebook as this information applies to all of your assignment submissions this quarter.

Once you complete the assignment, submit it on Datahub. You'll see this assignment show up within the "Submitted Assignments" section within the "Assignments" tab.

We're not going to grade this one, but we wanted to be sure you all got practice before doing the real thing for class.

<div class="alert alert-danger">
If you fail to click "Submit", we will not have access to or be able to grade your assignment. <b>ALWAYS REMEMBER TO CLICK SUBMIT.</b>
</div>

## Part 3: Academic Integrity

Navigate to the following pages: 
- https://academicintegrity.ucsd.edu/excel-integrity/define-cheating/index.html
- https://academicintegrity.ucsd.edu/faq (read the "Does...count as cheating?" section)

Read and reflect on the content there. Then, respond to the following situations with your own thoughts in the cell provided after each situation using Markdown text. 

Consider 1) if the action was a violation of academic integrity in COGS 18 and 2) if it was, what do you think the consequence should be.

**Situation 1**

A COGS 18 student is working on an assignment and is particularly stuck on one question. They go back through the notes and just can't figure it out. They look at the staff office hours schedule and realize that they won't be able to make it to any staff office hours this week, so they decide to ask a classmate for help. Their classmate agrees to meet. During this meeting they discuss where the stuck student is confused. The classmate helps the stuck student through the question. The stuck student writes the code during this process for the assignment and then explains the code they've just written back to their helpful classmate. The stuck student thanks their classmate for their help.

**Prof's thoughts**: This is 100% OK! In COGS 18, you're allowed and encouraged to help one another. In fact, when we explain things to others, we solidfy our own understanding, so both students are getting a lot out of this interaction!

**Situation 2**

A COGS 18 student is taking their exam. During this, they realize they're running out of time before the submission deadline and still have two questions left they just can't figure out. They text their friend who is in the class asking for the answers to those two questions. Their friend (who has already submitted the exam), wanting to help out, sends his exam code along. The struggling student changes the code a little bit and submits his exam.

**Prof's thoughts**: This is NOT ok. It is never ok to ask a classmate for their answers - be it on a coding lab, assignment, or exam. This is especially egregious as the questions on *exams* are not allowed to be discussed with anyone. This could lead to consequences for both the student asking and the student who provided the answers.

**Situation 3**

A COGS 18 student is taking their exam. During this, they realize they just can't figure out two questions while taking the exam. They copy the question from the exam and search in Google. In this search, they see a website pop up with this exact question in it...and click on the link. To their surprise, the answer to both questions are there on the website. They copy the code into their exam and submit their exam.

**Prof's thoughts**: This one may *seem* tough, but hopefully after I explain, it will clear things up as to why this is NOT ok. In this case, this code would NOT be code you wrote/came up with and thus you cannot use it on your exam. If/when this happens, it's because someone from COGS 18 this quarter posted my exam to the Internet. First, exams are *my* intellectual property (and so they are not your's to share/post publicly on a site like Chegg, for example) and are completely different from one quarter to the next, so I'm typically able to determine who posted it *and* who used the answer. *It is in your best interest to stay OFF of sites like Chegg.* If you're struggling on a question, a lot of other students are likely struggling on that question. It could be becasue I made the question too difficult (which I'll always consider when graing). The only way I can assess what you do and do not know (and what I have an have not taught well) is if you take the exam using your brain (with help from notes and general searches on the Internet for specific concepts). Please do NOT post my exam questions to the Internet. Please do not search for my exam questions on the Internet. Please avoid sites where answers are posted when taking exams.

## Optional: Anaconda

As noted above, assignments will be completed on Datahub. However, the second part of the course involves completing a project. This *can* be completed on datahub, but you'll likely want to complete this on your local computer. To do so, you'll need Python downloaded on your computer. 

Additionally, after this course, if you want to have the tools we use here, you'll want to have them installed on your own computer.

To ensure that this is possible, we ask that you **download the [Anaconda Distribution](https://www.anaconda.com/distribution/) now**. This is available for mac, windows,and linux operating systems. However, note that if you have a linux-based machine, you may run into a few hurdles upon installation.

The Anaconda distribution is:

> a package manager, an environment manager, a Python/R data science distribution, and a collection of over 1,500+ open source packages. Anaconda is free and easy to install, and it offers free community support."

This provides you with a local copy of Jupyter and access to commonly-used python packages.


## The End!

This is the end of the first Coding Lab!

Be sure you've made a concerted effort to complete all the tasks specified in this lab. Then, go ahead and submit on datahub!