# Question :-
"""Write a program to read the text from a given file, “poem.txt”
and find out whether it contains the word ‘twinkle’."""

file = open("poem.txt", 'r')
a = file.read()

if 'twinkle' in a:
    print("'twinkle' word is present in the file")
else:
    print("'twinkle' word is not present in the file")

file.close()