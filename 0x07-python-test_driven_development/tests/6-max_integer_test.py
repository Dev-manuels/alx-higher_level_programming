#!/usr/bin/python3
"""
Module containing unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class Test_max_integer(unittest.TestCase):
    """Test_max_integer

       Tests normal case max_integer(valid positive int lists)
       Tests normal case max_integer(valid negative int lists)
       Tests normal case max_integer(valid positive float lists)
    """
    def test_normal_case(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, 0]), 0)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([11.2, 2.6, 3.9, 4.3]), 11.2)
        self.assertEqual(max_integer([-11.2, -2.6, -3.9, -4.3]), -2.6)
        self.assertEqual(max_integer([11.2]), 11.2)
        self.assertEqual(max_integer([-4.3]), -4.3)

    def test_empty_list(self):
        self.assertEqual(max_integer(), None)
