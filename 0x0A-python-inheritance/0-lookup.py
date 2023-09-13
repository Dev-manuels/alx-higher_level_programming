#!/usr/bin/python3
"""
Module containing function lookup
"""


def lookup(obj):
    """lookup _summary_

    Args:
        obj

    Returns:
        list: list of available attributes and methods of obj
    """
    new_list = []
    for attr in dir(obj):
        if not callable(getattr(obj, attr)) or attr.startswith("__"):
            new_list.append(attr)

    return new_list
