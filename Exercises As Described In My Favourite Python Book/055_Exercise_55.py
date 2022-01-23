# Question :-
""" Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city's dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it."""

cities = {"Mumbai" : {"country" : "India" , "population" : "20.82 Million" , "fact" : "Most celebrities of India live in this city."} ,
          "Bhiwani" : {"country" : "India" , "population" : "4.399 Million" , "fact" : "Kabaddi Star Naveen Kumar Goyat belongs to this district."} ,
          "Kashmir" : {"country" : "India" , "population" : "10 Million" , "fact" : "It is known as heaven of Earth."}
          }

for city  , city_information in cities.items():
    country = city_information["country"].title()
    population = city_information["population"]
    fact = city_information["fact"]

    print(f"{city} is situated in {country}.")
    print(f"It's approximate population is {population}.")
    print(f"{fact}")
    print("\n")