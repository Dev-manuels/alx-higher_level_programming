#!/usr/bin/python3
"""
module containing class Student
"""


class Student:
    """
    Class student
    """
    def __init__(self, first_name, last_name, age):
        """__init__ Class constructor

        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to_json
        retrieves a dictionary representation of a Student instance

        Returns:
            dictionary: dictionary representation of self
        """
        return self.__dict__
