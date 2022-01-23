# Question :-
"""If the names of 2 friends are the same;
what will happen to the program in Program 6?

Answer :- Sonali will be removed from the dictionary because
I have not added her name into the keys. And whatever
I input in 'c' variable will be the final value of shubham.
That means the latest updated will will be counted as final."""


favLang = {}
a = input("Enter your favorite language Shubham\n")
b = input("Enter your favorite language Ankit\n")
c = input("Enter your favorite language Shubham\n")
d = input("Enter your favorite language Harshita\n")
favLang['shubham'] = a
favLang['ankit'] = b
favLang['shubham'] = c
favLang['harshita'] = d

print(favLang)