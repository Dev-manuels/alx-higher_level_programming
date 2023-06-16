#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list != []:
        temp = set()
        sum = 0
        for numb in my_list:
            temp.add(numb)
        for numb in temp:
            sum += numb
        return sum
