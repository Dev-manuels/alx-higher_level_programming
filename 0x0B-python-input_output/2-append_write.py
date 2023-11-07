#!/usr/bin/python3
"""
Module containing a function that appends text to a file
"""


def append_write(filename="", text=""):
    """append_write writes text to a file

    Args:
        filename (str): file path/ file name. Defaults to "".
        text (str): text to append to file. Defaults to "".
    """
    if len(filename) > 0 and len(text) > 0:
        with open(filename, mode="a", encoding="utf-8") as file:
            count = file.write(text)
            return count
