# Question :-
"""Choose a color for an alien as you did in Exercise 36 , and write an if-else chain.
•	 If the alien's color is green, print a statement that the player just earned 5 points for shooting the alien.
•	 If the alien's color isn't green, print a statement that the player just earned 10 points.
•	 Write one version of this program that runs the if block and another that runs the else block."""

alien_color = "yellow"

if alien_color == "green":
    print("Congratulations ! You have earned 5 points.")

else:
    print("Congratulations ! You have earned 10 points.")

# Version 1

alien_color = "yellow"

if alien_color == "yellow":
    print("Congratulations ! You have earned 5 points.")

else:
    print("Congratulations ! You have earned 10 points.")

# Version 2
alien_color = "yellow"

if alien_color == "red":
    print("Congratulations ! You have earned 5 points.")

else:
    print("Congratulations ! You have earned 10 points.")