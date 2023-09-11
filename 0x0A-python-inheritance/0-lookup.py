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
    return list(obj.__dict__())
