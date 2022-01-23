# Question :-
""" Modify your program from Exercise 46 so each person can have more than one favorite number. Then print each person's name along with their favorite numbers."""

favourite_numbers = {"Naveen Kumar Goyat" : "10 and 4" , 
                     "Prachi" : "14 and 10" , 
                     "Rahul" : "23 and 16" , 
                     "Mumma" : "13 and 28" , 
                     "Sister" : "18 and 8"}

for key , value in favourite_numbers.items():
    print(f"{key}'s favourite numbers are {value}.")