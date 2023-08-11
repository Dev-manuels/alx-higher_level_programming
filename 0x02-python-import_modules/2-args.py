#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("{} argument:".format(len(sys.argv)))
    elif len(sys.argv) == 0:
        print("{} arguments.".format(len(sys.argv))) 
    else:
        print("{} arguments:".format(len(sys.argv)))
    i = 1
    for arg in sys.argv:
        print("{}: {}".format(i, arg))
        i += 1
