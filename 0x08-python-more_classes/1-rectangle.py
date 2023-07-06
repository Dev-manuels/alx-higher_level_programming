#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """
    Represents a rectangle with width and height.

    Attributes:
        width (int): the width of the rectangle
        height (int): the height of the rectangle

    Methods:
        width: Getter to retrive the width of the rectangle
        width (value): Setter to set the width of the rectangle
        height: Getter to retreive the height of the rectangle
        height (value): Setter to set the height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
