#!/usr/bin/python3
""" documentaion for the test cases of the square """


import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch
import os
import io

class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class.
    """

    def test_square_creation(self):
        """
        Test creating an instance of Square.
        """
        square = Square(5)
        self.assertIsInstance(square, Base)
        self.assertIsInstance(square, Rectangle)
        self.assertIsInstance(square, Square)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)

    def test_area_calculation(self):
        """
        Test calculating the area of a Square.
        """
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_display_method(self):
        """
        Test the display method of a Square.
        """
        square = Square(3)
        expected_output = "###\n###\n###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            square.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
