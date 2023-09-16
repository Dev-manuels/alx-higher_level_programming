#!/usr/bin/python3
"""
Module containing class student (based on 9-student.py)
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

    def to_json(self, attrs=None):
        """to_json
        retrieves a dictionary representation of a Student instance

        Args:
            attrs (list, optional): list of attribute to retrive
            from the object. Defaults to None.

        Returns:
            dictionary: dictionary representation of self
        """
        if attrs is not None:
            new_dict = dict()
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict.update({key: value})
            return new_dict
        return self.__dict__

    def reload_from_json(self, json=None):
        """reload_from_json
        replaces all attributes of a Student instance

        Args:
            json (dict): dictionary containing new attibutes. Defaults to None.
        """
        if json is not None:
            for key, value in json.items():
                self.__dict__.update({key: value})
