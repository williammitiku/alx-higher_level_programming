#!/usr/bin/python3
for Digit1 in range(0, 9):
    for Digit2 in range(Digit1 + 1, 10):
        if Digit1 == 8 and Digit2 == 9:
            print("{}{}".format(Digit1, Digit2))
        else:
            print("{}{}".format(Digit1, Digit2), end=", ")
