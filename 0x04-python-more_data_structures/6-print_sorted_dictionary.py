#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        keys = a_dictionary.keys()
        for key in sorted(keys):
            print(key, ":", a_dictionary[key])
