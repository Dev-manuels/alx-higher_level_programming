#!/usr/bin/python3
"""
Module add_integer
"""


def add_integer(a=None, b=98):
    """function that adds two int

    Args:
        a (int): int a
        b (int, optional): int b. Defaults to 98.

    Raises:
        TypeError: If a or b is not an integer or a float.

    Returns:
        int: a + b
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        result = a + b
        if result == -float('inf') or result == float('inf'):
            return float('inf')
        return (int(a) + int(b))
