#!/usr/bin/python3
""" documentation for the test cases of the base problem """


import unittest
from models.base import Base
import json

class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def test_create_instance_with_id(self):
        """
        Test creating an instance of Base with a specified id.
        """
        base = Base(42)
        self.assertEqual(base.id, 42)

    def test_create_instance_without_id(self):
        """
        Test creating an instance of Base without specifying an id.
        """
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_create_instance_with_negative_id(self):
        """
        Test creating an instance of Base with a negative id.
        """
        base = Base(-42)
        self.assertEqual(base.id, -42)

    def test_create_instance_with_string_id(self):
        """
        Test creating an instance of Base with a string id.
        """
        base = Base("hello")
        self.assertEqual(base.id, "hello")

    def test_to_json_string_with_empty_list(self):
        """
        Test converting an empty list of dictionaries to JSON string.
        """
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_with_list_of_dicts(self):
        """
        Test converting a list of dictionaries to JSON string.
        """
        data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        json_str = Base.to_json_string(data)
        expected_json_str = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        self.assertEqual(json_str, expected_json_str)


if __name__ == '__main__':
    unittest.main()
