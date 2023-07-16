#!/usr/bin/python3
"""This is a test module for the base model class"""


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Set up test cases"""
        self.storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        """Clean up after test cases"""
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all(self):
        """Test the all method"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test the new method"""
        self.storage.new(self.base_model)
        key = "{}.{}".format(self.base_model.__class__.__name__,
                             self.base_model.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test the save method"""
        self.storage.new(self.base_model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload(self):
        """Test the reload method"""
        self.storage.new(self.base_model)
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(self.base_model.__class__.__name__,
                             self.base_model.id)
        self.assertIn(key, self.storage.all())

    def test_new_user(self):
        """Test that new method correctly adds User instances"""
        user = User()
        self.storage.new(user)
        key = "{}.{}".format(user.__class__.__name__, user.id)
        self.assertIn(key, self.storage.all())

    def test_new_state(self):
        """Test that new method correctly adds State instances"""
        state = State()
        self.storage.new(state)
        key = "{}.{}".format(state.__class__.__name__, state.id)
        self.assertIn(key, self.storage.all())

    def test_new_city(self):
        """Test that new method correctly adds City instances"""
        city = City()
        self.storage.new(city)
        key = "{}.{}".format(city.__class__.__name__, city.id)
        self.assertIn(key, self.storage.all())

    def test_new_amenity(self):
        """Test that new method correctly adds Amenity instances"""
        amenity = Amenity()
        self.storage.new(amenity)
        key = "{}.{}".format(amenity.__class__.__name__, amenity.id)
        self.assertIn(key, self.storage.all())

    def test_new_place(self):
        """Test that new method correctly adds Place instances"""
        place = Place()
        self.storage.new(place)
        key = "{}.{}".format(place.__class__.__name__, place.id)
        self.assertIn(key, self.storage.all())

    def test_new_review(self):
        """Test that new method correctly adds Review instances"""
        review = Review()
        self.storage.new(review)
        key = "{}.{}".format(review.__class__.__name__, review.id)
        self.assertIn(key, self.storage.all())

    def test_reload_with_new_classes(self):
        """Test that reload method correctly
        handles instances of new classes"""
        state = State()
        city = City()
        amenity = Amenity()
        place = Place()
        review = Review()

        self.storage.new(state)
        self.storage.new(city)
        self.storage.new(amenity)
        self.storage.new(place)
        self.storage.new(review)

        state_key = "{}.{}".format(state.__class__.__name__, state.id)
        city_key = "{}.{}".format(city.__class__.__name__, city.id)
        amenity_key = "{}.{}".format(amenity.__class__.__name__, amenity.id)
        place_key = "{}.{}".format(place.__class__.__name__, place.id)
        review_key = "{}.{}".format(review.__class__.__name__, review.id)

        self.storage.save()
        self.storage.reload()

        self.assertIn(state_key, self.storage.all())
        self.assertIn(city_key, self.storage.all())
        self.assertIn(amenity_key, self.storage.all())
        self.assertIn(place_key, self.storage.all())
        self.assertIn(review_key, self.storage.all())


if __name__ == '__main__':
    unittest.main()
