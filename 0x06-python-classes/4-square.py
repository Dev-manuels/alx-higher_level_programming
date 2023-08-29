#!/usr/bin/python3
""" Module containing a Square Class """


class Square:
    """Simple Square class
    """

    def __init__(self, size=0):
        """Initialize Square object

        Args:
            __size (int): size of square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif int(size) < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        """Calculates the area of a Square object

        Returns:
            int: area of the Square object
        """
        return (self.__size * self.__size)

    def size(self):
        """Getter for __size

        Returns:
            int: self.__size
        """
        return (self.__size)

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif int(value) < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(value)
