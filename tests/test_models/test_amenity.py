#!/usr/bin/python3
"""This is unittest for class Amenity that inherits from BaseModel"""


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test case for the Amenity class"""

    def test_init(self):
        """Test the __init__ method of the Amenity class"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_name(self):
        """Test the name attribute of the Amenity class"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        amenity.name = "Pool"
        self.assertEqual(amenity.name, "Pool")


if __name__ == '__main__':
    unittest.main()
