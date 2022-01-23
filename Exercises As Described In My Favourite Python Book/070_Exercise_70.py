# Question :-
""" Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country. """

def describe_city(name_of_city , name_of_country = "India"):
    print(f"{name_of_city} is in {name_of_country}.")

describe_city("Upleta")
describe_city("Bhiwani")
describe_city("London" , name_of_country="England")