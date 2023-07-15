#!/usr/bin/python3
"""This is a unittest code that tests the console module"""

import unittest
from console import HBNBCommand
from io import StringIO
import sys
from unittest.mock import patch


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

    def test_create(self):
        """Test the create command"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create")
            self.assertEqual(output.getvalue().strip(),
                             "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(output.getvalue().strip(),
                             "** class doesn't exist **")

    def test_show(self):
        """Test the show command"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show")
            self.assertEqual(output.getvalue().strip(),
                             "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(output.getvalue().strip(),
                             "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("show MyModel 1234-5678-9012")
            self.assertEqual(output.getvalue().strip(),
                             "** class doesn't exist **")

    def test_destroy(self):
        """Test the destroy command"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(output.getvalue().strip(),
                             "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(output.getvalue().strip(),
                             "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("destroy MyModel 1234-5678-9012")
            self.assertEqual(output.getvalue().strip(),
                             "** class doesn't exist **")

    def test_all(self):
        """Test the all command"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all MyModel")
            self.assertEqual(output.getvalue().strip(),
                             "** class doesn't exist **")


if __name__ == '__main__':
    unittest.main()
