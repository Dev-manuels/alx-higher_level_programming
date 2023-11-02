#!/usr/bin/python3
"""
Module for matrix_divided
"""


def matrix_divided(matrix=None, numb=None):
    """matrix_divided divides a matrix by div

    Args:
        matrix (list): list of list with values to be divided
            Defailts to None
        numb (int): divisor. Defaults to None

    Raises:
        TypeError: When matrix is not a list of list containing int/floats,
        When matrix is not a list, when matrix is not a list containing
        list of equal lengths
        ZeroDivisionError: when divisor is Zero

    Returns:
        list: new list with all elements divided by divisor
    """
    new_list = []
    """Validate matrix"""
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of "
            "integers/floats"
        )
    """Validate div"""
    if not isinstance(numb, (int, float)):
        raise TypeError(
            "div must be a number"
        )
    elif numb == 0:
        raise ZeroDivisionError("division by zero")
    """
    check that matrix is a list of list
    and containing floats or int
    """
    for row in matrix:
        if isinstance(row, list):
            if len(row) != len(matrix[0]):
                raise TypeError(
                    "Each row of the matrix must have the same size"
                )
            for item in row:
                if not isinstance(item, (int, float)):
                    raise TypeError(
                        "matrix must be a matrix (list of lists) of "
                        "integers/floats"
                    )
        else:
            raise TypeError(
                "matrix must be a matrix (list of lists) "
                "of integers/floats"
            )
    """perform matrix division"""
    for row in matrix:
        new_row = []
        for item in row:
            new_row.append(round((item / numb), 2))
        new_list.append(new_row)
    return new_list
