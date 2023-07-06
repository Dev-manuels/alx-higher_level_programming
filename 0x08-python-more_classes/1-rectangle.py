#!/usr/bin/python3
"""
Module rectangle class rectangle
"""


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
        self._width = width
        self._height = height

    @property
    def width(self):
        return (self._width)

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self._width = width

    @property
    def height(self):
        return (self._height)

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self._height = height
