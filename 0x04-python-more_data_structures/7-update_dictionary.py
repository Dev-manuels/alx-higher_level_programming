#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None and len(a_dictionary) > 0:
        a_dictionary.update({key: value})
    return a_dictionary
