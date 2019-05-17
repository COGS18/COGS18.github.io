---
interact_link: content/materials/17-APIs.ipynb
download_link: assets/downloads/17-APIs.ipynb.zip
pdf_link: assets/pdf/17-APIs.pdf
layout: materials
title: '17-APIs'
prev_page:
  url: /materials/16-CommandLine
  title: '16-CommandLine'
next_page:
  url: /materials/A1-Syntax
  title: 'A1-Syntax'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

## Course Announcements

- Midterm Exam Scores Posted (Median: 86%)
    - Can look at these during Coding Lab next week
    - OR during my office hours _NEXT_ week
- Friday of Week 9
    - Tom Donoghue will lecture
    - Professor Ellis' Office Hours cancelled 5/31
    - Will hold make-up office hours Tuesday of wk9 (5/28) 3-5PM
- Final Project Due (Wed of Finals week - 11:59 PM)
    - For help debugging projects
        - come to us with a specific function or single issue
        - "Spaghetti Code" will be hard for us to help you with


## Clicker Warm Up

Define a function `add_then_multiply` that takes three inputs, assumed to be numbers, adds the first two inputs together and then multiplies that sum by the third input. Return the output.

- A) I did it!
- B) I think I did it!
- C) I'm stuck.



{:.input_area}
```python
### YOUR CODE HERE
```


# APIs

- modules
    - review
    - module APIs
- RESTful APIs
    - LISC
    - Twitter API

## Application Programming Interface

<div class="alert alert-success">
An API is a programmatic interface to an application - a software to software interface, or way for programs to talk to other programs. 
</div>

If you are pointing and clicking on computer applications, that is _not_ an API.

If you are writing code to interact with software and get information, that _IS_ an API.

## Module APIs

Modules have an API. Every time you write or use a set of functions and/or classes, you are writing or using an API. 

## Quick Review: Modules

<div class="alert alert-success">
A 'module' is a set of Python code with functions, classes, etc. available in it. A Python package is a directory of modules.
</div>

Modules are stored in Python files. We can import these files into our namespace, to gain access to the module within Python.



{:.input_area}
```python
# Import & use the math module
import math
math.sqrt(9)
```


### Imports: `from` & `as`



{:.input_area}
```python
# Import a specific object from a module
from random import choice

# use random.choice
magic_8_ball = ['As I see it, yes!', 'Most likely.', 
                'Ask again later.', 'Don\'t Count on it', 
                'Outlook not so good']
choice(magic_8_ball)
```




{:.input_area}
```python
# Import a specific object from a module using an alias
from random import choice as ch

# use aliased name 
ch(magic_8_ball)
```


### Importing Custom Code



{:.input_area}
```python
# Import a class class from an external module
from remote import MyNumbers
```




{:.input_area}
```python
# Import a specific object from a module
from random import choice

# use random.choice
magic_8_ball = ['As I see it, yes!', 'Most likely.', 
                'Ask again later.', 'Don\'t Count on it', 
                'Outlook not so good']
choice(magic_8_ball)
```




{:.input_area}
```python
# Define an instance of our custom class
# apply method
out = MyNumbers(2, 3).add()
out
```




{:.input_area}
```python
# remember we only imported MyNumbers
choice?
```


## Module APIs

Modules have an API. Every time you write or use a set of functions and/or classes, you are writing or using an API. 

### Clicker Question #1

What will the following code snippet print out:



{:.input_area}
```python
def foo(a, b, c=0):
    d = c
    for e in a[:b]:
        d += e
    return d

print(foo(b=2, a=[10, 10, 10, 10]))
```


- A) 10
- B) 20
- C) 30 
- D) 40
- E) None

### Clicker Question #2

How easy did you find interpreting this code?

- A) Easy
- B) Fairly Easy
- C) Neutral
- D) Somewaht Difficult
- E) Difficult

Arguably, this function does _not_ have a good API.

### Function with Fixed Names

### Clicker Question #3

What will the following code snippet print out:



{:.input_area}
```python
def sum_across_list(list_to_count, end_index, start_val=0):

    running_count = start_val
    
    for element in list_to_count[:end_index]:
        running_count += element
    
    return running_count

print(sum_across_list(end_index=2, list_to_count=[10, 10, 10, 10]))
```


- A) 10
- B) 20
- C) 30 
- D) 40
- E) None

### Clicker Question #4

How easy did you find interpreting this code?

- A) Easy
- B) Fairly Easy
- C) Neutral
- D) Somewaht Difficult
- E) Difficult

This is the same function, but has a better API.

## Names Matter!

When writing an API, you are designing the user facing code that a programmer (maybe you in the future) will use.

When using an API, you are using the programmer-facing code that someone else wrote for the task. 

Taking time to have good names and clear documentation can *really help* a programmer interact with an API. 

### Clicker Question #5

Improve the code below's API:



{:.input_area}
```python
class G():
    
    def __init__(self, f, l=None):
        self.f = f
        self.l = l
    
    def ib(self):
        b1 = ['Tyrion', 'Cersei', 'Jon', 'Arya']
        b2 = ['Bran', 'The Mountain', 'The Hound', 'Lord Varys', 
                 'Melisandre', 'Brienne of Tarth']
        b3 = ['King Joffrey', 'Ramsay', 'Little Finger'] 
        
        if self.f is 'Arya':
            o = 'Super BAMF!'
        elif self.f in b1:
            o = 'Definitely a badass'
        elif self.f in b2:
            o = 'We\'ve got ourselves a tier 2 badass!'
        elif self.f in b3:
            o = 'Ew! Despised and reviled.'
        else:
            o = 'meh. could be a badass?'
        return o
```




{:.input_area}
```python
G('Cersei').ib()
```


- A) I made it all better!
- B) I made it slightly better!
- C) I think it's fine as it is.
- D) Super lost



{:.input_area}
```python
# our improved answer
class G():
    
    def __init__(self, f, l=None):
        self.f = f
        self.l = l
    
    def ib(self):
        b1 = ['Tyrion', 'Cersei', 'Jon', 'Arya']
        b2 = ['Bran', 'The Mountain', 'The Hound', 'Lord Varys', 
                 'Melisandre', 'Brienne of Tarth']
        b3 = ['King Joffrey', 'Ramsay', 'Little Finger'] 
        
        if self.f is 'Arya':
            o = 'Super BAMF!'
        elif self.f in b1:
            o = 'Definitely a badass'
        elif self.f in b2:
            o = 'We\'ve got ourselves a tier 2 badass!'
        elif self.f in b3:
            o = 'Ew! Despised and reviled.'
        else:
            o = 'meh. could be a badass?'
        return o
```


## Web APIs

APIs are an interface to interact with an application, _designed for programmatic use_:
- They allow systematic, controlled access to (for example) an applications database and procedures
- They can be used to request data and/or to request that the the application perform some procedure

### RESTful API

(Representational State Transfer API) 

An approach to interact with web addresses

## EUtils API

<div class="alert alert-success">
EUtils is a web accessible API for the National Center for Biotechnology Information, and the databases they curate.
</div>

### EUtils: Search

Search a database to get information we want it to return



{:.input_area}
```python
# Set the base URL for the e-utils API
# where you go to query information from this web address
base_url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
```


Build a URL like a Python function call...

We're just adding some additional 'parameters'.



{:.input_area}
```python
# Set the information we need for launching a search request
search = 'esearch.fcgi?'
term = 'term=' + 'brain'
```


Interacting with APIs specifies that we follow the rules specified by the API from which we're requesting information.

### EUtils: Fetch



{:.input_area}
```python
# Build the full search URL
search_url = base_url + search + term
print(search_url)
```




{:.input_area}
```python
# Set the information we need for launching a fetch request
fetch = 'efetch.fcgi?'
db = 'db=' + 'pubmed'
retmode = '&retmode=' + 'xml'
pubmed_id = '&id=' + str(30439964)
```




{:.input_area}
```python
# Build the full search URL
fetch_url = base_url + fetch + db + retmode + pubmed_id
print(fetch_url)
```


But, our goal isn't to see this information in a web browser. Web browsers are for humans. We want to use this information computationally...

## Requesting Web Pages from Python

To accomplish API interactions, we need to use HTTP requests.



{:.input_area}
```python
# The requests module allows you to send URL requests from python
import requests

# Beautiful Soup has functions to 'clean up' returned web pages into human-friendlier formats
from bs4 import BeautifulSoup
```


### EUtils Search, through Python



{:.input_area}
```python
print(search_url)
```




{:.input_area}
```python
# Request the search page, and parse
search_page = requests.get(search_url)
search_content = BeautifulSoup(search_page.content, 'xml')
```




{:.input_area}
```python
# Check out the content of the returned page
search_content
```


### EUtils Fetch, through Python



{:.input_area}
```python
print(fetch_url)
```




{:.input_area}
```python
# Request the fetch page, and parse
fetch_page = requests.get(fetch_url)
fetch_content = BeautifulSoup(fetch_page.content, 'lxml')
```




{:.input_area}
```python
# Check out the content of the page
# fetch_content
```


### BeautifulSoup Objects



{:.input_area}
```python
# Our 'fetch_content' variable is a custom BeautifulSoup object
type(fetch_content)
```




{:.input_area}
```python
# We can use some methods to access particular information
fetch_content.find('year').text
```


## Literature Scanner

But when making HTTP requests it can be difficult to figure out exactly what URL needs to be specified and how to get the contents back out.

So, often in Python we'll interact with an API indirectly. There are packages that will use methods and objects to make this easier on us.

**LISC** : Literature Scanner is a tool for automated meta-analyses of scientific literature (https://github.com/lisc-tools/lisc)



{:.input_area}
```python
# uncomment and run to have the following 
# example work in your notebook
# !pip install --user git+https://github.com/lisc-tools/lisc.git
# !pip install --user wordcloud
```




{:.input_area}
```python
# Import LISC - Words
from lisc.words import Words
```




{:.input_area}
```python
# Initialize Words object & set some search terms
words = Words()
words.set_terms(['brain']) 
```




{:.input_area}
```python
# Run words scrape
words.run_scrape(retmax='5')
```


### LISC: Words Data



{:.input_area}
```python
# Check out some information from our scraped data
for art in words['brain']:
    print(art['title'])
```




{:.input_area}
```python
%matplotlib inline
from lisc.plts.wc import make_wc
from lisc.data_all import DataAll
```




{:.input_area}
```python
## take a look at this function
make_wc?
```




{:.input_area}
```python
# Get the data from the 'brain' word search, and make a wordcloud
brain_dat = DataAll(words.results[0])
make_wc(brain_dat.word_freqs, 20, 'Brain')
```


## Twitter API



{:.input_area}
```python
# to use this on your computer
# uncomment and run following line
# !pip install tweepy
```


Then, follow the instructions [here](https://www.digitalocean.com/community/tutorials/how-to-authenticate-a-python-application-with-twitter-using-tweepy-on-ubuntu-14-04) for authetication of tweepy with Python.



{:.input_area}
```python
# Accessing Twitter API from Python
#  Note: to run this, you will have to fill in stw.py with your OAuth credentials.
#    You can do that here: https://apps.twitter.com/

# Import tweepy to access API
import tweepy
from tweepy import OAuthHandler

# Import my API credentials
from stw import *

# Twitter API requires Authentification with OAuth
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# # Create an API object to access Twitter
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(3):
    # Process a single status
    print(status.user.name)
    print(status.text, '\n')
```

