# Question :-
"""Use the count function to check how many times a word occurs in string which is stored in a particular file. Here is how you can use count function :-
>>> line = "Row, row, row your boat"
>>> line.count('row')
2
>>> line.lower().count('row')
3 
Notice that converting the string to lowercase using lower() catches all appearances of the word you're looking for, regardless of how it's formatted.
Write a program that reads the file you created and determines how many times the word 'the' appears in each text."""

with open("Extra_file_for_Exercise_106.txt" , "r") as mode:
        content = mode.read()
        counts = content.lower().count("the")
        print(counts)