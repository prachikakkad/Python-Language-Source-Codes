# Question :-
"""Write a function that accepts two parameters :- a city name and a country name. The function should return a single string of the form City, Country, such as Santiago, Chile. Store the function in a module. Create a file that tests the function you just wrote (remember that you need to import unittest and the function you want to test). Write a method called test_city_country() to verify that calling your function with values such as 'santiago' and 'chile' results in the correct string. Run test_cities.py, and make sure test_city_country() passes."""

import unittest

from Extra_file_for_Exercise_109 import city_country

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        delhi_india = city_country('delhi' , 'india')
        self.assertEqual(delhi_india, 'Delhi, India')

unittest.main()