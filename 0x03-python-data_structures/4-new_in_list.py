#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new_list = []
        i = 0
        for numb in my_list:
            if i == idx:
                i += 1
                new_list.append(element)
                continue
            else:
                new_list.append(numb)
            i += 1
        return new_list
