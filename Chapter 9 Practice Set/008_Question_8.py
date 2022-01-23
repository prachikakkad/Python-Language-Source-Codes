# Question :-
"""Write a program to find out whether a file is
identical and matches the content of another file."""

with open("poem.txt", 'r') as file1:
    f1 = file1.read()
with open("copyofpoem.txt", 'r') as file2:
    f2 = file2.read()

if f1 == f2:
    print("Both the files are identical !")
else:
    print("Both the files are not identical !")