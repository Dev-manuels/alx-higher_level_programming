#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is not None and len(a_dictionary) > 0:
        keys = []
        for key, val in a_dictionary.items():
            if val == value:
                keys.append(key)
        for key in keys:
            del (a_dictionary[key])
        return a_dictionary
