#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(f"{my_list[i]}", end=" ")
        print()
        return (i)
    except IndexError:
        count = 0
        for i in my_list:
            print(f"{i}", end=" ")
            count += 1
        print()
        return (count)
