#!/usr/bin/python3
"""This is unittest for class Review that inherits from BaseModel"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test case for the Review class"""

    def test_init(self):
        """Test the __init__ method of the Review class"""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_attributes(self):
        """Test the attributes of the Review class"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

        review.place_id = "1234"
        review.user_id = "abcd"
        review.text = "Great place!"

        self.assertEqual(review.place_id, "1234")
        self.assertEqual(review.user_id, "abcd")
        self.assertEqual(review.text, "Great place!")


if __name__ == '__main__':
    unittest.main()
