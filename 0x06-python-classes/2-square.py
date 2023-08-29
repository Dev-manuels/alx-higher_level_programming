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
        if isinstance(int, size):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
