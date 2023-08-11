#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv)
    argc -= 1
    if argc == 1:
        print("{} argument:".format(argc))
    elif argc == 0:
        print("{} arguments.".format(argc))
    else:
        print("{} arguments:".format(argc))
    i = 0
    for arg in sys.argv:
        if i != 0:
            print("{}: {}".format(i, arg))
        i += 1
