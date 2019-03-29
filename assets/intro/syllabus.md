---
output:
  pdf_document: default
---

# COGS 18: Introduction to Python
**Spring 2019, MWF 9-9:50**  
**Warren Lecture Hall 2001**

---

# COURSE OVERVIEW

Welcome to COGS18! The core goal of this class is to teach you introductory, hands-on skills for computer programming, specifically using the Python programming language. We aim to do so in a way that fits well within the cognitive science department, using particularly-relevant use cases. Our approach is to focus on programming as a tool and to get you started with the necessary background and basic skills required to get you reading and writing code. We aim to provide you with a strong foundation so that you can continue programming after you leave this class, applying the skills you learn here to your domain or topic of interest.

Note that this is the second time this course is being offered and the first time Professor Ellis is teaching it. We will do everything we can to make sure things run smoothly, but please be patient as we get things going and running as well as we can. We welcome (and will be asking for!) your feedback about this course. 

---

# COURSE STAFF & INFORMATION

**Instructor**: Shannon Ellis [sellis@ucsd.edu](sellis@ucsd.edu)  
**Instructor Office Hours**: Fridays, 3-5p (CSB 243)  
**TA Office Hours**: will be announced first week of class and this document will be updated 

| Role        | Name          					   | Section  |
| -------------: |:-----------------------------------------------:|:-----------:|
| TA 	           | Charles Chen				   | Wed 11AM & 12PM |
| TA 	           | Shreenivas Venkataramanan           | Mon 3PM, 4PM |
| IA	           | Weilun Yao                                       | Wed 1PM, Fri 12PM |
| IA	           | Severine Soltani                               |    Wed 1PM, Fri 11AM |
| IA	           | Stephen Jarrell                                 |    Wed 1PM, Fri 11AM |
| IA	           | Ahrial Young                                     |    Fri 11AM |
| IA	           | Myles Wright                                    |    Mon 4PM, Fri 10AM |
| IA	           | Miranda Go                                      |    Fri 10AM |
| IA	           | Edward Chen                                   |     Fri 12PM |

Course Website: https://cogs18.github.io   
Course Piazza*: http://piazza.com/ucsd/spring2019/cogs18  
Course podcast/screencast: https://podcast.ucsd.edu/  
Course Feedback (anonymous): [Google Form](https://goo.gl/forms/2nXnDNbgYuS1OsGF2)    

*You will be able to post anonymously on Piazza; however, you will only be anonymous to your classmates. Your Instructor and TAs will be able to see who you are.

---

#COURSE OBJECTIVES

- Program at an introductory level in the Python programming language
- Read basic Python programs, recognizing the structures they use and be able to explain how they work
- Solve basic problems using programmatic solutions
- Write and debug small Python programs
- Execute Python programs on your local computer, using notebooks and the command line
- Describe and implement best practices in Python, keeping in mind that programming is done by and for humans

To achieve these objectives, information will be presented during lecture. You will have the opportunity to program in lecture, during section, and throughout all assignments and your small final project. Examples throughout this course will be related to cognitive science, focusing on data analysis, artificial intelligence, human-computer interaction, and programmatic thinking.

---
# COURSE MATERIALS

- All students will need access to an iClicker*
- There is no textbook
- All materials will be provided via the course website

Software

- Python 3.6 (Anaconda distribution)
- Jupyter Notebooks

Detailed instructors for these installations will be listed on the course website and hands-on help will be offered across week 1. All of the software is freely-available for download. If you do not have a computer available, you will be able to complete the course requirements on UCSD computers.

*You will need a clicker, of this brand, as no other brand will work with the system we are using. You must [register your clicker on TritonEd](https://blink.ucsd.edu/faculty/instruction/tritoned/students.html#Register-your-iclicker-Remote-I) & bring it to lecture. If you previously registered one on TritonEd & are using the same clicker in this class, you do not have to register it again. If you would rather use the REEF app, you are free to do so; however, note that if the Wi-Fi is down, the app will not work and you will not get credit for those responses.

---
# GRADING & ATTENDANCE

**Grading**: 

|         | \% of Grade          					   | Requirement  |
| -------------: |:-----------------------------------------------:|:-----------|
| Coding Lab           | 15\%				   | Attend & Participate in 6/8 Coding Labs |
| Assignments 	           | 40\%           | Complete 4 Assignments |
| Midterm           | 20\%                                      | Written in-class midterm |
| Final Project	           | 25\%                              |    Submit final project |
 
**Final exam date**: No final exam, only final project deadline.

### Grades

All grades will be released on TritonED. We will try to send out automated alerts if we do not receive a submission and/or if it fails to be processed, but ultimately it is your responsibility to check your grades and get in touch if any are missing or you think there is a problem.
 
### Assignment Regrades

We will work hard to grade everyone fairly and return assignments quickly. But, we know you also work hard and want you to receive the grade you've earned. Occasionally, grading mistakes do happen, and it's important to us to correct them.
If you think there is a mistake in your grade, post to Piazza within 72 hours of your receipt of the grade. This post should include evidence of why you think your answer was correct (i.e. a specific reference to something said in lecture) and should point to the specific part of the assignment, reading quiz, or exam in question. Submit this post as a Question on Piazza, address it to 'Instructors', and select the tag 'regrades'.

### Lecture Attendance

Our goal is to make lecture worth your while to attend. That said, it will be up to you as to whether you come to lecture. Lecture attendance is not required, but is strongly recommended as time will be dedicated in-class to practicing the concepts presented during lecture.

There is an opportunity; however, for extra credit when it comes to lecture attendance. If you answer more than 50\% of the clicker questions (regardless of correctness) at more than 75\% of the lectures, you will get 1\% point of extra credit onto your final grade. 

### Coding labs (15\%)

Discussion section will be used as a coding lab. As such, you will be provided with specific tutorials or activities each week that are focused on preparing you for the assignments and projects. Across the quarter there will be 8 coding labs. If you attend at least 6 of these, you will receive full credit for coding labs. For each lab under 6 that you attend, 5\% credit will be deducted. (For example, if you attend 5 of 8 coding labs, you'll earn 10\% of the possible credit. If you attend 4, 5\%. If you attend 3 or fewer, you will not receive coding lab credit.) Note that to receive credit for a coding lab, you have to actually attend a section. These cannot be completed outside of section time. 

You should be signed up for a section for which you can attend. However, if you are unable to attend the section for which you are signed up, you are free to attend a different section any given week than the one in which you're assigned. You will receive attendance credit regardless of which section you attend. Note that this policy could change if too many people are attending one section each week. We intentionally have section capped at 35 people so that students can get help from their TAs and IAs.

### Assignments (30\%)

There will be four assignments, each worth ~8\% of your final grade. Assignments will be hands-on coding assignments. Assignments are to be completed individually. You will typically have about 1 week after release to complete each assignment. Assignments will be due on Mondays by 11:59PM. Late assignments will be accepted at 75\% credit for the first week after the due date. One week after the due date, answers will be released and assignments will no longer be able to be submitted for credit.

### Midterm (20\%)

There will be an in-class midterm on Friday May 10th, during the sixth week of class. The midterm will be include multiple choice and short answer questions.

### Final Project (35\%)

Successful completion of this class will require you to complete an independent coding project worth 35\% of your final grade. We will discuss the details elsewhere; however, briefly, you will either (1) expand upon one of the class assignments adding original elements or (2) write original code for a project topic of your choosing.


---
# OTHER GOOD STUFF

### Class Conduct

In all interactions in this class, you are expected to be respectful. This includes following the [UC San Diego principles of community](https://ucsd.edu/about/principles.html).
 
This class will be a welcoming, inclusive, and harassment-free experience for everyone, regardless of gender, gender identity and expression, age, sexual orientation, disability, physical appearance, body size, race, ethnicity, religion (or lack thereof), political beliefs/leanings, or technology choices.

At all times, you should be considerate and respectful. Always refrain from demeaning, discriminatory, or harassing behavior and speech. Last of all, take care of each other.

If you have a concern, please speak with Dr. Ellis, your TAs, or IAs. If you are uncomfortable doing so, that's ok! The [OPHD](https://blink.ucsd.edu/HR/policies/sexual/OPHD.html) (Office for the Prevention of Sexual Harassment and Discrimination) and [CARE](https://care.ucsd.edu/) (confidential advocacy and education office for sexual violence and gender-based violence) are wonderful resources on campus.  

### Academic Integrity

Don't cheat.

You are encouraged to (and at times will have to) work together and help one another. However, you are personally responsible for the work you submit. For assignments, it is also your responsibility to ensure you understand everything your group has submitted and to make sure the correct file has been uploaded, that the upload is uncorrupted, and that it renders correctly. Projects may include ideas and code from other sources, but these other sources must be documented with clear attribution. Please review academic integrity policies [here](http://academicintegrity.ucsd.edu).

We anticipate you all doing well in this course; however, if you are feeling lost or overwhelmed, that's ok! Should that occur, we recommend: (1) asking questions in class, (2) attending office hours and/or (3) asking for help on Piazza.


Cheating and plagiarism have been and will be strongly penalized. If, for whatever reason, TritonED is down or something else prohibits you from being able to turn in an assignment on time, immediately contact me by emailing your assignment by email (sellis@ucsd.edu), or else it will be graded as late.

### Disability Access
Students requesting accommodations due to a disability must provide a current Authorization for Accommodation (AFA) letter. These letters are issued by the Office for Students with Disabilities (OSD), which is located in University Center 202 behind Center Hall. Please make arrangements to contact Dr. Ellis privately to arrange accommodations.

Contacting the OSD can help you further:  
858.534.4382 (phone)  
osd@ucsd.edu (email)  
http://disabilities.ucsd.edu  

### How to Get Your Question(s) Answered and/or Provide Feedback 

It's great that we have so many ways to communicate, but it can get tricky to figure out who to contact or where your question belongs or when to expect a response. These guidelines are to help you get your question answered as quickly as possible and to ensure that we're able to get to everyone's questions. 

That said, to ensure that we're respecting their time, TAs and IAs have been instructed they're only obligated to answer questions between normal working hours (M-F 9am-5pm). However, I know that's not when you may be doing your work. So, please feel free to post whenever is best for you while knowing that if you post late at night or on a weekend, you may not get a response until the next day. As such, do your best not to wait until the last minute to ask a question.

If you have:

- **questions about course content** - these are awesome! We want everyone to see them and have their questions answered too, so post these to Piazza! 
- **a technical assignment question** - come to office hours (or post to Piazza). Answering technical questions is often best accomplished in person where we can discuss the question and talk through ideas. However, if that is not possible, post your question to Piazza. Be as specific as you can in the question you ask. And, for those answering, help your classmates as much as you can without just giving the answer. Help guide them, point them in a direction, provide pseudo code, but do not provide code that answers assignment questions.
- **been stuck on something for a while (>30min) and aren't even really sure where to start** - Programming can be frustrating and it may not always be obvious what is going wrong or why something isn't working. That's ok - we've all been there! IF you are stuck, you can and should reach out for help, even if you aren't exactly sure what your specific question is. To determine when to reach out, consider the 2-hour rule. This rule states that if you are stuck, work on that problem for an hour. Then, take a 30 minute break and do something else. When you come back after your break, try for another 30 minutes or so to solve your problem. If you are still completely stuck, stop and contact us (office hours, post on Piazza). If you don't have a specific question, include the information you have (what you're stuck on, the code you've been trying that hasn't been happening, and/or the error messages you've been getting).
- **questions about course logistics** - first, check the syllabus. If the answer is not there, check or post on Piazza or ask a classmate.
- **questions about a grade** - post as a question on Piazza, address it to 'Instructors,' and select the folder 'regrades'
- **a specific section-related question** - send a direct message on Piazza to your TA/IA
- **something super cool to share related to class or want to talk about a topic in further depth** - feel free to email Dr. Ellis (sellis@ucsd.edu) or come to office hours. Be sure to include COGS108 in the email subject line and your full name in your message.
- **some feedback about the course you want to share anonymously** - If you've been offended by an example in class, really liked or disliked a lesson, or wish there were something covered in class that wasn't but would rather not share this publicly, etc., please fill out the anonymous Google Form*

*This form can be taken down at any time if it's not being used for its intended purpose; however, you all will be notified should that happen. 

