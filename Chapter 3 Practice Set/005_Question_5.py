# Question :-
"""Write a program to format the
following letter using escape sequence
characters.
letter = “Dear Harry,  This Python course in nice.  Thanks!!”
"""

letter = '''Dear Harry,  This Python course in nice.  Thanks!!'''
print("Before replacing :-")
print(letter)
letter = letter.replace("  ", "\n")
letter = letter.replace("  ", "\n")
print("After replacing :-")
print(letter)
