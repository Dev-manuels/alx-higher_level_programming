#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        sorted_keys = sorted(a_dictionary.keys())
        for k in sorted_keys:
            v = a_dictionary[k]
            print("{}: {}".format(k, v))
