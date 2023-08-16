#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) > 0:
        for int in rev(my_list):
            print("{:d}".format(int))
