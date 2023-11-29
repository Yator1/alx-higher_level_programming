#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number) % 10
if number < 0:
    num = -num
num_str = str(num)
if int(num) > 5:
    print(f"Last digit of {number} is {num_str} and is greater than 5")
elif int(num) == 0:
    print(f"Last digit of {number} is {num_str} and is 0")
elif int(num) < 6 and int(num) != 0:
    print(f"Last digit of {number} is {num_str} and is less "
          f"than 6 and not 0")
