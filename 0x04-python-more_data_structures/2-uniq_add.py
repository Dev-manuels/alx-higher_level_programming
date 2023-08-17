#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) >= 0:
        uniq = set(my_list)
        sum = 0
        for item in uniq:
            sum += item
        return sum
