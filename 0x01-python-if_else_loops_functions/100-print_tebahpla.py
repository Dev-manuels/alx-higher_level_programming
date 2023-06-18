#!/usr/bin/python3
for i in reversed(range(ord('a'), ord('z')+1)):
    j = 0
    if i % 2 == 0:
        j = i
    else:
        j = i - 32
    print("{}".format(chr(j)), end="")
