#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) > 0:
        new_list = []
        for number in my_list:
            if int(number) % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)
        return new_list
    return None
