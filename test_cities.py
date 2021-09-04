import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        city_country_name = city_country('sydney', 'australia')
        self.assertEqual(city_country_name, 'Sydney, Australia')

    def test_city_country_population(self):
        city_country_population_name = city_country('sydney', 'australia', 50000)
        # self.assertEqual(city_country_population_name, 'Sydney, Australia - Population 50000')
        self.assertEqual('Sydney, Australia - Population 50000', city_country_population_name)

if __name__ == '__main__':
    unittest.main()