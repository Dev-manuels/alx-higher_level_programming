#!/usr/bin/python3
"""
Module add_integer
"""


def add_integer(a, b=98):
    """function that adds two int

    Args:
        a (int): int a
        b (int, optional): int b. Defaults to 98.

    Raises:
        TypeError: If a or b is not an integer or a float.

    Returns:
        int: a + b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
