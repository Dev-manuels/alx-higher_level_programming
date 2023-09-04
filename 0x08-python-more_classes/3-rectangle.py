#!/usr/bin/python3
"""Module containing class rectangle"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter

        Args:
            value (int): New value for width

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter

        Args:
            value (int): New value for height

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """area reterive value of area

        Returns:
            int: value of area of object Rectangle
        """
        return (self.height * self.width)

    def perimeter(self):
        """perimeter of Rectangle

        Returns:
            int: value of perimeter of Rectangle object
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return ((self.width + self.height) * 2)

    def __str__(self):
        """__str__ string representation of Rectangle object

        Returns:
            string: string representation of rectangle object
        """
        str = ""
        if self.width == 0 or self.height == 0:
            return str
        else:
            for _ in range(self.height):
                for _ in range(self.width):
                    str += '#'
                str += '\n'
            return str
