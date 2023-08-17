#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        keys = sorted(a_dictionary)
        for key in keys:
            print(key, ":", a_dictionary[key])
