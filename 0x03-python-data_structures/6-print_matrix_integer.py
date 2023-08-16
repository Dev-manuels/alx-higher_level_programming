#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) > 0 and matrix is not None:
        for row in matrix:
            for column in row:
                if column != row[-1]:
                    print("{:d}".format(column), end=" ")
                else:
                    print("{:d}".format(column))
    else:
        print("")
