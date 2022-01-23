# Question :-
""" A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let's call it a glossary.
•	 Think of five programming words you've learned about. Use these words as the keys in your glossary, and store their meanings as values.
•	 Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output. """

glossary = {"Python" : "Overall all-rounder language." , 
            "HTML" : "Language used for creating basic web page designs." , 
            "C++" : "Language used for game development." , 
            "Java" : "Language used for Android Development." , 
            "CSS" : "Language used for making webpage look more better."}

word1 = "Python"
print(f"{word1.title()} : {glossary[word1]}")

word2 = "HTML"
print(f"{word2.title()} : {glossary[word2]}")

word3 = "C++"
print(f"{word3.title()} : {glossary[word3]}")

word4 = "Java"
print(f"{word4.title()} : {glossary[word4]}")

word5 = "CSS"
print(f"{word5.title()} : {glossary[word5]}")