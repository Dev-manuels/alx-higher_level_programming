#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last = int(str(number)[-1])
else:
    last = -int(str(number)[-1])
print(f"Last digit of {str(number)} is {str(last)} ", end="")
if last > 5:
    print("and is greater than 5")
elif last == 0:
    print("and is 0")
elif last < 6 and last != 0:
    print("and is less than 6 and not 0")
