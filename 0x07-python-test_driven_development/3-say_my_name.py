#!/usr/bin/python3
"""
Module containing say_my_name
"""


def say_my_name(first_name=None, last_name=""):
    """say_my_name prints My name is <first name> <last name>

    Args:
        first_name (str): first name. Defaults to None
        last_name (str, optional): last name. Defaults to "".

    Raises:
        TypeError: If first or last name is not a string
    """
    if first_name is None:
        return None
    elif not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
