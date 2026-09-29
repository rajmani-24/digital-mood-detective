🧠 Digital Mood Detective

**Digital Mood Detective**--- is a Python-based text analysis project developed by **Rajmani**.

The program estimates a user's mood by analyzing their written responses. Instead of directly asking the user about their mood, it examines their text for positive and negative words, punctuation, capitalization, and other basic writing patterns.

---
 📌 Project Description

The Digital Mood Detective collects responses from the user and analyzes the entered text using Python.

It detects positive and negative words, calculates a **Mood Score between 0 and 100**, and then classifies the estimated mood into different categories such as:

* 😄 Excited
* 🙂 Happy
* 😐 Neutral
* 😟 Stressed
* 😔 Low

After determining the estimated mood, the program also displays a personalized message based on the result.

---
 🎯 Objective

The main objective of this project is to demonstrate how Python can be used for basic **text analysis and sentiment-based processing**.

The project combines several fundamental programming concepts to create an interactive and practical application.

---
⚙️ Working Concept

The program follows this process:

   text
User Input
    ↓
Text Collection
    ↓
Text Processing
    ↓
Positive & Negative Word Detection
    ↓
Mood Score Calculation
    ↓
Mood Classification
    ↓
Personalized Result


Positive words increase the mood score, while negative words decrease it. Additional factors such as exclamation marks and writing patterns are also considered.

The final score is restricted between **0 and 100**.


 🐍 Concepts Used

The project uses the following Python concepts:

* Variables
* User Input and Output
* Strings
* Lists
* `for` Loops
* Conditional Statements
* Arithmetic Operations
* String Manipulation
* Regular Expressions
* Built-in Python Modules
* Basic Text Analysis

---
 📚 Libraries Used

The project primarily uses Python's built-in libraries:

### `re`

Used for identifying and counting words in the user's text.

### `datetime`

Used for working with date and time information and can support future mood-tracking features.

No external libraries are required for the basic version.

 🖥️ Example:-

=============================================
        DIGITAL MOOD DETECTIVE
=============================================

What is your name? Raj

How was your day?
Amazing! I had a great day!

What is on your mind?
I am excited about my project!

What did you do today?
I worked on my Python program and had fun!

=============================================
             YOUR RESULTS
=============================================

Name: Raj
Words written: 24
Positive words: 5
Negative words: 0
Exclamation marks: 3

---------------------------------------------
Estimated Mood : EXCITED
Mood Score     : 96/100
---------------------------------------------

Digital Mirror:
You seem to have a lot of positive energy today

---
 🚀 Future Improvements

The project can be enhanced in the future by adding:

* Graphical User Interface (GUI)
* Mood history and daily tracking
* Mood graphs using Matplotlib
* Advanced Natural Language Processing (NLP)
* More emotion categories
* Long-term mood trend analysis
* Voice-based input
* AI-based sentiment analysis

 ⚠️ Disclaimer

The mood detected by this program is only an **approximation based on text patterns**. It should not be considered a scientific, psychological, or medical assessment.


## 👤 Author

**Rajmani**

-- Project: Digital Mood Detective

-- Language: Python

-- Type: Text Analysis / Sentiment-Based Project
