#!/usr/bin/python3
"""This is a unittest for the class State that inherits from BaseModel"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test case for the State class"""

    def test_init(self):
        """Test the __init__ method of the State class"""
        state = State()
        self.assertIsInstance(state, State)

    def test_name(self):
        """Test the name attribute of the State class"""
        state = State()
        self.assertEqual(state.name, "")
        state.name = "California"
        self.assertEqual(state.name, "California")


if __name__ == '__main__':
    unittest.main()
