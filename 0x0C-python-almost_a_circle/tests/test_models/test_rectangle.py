"""
Module containing unittests for rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """TestRectangle
    Unittest for class rectangle

    Args:
        unittest (class): unittest
    """
    def test_rectangle_constructor(self):
        """test_rectangle_constructor
        test the Rectangle class constructor without id
        """
        rect = Rectangle(10, 20)
        self.assertIsInstance(rect, Rectangle)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 1)

    def test_rectangle_constructor_with_id(self):
        """test_rectangle_constructor_with_id
        tests the rectangle class with id
        """
        rect = Rectangle(10, 20, id=42)
        self.assertIsInstance(rect, Rectangle)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 42)

    def test_rectangle_setters(self):
        """test_rectangle_setters
        test property setters of class Rectangle
        """
        rect = Rectangle(10, 20)
        rect.width = 30
        rect.height = 40
        rect.x = 5
        rect.y = 10
        self.assertEqual(rect.width, 30)
        self.assertEqual(rect.height, 40)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 10)


if __name__ == '__main__':
    unittest.main()
