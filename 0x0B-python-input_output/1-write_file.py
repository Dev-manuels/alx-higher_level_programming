#!/usr/bin/python3
"""
Module containing a function that writes to a file
"""


def write_file(filename="", text=""):
    """write_file writes text to a file

    Args:
        filename (str): file path/ file name. Defaults to "".
        text (str): text to write to file. Defaults to "".
    """
    if len(filename) > 1 and len(text) > 1:
        with open(filename, mode="w", encoding="utf-8") as file:
            count = file.write(text)
            return count
