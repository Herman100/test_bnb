#!/usr/bin/python3
"""This is a unittest code that tests the console module"""

import unittest
from console import HBNBCommand
from io import StringIO
import sys


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

    def test_emptyline(self):
        """Test that an empty line doesn't execute anything"""
        hbnb = HBNBCommand()
        output = StringIO()
        sys.stdout = output
        hbnb.onecmd('\n')
        self.assertEqual(output.getvalue(), '')
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()
