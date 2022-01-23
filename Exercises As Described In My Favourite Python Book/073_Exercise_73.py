# Question :-
"""Start with your program from Exercise 72. Write a while loop that allows users to enter an album's artist and title. Once you have that information, call make_album() with the user's input and print the dictionary that's created. Be sure to include a quit value in the while loop."""

def make_album(artist , title):
    music_album = {artist : title}
    return music_album


while True:
    details_1 = input("Enter the name of artist:-\n")
    details_2 = input("Enter the name of song:-\n")

    output = make_album(details_1 , details_2)
    print(output)
    
    ask = input("Would you like to add one more song to the list ? (yes/no)\n")

    if ask == "no":
        break

    elif ask != "yes" and ask != "no":
        continue

    else:
        continue
