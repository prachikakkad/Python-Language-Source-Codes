# Question :-
"""A file contains the word “Donkey” multiple times. You need to write a
program which replaces this word with ###### by updating the same file."""

with open("question4.txt", 'r') as file:
     a = file.read()

a = a.replace("######", "Donkey")


with open("question4.txt", 'w')as f:
    f.write(a)