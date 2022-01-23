# Question :-
""" Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you'd like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once."""

languages = ["C" , "C++" , "Javascript" , "Django" , "PHP" , "HTML" , "CSS" , "Ruby"]

languages.append("Python")

languages.insert(9 , "Java")

del languages[0]

languages.pop(0)

languages.remove("Ruby")

print(sorted(languages))

print(languages)

languages.sort()

print(languages)

languages.reverse()

print(languages)

print(len(languages))