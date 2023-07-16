#!/usr/bin/python3
"""This module is a unittest for class City that inherits from BaseModel"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test case for the City class"""

    def test_init(self):
        """Test the __init__ method of the City class"""
        city = City()
        self.assertIsInstance(city, City)

    def test_name(self):
        """Test the name attribute of the City class"""
        city = City()
        self.assertEqual(city.name, "")
        city.name = "San Francisco"
        self.assertEqual(city.name, "San Francisco")

    def test_state_id(self):
        """Test the state_id attribute of the City class"""
        city = City()
        self.assertEqual(city.state_id, "")
        city.state_id = "CA"
        self.assertEqual(city.state_id, "CA")


if __name__ == '__main__':
    unittest.main()
