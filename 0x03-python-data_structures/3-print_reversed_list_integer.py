#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None and len(my_list) > 0:
        for int in reversed(my_list):
            print("{:d}".format(int))
