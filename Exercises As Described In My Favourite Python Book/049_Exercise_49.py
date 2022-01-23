# Question :-
"""Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile' : 'egypt'.
•	 Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
•	 Use a loop to print the name of each river included in the dictionary.
•	 Use a loop to print the name of each country included in the dictionary."""


river_dictionary = {"Nile" : "Egypt" , "Yamuna" : "India" , "Thames" : "England"}

for key , value in river_dictionary.items():
    print(f"{key} runs through {value}.")

print()

for key in river_dictionary.keys():
    print(key)

print()

for value in river_dictionary.values():
    print(value)

print()