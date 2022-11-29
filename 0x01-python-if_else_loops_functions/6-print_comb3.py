#!/usr/bin/python3
for i in range(0, 8):
    for y in range(i + 1, 10):
        print("{}{}, ".format(i, y), end="")
print("{}{}".format(i + 1, y))
