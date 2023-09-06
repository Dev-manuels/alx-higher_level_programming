#!/usr/bin/python3
"""
Module containing print_square
"""


def print_square(size=None):
    """print_square _summary_

    Args:
        size (int): Size of square.
        Defaults to None and prints nothing.

    Raises:
        TypeError: If size is not an integer
        ValueError: when size is less than zero
    """
    if not isinstance(size, int) or size is None:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for _ in range(size):
            for _ in range(size):
                print("#", end="")
            print()
