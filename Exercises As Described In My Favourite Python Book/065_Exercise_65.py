# Question :-
""" Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world , where would you go? Include a block of code that prints the results of the poll. """

name_prompt = "What's your name ?\n"
place_prompt = "If you could visit one place in the world, where would it be ?\n"
continue_prompt = "Would you like to let someone else respond ? (yes/no)\n"

responses = {}

while True:
    name = input(name_prompt)
    place = input(place_prompt)

    responses[name] = place

    repeat = input(continue_prompt)

    if repeat == "no":
        break

    elif repeat != "yes" and repeat != "no":
        continue

    else:
        continue

print("--- Results ---")

for name, place in responses.items():
    print(name.title() + " would like to visit " + place.title() + ".")