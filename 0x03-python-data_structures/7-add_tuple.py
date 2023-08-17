#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is not None and tuple_b is not None:
        a = 0
        b = 0
        if len(tuple_a) >= 1:
            a += tuple_a[0]
        if len(tuple_b) >= 1:
            a += tuple_b[0]
        if len(tuple_a) >= 2:
            b += tuple_a[1]
        if len(tuple_b) >= 2:
            b += tuple_b[1]
        return (a, b)
