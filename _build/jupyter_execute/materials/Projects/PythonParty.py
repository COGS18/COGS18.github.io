#!/usr/bin/env python
# coding: utf-8

# # Python Party!
# 
# It's a bit less of a party while learning remotely...

# **Course Announcements**
# 
# - **A4** due Mon 2/28 (11:59 PM)
# - **CL7** due *next* Wednesday (3/2)
# 
# **Note**
# - Prof Ellis' OH: extra **zoom office hours today 9-10 AM** (will use normal zoom link on canvas; make-up for Monday)

# **Black History Month**: Foundational Fridays
# 
# - [Kimberly Bryant](https://twitter.com/6Gems) - founder and CEO of BlackGirlsCode
# - [Dr. Joy Buolamwini](https://twitter.com/jovialjoy) - founder of the Algorithmic Justice League
# - [Dr. Timnit Gebru](https://twitter.com/timnitGebru) - founder of The Distributed AI Research Institute; AI Ethics
# - [Erica Baker](https://twitter.com/EricaJoy) - CTO at DCCC
# 
# Note: From 1977 to 2013, the. largest # of black women to earn a CS PhD in any given year was...10

# **Q&A**
# 
# Q: is there an easy way to download all the lecture notes from datahub using code in the terminal on my computer?  
# A: Yes - you can zip/tar all the contents on datahub into a single file, download, and then unzip/untar on your computer. I will provide instructions on this at the end of the quarter.
# 
# Q: I was using cat, and it wasn't printing anything out even though I know that new_file was placed within dir_name. Is there a reason for this?  
# A: This is likely b/c you didn't add any contents to that file. Open that file up, add some text, and try `cat` again.
# 
# Q: I still don't understand the purpose of using the command line.   
# A: Quickly navigate to and organize files. Also, run python scripts (we'll be doing this today).
# 
# Q: Why can't we just stick to jupyter for an intro class  
# A: Because understanding how to work with .py files is critical for moving forward/understanding other code you see out in the world.
# 
# Q: What does `!cd ~/` do?  
# A: Takes you to your home directory. If you're already in your home directory...it will leave you where you are.
# 
# Q: How do we use the command line directly on our computer, like in our computer's terminal?   
# A: Search for "terminal" on your computer (if you don't have a terminal application already installed (depends on your computer), you could download a "bash shell". (I use iTerm.)
# 
# Q: What is the difference between shell command and command line? Is there a difference?  
# A: The command line is where you type shell commands. So, when you open up a terminal and get the black background, that is the command line. One thing you can do at the command line is type shell commands.
# 
# Q: Is the command line somewhere we are able to write code or is it purely used for locating files, documents, and code that has already been written? A follow-up question if we don't write code in the command line would be where would we write code then? Just in another Jupyter Notebook file that we then retrieve using the command line?  
# A: In a text editor! (The part of the notes we didn't get to on Wednesday but will discuss today.)
# 
# Q: How is array different from other collections (like tuples, lists, dictionaries)?  
# A: We'll discuss arrays next week when we discuss `numpy`, but for now, arrays can be N-dimensional.

# ## Project-based Course
# 
# Today starts the transition to a project-based course!
# 
# - [Project Overview](https://cogs18.github.io/projects/overview.html)    
# - [Project Ideas](https://cogs18.github.io/projects/ProjectIdeas.html)   
# - [Project FAQ](https://cogs18.github.io/projects/faq.html)
# - [Project Template](https://cogs18.github.io/assets/intro/projects/ProjectTemplate.zip)

# ## Project Options
# 
# Choose ONE:
# - **Complete the final project**
#     - we're discussing the details today
#     - submitted on datahub or Canvas by 11:59 PM on day of the final
#     - opportunity to learn the most! 
#     - takes a lot more time  
#     - opportunities for extra credit (going above & beyond; GitHub)
#     - *can* ask staff for help/ask questions throughout

# - **Complete the final exam** 
#     - it will be a guided mini-project 
#     - will be taken on datahub
#     - 24h+ to complete 

# Caveats if you take the final exam:
# 1. The highest grade you can get in the course is an A (not an A+)
# 2. There is no additional opportunities for extra credit (Note: if you've been filling out daily participation surveys that EC *will* apply to both exam and project)
# 3. You have to complete on your own (same rules as previous midterms)

# Submit one, *NOT* both (I have lots of grading at the end of the quarter!). If you do both, I will use the lower score.

# ## Project Overview
# - must implement some new thing (_not_ grading on complexity)
# - completed individually
# - uses good code practices
# - What you will turn in: folder on datahub OR zip file with your project on Canvas
#     - \>= 1 Jupyter notebook (minimally includes project description)
#         - ideally: demonstrates how your project runs (likely only a few lines of code)
#     - \>= 1 module (having an additional script is optional)
#         - has *at least* three (3) unique/original functions or methods
#     - a test file with \>= 3 tests

# ## Project Topics
# - Encryption (A2)
# - Chatbots (A3)
# - Artificial Agents (A4)
# - A Data Analysis (A5)
# - Choose your own adventure (propose and develop your own project idea)

# ### Taboo (Off-limit) topics $^*$
# - Hangman
# - `turtle` drawings
# - tic-tac-toe
# - blackjack
# - Magic 8 Ball
# - Rock, Paper, Scissors
# - Snake Game
# - Connect4 Game 
# 
# $^*$If you have a really new hangman implementation/idea or are super stoked about your great `turtle` idea or have invented a spin on traditional tic-tac-toe/blackjack/magic 8 ball/rock, paper, scissors, you'll need to pitch your idea to (via campuswire/email or in office hours) and get approval from Professor Ellis

# ### Process:
# 
# 1. Download 1) template from website OR 2) fetch Project on datahub
# 2. Brainstorm an idea
# 3. Design what "pieces" (functions/classes/etc.) you need to execute that idea
# 4. Start writing code + tests
# 5. Submit on 1) Canvas or 2) datahub

# #### Why template + Canvas?
# 
# - Certain packages do not work on datahub (game packages; audio; GUI)
# - Working outside of datahub will be helpful in the future
# - You are not dependent on the Internet working well

# #### Project advice:
# - Work steadily over time
# - Work to first create a minimal viable product
#     - modular design
#     - multiple, independent pieces
# - Rapid prototyping + testing

# ### Grading
# | Component        | Grade Value |
# |:-------------: |:-----------:|
# | Concept | 5% | 
# | File Structure | 5% | 
# | Project Description | 10% | 
# | Approach | 20% | 
# | Project Code | 30% | 
# | Code Style | 10% | 
# | Code Documentation | 10% | 
# | Code Tests | 10% | 
# | Extra Credit | 4% | 
# | GitHub Extra Credit | 1% | 

# #### Extra Credit:
# - Go beyond the requirements of the project / press yourself to learn something new (*up to* 4%)
# - Put your project on GitHub (1%)
# 

# #### Clicker Question #1
# Do you have an idea of what you want to do for your **project**?
# 
# - A) absolutely no idea
# - B) some idea, but not sure
# - C) fairly good idea
# - D) I know exactly what I want to do.
# - E) I'm thinking I'm going to take the final exam

# ### Example Projects: 
# 
# * Previous Examples: https://github.com/COGS18/Projects#projects
# * Andrew's project video

# ## Python Party!
# 
# What questions remain for you?
