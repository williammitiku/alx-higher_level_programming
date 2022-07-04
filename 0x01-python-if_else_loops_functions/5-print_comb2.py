#!/usr/bin/python3
endLine = ", "
for i in range(0, 100):
    if i < 10:
        print("{}{}".format(0, i), end=endLine)
    else:
        if i == 99:
            endLine = "\n"
        print(i, end=endLine)
