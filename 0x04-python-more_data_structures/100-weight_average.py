#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) > 0:
        sum = 0
        sum_w = 0
        for item in my_list:
            sum += (item[0] * item[1])
            sum_w += item[1]
        return (sum/sum_w)
    return 0
