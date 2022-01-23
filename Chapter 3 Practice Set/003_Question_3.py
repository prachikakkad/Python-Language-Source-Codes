# Question :-
''' Write a program to detect double spaces
in a string.'''

string1 = "This is a string with double  spaces in it."
string2 = "This is a string without double spaces in it."

DoubleSpaces1 = string1.find("  ")
print(DoubleSpaces1)

DoubleSpaces2 = string2.find("  ")
print(DoubleSpaces2)