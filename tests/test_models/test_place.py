#!/usr/bin/python3
"""This is unittest for class Place that inherits from BaseModel"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test case for the Place class"""

    def test_init(self):
        """Test the __init__ method of the Place class"""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_attributes(self):
        """Test the attributes of the Place class"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.state_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

        place.city_id = "1234"
        place.state_id = "5678"
        place.user_id = "abcd"
        place.name = "My Place"
        place.description = "A cozy little place"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["efgh", "ijkl"]

        self.assertEqual(place.city_id, "1234")
        self.assertEqual(place.state_id, "5678")
        self.assertEqual(place.user_id, "abcd")
        self.assertEqual(place.name, "My Place")
        self.assertEqual(place.description, "A cozy little place")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["efgh", "ijkl"])


if __name__ == '__main__':
    unittest.main()
