# Question :-
""" Write a program that prompts for the user's favorite number. Use json.dump() to store this number in a file.Then read the file and print the message, "I know your favorite number ! It's __________ !" """

import json

fav_num = input("Enter your favourite number :-\n")
fav_num = int(fav_num)
with open("Extra_file_for_Exercise_107.txt" , "w") as mode:
    json.dump(fav_num , mode)

with open("Extra_file_for_Exercise_107.txt" , "r") as mode:
    variable = json.load(mode)
    print(f"I know ypur favourite number ! It's {variable} !")