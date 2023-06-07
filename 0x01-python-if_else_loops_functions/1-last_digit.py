#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
outnumb = abs(number) % 10
if number < 0:
    outnumb = (abs(number) % 10) * -1
print(f"Last digit of {number} is {outnumb}", end="")
if outnumb > 5:
    print(f" and is greater than 5")
elif outnumb < 6 and outnumb != 0:
    print(f" and is less than 6 and not 0")
else:
    print(f" and is 0")
