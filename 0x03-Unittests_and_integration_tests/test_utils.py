#!/usr/bin/env python3
"""
Module test_utils
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test Class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests utils.access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
        ])
    def test_access_nested_map_exception(self, nested_map, path, err):
        """Tests utils.access_nested_map for KeyError"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path) == err


if __name__ == '__main__':
    """Main entry"""
    unittest.main()
