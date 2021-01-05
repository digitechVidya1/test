"""
It provides some very useful features for Machine Learning projects like:

Noun phrase extraction
Part-of-speech tagging
Sentiment analysis
Classification
Tokenization
Word and phrase frequencies
Parsing
n-grams
Word inflexion and lemmatization
Spelling correction
Add new models or languages through extensions
WordNet integration
You can simply install the TextBlob library in your systems by writing a pip command; pip install textblob.
"""
from textblob import TextBlob

words = ["deta","analyeis"]

correct_word = []

for i in words:
    correct_word.append(TextBlob(i))

print("Wrong words: ",words)
print("Correct Words are: ")

for i in correct_word:
    print(i.correct(),end=" ")