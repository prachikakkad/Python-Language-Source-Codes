# Question :-
""" Modify your except block in Exercise 104 to fail silently if either file is missing."""

try :
    with open("Extra_file_for_Exercise_104_01.txt" , "r") as mode:
        print("Cat's Name :-")
        content = mode.readlines()
        for line in content:
            print(line.rstrip())

    with open("Extra_file_for_Exercise_104_02.txt" , "r") as mode:
        print("Dog's name :-")
        content = mode.readlines()
        for line in content:
            print(line.rstrip())

except FileNotFoundError:
    pass