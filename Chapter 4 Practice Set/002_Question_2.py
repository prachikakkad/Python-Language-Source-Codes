# Question :-
""" Write a program to accept the marks
of 6 students and display them in
a sorted manner."""

m1 = int(input("Enter the marks of student 1 :- \n"))
m2 = int(input("Enter the marks of student 2 :- \n"))
m3 = int(input("Enter the marks of student 3 :- \n"))
m4 = int(input("Enter the marks of student 4 :- \n"))
m5 = int(input("Enter the marks of student 5 :- \n"))
m6 = int(input("Enter the marks of student 6 :- \n"))

marks_list = [m1, m2, m3, m4, m5, m6]
marks_list.sort()
print(marks_list)