# Question :-
"""Start with the program you wrote for Exercise 45. Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person."""

details_1 = {"first_name" : "Prachi" , 
           "last_name" : "Kakkad" , 
           "age" : 15 , 
           "town" : "Upleta"}

details_2 = {"first_name" : "Naveen" , 
           "last_name" : "Goyat" , 
           "age" : 21 , 
           "town" : "Bhiwani"}

people = [details_1 , details_2]

for detail in people:
    name = detail['first_name'].title() + " " + detail['last_name'].title()
    age = str(detail['age'])
    city = detail['town'].title()
    
    print(name + " is " + age + " years old and hometown is " + city + ".")