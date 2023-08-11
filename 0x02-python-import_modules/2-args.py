#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = 0
    argc -= 1
    if argc == 1:
        print("{} argument:".format(argc))
    elif argc == 0:
        print("{} arguments.".format(argc))
    else:
        print("{} arguments:".format(argc))
    i = 1
    for arg in sys.argv:
        print("{}: {}".format(i, arg))
        i += 1
