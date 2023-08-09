#!/usr/bin/python3
j = 0
for i in range(122, 96, -1):
    j += 1
    if j % 2 == 1:
        print(chr(i), end="")
    else:
        print(chr(i - 32), end="")
