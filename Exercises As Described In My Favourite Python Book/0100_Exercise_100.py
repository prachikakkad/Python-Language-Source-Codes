# Question :-
""" Write a while loop that prompts users for their name. When they enter their name , print a greeting to the screen and add a line recording their visit in a file. Make sure each entry appears on a new line in the file. """

while True:
    ask = input("Enter your name\nEnter 'quit' when you are done :-\n")
    if "quit" in ask:
        exit()
    else:
        with open("Extra_file_for_Exercise_100.txt" , "a") as mode:
            mode.write(f"{ask}\n")
        print(f"Welcome {ask} !")
