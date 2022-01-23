# Question :-
"""Write a program to find out the line number where
 python is present from question 5."""

content = True
i = 1
with open("log.txt", 'r') as file:
    while content:
        content = file.readline()
        if "python" in content:
            print(content)
            print(f"The word 'python' is present in {i} line")
        i += 1

