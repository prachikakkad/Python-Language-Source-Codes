# Question :-
""" Write a program to generate multiplication tables
from 1 to 20 and write it to the different files.
Place these files in a folder for a 13-year-old boy."""

for i in range(1, 21):
    with open(f"Tables/Table of {i}.txt", 'w') as file:
        for j in range(1, 11):
            file.write(f"{i} X {j} = {i*j}\n")
