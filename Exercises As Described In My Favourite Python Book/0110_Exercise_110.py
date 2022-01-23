# Question :-
""" Modify your function of Exercise 109 so it requires a third parameter, population. It should now return a single string of the form City, Country - population xxx, such as Delhi, India - population 5000000. Run test_cities.py again. Make sure test_city_country() fails this time. Modify the function so the population parameter is optional. Run test_cities.py again, and make sure test_city_country() passes again. Write a second test called test_city_country_population() that verifies you can call your function with the values 'Delhi', 'India', and 'population=5000000'. Run test_cities.py again, and make sure this new test passes."""

import unittest

from Extra_file_for_Exercise_110 import city_country

class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        """Does a simple city and country pair work?"""
        Delhi_India = city_country('delhi', 'india')
        self.assertEqual(Delhi_India, 'Delhi, India')

    def test_city_country_population(self):
        """Can I include a population argument?"""
        Delhi_India = city_country('delhi', 'india', population=5000000)
        self.assertEqual(Delhi_India, 'Delhi, India - population 5000000')

unittest.main()