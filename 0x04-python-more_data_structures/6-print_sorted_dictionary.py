#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None and len(a_dictionary) > 0:
        keys = a_dictionary.keys()
        for key in sorted(keys):
            print("{} : {}".format(key, a_dictionary[key]))
