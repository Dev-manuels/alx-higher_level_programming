#!/usr/bin/python3
"""
Module containing print_square
"""


def print_square(size):
    """print_square prints a square to screen

    Args:
        size (int): size length of the square

    Raises:
        TypeError: If size is not an integer
        ValueError: when size is less than zero
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        if size == 0:
            print()
        else:
            for _ in range(size):
                for _ in range(size):
                    print("#", end="")
                print()
