"""
Module containing unittests for Square class
"""
import io
import unittest
from models.square import Square
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    """TestSquare
    Test case class for Square

    Args:
        unittest (Class): Unittest
    """

    def test_square_constructor(self):
        """test_square_constructor
        tests that the Square class basic constructor works
        """
        sqr = Square(10)
        self.assertEqual(sqr.height, 10)
        self.assertEqual(sqr.width, 10)
        self.assertEqual(sqr.x, 0)
        self.assertEqual(sqr.y, 0)

    def test_square_constructor_with_id(self):
        """test_square_constructor_with_id
        Test that the full args passed to the constructor are functional
        """
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
