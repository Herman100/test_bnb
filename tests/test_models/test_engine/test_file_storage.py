#!/usr/bin/python3
"""This is a test module for the base model class"""


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


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


if __name__ == '__main__':
    unittest.main()
