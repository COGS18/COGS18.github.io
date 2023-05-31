#!/usr/bin/env python
# coding: utf-8

# Answers/points to **in-class** exam: https://cogs18.github.io/assets/intro/exams/E2_Sp23_Answers.pdf

# # COGS 18 - Exam 2 (Take-Home)
# 
# This is the take-home portion of the second exam for Spring 2023. It covers the technical implementation of topics through the Command Line Lecture.
# 
# This take-home portion of the exam is out of 2.5 points, worth 2.5% of your grade.
# 
# **PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**
# 
# **PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE ASSIGNMENT.** (Note that you can add additional cells, if you want to test things out.

# #### Instructions
# 
# #### Timing
# - There will be a multi-day window during which you can complete this exam.
# - Exam deadline (submit button on Datahub) is 11:59pm Friday May 26th.
# 
# #### The Rules
# - You are to complete this exam on your own.
# - This is open-notes & open-Internet.
# - You may not talk to any humans about this exam. 
# - The following are all *prohibited*:
#     - text/phone/online chat communication
#     - posting questions to a message board where a human could respond (Discord, Chegg, any similar site)
#     - viewing exam questions from a message board (as described above)
#     - asking anyone via any form about a question on this test directly
# - Clarification questions will ***not*** be allowed and there will be no posting on Piazza about the exam at all. 
#     - Piazza posts about the exam will not be answered and will be deleted. 
#     - Students who post questions about the exam to Piazza are at risk of losing points on the exam.
#     - If you are confused about wording, add a note to your exam explaining your confusion and how you interpreted the question. 
#     - Note: This policy is b/c we are incapable of responding for the entirety of the exam. This is the only way to make it fair across the board for students.
#     - If you have a technical issue completing the exam, message (Piazza or email) Prof Ellis ASAP.
# 

#  <span style="color: red;">Note: </span> This portion of the midterm will be autograded, similar to an assingment. `assert` statements are there to guide your thinking but do not guarantee you've gotten the answer correct.

# ### Q0 - Honor Code (0.05 points)
# 
# In the cell below, include a variable `honor_code` that stores the boolean `True` if you agree to the following statement:
# 
# >I agree that this exam was completed individually with the knowlege in my brain, information the notes from this course, and/or with searching for help on the Internet *without searching for answers to the text from these questions directly*. I did not ask anyone about specific questions on this exam. I did not post these questions (in part or in whole) on the Internet. I did not copy answers to these questions from anywhere or anyone else. I understand all code I've written on this exam and could explain my answers to someone else if asked.
# 

# In[1]:


### BEGIN SOLUTION
honor_code = True
### END SOLUTION


# In[2]:


assert honor_code


# ### Background
# 
# On the in-person portion of the midterm you were told the following: We’re going to work to build a `MusicPlayer` type object. The idea here is that there will be a single class (`MusicPlayer`) with a few attributes (described below) and two methods: 1) `add_song()`, a method to add a song to our playlist and  2) `change_volume()`, a method that changes the value of the volume for our `MusicPlayer`.
# 

# ### Q1 - `MusicPlayer()` (2 pts)
# 
# Create a `MusicPlayer` class that includes the following components:
# 
# **Step 1**:  \
# To start building your `MusicPlayer()` type object, you’ll first need to create the class and specify the necessary instance attributes: 1) `playlist` (which will be an empty list) and 2) `volume` (which will be 50) when an instance of the object is first created.
# 
# **Step 2**:  \
# Now, your `MusicPlayer()` needs an `add_song()` method. This method should take a song in as input and add that song to the object’s `playlist` attribute.
# 
# **Step 3**:   \
# Finally, your object needs a `change_volume()` method. This method should take in a numeric value specifying by how much the volume should change. Your code should ensure that the volume after it’s changed can only be a value between 0 and 100. (For example, if your volume was 90 and you specified to change_volume() by 20, the value stored in volume should be 100…the max possible value.) 

# In[3]:


### BEGIN SOLUTION
class MusicPlayer():
    
    def __init__(self):
        self.playlist = []
        self.volume = 50
        
    def add_song(self, song):
        self.playlist.append(song)
    
    def change_volume(self, change):
        self.volume = self.volume + change
        
        if self.volume > 100:
            self.volume = 100
        elif self.volume < 0:
            self.volume = 0
### END SOLUTION


# In[4]:


# you can use this cell to test/execute/check your thinking (optional)


# In[5]:


assert callable(MusicPlayer)
# create instance of object
myplayer = MusicPlayer()


# In[6]:


# hidden tests that check the playlist instance attribute
### BEGIN HIDDEN TESTS
# rerun the following just in case a student 
# uses the myplayer above to test things out
myplayer = MusicPlayer()
assert myplayer.playlist == []
### END HIDDEN TESTS


# In[7]:


# hidden tests that check the volume instance attribute
### BEGIN HIDDEN TESTS
assert myplayer.volume == 50
### END HIDDEN TESTS


# In[8]:


# hidden tests that check the add_song method executes without error
### BEGIN HIDDEN TESTS
myplayer.add_song('You and Me on the Rock')
### END HIDDEN TESTS


# In[9]:


# hidden tests that check the add_song method does what it's supposed to
### BEGIN HIDDEN TESTS
myplayer.add_song('Sinners, Saints, and Fools')
assert len(myplayer.playlist) == 2
### END HIDDEN TESTS


# In[10]:


# hidden tests that check the change_volume method executes without error
### BEGIN HIDDEN TESTS
myplayer.change_volume(10)
### END HIDDEN TESTS


# In[11]:


# hidden tests that check the change_volume method does what it's supposed to
### BEGIN HIDDEN TESTS
assert myplayer.volume == 60
### END HIDDEN TESTS


# In[12]:


# hidden tests that check the change_volume method follows the 0-100 rule specified in question
### BEGIN HIDDEN TESTS
myplayer.change_volume(50)
assert myplayer.volume == 100
myplayer.change_volume(-110)
assert myplayer.volume == 0
### END HIDDEN TESTS


# ### Q2 - Create an Instance (0.45 pts)
# 
# Here, you'll initialize `my_music`, an instance of your `MusicPlayer` object.
# 
# After initializing `my_music`, you'll add three of your favorite songs to its playlist (using `add_song`) and then `change_volume` such that the `volume` is 20 after execution.

# In[18]:


### BEGIN SOLUTION
my_music = MusicPlayer()
my_music.add_song('Every Time I Hear That Song')
my_music.add_song('The Mother')
my_music.add_song('The Story')
my_music.change_volume(-30)
### END SOLUTION


# In[19]:


# you can use this cell to test/execute/check your thinking (optional)


# In[20]:


assert my_music


# In[21]:


# hidden tests that check the playlist is correct
### BEGIN HIDDEN TESTS
assert len(my_music.playlist) == 3
### END HIDDEN TESTS


# In[22]:


# hidden tests that check the volume is correct
### BEGIN HIDDEN TESTS
assert my_music.volume == 20
### END HIDDEN TESTS


# ## Submit
# 
# Midterm Complete - go ahead and check your work, restart & run all to make sure it all runs without issue, and **submit on datahub**!
