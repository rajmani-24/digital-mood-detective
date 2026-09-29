from datetime import datetime
import re

# -----------------------------
# DIGITAL MOOD DETECTIVE
# -----------------------------

print("=" * 45)
print("        DIGITAL MOOD DETECTIVE")
print("=" * 45)

print("\nAnswer the following questions naturally.\n")

# Take input
name = input("What is your name? ")
day = input("How was your day? ")
thoughts = input("What is on your mind right now? ")
activity = input("What did you do today? ")

# Combine all text
text = day + " " + thoughts + " " + activity

# Convert to lowercase
lower_text = text.lower()

# -----------------------------
# MOOD WORD DATABASE
# -----------------------------

positive_words = [
    "happy", "good", "great", "amazing", "awesome",
    "excited", "love", "fun", "nice", "best",
    "wonderful", "excellent", "joy", "enjoy", "proud"
]

negative_words = [
    "sad", "bad", "angry", "hate", "tired",
    "stress", "stressed", "worried", "upset",
    "lonely", "boring", "bored", "pain", "cry"
]

# Count words
positive_count = 0
negative_count = 0

for word in positive_words:
    positive_count += lower_text.count(word)

for word in negative_words:
    negative_count += lower_text.count(word)

# -----------------------------
# TEXT ANALYSIS
# -----------------------------

total_words = len(re.findall(r'\b\w+\b', text))

exclamation_count = text.count("!")
question_count = text.count("?")

capital_count = sum(1 for char in text if char.isupper())

# -----------------------------
# MOOD CALCULATION
# -----------------------------

score = 50

score += positive_count * 8
score -= negative_count * 8
score += exclamation_count * 2

# Keep score between 0 and 100
score = max(0, min(100, score))

# Determine mood
if score >= 75:
    mood = "EXCITED 😄"
elif score >= 60:
    mood = "HAPPY 🙂"
elif score >= 45:
    mood = "NEUTRAL 😐"
elif score >= 30:
    mood = "STRESSED 😟"
else:
    mood = "LOW 😔"

# -----------------------------
# DISPLAY RESULT
# -----------------------------

print("\n" + "=" * 45)
print("             YOUR RESULTS")
print("=" * 45)

print(f"\nName: {name}")
print(f"Words written: {total_words}")
print(f"Positive words: {positive_count}")
print(f"Negative words: {negative_count}")
print(f"Exclamation marks: {exclamation_count}")
print(f"Questions asked: {question_count}")
print(f"Capital letters: {capital_count}")

print("\n---------------------------------------------")
print(f"Estimated Mood : {mood}")
print(f"Mood Score     : {score}/100")
print("---------------------------------------------")

# -----------------------------
# PERSONALIZED MESSAGE
# -----------------------------

if score >= 75:
    message = "You seem to have a lot of positive energy today! 🚀"

elif score >= 60:
    message = "Looks like you're having a pretty good day! 😊"

elif score >= 45:
    message = "Your mood seems fairly balanced today. 😐"

elif score >= 30:
    message = "You seem to have some stress on your mind. Take a break if you can."

else:
    message = "You seem to be having a difficult day. Be kind to yourself."

print("\nDigital Mirror:")
print(message)

print("\n" + "=" * 45)
print("Analysis completed!")
print("=" * 45)