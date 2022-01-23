# Question :-
""" Write a while loop that asks people why they like programming. Each time someone enters a reason, add their reason to a file that stores all the responses. """

while True:
    ask = input("Can you tell us why do you like programming ? \nEnter 'quit' when you are done !\n")
    if "quit" in ask:
        exit()
    else:
        with open("Extra_file_for_Exercise_101.txt" , "a") as mode:
            mode.write(f"{ask}\n")
            print("Your response has been stored !")