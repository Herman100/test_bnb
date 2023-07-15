#!/usr/bin/python3
"""This is a unittest code that tests the base model class"""


import unittest
from models.base_model import BaseModel
from models import storage
import os


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def setUp(self):
        """Set up test cases"""
        self.base_model = BaseModel()

    def tearDown(self):
        """Clean up after test cases"""
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_init(self):
        """Test the __init__ method"""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsNotNone(self.base_model.id)
        self.assertIsNotNone(self.base_model.created_at)
        self.assertIsNotNone(self.base_model.updated_at)

    def test_str(self):
        """Test the __str__ method"""
        expected_str = "[{}] ({}) {}".format(
                self.base_model.__class__.__name__,
                self.base_model.id,
                self.base_model.__dict__
                )
        self.assertEqual(str(self.base_model), expected_str)

    def test_save(self):
        """Test the save method"""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertTrue(os.path.exists(storage._FileStorage__file_path))

    def test_to_dict(self):
        """Test the to_dict method"""
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict["__class__"], "BaseModel")
        self.assertEqual(base_model_dict["id"], self.base_model.id)
        self.assertEqual(base_model_dict["created_at"],
                         self.base_model.created_at.isoformat())
        self.assertEqual(base_model_dict["updated_at"],
                         self.base_model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
