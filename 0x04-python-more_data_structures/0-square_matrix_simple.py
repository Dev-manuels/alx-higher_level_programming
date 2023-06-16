#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix != []:
        new_matrix = []
        for row in matrix:
            new_row = []
            for numb in row:
                new_row.append(numb * numb)
            new_matrix.append(new_row)
        return (new_matrix)
