# Question :-
""" Open a blank file in your text editor and write a few lines summarizing what you've learned about Python so far. Start each line with the phrase :-
In Python you can.... 
Save the file in the same directory as your exercises from this chapter. Write a program that reads the file and prints what you wrote three times. Print the contents once by reading in the entire file, once by looping over the file object, and once by storing the lines in a list and then working with them outside the with block."""

with open("Extra_file_for_Exercise_96.txt" , "r") as mode:
    content = mode.read()
print("Reading Entire File :-")
print(content)

print()

with open("Extra_file_for_Exercise_96.txt" , "r") as mode:
    print("By looping :-")
    for line in mode:
        print(line.rstrip())

print()

with open("Extra_file_for_Exercise_96.txt" , "r") as mode:
    content = mode.readlines()
    print("By storing lines in a list :-")
    for line in content:
        print(line.rstrip())