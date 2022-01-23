# Question :-
"""Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. Loop through the dictionary , and print each person's name and their favorite places."""

favourite_places = {"Naveen Goyat" : "Haryana" , 
                    "Prachi Kakkad" : "Haryana and Kashmir" ,
                    "Rahul Vaidya" : "Maharashtra"}

for key , value in favourite_places.items():
    print(f"{key}'s favourite place is {value}.")