#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) != 0:
        sqr = []
        for row in matrix:
            tmp = []
            for item in row:
                tmp.append(item**2)
            sqr.append(tmp)
        return sqr
