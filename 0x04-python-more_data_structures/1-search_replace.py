#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    if my_list != []:
        for numb in my_list:
            if numb == search:
                new_list.append(replace)
            else:
                new_list.append(numb)
    return (new_list)
