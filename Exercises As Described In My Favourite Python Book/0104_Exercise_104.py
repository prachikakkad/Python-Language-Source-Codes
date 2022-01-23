# Question :-
""" Make two files , Store at least three names of cats in the first file and three names of dogs in the second file. Write a program that tries to read these files and print the contents of the file to the screen. Wrap your code in a try-except block to catch the FileNotFound error , and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block executes properly."""

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
    print("The file doesn't Exist !")