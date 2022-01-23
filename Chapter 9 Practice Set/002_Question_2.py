# Question :-
"""The game() function in a program lets a user play
a game and returns the score as an integer. You need to
read a file “Hiscore.txt” which is either blank or
contains the previous Hi-score. You need to write a
program to update the Hi-score whenever game() breaks
the Hi-Score."""


def game():
    return 33


score = game()

with open("Hiscore.txt") as file:
    hiscore = file.read()

if hiscore == '':
    with open("Hiscore.txt", 'w') as file:
        file.write(str(score))

elif score > int(hiscore):
    with open("Hiscore.txt", 'w') as file:
        file.write(str(score))