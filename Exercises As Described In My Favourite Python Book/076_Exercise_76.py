# Question :-
""" Start with your work from Exercise 75. Call the function make_great() with a copy of the list of magician's names. Because the original list will be unchanged, return the new list and store it in a separate list.Call show_magicians() with each list to show that you have one list of the original names and one list with the Great added to each magician's name. """

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)

    return magicians # new line added

magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)
print()

# Other Lines added
print("Great magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print()

print("Original magicians:")
show_magicians(magicians)