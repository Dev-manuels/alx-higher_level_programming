#!/usr/bin/python3
"""
module containing a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer
and boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """class_to_json returns the dictionary description of an object

    Args:
        obj (object): object to be viewed

    Returns:
        dict: dictionary of the attributed of obj
    """
    return obj.__dict__
