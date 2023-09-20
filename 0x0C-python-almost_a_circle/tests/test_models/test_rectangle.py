#!/usr/bin/python3
""" documentation for the test cases of the rectangle """


import unittest
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch
import os
import io

class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def test_rectangle_creation(self):
        """
        Test creating an instance of Rectangle.
        """
        rectangle = Rectangle(4, 5)
        self.assertIsInstance(rectangle, Base)
        self.assertIsInstance(rectangle, Rectangle)
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 5)

    def test_area_calculation(self):
        """
        Test calculating the area of a Rectangle.
        """
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.area(), 20)

    def test_display_method(self):
        """
        Test the display method of a Rectangle.
        """
        rectangle = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rectangle.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
