#!/usr/bin/python3
"""
Module Containing Class BaseGeometry
"""


class BaseGeometry:
    """
    Class BaseGeometry
    """
    def area(self):
        """area

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator

        check that value is of type int and greter than 0
        Args:
            name (string): name of value
            value (int): value

        Raises:
            TypeError: when value is not of type int
            ValueError: when value is less than 1
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if 0 >= value:
            raise ValueError(f"{name} must be greater than 0")
