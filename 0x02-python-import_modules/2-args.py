#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numb = len(sys.argv) - 1
    i = 0
    if numb == 1:
        print(f"{numb} argument:")
    elif numb > 1:
        print(f"{numb} arguments:")
    else:
        print(f"{numb} arguments.")
    if numb != 0:
        for arg in sys.argv:
            if i == 0:
                i += 1
                continue
            print(f"{i}: {arg}")
            i += 1
