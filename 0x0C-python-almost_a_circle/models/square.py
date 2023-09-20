#!/usr/bin/python3
"""
Module containing Square class that inherites from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """__init__
        Constructor for class Square

        Args:
            size (int): size of square
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): id. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__
        String representation of Square object

        Returns:
            string: representation of Square object
        """
        return (f"[Square] ({self.id}) {self.__x}/{self.__x} "
                f"- {self.__height}")
