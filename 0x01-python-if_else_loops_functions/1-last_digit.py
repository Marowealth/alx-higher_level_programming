#!/usr/bin/python3
import random

#Last digit
number = random.randint(-10000, 10000)
a = str(number)
last_digit =int(a[-1])
if last_digit > 5:
    print(f'Last digit of {number} is {last_digit} and is greater than 5')
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
elif last_digit==0:
    print(f"Last digit of {number} is {last_digit} and is 0")
