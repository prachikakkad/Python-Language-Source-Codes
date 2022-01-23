# Question :-
"""A movie theater charges different ticket prices depending on a person's age. If a person is under the age of 3, the ticket is free ; if they are between 3 and 12, the ticket is $10 ; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket."""

while True:
    age = input("What is your age ?\n")
    age = int(age)

    if age <= 3 and age > 0:
        print("The ticket is free for you.")

    elif age > 3 and age < 12:
        print("The cost of ticket for you is $10.")

    elif age > 12:
        print("The cost of ticket for you is $15.")

    else:
        print(f"Enter VALID age. {age} is INVALID !")