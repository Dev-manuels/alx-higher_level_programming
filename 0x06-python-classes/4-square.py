#!/usr/bin/python3
""" Module containing a Square Class """


class Square:
    """Simple Square class
    """

    def __init__(self, size=0):
        """Initialize Square object

        Args:
            __size (int): size of square object

        Raises:
            TypeError: "size must be an integer"
            ValueError: "size must be >= 0"
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

    @property
    def size(self):
        """Getter for __size

        Returns:
            int: self.__size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter for __size

        Args:
            value (int): new value for __size

        Raises:
            TypeError: "size must be an integer"
            ValueError: "size must be >= 0"
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif int(value) < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(value)
