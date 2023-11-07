#!/usr/bin/python3
"""
Module containing a function that returns an object
(Python data structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """from_json_string
    returns  (Python data structure) represented by a JSON string

    Args:
        my_str (JSON string): JSON string to be converted to python object

    Returns:
        python object: decoded JSON string
    """
    return json.loads(my_str)
