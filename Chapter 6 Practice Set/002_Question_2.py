# Question :-
""" Write a program to find out whether a student is pass or fail if it requires
a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user."""

English = int(input("Enter your marks in English out of 100 :-\n"))
Maths = int(input("Enter your marks in Maths out of 100 :-\n"))
Science = int(input("Enter your marks in Science out of 100 :-\n"))
total = English + Maths + Science

if English > 100 or Maths > 100 or Science > 100:
    print("Don't Be Oversmart ! Enter VALID Marks")
    print("Restart the program and Enter VALID Marks !")

elif total >= 40 and English >= 33 and Maths >= 33 and Science >= 33:
    print("Congratulations ! You are passed !")

else:
    print("Sorry ! You are failed !")