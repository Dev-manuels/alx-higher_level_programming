"""
Module containing unittests for Square class
"""
import io
import unittest
from models.square import Square
from unittest.mock import patch


class TestSquare(unittest.TestCase):

    def test_square_constructor(self):
        sqr = Square(10)
        self.assertEqual(sqr.height, 10)
        self.assertEqual(sqr.width, 10)
        self.assertEqual(sqr.x, 0)
        self.assertEqual(sqr.y, 0)

    def test_square_constructor_with_id(self):
        sqr = Square(5, 1, 1, 10)
        self.assertEqual(sqr.height, 5)
        self.assertEqual(sqr.width, 5)
        self.assertEqual(sqr.x, 1)
        self.assertEqual(sqr.y, 1)
        self.assertEqual(sqr.id, 10)

    def test_square_setters(self):
        """test_square_setters
        test property setters of class square
        """
        rect = Square(10)
        self.assertEqual(rect.width, 10)
        rect.width = 30
        rect.x = 5
        rect.y = 10
        self.assertEqual(rect.width, 30)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 10)
