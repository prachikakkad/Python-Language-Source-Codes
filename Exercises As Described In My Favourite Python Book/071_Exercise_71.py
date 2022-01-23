# Question :-
""" Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value that's returned."""

def city_country(name_of_city , name_of_country):
    return name_of_city + " , " +  name_of_country

city = city_country("Mumbai" , "India")
print(city)

city = city_country("London" , "England")
print(city)

city = city_country("Ushuaia" , "Argentina")
print(city)