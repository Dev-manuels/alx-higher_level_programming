#!/usr/bin/python3
"""
Module function that returns the JSON
representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """to_json_string
    returns the JSON representation of an object

    Args:
        my_obj (object): object to be converted to JSON

    Returns:
        JSON: JSON representation object
    """
    return (json.dumps(my_obj))
