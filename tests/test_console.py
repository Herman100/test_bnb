#!/usr/bin/python3
"""This is a unittest code that tests the console module"""

import unittest
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test the HBNBCommand class"""

    def test_do_quit(self):
        """Test the quit method"""
        hbnb = HBNBCommand()
        self.assertEqual(hbnb.do_quit(''), True)

    def test_do_EOF(self):
        """Test the do_eof method"""
        hbnb = HBNBCommand()
        self.assertEqual(hbnb.do_EOF(''), True)


if __name__ == '__main__':
    unittest.main()
