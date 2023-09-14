#!/usr/bin/python3
"""
Module containing Class Rectangle that inherits from
Class BaseGeometry in module "7-base_geometry.py"
"""
import importlib

# Specify the module name and importing it using importlib
module_name = '7-base_geometry'
module = importlib.import_module(module_name)

# Access the class from the module
BaseGeometry = module.BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle
    inherits from class BaseGeometry

    Args:
        BaseGeometry (class): Base class for class Rectangle
    """
    def __init__(self, width, height):
        integer_validator("width", width)
        self.__width = width
        integer_validator("height", height)
        self.__height = height
