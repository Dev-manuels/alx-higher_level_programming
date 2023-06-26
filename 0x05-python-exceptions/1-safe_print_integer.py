#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        pass
    finally:
        return (isinstance(value, int))
