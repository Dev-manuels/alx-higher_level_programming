#!/usr/bin/python3
"""Module containing class rectangle"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        tmp = ""
        if self.width <= 0 or self.height <= 0:
            return tmp
        else:
            for i in range(0, self.height):
                for _ in range(self.width):
                    tmp += '#'
                if i != self.height - 1:
                    tmp += '\n'
            return tmp

    def __repr__(self):
        """Return a string representation of the object."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """__del__ delete rectangle object
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
