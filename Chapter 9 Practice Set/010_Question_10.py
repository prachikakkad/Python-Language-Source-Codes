# Question :-
"""Write a python program to rename a file to
“renamed_by_python.txt.”"""


import os

oldname = "C:\\Users\\hp\\Desktop\\Programming Language Source Codes\\Python Language\\Chapter 9 Practice Set\\sample.txt"
newname = "renamed_by_python.txt"
with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:
    f.write(content)

os.remove(oldname)