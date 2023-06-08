#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numb = len(sys.argv) - 1
    i = 0
    total = 0
    if numb >= 1:
        for arg in sys.argv:
            if i == 0:
                i += 1
                continue
            total += int(arg)
            i += 1
    print(f"{total}")
