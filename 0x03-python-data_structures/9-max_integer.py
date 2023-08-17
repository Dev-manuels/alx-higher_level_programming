#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0:
        large = -5
        for number in my_list:
            if number >= large:
                large = number
        return large
    return None
