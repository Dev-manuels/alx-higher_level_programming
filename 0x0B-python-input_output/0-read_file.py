#!/usr/bin/python3
"""
Module containing function read_file that reads a text file(UTF8)
and prints its content to stdout
"""


def read_file(filename=""):
    """read_file reads and prints the content of a file

    Args:
        filename (str): filepath/name. Defaults to ""
    """
    if len(filename) > 1:
        with open(filename, encoding="utf-8") as file:
            for line in file:
                print(line)
