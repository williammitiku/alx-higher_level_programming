#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    dig = -number % 10
    dig = -dig
else:
    dig = number % 10
if dig > 5:
    print("Last digit of {} is {} and is greater \
than 5".format(number, dig))
elif dig < 6 and dig != 0:
    print("Last digit of {} is {} and is less than \
6 and not 0".format(number, dig))
elif dig == 0:
    print("Last digit of {} is {} and is 0".format(number, dig))
