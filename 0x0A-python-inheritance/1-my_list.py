#!/usr/bin/python3
"""
Module containing MyList class which inherits from list
"""


class MyList(list):
    """MyList inherits from list
    adds method print_sorted

    Args:
        list (Class): BaseClass of MyList
    """

    def print_sorted(self):
        """
        print_sorted MyList object
        """
        new_list = self.copy()
        new_list.sort()
        print(new_list)
