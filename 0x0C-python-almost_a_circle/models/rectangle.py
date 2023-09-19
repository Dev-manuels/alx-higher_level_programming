#!/usr/bin/python3
"""
Module containing class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle
    Class rectangle, inherits from class Base

    Args:
        Base (class): Parent class

    Returns:
        object: rectangle object
    """
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def area(self):
        return (self.__height * self.__width)

    @width.setter
    def width(self, width):
        """width
        sets value of width

        Args:
            width (int): new value for width

        Raises:
            TypeError: when width is not a integer
            ValueError: when width is less or equal to 0
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 1:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        """height
        sets value of height

        Args:
            height (int): new value for height

        Raises:
            TypeError: when height is not a integer
            ValueError: when height is less or equal to 0
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 1:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @x.setter
    def x(self, x):
        """x
        sets the value of x

        Args:
            x (int): new value for x

        Raises:
            TypeError: when x is not a integer
            ValueError: when x is less than 0
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        """y
        sets the value of y

        Args:
            y (int): new value for y

        Raises:
            TypeError: when y is not a integer
            ValueError: when y is less than 0
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
